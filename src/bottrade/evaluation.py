from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import UTC, datetime, timedelta
from typing import Any

import pandas as pd

from bottrade.config import AppConfig
from bottrade.domain import Asset, RiskState
from bottrade.metrics import annualized_sharpe, max_drawdown_from_equity, profit_factor
from bottrade.models.registry import ModelRegistry
from bottrade.storage import Storage
from bottrade.utils import utc_now


def _utc_timestamp(value: Any) -> pd.Timestamp:
    stamp = pd.Timestamp(value)
    return stamp.tz_localize("UTC") if stamp.tzinfo is None else stamp.tz_convert("UTC")


def _closed_trade_returns(fills: pd.DataFrame) -> dict[tuple[str, str], list[float]]:
    output: dict[tuple[str, str], list[float]] = {}
    if fills.empty:
        return output
    for (ledger, asset), group in fills.sort_values("as_of").groupby(["ledger", "asset"]):
        quantity = 0.0
        cycle_cost = 0.0
        cycle_proceeds = 0.0
        returns: list[float] = []
        for row in group.itertuples(index=False):
            notional = float(row.quantity) * float(row.price)
            if row.side == "BUY":
                if quantity <= 1e-12:
                    cycle_cost = 0.0
                    cycle_proceeds = 0.0
                quantity += float(row.quantity)
                cycle_cost += notional + float(row.fee)
            else:
                quantity -= float(row.quantity)
                cycle_proceeds += notional - float(row.fee)
                if quantity <= 1e-10 and cycle_cost > 0:
                    returns.append((cycle_proceeds - cycle_cost) / cycle_cost)
                    quantity = 0.0
                    cycle_cost = 0.0
                    cycle_proceeds = 0.0
        output[(str(ledger), str(asset))] = returns
    return output


def _benchmark_sharpes(
    prices: pd.Series,
    annualization_days: int,
    cost_per_leg: float,
) -> dict[str, float]:
    clean = pd.to_numeric(prices, errors="coerce").dropna()
    if clean.empty:
        return {"cash": 0.0, "buy_hold_risk_equivalent": 0.0, "moving_average": 0.0}
    hourly_price = clean.resample("1h").last().ffill().dropna()
    daily_price = hourly_price.resample("1D").last().dropna()
    returns = daily_price.pct_change().fillna(0.0)
    moving_signal = (
        hourly_price.rolling(24, min_periods=24).mean()
        > hourly_price.rolling(72, min_periods=72).mean()
    ).astype(float)
    held_signal = moving_signal.shift(1).fillna(0.0)
    turnover = held_signal.diff().abs().fillna(held_signal.abs())
    moving_returns = (
        held_signal * hourly_price.pct_change().fillna(0.0)
        - turnover * cost_per_leg
    )
    moving_daily = (1.0 + moving_returns).resample("1D").prod() - 1.0
    return {
        "cash": 0.0,
        "buy_hold_risk_equivalent": annualized_sharpe(returns, annualization_days),
        "moving_average": annualized_sharpe(moving_daily, annualization_days),
    }


@dataclass(frozen=True, slots=True)
class PaperAssetLedgerMetrics:
    ledger: str
    asset: str
    total_return: float
    stress_total_return: float
    sharpe: float
    max_drawdown: float
    profit_factor: float
    closed_trades: int
    execution_cost: float
    execution_cost_fraction: float
    benchmark_sharpes: dict[str, float]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class FinalGateEvaluator:
    def __init__(self, config: AppConfig, storage: Storage) -> None:
        self.config = config
        self.storage = storage
        self.registry = ModelRegistry(config)

    def _paper_start(self) -> tuple[datetime | None, dict[str, Any] | None]:
        phases = [
            item for item in self.storage.paper_phase_history() if item["phase"] == "paper"
        ]
        if not phases:
            return None, None
        phase = phases[-1]
        started = _utc_timestamp(phase["started_at"]).to_pydatetime()
        return started, phase

    def _asset_ledger_metrics(
        self,
        *,
        start: datetime,
        asset: Asset,
        ledger: str,
        snapshots: pd.DataFrame,
        fills: pd.DataFrame,
        trade_returns: dict[tuple[str, str], list[float]],
    ) -> PaperAssetLedgerMetrics:
        initial = next(
            item.initial_cash for item in self.config.paper.ledgers if item.name == ledger
        )
        rows = snapshots[
            (snapshots["ledger"] == ledger) & (snapshots["asset"] == asset.value)
        ].copy()
        rows["as_of"] = pd.to_datetime(rows["as_of"], utc=True)
        rows = rows.sort_values("as_of").set_index("as_of")
        total_pnl = rows["realized_pnl"] + rows["unrealized_pnl"]
        daily_pnl = total_pnl.resample("1D").last().ffill()
        sleeve_equity = (float(initial) + daily_pnl).clip(lower=1e-9)
        daily_returns = sleeve_equity.pct_change().fillna(
            (sleeve_equity.iloc[0] / float(initial) - 1.0) if len(sleeve_equity) else 0.0
        )
        if sleeve_equity.empty:
            total_return = 0.0
            drawdown = 0.0
            sharpe = 0.0
        else:
            total_return = float(sleeve_equity.iloc[-1] / float(initial) - 1.0)
            drawdown = max_drawdown_from_equity(sleeve_equity)
            sharpe = annualized_sharpe(daily_returns, self.config.backtest.annualization_days)

        asset_fills = fills[(fills["ledger"] == ledger) & (fills["asset"] == asset.value)]
        observed_execution_cost = 0.0
        for fill in asset_fills.itertuples(index=False):
            midpoint = (float(fill.bid) + float(fill.ask)) / 2.0
            if str(fill.side) == "BUY":
                adverse_execution = max(float(fill.price) - midpoint, 0.0)
            else:
                adverse_execution = max(midpoint - float(fill.price), 0.0)
            observed_execution_cost += float(fill.fee)
            observed_execution_cost += float(fill.quantity) * adverse_execution
        closed = trade_returns.get((ledger, asset.value), [])
        prices = rows["market_price"] if not rows.empty else pd.Series(dtype=float)
        return PaperAssetLedgerMetrics(
            ledger=ledger,
            asset=asset.value,
            total_return=total_return,
            stress_total_return=(
                total_return - observed_execution_cost / float(initial)
            ),
            sharpe=sharpe,
            max_drawdown=drawdown,
            profit_factor=profit_factor(closed),
            closed_trades=len(closed),
            execution_cost=observed_execution_cost,
            execution_cost_fraction=observed_execution_cost / float(initial),
            benchmark_sharpes=_benchmark_sharpes(
                prices,
                self.config.backtest.annualization_days,
                self.config.backtest.cost_per_leg,
            ),
        )

    def evaluate(self, *, as_of: datetime | None = None) -> dict[str, Any]:
        now = (as_of or utc_now()).astimezone(UTC)
        start, phase = self._paper_start()
        if start is None or phase is None:
            return {
                "eligible_for_future_real_review": False,
                "global_reasons": ["official_paper_not_started"],
                "assets": {},
            }
        phase_end = (
            _utc_timestamp(phase["ended_at"]).to_pydatetime()
            if phase.get("ended_at") is not None
            else now
        )
        evaluation_end = min(now, phase_end)
        equity = pd.DataFrame(self.storage.recent_equity(limit=1_000_000))
        snapshots = pd.DataFrame(self.storage.recent_position_snapshots(limit=1_000_000))
        fills = pd.DataFrame(self.storage.recent_fills(limit=1_000_000))
        risk = pd.DataFrame(self.storage.recent_risk_events(limit=1_000_000))
        for frame in (equity, snapshots, fills, risk):
            if not frame.empty:
                frame["as_of"] = pd.to_datetime(frame["as_of"], utc=True)
                frame.drop(frame[frame["as_of"] < pd.Timestamp(start)].index, inplace=True)
                frame.drop(
                    frame[frame["as_of"] > pd.Timestamp(evaluation_end)].index,
                    inplace=True,
                )
        if snapshots.empty:
            snapshots = pd.DataFrame(
                columns=[
                    "ledger",
                    "asset",
                    "as_of",
                    "realized_pnl",
                    "unrealized_pnl",
                    "market_price",
                ]
            )
        if fills.empty:
            fills = pd.DataFrame(
                columns=["ledger", "asset", "as_of", "side", "quantity", "price", "fee"]
            )
        trade_returns = _closed_trade_returns(fills)

        global_reasons: list[str] = []
        elapsed_days = (evaluation_end - start).total_seconds() / 86_400
        if elapsed_days < self.config.paper.official_paper_days:
            global_reasons.append("official_paper_duration_incomplete")
        if phase["status"] != "completed":
            global_reasons.append("official_paper_phase_not_closed")
        recent_cutoff = evaluation_end - timedelta(days=self.config.gates.incident_free_days)
        if not risk.empty:
            recent_critical = risk[
                (risk["severity"] == "critical") & (risk["as_of"] >= pd.Timestamp(recent_cutoff))
            ]
            if not recent_critical.empty:
                global_reasons.append("critical_incident_in_last_90_days")
            risk_violations = risk[
                risk["state"].isin(
                    [RiskState.CIRCUIT_BREAKER.value, RiskState.DAILY_STOP.value]
                )
                | risk["message"].str.contains("position_loss_limit", na=False)
            ]
            violated_ledgers = sorted(risk_violations["ledger"].unique().tolist())
            if violated_ledgers:
                global_reasons.append("risk_limit_reached:" + ",".join(violated_ledgers))

        asset_results: dict[str, Any] = {}
        active_assets = set(phase.get("active_assets", []))
        for asset in Asset:
            reasons: list[str] = []
            if asset.value not in active_assets:
                reasons.append("paper:inactive_cash_by_frozen_phase")
            try:
                _, metadata = self.registry.resolve(asset, "champion")
                offline_reasons = self.registry.offline_gate_reasons(metadata)
                reasons.extend(f"holdout:{reason}" for reason in offline_reasons)
            except (FileNotFoundError, ValueError) as exc:
                metadata = None
                reasons.append(f"holdout_model_unavailable:{exc}")
            ledgers = [
                self._asset_ledger_metrics(
                    start=start,
                    asset=asset,
                    ledger=ledger.name,
                    snapshots=snapshots,
                    fills=fills,
                    trade_returns=trade_returns,
                )
                for ledger in self.config.paper.ledgers
            ]
            for metrics in ledgers:
                prefix = f"paper:{metrics.ledger}"
                if metrics.sharpe < self.config.gates.min_sharpe:
                    reasons.append(f"{prefix}:sharpe_below_gate")
                if metrics.max_drawdown > self.config.gates.max_drawdown:
                    reasons.append(f"{prefix}:drawdown_above_gate")
                if metrics.profit_factor < self.config.gates.min_profit_factor:
                    reasons.append(f"{prefix}:profit_factor_below_gate")
                if metrics.closed_trades < self.config.gates.min_closed_trades:
                    reasons.append(f"{prefix}:insufficient_trades")
                if metrics.stress_total_return <= 0:
                    reasons.append(f"{prefix}:negative_stress_return")
                if metrics.sharpe <= max(metrics.benchmark_sharpes.values(), default=0.0):
                    reasons.append(f"{prefix}:did_not_beat_live_controls")
            asset_results[asset.value] = {
                "passed": not reasons and not global_reasons,
                "reasons": reasons,
                "holdout": metadata.holdout_metrics if metadata is not None else {},
                "paper_ledgers": [item.to_dict() for item in ledgers],
            }
        return {
            "as_of": evaluation_end.isoformat(),
            "official_paper_started_at": start.isoformat(),
            "elapsed_days": elapsed_days,
            "eligible_for_future_real_review": (
                not global_reasons and any(item["passed"] for item in asset_results.values())
            ),
            "global_reasons": global_reasons,
            "assets": asset_results,
            "disclaimer": (
                "Passing these gates does not authorize real orders; a new paid-infrastructure, "
                "key-security, legal/tax and explicit authorization review is required."
            ),
        }
