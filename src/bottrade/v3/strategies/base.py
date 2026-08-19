from __future__ import annotations

import hashlib
from collections.abc import Iterable
from typing import Protocol

import numpy as np
import pandas as pd

from bottrade.domain import Asset
from bottrade.v3.config import V3Config
from bottrade.v3.costs import CostModel
from bottrade.v3.domain import StrategyFamily

REQUIRED_MARKET_COLUMNS = {"as_of", "close", "ewma_volatility_1h", "continuity_segment_id"}


class CandidateGenerator(Protocol):
    family: StrategyFamily

    def generate(self, frame: pd.DataFrame, asset: Asset) -> pd.DataFrame:
        ...


def require_columns(frame: pd.DataFrame, columns: Iterable[str]) -> None:
    missing = sorted(set(columns) - set(frame.columns))
    if missing:
        raise ValueError(f"feature frame missing columns: {missing}")


def asof_frame(frame: pd.DataFrame) -> pd.DataFrame:
    data = frame.copy()
    if "as_of" not in data and "open_time" in data:
        data["as_of"] = pd.to_datetime(data["open_time"], utc=True) + pd.Timedelta(hours=1)
    if "as_of" not in data:
        raise ValueError("feature frame requires as_of")
    data["as_of"] = pd.to_datetime(data["as_of"], utc=True)
    return data.sort_values("as_of").drop_duplicates("as_of", keep="last").reset_index(drop=True)


def candidate_id(asset: Asset, as_of: pd.Timestamp, variant_id: str) -> str:
    timestamp = pd.Timestamp(as_of)
    timestamp = timestamp.tz_localize("UTC") if timestamp.tzinfo is None else timestamp.tz_convert("UTC")
    normalized = timestamp.isoformat()
    payload = f"v3|{asset.value}|{normalized}|{variant_id}".encode()
    return hashlib.sha256(payload).hexdigest()[:32]


def parse_horizon(variant_id: str) -> int:
    marker = variant_id.rsplit("_h", 1)
    if len(marker) != 2 or not marker[1].isdigit():
        raise ValueError(f"variant must end with _h<hours>: {variant_id}")
    return int(marker[1])


def emit_candidates(
    *,
    frame: pd.DataFrame,
    asset: Asset,
    family: StrategyFamily,
    variant_id: str,
    mask: pd.Series,
    signal_strength: pd.Series,
    config: V3Config,
    costs: CostModel,
) -> pd.DataFrame:
    data = asof_frame(frame)
    require_columns(data, REQUIRED_MARKET_COLUMNS)
    horizon = parse_horizon(variant_id)
    if horizon not in config.horizons:
        raise ValueError(f"variant horizon {horizon} is not configured")
    selected = data.loc[mask.fillna(False)].copy()
    if selected.empty:
        return pd.DataFrame(columns=candidate_columns())
    strength = pd.to_numeric(signal_strength.reindex(selected.index), errors="coerce")
    volatility = pd.to_numeric(selected["ewma_volatility_1h"], errors="coerce")
    valid = volatility.gt(0) & np.isfinite(volatility) & np.isfinite(strength)
    selected = selected.loc[valid].copy()
    strength = strength.loc[selected.index]
    volatility = volatility.loc[selected.index]
    if selected.empty:
        return pd.DataFrame(columns=candidate_columns())
    snapshot = costs.snapshot()
    result = pd.DataFrame(
        {
            "candidate_id": [candidate_id(asset, value, variant_id) for value in selected["as_of"]],
            "asset": asset.value,
            "as_of": pd.to_datetime(selected["as_of"], utc=True).to_numpy(),
            "strategy_family": family.value,
            "variant_id": variant_id,
            "horizon_hours": horizon,
            "signal_strength": strength.to_numpy(dtype=float),
            "reference_price": pd.to_numeric(selected["close"], errors="coerce").to_numpy(float),
            "ewma_volatility_1h": volatility.to_numpy(dtype=float),
            "take_profit_return": snapshot.round_trip_return
            + config.take_profit_vol_multiplier * volatility.to_numpy(dtype=float) * np.sqrt(horizon),
            "stop_loss_return": -config.stop_loss_vol_multiplier
            * volatility.to_numpy(dtype=float)
            * np.sqrt(horizon),
            "continuity_segment_id": selected["continuity_segment_id"].astype(str).to_numpy(),
            "feature_schema_version": config.feature_schema_version,
            "cost_model_version": costs.version,
        }
    )
    result["as_of"] = pd.to_datetime(result["as_of"], utc=True)
    result = result.dropna(subset=["reference_price", "signal_strength"])
    return result[candidate_columns()].reset_index(drop=True)


def candidate_columns() -> list[str]:
    return [
        "candidate_id",
        "asset",
        "as_of",
        "strategy_family",
        "variant_id",
        "horizon_hours",
        "signal_strength",
        "reference_price",
        "ewma_volatility_1h",
        "take_profit_return",
        "stop_loss_return",
        "continuity_segment_id",
        "feature_schema_version",
        "cost_model_version",
    ]
