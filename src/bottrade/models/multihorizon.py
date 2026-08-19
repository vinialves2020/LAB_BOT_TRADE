"""Multi-horizon classification/regression models for protocol V2.

The V1 runner exposed one continuous target.  This module keeps the V2 target
contract explicit: every horizon has a normalized-return regressor and a
cost-aware classifier, and policy code can calibrate probabilities without
changing either estimator.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import (
    HistGradientBoostingClassifier,
    RandomForestClassifier,
    VotingClassifier,
)
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from bottrade.domain import HorizonForecast, ModelFamily
from bottrade.models.random_forest import (
    HistGradientBoostingRegressorModel,
    RandomForestRegressorModel,
    SeedEnsembleRegressorModel,
)
from bottrade.multihorizon import SigmoidCalibrator, select_horizon_forecast


@dataclass(frozen=True, slots=True)
class MultiHorizonPrediction:
    horizons: tuple[int, ...]
    normalized_returns: dict[int, np.ndarray]
    gross_returns: dict[int, np.ndarray]
    probabilities: dict[int, np.ndarray]


def _classifier_pipeline(
    family: ModelFamily,
    params: dict[str, Any],
    seed: int,
    labels: np.ndarray,
) -> Pipeline:
    unique = np.unique(labels[np.isfinite(labels)])
    if len(unique) < 2:
        estimator: Any = DummyClassifier(strategy="prior")
    elif family == ModelFamily.RANDOM_FOREST:
        accepted = {
            key: value
            for key, value in params.items()
            if key
            in {
                "n_estimators",
                "max_depth",
                "min_samples_leaf",
                "max_features",
                "class_weight",
                "criterion",
            }
        }
        estimator = RandomForestClassifier(random_state=seed, n_jobs=-1, **accepted)
    elif family == ModelFamily.HIST_GRADIENT_BOOSTING:
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
        estimator = HistGradientBoostingClassifier(random_state=seed, **accepted)
    else:
        raise ValueError("multi-horizon tabular models support RF and HGB")
    return Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("classifier", estimator),
        ]
    )


def _export_sklearn_onnx(pipeline: Pipeline, path: Path, n_features: int) -> None:
    try:
        import skl2onnx.common._container as container
        from skl2onnx import convert_sklearn
        from skl2onnx.common.data_types import FloatTensorType
    except ImportError as exc:  # pragma: no cover - optional deployment extra
        raise RuntimeError("install the 'ml' extra to export ONNX models") from exc
    original_make_node = container.make_node

    def safe_make_node(op_type: Any, inputs: Any, outputs: Any, **attrs: Any) -> Any:
        for key, value in list(attrs.items()):
            if isinstance(value, list) and any(isinstance(item, bool) for item in value):
                attrs[key] = [int(item) if isinstance(item, bool) else item for item in value]
            elif isinstance(value, np.ndarray) and value.dtype == np.bool_:
                attrs[key] = value.astype(np.int64)
        return original_make_node(op_type, inputs, outputs, **attrs)

    container.make_node = safe_make_node
    try:
        model = convert_sklearn(
            pipeline,
            initial_types=[("features", FloatTensorType([None, n_features]))],
            target_opset=18,
        )
    finally:
        container.make_node = original_make_node
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(model.SerializeToString())


class MultiHorizonTabularModel:
    """Independent per-horizon heads with a shared point-in-time feature matrix."""

    def __init__(
        self,
        *,
        family: ModelFamily,
        params: dict[str, Any],
        horizons: tuple[int, ...] = (3, 6, 12),
        seed: int = 11,
        seeds: list[int] | tuple[int, ...] | None = None,
    ) -> None:
        if family not in {ModelFamily.RANDOM_FOREST, ModelFamily.HIST_GRADIENT_BOOSTING}:
            raise ValueError("family must be random_forest or hist_gradient_boosting")
        self.family = family
        self.params = dict(params)
        self.horizons = tuple(sorted({int(item) for item in horizons}))
        if not self.horizons or any(item <= 0 for item in self.horizons):
            raise ValueError("horizons must contain positive values")
        self.seed = int(seed)
        self.seeds = tuple(int(item) for item in (seeds or [seed]))
        self.regressors: dict[int, Any] = {}
        self.classifiers: dict[int, Pipeline] = {}
        self.n_features: int | None = None

    def fit(self, x: np.ndarray, frame: pd.DataFrame, indices: np.ndarray) -> dict[str, Any]:
        self.n_features = int(x.shape[1])
        train_indices = np.asarray(indices, dtype=int)
        for horizon in self.horizons:
            suffix = f"_{horizon}h"
            target_name = f"target_normalized_return{suffix}"
            label_name = f"label_tradeable{suffix}"
            if target_name not in frame or label_name not in frame:
                raise ValueError(f"dataset is missing V2 target columns for {horizon}h")
            target = pd.to_numeric(frame[target_name], errors="coerce").to_numpy(dtype=float)
            labels = pd.to_numeric(frame[label_name], errors="coerce").to_numpy(dtype=float)
            valid_reg = train_indices[np.isfinite(target[train_indices])]
            valid_cls = train_indices[np.isfinite(labels[train_indices])]
            if len(valid_reg) == 0 or len(valid_cls) == 0:
                raise ValueError(f"no finite training labels for {horizon}h")
            if len(self.seeds) > 1:
                regressor = SeedEnsembleRegressorModel(
                    family=self.family.value,
                    params=self.params,
                    seeds=list(self.seeds),
                )
            elif self.family == ModelFamily.RANDOM_FOREST:
                regressor = RandomForestRegressorModel(self.params, self.seed)
            else:
                regressor = HistGradientBoostingRegressorModel(self.params, self.seed)
            regressor.fit(x, target, valid_reg)
            if len(self.seeds) > 1:
                classifier = VotingClassifier(
                    estimators=[
                        (
                            f"seed_{member_seed}",
                            _classifier_pipeline(
                                self.family,
                                self.params,
                                member_seed,
                                labels[valid_cls],
                            ),
                        )
                        for member_seed in self.seeds
                    ],
                    voting="soft",
                    flatten_transform=False,
                )
            else:
                classifier = _classifier_pipeline(
                    self.family, self.params, self.seed, labels[valid_cls]
                )
            classifier.fit(x[valid_cls], labels[valid_cls].astype(int))
            self.regressors[horizon] = regressor
            self.classifiers[horizon] = classifier
        return {"train_samples": int(len(train_indices)), "horizons": list(self.horizons)}

    def predict(
        self,
        x: np.ndarray,
        indices: np.ndarray,
        volatility: np.ndarray,
    ) -> MultiHorizonPrediction:
        if self.n_features is None or not self.regressors:
            raise RuntimeError("model must be fitted before prediction")
        selected = np.asarray(indices, dtype=int)
        vol = np.asarray(volatility, dtype=float)
        if len(vol) != len(selected):
            raise ValueError("volatility and prediction indices must have equal length")
        normalized: dict[int, np.ndarray] = {}
        gross: dict[int, np.ndarray] = {}
        probabilities: dict[int, np.ndarray] = {}
        for horizon in self.horizons:
            normalized_values = self.regressors[horizon].predict(x, selected)
            probability_matrix = self.classifiers[horizon].predict_proba(x[selected])
            classifier = self.classifiers[horizon]
            if hasattr(classifier, "classes_"):
                classes = np.asarray(classifier.classes_)
            else:
                classes = np.asarray(classifier.named_steps["classifier"].classes_)
            if probability_matrix.shape[1] == 1:
                probability_values = (
                    probability_matrix[:, 0]
                    if len(classes) and int(classes[0]) == 1
                    else np.zeros(len(selected), dtype=float)
                )
            else:
                probability_values = probability_matrix[:, 1]
            normalized[horizon] = normalized_values
            gross[horizon] = normalized_values * vol
            probabilities[horizon] = np.asarray(probability_values, dtype=float)
        return MultiHorizonPrediction(self.horizons, normalized, gross, probabilities)

    def select(
        self,
        prediction: MultiHorizonPrediction,
        *,
        round_trip_cost: float,
        probability_threshold: float,
        margin_bps: float,
    ) -> tuple[list[HorizonForecast | None], np.ndarray]:
        choices: list[HorizonForecast | None] = []
        signals = np.zeros(len(next(iter(prediction.gross_returns.values()))), dtype=float)
        for row in range(len(signals)):
            choice = select_horizon_forecast(
                horizons=prediction.horizons,
                expected_gross_returns=(prediction.gross_returns[h][row] for h in prediction.horizons),
                probabilities=(prediction.probabilities[h][row] for h in prediction.horizons),
                round_trip_cost=round_trip_cost,
                probability_threshold=probability_threshold,
                margin_bps=margin_bps,
            )
            choices.append(choice)
            signals[row] = 1.0 if choice is not None else 0.0
        return choices, signals

    def export_onnx(self, directory: Path) -> dict[str, str]:
        if self.n_features is None:
            raise RuntimeError("model must be fitted before export")
        directory.mkdir(parents=True, exist_ok=True)
        manifest: dict[str, tuple[str, str]] = {}
        for horizon in self.horizons:
            reg_path = directory / f"horizon_{horizon}h_regression.onnx"
            self.regressors[horizon].export_onnx(reg_path)
            cls_path = directory / f"horizon_{horizon}h_classification.onnx"
            _export_sklearn_onnx(self.classifiers[horizon], cls_path, self.n_features)
            manifest[str(horizon)] = str(reg_path.name), str(cls_path.name)
        (directory / "multihorizon.json").write_text(
            json.dumps({"horizons": list(self.horizons), "files": manifest}, indent=2),
            encoding="utf-8",
        )
        return manifest

    def save_native(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(self, path)


def calibrate_horizon_probabilities(
    prediction: MultiHorizonPrediction,
    labels: dict[int, np.ndarray],
) -> dict[int, np.ndarray]:
    """Fit a sigmoid per horizon on chronological out-of-sample predictions."""

    calibrated: dict[int, np.ndarray] = {}
    for horizon in prediction.horizons:
        calibrator = SigmoidCalibrator().fit(
            prediction.probabilities[horizon], labels[horizon]
        )
        calibrated[horizon] = calibrator.predict(prediction.probabilities[horizon])
    return calibrated
