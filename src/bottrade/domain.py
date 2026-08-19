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


@dataclass(frozen=True, slots=True)
class DataArmSpec:
    """Point-in-time description of a feature arm.

    ``DataArm`` is kept for V1 compatibility.  V2 arms are composable so that
    the same core can be ablated with derivatives, on-chain and sentiment data
    without adding another enum value for every possible combination.
    """

    arm_id: str
    include_intrahour: bool = False
    include_derivatives: bool = False
    include_onchain: bool = False
    include_sentiment: bool = False
    parent_id: str | None = None
    schema_version: str = "arm-v2"

    @classmethod
    def from_id(cls, value: str | DataArm | DataArmSpec) -> DataArmSpec:
        if isinstance(value, cls):
            return value
        text = str(value.value if isinstance(value, DataArm) else value)
        legacy = {
            DataArm.MARKET.value: cls("market", parent_id=None),
            DataArm.MARKET_ONCHAIN.value: cls("market_onchain", include_onchain=True),
            DataArm.MARKET_SENTIMENT.value: cls("market_sentiment", include_sentiment=True),
            DataArm.MARKET_ALL.value: cls(
                "market_all", include_onchain=True, include_sentiment=True
            ),
        }
        if text in legacy:
            return legacy[text]
        if text == "market_1h_15m":
            return cls(text, include_intrahour=True)
        if text == "market_1h":
            return cls(text)
        if text == "market_1h_15m_derivatives":
            return cls(text, include_intrahour=True, include_derivatives=True)
        if text.endswith("_onchain"):
            parent = text.removesuffix("_onchain")
            base = cls.from_id(parent)
            return cls(text, base.include_intrahour, base.include_derivatives, True, base.include_sentiment, parent)
        if text.endswith("_sentiment"):
            parent = text.removesuffix("_sentiment")
            base = cls.from_id(parent)
            return cls(text, base.include_intrahour, base.include_derivatives, base.include_onchain, True, parent)
        if text.endswith("_all"):
            parent = text.removesuffix("_all")
            base = cls.from_id(parent)
            return cls(text, base.include_intrahour, base.include_derivatives, True, True, parent)
        raise ValueError(f"unsupported data arm: {value}")

    @property
    def components(self) -> tuple[str, ...]:
        values = ["market_1h"]
        if self.include_intrahour:
            values.append("intrahour_15m")
        if self.include_derivatives:
            values.append("derivatives")
        if self.include_onchain:
            values.append("onchain")
        if self.include_sentiment:
            values.append("sentiment")
        return tuple(values)


class ModelFamily(StrEnum):
    RANDOM_FOREST = "random_forest"
    HIST_GRADIENT_BOOSTING = "hist_gradient_boosting"
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
    continuity_segment_id: str | None = None
    source_coverage: dict[str, float] = field(default_factory=dict)
    source_freshness_hours: dict[str, float] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class HorizonForecast:
    horizon_hours: int
    expected_gross_return: float
    expected_net_return: float
    probability_net_positive: float
    threshold_probability: float = 0.5
    cost_margin_bps: float = 0.0
    lower_bound_return: float | None = None


@dataclass(frozen=True, slots=True)
class Forecast:
    asset: Asset
    as_of: datetime
    horizon_hours: int
    expected_return: float
    model_family: ModelFamily
    model_version: str
    data_version: str
    data_arm: DataArm | DataArmSpec | str
    threshold_return: float
    is_fallback: bool = False
    is_shadow: bool = False
    horizons: tuple[HorizonForecast, ...] = ()
    selected_horizon_hours: int | None = None
    policy_version: str = "v1"
    ensemble_id: str | None = None


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
