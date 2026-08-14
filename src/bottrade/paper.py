from __future__ import annotations

import logging
from datetime import datetime
from decimal import Decimal

from bottrade.config import AppConfig
from bottrade.domain import (
    Asset,
    ExchangeRules,
    Forecast,
    MarketQuote,
    RiskEvent,
    RiskState,
    RunStage,
)
from bottrade.execution import PaperExecutionSimulator
from bottrade.risk import PortfolioRiskEngine
from bottrade.storage import Storage
from bottrade.utils import ensure_utc, utc_now

LOGGER = logging.getLogger(__name__)


class PaperTradingEngine:
    def __init__(self, config: AppConfig, storage: Storage) -> None:
        self.config = config
        self.storage = storage
        self.risk = PortfolioRiskEngine(config.paper)
        self.execution = PaperExecutionSimulator(config.backtest.fee_bps_per_leg)

    def _validate_clock(self, as_of: datetime) -> None:
        delta = abs((utc_now() - ensure_utc(as_of)).total_seconds())
        if delta > self.config.features.market_stale_minutes * 60:
            raise ValueError(f"market/forecast timestamp is stale by {delta:.1f}s")

    def _plan_targets(
        self,
        *,
        ledger: str,
        as_of: datetime,
        targets: list,
        quotes: dict[Asset, MarketQuote],
        rules: dict[Asset, ExchangeRules],
        equity: Decimal,
    ) -> list:
        position_map = {item.asset: item for item in self.storage.positions(ledger, as_of)}
        planned = []
        for target in targets:
            order = self.execution.target_order(
                ledger=ledger,
                target=target,
                position=position_map[target.asset],
                equity=equity,
                quote=quotes[target.asset],
                rules=rules[target.asset],
            )
            if order is not None:
                planned.append(order)
        planned.sort(key=lambda order: 0 if order.side == "SELL" else 1)
        order_fills = []
        for order in planned:
            fill = self.execution.fill(order, quotes[order.asset])
            order_fills.append((order, fill))
        return order_fills

    def signal_cycle(
        self,
        *,
        as_of: datetime,
        forecasts: dict[Asset, Forecast],
        shadow_forecasts: dict[Asset, Forecast] | None = None,
        volatilities: dict[Asset, float],
        quotes: dict[Asset, MarketQuote],
        rules: dict[Asset, ExchangeRules],
        enforce_clock: bool = True,
        enforce_phase: bool = True,
    ) -> dict[str, int | str]:
        as_of = ensure_utc(as_of)
        if enforce_phase:
            phase = self.storage.active_paper_phase()
            if phase is None or phase["phase"] not in {
                RunStage.CANARY.value,
                RunStage.PAPER.value,
            }:
                raise RuntimeError("paper mutation requires an active canary or paper phase")
            active_assets = {Asset(value) for value in phase.get("active_assets", [])}
            unexpected = set(forecasts) - active_assets
            if unexpected:
                raise RuntimeError(
                    "forecast attempted to activate assets outside the frozen phase: "
                    + ", ".join(sorted(asset.value for asset in unexpected))
                )
        if enforce_clock:
            self._validate_clock(as_of)
        missing = (set(Asset) - quotes.keys()) | (set(Asset) - rules.keys())
        if missing:
            raise ValueError(
                f"signal cycle is missing market/rule assets: "
                f"{sorted(item.value for item in missing)}"
            )
        missing_volatility = set(forecasts) - set(volatilities)
        if missing_volatility:
            raise ValueError(
                "signal cycle is missing forecast volatility for: "
                + ", ".join(sorted(item.value for item in missing_volatility))
            )
        cycle_key = as_of.isoformat()
        if not self.storage.claim_cycle("signal", cycle_key):
            return {"status": "duplicate", "orders": 0}
        orders = 0
        planned_fills = []
        try:
            for forecast in forecasts.values():
                self.storage.record_forecast(forecast)
            for forecast in (shadow_forecasts or {}).values():
                self.storage.record_forecast(forecast)
            prices = {asset: quote.mid for asset, quote in quotes.items()}
            for ledger in self.storage.ledger_names():
                equity = self.storage.equity_snapshot(ledger, as_of, prices)
                positions = self.storage.positions(ledger, as_of)
                assessment = self.risk.assess(
                    status=self.storage.ledger_status(ledger),
                    equity=equity,
                    positions=positions,
                    as_of=as_of,
                )
                if assessment.close_assets:
                    if assessment.state in {RiskState.CIRCUIT_BREAKER, RiskState.DAILY_STOP}:
                        self.storage.set_ledger_status(ledger, assessment.state)
                    self.storage.record_risk_event(
                        RiskEvent(
                            ledger=ledger,
                            as_of=as_of,
                            state=assessment.state,
                            severity=(
                                "critical"
                                if assessment.state
                                in {RiskState.CIRCUIT_BREAKER, RiskState.DAILY_STOP}
                                else "warning"
                            ),
                            message=assessment.reason,
                        )
                    )
                current_weights = {position.asset: position.weight for position in positions}
                targets = self.risk.target_positions(
                    forecasts=forecasts,
                    volatilities=volatilities,
                    current_weights=current_weights,
                    as_of=as_of,
                    block_new_positions=assessment.block_new_positions,
                    forced_closures=assessment.close_assets,
                )
                planned_fills.extend(self._plan_targets(
                    ledger=ledger,
                    as_of=as_of,
                    targets=targets,
                    quotes=quotes,
                    rules=rules,
                    equity=equity.equity,
                ))
            orders = self.storage.apply_order_fills(planned_fills)
            for ledger in self.storage.ledger_names():
                self.storage.equity_snapshot(ledger, as_of, prices)
            self.storage.finish_cycle("signal", cycle_key)
            return {"status": "completed", "orders": orders}
        except Exception as exc:
            self.storage.finish_cycle("signal", cycle_key, error=str(exc))
            raise

    def risk_cycle(
        self,
        *,
        as_of: datetime,
        quotes: dict[Asset, MarketQuote],
        rules: dict[Asset, ExchangeRules],
    ) -> dict[str, int | str]:
        as_of = ensure_utc(as_of)
        phase = self.storage.active_paper_phase()
        if phase is None or phase["phase"] not in {
            RunStage.CANARY.value,
            RunStage.PAPER.value,
        }:
            raise RuntimeError("paper mutation requires an active canary or paper phase")
        cycle_key = as_of.replace(second=0, microsecond=0).isoformat()
        if not self.storage.claim_cycle("risk", cycle_key):
            return {"status": "duplicate", "orders": 0}
        orders = 0
        planned_fills = []
        try:
            prices = {asset: quote.mid for asset, quote in quotes.items()}
            empty_forecasts: dict[Asset, Forecast] = {}
            for ledger in self.storage.ledger_names():
                equity = self.storage.equity_snapshot(ledger, as_of, prices)
                positions = self.storage.positions(ledger, as_of)
                assessment = self.risk.assess(
                    status=self.storage.ledger_status(ledger),
                    equity=equity,
                    positions=positions,
                    as_of=as_of,
                )
                if not assessment.close_assets:
                    continue
                if assessment.state in {RiskState.CIRCUIT_BREAKER, RiskState.DAILY_STOP}:
                    self.storage.set_ledger_status(ledger, assessment.state)
                self.storage.record_risk_event(
                    RiskEvent(
                        ledger=ledger,
                        as_of=as_of,
                        state=assessment.state,
                        severity=(
                            "critical"
                            if assessment.state == RiskState.CIRCUIT_BREAKER
                            else "warning"
                        ),
                        message=assessment.reason,
                        metadata={"assets": [asset.value for asset in assessment.close_assets]},
                    )
                )
                current_weights = {position.asset: position.weight for position in positions}
                targets = self.risk.target_positions(
                    forecasts=empty_forecasts,
                    volatilities={},
                    current_weights=current_weights,
                    as_of=as_of,
                    block_new_positions=True,
                    forced_closures=assessment.close_assets,
                )
                planned_fills.extend(self._plan_targets(
                    ledger=ledger,
                    as_of=as_of,
                    targets=targets,
                    quotes=quotes,
                    rules=rules,
                    equity=equity.equity,
                ))
            orders = self.storage.apply_order_fills(planned_fills)
            for ledger in self.storage.ledger_names():
                self.storage.equity_snapshot(ledger, as_of, prices)
            self.storage.finish_cycle("risk", cycle_key)
            return {"status": "completed", "orders": orders}
        except Exception as exc:
            self.storage.finish_cycle("risk", cycle_key, error=str(exc))
            raise
