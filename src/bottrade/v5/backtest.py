from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any, Literal

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from bottrade.v4.backtest import (
    FoldResult,
    choose_policy,
    select_trades,
    summarize_trades,
)
from bottrade.v4.config import V4Config
from bottrade.v4.features import DirectDataset
from bottrade.v5.config import V5Config
from bottrade.v5.models.random_forest import RFEnsemble
from bottrade.v5.models.transformer import PatchTransformerEnsemble
from bottrade.v5.models.xgboost_ref import create_xgboost_reference
from bottrade.validation import require_minimum_folds, walk_forward_folds


@dataclass(frozen=True, slots=True)
class ModelRunResult:
    model_name: str
    asset: str
    folds: tuple[FoldResult, ...]
    trades: pd.DataFrame
    stress_trades: pd.DataFrame
    metrics: dict[str, float | int]
    predictive_metrics: dict[str, float]
    fit_time_seconds: float
    predict_time_seconds: float
    gate_status: dict[str, bool]
    model_ensemble: Any = None


def _to_v4_config(config: V5Config) -> V4Config:
    """Map V5Config execution settings into V4Config expected by select_trades."""
    return V4Config(
        round_trip_bps=config.round_trip_bps,
        stress_multiplier=config.stress_multiplier,
        entry_margins_bps=config.entry_margins_bps,
        stateful_hourly=config.stateful_hourly,
        max_holding_hours=config.max_holding_hours,
        exit_on_non_positive=config.exit_on_non_positive,
        uncertainty_std_multiplier=config.uncertainty_std_multiplier,
        max_round_trips_per_asset_day=config.max_round_trips_per_asset_day,
        minimum_calibration_trades=config.minimum_calibration_trades,
    )


def compute_predictive_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    mask = np.isfinite(y_true) & np.isfinite(y_pred)
    if not mask.any() or int(mask.sum()) < 5:
        return {"mae": 0.0, "ic_pearson": 0.0, "ic_spearman": 0.0, "directional_accuracy": 0.5}
    yt = y_true[mask]
    yp = y_pred[mask]
    mae = float(np.mean(np.abs(yt - yp)))
    var_t = float(np.var(yt))
    var_p = float(np.var(yp))
    if var_t > 1e-12 and var_p > 1e-12:
        pearson = float(np.corrcoef(yt, yp)[0, 1])
        spearman = float(spearmanr(yt, yp).statistic)
    else:
        pearson = 0.0
        spearman = 0.0
    dir_acc = float(np.mean(np.sign(yt) == np.sign(yp)))
    return {
        "mae": mae,
        "ic_pearson": pearson,
        "ic_spearman": spearman,
        "directional_accuracy": dir_acc,
    }


def evaluate_gates(metrics: dict[str, float | int], config: V5Config) -> dict[str, bool]:
    monthly_trades = float(metrics.get("average_monthly_trades", 0.0))
    sharpe = float(metrics.get("sharpe_daily", 0.0))
    pf = float(metrics.get("profit_factor", 0.0))
    max_dd = float(metrics.get("maximum_drawdown", 1.0))
    total_ret = float(metrics.get("total_return", -1.0))

    pass_frequency = monthly_trades >= config.minimum_asset_monthly_trades
    pass_sharpe = sharpe >= config.minimum_sharpe
    pass_pf = pf >= config.minimum_profit_factor
    pass_drawdown = max_dd <= config.maximum_drawdown
    pass_return = total_ret > 0.0

    all_passed = pass_frequency and pass_sharpe and pass_pf and pass_drawdown and pass_return
    return {
        "frequency": pass_frequency,
        "sharpe": pass_sharpe,
        "profit_factor": pass_pf,
        "drawdown": pass_drawdown,
        "positive_return": pass_return,
        "overall": all_passed,
    }


def run_ensemble_walk_forward(
    model_name: Literal["random_forest", "transformer", "xgboost"],
    dataset: DirectDataset,
    *,
    config: V5Config,
    max_folds: int | None = None,
    seeds_override: tuple[int, ...] | None = None,
) -> ModelRunResult:
    frame = dataset.frame.copy().sort_values("as_of").reset_index(drop=True)
    valid = frame["label_valid"].astype(bool) & np.isfinite(frame[dataset.target_column])
    frame = frame.loc[valid].reset_index(drop=True)
    if frame.empty:
        raise ValueError("dataset has no valid pre-holdout labels")

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
    else:
        if max_folds < 1:
            raise ValueError("max_folds must be positive")
        selected_folds = folds[-max_folds:]

    x = frame[list(dataset.feature_columns)].to_numpy(dtype=np.float32)
    y = frame[dataset.target_column].to_numpy(dtype=np.float32)
    v4_compat = _to_v4_config(config)

    results: list[FoldResult] = []
    all_trades: list[pd.DataFrame] = []
    all_stress_trades: list[pd.DataFrame] = []
    total_fit_time = 0.0
    total_predict_time = 0.0
    all_test_preds: list[np.ndarray] = []
    all_test_actuals: list[np.ndarray] = []
    last_ensemble: Any = None

    for fold in selected_folds:
        if model_name == "random_forest":
            ensemble = RFEnsemble.create(
                config=config,
                feature_names=dataset.feature_columns,
                seeds=seeds_override,
            )
        elif model_name == "transformer":
            ensemble = PatchTransformerEnsemble.create(
                config=config,
                feature_names=dataset.feature_columns,
                seeds=seeds_override,
            )
        elif model_name == "xgboost":
            ensemble = create_xgboost_reference(
                config=config,
                feature_names=dataset.feature_columns,
                seeds=seeds_override,
            )
        else:
            raise ValueError(f"unknown model {model_name}")

        t0 = time.perf_counter()
        ensemble.fit(x, y, fold.train_indices)
        total_fit_time += time.perf_counter() - t0
        last_ensemble = ensemble

        t0 = time.perf_counter()
        cal_mean, cal_std = ensemble.predict_summary(x, fold.calibration_indices)
        test_mean, test_std = ensemble.predict_summary(x, fold.test_indices)
        total_predict_time += time.perf_counter() - t0

        cal_frame = frame.iloc[fold.calibration_indices].reset_index(drop=True)
        policy, cal_meta = choose_policy(cal_frame, cal_mean, cal_std, config=v4_compat)

        test_frame = frame.iloc[fold.test_indices].reset_index(drop=True)
        trades = select_trades(test_frame, test_mean, test_std, config=v4_compat, policy=policy, cost_multiplier=1.0)
        stress_trades = select_trades(
            test_frame, test_mean, test_std, config=v4_compat, policy=policy, cost_multiplier=config.stress_multiplier
        )

        all_trades.append(trades)
        all_stress_trades.append(stress_trades)
        all_test_preds.append(test_mean)
        all_test_actuals.append(test_frame[dataset.target_column].to_numpy(dtype=float))

        results.append(
            FoldResult(
                name=fold.name,
                policy=policy,
                metrics=summarize_trades(trades),
                seed_metrics={},
                calibration=cal_meta,
                trades=trades,
            )
        )

    merged_trades = pd.concat(all_trades, ignore_index=True) if all_trades else pd.DataFrame()
    merged_stress_trades = pd.concat(all_stress_trades, ignore_index=True) if all_stress_trades else pd.DataFrame()
    overall_metrics = summarize_trades(merged_trades)
    stress_metrics = summarize_trades(merged_stress_trades)
    overall_metrics["stress_return"] = stress_metrics["total_return"]
    overall_metrics["stress_sharpe"] = stress_metrics["sharpe_daily"]

    y_all_actual = np.concatenate(all_test_actuals) if all_test_actuals else np.empty(0)
    y_all_pred = np.concatenate(all_test_preds) if all_test_preds else np.empty(0)
    pred_metrics = compute_predictive_metrics(y_all_actual, y_all_pred)
    gate_status = evaluate_gates(overall_metrics, config)

    return ModelRunResult(
        model_name=model_name,
        asset=dataset.asset.value,
        folds=tuple(results),
        trades=merged_trades,
        stress_trades=merged_stress_trades,
        metrics=overall_metrics,
        predictive_metrics=pred_metrics,
        fit_time_seconds=total_fit_time,
        predict_time_seconds=total_predict_time,
        gate_status=gate_status,
        model_ensemble=last_ensemble,
    )
