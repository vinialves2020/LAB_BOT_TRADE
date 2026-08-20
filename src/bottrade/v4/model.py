from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np

from bottrade.v4.config import V4Config

DEFAULT_XGB_PARAMS: dict[str, Any] = {
    "n_estimators": 400,
    "max_depth": 5,
    "learning_rate": 0.03,
    "min_child_weight": 20.0,
    "subsample": 0.8,
    "colsample_bytree": 0.8,
    "reg_alpha": 0.0,
    "reg_lambda": 5.0,
    "gamma": 0.0,
    "objective": "reg:pseudohubererror",
    "eval_metric": "mae",
    "tree_method": "hist",
    "device": "cpu",
    "n_jobs": -1,
}


def _require_xgboost() -> Any:
    try:
        import xgboost as xgb
    except ImportError as exc:  # pragma: no cover - exercised in minimal runtime
        raise RuntimeError("install the 'ml' extra to train XGBoost") from exc
    return xgb


@dataclass(slots=True)
class XGBEnsemble:
    """Five-seed XGBoost regression ensemble with an auditable schema."""

    params: dict[str, Any]
    seeds: tuple[int, ...]
    feature_names: tuple[str, ...]
    members: list[Any]

    @classmethod
    def create(
        cls,
        *,
        config: V4Config,
        feature_names: tuple[str, ...],
        params: dict[str, Any] | None = None,
    ) -> XGBEnsemble:
        merged = dict(DEFAULT_XGB_PARAMS)
        merged.update(params or {})
        merged["objective"] = config.objective
        merged["tree_method"] = config.tree_method
        merged["device"] = config.device
        return cls(
            params=merged,
            seeds=tuple(config.seeds),
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
            raise ValueError("feature matrix does not match the frozen feature schema")
        if indices.size == 0:
            raise ValueError("cannot train an ensemble with no rows")
        if not np.isfinite(y_values[indices]).all():
            raise ValueError("training labels contain NaN or infinity")
        xgb = _require_xgboost()
        self.members = []
        for seed in self.seeds:
            model = xgb.XGBRegressor(**self.params, random_state=int(seed))
            model.fit(x_values[indices], y_values[indices], verbose=False)
            self.members.append(model)
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
            raise ValueError("feature matrix does not match the frozen feature schema")
        selected = values if indices is None else values[np.asarray(indices, dtype=int)]
        predictions = np.vstack([np.asarray(model.predict(selected), dtype=float) for model in self.members])
        return predictions

    def predict_summary(
        self, x: np.ndarray, indices: np.ndarray | None = None
    ) -> tuple[np.ndarray, np.ndarray]:
        predictions = self.predict_members(x, indices)
        return predictions.mean(axis=0), predictions.std(axis=0, ddof=0)

    def feature_importance(self) -> dict[str, float]:
        if not self.members:
            raise RuntimeError("ensemble must be fitted before feature importance")
        values = np.vstack(
            [np.asarray(model.feature_importances_, dtype=float) for model in self.members]
        ).mean(axis=0)
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
        for position, model in enumerate(self.members):
            name = f"member_{position:02d}.json"
            model.save_model(str(destination / name))
            files.append(name)
        metadata = {
            "format": "xgboost-json",
            "ensemble_id": self.ensemble_id,
            "params": self.params,
            "seeds": list(self.seeds),
            "feature_names": list(self.feature_names),
            "members": files,
        }
        (destination / "metadata.json").write_text(
            json.dumps(metadata, indent=2, sort_keys=True, default=str), encoding="utf-8"
        )
        return destination

    @classmethod
    def load_native(cls, directory: str | Path) -> XGBEnsemble:
        source = Path(directory)
        metadata = json.loads((source / "metadata.json").read_text(encoding="utf-8"))
        xgb = _require_xgboost()
        members = []
        for filename in metadata["members"]:
            model = xgb.XGBRegressor()
            model.load_model(str(source / filename))
            members.append(model)
        return cls(
            params=dict(metadata["params"]),
            seeds=tuple(int(seed) for seed in metadata["seeds"]),
            feature_names=tuple(str(name) for name in metadata["feature_names"]),
            members=members,
        )

    def export_onnx(self, directory: str | Path) -> list[Path]:
        """Export every member; absence of the converter is an explicit failure."""

        try:
            import onnxmltools
            from onnxmltools.convert.common.data_types import FloatTensorType
        except ImportError as exc:  # pragma: no cover - optional dependency
            raise RuntimeError("install onnxmltools to export XGBoost artifacts") from exc
        if not self.members:
            raise RuntimeError("ensemble must be fitted before ONNX export")
        destination = Path(directory)
        destination.mkdir(parents=True, exist_ok=True)
        paths: list[Path] = []
        initial_types = [("features", FloatTensorType([None, len(self.feature_names)]))]
        for position, model in enumerate(self.members):
            path = destination / f"member_{position:02d}.onnx"
            converted = onnxmltools.convert_xgboost(
                model,
                initial_types=initial_types,
                # onnxmltools 1.16 currently supports up to opset 15 for
                # XGBoost even when the installed ONNX package is newer.
                target_opset=15,
            )
            path.write_bytes(converted.SerializeToString())
            paths.append(path)
        return paths

    def verify_onnx(self, paths: list[Path], x: np.ndarray, indices: np.ndarray) -> float:
        try:
            import onnxruntime as ort
        except ImportError as exc:  # pragma: no cover - optional dependency
            raise RuntimeError("install onnxruntime to verify XGBoost ONNX artifacts") from exc
        if len(paths) != len(self.members):
            raise ValueError("one ONNX path is required for every ensemble member")
        sample = np.asarray(x, dtype=np.float32)[np.asarray(indices, dtype=int)]
        maximum = 0.0
        for model, path in zip(self.members, paths, strict=True):
            native = np.asarray(model.predict(sample), dtype=float)
            session = ort.InferenceSession(str(path), providers=["CPUExecutionProvider"])
            input_name = session.get_inputs()[0].name
            deployed = np.asarray(session.run(None, {input_name: sample})[0]).reshape(-1)
            maximum = max(maximum, float(np.max(np.abs(native - deployed))))
        return maximum
