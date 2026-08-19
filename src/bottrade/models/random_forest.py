from __future__ import annotations

from pathlib import Path
from typing import Any

import joblib
import numpy as np
from sklearn.ensemble import (
    HistGradientBoostingRegressor,
    RandomForestRegressor,
    VotingRegressor,
)
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
            import skl2onnx.common._container as container
            from skl2onnx import convert_sklearn
            from skl2onnx.common.data_types import FloatTensorType
        except ImportError as exc:
            raise RuntimeError("install the 'ml' extra to export sklearn models to ONNX") from exc
        # skl2onnx currently emits Python bools for the HGB tree ensemble's
        # integer-valued missing-value attribute.  ONNX rejects that type on
        # recent protobuf versions; normalize only during this conversion.
        original_make_node = container.make_node

        def _safe_make_node(op_type: Any, inputs: Any, outputs: Any, **attrs: Any) -> Any:
            for key, value in list(attrs.items()):
                if isinstance(value, list) and any(isinstance(item, bool) for item in value):
                    attrs[key] = [int(item) if isinstance(item, bool) else item for item in value]
                elif isinstance(value, np.ndarray) and value.dtype == np.bool_:
                    attrs[key] = value.astype(np.int64)
            return original_make_node(op_type, inputs, outputs, **attrs)

        container.make_node = _safe_make_node
        try:
            model = convert_sklearn(
                self.pipeline,
                initial_types=[("features", FloatTensorType([None, self.n_features]))],
                target_opset=18,
            )
        finally:
            container.make_node = original_make_node
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


class HistGradientBoostingRegressorModel(SklearnRegressorModel):
    """ONNX-compatible tabular challenger for the V2 protocol."""

    def __init__(self, params: dict[str, Any], seed: int) -> None:
        accepted = {
            key: value
            for key, value in params.items()
            if key
            in {
                "learning_rate",
                "max_iter",
                "max_leaf_nodes",
                "max_depth",
                "min_samples_leaf",
                "l2_regularization",
                "max_bins",
                "early_stopping",
                "validation_fraction",
                "n_iter_no_change",
                "tol",
            }
        }
        accepted["random_state"] = seed
        super().__init__(
            Pipeline(
                [
                    ("imputer", SimpleImputer(strategy="median")),
                    ("regressor", HistGradientBoostingRegressor(**accepted)),
                ]
            ),
            family="hist_gradient_boosting",
        )

    @property
    def feature_importances_(self) -> np.ndarray:
        estimator = self.pipeline.named_steps["regressor"]
        return np.asarray(getattr(estimator, "feature_importances_", np.zeros(self.n_features or 0)))


class SeedEnsembleRegressorModel(SklearnRegressorModel):
    """Mean ensemble used for the frozen V2 tabular artifact.

    ``VotingRegressor`` keeps every seed in one native/ONNX graph, so the
    deployed prediction is the arithmetic mean rather than the best seed.
    The HGB converter currently emits boolean tree attributes on some sklearn
    versions; the parent export method normalizes those attributes.
    """

    def __init__(
        self,
        *,
        family: str,
        params: dict[str, Any],
        seeds: list[int],
    ) -> None:
        if not seeds:
            raise ValueError("an ensemble requires at least one seed")
        estimators: list[tuple[str, Pipeline]] = []
        for seed in seeds:
            if family == "random_forest":
                estimator: Any = RandomForestRegressor(random_state=seed, **params)
            elif family == "hist_gradient_boosting":
                accepted = {
                    key: value
                    for key, value in params.items()
                    if key
                    in {
                        "learning_rate",
                        "max_iter",
                        "max_leaf_nodes",
                        "max_depth",
                        "min_samples_leaf",
                        "l2_regularization",
                        "max_bins",
                        "early_stopping",
                        "validation_fraction",
                        "n_iter_no_change",
                        "tol",
                    }
                }
                estimator = HistGradientBoostingRegressor(
                    random_state=seed, **accepted
                )
            else:
                raise ValueError(f"unsupported tabular ensemble family: {family}")
            estimators.append(
                (
                    f"seed_{seed}",
                    Pipeline(
                        [
                            ("imputer", SimpleImputer(strategy="median")),
                            ("regressor", estimator),
                        ]
                    ),
                )
            )
        super().__init__(VotingRegressor(estimators=estimators), family=family)
        self.seeds = tuple(int(seed) for seed in seeds)

    @property
    def feature_importances_(self) -> np.ndarray:
        values: list[np.ndarray] = []
        for pipeline in getattr(self.pipeline, "estimators_", []):
            estimator = pipeline.named_steps["regressor"]
            importance = getattr(estimator, "feature_importances_", None)
            if importance is not None:
                values.append(np.asarray(importance, dtype=float))
        return (
            np.mean(np.stack(values), axis=0)
            if values
            else np.zeros(self.n_features or 0, dtype=float)
        )
