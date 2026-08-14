from __future__ import annotations

import json
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any, Literal

import numpy as np
from pydantic import BaseModel, ConfigDict, Field

from bottrade.config import AppConfig
from bottrade.domain import Asset, DataArm, ModelFamily, RunStage
from bottrade.models.preprocessing import RobustStandardizer
from bottrade.utils import deterministic_id, sha256_file, utc_now


class ModelMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", allow_inf_nan=False)

    version: str
    asset: Asset
    family: ModelFamily
    data_arm: DataArm
    stage: RunStage = RunStage.DEVELOPMENT
    trained_at: datetime
    training_end: datetime
    horizon_hours: int
    sequence_length: int
    feature_names: list[str]
    feature_schema_version: str
    data_version: str
    threshold_return: float
    seed: int
    parameters: dict[str, Any]
    protocol_phase: Literal["development", "holdout", "refit"] = "development"
    protocol_eligible: bool = False
    selection_id: str = ""
    selection_role: str = ""
    parent_version: str = ""
    selection_metrics: dict[str, float | int] = Field(default_factory=dict)
    selection_stress_metrics: dict[str, float | int] = Field(default_factory=dict)
    holdout_metrics: dict[str, float | int] = Field(default_factory=dict)
    stress_metrics: dict[str, float | int] = Field(default_factory=dict)
    benchmark_metrics: dict[str, dict[str, float | int]] = Field(default_factory=dict)
    predictive_metrics: dict[str, float | int] = Field(default_factory=dict)
    regime_metrics: dict[str, dict[str, Any]] = Field(default_factory=dict)
    operational_metrics: dict[str, float | int | str] = Field(default_factory=dict)
    source_control: dict[str, str | bool] = Field(default_factory=dict)
    explainability_complete: bool = False
    onnx_verified: bool
    onnx_max_abs_error: float
    artifact_sha256: str = ""
    bundle_hashes: dict[str, str] = Field(default_factory=dict)
    canary_started_at: datetime | None = None
    canary_passed_at: datetime | None = None


class OnnxPredictor:
    def __init__(self, bundle_path: Path, metadata: ModelMetadata) -> None:
        try:
            import onnxruntime as ort
        except ImportError as exc:
            raise RuntimeError("onnxruntime is required for paper inference") from exc
        self.bundle_path = bundle_path
        self.metadata = metadata
        self.session = ort.InferenceSession(
            str(bundle_path / "model.onnx"), providers=["CPUExecutionProvider"]
        )
        self.standardizer: RobustStandardizer | None = None
        preprocessor_path = bundle_path / "preprocessor.json"
        if preprocessor_path.exists():
            self.standardizer = RobustStandardizer.read(preprocessor_path)

    def predict_latest(self, feature_values: np.ndarray) -> float:
        expected_features = len(self.metadata.feature_names)
        if feature_values.ndim != 2 or feature_values.shape[1] != expected_features:
            raise ValueError(
                f"expected [time,{expected_features}] features, got {feature_values.shape}"
            )
        if self.metadata.family == ModelFamily.TRANSFORMER:
            if len(feature_values) < self.metadata.sequence_length:
                raise ValueError("insufficient Transformer lookback")
            if self.standardizer is None:
                raise RuntimeError("Transformer bundle is missing preprocessor.json")
            transformed = self.standardizer.transform(feature_values)
            sequence = transformed[-self.metadata.sequence_length :][None, :, :]
            result = self.session.run(None, {"sequence": sequence.astype(np.float32)})[0]
        else:
            row = feature_values[-1:].astype(np.float32)
            result = self.session.run(None, {"features": row})[0]
        return float(np.asarray(result).reshape(-1)[0])


class ModelRegistry:
    ALLOWED_SLOTS = {"champion", "challenger", "market_fallback"}
    VERSION_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,199}")

    def __init__(self, config: AppConfig) -> None:
        self.config = config
        self.root = config.project.artifact_dir / "registry"

    def _slot(self, asset: Asset, slot: str) -> Path:
        return self.root / asset.value / slot

    @classmethod
    def _validate_slot(cls, slot: str) -> None:
        if slot not in cls.ALLOWED_SLOTS:
            raise ValueError(f"invalid model registry slot: {slot}")

    def _version_directory(self, asset: Asset, version: str) -> Path:
        if not self.VERSION_PATTERN.fullmatch(version):
            raise ValueError(f"invalid model version identifier: {version!r}")
        versions_root = self._slot(asset, "versions").resolve()
        destination = (versions_root / version).resolve()
        if destination.parent != versions_root:
            raise ValueError("model version escaped the registry root")
        return destination

    def register(self, source_directory: Path, metadata: ModelMetadata) -> Path:
        model_path = source_directory / "model.onnx"
        if not model_path.exists():
            raise FileNotFoundError(model_path)
        if not metadata.onnx_verified:
            raise ValueError("unverified ONNX artifacts cannot be registered")
        destination = self._version_directory(metadata.asset, metadata.version)
        if destination.exists():
            existing = self.load_metadata(destination)
            if existing.artifact_sha256 != sha256_file(model_path):
                raise FileExistsError(f"version already exists with different content: {destination}")
            return destination
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary = destination.with_name(destination.name + ".tmp")
        if temporary.exists():
            shutil.rmtree(temporary)
        shutil.copytree(source_directory, temporary)
        metadata.artifact_sha256 = sha256_file(temporary / "model.onnx")
        runtime_files = ["model.onnx"]
        if (temporary / "preprocessor.json").exists():
            runtime_files.append("preprocessor.json")
        metadata.bundle_hashes = {
            name: sha256_file(temporary / name) for name in runtime_files
        }
        self._write_metadata(temporary, metadata)
        temporary.replace(destination)
        return destination

    def _write_metadata(self, directory: Path, metadata: ModelMetadata) -> None:
        path = directory / "metadata.json"
        temporary = path.with_suffix(".json.tmp")
        temporary.write_text(
            json.dumps(metadata.model_dump(mode="json"), indent=2, sort_keys=True),
            encoding="utf-8",
        )
        temporary.replace(path)

    @staticmethod
    def load_metadata(directory: Path) -> ModelMetadata:
        return ModelMetadata.model_validate_json((directory / "metadata.json").read_text("utf-8"))

    @staticmethod
    def _validate_bundle(directory: Path, metadata: ModelMetadata) -> None:
        expected_hashes = metadata.bundle_hashes or {
            "model.onnx": metadata.artifact_sha256
        }
        for relative, expected in expected_hashes.items():
            path = (directory / relative).resolve()
            if not path.is_relative_to(directory.resolve()) or not path.is_file():
                raise ValueError(f"registered model bundle file is invalid: {relative}")
            if sha256_file(path) != expected:
                raise ValueError(f"registered model checksum mismatch: {relative}")

    def load_version(self, asset: Asset, version: str) -> tuple[Path, ModelMetadata]:
        directory = self._version_directory(asset, version)
        metadata = self.load_metadata(directory)
        self._validate_bundle(directory, metadata)
        return directory, metadata

    def offline_gate_reasons(self, metadata: ModelMetadata) -> list[str]:
        gates = self.config.gates
        metrics = metadata.holdout_metrics
        stress = metadata.stress_metrics
        reasons: list[str] = []
        if metadata.protocol_phase not in {"holdout", "refit"}:
            reasons.append("holdout_not_opened")
        if not metadata.protocol_eligible:
            reasons.append("reduced_or_non_protocol_run")
        if not metadata.selection_id:
            reasons.append("missing_pre_holdout_selection_lock")
        if not metadata.explainability_complete:
            reasons.append("explainability_incomplete")
        if float(metrics.get("sharpe", 0)) < gates.min_sharpe:
            reasons.append("sharpe_below_gate")
        if float(metrics.get("max_drawdown", 1)) > gates.max_drawdown:
            reasons.append("drawdown_above_gate")
        if float(metrics.get("profit_factor", 0)) < gates.min_profit_factor:
            reasons.append("profit_factor_below_gate")
        if int(metrics.get("closed_trades", 0)) < gates.min_closed_trades:
            reasons.append("insufficient_trades")
        if gates.require_positive_stress_return and float(stress.get("total_return", -1)) <= 0:
            reasons.append("negative_stress_return")
        baseline_sortinos = [
            float(value.get("sortino", 0)) for value in metadata.benchmark_metrics.values()
        ]
        if baseline_sortinos and float(metrics.get("sortino", 0)) <= max(baseline_sortinos):
            reasons.append("did_not_beat_benchmark")
        if not metadata.onnx_verified:
            reasons.append("onnx_not_verified")
        return reasons

    def _holdout_lineage_root(self, metadata: ModelMetadata) -> str:
        seen: set[str] = set()
        current = metadata
        while current.protocol_phase == "refit":
            if not current.parent_version or current.parent_version in seen:
                raise ValueError("invalid or cyclic refit lineage")
            seen.add(current.parent_version)
            parent_dir = self._version_directory(current.asset, current.parent_version)
            current = self.load_metadata(parent_dir)
            if current.selection_id != metadata.selection_id:
                raise ValueError("refit lineage changed selection lock")
        if current.protocol_phase != "holdout":
            raise ValueError("refit lineage does not end in a holdout artifact")
        return current.version

    def promote(
        self,
        *,
        asset: Asset,
        version: str,
        slot: Literal["champion", "challenger", "market_fallback"],
        stage: RunStage = RunStage.CANARY,
    ) -> Path:
        self._validate_slot(slot)
        version_dir = self._version_directory(asset, version)
        metadata = self.load_metadata(version_dir)
        self._validate_bundle(version_dir, metadata)
        if metadata.asset != asset:
            raise ValueError("model asset does not match promotion target")
        if stage in {RunStage.CANARY, RunStage.PAPER}:
            reasons = self.offline_gate_reasons(metadata)
            if reasons:
                raise ValueError(f"model failed offline promotion gates: {', '.join(reasons)}")
            from bottrade.selection import SelectionManager

            lock = SelectionManager(self.config).load(asset)
            if metadata.selection_id != lock.selection_id:
                raise ValueError("model does not belong to the active pre-holdout selection lock")
            lineage_root = self._holdout_lineage_root(metadata)
            if lock.holdout_versions.get(slot) != lineage_root:
                raise ValueError(f"version is not in the frozen holdout lineage for {slot}")
            if metadata.protocol_phase == "refit" and metadata.selection_role != slot:
                raise ValueError("refit role differs from the target registry slot")
        if (
            stage == RunStage.PAPER
            and metadata.canary_passed_at is None
            and metadata.protocol_phase != "refit"
        ):
            raise ValueError("paper promotion requires a completed canary")
        if slot == "market_fallback" and metadata.data_arm != DataArm.MARKET:
            raise ValueError("market_fallback must use the market-only arm")
        metadata.stage = stage
        if stage == RunStage.CANARY and metadata.canary_started_at is None:
            metadata.canary_started_at = utc_now()
        self._write_metadata(version_dir, metadata)
        pointer = {
            "asset": asset.value,
            "slot": slot,
            "version": version,
            "stage": stage.value,
            "updated_at": utc_now().isoformat(),
            "pointer_id": deterministic_id(asset.value, slot, version, stage.value),
        }
        pointer_path = self._slot(asset, f"{slot}.json")
        pointer_path.parent.mkdir(parents=True, exist_ok=True)
        temporary = pointer_path.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(pointer, indent=2, sort_keys=True), encoding="utf-8")
        temporary.replace(pointer_path)
        return pointer_path

    def mark_canary_passed(self, asset: Asset, version: str) -> None:
        directory = self._version_directory(asset, version)
        metadata = self.load_metadata(directory)
        metadata.canary_passed_at = utc_now()
        self._write_metadata(directory, metadata)

    def resolve(self, asset: Asset, slot: str = "champion") -> tuple[Path, ModelMetadata]:
        self._validate_slot(slot)
        pointer_path = self._slot(asset, f"{slot}.json")
        if not pointer_path.exists():
            raise FileNotFoundError(f"no {slot} pointer for {asset.value}")
        pointer = json.loads(pointer_path.read_text(encoding="utf-8"))
        directory = self._version_directory(asset, str(pointer["version"]))
        metadata = self.load_metadata(directory)
        self._validate_bundle(directory, metadata)
        return directory, metadata

    def predictor(self, asset: Asset, slot: str = "champion") -> OnnxPredictor:
        directory, metadata = self.resolve(asset, slot)
        return OnnxPredictor(directory, metadata)

    def upload_version(self, asset: Asset, version: str) -> str:
        bucket_name = self.config.runtime.model_bucket
        if not bucket_name:
            raise ValueError("runtime.model_bucket is not configured")
        try:
            from google.cloud import storage
        except ImportError as exc:
            raise RuntimeError("install the 'cloud' extra to upload model artifacts") from exc
        directory = self._version_directory(asset, version)
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        prefix = f"{self.config.runtime.model_prefix}/{asset.value}/versions/{version}"
        for path in directory.rglob("*"):
            if path.is_file():
                relative = path.relative_to(directory).as_posix()
                bucket.blob(f"{prefix}/{relative}").upload_from_filename(path)
        return f"gs://{bucket_name}/{prefix}"

    def publish_active(self, asset: Asset, slot: str = "champion") -> str:
        self._validate_slot(slot)
        bucket_name = self.config.runtime.model_bucket
        if not bucket_name:
            raise ValueError("runtime.model_bucket is not configured")
        try:
            from google.cloud import storage
        except ImportError as exc:
            raise RuntimeError("install the 'cloud' extra to publish model artifacts") from exc
        pointer_path = self._slot(asset, f"{slot}.json")
        _, metadata = self.resolve(asset, slot)
        self.upload_version(asset, metadata.version)
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        pointer_blob = (
            f"{self.config.runtime.model_prefix}/{asset.value}/{slot}.json"
        )
        bucket.blob(pointer_blob).upload_from_filename(pointer_path)
        return f"gs://{bucket_name}/{pointer_blob}"

    def hydrate_active(self, asset: Asset, slot: str = "champion") -> Path:
        self._validate_slot(slot)
        bucket_name = self.config.runtime.model_bucket
        if not bucket_name:
            return self.resolve(asset, slot)[0]
        try:
            from google.cloud import storage
        except ImportError as exc:
            raise RuntimeError("install the 'cloud' extra to download model artifacts") from exc
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        base = f"{self.config.runtime.model_prefix}/{asset.value}"
        pointer_path = self._slot(asset, f"{slot}.json")
        pointer_path.parent.mkdir(parents=True, exist_ok=True)
        pointer_blob = bucket.blob(f"{base}/{slot}.json")
        if not pointer_blob.exists():
            raise FileNotFoundError(f"no cloud pointer for {asset.value}/{slot}")
        pointer_blob.download_to_filename(pointer_path)
        pointer = json.loads(pointer_path.read_text(encoding="utf-8"))
        version = pointer["version"]
        destination = self._version_directory(asset, str(version))
        destination.mkdir(parents=True, exist_ok=True)
        blobs = list(bucket.list_blobs(prefix=f"{base}/versions/{version}/"))
        if not blobs:
            raise FileNotFoundError(f"no cloud model bundle for {asset.value}/{version}")
        prefix = f"{base}/versions/{version}/"
        for blob in blobs:
            relative = blob.name.removeprefix(prefix)
            if not relative:
                continue
            target = (destination / relative).resolve()
            if not target.is_relative_to(destination.resolve()):
                raise ValueError(f"cloud model object escaped bundle root: {blob.name}")
            target.parent.mkdir(parents=True, exist_ok=True)
            blob.download_to_filename(target)
        self.resolve(asset, slot)
        return destination
