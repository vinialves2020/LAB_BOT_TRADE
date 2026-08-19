from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum
from typing import Any

from bottrade.domain import Asset


class StrategyFamily(StrEnum):
    TREND = "trend"
    REVERSAL = "reversal"
    BREAKOUT = "breakout"


class CandidateOutcome(StrEnum):
    TAKE_PROFIT = "take_profit"
    STOP_LOSS = "stop_loss"
    TIMEOUT = "timeout"
    RISK_EXIT = "risk_exit"
    INVALID = "invalid"


@dataclass(frozen=True, slots=True)
class TradeCandidate:
    candidate_id: str
    asset: Asset
    as_of: datetime
    strategy_family: StrategyFamily
    variant_id: str
    horizon_hours: int
    signal_strength: float
    reference_price: float
    ewma_volatility_1h: float
    take_profit_return: float
    stop_loss_return: float
    continuity_segment_id: str
    feature_schema_version: str
    cost_model_version: str


@dataclass(frozen=True, slots=True)
class EventOutcome:
    candidate_id: str
    asset: Asset
    strategy_family: StrategyFamily
    variant_id: str
    entry_time: datetime | None
    entry_price: float | None
    exit_time: datetime | None
    exit_price: float | None
    outcome: CandidateOutcome
    gross_return: float | None
    net_return_1x: float | None
    net_return_2x: float | None
    net_return_3x: float | None
    mfe: float | None
    mae: float | None
    bars_to_exit: int | None
    label_valid: bool
    invalid_reason: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class MetaDecision:
    candidate_id: str
    asset: Asset
    as_of: datetime
    probability_net_positive: float
    expected_net_return: float
    expected_mae: float | None
    approved: bool
    threshold_probability: float
    margin_bps: float
    model_family: str
    model_version: str
    ensemble_id: str


@dataclass(frozen=True, slots=True)
class PortfolioTrade:
    candidate_id: str
    asset: Asset
    entry_time: datetime
    exit_time: datetime
    entry_price: float
    exit_price: float
    weight: float
    gross_return: float
    net_return: float
    cost_return: float
    outcome: CandidateOutcome


@dataclass(frozen=True, slots=True)
class V3GateResult:
    passed: bool
    reasons: tuple[str, ...]
    metrics: dict[str, float | int | bool]

