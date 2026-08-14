from __future__ import annotations

from pathlib import Path
from typing import Any

import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from bottrade.models.base import ResearchRegressor


class SklearnRegressorModel(ResearchRegressor):
    def __init__(self, pipeline: Pipeline, family: str) -> None:
        self.pipeline = pipeline
        self.family = family
        self.n_features: int | None = None

    def fit(self, x: np.ndarray, y: np.ndarray, indices: np.ndarray) -> dict[str, Any]:
        self.n_features = x.shape[1]
        self.pipeline.fit(x[indices], y[indices])
        return {"train_samples": int(len(indices))}

    def predict(self, x: np.ndarray, indices: np.ndarray) -> np.ndarray:
        return np.asarray(self.pipeline.predict(x[indices]), dtype=np.float64)

    def export_onnx(self, path: Path) -> None:
        if self.n_features is None:
            raise RuntimeError("model must be fitted before export")
        try:
            from skl2onnx import convert_sklearn
            from skl2onnx.common.data_types import FloatTensorType
        except ImportError as exc:
            raise RuntimeError("install the 'ml' extra to export sklearn models to ONNX") from exc
        model = convert_sklearn(
            self.pipeline,
            initial_types=[("features", FloatTensorType([None, self.n_features]))],
            target_opset=18,
        )
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(model.SerializeToString())

    def verify_onnx(self, path: Path, x: np.ndarray, indices: np.ndarray) -> float:
        try:
            import onnxruntime as ort
        except ImportError as exc:
            raise RuntimeError("install the 'ml' extra to verify ONNX models") from exc
        sample_indices = indices[: min(128, len(indices))]
        native = self.predict(x, sample_indices)
        session = ort.InferenceSession(str(path), providers=["CPUExecutionProvider"])
        deployed = session.run(None, {"features": x[sample_indices].astype(np.float32)})[0]
        deployed = np.asarray(deployed).reshape(-1)
        return float(np.max(np.abs(native - deployed))) if len(native) else 0.0

    def save_native(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(self.pipeline, path)


class RandomForestRegressorModel(SklearnRegressorModel):
    def __init__(self, params: dict[str, Any], seed: int) -> None:
        model = RandomForestRegressor(random_state=seed, **params)
        super().__init__(
            Pipeline(
                [
                    ("imputer", SimpleImputer(strategy="median")),
                    ("regressor", model),
                ]
            ),
            family="random_forest",
        )

    @property
    def feature_importances_(self) -> np.ndarray:
        return np.asarray(self.pipeline.named_steps["regressor"].feature_importances_)


class RidgeRegressorModel(SklearnRegressorModel):
    def __init__(self, alpha: float = 1.0) -> None:
        super().__init__(
            Pipeline(
                [
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler()),
                    ("regressor", Ridge(alpha=alpha)),
                ]
            ),
            family="ridge",
        )
