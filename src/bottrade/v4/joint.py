"""V4.4 cost-aware classification + regression experiment.

The module intentionally lives beside the V4.3 regressor.  It is a bounded
challenger: one binary label asks whether the next hourly return pays the
configured round-trip cost, while a regression forecast estimates its size.
An entry requires both forecasts to agree.  The holdout is never read here.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

import numpy as np
import pandas as pd

from bottrade.v4.backtest import _valid_frame, summarize_trades
from bottrade.v4.config import V4Config
from bottrade.v4.features import DirectDataset
from bottrade.validation import require_minimum_folds, walk_forward_folds

JOINT_XGB_PARAMS: dict[str, Any] = {
    "n_estimators": 400,
    "max_depth": 5,
    "learning_rate": 0.03,
    "min_child_weight": 20.0,
    "subsample": 0.8,
    "colsample_bytree": 0.8,
    "reg_alpha": 0.0,
    "reg_lambda": 5.0,
    "gamma": 0.0,
    "n_jobs": -1,
}

JOINT_HGB_PARAMS: dict[str, Any] = {
    "max_iter": 300,
    "max_leaf_nodes": 31,
    "learning_rate": 0.05,
    "min_samples_leaf": 20,
    "l2_regularization": 1.0,
}


def _require_xgboost() -> Any:
    try:
        import xgboost as xgb
    except ImportError as exc:  # pragma: no cover - optional training extra
        raise RuntimeError("install the 'ml' extra to train the joint XGBoost model") from exc
    return xgb


def _require_sklearn() -> tuple[Any, Any, Any, Any]:
    try:
        from sklearn.dummy import DummyClassifier
        from sklearn.ensemble import HistGradientBoostingClassifier, HistGradientBoostingRegressor
        from sklearn.linear_model import LogisticRegression
    except ImportError as exc:  # pragma: no cover - optional training extra
        raise RuntimeError("install the 'ml' extra to train the joint challenger") from exc
    return (
        DummyClassifier,
        HistGradientBoostingClassifier,
        HistGradientBoostingRegressor,
        LogisticRegression,
    )


@dataclass(frozen=True, slots=True)
class ProbabilityCalibrator:
    """Monotone sigmoid calibration fitted only on past OOS probabilities."""

    intercept: float = 0.0
    slope: float = 1.0
    identity: bool = True

    def transform(self, probabilities: np.ndarray) -> np.ndarray:
        values = np.asarray(probabilities, dtype=float)
        if self.identity:
            return np.clip(values, 0.0, 1.0)
        logits = np.log(np.clip(values, 1e-6, 1.0 - 1e-6) / np.clip(1.0 - values, 1e-6, 1.0))
        logits = np.clip(self.intercept + self.slope * logits, -40.0, 40.0)
        return 1.0 / (1.0 + np.exp(-logits))


def fit_probability_calibrator(
    probabilities: np.ndarray, labels: np.ndarray
) -> ProbabilityCalibrator:
    """Fit a chronological sigmoid calibrator without in-sample predictions."""

    values = np.asarray(probabilities, dtype=float)
    target = np.asarray(labels, dtype=int)
    mask = np.isfinite(values) & np.isfinite(target)
    if int(mask.sum()) < 20 or np.unique(target[mask]).size < 2:
        return ProbabilityCalibrator()
    _, _, _, LogisticRegression = _require_sklearn()
    clipped = np.clip(values[mask], 1e-6, 1.0 - 1e-6)
    logits = np.log(clipped / (1.0 - clipped)).reshape(-1, 1)
    model = LogisticRegression(C=1.0, solver="lbfgs", random_state=11)
    model.fit(logits, target[mask])
    return ProbabilityCalibrator(
        intercept=float(model.intercept_[0]),
        slope=float(model.coef_[0][0]),
        identity=False,
    )


@dataclass(slots=True)
class JointEnsemble:
    """Five-seed paired regression/classification ensemble."""

    family: Literal["xgboost", "hist_gradient_boosting"]
    config: V4Config
    params: dict[str, Any]
    seeds: tuple[int, ...]
    feature_names: tuple[str, ...]
    regressors: list[Any] = field(default_factory=list)
    classifiers: list[Any] = field(default_factory=list)

    @classmethod
    def create(
        cls,
        *,
        family: Literal["xgboost", "hist_gradient_boosting"],
        config: V4Config,
        feature_names: tuple[str, ...],
        params: dict[str, Any] | None = None,
        seeds: tuple[int, ...] | None = None,
    ) -> JointEnsemble:
        if family not in {"xgboost", "hist_gradient_boosting"}:
            raise ValueError("family must be xgboost or hist_gradient_boosting")
        defaults = JOINT_XGB_PARAMS if family == "xgboost" else JOINT_HGB_PARAMS
        merged = dict(defaults)
        merged.update(params or {})
        return cls(
            family=family,
            config=config,
            params=merged,
            seeds=tuple(config.seeds if seeds is None else seeds),
            feature_names=tuple(feature_names),
        )

    def _new_models(self, seed: int) -> tuple[Any, Any]:
        if self.family == "xgboost":
            xgb = _require_xgboost()
            common = dict(self.params)
            common.update(
                {
                    "tree_method": self.config.tree_method,
                    "device": self.config.device,
                    "random_state": int(seed),
                }
            )
            reg = xgb.XGBRegressor(
                **common,
                objective="reg:squarederror",
                eval_metric="mae",
            )
            clf = xgb.XGBClassifier(
                **common,
                objective="binary:logistic",
                eval_metric="logloss",
            )
            return reg, clf
        DummyClassifier, HistGradientBoostingClassifier, HistGradientBoostingRegressor, _ = (
            _require_sklearn()
        )
        reg = HistGradientBoostingRegressor(**self.params, random_state=int(seed))
        clf = HistGradientBoostingClassifier(**self.params, random_state=int(seed))
        # The dummy is selected in fit() if a fold happens to contain one class.
        return reg, clf

    def fit(self, x: np.ndarray, target_return: np.ndarray, target_class: np.ndarray, train_indices: np.ndarray) -> dict[str, Any]:
        values = np.asarray(x, dtype=np.float32)
        returns = np.asarray(target_return, dtype=np.float32)
        labels = np.asarray(target_class, dtype=int)
        indices = np.asarray(train_indices, dtype=int)
        if values.ndim != 2 or values.shape[1] != len(self.feature_names):
            raise ValueError("feature matrix does not match the frozen feature schema")
        if indices.size == 0 or not np.isfinite(returns[indices]).all():
            raise ValueError("joint training labels are empty or non-finite")
        self.regressors = []
        self.classifiers = []
        DummyClassifier, _, _, _ = _require_sklearn()
        for seed in self.seeds:
            reg, clf = self._new_models(seed)
            reg.fit(values[indices], returns[indices])
            if np.unique(labels[indices]).size < 2:
                clf = DummyClassifier(strategy="prior")
            clf.fit(values[indices], labels[indices])
            self.regressors.append(reg)
            self.classifiers.append(clf)
        return {"train_samples": int(len(indices)), "members": len(self.seeds)}

    def predict_reg_members(self, x: np.ndarray, indices: np.ndarray) -> np.ndarray:
        values = np.asarray(x, dtype=np.float32)[np.asarray(indices, dtype=int)]
        return np.vstack([np.asarray(model.predict(values), dtype=float) for model in self.regressors])

    def predict_prob_members(self, x: np.ndarray, indices: np.ndarray) -> np.ndarray:
        values = np.asarray(x, dtype=np.float32)[np.asarray(indices, dtype=int)]
        probabilities = []
        for model in self.classifiers:
            predicted = np.asarray(model.predict_proba(values), dtype=float)
            probabilities.append(predicted[:, 1] if predicted.shape[1] > 1 else predicted[:, 0])
        return np.vstack(probabilities)

    def feature_importance(self) -> dict[str, float]:
        values: list[np.ndarray] = []
        for model in self.regressors:
            importance = getattr(model, "feature_importances_", None)
            if importance is not None:
                values.append(np.asarray(importance, dtype=float))
        if not values:
            return {}
        average = np.vstack(values).mean(axis=0)
        return dict(
            sorted(
                zip(self.feature_names, average, strict=True),
                key=lambda item: item[1],
                reverse=True,
            )
        )


@dataclass(frozen=True, slots=True)
class JointPolicy:
    probability_threshold: float
    margin_bps: int


def select_joint_stateful_trades(
    frame: pd.DataFrame,
    predictions: np.ndarray,
    deviations: np.ndarray,
    probabilities: np.ndarray,
    *,
    config: V4Config,
    policy: JointPolicy,
    cost_multiplier: float = 1.0,
) -> pd.DataFrame:
    """Long/flat policy requiring cost-paying regression and classification."""

    if not (len(frame) == len(predictions) == len(deviations) == len(probabilities)):
        raise ValueError("joint prediction arrays must align with the frame")
    data = frame.copy().sort_values("as_of").reset_index(drop=True)
    data["prediction"] = np.asarray(predictions, dtype=float)
    data["prediction_std"] = np.asarray(deviations, dtype=float)
    data["probability_net_positive"] = np.asarray(probabilities, dtype=float)
    for column in ("as_of", "entry_time", "exit_time"):
        data[column] = pd.to_datetime(data[column], utc=True)
    threshold = np.log1p(
        (config.round_trip_bps * cost_multiplier + policy.margin_bps) / 10_000.0
    )
    selected: list[dict[str, object]] = []
    position: dict[str, object] | None = None
    daily_entries: dict[object, int] = {}

    def close_position(exit_time: pd.Timestamp, exit_price: float, exit_prediction: float) -> None:
        nonlocal position
        if position is None:
            return
        entry_price = float(position["entry_price"])
        if not np.isfinite(exit_price) or exit_price <= 0 or entry_price <= 0:
            position = None
            return
        gross = exit_price / entry_price - 1.0
        selected.append(
            {
                "as_of": position["as_of"],
                "entry_time": position["entry_time"],
                "exit_time": exit_time,
                "entry_price": entry_price,
                "exit_price": exit_price,
                "gross_return": gross,
                "net_return": gross - config.round_trip_bps * cost_multiplier / 10_000.0,
                "prediction": position["prediction"],
                "exit_prediction": exit_prediction,
                "probability_net_positive": position["probability"],
                "margin_bps": policy.margin_bps,
                "probability_threshold": policy.probability_threshold,
            }
        )
        position = None

    for row in data.itertuples(index=False):
        entry_time = pd.Timestamp(row.entry_time)
        prediction = float(row.prediction)
        deviation = float(row.prediction_std)
        probability = float(row.probability_net_positive)
        effective = prediction - config.uncertainty_std_multiplier * deviation
        valid = bool(row.label_valid) and np.isfinite(float(row.entry_price))
        classification_ok = probability >= policy.probability_threshold
        if position is not None:
            held_hours = (entry_time - pd.Timestamp(position["entry_time"])).total_seconds() / 3600.0
            should_exit = (
                not valid
                or held_hours >= config.max_holding_hours
                or effective < -threshold
                or not classification_ok
                or (config.exit_on_non_positive and effective <= 0.0)
            )
            if should_exit:
                close_position(entry_time, float(row.entry_price), prediction)
                continue
        if position is None and valid and classification_ok and effective > threshold:
            day = entry_time.date()
            if daily_entries.get(day, 0) < config.max_round_trips_per_asset_day:
                position = {
                    "as_of": row.as_of,
                    "entry_time": entry_time,
                    "entry_price": float(row.entry_price),
                    "prediction": prediction,
                    "probability": probability,
                }
                daily_entries[day] = daily_entries.get(day, 0) + 1
    if position is not None and len(data):
        last = data.iloc[-1]
        close_position(
            pd.Timestamp(last["exit_time"]),
            float(last["exit_price"]),
            float(last["prediction"]),
        )
    return pd.DataFrame(selected)


def choose_joint_policy(
    frame: pd.DataFrame,
    predictions: np.ndarray,
    deviations: np.ndarray,
    probabilities: np.ndarray,
    *,
    config: V4Config,
) -> tuple[JointPolicy, dict[str, Any]]:
    candidates: list[tuple[float, JointPolicy, dict[str, float | int]]] = []
    for probability_threshold in (0.50, 0.55, 0.60):
        for margin in config.entry_margins_bps:
            policy = JointPolicy(probability_threshold, int(margin))
            trades = select_joint_stateful_trades(
                frame,
                predictions,
                deviations,
                probabilities,
                config=config,
                policy=policy,
            )
            metrics = summarize_trades(trades)
            if int(metrics["closed_trades"]) < config.minimum_calibration_trades:
                continue
            score = float(metrics["sortino_daily"])
            if not np.isfinite(score):
                score = 1e9 if float(metrics["total_return"]) > 0 else -1e9
            candidates.append((score, policy, metrics))
    if not candidates:
        fallback = JointPolicy(0.60, max(config.entry_margins_bps))
        return fallback, {"status": "insufficient_calibration_trades", "trades": 0}
    _, policy, metrics = max(
        candidates,
        key=lambda item: (item[0], -item[1].probability_threshold, -item[1].margin_bps),
    )
    return policy, {"status": "selected", "metrics": metrics, "trades": int(metrics["closed_trades"])}


@dataclass(frozen=True, slots=True)
class JointFoldResult:
    name: str
    policy: JointPolicy
    metrics: dict[str, float | int]
    seed_metrics: dict[str, dict[str, float | int]]
    calibration: dict[str, Any]
    trades: pd.DataFrame


@dataclass(frozen=True, slots=True)
class JointWalkForwardResult:
    asset: str
    family: str
    folds: tuple[JointFoldResult, ...]
    trades: pd.DataFrame
    metrics: dict[str, float | int]
    feature_importance: dict[str, float] = field(default_factory=dict)


def run_joint_walk_forward(
    dataset: DirectDataset,
    *,
    config: V4Config,
    family: Literal["xgboost", "hist_gradient_boosting"],
    params: dict[str, Any] | None = None,
    max_folds: int | None = None,
    fold_selection: Literal["last", "first"] = "last",
    seeds_override: tuple[int, ...] | None = None,
) -> JointWalkForwardResult:
    frame = _valid_frame(dataset)
    if frame.empty:
        raise ValueError("dataset has no valid pre-holdout labels")
    raw_target_return = frame[dataset.target_column].to_numpy(dtype=float)
    if config.normalized_return_target:
        if "ewma_volatility_1h" not in frame:
            raise ValueError("normalized target requires ewma_volatility_1h in the feature schema")
        raw_volatility = pd.to_numeric(
            frame["ewma_volatility_1h"], errors="coerce"
        ).to_numpy(dtype=float)
        usable = np.isfinite(raw_volatility) & (raw_volatility >= 0.0)
        frame = frame.loc[usable].reset_index(drop=True)
        raw_target_return = raw_target_return[usable]
        # A zero-volatility candle has no directional information; the tiny
        # floor keeps the normalized target finite without inventing a price
        # or volume observation.
        target_volatility = np.maximum(raw_volatility[usable], 1e-6)
        y_return = (raw_target_return / target_volatility).astype(np.float32)
    else:
        target_volatility = np.ones(len(frame), dtype=float)
        y_return = raw_target_return.astype(np.float32)
    if frame.empty:
        raise ValueError("normalized target has no rows with causal volatility")
    timestamps = pd.to_datetime(frame["as_of"], utc=True)
    folds = walk_forward_folds(
        timestamps,
        train_months=config.train_months,
        calibration_months=config.calibration_months,
        test_months=config.test_months,
        purge_hours=config.purge_hours,
        segment_ids=frame.get("continuity_segment_id"),
        minimum_coverage=0.95,
    )
    if max_folds is None:
        require_minimum_folds(folds, config.minimum_pre_holdout_folds)
        selected_folds = folds
    elif max_folds < 1:
        raise ValueError("max_folds must be positive")
    elif fold_selection == "first":
        selected_folds = folds[:max_folds]
    else:
        selected_folds = folds[-max_folds:]
    if fold_selection not in {"first", "last"}:
        raise ValueError("fold_selection must be 'first' or 'last'")

    x = frame[list(dataset.feature_columns)].to_numpy(dtype=np.float32)
    y_class = (frame["gross_return"].to_numpy(dtype=float) > config.round_trip_bps / 10_000.0).astype(int)
    results: list[JointFoldResult] = []
    all_trades: list[pd.DataFrame] = []
    all_stress_trades: list[pd.DataFrame] = []
    importance: dict[str, list[float]] = {name: [] for name in dataset.feature_columns}
    for fold in selected_folds:
        ensemble = JointEnsemble.create(
            family=family,
            config=config,
            feature_names=dataset.feature_columns,
            params=params,
            seeds=seeds_override,
        )
        ensemble.fit(x, y_return, y_class, fold.train_indices)
        cal_reg_members = ensemble.predict_reg_members(x, fold.calibration_indices)
        cal_prob_members = ensemble.predict_prob_members(x, fold.calibration_indices)
        calibration_volatility = target_volatility[fold.calibration_indices]
        cal_reg = cal_reg_members.mean(axis=0) * calibration_volatility
        cal_reg_std = cal_reg_members.std(axis=0, ddof=0) * calibration_volatility
        cal_prob = cal_prob_members.mean(axis=0)
        calibrator = fit_probability_calibrator(cal_prob, y_class[fold.calibration_indices])
        cal_prob = calibrator.transform(cal_prob)
        policy, calibration = choose_joint_policy(
            frame.iloc[fold.calibration_indices].reset_index(drop=True),
            cal_reg,
            cal_reg_std,
            cal_prob,
            config=config,
        )
        test_reg_members = ensemble.predict_reg_members(x, fold.test_indices)
        test_prob_members = ensemble.predict_prob_members(x, fold.test_indices)
        test_volatility = target_volatility[fold.test_indices]
        test_reg = test_reg_members.mean(axis=0) * test_volatility
        test_reg_std = test_reg_members.std(axis=0, ddof=0) * test_volatility
        test_prob = calibrator.transform(test_prob_members.mean(axis=0))
        test_frame = frame.iloc[fold.test_indices].reset_index(drop=True)
        trades = select_joint_stateful_trades(
            test_frame,
            test_reg,
            test_reg_std,
            test_prob,
            config=config,
            policy=policy,
        )
        metrics = summarize_trades(trades)
        stress_trades = select_joint_stateful_trades(
            test_frame,
            test_reg,
            test_reg_std,
            test_prob,
            config=config,
            policy=policy,
            cost_multiplier=config.stress_multiplier,
        )
        metrics.update(
            {f"stress_{key}": value for key, value in summarize_trades(stress_trades).items()}
        )
        seed_metrics: dict[str, dict[str, float | int]] = {}
        for seed, reg_member, prob_member in zip(
            ensemble.seeds,
            test_reg_members,
            test_prob_members,
            strict=True,
        ):
            member_prob = calibrator.transform(prob_member)
            member_trades = select_joint_stateful_trades(
                test_frame,
                reg_member * test_volatility,
                np.zeros(len(reg_member), dtype=float),
                member_prob,
                config=config,
                policy=policy,
            )
            seed_metrics[str(seed)] = summarize_trades(member_trades)
        results.append(
            JointFoldResult(
                fold.name,
                policy,
                metrics,
                seed_metrics,
                {
                    "status": calibration.get("status", "unknown"),
                    "probability_intercept": calibrator.intercept,
                    "probability_slope": calibrator.slope,
                    "probability_identity": calibrator.identity,
                    "selected_trades": calibration.get("trades", 0),
                },
                trades,
            )
        )
        if not trades.empty:
            all_trades.append(
                trades.assign(
                    fold=fold.name,
                    margin_bps=policy.margin_bps,
                    probability_threshold=policy.probability_threshold,
                )
            )
        if not stress_trades.empty:
            all_stress_trades.append(
                stress_trades.assign(
                    fold=fold.name,
                    margin_bps=policy.margin_bps,
                    probability_threshold=policy.probability_threshold,
                )
            )
        for name, value in ensemble.feature_importance().items():
            importance[name].append(value)
    combined = pd.concat(all_trades, ignore_index=True) if all_trades else pd.DataFrame()
    stress_combined = pd.concat(all_stress_trades, ignore_index=True) if all_stress_trades else pd.DataFrame()
    metrics = summarize_trades(combined)
    metrics.update(
        {f"stress_{key}": value for key, value in summarize_trades(stress_combined).items()}
    )
    averaged_importance = {
        name: float(np.mean(values)) for name, values in importance.items() if values
    }
    return JointWalkForwardResult(
        asset=dataset.asset.value,
        family=family,
        folds=tuple(results),
        trades=combined,
        metrics=metrics,
        feature_importance=dict(
            sorted(averaged_importance.items(), key=lambda item: item[1], reverse=True)
        ),
    )
