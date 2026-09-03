from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

import numpy as np
import pandas as pd

from bottrade.v4.config import V4Config
from bottrade.v4.features import DirectDataset
from bottrade.v4.model import XGBEnsemble
from bottrade.validation import require_minimum_folds, walk_forward_folds


@dataclass(frozen=True, slots=True)
class Policy:
    margin_bps: int

    @property
    def threshold_log_return(self) -> float:
        return float(np.log1p((24.0 + self.margin_bps) / 10_000.0))


@dataclass(frozen=True, slots=True)
class FoldResult:
    name: str
    policy: Policy
    metrics: dict[str, float | int]
    seed_metrics: dict[str, dict[str, float | int]]
    calibration: dict[str, float | int]
    trades: pd.DataFrame


@dataclass(frozen=True, slots=True)
class WalkForwardResult:
    asset: str
    folds: tuple[FoldResult, ...]
    trades: pd.DataFrame
    metrics: dict[str, float | int]
    feature_importance: dict[str, float] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class ReturnCalibrator:
    """Chronological affine calibration for a return forecast."""

    intercept: float
    slope: float

    def transform(self, values: np.ndarray) -> np.ndarray:
        return self.intercept + self.slope * np.asarray(values, dtype=float)


def fit_return_calibrator(predictions: np.ndarray, targets: np.ndarray) -> ReturnCalibrator:
    """Fit a monotone calibration only on past out-of-sample predictions."""

    x = np.asarray(predictions, dtype=float)
    y = np.asarray(targets, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    if int(mask.sum()) < 20:
        return ReturnCalibrator(intercept=0.0, slope=1.0)
    x_valid = x[mask]
    y_valid = y[mask]
    variance = float(np.var(x_valid))
    if variance <= 1e-12:
        return ReturnCalibrator(intercept=float(np.mean(y_valid)), slope=0.0)
    slope = float(np.cov(x_valid, y_valid, ddof=0)[0, 1] / variance)
    intercept = float(np.mean(y_valid) - slope * np.mean(x_valid))
    # Never invert a model after seeing calibration.  A negative slope means
    # this candidate has no monotone edge and must naturally stop trading.
    return ReturnCalibrator(intercept=intercept, slope=max(0.0, slope))


def _daily_returns(trades: pd.DataFrame) -> pd.Series:
    if trades.empty:
        return pd.Series(dtype=float)
    values = trades.copy()
    values["exit_time"] = pd.to_datetime(values["exit_time"], utc=True)
    return values.groupby(values["exit_time"].dt.floor("D"))["net_return"].sum()


def summarize_trades(trades: pd.DataFrame) -> dict[str, float | int]:
    if trades.empty:
        return {
            "closed_trades": 0,
            "total_return": 0.0,
            "sharpe_daily": 0.0,
            "sortino_daily": 0.0,
            "maximum_drawdown": 0.0,
            "profit_factor": 0.0,
            "turnover_round_trips": 0,
            "average_monthly_trades": 0.0,
        }
    returns = pd.to_numeric(trades["net_return"], errors="coerce").dropna()
    daily = _daily_returns(trades)
    mean = float(daily.mean()) if len(daily) else 0.0
    std = float(daily.std(ddof=1)) if len(daily) > 1 else 0.0
    downside = daily[daily < 0.0]
    downside_std = float(np.sqrt(np.mean(np.square(downside)))) if len(downside) else 0.0
    sharpe = mean / std * np.sqrt(365.0) if std > 0 else 0.0
    sortino = mean / downside_std * np.sqrt(365.0) if downside_std > 0 else (0.0 if mean <= 0 else float("inf"))
    equity = (1.0 + returns).cumprod()
    drawdown = equity / equity.cummax() - 1.0
    positive = float(returns[returns > 0].sum())
    negative = float(-returns[returns < 0].sum())
    exit_dates = pd.to_datetime(trades["exit_time"], utc=True).dt.tz_localize(None)
    months = exit_dates.dt.to_period("M").nunique()
    return {
        "closed_trades": int(len(returns)),
        "total_return": float(equity.iloc[-1] - 1.0),
        "sharpe_daily": float(sharpe),
        "sortino_daily": float(sortino),
        "maximum_drawdown": float(-drawdown.min()),
        "profit_factor": float(positive / negative) if negative > 0 else (float("inf") if positive > 0 else 0.0),
        "turnover_round_trips": int(len(returns)),
        "average_monthly_trades": float(len(returns) / months) if months else 0.0,
    }


def select_stateful_trades(
    frame: pd.DataFrame,
    predictions: np.ndarray,
    deviations: np.ndarray,
    *,
    config: V4Config,
    policy: Policy,
    cost_multiplier: float = 1.0,
) -> pd.DataFrame:
    """Simulate a one-hour forecast with a persistent long/flat position."""

    if len(frame) != len(predictions) or len(frame) != len(deviations):
        raise ValueError("prediction arrays must align with the frame")
    data = frame.copy().sort_values("as_of").reset_index(drop=True)
    data["prediction"] = np.asarray(predictions, dtype=float)
    data["prediction_std"] = np.asarray(deviations, dtype=float)
    data["as_of"] = pd.to_datetime(data["as_of"], utc=True)
    data["entry_time"] = pd.to_datetime(data["entry_time"], utc=True)
    data["exit_time"] = pd.to_datetime(data["exit_time"], utc=True)
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
                "margin_bps": policy.margin_bps,
            }
        )
        position = None

    for row in data.itertuples(index=False):
        entry_time = pd.Timestamp(row.entry_time)
        prediction = float(row.prediction)
        deviation = float(row.prediction_std)
        effective = prediction - config.uncertainty_std_multiplier * deviation
        valid = bool(row.label_valid) and np.isfinite(float(row.entry_price))
        if position is not None:
            current_price = float(row.entry_price)
            position["peak_price"] = max(float(position.get("peak_price", position["entry_price"])), current_price)
            entry_p = float(position["entry_price"])
            current_gross = current_price / entry_p - 1.0 if entry_p > 0 else 0.0
            peak_gross = float(position["peak_price"]) / entry_p - 1.0 if entry_p > 0 else 0.0
            held_hours = (entry_time - pd.Timestamp(position["entry_time"])).total_seconds() / 3600.0
            vol_1h = float(getattr(row, "ewma_volatility_1h", 0.008))
            if not np.isfinite(vol_1h) or vol_1h <= 0:
                vol_1h = 0.008
            trailing_stop = peak_gross >= (2.0 * vol_1h) and current_gross <= (peak_gross * 0.50)
            hard_stop = current_gross <= (-3.0 * vol_1h)

            should_exit = (
                not valid
                or held_hours >= config.max_holding_hours
                or effective < -threshold
                or (config.exit_on_non_positive and effective <= 0.0)
                or trailing_stop
                or hard_stop
            )
            if should_exit:
                close_position(entry_time, float(row.entry_price), prediction)
                # Do not reverse/open again on the same candle.  This keeps a
                # close and a new entry from becoming an artificial round trip.
                continue

        vol_ratio = getattr(row, "volatility_ratio_6h_168h", 1.0)
        vol_compressed = np.isfinite(vol_ratio) and float(vol_ratio) < 0.65

        # Macro BTC Trend Filter: if trading an altcoin and BTC is in a sharp 24h drop (< -1.8%), avoid buying
        btc_24h = getattr(row, "ctx_BTCUSDT_return_24h", None)
        btc_dumping = btc_24h is not None and np.isfinite(float(btc_24h)) and float(btc_24h) < -0.018

        # Altcoin structural downtrend filter: if asset is > 2% below its 168h weekly EMA and BTC is negative
        own_ema_168 = getattr(row, "close_to_ema_168h", 0.0)
        own_in_downtrend = (
            btc_24h is not None
            and np.isfinite(float(own_ema_168))
            and float(own_ema_168) < -0.020
            and float(btc_24h) < 0.0
        )

        # Turbulent chop filter: when market is in a sideways range (within 2% of 72h EMA and vol_ratio >= 0.95),
        # only allow entry if confirmed by positive taker CVD (cvd_ratio_6h > 0.02)
        has_chop_cols = hasattr(row, "close_to_ema_72h") and hasattr(row, "cvd_ratio_6h")
        if has_chop_cols:
            close_to_ema_72 = row.close_to_ema_72h
            cvd_6h = row.cvd_ratio_6h
            in_sideways_range = (
                np.isfinite(close_to_ema_72)
                and abs(float(close_to_ema_72)) < 0.020
                and np.isfinite(vol_ratio)
                and float(vol_ratio) >= 0.95
            )
            cvd_confirmed = np.isfinite(cvd_6h) and float(cvd_6h) > 0.02
            turbulent_chop = in_sideways_range and not cvd_confirmed
        else:
            turbulent_chop = False

        # Solana specific regime protection:
        # Solana is a high-beta momentum asset that gets severely chopped in sideways drift.
        # Require SOL to only enter when there is directional trend (outside +/- 2.5% of 72h EMA).
        current_asset = str(getattr(row, "asset", ""))
        if current_asset == "SOLUSDT" and hasattr(row, "close_to_ema_72h"):
            close_to_ema_72 = row.close_to_ema_72h
            sol_sideways_filter = (
                np.isfinite(close_to_ema_72)
                and abs(float(close_to_ema_72)) < 0.025
            )
        else:
            sol_sideways_filter = False

        entry_allowed = (
            not vol_compressed
            and not btc_dumping
            and not own_in_downtrend
            and not turbulent_chop
            and not sol_sideways_filter
        )

        if position is None and valid and effective > threshold and entry_allowed:
            day = entry_time.date()
            if daily_entries.get(day, 0) < config.max_round_trips_per_asset_day:
                position = {
                    "as_of": row.as_of,
                    "entry_time": entry_time,
                    "entry_price": float(row.entry_price),
                    "peak_price": float(row.entry_price),
                    "prediction": prediction,
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


def select_trades(
    frame: pd.DataFrame,
    predictions: np.ndarray,
    deviations: np.ndarray,
    *,
    config: V4Config,
    policy: Policy,
    cost_multiplier: float = 1.0,
) -> pd.DataFrame:
    """Apply the cost gate and the one-position/no-overlap rules."""

    if config.stateful_hourly:
        return select_stateful_trades(
            frame,
            predictions,
            deviations,
            config=config,
            policy=policy,
            cost_multiplier=cost_multiplier,
        )

    if len(frame) != len(predictions) or len(frame) != len(deviations):
        raise ValueError("prediction arrays must align with the frame")
    data = frame.copy()
    data["prediction"] = np.asarray(predictions, dtype=float)
    data["prediction_std"] = np.asarray(deviations, dtype=float)
    threshold = np.log1p(
        (config.round_trip_bps * cost_multiplier + policy.margin_bps) / 10_000.0
    )
    effective = data["prediction"] - config.uncertainty_std_multiplier * data["prediction_std"]
    data = data[
        data["label_valid"].astype(bool)
        & np.isfinite(data["prediction"])
        & effective.gt(threshold)
    ].copy()
    if data.empty:
        return data.assign(net_return=pd.Series(dtype=float))
    data["as_of"] = pd.to_datetime(data["as_of"], utc=True)
    data["entry_time"] = pd.to_datetime(data["entry_time"], utc=True)
    data["exit_time"] = pd.to_datetime(data["exit_time"], utc=True)
    data = data.sort_values("as_of").reset_index(drop=True)
    selected: list[pd.Series] = []
    last_exit: pd.Timestamp | None = None
    daily_count: dict[object, int] = {}
    for _, row in data.iterrows():
        entry = pd.Timestamp(row["entry_time"])
        if last_exit is not None and entry < last_exit:
            continue
        day = entry.date()
        if daily_count.get(day, 0) >= config.max_round_trips_per_asset_day:
            continue
        selected.append(row)
        last_exit = pd.Timestamp(row["exit_time"])
        daily_count[day] = daily_count.get(day, 0) + 1
    if not selected:
        return data.iloc[0:0].copy().assign(net_return=pd.Series(dtype=float))
    result = pd.DataFrame(selected).reset_index(drop=True)
    result["net_return"] = pd.to_numeric(result["gross_return"], errors="coerce") - (
        config.round_trip_bps * cost_multiplier / 10_000.0
    )
    return result


def choose_policy(
    frame: pd.DataFrame,
    predictions: np.ndarray,
    deviations: np.ndarray,
    *,
    config: V4Config,
) -> tuple[Policy, dict[str, Any]]:
    candidates: list[tuple[float, Policy, dict[str, float | int], pd.DataFrame]] = []
    for margin in config.entry_margins_bps:
        policy = Policy(int(margin))
        trades = select_trades(
            frame,
            predictions,
            deviations,
            config=config,
            policy=policy,
            cost_multiplier=1.0,
        )
        metrics = summarize_trades(trades)
        if int(metrics["closed_trades"]) < config.minimum_calibration_trades:
            continue
        score = float(metrics["sortino_daily"])
        if not np.isfinite(score):
            score = 1e9 if float(metrics["total_return"]) > 0 else -1e9
        candidates.append((score, policy, metrics, trades))
    if not candidates:
        # A rejected calibration must remain visible in the report; it must not
        # silently lower the threshold until trades appear.
        fallback = Policy(max(config.entry_margins_bps))
        return fallback, {"status": "insufficient_calibration_trades", "trades": 0}
    _, policy, metrics, trades = max(candidates, key=lambda item: (item[0], -item[1].margin_bps))
    return policy, {"status": "selected", "metrics": metrics, "trades": int(len(trades))}


def _valid_frame(dataset: DirectDataset) -> pd.DataFrame:
    frame = dataset.frame.copy().sort_values("as_of").reset_index(drop=True)
    valid = frame["label_valid"].astype(bool) & np.isfinite(frame[dataset.target_column])
    return frame.loc[valid].reset_index(drop=True)


def run_walk_forward(
    dataset: DirectDataset,
    *,
    config: V4Config,
    params: dict[str, Any] | None = None,
    max_folds: int | None = None,
    seeds_override: tuple[int, ...] | None = None,
    fold_selection: Literal["last", "first"] = "last",
    evaluation_split: Literal["test", "calibration"] = "test",
) -> WalkForwardResult:
    frame = _valid_frame(dataset)
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
    elif max_folds < 1:
        raise ValueError("max_folds must be positive")
    if fold_selection not in {"last", "first"}:
        raise ValueError("fold_selection must be 'last' or 'first'")
    if evaluation_split not in {"test", "calibration"}:
        raise ValueError("evaluation_split must be 'test' or 'calibration'")
    if max_folds is None:
        selected_folds = folds
    elif fold_selection == "first":
        selected_folds = folds[:max_folds]
    else:
        selected_folds = folds[-max_folds:]
    x = frame[list(dataset.feature_columns)].to_numpy(dtype=np.float32)
    y = frame[dataset.target_column].to_numpy(dtype=np.float32)
    results: list[FoldResult] = []
    all_trades: list[pd.DataFrame] = []
    all_stress_trades: list[pd.DataFrame] = []
    importance: dict[str, list[float]] = {name: [] for name in dataset.feature_columns}
    for fold in selected_folds:
        ensemble = XGBEnsemble.create(
            config=config,
            feature_names=dataset.feature_columns,
            params=params,
            seeds=seeds_override,
        )
        ensemble.fit(x, y, fold.train_indices)
        calibration_mean, calibration_std = ensemble.predict_summary(x, fold.calibration_indices)
        calibration_frame = frame.iloc[fold.calibration_indices].reset_index(drop=True)
        calibrator = (
            fit_return_calibrator(
                calibration_mean,
                calibration_frame[dataset.target_column].to_numpy(dtype=float),
            )
            if config.calibrate_return_scale
            else ReturnCalibrator(intercept=0.0, slope=1.0)
        )
        calibration_mean = calibrator.transform(calibration_mean)
        calibration_std = np.abs(calibrator.slope) * calibration_std
        policy, _ = choose_policy(
            calibration_frame,
            calibration_mean,
            calibration_std,
            config=config,
        )
        test_mean, test_std = ensemble.predict_summary(x, fold.test_indices)
        test_mean = calibrator.transform(test_mean)
        test_std = np.abs(calibrator.slope) * test_std
        test_frame = frame.iloc[fold.test_indices].reset_index(drop=True)
        if evaluation_split == "calibration":
            evaluation_mean = calibration_mean
            evaluation_std = calibration_std
            evaluation_frame = calibration_frame
            evaluation_indices = fold.calibration_indices
        else:
            evaluation_mean = test_mean
            evaluation_std = test_std
            evaluation_frame = test_frame
            evaluation_indices = fold.test_indices
        trades = select_trades(
            evaluation_frame,
            evaluation_mean,
            evaluation_std,
            config=config,
            policy=policy,
            cost_multiplier=1.0,
        )
        metrics = summarize_trades(trades)
        stress_trades = select_trades(
            evaluation_frame,
            evaluation_mean,
            evaluation_std,
            config=config,
            policy=policy,
            cost_multiplier=config.stress_multiplier,
        )
        metrics.update(
            {f"stress_{key}": value for key, value in summarize_trades(stress_trades).items()}
        )
        seed_metrics: dict[str, dict[str, float | int]] = {}
        member_predictions = ensemble.predict_members(x, evaluation_indices)
        for seed, member_prediction in zip(ensemble.seeds, member_predictions, strict=True):
            member_prediction = calibrator.transform(member_prediction)
            member_trades = select_trades(
                evaluation_frame,
                member_prediction,
                np.zeros(len(member_prediction), dtype=float),
                config=config,
                policy=policy,
                cost_multiplier=1.0,
            )
            seed_metrics[str(seed)] = summarize_trades(member_trades)
        results.append(
            FoldResult(
                fold.name,
                policy,
                metrics,
                seed_metrics,
                {"intercept": calibrator.intercept, "slope": calibrator.slope},
                trades,
            )
        )
        if not trades.empty:
            all_trades.append(trades.assign(fold=fold.name, margin_bps=policy.margin_bps))
        if not stress_trades.empty:
            all_stress_trades.append(
                stress_trades.assign(fold=fold.name, margin_bps=policy.margin_bps)
            )
        for name, value in ensemble.feature_importance().items():
            importance[name].append(value)
    combined = pd.concat(all_trades, ignore_index=True) if all_trades else pd.DataFrame()
    stress_combined = (
        pd.concat(all_stress_trades, ignore_index=True) if all_stress_trades else pd.DataFrame()
    )
    metrics = summarize_trades(combined)
    metrics.update(
        {f"stress_{key}": value for key, value in summarize_trades(stress_combined).items()}
    )
    averaged_importance = {
        name: float(np.mean(values)) for name, values in importance.items() if values
    }
    return WalkForwardResult(
        asset=dataset.asset.value,
        folds=tuple(results),
        trades=combined,
        metrics=metrics,
        feature_importance=dict(
            sorted(averaged_importance.items(), key=lambda item: item[1], reverse=True)
        ),
    )
