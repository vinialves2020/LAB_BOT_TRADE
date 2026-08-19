from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from bottrade.config import BacktestConfig
from bottrade.metrics import PerformanceMetrics, calculate_performance, compound_returns
from bottrade.multihorizon import monthly_trade_gate, select_horizon_forecast


class CalibrationEligibilityError(ValueError):
    """No pre-registered threshold passed the calibration activity gates."""


@dataclass(frozen=True, slots=True)
class BacktestResult:
    timeline: pd.DataFrame
    trades: pd.DataFrame
    metrics: PerformanceMetrics
    threshold_return: float
    cost_multiplier: float


@dataclass(frozen=True, slots=True)
class CostAwarePolicy:
    probability_threshold: float
    margin_bps: float
    round_trip_cost: float
    activity: dict[str, float | int | bool]


def select_cost_aware_policy(
    frame: pd.DataFrame,
    expected_gross_returns: dict[int, np.ndarray],
    probabilities: dict[int, np.ndarray],
    config: BacktestConfig,
    *,
    position_size: float = 1.0,
) -> CostAwarePolicy:
    """Select a frozen probability/cost policy on a calibration slice."""

    horizons = tuple(sorted(expected_gross_returns))
    if horizons != tuple(sorted(probabilities)):
        raise ValueError("expected return and probability horizons differ")
    candidates: list[CostAwarePolicy] = []
    for probability_threshold in config.probability_thresholds:
        for margin_bps in config.threshold_margin_bps:
            signals: list[float] = []
            planned_horizons: list[float] = []
            for row in range(len(frame)):
                choice = select_horizon_forecast(
                    horizons=horizons,
                    expected_gross_returns=(expected_gross_returns[h][row] for h in horizons),
                    probabilities=(probabilities[h][row] for h in horizons),
                    round_trip_cost=config.round_trip_cost,
                    probability_threshold=probability_threshold,
                    margin_bps=margin_bps,
                )
                signals.append(1.0 if choice is not None else 0.0)
                planned_horizons.append(float(choice.horizon_hours) if choice else np.nan)
            signal_count = int(np.sum(signals))
            result = simulate_long_flat(
                frame,
                np.asarray(signals, dtype=float),
                threshold_return=0.5,
                cost_per_leg=config.cost_per_leg,
                max_holding_hours=config.max_holding_hours,
                annualization_days=config.annualization_days,
                position_size=position_size,
                selected_horizons=np.asarray(planned_horizons, dtype=float),
            )
            activity = monthly_trade_gate(
                result.trades,
                start_time=frame["as_of"].min() if len(frame) else None,
                end_time=frame["as_of"].max() if len(frame) else None,
            )
            activity["calibration_closed_trades"] = signal_count
            candidates.append(
                CostAwarePolicy(
                    probability_threshold=probability_threshold,
                    margin_bps=float(margin_bps),
                    round_trip_cost=config.round_trip_cost,
                    activity=activity | {"sortino": result.metrics.sortino},
                )
            )
    eligible = [
        item
        for item in candidates
        if int(item.activity.get("calibration_closed_trades", 0))
        >= max(config.minimum_calibration_trades, config.minimum_calibration_trades_per_asset)
        and bool(item.activity.get("passed", False))
        and float(item.activity.get("sortino", -np.inf)) > -np.inf
    ]
    if not eligible:
        raise CalibrationEligibilityError("no cost-aware policy passed calibration")
    return max(
        eligible,
        key=lambda item: (
            float(item.activity.get("sortino", -np.inf)),
            int(item.activity.get("calibration_closed_trades", 0)),
            -item.margin_bps,
        ),
    )


def simulate_long_flat(
    frame: pd.DataFrame,
    predictions: np.ndarray | pd.Series,
    *,
    threshold_return: float,
    cost_per_leg: float,
    max_holding_hours: int,
    annualization_days: int = 365,
    cost_multiplier: float = 1.0,
    position_size: float = 1.0,
    daily_loss_limit: float | None = None,
    position_loss_limit: float | None = None,
    drawdown_circuit_breaker: float | None = None,
    selected_horizons: np.ndarray | pd.Series | None = None,
) -> BacktestResult:
    if len(frame) != len(predictions):
        raise ValueError("predictions and frame must have equal length")
    planned_horizons = (
        np.asarray(selected_horizons, dtype=float)
        if selected_horizons is not None
        else np.full(len(frame), float(max_holding_hours), dtype=float)
    )
    if len(planned_horizons) != len(frame):
        raise ValueError("selected horizons and frame must have equal length")
    data = frame[["as_of", "next_hour_return"]].copy().reset_index(drop=True)
    data["prediction"] = np.asarray(predictions, dtype=float)
    positions: list[float] = []
    strategy_returns: list[float] = []
    transaction_costs: list[float] = []
    risk_states: list[str] = []
    trade_rows: list[dict[str, object]] = []
    position = 0.0
    held = 0
    entry_time: pd.Timestamp | None = None
    trade_growth = 1.0
    trade_cost = 0.0
    planned_holding = float(max_holding_hours)
    turnover = 0.0
    leg_cost = cost_per_leg * cost_multiplier
    if not 0 < position_size <= 1:
        raise ValueError("position_size must be in (0, 1]")
    equity_value = 1.0
    peak_equity = 1.0
    day_start_equity = 1.0
    current_day: object | None = None
    daily_blocked = False
    circuit_breaker = False

    for row in data.itertuples(index=False):
        timestamp = pd.Timestamp(row.as_of)
        if timestamp.date() != current_day:
            current_day = timestamp.date()
            day_start_equity = equity_value
            daily_blocked = False
        drawdown = 1.0 - equity_value / peak_equity if peak_equity > 0 else 1.0
        daily_return = equity_value / day_start_equity - 1.0 if day_start_equity > 0 else -1.0
        if drawdown_circuit_breaker is not None and drawdown >= drawdown_circuit_breaker:
            circuit_breaker = True
        if daily_loss_limit is not None and daily_return <= -daily_loss_limit:
            daily_blocked = True
        position_stopped = bool(
            position > 0
            and position_loss_limit is not None
            and trade_growth - 1.0 - trade_cost <= -position_loss_limit
        )
        desired = position
        reason = "hold"
        if position > 0 and circuit_breaker:
            desired = 0.0
            reason = "drawdown_circuit_breaker"
        elif position > 0 and daily_blocked:
            desired = 0.0
            reason = "daily_loss_exit"
        elif position > 0 and position_stopped:
            desired = 0.0
            reason = "position_loss_exit"
        elif (
            position == 0.0
            and not circuit_breaker
            and not daily_blocked
            and np.isfinite(row.prediction)
            and row.prediction > threshold_return
        ):
            desired = position_size
            reason = "entry_signal"
        elif position > 0.0 and (
            not np.isfinite(row.prediction)
            or row.prediction <= 0.0
            or held >= planned_holding
        ):
            desired = 0.0
            reason = (
                "forecast_exit"
                if not np.isfinite(row.prediction) or row.prediction <= 0
                else "max_holding_exit"
            )

        delta = desired - position
        cost = abs(delta) * leg_cost
        turnover += abs(delta)
        if delta > 0:
            entry_time = pd.Timestamp(row.as_of)
            held = 0
            row_index = len(positions)
            candidate_holding = planned_horizons[row_index]
            planned_holding = (
                max(1.0, float(candidate_holding))
                if np.isfinite(candidate_holding)
                else float(max_holding_hours)
            )
            trade_growth = 1.0
            trade_cost = cost
        hourly_return = desired * float(row.next_hour_return) - cost
        if desired > 0:
            held += 1
            trade_growth *= 1.0 + desired * float(row.next_hour_return)
        if delta < 0 and entry_time is not None:
            trade_cost += cost
            trade_return = trade_growth - 1.0 - trade_cost
            trade_rows.append(
                {
                    "entry_time": entry_time,
                    "exit_time": pd.Timestamp(row.as_of),
                    "return": trade_return,
                    "holding_hours": held,
                    "exit_reason": reason,
                }
            )
            entry_time = None
            held = 0
            trade_growth = 1.0
            trade_cost = 0.0
        positions.append(desired)
        strategy_returns.append(hourly_return)
        transaction_costs.append(cost)
        if circuit_breaker:
            risk_states.append("circuit_breaker")
        elif daily_blocked:
            risk_states.append("daily_stop")
        elif position_stopped:
            risk_states.append("position_stop")
        else:
            risk_states.append("normal")
        equity_value *= max(1.0 + hourly_return, 1e-9)
        peak_equity = max(peak_equity, equity_value)
        position = desired

    if position > 0 and strategy_returns:
        exit_cost = position * leg_cost
        strategy_returns[-1] -= exit_cost
        transaction_costs[-1] += exit_cost
        turnover += position
        trade_return = trade_growth - 1.0 - trade_cost - exit_cost
        trade_rows.append(
            {
                "entry_time": entry_time,
                "exit_time": pd.Timestamp(data.iloc[-1]["as_of"]),
                "return": trade_return,
                "holding_hours": held,
                "exit_reason": "end_of_sample",
            }
        )
        positions[-1] = 0.0

    data["position"] = positions
    data["transaction_cost"] = transaction_costs
    data["strategy_return"] = strategy_returns
    data["risk_state"] = risk_states
    data["equity"] = compound_returns(data["strategy_return"])
    trades = pd.DataFrame(trade_rows)
    metrics = calculate_performance(
        hourly_returns=data["strategy_return"],
        timestamps=data["as_of"],
        positions=data["position"],
        turnover=turnover,
        transaction_cost=float(data["transaction_cost"].sum()),
        trade_returns=trades["return"].tolist() if not trades.empty else [],
        annualization_days=annualization_days,
    )
    return BacktestResult(
        timeline=data,
        trades=trades,
        metrics=metrics,
        threshold_return=threshold_return,
        cost_multiplier=cost_multiplier,
    )


def select_entry_threshold(
    frame: pd.DataFrame,
    predictions: np.ndarray,
    config: BacktestConfig,
    *,
    position_size: float = 1.0,
    daily_loss_limit: float | None = None,
    position_loss_limit: float | None = None,
    drawdown_circuit_breaker: float | None = None,
) -> tuple[float, BacktestResult]:
    candidates = [
        config.round_trip_cost + margin / 10_000 for margin in config.threshold_margin_bps
    ]
    evaluated: list[tuple[float, BacktestResult]] = []
    for threshold in candidates:
        result = simulate_long_flat(
            frame,
            predictions,
            threshold_return=threshold,
            cost_per_leg=config.cost_per_leg,
            max_holding_hours=config.max_holding_hours,
            annualization_days=config.annualization_days,
            position_size=position_size,
            daily_loss_limit=daily_loss_limit,
            position_loss_limit=position_loss_limit,
            drawdown_circuit_breaker=drawdown_circuit_breaker,
        )
        evaluated.append((threshold, result))
    eligible = [
        item
        for item in evaluated
        if item[1].metrics.closed_trades >= config.minimum_calibration_trades
        and item[1].metrics.turnover / max(len(frame) / 24, 1)
        <= config.maximum_calibration_turnover_per_day
    ]
    if not eligible:
        raise CalibrationEligibilityError(
            "no entry threshold satisfies calibration trade-count and turnover constraints"
        )
    return max(
        eligible,
        key=lambda item: (
            item[1].metrics.sortino,
            item[1].metrics.total_return,
            -item[1].metrics.max_drawdown,
        ),
    )
