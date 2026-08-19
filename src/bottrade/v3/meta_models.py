from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import joblib
import numpy as np


class ChronologicalProbabilityCalibrator:
    """Sigmoid calibrator trained only on chronological out-of-fold scores."""

    def __init__(self) -> None:
        self.intercept_: float = 0.0
        self.coef_: float = 1.0
        self.fitted: bool = False

    def fit(self, scores: np.ndarray, targets: np.ndarray) -> ChronologicalProbabilityCalibrator:
        values = np.asarray(scores, dtype=float)
        y = np.asarray(targets, dtype=int)
        valid = np.isfinite(values) & np.isfinite(y)
        values = values[valid]
        y = y[valid]
        if len(values) < 20 or len(np.unique(y)) < 2:
            self.fitted = False
            return self
        from sklearn.linear_model import LogisticRegression

        model = LogisticRegression(C=1.0, solver="lbfgs")
        model.fit(values.reshape(-1, 1), y)
        self.intercept_ = float(model.intercept_[0])
        self.coef_ = float(model.coef_[0, 0])
        self.fitted = True
        return self

    def transform(self, scores: np.ndarray) -> np.ndarray:
        values = np.asarray(scores, dtype=float)
        logits = self.intercept_ + self.coef_ * values if self.fitted else values
        logits = np.clip(logits, -40.0, 40.0)
        return 1.0 / (1.0 + np.exp(-logits))

    def to_dict(self) -> dict[str, float | bool]:
        return {"intercept": self.intercept_, "coef": self.coef_, "fitted": self.fitted}


def _chronological_oof_scores(
    model_factory: Any,
    x: np.ndarray,
    y: np.ndarray,
    *,
    splits: int = 3,
) -> tuple[np.ndarray, np.ndarray]:
    from sklearn.model_selection import TimeSeriesSplit

    if len(x) < max(30, splits * 5):
        return np.empty(0), np.empty(0, dtype=int)
    splitter = TimeSeriesSplit(n_splits=splits)
    scores: list[np.ndarray] = []
    targets: list[np.ndarray] = []
    for train_index, validation_index in splitter.split(x):
        model = model_factory()
        model.fit(x[train_index], y[train_index])
        if hasattr(model, "predict_proba"):
            prediction = model.predict_proba(x[validation_index])[:, 1]
        else:
            prediction = model.predict(x[validation_index])
        scores.append(np.asarray(prediction, dtype=float))
        targets.append(y[validation_index])
    return np.concatenate(scores), np.concatenate(targets)


@dataclass
class MetaModelBundle:
    family: str
    feature_columns: tuple[str, ...]
    classifier: Any
    regressor: Any
    mae_model: Any | None
    calibrator: ChronologicalProbabilityCalibrator
    model_version: str
    sequence_model: bool = False
    sequence_length: int = 1
    feature_mean: np.ndarray | None = None
    feature_scale: np.ndarray | None = None

    def _prepare(self, x: np.ndarray) -> np.ndarray:
        values = np.asarray(x, dtype=np.float32)
        if self.feature_mean is not None and self.feature_scale is not None:
            values = (values - self.feature_mean) / self.feature_scale
        return values

    def predict(self, x: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray | None]:
        values = self._prepare(x)
        if self.sequence_model:
            if values.ndim == 2:
                values = values[:, None, :]
            probability, expected, mae = self.classifier.predict(values)
            return probability, expected, mae
        raw_probability = self.classifier.predict_proba(values)[:, 1]
        probability = self.calibrator.transform(raw_probability)
        expected = np.asarray(self.regressor.predict(values), dtype=float)
        mae = np.asarray(self.mae_model.predict(values), dtype=float) if self.mae_model else None
        return probability, expected, mae

    def save_native(self, path: Path) -> None:
        path.mkdir(parents=True, exist_ok=True)
        joblib.dump(self, path / "bundle.joblib")
        (path / "metadata.json").write_text(
            json.dumps(
                {
                    "family": self.family,
                    "feature_columns": list(self.feature_columns),
                    "model_version": self.model_version,
                    "sequence_model": self.sequence_model,
                    "sequence_length": self.sequence_length,
                    "calibrator": self.calibrator.to_dict(),
                },
                indent=2,
            ),
            encoding="utf-8",
        )

    @classmethod
    def load_native(cls, path: Path) -> MetaModelBundle:
        model = joblib.load(path / "bundle.joblib")
        if not isinstance(model, cls):
            raise TypeError("native artifact is not a MetaModelBundle")
        return model

    def export_onnx(self, path: Path, x_sample: np.ndarray) -> dict[str, float]:
        path.mkdir(parents=True, exist_ok=True)
        if self.sequence_model:
            import onnxruntime as ort

            values = self._prepare(x_sample)
            if values.ndim == 2:
                values = values[:, None, :]
            self.classifier.export_onnx(path / "transformer.onnx", values)
            session = ort.InferenceSession(
                str(path / "transformer.onnx"), providers=["CPUExecutionProvider"]
            )
            native = self.classifier.predict(values)
            outputs = session.run(None, {session.get_inputs()[0].name: values.astype(np.float32)})
            converted_outputs = [
                1.0 / (1.0 + np.exp(-np.clip(np.asarray(outputs[0], dtype=float), -40.0, 40.0))),
                np.asarray(outputs[1], dtype=float),
                np.asarray(outputs[2], dtype=float),
            ]
            errors = [
                float(np.max(np.abs(np.asarray(expected) - np.asarray(actual))))
                for expected, actual in zip(native, converted_outputs, strict=True)
            ]
            max_error = max(errors, default=0.0)
            if max_error > 1e-4:
                raise ValueError(f"ONNX mismatch {max_error} exceeds 1e-4")
            return {"max_abs_error": max_error}
        import onnxruntime as ort

        # skl2onnx versions before the current ONNX protobuf API may pass
        # numpy scalar/bool attributes to ``make_node``.  Recent ONNX releases
        # reject those values even though the model semantics are valid.  The
        # compatibility shim is scoped to conversion and is restored in the
        # finally block below.
        import skl2onnx.common._container as skl_container
        from skl2onnx import convert_sklearn
        from skl2onnx.common.data_types import FloatTensorType

        original_make_node = skl_container.make_node

        def _plain(value: Any) -> Any:
            if isinstance(value, np.ndarray):
                return value.tolist()
            if isinstance(value, np.generic):
                return value.item()
            if isinstance(value, (list, tuple)):
                return [_plain(item) for item in value]
            return int(value) if isinstance(value, bool) else value

        def _safe_make_node(*args: Any, **kwargs: Any) -> Any:
            return original_make_node(*args, **{key: _plain(value) for key, value in kwargs.items()})

        skl_container.make_node = _safe_make_node

        initial_types = [("float_input", FloatTensorType([None, x_sample.shape[1]]))]
        errors: list[float] = []
        try:
            for name, model in (
                ("classifier", self.classifier),
                ("regressor", self.regressor),
                ("mae", self.mae_model),
            ):
                if model is None:
                    continue
                onx = convert_sklearn(model, initial_types=initial_types)
                output = path / f"{name}.onnx"
                output.write_bytes(onx.SerializeToString())
                session = ort.InferenceSession(str(output), providers=["CPUExecutionProvider"])
                native = (
                    model.predict_proba(x_sample)[:, 1]
                    if name == "classifier"
                    else np.asarray(model.predict(x_sample), dtype=float)
                )
                onnx_result = session.run(
                    None, {session.get_inputs()[0].name: x_sample.astype(np.float32)}
                )
                if name == "classifier":
                    # Classifier outputs may be a list of maps depending on the
                    # converter.  The final probability is always the last value.
                    raw = onnx_result[-1]
                    if isinstance(raw, list):
                        converted = np.asarray([float(item[1]) for item in raw])
                    else:
                        converted = np.asarray(raw)[:, -1]
                else:
                    converted = np.asarray(onnx_result[0], dtype=float).reshape(-1)
                errors.append(float(np.max(np.abs(native - converted))))
        finally:
            skl_container.make_node = original_make_node
        (path / "calibrator.json").write_text(
            json.dumps(self.calibrator.to_dict(), indent=2), encoding="utf-8"
        )
        max_error = max(errors) if errors else 0.0
        if max_error > 1e-4:
            raise ValueError(f"ONNX mismatch {max_error} exceeds 1e-4")
        return {"max_abs_error": max_error}


def _fit_sklearn_models(
    family: str,
    x: np.ndarray,
    y_class: np.ndarray,
    y_return: np.ndarray,
    y_mae: np.ndarray | None,
    *,
    seed: int,
    params: dict[str, Any] | None = None,
) -> MetaModelBundle:
    parameters = dict(params or {})
    if family == "random_forest":
        from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

        def classifier_factory() -> RandomForestClassifier:
            return RandomForestClassifier(
                n_estimators=int(parameters.get("n_estimators", 300)),
                max_depth=parameters.get("max_depth", 14),
                min_samples_leaf=int(parameters.get("min_samples_leaf", 8)),
                max_features=parameters.get("max_features", 0.7),
                random_state=seed,
                n_jobs=-1,
                class_weight="balanced_subsample",
            )
        regressor = RandomForestRegressor(
            n_estimators=int(parameters.get("n_estimators", 300)),
            max_depth=parameters.get("max_depth", 14),
            min_samples_leaf=int(parameters.get("min_samples_leaf", 8)),
            max_features=parameters.get("max_features", 0.7),
            random_state=seed,
            n_jobs=-1,
        )
        mae_model = RandomForestRegressor(
            n_estimators=int(parameters.get("n_estimators", 300)),
            max_depth=parameters.get("max_depth", 14),
            min_samples_leaf=int(parameters.get("min_samples_leaf", 8)),
            max_features=parameters.get("max_features", 0.7),
            random_state=seed,
            n_jobs=-1,
        ) if y_mae is not None else None
    elif family == "hist_gradient_boosting":
        from sklearn.ensemble import HistGradientBoostingClassifier, HistGradientBoostingRegressor

        def classifier_factory() -> HistGradientBoostingClassifier:
            return HistGradientBoostingClassifier(
                learning_rate=float(parameters.get("learning_rate", 0.05)),
                max_iter=int(parameters.get("max_iter", 300)),
                max_leaf_nodes=int(parameters.get("max_leaf_nodes", 31)),
                min_samples_leaf=int(parameters.get("min_samples_leaf", 30)),
                l2_regularization=float(parameters.get("l2_regularization", 1.0)),
                early_stopping=False,
                random_state=seed,
            )
        regressor = HistGradientBoostingRegressor(
            learning_rate=float(parameters.get("learning_rate", 0.05)),
            max_iter=int(parameters.get("max_iter", 300)),
            max_leaf_nodes=int(parameters.get("max_leaf_nodes", 31)),
            min_samples_leaf=int(parameters.get("min_samples_leaf", 30)),
            l2_regularization=float(parameters.get("l2_regularization", 1.0)),
            early_stopping=False,
            random_state=seed,
        )
        mae_model = (
            HistGradientBoostingRegressor(
                learning_rate=float(parameters.get("learning_rate", 0.05)),
                max_iter=int(parameters.get("max_iter", 300)),
                max_leaf_nodes=int(parameters.get("max_leaf_nodes", 31)),
                min_samples_leaf=int(parameters.get("min_samples_leaf", 30)),
                l2_regularization=float(parameters.get("l2_regularization", 1.0)),
                early_stopping=False,
                random_state=seed,
            )
            if y_mae is not None
            else None
        )
    else:
        raise ValueError(f"unsupported sklearn meta family: {family}")
    classifier = classifier_factory()
    classifier.fit(x, y_class)
    regressor.fit(x, y_return)
    if mae_model is not None and y_mae is not None:
        mae_model.fit(x, y_mae)
    oof_scores, oof_targets = _chronological_oof_scores(
        classifier_factory, x, y_class, splits=3
    )
    calibrator = ChronologicalProbabilityCalibrator().fit(oof_scores, oof_targets)
    return MetaModelBundle(
        family=family,
        feature_columns=tuple(f"feature_{index}" for index in range(x.shape[1])),
        classifier=classifier,
        regressor=regressor,
        mae_model=mae_model,
        calibrator=calibrator,
        model_version=f"v3-{family}-seed-{seed}",
    )


def fit_meta_model(
    family: str,
    x: np.ndarray,
    y_class: np.ndarray,
    y_return: np.ndarray,
    y_mae: np.ndarray | None = None,
    *,
    seed: int = 11,
    params: dict[str, Any] | None = None,
) -> MetaModelBundle:
    values = np.asarray(x, dtype=np.float32)
    targets = np.asarray(y_class, dtype=int)
    returns = np.asarray(y_return, dtype=float)
    if len(values) != len(targets) or len(values) != len(returns):
        raise ValueError("feature and target lengths differ")
    if len(np.unique(targets)) < 2:
        raise ValueError("classification target must contain both classes")
    if family in {"random_forest", "hist_gradient_boosting"}:
        if values.ndim != 2:
            raise ValueError("tabular meta-models require a 2D feature matrix")
        return _fit_sklearn_models(family, values, targets, returns, y_mae, seed=seed, params=params)
    if family == "transformer":
        if values.ndim not in {2, 3}:
            raise ValueError("transformer meta-model requires a 2D or 3D feature matrix")
        from bottrade.v3.transformer import fit_transformer_meta_model

        return fit_transformer_meta_model(values, targets, returns, y_mae, seed=seed, params=params)
    raise ValueError(f"unsupported V3 meta-model family: {family}")
