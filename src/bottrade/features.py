from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

import numpy as np
import pandas as pd

from bottrade.config import FeatureConfig
from bottrade.domain import Asset, DataArm

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
}
FEATURE_SCHEMA_VERSION = "features-v3"


@dataclass(frozen=True, slots=True)
class FeatureFrame:
    asset: Asset
    arm: DataArm
    frame: pd.DataFrame
    feature_columns: tuple[str, ...]
    schema_version: str = FEATURE_SCHEMA_VERSION


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
    merged[f"{prefix}_event_time"] = merged["event_time"]
    merged[f"{prefix}_available_at"] = merged["available_at"]
    merged[f"{prefix}_age_hours"] = age
    merged[f"{prefix}_missing"] = merged["event_time"].isna().astype(float)
    merged[f"{prefix}_stale"] = ((age > stale_hours) | age.isna()).astype(float)
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
        arm: DataArm = DataArm.MARKET,
        include_labels: bool = True,
    ) -> FeatureFrame:
        prepared = {symbol: _prepare_market(frame) for symbol, frame in market.items()}
        target = prepared[asset.value]
        base = target[
            [
                "as_of",
                "open_time",
                "open",
                "close",
                "is_closed",
            ]
        ].copy()
        for symbol, frame in prepared.items():
            prefix = symbol.removesuffix("USDT").lower()
            context = _context_features(frame, prefix, self.config.lag_hours)
            base = base.merge(context, on="as_of", how="left", validate="one_to_one")
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

        include_onchain = arm in {DataArm.MARKET_ONCHAIN, DataArm.MARKET_ALL}
        include_sentiment = arm in {DataArm.MARKET_SENTIMENT, DataArm.MARKET_ALL}
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

        close = target["close"].astype(float).replace(0, np.nan)
        execution_open = target["open"].astype(float).shift(-1)
        future_close = close.shift(-self.config.horizon_hours)
        hourly_log_return = np.log(close).diff()
        volatility = truncated_ewma_std(hourly_log_return, self.config.lookback_hours)
        base["execution_open"] = execution_open.to_numpy()
        base["reference_close"] = close.to_numpy()
        base["future_close"] = future_close.to_numpy()
        base["target_raw_return"] = np.log(future_close / execution_open).to_numpy()
        base["target_volatility"] = volatility.to_numpy()
        base["target_normalized_return"] = (
            base["target_raw_return"] / base["target_volatility"].replace(0, np.nan)
        )
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
        if include_labels:
            base = base[base["label_window_closed"].astype(bool)].reset_index(
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
            and pd.api.types.is_numeric_dtype(base[column])
        )
        return FeatureFrame(asset=asset, arm=arm, frame=base, feature_columns=feature_columns)
