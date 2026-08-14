from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime

import numpy as np

from bottrade.config import PaperConfig
from bottrade.domain import (
    Asset,
    EquitySnapshot,
    Forecast,
    PositionSnapshot,
    RiskState,
    TargetPosition,
)


@dataclass(frozen=True, slots=True)
class RiskAssessment:
    state: RiskState
    block_new_positions: bool
    close_assets: tuple[Asset, ...]
    reason: str


def _capped_inverse_volatility(
    active: list[Asset],
    volatilities: dict[Asset, float],
    *,
    max_asset_weight: float,
    max_gross_weight: float,
) -> dict[Asset, float]:
    if not active:
        return {}
    budget = min(max_gross_weight, len(active) * max_asset_weight)
    scores = {
        asset: 1.0 / max(float(volatilities.get(asset, np.nan)), 1e-8)
        if np.isfinite(volatilities.get(asset, np.nan))
        else 1.0
        for asset in active
    }
    weights = {asset: 0.0 for asset in active}
    remaining = set(active)
    remaining_budget = budget
    while remaining and remaining_budget > 1e-12:
        total_score = sum(scores[asset] for asset in remaining)
        if total_score <= 0:
            equal = remaining_budget / len(remaining)
            for asset in remaining:
                weights[asset] += min(equal, max_asset_weight - weights[asset])
            break
        capped: list[Asset] = []
        proposals = {
            asset: remaining_budget * scores[asset] / total_score for asset in remaining
        }
        for asset, proposal in proposals.items():
            capacity = max_asset_weight - weights[asset]
            if proposal >= capacity:
                weights[asset] += capacity
                remaining_budget -= capacity
                capped.append(asset)
        if not capped:
            for asset, proposal in proposals.items():
                weights[asset] += proposal
            remaining_budget = 0.0
        else:
            remaining.difference_update(capped)
    return weights


class PortfolioRiskEngine:
    def __init__(self, config: PaperConfig) -> None:
        self.config = config

    def assess(
        self,
        *,
        status: RiskState,
        equity: EquitySnapshot,
        positions: list[PositionSnapshot],
        as_of: datetime,
    ) -> RiskAssessment:
        open_assets = tuple(position.asset for position in positions if position.quantity > 0)
        if status == RiskState.CIRCUIT_BREAKER:
            return RiskAssessment(status, True, open_assets, "circuit breaker requires manual resume")
        if status == RiskState.MANUAL_PAUSE:
            return RiskAssessment(status, True, (), "ledger is manually paused")
        if equity.drawdown >= self.config.drawdown_circuit_breaker:
            return RiskAssessment(
                RiskState.CIRCUIT_BREAKER,
                True,
                open_assets,
                "portfolio drawdown limit reached",
            )
        if equity.daily_return <= -self.config.daily_loss_limit:
            return RiskAssessment(
                RiskState.DAILY_STOP,
                True,
                open_assets,
                "daily loss limit reached",
            )
        stopped: list[Asset] = []
        loss_stopped: list[Asset] = []
        for position in positions:
            if position.quantity <= 0:
                continue
            loss_fraction = (
                float(position.unrealized_pnl / equity.equity) if equity.equity > 0 else -1.0
            )
            opened_at = position.opened_at
            if opened_at is not None:
                if opened_at.tzinfo is None:
                    opened_at = opened_at.replace(tzinfo=UTC)
                holding_hours = (as_of.astimezone(UTC) - opened_at.astimezone(UTC)).total_seconds() / 3600
            else:
                holding_hours = 0.0
            if loss_fraction <= -self.config.position_loss_limit or holding_hours >= self.config.max_holding_hours:
                stopped.append(position.asset)
                if loss_fraction <= -self.config.position_loss_limit:
                    loss_stopped.append(position.asset)
        if stopped:
            return RiskAssessment(
                RiskState.POSITION_STOP,
                False,
                tuple(stopped),
                "position_loss_limit_reached" if loss_stopped else "maximum_holding_exit",
            )
        if status == RiskState.DAILY_STOP:
            return RiskAssessment(status, True, open_assets, "daily stop remains active until UTC reset")
        return RiskAssessment(RiskState.NORMAL, False, (), "risk checks passed")

    def target_positions(
        self,
        *,
        forecasts: dict[Asset, Forecast],
        volatilities: dict[Asset, float],
        current_weights: dict[Asset, float],
        as_of: datetime,
        block_new_positions: bool = False,
        forced_closures: tuple[Asset, ...] = (),
    ) -> list[TargetPosition]:
        active = [
            asset
            for asset, forecast in forecasts.items()
            if (
                forecast.expected_return > forecast.threshold_return
                or (
                    current_weights.get(asset, 0.0) > 0
                    and forecast.expected_return > 0.0
                )
            )
            and asset not in forced_closures
            and not block_new_positions
        ]
        proposed = _capped_inverse_volatility(
            active,
            volatilities,
            max_asset_weight=self.config.max_asset_weight,
            max_gross_weight=self.config.max_gross_weight,
        )
        targets: list[TargetPosition] = []
        for asset in Asset:
            target = proposed.get(asset, 0.0)
            current = current_weights.get(asset, 0.0)
            if asset in forced_closures:
                target = 0.0
                reason = "forced_risk_exit"
            elif block_new_positions and current > 0:
                target = current
                reason = "risk_block_hold_existing"
            elif (
                current > 0
                and asset in forecasts
                and forecasts[asset].expected_return <= 0.0
            ):
                target = 0.0
                reason = "forecast_exit_non_positive"
            elif abs(target - current) < self.config.rebalance_band:
                target = current
                reason = "rebalance_band"
            elif target > current:
                reason = "qualified_inverse_vol_entry"
            else:
                reason = "forecast_exit_or_rebalance"
            targets.append(
                TargetPosition(
                    asset=asset,
                    as_of=as_of,
                    target_weight=max(0.0, min(target, self.config.max_asset_weight)),
                    reason=reason,
                    risk_state=(
                        RiskState.POSITION_STOP if asset in forced_closures else RiskState.NORMAL
                    ),
                )
            )
        gross = sum(item.target_weight for item in targets)
        if gross > self.config.max_gross_weight + 1e-12:
            scale = self.config.max_gross_weight / gross
            targets = [
                TargetPosition(
                    asset=item.asset,
                    as_of=item.as_of,
                    target_weight=item.target_weight * scale,
                    reason=f"{item.reason}:gross_scaled",
                    risk_state=item.risk_state,
                )
                for item in targets
            ]
        return targets
