from __future__ import annotations

import json
import math
from datetime import datetime
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field

from bottrade.config import AppConfig
from bottrade.domain import Asset, DataArm, ModelFamily
from bottrade.utils import content_hash, sha256_file, utc_now


class SelectionLock(BaseModel):
    model_config = ConfigDict(extra="forbid")

    protocol_version: str = "v1"
    selection_id: str
    asset: Asset
    status: Literal["selected", "cash"]
    created_at: datetime
    holdout_start: str
    holdout_end: str
    required_candidates: list[str]
    candidates: list[dict[str, Any]] = Field(default_factory=list)
    roles: dict[str, dict[str, Any]] = Field(default_factory=dict)
    chosen_run_id: str = ""
    chosen_version: str = ""
    family: ModelFamily | None = None
    data_arm: DataArm | None = None
    parameters: dict[str, Any] = Field(default_factory=dict)
    data_version: str = ""
    feature_schema_version: str = ""
    experiment_path: str = ""
    experiment_sha256: str = ""
    holdout_opened_at: dict[str, datetime] = Field(default_factory=dict)
    holdout_completed_at: dict[str, datetime] = Field(default_factory=dict)
    holdout_versions: dict[str, str] = Field(default_factory=dict)


class SelectionManager:
    def __init__(self, config: AppConfig) -> None:
        self.config = config
        self.root = config.project.artifact_dir / "selections"

    def path(self, asset: Asset) -> Path:
        return self.root / f"{asset.value}.json"

    def load(self, asset: Asset) -> SelectionLock:
        path = self.path(asset)
        if not path.exists():
            raise FileNotFoundError(f"selection lock is missing for {asset.value}")
        lock = SelectionLock.model_validate_json(path.read_text(encoding="utf-8"))
        expected_id = content_hash(
            [
                {
                    "asset": lock.asset.value,
                    "holdout": [lock.holdout_start, lock.holdout_end],
                    "candidates": lock.candidates,
                    "chosen_run_id": lock.chosen_run_id or "cash",
                    "roles": lock.roles,
                }
            ]
        )[:20]
        if lock.selection_id != expected_id:
            raise ValueError(f"selection lock integrity check failed: {path}")
        return lock

    def _write(self, lock: SelectionLock) -> Path:
        path = self.path(lock.asset)
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix(".json.tmp")
        temporary.write_text(
            json.dumps(lock.model_dump(mode="json"), indent=2, sort_keys=True),
            encoding="utf-8",
        )
        temporary.replace(path)
        return path

    def _records(self, asset: Asset) -> list[dict[str, Any]]:
        root = self.config.project.artifact_dir / "experiments" / asset.value
        records: list[dict[str, Any]] = []
        if not root.exists():
            return records
        for path in root.rglob("experiment.json"):
            record = json.loads(path.read_text(encoding="utf-8"))
            if (
                record.get("phase") == "development"
                and bool(record.get("protocol_eligible"))
                and record.get("asset") == asset.value
            ):
                record["experiment_path"] = str(path.resolve())
                record["experiment_sha256"] = sha256_file(path)
                records.append(record)
        return records

    def _gate_reasons(self, record: dict[str, Any]) -> list[str]:
        metrics = record.get("selection_metrics", {})
        reasons: list[str] = []
        source_control = record.get("source_control", {})
        if source_control.get("commit") in {None, "", "unavailable"}:
            reasons.append("source_commit_unavailable")
        if source_control.get("dirty") is not False:
            reasons.append("source_tree_not_clean")
        if not bool(record.get("explainability_complete")):
            reasons.append("explainability_incomplete")
        onnx_error = float(record.get("onnx_max_abs_error", math.inf))
        tolerance = float(record.get("onnx_tolerance", self.config.training.onnx_tolerance))
        if not math.isfinite(onnx_error) or onnx_error > tolerance:
            reasons.append("onnx_not_verified")
        for name in ("sortino", "sharpe", "max_drawdown", "total_return"):
            if not math.isfinite(float(metrics.get(name, math.nan))):
                reasons.append(f"invalid_{name}")
        return reasons

    def select(self, asset: Asset) -> SelectionLock:
        destination = self.path(asset)
        if destination.exists():
            raise FileExistsError(
                f"selection is immutable and already exists: {destination}; start a new protocol version"
            )
        required = [
            f"{family.value}:{DataArm(arm).value}"
            for family in (ModelFamily.RANDOM_FOREST, ModelFamily.TRANSFORMER)
            for arm in self.config.features.arms
        ]
        records = self._records(asset)
        by_key: dict[str, list[dict[str, Any]]] = {}
        for record in records:
            key = f"{record['family']}:{record['arm']}"
            by_key.setdefault(key, []).append(record)
        missing = [key for key in required if key not in by_key]
        if missing:
            raise ValueError(
                "cannot freeze selection before all eight protocol candidates exist: "
                + ", ".join(missing)
            )
        selected_records: dict[str, dict[str, Any]] = {}
        for family in (ModelFamily.RANDOM_FOREST, ModelFamily.TRANSFORMER):
            market_key = f"{family.value}:{DataArm.MARKET.value}"
            market_record = sorted(
                by_key[market_key],
                key=lambda item: str(item.get("created_at", item.get("version", ""))),
            )[-1]
            selected_records[market_key] = market_record
            for arm in self.config.features.arms:
                key = f"{family.value}:{DataArm(arm).value}"
                if key == market_key:
                    continue
                matching = [
                    item
                    for item in by_key[key]
                    if item.get("parameters") == market_record.get("parameters")
                ]
                if not matching:
                    raise ValueError(
                        f"{key} was not evaluated with the currently frozen {market_key} "
                        "parameters; rerun that ablation before selection"
                    )
                selected_records[key] = sorted(
                    matching,
                    key=lambda item: str(item.get("created_at", item.get("version", ""))),
                )[-1]
        candidates: list[dict[str, Any]] = []
        eligible: list[dict[str, Any]] = []
        for key in required:
            # Use the latest candidate tied to the same family-specific market search.
            record = selected_records[key]
            reasons = self._gate_reasons(record)
            summary = {
                "key": key,
                "run_id": record["run_id"],
                "version": record["version"],
                "selection_metrics": record["selection_metrics"],
                "selection_stress_metrics": record["selection_stress_metrics"],
                "median_fold_sortino": record.get("median_fold_sortino", -1_000_000.0),
                "gate_reasons": reasons,
                "experiment_path": record["experiment_path"],
                "experiment_sha256": record["experiment_sha256"],
            }
            candidates.append(summary)
            if not reasons:
                eligible.append(record)

        def rank_key(item: dict[str, Any]) -> tuple[float, float, float]:
            return (
                float(item.get("median_fold_sortino", -1_000_000.0)),
                -float(item["selection_metrics"].get("max_drawdown", 1.0)),
                float(item["selection_stress_metrics"].get("total_return", -1.0)),
            )
        chosen = max(
            eligible,
            key=rank_key,
            default=None,
        )
        fallback = max(
            [item for item in eligible if item["arm"] == DataArm.MARKET.value],
            key=rank_key,
            default=None,
        )
        challenger = max(
            [item for item in eligible if chosen is None or item["run_id"] != chosen["run_id"]],
            key=rank_key,
            default=None,
        )
        # An alternative-data champion is unsafe without a frozen market-only fallback.
        if chosen is not None and chosen["arm"] != DataArm.MARKET.value and fallback is None:
            chosen = None
            challenger = None

        def role_payload(record: dict[str, Any] | None) -> dict[str, Any]:
            if record is None:
                return {}
            return {
                "run_id": record["run_id"],
                "version": record["version"],
                "family": record["family"],
                "data_arm": record["arm"],
                "parameters": record["parameters"],
                "data_version": record["data_version"],
                "feature_schema_version": record["feature_schema_version"],
                "experiment_path": record["experiment_path"],
                "experiment_sha256": record["experiment_sha256"],
            }

        roles = {
            "champion": role_payload(chosen),
            "market_fallback": role_payload(fallback),
            "challenger": role_payload(challenger),
        }
        payload_for_id = {
            "asset": asset.value,
            "holdout": [self.config.training.holdout_start, self.config.training.holdout_end],
            "candidates": candidates,
            "chosen_run_id": chosen["run_id"] if chosen else "cash",
            "roles": roles,
        }
        lock = SelectionLock(
            selection_id=content_hash([payload_for_id])[:20],
            asset=asset,
            status="selected" if chosen else "cash",
            created_at=utc_now(),
            holdout_start=self.config.training.holdout_start,
            holdout_end=self.config.training.holdout_end,
            required_candidates=required,
            candidates=candidates,
            roles=roles,
            chosen_run_id=chosen["run_id"] if chosen else "",
            chosen_version=chosen["version"] if chosen else "",
            family=ModelFamily(chosen["family"]) if chosen else None,
            data_arm=DataArm(chosen["arm"]) if chosen else None,
            parameters=chosen["parameters"] if chosen else {},
            data_version=chosen["data_version"] if chosen else "",
            feature_schema_version=chosen["feature_schema_version"] if chosen else "",
            experiment_path=chosen["experiment_path"] if chosen else "",
            experiment_sha256=chosen["experiment_sha256"] if chosen else "",
        )
        self._write(lock)
        return lock

    def role(self, lock: SelectionLock, role: str) -> dict[str, Any]:
        if role not in {"champion", "market_fallback", "challenger"}:
            raise ValueError(f"invalid frozen role: {role}")
        record = lock.roles.get(role, {})
        if not record:
            raise ValueError(f"selection lock has no eligible {role}")
        return record

    def claim_holdout(
        self, asset: Asset, *, role: str = "champion", resume: bool = False
    ) -> SelectionLock:
        lock = self.load(asset)
        if lock.status != "selected":
            raise ValueError(f"{asset.value} has no eligible pre-holdout champion and remains cash")
        selected = self.role(lock, role)
        experiment = Path(selected["experiment_path"])
        if not experiment.exists() or sha256_file(experiment) != selected["experiment_sha256"]:
            raise ValueError("selected experiment changed after the selection lock")
        if role in lock.holdout_completed_at:
            raise ValueError(f"holdout was already completed for role {role}")
        if role in lock.holdout_opened_at and not resume:
            raise ValueError(
                "holdout access was already claimed; use --resume only to recover the same frozen run"
            )
        if role not in lock.holdout_opened_at:
            lock.holdout_opened_at[role] = utc_now()
            self._write(lock)
        return lock

    def complete_holdout(self, asset: Asset, role: str, version: str) -> SelectionLock:
        lock = self.load(asset)
        if role not in lock.holdout_opened_at:
            raise ValueError("holdout was not claimed")
        if role in lock.holdout_completed_at:
            if lock.holdout_versions.get(role) != version:
                raise ValueError("holdout already completed with a different artifact")
            return lock
        completed = utc_now()
        selected_run = self.role(lock, role)["run_id"]
        # One evaluation can satisfy multiple pre-frozen roles when they intentionally
        # reference the very same development candidate.
        for candidate_role, record in lock.roles.items():
            if record and record.get("run_id") == selected_run:
                lock.holdout_opened_at.setdefault(candidate_role, lock.holdout_opened_at[role])
                lock.holdout_completed_at[candidate_role] = completed
                lock.holdout_versions[candidate_role] = version
        self._write(lock)
        return lock
