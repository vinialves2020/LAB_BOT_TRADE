from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

import pandas as pd


@dataclass(frozen=True, slots=True)
class CostSnapshot:
    version: str
    fee_bps_per_leg: float
    spread_bps_round_trip: float
    slippage_bps_per_leg: float
    source: str
    as_of: pd.Timestamp | None = None

    @property
    def per_leg_bps(self) -> float:
        return self.fee_bps_per_leg + self.spread_bps_round_trip / 2.0 + self.slippage_bps_per_leg

    @property
    def round_trip_bps(self) -> float:
        return 2.0 * self.per_leg_bps

    @property
    def round_trip_return(self) -> float:
        return self.round_trip_bps / 10_000.0


@dataclass(frozen=True, slots=True)
class CostModel:
    fallback_fee_bps_per_leg: float = 10.0
    fallback_spread_bps: float = 2.0
    fallback_slippage_bps: float = 1.0
    version: str = "v3-cost-fallback-1"

    def snapshot(
        self,
        *,
        as_of: pd.Timestamp | None = None,
        fee_bps_per_leg: float | None = None,
        spread_bps: float | None = None,
        slippage_bps_per_leg: float | None = None,
        source: str = "configured-fallback",
    ) -> CostSnapshot:
        fee = self.fallback_fee_bps_per_leg if fee_bps_per_leg is None else float(fee_bps_per_leg)
        spread = self.fallback_spread_bps if spread_bps is None else float(spread_bps)
        slippage = (
            self.fallback_slippage_bps
            if slippage_bps_per_leg is None
            else float(slippage_bps_per_leg)
        )
        if min(fee, spread, slippage) < 0:
            raise ValueError("cost components cannot be negative")
        return CostSnapshot(
            version=self.version,
            fee_bps_per_leg=fee,
            spread_bps_round_trip=spread,
            slippage_bps_per_leg=slippage,
            source=source,
            as_of=as_of,
        )

    def from_row(self, row: pd.Series, *, as_of: pd.Timestamp | None = None) -> CostSnapshot:
        def _value(name: str) -> float | None:
            if name not in row or pd.isna(row[name]):
                return None
            return float(row[name])

        return self.snapshot(
            as_of=as_of,
            fee_bps_per_leg=_value("fee_bps_per_leg"),
            spread_bps=_value("spread_bps"),
            slippage_bps_per_leg=_value("slippage_bps_per_leg"),
            source="point-in-time-row",
        )

    @staticmethod
    def net_return(gross_return: float, snapshot: CostSnapshot, multiplier: float = 1.0) -> float:
        if multiplier < 1:
            raise ValueError("cost multiplier must be at least one")
        return float(gross_return) - snapshot.round_trip_return * multiplier

    @staticmethod
    def net_decimal(gross_return: Decimal, snapshot: CostSnapshot, multiplier: float = 1.0) -> Decimal:
        return gross_return - Decimal(str(snapshot.round_trip_return * multiplier))
