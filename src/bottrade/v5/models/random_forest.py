from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from bottrade.v5.config import V5Config


@dataclass(slots=True)
class RFEnsemble:
    """Five-seed rightsized Random Forest ensemble for fast and robust training."""

    params: dict[str, Any]
    seeds: tuple[int, ...]
    feature_names: tuple[str, ...]
    members: list[Pipeline]

    @classmethod
    def create(
        cls,
        *,
        config: V5Config,
        feature_names: tuple[str, ...],
        params: dict[str, Any] | None = None,
        seeds: tuple[int, ...] | None = None,
    ) -> RFEnsemble:
        rf_params = {
            "n_estimators": config.rf_n_estimators,
            "max_depth": config.rf_max_depth,
            "max_samples": config.rf_max_samples,
            "max_features": config.rf_max_features,
            "min_samples_leaf": config.rf_min_samples_leaf,
            "n_jobs": config.rf_n_jobs,
        }
        if params:
            rf_params.update(params)
        return cls(
            params=rf_params,
            seeds=tuple(config.seeds if seeds is None else seeds),
            feature_names=tuple(feature_names),
            members=[],
        )

    @property
    def ensemble_id(self) -> str:
        payload = json.dumps(
            {
                "params": self.params,
                "seeds": self.seeds,
                "features": self.feature_names,
            },
            sort_keys=True,
            default=str,
        ).encode("utf-8")
        return hashlib.sha256(payload).hexdigest()[:16]

    def fit(self, x: np.ndarray, y: np.ndarray, train_indices: np.ndarray) -> dict[str, Any]:
        x_values = np.asarray(x, dtype=np.float32)
        y_values = np.asarray(y, dtype=np.float32)
        indices = np.asarray(train_indices, dtype=int)
        if x_values.ndim != 2 or x_values.shape[1] != len(self.feature_names):
            raise ValueError("feature matrix does not match feature schema")
        if indices.size == 0:
            raise ValueError("cannot train an ensemble with no rows")
        if not np.isfinite(y_values[indices]).all():
            raise ValueError("training labels contain NaN or infinity")

        self.members = []
        for seed in self.seeds:
            model = RandomForestRegressor(**self.params, random_state=int(seed))
            pipe = Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("regressor", model),
            ])
            pipe.fit(x_values[indices], y_values[indices])
            self.members.append(pipe)

        return {
            "train_samples": int(len(indices)),
            "members": len(self.members),
            "ensemble_id": self.ensemble_id,
        }

    def predict_members(self, x: np.ndarray, indices: np.ndarray | None = None) -> np.ndarray:
        if not self.members:
            raise RuntimeError("ensemble must be fitted before prediction")
        values = np.asarray(x, dtype=np.float32)
        if values.ndim != 2 or values.shape[1] != len(self.feature_names):
            raise ValueError("feature matrix does not match feature schema")
        selected = values if indices is None else values[np.asarray(indices, dtype=int)]
        predictions = np.vstack([
            np.asarray(model.predict(selected), dtype=float) for model in self.members
        ])
        return predictions

    def predict_summary(
        self, x: np.ndarray, indices: np.ndarray | None = None
    ) -> tuple[np.ndarray, np.ndarray]:
        predictions = self.predict_members(x, indices)
        return predictions.mean(axis=0), predictions.std(axis=0, ddof=0)

    def feature_importance(self) -> dict[str, float]:
        if not self.members:
            raise RuntimeError("ensemble must be fitted before feature importance")
        values = np.vstack([
            np.asarray(pipe.named_steps["regressor"].feature_importances_, dtype=float)
            for pipe in self.members
        ]).mean(axis=0)
        return {
            name: float(value)
            for name, value in sorted(
                zip(self.feature_names, values, strict=True), key=lambda item: item[1], reverse=True
            )
        }

    def save_native(self, directory: str | Path) -> Path:
        if not self.members:
            raise RuntimeError("ensemble must be fitted before saving")
        destination = Path(directory)
        destination.mkdir(parents=True, exist_ok=True)
        files: list[str] = []
        for position, pipe in enumerate(self.members):
            name = f"member_{position:02d}.joblib"
            joblib.dump(pipe, destination / name)
            files.append(name)
        metadata = {
            "format": "rf-sklearn-joblib",
            "ensemble_id": self.ensemble_id,
            "params": self.params,
            "seeds": list(self.seeds),
            "feature_names": list(self.feature_names),
            "members": files,
        }
        (destination / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
        return destination

    @classmethod
    def load_native(cls, directory: str | Path) -> RFEnsemble:
        source = Path(directory)
        meta_path = source / "metadata.json"
        if not meta_path.exists():
            raise FileNotFoundError(meta_path)
        metadata = json.loads(meta_path.read_text(encoding="utf-8"))
        members: list[Pipeline] = []
        for name in metadata["members"]:
            pipe = joblib.load(source / name)
            members.append(pipe)
        return cls(
            params=dict(metadata["params"]),
            seeds=tuple(metadata["seeds"]),
            feature_names=tuple(metadata["feature_names"]),
            members=members,
        )

    def export_onnx(self, directory: str | Path) -> Path:
        if not self.members:
            raise RuntimeError("ensemble must be fitted before ONNX export")
        destination = Path(directory)
        destination.mkdir(parents=True, exist_ok=True)
        try:
            import skl2onnx.common._container as container
            from skl2onnx import convert_sklearn
            from skl2onnx.common.data_types import FloatTensorType
        except ImportError as exc:
            raise RuntimeError("install the 'ml' extra to export sklearn models to ONNX") from exc

        original_make_node = container.make_node

        def _safe_make_node(op_type: Any, inputs: Any, outputs: Any, **attrs: Any) -> Any:
            for key, value in list(attrs.items()):
                if isinstance(value, list) and any(isinstance(item, bool) for item in value):
                    attrs[key] = [int(item) if isinstance(item, bool) else item for item in value]
                elif isinstance(value, np.ndarray) and value.dtype == np.bool_:
                    attrs[key] = value.astype(np.int64)
            return original_make_node(op_type, inputs, outputs, **attrs)

        container.make_node = _safe_make_node
        onnx_files: list[str] = []
        initial_types = [("features", FloatTensorType([None, len(self.feature_names)]))]
        try:
            for position, pipe in enumerate(self.members):
                model_proto = convert_sklearn(pipe, initial_types=initial_types, target_opset=18)
                file_name = f"member_{position:02d}.onnx"
                (destination / file_name).write_bytes(model_proto.SerializeToString())
                onnx_files.append(file_name)
        finally:
            container.make_node = original_make_node

        manifest = {
            "format": "rf-onnx-ensemble",
            "ensemble_id": self.ensemble_id,
            "feature_names": list(self.feature_names),
            "members": onnx_files,
        }
        (destination / "onnx_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        return destination

    def verify_onnx(self, directory: str | Path, x: np.ndarray, indices: np.ndarray | None = None) -> float:
        try:
            import onnxruntime as ort
        except ImportError as exc:
            raise RuntimeError("install the 'ml' extra to verify ONNX") from exc
        destination = Path(directory)
        manifest_path = destination / "onnx_manifest.json"
        if not manifest_path.exists():
            raise FileNotFoundError(manifest_path)
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        selected = x if indices is None else x[np.asarray(indices, dtype=int)]
        sample = selected[: min(128, len(selected))].astype(np.float32)
        native = self.predict_members(sample)
        onnx_predictions: list[np.ndarray] = []
        for file_name in manifest["members"]:
            session = ort.InferenceSession(str(destination / file_name), providers=["CPUExecutionProvider"])
            input_name = session.get_inputs()[0].name
            pred = session.run(None, {input_name: sample})[0]
            onnx_predictions.append(np.asarray(pred, dtype=float).reshape(-1))
        onnx_array = np.vstack(onnx_predictions)
        max_err = float(np.max(np.abs(native - onnx_array)))
        if max_err > 1e-4:
            raise ValueError(f"ONNX parity check failed with max error {max_err:.2e} > 1e-4")
        return max_err
