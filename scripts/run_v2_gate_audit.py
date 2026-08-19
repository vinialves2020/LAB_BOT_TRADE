"""Pre-holdout V2 calibration and activity-gate sensitivity audit.

This script deliberately does not call the promotion/holdout workflow.  It
fits one frozen core configuration per fold, calibrates probabilities on the
chronological calibration slice, and records how alternative diagnostic gates
would change policy eligibility.  The official config is never rewritten.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from sklearn.metrics import brier_score_loss, roc_auc_score

from bottrade.backtest import simulate_long_flat
from bottrade.config import AppConfig, load_config
from bottrade.dataset import DatasetBuilder
from bottrade.domain import Asset, ModelFamily
from bottrade.metrics import calculate_performance
from bottrade.models.multihorizon import MultiHorizonPrediction, MultiHorizonTabularModel
from bottrade.models.transformer_multihorizon import TransformerMultiHorizonModel
from bottrade.multihorizon import SigmoidCalibrator, monthly_trade_gate, select_horizon_forecast
from bottrade.training import ExperimentRunner

GATE_VARIANTS: dict[str, dict[str, float]] = {
    "strict_v2": {
        "minimum_closed_trades": 60,
        "minimum_monthly_trades": 10,
        "minimum_average_monthly_trades": 20,
        "maximum_turnover_per_day": 2,
    },
    "remove_closed_trade_floor": {
        "minimum_closed_trades": 0,
        "minimum_monthly_trades": 10,
        "minimum_average_monthly_trades": 20,
        "maximum_turnover_per_day": 2,
    },
    "remove_monthly_floor": {
        "minimum_closed_trades": 60,
        "minimum_monthly_trades": 0,
        "minimum_average_monthly_trades": 0,
        "maximum_turnover_per_day": 2,
    },
    "relaxed_frequency": {
        "minimum_closed_trades": 30,
        "minimum_monthly_trades": 5,
        "minimum_average_monthly_trades": 10,
        "maximum_turnover_per_day": 2,
    },
    "signal_ceiling": {
        "minimum_closed_trades": 0,
        "minimum_monthly_trades": 0,
        "minimum_average_monthly_trades": 0,
        "maximum_turnover_per_day": 2,
    },
}


def _json_number(value: Any) -> float | int | None:
    if isinstance(value, (np.integer, int)):
        return int(value)
    number = float(value)
    return number if np.isfinite(number) else None


def _ece(probabilities: np.ndarray, labels: np.ndarray, bins: int = 10) -> float:
    values = np.asarray(probabilities, dtype=float)
    targets = np.asarray(labels, dtype=float)
    finite = np.isfinite(values) & np.isfinite(targets)
    values = values[finite]
    targets = targets[finite]
    if not len(values):
        return 0.0
    edges = np.linspace(0.0, 1.0, bins + 1)
    result = 0.0
    for left, right in zip(edges[:-1], edges[1:], strict=True):
        mask = (values >= left) & (values <= right if right == 1 else values < right)
        if mask.any():
            result += float(mask.mean()) * abs(float(values[mask].mean()) - float(targets[mask].mean()))
    return result


def _metrics(result: Any) -> dict[str, float | int | None]:
    return {key: _json_number(value) for key, value in result.metrics.to_dict().items()}


def _prediction_from_transformer(
    regression: np.ndarray,
    probability: np.ndarray,
    horizons: tuple[int, ...],
    volatility: np.ndarray,
) -> MultiHorizonPrediction:
    return MultiHorizonPrediction(
        horizons=horizons,
        normalized_returns={horizon: regression[:, index] for index, horizon in enumerate(horizons)},
        gross_returns={
            horizon: regression[:, index] * volatility for index, horizon in enumerate(horizons)
        },
        probabilities={horizon: probability[:, index] for index, horizon in enumerate(horizons)},
    )


def _policy_result(
    frame: pd.DataFrame,
    prediction: MultiHorizonPrediction,
    probabilities: dict[int, np.ndarray],
    config: AppConfig,
    probability_threshold: float,
    margin_bps: float,
    cost_multiplier: float = 1.0,
) -> Any:
    choices = []
    for row in range(len(frame)):
        choices.append(
            select_horizon_forecast(
                horizons=prediction.horizons,
                expected_gross_returns=(prediction.gross_returns[horizon][row] for horizon in prediction.horizons),
                probabilities=(probabilities[horizon][row] for horizon in prediction.horizons),
                round_trip_cost=config.backtest.round_trip_cost * cost_multiplier,
                probability_threshold=probability_threshold,
                margin_bps=margin_bps,
            )
        )
    gross = np.asarray([choice.expected_gross_return if choice else 0.0 for choice in choices])
    selected_horizons = np.asarray(
        [choice.horizon_hours if choice else np.nan for choice in choices], dtype=float
    )
    return simulate_long_flat(
        frame,
        gross,
        threshold_return=(
            config.backtest.round_trip_cost * cost_multiplier + margin_bps / 10_000.0
        ),
        cost_per_leg=config.backtest.cost_per_leg,
        max_holding_hours=config.backtest.max_holding_hours,
        annualization_days=config.backtest.annualization_days,
        cost_multiplier=cost_multiplier,
        position_size=config.paper.max_asset_weight,
        daily_loss_limit=config.paper.daily_loss_limit,
        position_loss_limit=config.paper.position_loss_limit,
        drawdown_circuit_breaker=config.paper.drawdown_circuit_breaker,
        selected_horizons=selected_horizons,
    )


def _select_policy(
    frame: pd.DataFrame,
    prediction: MultiHorizonPrediction,
    probabilities: dict[int, np.ndarray],
    config: AppConfig,
    gate: dict[str, float],
) -> dict[str, Any]:
    candidates: list[tuple[float, float, Any, dict[str, Any]]] = []
    for probability_threshold in config.training.probability_thresholds:
        for margin_bps in config.backtest.threshold_margin_bps:
            result = _policy_result(
                frame,
                prediction,
                probabilities,
                config,
                float(probability_threshold),
                float(margin_bps),
            )
            turnover_per_day = result.metrics.turnover / max(len(frame) / 24.0, 1.0)
            activity = monthly_trade_gate(
                result.trades,
                start_time=frame["as_of"].min(),
                end_time=frame["as_of"].max(),
                minimum_average=int(gate["minimum_average_monthly_trades"]),
                minimum_month=int(gate["minimum_monthly_trades"]),
            )
            activity = {
                **activity,
                "turnover_per_day": _json_number(turnover_per_day),
                "calibration_closed_trades": int(result.metrics.closed_trades),
            }
            if (
                result.metrics.closed_trades >= int(gate["minimum_closed_trades"])
                and turnover_per_day <= float(gate["maximum_turnover_per_day"])
                and bool(activity["passed"])
            ):
                candidates.append((float(probability_threshold), float(margin_bps), result, activity))
    if not candidates:
        return {"eligible": False}
    probability_threshold, margin_bps, result, activity = max(
        candidates,
        key=lambda item: (
            float(item[2].metrics.sortino),
            float(item[2].metrics.total_return),
            -float(item[2].metrics.max_drawdown),
        ),
    )
    return {
        "eligible": True,
        "probability_threshold": probability_threshold,
        "margin_bps": margin_bps,
        "calibration_metrics": _metrics(result),
        "calibration_activity": activity,
    }


def _aggregate_test_results(results: list[Any], config: AppConfig) -> dict[str, Any] | None:
    if not results:
        return None
    timeline = pd.concat([result.timeline for result in results], ignore_index=True)
    trade_frames = [result.trades for result in results if not result.trades.empty]
    trades = (
        pd.concat(trade_frames, ignore_index=True)
        if trade_frames
        else pd.DataFrame(columns=["return"])
    )
    metrics = calculate_performance(
        hourly_returns=timeline["strategy_return"],
        timestamps=timeline["as_of"],
        positions=timeline["position"],
        turnover=float(sum(result.metrics.turnover for result in results)),
        transaction_cost=float(sum(result.metrics.transaction_cost for result in results)),
        trade_returns=trades["return"].tolist() if not trades.empty else [],
        annualization_days=config.backtest.annualization_days,
    )
    return metrics.to_dict()


def _probability_summary(records: dict[int, list[dict[str, np.ndarray]]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for horizon, chunks in records.items():
        raw = np.concatenate([item["raw"] for item in chunks])
        calibrated = np.concatenate([item["calibrated"] for item in chunks])
        labels = np.concatenate([item["labels"] for item in chunks])
        output[str(horizon)] = {
            "samples": int(len(labels)),
            "label_rate": _json_number(labels.mean()),
            "raw_mean": _json_number(raw.mean()),
            "raw_std": _json_number(raw.std()),
            "calibrated_mean": _json_number(calibrated.mean()),
            "calibrated_std": _json_number(calibrated.std()),
            "calibrated_brier": _json_number(brier_score_loss(labels, calibrated)),
            "calibrated_auc": _json_number(
                roc_auc_score(labels, calibrated) if np.unique(labels).size > 1 else 0.5
            ),
            "calibrated_ece": _json_number(_ece(calibrated, labels)),
        }
    return output


def run_asset_family(
    config: AppConfig,
    asset: Asset,
    family: ModelFamily,
    *,
    max_folds: int | None,
) -> dict[str, Any]:
    dataset = DatasetBuilder(config).load(asset, config.training.frozen_core_arm)
    runner = ExperimentRunner(config)
    folds = runner._folds(dataset.frame, phase="development", max_folds=max_folds)
    params_path = (
        config.project.artifact_dir
        / "experiments"
        / asset.value
        / config.training.frozen_core_arm
        / family.value
        / "best_params.json"
    )
    if not params_path.exists():
        raise FileNotFoundError(f"frozen core params missing: {params_path}")
    params = json.loads(params_path.read_text(encoding="utf-8"))
    frame = dataset.frame
    x = frame.loc[:, dataset.feature_columns].to_numpy(dtype=np.float64)
    x[~np.isfinite(x)] = np.nan
    horizons = tuple(config.features.forecast_horizons)
    probability_records: dict[int, list[dict[str, np.ndarray]]] = {horizon: [] for horizon in horizons}
    gate_records = {
        name: {"eligible_folds": 0, "folds": [], "test_results": []}
        for name in GATE_VARIANTS
    }
    fold_summaries: list[dict[str, Any]] = []

    for fold_number, fold in enumerate(folds, 1):
        print(f"{asset.value} {family.value} fold {fold_number}/{len(folds)} {fold.name}", flush=True)
        if family in {ModelFamily.RANDOM_FOREST, ModelFamily.HIST_GRADIENT_BOOSTING}:
            model = MultiHorizonTabularModel(
                family=family,
                params=params,
                horizons=horizons,
                seed=config.training.seeds[0],
            )
            model.fit(x, frame, fold.train_indices)
            cal_frame = frame.iloc[fold.calibration_indices].reset_index(drop=True)
            test_frame = frame.iloc[fold.test_indices].reset_index(drop=True)
            cal_prediction = model.predict(
                x,
                fold.calibration_indices,
                cal_frame["target_volatility"].to_numpy(dtype=float),
            )
            test_prediction = model.predict(
                x,
                fold.test_indices,
                test_frame["target_volatility"].to_numpy(dtype=float),
            )
        else:
            regression_targets = np.column_stack(
                [frame[f"target_normalized_return_{horizon}h"] for horizon in horizons]
            ).astype(float)
            classification_targets = np.column_stack(
                [frame[f"label_tradeable_{horizon}h"] for horizon in horizons]
            ).astype(float)
            model = TransformerMultiHorizonModel(
                n_features=x.shape[1],
                sequence_length=config.features.lookback_hours,
                horizons=horizons,
                params=params,
                seed=config.training.seeds[0],
                calendar_hour_index=(
                    dataset.feature_columns.index("calendar_hour_index")
                    if "calendar_hour_index" in dataset.feature_columns
                    else None
                ),
                calendar_day_index=(
                    dataset.feature_columns.index("calendar_day_index")
                    if "calendar_day_index" in dataset.feature_columns
                    else None
                ),
            )
            model.fit(x, regression_targets, classification_targets, fold.train_indices)
            cal_indices = fold.calibration_indices
            test_indices = fold.test_indices
            cal_regression, cal_probability = model.predict(x, cal_indices)
            test_regression, test_probability = model.predict(x, test_indices)
            cal_frame = frame.iloc[cal_indices].reset_index(drop=True)
            test_frame = frame.iloc[test_indices].reset_index(drop=True)
            cal_prediction = _prediction_from_transformer(
                cal_regression,
                cal_probability,
                horizons,
                cal_frame["target_volatility"].to_numpy(dtype=float),
            )
            test_prediction = _prediction_from_transformer(
                test_regression,
                test_probability,
                horizons,
                test_frame["target_volatility"].to_numpy(dtype=float),
            )

        calibration_probabilities: dict[int, np.ndarray] = {}
        test_probabilities: dict[int, np.ndarray] = {}
        for horizon in horizons:
            labels = cal_frame[f"label_tradeable_{horizon}h"].to_numpy(dtype=float)
            calibrator = SigmoidCalibrator().fit(cal_prediction.probabilities[horizon], labels)
            calibration_probabilities[horizon] = calibrator.predict(cal_prediction.probabilities[horizon])
            test_probabilities[horizon] = calibrator.predict(test_prediction.probabilities[horizon])
            # Report calibration on the untouched test slice.  The sigmoid is
            # fitted only on ``cal_frame`` above; its test metrics therefore
            # remain genuinely out-of-sample for this fold.
            probability_records[horizon].append(
                {
                    "raw": test_prediction.probabilities[horizon],
                    "calibrated": test_probabilities[horizon],
                    "labels": test_frame[f"label_tradeable_{horizon}h"].to_numpy(dtype=float),
                }
            )

        fold_summary: dict[str, Any] = {"fold": fold.name, "gates": {}}
        for gate_name, gate in GATE_VARIANTS.items():
            selected = _select_policy(
                cal_frame,
                cal_prediction,
                calibration_probabilities,
                config,
                gate,
            )
            if selected["eligible"]:
                test = _policy_result(
                    test_frame,
                    test_prediction,
                    test_probabilities,
                    config,
                    float(selected["probability_threshold"]),
                    float(selected["margin_bps"]),
                )
                stress = _policy_result(
                    test_frame,
                    test_prediction,
                    test_probabilities,
                    config,
                    float(selected["probability_threshold"]),
                    float(selected["margin_bps"]),
                    cost_multiplier=config.backtest.stress_multiplier,
                )
                gate_records[gate_name]["eligible_folds"] += 1
                gate_records[gate_name]["test_results"].append(test)
                selected["test_metrics"] = _metrics(test)
                selected["stress_metrics"] = _metrics(stress)
            gate_records[gate_name]["folds"].append(selected)
            fold_summary["gates"][gate_name] = {
                key: value
                for key, value in selected.items()
                if key
                in {
                    "eligible",
                    "probability_threshold",
                    "margin_bps",
                    "calibration_metrics",
                    "calibration_activity",
                }
            }
        fold_summaries.append(fold_summary)

    gate_output: dict[str, Any] = {}
    for gate_name, record in gate_records.items():
        eligible = [item for item in record["folds"] if item.get("eligible")]
        test_metrics = _aggregate_test_results(record["test_results"], config)
        stress_results = []
        for item in eligible:
            # Stress metrics are kept at fold level; aggregate timelines are not
            # retained twice to keep the audit artifact small.
            stress_results.append(item.get("stress_metrics"))
        gate_output[gate_name] = {
            "gate": GATE_VARIANTS[gate_name],
            "fold_count": len(record["folds"]),
            "eligible_folds": int(record["eligible_folds"]),
            "eligible_fraction": _json_number(record["eligible_folds"] / max(len(record["folds"]), 1)),
            "selected_probability_thresholds": [item.get("probability_threshold") for item in eligible],
            "selected_margin_bps": [item.get("margin_bps") for item in eligible],
            "calibration_closed_trades": [
                item["calibration_activity"].get("calibration_closed_trades") for item in eligible
            ],
            "test_metrics": test_metrics,
            "stress_fold_metrics": stress_results,
        }
    return {
        "asset": asset.value,
        "family": family.value,
        "arm": config.training.frozen_core_arm,
        "fold_count": len(folds),
        "holdout_opened": False,
        "params": params,
        "probability_calibration": _probability_summary(probability_records),
        "gates": gate_output,
        "folds": fold_summaries,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/v2.yaml")
    parser.add_argument("--family", choices=[item.value for item in ModelFamily], default="hist_gradient_boosting")
    parser.add_argument("--asset", choices=[item.value for item in Asset], default=None)
    parser.add_argument("--max-folds", type=int, default=None)
    parser.add_argument("--output", default="artifacts/logs/v2_gate_audit.json")
    args = parser.parse_args()
    config = load_config(args.config)
    family = ModelFamily(args.family)
    results: list[dict[str, Any]] = []
    started = time.time()
    assets = [Asset(args.asset)] if args.asset else list(Asset)
    for asset in assets:
        results.append(run_asset_family(config, asset, family, max_folds=args.max_folds))
    payload = {
        "protocol_version": config.training.protocol_version,
        "holdout_start": str(config.training.holdout_start),
        "holdout_end": str(config.training.holdout_end),
        "holdout_opened": False,
        "family": family.value,
        "gate_variants": GATE_VARIANTS,
        "max_folds": args.max_folds,
        "elapsed_seconds": time.time() - started,
        "results": results,
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True, default=str), encoding="utf-8")
    print(json.dumps({"output": str(output), "family": family.value, "elapsed_seconds": payload["elapsed_seconds"]}))


if __name__ == "__main__":
    main()
