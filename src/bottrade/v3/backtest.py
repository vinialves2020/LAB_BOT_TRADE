from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from bottrade.v3.config import V3Config
from bottrade.v3.costs import CostModel
from bottrade.v3.statistics import summarize_returns


@dataclass(frozen=True, slots=True)
class SignalCeilingResult:
    trades: pd.DataFrame
    timeline: pd.DataFrame
    metrics: dict[str, float | int]


def _select_non_overlapping(
    labels: pd.DataFrame,
    *,
    cost_multiplier: float,
    maximum_round_trips_per_day: int,
) -> pd.DataFrame:
    if labels.empty:
        return labels.copy()
    required = {"label_valid", "entry_time", "exit_time", "asset", "signal_strength"}
    if not required.issubset(labels.columns):
        return labels.iloc[0:0].copy()
    data = labels[labels["label_valid"].astype(bool)].copy()
    if data.empty:
        return data
    data["entry_time"] = pd.to_datetime(data["entry_time"], utc=True)
    data["exit_time"] = pd.to_datetime(data["exit_time"], utc=True)
    data["_return"] = pd.to_numeric(data[f"net_return_{int(cost_multiplier)}x"], errors="coerce")
    data = data.sort_values(["asset", "entry_time", "signal_strength"], ascending=[True, True, False])
    selected: list[pd.Series] = []
    last_exit: dict[str, pd.Timestamp] = {}
    counts: dict[tuple[str, object], int] = {}
    for _, row in data.iterrows():
        asset = str(row["asset"])
        entry = pd.Timestamp(row["entry_time"])
        exit_time = pd.Timestamp(row["exit_time"])
        if asset in last_exit and entry < last_exit[asset]:
            continue
        key = (asset, entry.date())
        if counts.get(key, 0) >= maximum_round_trips_per_day:
            continue
        last_exit[asset] = exit_time
        counts[key] = counts.get(key, 0) + 1
        selected.append(row)
    if not selected:
        return data.iloc[0:0].copy()
    return pd.DataFrame(selected).reset_index(drop=True)


def signal_ceiling_backtest(
    labels: pd.DataFrame,
    *,
    config: V3Config,
    costs: CostModel | None = None,
    cost_multiplier: float = 1.0,
) -> SignalCeilingResult:
    """Backtest transparent candidates without any ML filtering."""

    if cost_multiplier not in (1.0, 2.0, 3.0):
        raise ValueError("cost_multiplier must be 1, 2 or 3")
    selected = _select_non_overlapping(
        labels,
        cost_multiplier=cost_multiplier,
        maximum_round_trips_per_day=config.maximum_round_trips_per_asset_day,
    )
    if selected.empty:
        timeline = pd.DataFrame(columns=["as_of", "strategy_return"])
        metrics = summarize_returns(pd.Series(dtype=float), pd.Series(dtype="datetime64[ns, UTC]"), [])
        return SignalCeilingResult(selected, timeline, metrics)
    selected["net_return"] = selected["_return"]
    selected["exit_time"] = pd.to_datetime(selected["exit_time"], utc=True)
    selected["entry_time"] = pd.to_datetime(selected["entry_time"], utc=True)
    timeline = selected[["exit_time", "net_return"]].rename(columns={"exit_time": "as_of"})
    timeline = timeline.groupby("as_of", as_index=False)["net_return"].sum()
    timeline["strategy_return"] = timeline["net_return"]
    metrics = summarize_returns(
        timeline["strategy_return"],
        timeline["as_of"],
        selected["net_return"],
        annualization_days=365,
    )
    return SignalCeilingResult(selected.drop(columns=["_return"], errors="ignore"), timeline, metrics)
