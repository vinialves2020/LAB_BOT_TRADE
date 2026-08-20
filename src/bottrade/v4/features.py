from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

from bottrade.domain import Asset
from bottrade.v3.config import V3Config
from bottrade.v3.features import V3FeatureBuilder
from bottrade.v4.config import V4Config
from bottrade.validation import continuity_segments


@dataclass(frozen=True, slots=True)
class DirectDataset:
    """Causal features and direct return labels for one asset."""

    asset: Asset
    frame: pd.DataFrame
    feature_columns: tuple[str, ...]
    target_column: str = "target_return"

    @property
    def timestamps(self) -> pd.Series:
        return pd.to_datetime(self.frame["as_of"], utc=True)


def _numeric(frame: pd.DataFrame, name: str) -> pd.Series:
    if name not in frame:
        return pd.Series(np.nan, index=frame.index, dtype=float)
    return pd.to_numeric(frame[name], errors="coerce").replace([np.inf, -np.inf], np.nan)


def _normalise_market(frame: pd.DataFrame) -> pd.DataFrame:
    data = frame.copy()
    if "open_time" not in data:
        raise ValueError("market frame requires open_time")
    data["open_time"] = pd.to_datetime(data["open_time"], utc=True, errors="coerce")
    data = data.dropna(subset=["open_time"])
    if "is_closed" in data:
        data = data[data["is_closed"].astype(bool)]
    return data.sort_values("open_time").drop_duplicates("open_time", keep="last").reset_index(drop=True)


def _relative_features(frame: pd.DataFrame, *, stationary: bool = False) -> pd.DataFrame:
    """Turn absolute prices in the reusable V3 builder into causal ratios."""

    result = frame.copy()
    close = _numeric(result, "close")
    for span in (6, 12, 24, 48, 72, 168):
        name = f"ema_{span}h"
        if name in result:
            result[f"close_to_{name}"] = close / _numeric(result, name) - 1.0
    for horizon in (24, 72):
        high_name = f"previous_high_{horizon}h"
        low_name = f"previous_low_{horizon}h"
        if high_name in result:
            result[f"close_to_{high_name}"] = close / _numeric(result, high_name) - 1.0
        if low_name in result:
            result[f"close_to_{low_name}"] = close / _numeric(result, low_name) - 1.0
    if stationary:
        # Activity fields are useful, but their absolute scale drifts as the
        # market grows.  Keep causal log transforms and signed imbalances while
        # removing their raw counterparts below.  All denominators are guarded
        # so a malformed/empty candle becomes NaN and is handled by XGBoost's
        # missing-value branch rather than being imputed.
        for column in (
            "volume",
            "quote_volume",
            "trade_count",
            "taker_buy_base_volume",
            "intrahour_volume",
            "intrahour_trade_count",
        ):
            if column in result:
                result[f"log1p_{column}"] = np.log1p(_numeric(result, column).clip(lower=0.0))
        if "taker_buy_ratio" in result:
            result["taker_buy_imbalance"] = 2.0 * _numeric(result, "taker_buy_ratio") - 1.0
        if "intrahour_taker_ratio" in result:
            result["intrahour_taker_imbalance"] = (
                2.0 * _numeric(result, "intrahour_taker_ratio") - 1.0
            )
        vol_168 = _numeric(result, "volatility_168h").replace(0.0, np.nan)
        for horizon in (6, 24, 72):
            name = f"volatility_{horizon}h"
            if name in result:
                result[f"volatility_ratio_{horizon}h_168h"] = _numeric(result, name) / vol_168
    # Absolute price columns are not useful to a per-asset model and would make
    # the schema needlessly asset-specific.  The ratios above preserve their
    # information without changing the point-in-time timestamp.
    drop = {
        "open_time",
        "as_of",
        "asset",
        "open",
        "high",
        "low",
        "close",
        "ema_6h",
        "ema_12h",
        "ema_24h",
        "ema_48h",
        "ema_72h",
        "ema_168h",
        "previous_high_24h",
        "previous_high_72h",
        "previous_low_24h",
        "previous_low_72h",
        # This is a validation mask that looks ahead to confirm future
        # timestamps.  It is used only by the label gate, never as a model
        # feature, so live inference cannot accidentally receive future data.
        "continuity_valid",
    }
    if stationary:
        drop.update(
            {
                "volume",
                "quote_volume",
                "trade_count",
                "taker_buy_base_volume",
                "intrahour_volume",
                "intrahour_trade_count",
            }
        )
    return result.drop(columns=drop.intersection(result.columns), errors="ignore")


def build_features(
    *,
    asset: Asset,
    market: Mapping[str, pd.DataFrame],
    intrahour: Mapping[str, pd.DataFrame] | None,
    config: V4Config,
) -> pd.DataFrame:
    """Build only point-in-time market features for one asset."""

    v3 = V3Config(
        holdout_start=config.holdout_start,
        holdout_end=config.holdout_end,
        lookback_hours=config.lookback_hours,
        horizons=(config.horizon_hours,),
        purge_hours=config.purge_hours,
    ).validate()
    prepared_market = {str(symbol): _normalise_market(frame) for symbol, frame in market.items()}
    prepared_intrahour = (
        {str(symbol): _normalise_market(frame) for symbol, frame in intrahour.items()}
        if intrahour is not None and config.include_intrahour_15m
        else None
    )
    built = V3FeatureBuilder(v3).build(
        asset=asset,
        market=prepared_market,
        intrahour=prepared_intrahour,
        include_intrahour=config.include_intrahour_15m,
    )
    built = built.sort_values("as_of").drop_duplicates("as_of", keep="last").reset_index(drop=True)
    relative = _relative_features(built, stationary=config.stationary_features)
    numeric = relative.select_dtypes(include=[np.number]).copy()
    numeric = numeric.replace([np.inf, -np.inf], np.nan)
    # Explicit completeness columns are kept as model inputs, while the label
    # builder below enforces the hard continuity rule.
    numeric.insert(0, "as_of", pd.to_datetime(built["as_of"], utc=True).to_numpy())
    numeric["continuity_segment_id"] = built["continuity_segment_id"].astype(str).to_numpy()
    return numeric


def _segment_index(frame: pd.DataFrame) -> pd.Series:
    return continuity_segments(frame["open_time"], expected_frequency="1h").astype(str)


def build_direct_dataset(
    *,
    asset: Asset,
    features: pd.DataFrame,
    market: pd.DataFrame,
    config: V4Config,
    pre_holdout_only: bool = True,
) -> DirectDataset:
    """Join next-open/12h-close labels without interpolating gaps."""

    data = _normalise_market(market)
    if data.empty:
        raise ValueError(f"empty market frame for {asset.value}")
    times = pd.to_datetime(data["open_time"], utc=True)
    opens = _numeric(data, "open").to_numpy(float)
    closes = _numeric(data, "close").to_numpy(float)
    segments = _segment_index(data).to_numpy()
    time_values = times.array.asi8
    horizon = config.horizon_hours
    rows: list[dict[str, object]] = []
    source = features.copy()
    source["as_of"] = pd.to_datetime(source["as_of"], utc=True, errors="coerce")
    source = source.dropna(subset=["as_of"]).sort_values("as_of").reset_index(drop=True)
    holdout_start = pd.Timestamp(config.holdout_start).tz_convert("UTC")
    holdout_end = pd.Timestamp(config.holdout_end).tz_convert("UTC")
    for row in source.itertuples(index=False):
        as_of = pd.Timestamp(row.as_of)
        position = int(np.searchsorted(time_values, as_of.value, side="left"))
        exit_position = position + horizon - 1
        valid = position < len(data) and exit_position < len(data)
        reason = None
        if not valid:
            reason = "missing_entry_or_horizon"
        elif time_values[position] != as_of.value:
            valid = False
            reason = "entry_timestamp_not_available"
        else:
            expected = np.arange(time_values[position], time_values[exit_position] + 1, pd.Timedelta(hours=1).value)
            actual = time_values[position : exit_position + 1]
            if len(actual) != horizon or not np.array_equal(actual, expected):
                valid = False
                reason = "market_gap_in_horizon"
            elif segments[position] != segments[exit_position]:
                valid = False
                reason = "segment_changed"
            elif not np.isfinite(opens[position]) or opens[position] <= 0 or not np.isfinite(closes[exit_position]):
                valid = False
                reason = "invalid_execution_price"
        entry_time = times.iloc[position] if position < len(data) else pd.NaT
        exit_time = times.iloc[exit_position] if exit_position < len(data) else pd.NaT
        gross = (
            float(closes[exit_position] / opens[position] - 1.0)
            if valid
            else np.nan
        )
        row_data = dict(zip(source.columns, row, strict=False))
        row_data.update(
            {
                "asset": asset.value,
                "entry_time": entry_time,
                "exit_time": exit_time,
                "entry_price": float(opens[position]) if position < len(data) else np.nan,
                "exit_price": float(closes[exit_position]) if exit_position < len(data) else np.nan,
                "gross_return": gross,
                "target_return": np.log1p(gross) if valid and gross > -1.0 else np.nan,
                "net_return_1x": gross - config.round_trip_bps / 10_000 if valid else np.nan,
                "net_return_2x": gross - 2.0 * config.round_trip_bps / 10_000 if valid else np.nan,
                "label_valid": bool(valid),
                "invalid_reason": reason,
            }
        )
        if pre_holdout_only and (as_of >= holdout_start or (valid and exit_time >= holdout_start)):
            row_data["label_valid"] = False
            row_data["invalid_reason"] = "holdout_closed"
        elif not pre_holdout_only and (as_of > holdout_end or (valid and exit_time > holdout_end)):
            row_data["label_valid"] = False
            row_data["invalid_reason"] = "outside_available_window"
        rows.append(row_data)
    labeled = pd.DataFrame(rows)
    protected = {
        "as_of",
        "asset",
        "entry_time",
        "exit_time",
        "entry_price",
        "exit_price",
        "gross_return",
        "target_return",
        "net_return_1x",
        "net_return_2x",
        "label_valid",
        "invalid_reason",
        "continuity_segment_id",
    }
    feature_columns = tuple(
        column
        for column in labeled.columns
        if column not in protected and pd.api.types.is_numeric_dtype(labeled[column])
    )
    if not feature_columns:
        raise ValueError("no numeric feature columns were produced")
    labeled[list(feature_columns)] = labeled[list(feature_columns)].replace(
        [np.inf, -np.inf], np.nan
    )
    labeled = labeled.sort_values("as_of").reset_index(drop=True)
    return DirectDataset(asset=asset, frame=labeled, feature_columns=feature_columns)


def load_raw_market(data_dir: str | Path, asset: Asset, interval: str) -> pd.DataFrame:
    path = Path(data_dir) / "raw" / "market" / f"{asset.value}_{interval}.parquet"
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_parquet(path)
