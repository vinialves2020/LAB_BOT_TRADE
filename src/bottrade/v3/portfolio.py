from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from bottrade.v3.config import V3Config
from bottrade.v3.statistics import summarize_returns


@dataclass(frozen=True, slots=True)
class PortfolioBacktestResult:
    ledger_name: str
    initial_cash: float
    trades: pd.DataFrame
    timeline: pd.DataFrame
    metrics: dict[str, float | int]


def inverse_volatility_weights(
    rows: pd.DataFrame,
    *,
    max_asset_weight: float,
    max_gross_weight: float,
) -> pd.Series:
    if rows.empty:
        return pd.Series(dtype=float)
    volatility = pd.to_numeric(rows["ewma_volatility_1h"], errors="coerce").clip(lower=1e-8)
    inverse = 1.0 / volatility
    weights = inverse / inverse.sum() * max_gross_weight
    weights = weights.clip(upper=max_asset_weight)
    total = float(weights.sum())
    if total > max_gross_weight:
        weights *= max_gross_weight / total
    return weights


def _candidate_return(row: pd.Series, multiplier: float) -> float:
    column = f"net_return_{int(multiplier)}x"
    if column in row and pd.notna(row[column]):
        return float(row[column])
    return float(row.get("net_return", 0.0))


def portfolio_backtest(
    decisions: pd.DataFrame,
    *,
    config: V3Config,
    ledger_name: str = "paper_500",
    initial_cash: float = 500.0,
    cost_multiplier: float = 1.0,
) -> PortfolioBacktestResult:
    """Replay approved event decisions with portfolio caps and risk stops."""

    if decisions.empty:
        empty = pd.DataFrame(columns=["as_of", "strategy_return"])
        return PortfolioBacktestResult(ledger_name, initial_cash, pd.DataFrame(), empty, summarize_returns([], [], []))
    data = decisions.copy()
    if "approved" in data:
        data = data[data["approved"].astype(bool)].copy()
    required = {"asset", "entry_time", "exit_time", "ewma_volatility_1h"}
    if not required.issubset(data.columns):
        raise ValueError(f"portfolio decisions missing columns: {sorted(required - set(data.columns))}")
    data["entry_time"] = pd.to_datetime(data["entry_time"], utc=True)
    data["exit_time"] = pd.to_datetime(data["exit_time"], utc=True)
    data = data.sort_values(["entry_time", "expected_net_return"], ascending=[True, False])
    active: dict[str, pd.Timestamp] = {}
    active_weights: dict[str, float] = {}
    daily_entries: dict[tuple[str, object], int] = {}
    equity = 1.0
    peak = 1.0
    day_start = 1.0
    current_day: object | None = None
    circuit_breaker = False
    accepted: list[dict[str, object]] = []
    for timestamp, group in data.groupby("entry_time", sort=True):
        timestamp = pd.Timestamp(timestamp)
        # Realize positions that ended at or before this event before applying
        # the next signal.  This keeps same-asset entries from being blocked
        # by stale state after a timeout/stop event.
        for asset in list(active):
            if active[asset] <= timestamp:
                active.pop(asset, None)
                active_weights.pop(asset, None)
        day = timestamp.date()
        if day != current_day:
            current_day = day
            day_start = equity
        drawdown = 1.0 - equity / peak if peak > 0 else 1.0
        if drawdown >= config.drawdown_circuit_breaker:
            circuit_breaker = True
        day_return = equity / day_start - 1.0 if day_start > 0 else -1.0
        if circuit_breaker or day_return <= -config.daily_loss_limit:
            continue
        group = group.sort_values("expected_net_return", ascending=False).drop_duplicates("asset")
        available = group[~group["asset"].astype(str).isin(active.keys())].copy()
        if available.empty:
            continue
        eligible_rows: list[pd.Series] = []
        for _, row in available.iterrows():
            key = (str(row["asset"]), day)
            if daily_entries.get(key, 0) >= config.maximum_round_trips_per_asset_day:
                continue
            eligible_rows.append(row)
        if not eligible_rows:
            continue
        eligible = pd.DataFrame(eligible_rows)
        weights = inverse_volatility_weights(
            eligible,
            max_asset_weight=config.max_asset_weight,
            max_gross_weight=config.max_gross_weight,
        )
        free_gross = max(0.0, config.max_gross_weight - sum(active_weights.values()))
        if float(weights.sum()) > free_gross and float(weights.sum()) > 0:
            weights *= free_gross / float(weights.sum())
        group_return = 0.0
        for index, row in eligible.iterrows():
            weight = float(weights.loc[index])
            if weight <= 0:
                continue
            asset = str(row["asset"])
            entry = pd.Timestamp(row["entry_time"])
            exit_time = pd.Timestamp(row["exit_time"])
            net_return = _candidate_return(row, cost_multiplier)
            weighted_return = weight * net_return
            risk_exit = False
            if weighted_return <= -config.position_loss_limit:
                weighted_return = -config.position_loss_limit
                risk_exit = True
            accepted.append(
                {
                    "candidate_id": row.get("candidate_id", ""),
                    "asset": asset,
                    "entry_time": entry,
                    "exit_time": exit_time,
                    "weight": weight,
                    "gross_return": float(row.get("gross_return", net_return)),
                    "net_return": net_return,
                    "weighted_return": weighted_return,
                    "outcome": "risk_exit" if risk_exit else str(row.get("outcome", "timeout")),
                    "cost_multiplier": cost_multiplier,
                }
            )
            active[asset] = exit_time
            active_weights[asset] = weight
            daily_entries[(asset, day)] = daily_entries.get((asset, day), 0) + 1
            group_return += weighted_return
        if group_return:
            equity *= max(1.0 + group_return, 1e-9)
            peak = max(peak, equity)
    trades = pd.DataFrame(accepted)
    if trades.empty:
        timeline = pd.DataFrame(columns=["as_of", "strategy_return"])
        metrics = summarize_returns([], [], [])
    else:
        timeline = trades.groupby("exit_time", as_index=False)["weighted_return"].sum()
        timeline = timeline.rename(columns={"exit_time": "as_of", "weighted_return": "strategy_return"})
        metrics = summarize_returns(
            timeline["strategy_return"], timeline["as_of"], trades["weighted_return"]
        )
        metrics["initial_cash"] = initial_cash
        metrics["ending_cash"] = initial_cash * float(np.prod(1.0 + timeline["strategy_return"].to_numpy()))
        metrics["exposure_mean"] = float(trades["weight"].mean())
    return PortfolioBacktestResult(ledger_name, initial_cash, trades, timeline, metrics)
