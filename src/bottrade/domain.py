from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from enum import StrEnum
from typing import Any


class Asset(StrEnum):
    BTCUSDT = "BTCUSDT"
    ETHUSDT = "ETHUSDT"
    SOLUSDT = "SOLUSDT"


class DataArm(StrEnum):
    MARKET = "market"
    MARKET_ONCHAIN = "market_onchain"
    MARKET_SENTIMENT = "market_sentiment"
    MARKET_ALL = "market_all"


class ModelFamily(StrEnum):
    RANDOM_FOREST = "random_forest"
    TRANSFORMER = "transformer"
    RIDGE = "ridge"


class RiskState(StrEnum):
    NORMAL = "normal"
    DAILY_STOP = "daily_stop"
    POSITION_STOP = "position_stop"
    CIRCUIT_BREAKER = "circuit_breaker"
    DATA_STALE = "data_stale"
    MODEL_INVALID = "model_invalid"
    OPERATIONAL_ERROR = "operational_error"
    MANUAL_PAUSE = "manual_pause"


class RunStage(StrEnum):
    DEVELOPMENT = "development"
    CANARY = "canary"
    PAPER = "paper"


@dataclass(frozen=True, slots=True)
class FeatureSnapshot:
    asset: Asset
    as_of: datetime
    available_at: datetime
    values: dict[str, float]
    schema_version: str
    stale_flags: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class Forecast:
    asset: Asset
    as_of: datetime
    horizon_hours: int
    expected_return: float
    model_family: ModelFamily
    model_version: str
    data_version: str
    data_arm: DataArm
    threshold_return: float
    is_fallback: bool = False
    is_shadow: bool = False


@dataclass(frozen=True, slots=True)
class TargetPosition:
    asset: Asset
    as_of: datetime
    target_weight: float
    reason: str
    risk_state: RiskState = RiskState.NORMAL


@dataclass(frozen=True, slots=True)
class ExchangeRules:
    symbol: str
    min_quantity: Decimal
    max_quantity: Decimal
    step_size: Decimal
    tick_size: Decimal
    min_notional: Decimal


@dataclass(frozen=True, slots=True)
class MarketQuote:
    asset: Asset
    as_of: datetime
    bid: Decimal
    ask: Decimal
    bid_quantity: Decimal
    ask_quantity: Decimal
    bids: tuple[tuple[Decimal, Decimal], ...] = ()
    asks: tuple[tuple[Decimal, Decimal], ...] = ()

    @property
    def mid(self) -> Decimal:
        return (self.bid + self.ask) / Decimal("2")

    @property
    def spread_bps(self) -> float:
        if self.mid <= 0:
            return 0.0
        return float((self.ask - self.bid) / self.mid * Decimal("10000"))


@dataclass(frozen=True, slots=True)
class PaperOrder:
    client_order_id: str
    ledger: str
    asset: Asset
    as_of: datetime
    side: str
    quantity: Decimal
    reference_price: Decimal
    reason: str


@dataclass(frozen=True, slots=True)
class PaperFill:
    client_order_id: str
    ledger: str
    asset: Asset
    as_of: datetime
    side: str
    quantity: Decimal
    price: Decimal
    fee: Decimal
    bid: Decimal
    ask: Decimal
    visible_depth_quantity: Decimal
    visible_depth_notional: Decimal
    spread_bps: float
    impact_bps: float


@dataclass(frozen=True, slots=True)
class PositionSnapshot:
    ledger: str
    asset: Asset
    as_of: datetime
    quantity: Decimal
    average_price: Decimal
    market_price: Decimal
    market_value: Decimal
    unrealized_pnl: Decimal
    weight: float
    opened_at: datetime | None = None


@dataclass(frozen=True, slots=True)
class EquitySnapshot:
    ledger: str
    as_of: datetime
    cash: Decimal
    positions_value: Decimal
    equity: Decimal
    peak_equity: Decimal
    drawdown: float
    daily_return: float


@dataclass(frozen=True, slots=True)
class RiskEvent:
    ledger: str
    as_of: datetime
    state: RiskState
    severity: str
    message: str
    metadata: dict[str, Any] = field(default_factory=dict)
