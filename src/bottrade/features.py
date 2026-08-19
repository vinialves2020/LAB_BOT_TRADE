from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

import numpy as np
import pandas as pd

from bottrade.config import FeatureConfig
from bottrade.domain import Asset, DataArm, DataArmSpec
from bottrade.validation import continuity_segments, valid_continuity_mask

META_COLUMNS = {
    "as_of",
    "open_time",
    "reference_close",
    "execution_open",
    "future_close",
    "target_raw_return",
    "target_volatility",
    "target_normalized_return",
    "next_hour_return",
    "is_closed",
    "label_window_closed",
    "label_tradeable",
    "label_window_closed_3h",
    "future_close_3h",
    "future_close_6h",
    "future_close_12h",
    "continuity_segment_id",
    "continuity_valid",
    "market_context_complete",
}
FEATURE_SCHEMA_VERSION = "features-v3"
FEATURE_SCHEMA_VERSION_V2 = "features-v4"
DERIVATIVE_FIELDS = (
    "funding_rate",
    "premium",
    "mark_price",
    "index_price",
    "basis",
    "volume",
    "taker_buy_volume",
    "taker_sell_volume",
    "open_interest",
    "long_short_ratio",
)


def _intrahour_feature_names(prefix: str) -> list[str]:
    return [
        f"market_{prefix}_intrahour_return",
        f"market_{prefix}_intrahour_volatility",
        f"market_{prefix}_intrahour_log_range",
        f"market_{prefix}_intrahour_high_low",
        f"market_{prefix}_intrahour_volume_log",
        f"market_{prefix}_intrahour_quote_volume_log",
        f"market_{prefix}_intrahour_trade_count_log",
        f"market_{prefix}_intrahour_taker_ratio",
        f"market_{prefix}_intrahour_bars",
        f"market_{prefix}_intrahour_complete",
    ]


@dataclass(frozen=True, slots=True)
class FeatureFrame:
    asset: Asset
    arm: DataArm | DataArmSpec
    frame: pd.DataFrame
    feature_columns: tuple[str, ...]
    schema_version: str = FEATURE_SCHEMA_VERSION
    arm_spec: DataArmSpec | None = None


def _zscore(series: pd.Series, window: int, min_periods: int | None = None) -> pd.Series:
    minimum = min_periods or max(3, window // 3)
    mean = series.rolling(window, min_periods=minimum).mean()
    std = series.rolling(window, min_periods=minimum).std(ddof=0)
    return (series - mean) / std.replace(0, np.nan)


def truncated_ewma_std(series: pd.Series, window: int) -> pd.Series:
    """Exponentially weighted deviation with a hard, point-in-time window."""

    if window < 2:
        raise ValueError("EWMA window must be at least two observations")
    values = pd.to_numeric(series, errors="coerce").to_numpy(dtype=float)
    alpha = 2.0 / (window + 1.0)
    weights = np.power(1.0 - alpha, np.arange(window - 1, -1, -1, dtype=float))
    weights /= weights.sum()
    output = np.full(len(values), np.nan, dtype=float)
    if len(values) < window:
        return pd.Series(output, index=series.index)
    filled = np.where(np.isfinite(values), values, 0.0)
    valid = np.isfinite(values).astype(float)
    weighted_mean = np.convolve(filled, weights[::-1], mode="valid")
    weighted_square = np.convolve(filled**2, weights[::-1], mode="valid")
    valid_count = np.convolve(valid, np.ones(window), mode="valid")
    variance = np.maximum(weighted_square - weighted_mean**2, 0.0)
    unbiased_correction = 1.0 / (1.0 - float(np.sum(weights**2)))
    estimates = np.sqrt(variance * unbiased_correction)
    estimates[valid_count < window] = np.nan
    output[window - 1 :] = estimates
    return pd.Series(output, index=series.index)


def _prepare_market(frame: pd.DataFrame) -> pd.DataFrame:
    data = frame.copy()
    for column in ("open_time", "close_time", "as_of"):
        if column in data:
            data[column] = pd.to_datetime(data[column], utc=True)
    if "as_of" not in data:
        data["as_of"] = data["open_time"] + pd.Timedelta(hours=1)
    if "is_closed" not in data:
        data["is_closed"] = True
    return data.sort_values("as_of").drop_duplicates("as_of", keep="last").reset_index(drop=True)


def _intrahour_features(frame: pd.DataFrame, prefix: str) -> pd.DataFrame:
    """Aggregate closed 15-minute candles into point-in-time hourly features."""

    if frame.empty:
        return pd.DataFrame(
            {name: pd.Series(dtype=float) for name in _intrahour_feature_names(prefix)}
        ).assign(as_of=pd.Series(dtype="datetime64[ns, UTC]"))[
            ["as_of", *_intrahour_feature_names(prefix)]
        ]
    data = frame.copy()
    for column in ("open_time", "close_time", "as_of"):
        if column in data:
            data[column] = pd.to_datetime(data[column], utc=True)
    if "open_time" not in data:
        raise ValueError("intrahour data requires open_time")
    if "as_of" not in data:
        data["as_of"] = data["open_time"] + pd.Timedelta(minutes=15)
    data = data.sort_values("open_time").drop_duplicates("open_time", keep="last")
    if "is_closed" in data:
        data = data[data["is_closed"].astype(bool)].copy()
    if data.empty:
        return pd.DataFrame(
            {name: pd.Series(dtype=float) for name in _intrahour_feature_names(prefix)}
        ).assign(as_of=pd.Series(dtype="datetime64[ns, UTC]"))[
            ["as_of", *_intrahour_feature_names(prefix)]
        ]
    data["hour_as_of"] = data["open_time"].dt.floor("1h") + pd.Timedelta(hours=1)
    open_price = pd.to_numeric(data["open"], errors="coerce").replace(0, np.nan)
    close = pd.to_numeric(data["close"], errors="coerce").replace(0, np.nan)
    high = pd.to_numeric(data["high"], errors="coerce")
    low = pd.to_numeric(data["low"], errors="coerce")
    def _numeric_column(name: str) -> pd.Series:
        if name not in data:
            return pd.Series(0.0, index=data.index)
        return pd.to_numeric(data[name], errors="coerce")

    volume = _numeric_column("volume").clip(lower=0)
    quote_volume = _numeric_column("quote_volume").clip(lower=0)
    trades = _numeric_column("trade_count").clip(lower=0)
    taker = _numeric_column("taker_buy_base_volume").clip(lower=0)
    # Keep optional Binance columns present for the grouped aggregation.  A
    # missing field is represented as zero and remains auditable through the
    # completeness flag instead of being silently fabricated.
    data["volume"] = volume
    data["quote_volume"] = quote_volume
    data["trade_count"] = trades
    data["_log_return"] = np.log(close / open_price)
    data["_log_range"] = np.log(high / low.replace(0, np.nan))
    data["_taker_ratio"] = taker / volume.replace(0, np.nan)
    grouped = data.groupby("hour_as_of", sort=True)
    result = grouped.agg(
        intrahour_return_sum=("_log_return", "sum"),
        intrahour_return_std=("_log_return", "std"),
        intrahour_log_range=("_log_range", "sum"),
        intrahour_high=("high", "max"),
        intrahour_low=("low", "min"),
        intrahour_volume=("volume", "sum"),
        intrahour_quote_volume=("quote_volume", "sum"),
        intrahour_trade_count=("trade_count", "sum"),
        intrahour_taker_ratio=("_taker_ratio", "mean"),
        intrahour_bars=("open_time", "count"),
    ).reset_index(names="as_of")
    result[f"market_{prefix}_intrahour_return"] = result.pop("intrahour_return_sum")
    result[f"market_{prefix}_intrahour_volatility"] = result.pop("intrahour_return_std")
    result[f"market_{prefix}_intrahour_log_range"] = result.pop("intrahour_log_range")
    result[f"market_{prefix}_intrahour_high_low"] = np.log(
        result.pop("intrahour_high") / result.pop("intrahour_low").replace(0, np.nan)
    )
    result[f"market_{prefix}_intrahour_volume_log"] = np.log1p(result.pop("intrahour_volume"))
    result[f"market_{prefix}_intrahour_quote_volume_log"] = np.log1p(
        result.pop("intrahour_quote_volume")
    )
    result[f"market_{prefix}_intrahour_trade_count_log"] = np.log1p(
        result.pop("intrahour_trade_count")
    )
    result[f"market_{prefix}_intrahour_taker_ratio"] = result.pop("intrahour_taker_ratio")
    result[f"market_{prefix}_intrahour_bars"] = result.pop("intrahour_bars").astype(float)
    result[f"market_{prefix}_intrahour_complete"] = (
        result[f"market_{prefix}_intrahour_bars"] >= 4
    ).astype(float)
    return result


def _resolve_optional_frame(
    value: pd.DataFrame | dict[str, pd.DataFrame] | None,
    asset: Asset,
) -> pd.DataFrame:
    if value is None:
        return pd.DataFrame()
    if isinstance(value, dict):
        return value.get(asset.value, pd.DataFrame())
    return value


def _context_features(frame: pd.DataFrame, prefix: str, lags: Iterable[int]) -> pd.DataFrame:
    close = frame["close"].astype(float)
    volume = frame["quote_volume"].astype(float).clip(lower=0)
    log_close = np.log(close.replace(0, np.nan))
    result = pd.DataFrame({"as_of": frame["as_of"]})
    hourly_return = log_close.diff()
    result[f"market_{prefix}_return_1h"] = hourly_return
    for lag in lags:
        result[f"market_{prefix}_return_{lag}h"] = log_close.diff(lag)
    for window in [value for value in lags if value >= 3]:
        result[f"market_{prefix}_volatility_{window}h"] = hourly_return.rolling(
            window, min_periods=max(3, window // 3)
        ).std(ddof=0)
        result[f"market_{prefix}_volume_z_{window}h"] = _zscore(np.log1p(volume), window)
    return result


def _target_microstructure(frame: pd.DataFrame, lags: Iterable[int]) -> pd.DataFrame:
    data = pd.DataFrame({"as_of": frame["as_of"]})
    open_price = frame["open"].astype(float).replace(0, np.nan)
    close = frame["close"].astype(float).replace(0, np.nan)
    high = frame["high"].astype(float)
    low = frame["low"].astype(float)
    volume = frame["volume"].astype(float).clip(lower=0)
    quote_volume = frame["quote_volume"].astype(float).clip(lower=0)
    trades = frame["trade_count"].astype(float).clip(lower=0)
    taker = frame["taker_buy_base_volume"].astype(float).clip(lower=0)
    data["market_target_log_range"] = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    data["market_target_log_body"] = np.log(close / open_price)
    data["market_target_log_volume"] = np.log1p(volume)
    data["market_target_log_quote_volume"] = np.log1p(quote_volume)
    data["market_target_log_trade_count"] = np.log1p(trades)
    data["market_target_taker_buy_ratio"] = taker / volume.replace(0, np.nan)
    base_columns = [column for column in data.columns if column != "as_of"]
    generated: dict[str, pd.Series] = {}
    for column in base_columns:
        for lag in lags:
            generated[f"{column}_lag_{lag}h"] = data[column].shift(lag)
        for window in [value for value in lags if value >= 3]:
            generated[f"{column}_mean_{window}h"] = data[column].rolling(
                window, min_periods=max(3, window // 3)
            ).mean()
            generated[f"{column}_std_{window}h"] = data[column].rolling(
                window, min_periods=max(3, window // 3)
            ).std(ddof=0)
    return pd.concat([data, pd.DataFrame(generated, index=data.index)], axis=1)


def prepare_daily_alternative(frame: pd.DataFrame, prefix: str) -> pd.DataFrame:
    if frame.empty:
        return frame.copy()
    data = frame.copy().sort_values("event_time")
    data["event_time"] = pd.to_datetime(data["event_time"], utc=True)
    data["available_at"] = pd.to_datetime(data["available_at"], utc=True)
    original_numeric = [
        column
        for column in data.columns
        if column not in {"event_time", "available_at", "classification"}
        and pd.api.types.is_numeric_dtype(data[column])
    ]
    result = data[["event_time", "available_at"]].copy()
    for column in original_numeric:
        clean_name = column if column.startswith(prefix) else f"{prefix}_{column}"
        values = pd.to_numeric(data[column], errors="coerce")
        result[clean_name] = values
        result[f"{clean_name}_missing"] = values.isna().astype(float)
        result[f"{clean_name}_change_1d"] = values.pct_change(fill_method=None).clip(-10, 10)
        result[f"{clean_name}_change_7d"] = values.pct_change(7, fill_method=None).clip(-10, 10)
        result[f"{clean_name}_z_30d"] = _zscore(values, 30, min_periods=10)
    return result


def prepare_derivatives(frame: pd.DataFrame, delay_hours: int = 24) -> pd.DataFrame:
    """Normalize archived derivative observations for point-in-time joins.

    Official mark/index/premium/funding archives do not all use the same
    timestamp names.  This adapter accepts the common variants while
    requiring an explicit availability timestamp when one is supplied.  If an
    archive contains only an event timestamp, availability is conservatively
    delayed by ``delay_hours``; no recent-only endpoint is synthesized here.
    """

    if frame.empty:
        return frame.copy()
    data = frame.copy()
    event_column = next(
        (name for name in ("event_time", "as_of", "timestamp", "time") if name in data),
        None,
    )
    if event_column is None:
        raise ValueError("derivatives data requires event_time/as_of/timestamp")
    data["event_time"] = pd.to_datetime(data[event_column], utc=True, errors="coerce")
    if "available_at" in data:
        data["available_at"] = pd.to_datetime(data["available_at"], utc=True, errors="coerce")
    else:
        data["available_at"] = data["event_time"] + pd.Timedelta(hours=delay_hours)
    keep = data["event_time"].notna() & data["available_at"].notna()
    data = data.loc[keep].copy()
    drop = {event_column, "event_time", "available_at", "as_of", "timestamp", "time"}
    numeric = [
        column
        for column in data.columns
        if column not in drop and pd.api.types.is_numeric_dtype(data[column])
    ]
    result = data[["event_time", "available_at", *numeric]].copy()
    for column in numeric:
        values = pd.to_numeric(result[column], errors="coerce")
        clean = column.lower().replace(" ", "_")
        # Preserve the canonical names requested by the protocol when the
        # source used a known alias; other fields remain source-prefixed.
        aliases = {
            "fundingrate": "funding_rate",
            "funding": "funding_rate",
            "markprice": "mark_price",
            "indexprice": "index_price",
            "premiumindex": "premium",
            "openinterest": "open_interest",
        }
        clean = aliases.get(clean, clean)
        result[f"derivatives_{clean}"] = values
        result[f"derivatives_{clean}_missing"] = values.isna().astype(float)
    return result.drop(columns=numeric, errors="ignore")


def merge_point_in_time(
    base: pd.DataFrame,
    alternative: pd.DataFrame,
    *,
    prefix: str,
    stale_hours: int,
) -> pd.DataFrame:
    left = base.sort_values("as_of").copy()
    if alternative.empty:
        left[f"{prefix}_event_time"] = pd.NaT
        left[f"{prefix}_available_at"] = pd.NaT
        left[f"{prefix}_age_hours"] = np.nan
        left[f"{prefix}_missing"] = 1.0
        left[f"{prefix}_stale"] = 1.0
        if prefix == "derivatives":
            for field in DERIVATIVE_FIELDS:
                left[f"derivatives_{field}"] = np.nan
                left[f"derivatives_{field}_missing"] = 1.0
        return left
    right = alternative.sort_values("available_at").copy()
    merged = pd.merge_asof(
        left,
        right,
        left_on="as_of",
        right_on="available_at",
        direction="backward",
        allow_exact_matches=True,
    )
    age = (merged["as_of"] - merged["event_time"]).dt.total_seconds() / 3600
    future_event = merged["event_time"] > merged["as_of"]
    merged[f"{prefix}_event_time"] = merged["event_time"]
    merged[f"{prefix}_available_at"] = merged["available_at"]
    merged[f"{prefix}_age_hours"] = age
    merged[f"{prefix}_missing"] = merged["event_time"].isna().astype(float)
    merged[f"{prefix}_future_event"] = future_event.astype(float)
    merged[f"{prefix}_stale"] = ((age > stale_hours) | age.isna() | future_event).astype(float)
    if future_event.any():
        protected = {
            f"{prefix}_event_time",
            f"{prefix}_available_at",
            f"{prefix}_age_hours",
            f"{prefix}_missing",
            f"{prefix}_future_event",
            f"{prefix}_stale",
            "as_of",
        }
        value_columns = [column for column in merged.columns if column.startswith(prefix + "_")]
        merged.loc[future_event, [column for column in value_columns if column not in protected]] = np.nan
    merged = merged.drop(columns=["event_time", "available_at"], errors="ignore")
    return merged


class FeatureBuilder:
    def __init__(self, config: FeatureConfig) -> None:
        self.config = config

    def build(
        self,
        *,
        asset: Asset,
        market: dict[str, pd.DataFrame],
        onchain: pd.DataFrame | None = None,
        sentiment: pd.DataFrame | None = None,
        arm: DataArm | DataArmSpec | str = DataArm.MARKET,
        include_labels: bool = True,
        intrahour: dict[str, pd.DataFrame] | None = None,
        derivatives: pd.DataFrame | dict[str, pd.DataFrame] | None = None,
    ) -> FeatureFrame:
        arm_spec = DataArmSpec.from_id(arm)
        prepared = {symbol: _prepare_market(frame) for symbol, frame in market.items()}
        target = prepared[asset.value]
        target_segments = continuity_segments(target["open_time"])
        base = target[
            [
                "as_of",
                "open_time",
                "open",
                "close",
                "is_closed",
            ]
        ].copy()
        base["continuity_segment_id"] = target_segments.to_numpy()
        for symbol, frame in prepared.items():
            prefix = symbol.removesuffix("USDT").lower()
            context = _context_features(frame, prefix, self.config.lag_hours)
            context_valid = valid_continuity_mask(
                frame["open_time"],
                lookback_hours=self.config.lookback_hours,
                max_horizon_hours=(
                    max(self.config.forecast_horizons) if include_labels else 0
                ),
            )
            context_valid_by_time = dict(zip(frame["as_of"], context_valid, strict=True))
            context[f"market_{prefix}_continuity_valid"] = context["as_of"].map(
                context_valid_by_time
            ).astype(float)
            base = base.merge(context, on="as_of", how="left", validate="one_to_one")
        availability_columns = [
            column
            for column in base.columns
            if column.startswith("market_") and column.endswith("return_1h")
        ]
        base["market_context_complete"] = base[availability_columns].notna().all(axis=1).astype(float)
        context_valid_columns = [
            column
            for column in base.columns
            if column.startswith("market_") and column.endswith("_continuity_valid")
        ]
        if context_valid_columns:
            base["market_context_complete"] = (
                base["market_context_complete"].astype(bool)
                & base[context_valid_columns].eq(1.0).all(axis=1)
            ).astype(float)
        base = base.merge(
            _target_microstructure(target, self.config.lag_hours),
            on="as_of",
            how="left",
        )
        hour = base["as_of"].dt.hour + base["as_of"].dt.minute / 60
        day = base["as_of"].dt.dayofweek
        base["calendar_hour_sin"] = np.sin(2 * np.pi * hour / 24)
        base["calendar_hour_cos"] = np.cos(2 * np.pi * hour / 24)
        base["calendar_day_sin"] = np.sin(2 * np.pi * day / 7)
        base["calendar_day_cos"] = np.cos(2 * np.pi * day / 7)
        base["calendar_hour_index"] = base["as_of"].dt.hour.astype(float)
        base["calendar_day_index"] = base["as_of"].dt.dayofweek.astype(float)

        if arm_spec.include_intrahour:
            for symbol in prepared:
                raw_intrahour = (intrahour or {}).get(symbol, pd.DataFrame())
                prefix = symbol.removesuffix("USDT").lower()
                base = base.merge(
                    _intrahour_features(raw_intrahour, prefix),
                    on="as_of",
                    how="left",
                    validate="one_to_one",
                )
        include_onchain = arm_spec.include_onchain
        include_sentiment = arm_spec.include_sentiment
        if include_onchain:
            prepared_onchain = prepare_daily_alternative(
                onchain if onchain is not None else pd.DataFrame(), "onchain"
            )
            base = merge_point_in_time(
                base,
                prepared_onchain,
                prefix="onchain",
                stale_hours=self.config.alternative_stale_hours,
            )
        if include_sentiment:
            prepared_sentiment = prepare_daily_alternative(
                sentiment if sentiment is not None else pd.DataFrame(), "sentiment"
            )
            base = merge_point_in_time(
                base,
                prepared_sentiment,
                prefix="sentiment",
                stale_hours=self.config.alternative_stale_hours,
            )
        if arm_spec.include_derivatives:
            derivative_frame = _resolve_optional_frame(derivatives, asset)
            prepared_derivatives = (
                prepare_derivatives(derivative_frame, self.config.alternative_delay_hours)
                if not derivative_frame.empty
                else derivative_frame
            )
            base = merge_point_in_time(
                base,
                prepared_derivatives,
                prefix="derivatives",
                stale_hours=self.config.derivatives_stale_hours,
            )

        close = target["close"].astype(float).replace(0, np.nan)
        execution_open = target["open"].astype(float).shift(-1)
        hourly_log_return = np.log(close).diff()
        volatility = truncated_ewma_std(hourly_log_return, self.config.lookback_hours)
        base["execution_open"] = execution_open.to_numpy()
        base["reference_close"] = close.to_numpy()
        base["target_volatility"] = volatility.to_numpy()
        for horizon in sorted(set(self.config.forecast_horizons)):
            future_close = close.shift(-horizon)
            raw_return = np.log(future_close / execution_open)
            normalized_return = raw_return / volatility.replace(0, np.nan)
            suffix = f"_{horizon}h"
            base[f"future_close{suffix}"] = future_close.to_numpy()
            base[f"target_raw_return{suffix}"] = raw_return.to_numpy()
            base[f"target_normalized_return{suffix}"] = normalized_return.to_numpy()
            base[f"label_tradeable{suffix}"] = (
                raw_return > self.config.label_cost_bps / 10_000.0
            ).astype(float).to_numpy()
            base[f"label_window_closed{suffix}"] = (
                target["is_closed"].astype(bool).shift(-horizon, fill_value=False).to_numpy()
            )
        default_suffix = f"_{self.config.horizon_hours}h"
        base["future_close"] = base[f"future_close{default_suffix}"]
        base["target_raw_return"] = base[f"target_raw_return{default_suffix}"]
        base["target_normalized_return"] = base[f"target_normalized_return{default_suffix}"]
        base["label_window_closed"] = (
            target["is_closed"]
            .astype(bool)
            .shift(-self.config.horizon_hours, fill_value=False)
            .to_numpy()
        )
        base["next_hour_return"] = (
            target["open"].astype(float).shift(-2) / execution_open - 1
        ).to_numpy()
        base = base.drop(columns=["open", "close"])
        base = base[base["is_closed"].astype(bool)].reset_index(drop=True)
        if self.config.historical_gap_policy == "gap_aware_segments":
            valid = valid_continuity_mask(
                target["open_time"],
                lookback_hours=self.config.lookback_hours,
                max_horizon_hours=(
                    max(self.config.forecast_horizons) if include_labels else 0
                ),
            )
            valid_by_as_of = dict(zip(target["as_of"], valid, strict=True))
            base["continuity_valid"] = base["as_of"].map(valid_by_as_of).fillna(False).astype(float)
            base = base[base["continuity_valid"] > 0].reset_index(drop=True)
            base = base[base["market_context_complete"] > 0].reset_index(drop=True)
        if include_labels:
            required_labels = [
                f"label_window_closed_{horizon}h" for horizon in self.config.forecast_horizons
            ]
            base = base[base[required_labels].all(axis=1)].reset_index(
                drop=True
            )
            base = base.dropna(
                subset=[
                    "target_normalized_return",
                    "target_raw_return",
                    "next_hour_return",
                ]
            ).reset_index(drop=True)
        feature_columns = tuple(
            column
            for column in base.columns
            if column not in META_COLUMNS
            and not column.startswith(("target_", "future_", "label_"))
            and pd.api.types.is_numeric_dtype(base[column])
        )
        return FeatureFrame(
            asset=asset,
            arm=arm if isinstance(arm, (DataArm, DataArmSpec)) else arm_spec,
            frame=base,
            feature_columns=feature_columns,
            schema_version=(
                FEATURE_SCHEMA_VERSION_V2
                if self.config.historical_gap_policy == "gap_aware_segments"
                else FEATURE_SCHEMA_VERSION
            ),
            arm_spec=arm_spec,
        )
