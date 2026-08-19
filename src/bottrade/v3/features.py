from __future__ import annotations

from collections.abc import Mapping

import numpy as np
import pandas as pd

from bottrade.domain import Asset
from bottrade.features import truncated_ewma_std
from bottrade.v3.config import V3Config
from bottrade.validation import continuity_segments, valid_continuity_mask


def _utc(value: pd.Series) -> pd.Series:
    return pd.to_datetime(value, utc=True, errors="coerce")


def _normalise_market(frame: pd.DataFrame, interval_minutes: int) -> pd.DataFrame:
    data = frame.copy()
    if "open_time" not in data:
        raise ValueError("market data requires open_time")
    data["open_time"] = _utc(data["open_time"])
    if "as_of" in data:
        data["as_of"] = _utc(data["as_of"])
    else:
        data["as_of"] = data["open_time"] + pd.Timedelta(minutes=interval_minutes)
    if "is_closed" not in data:
        data["is_closed"] = True
    data = data[data["is_closed"].astype(bool)].copy()
    data = data.sort_values("open_time").drop_duplicates("open_time", keep="last")
    return data.reset_index(drop=True)


def _numeric(data: pd.DataFrame, name: str, default: float = 0.0) -> pd.Series:
    if name not in data:
        return pd.Series(default, index=data.index, dtype=float)
    return pd.to_numeric(data[name], errors="coerce")


def _zscore(values: pd.Series, window: int) -> pd.Series:
    mean = values.rolling(window, min_periods=max(3, window // 3)).mean()
    std = values.rolling(window, min_periods=max(3, window // 3)).std(ddof=0)
    return (values - mean) / std.replace(0, np.nan)


def _market_features(data: pd.DataFrame, config: V3Config) -> pd.DataFrame:
    close = _numeric(data, "close").replace(0, np.nan)
    high = _numeric(data, "high").replace(0, np.nan)
    low = _numeric(data, "low").replace(0, np.nan)
    volume = _numeric(data, "quote_volume")
    if volume.eq(0).all():
        volume = _numeric(data, "volume")
    log_close = np.log(close)
    hourly_return = log_close.diff()
    result = data[["open_time", "as_of", "open", "high", "low", "close"]].copy()
    result["volume"] = _numeric(data, "volume")
    result["quote_volume"] = _numeric(data, "quote_volume")
    result["trade_count"] = _numeric(data, "trade_count")
    result["taker_buy_base_volume"] = _numeric(data, "taker_buy_base_volume")
    result["log_return_1h"] = hourly_return
    result["return_1h"] = hourly_return
    for horizon in (3, 6, 12, 24, 72, 168):
        result[f"return_{horizon}h"] = log_close.diff(horizon)
        result[f"volatility_{horizon}h"] = hourly_return.rolling(
            horizon, min_periods=max(3, horizon // 3)
        ).std(ddof=0)
    result["ewma_volatility_1h"] = truncated_ewma_std(hourly_return, config.lookback_hours).to_numpy()
    for span in (6, 12, 24, 48, 72, 168):
        result[f"ema_{span}h"] = close.ewm(span=span, min_periods=span, adjust=False).mean()
    result["volume_z_24h"] = _zscore(np.log1p(volume.clip(lower=0)), 24)
    result["range_return"] = np.log(high / low)
    result["body_return"] = np.log(close / _numeric(data, "open").replace(0, np.nan))
    result["taker_buy_ratio"] = result["taker_buy_base_volume"] / result["volume"].replace(0, np.nan)
    result["previous_high_24h"] = high.rolling(24).max().shift(1)
    result["previous_high_72h"] = high.rolling(72).max().shift(1)
    result["previous_low_24h"] = low.rolling(24).min().shift(1)
    result["previous_low_72h"] = low.rolling(72).min().shift(1)
    segments = continuity_segments(result["open_time"], expected_frequency="1h")
    result["continuity_segment_id"] = segments.to_numpy()
    result["continuity_valid"] = valid_continuity_mask(
        result["open_time"],
        lookback_hours=config.lookback_hours,
        max_horizon_hours=max(config.horizons),
        expected_frequency="1h",
    ).to_numpy()
    return result


def _intrahour_features(frame: pd.DataFrame) -> pd.DataFrame:
    data = _normalise_market(frame, 15)
    if data.empty:
        return pd.DataFrame(columns=["as_of", "intrahour_complete"])
    data["hour_as_of"] = data["open_time"].dt.floor("1h") + pd.Timedelta(hours=1)
    data = data.sort_values("open_time").drop_duplicates("open_time", keep="last")
    data["slot"] = ((data["open_time"] - (data["hour_as_of"] - pd.Timedelta(hours=1))).dt.total_seconds() / 900).round().astype(int)
    data["sub_return"] = np.log(
        _numeric(data, "close").replace(0, np.nan) / _numeric(data, "open").replace(0, np.nan)
    )
    grouped = data.groupby("hour_as_of", sort=True)
    aggregate = grouped.agg(
        first_open=("open", "first"),
        last_close=("close", "last"),
        high_value=("high", "max"),
        low_value=("low", "min"),
        intrahour_volume=("volume", "sum"),
        intrahour_trade_count=("trade_count", "sum"),
        intrahour_taker_volume=("taker_buy_base_volume", "sum"),
        bar_count=("open_time", "size"),
        first_open_time=("open_time", "min"),
        last_open_time=("open_time", "max"),
    )
    index = aggregate.index
    aggregate["intrahour_complete"] = (
        aggregate["bar_count"].eq(4)
        & aggregate["first_open_time"].eq(index - pd.Timedelta(hours=1))
        & aggregate["last_open_time"].eq(index - pd.Timedelta(minutes=15))
    ).astype(float)
    returns = data.pivot(index="hour_as_of", columns="slot", values="sub_return").reindex(columns=range(4))
    volumes = data.pivot(index="hour_as_of", columns="slot", values="volume").reindex(columns=range(4))
    trades = data.pivot(index="hour_as_of", columns="slot", values="trade_count").reindex(columns=range(4))
    return_array = returns.to_numpy(dtype=float)
    path = np.exp(np.nancumsum(np.nan_to_num(return_array, nan=0.0), axis=1))
    drawdown = path / np.maximum.accumulate(path, axis=1) - 1.0
    drawup = path / np.minimum.accumulate(path, axis=1) - 1.0
    high = pd.to_numeric(aggregate["high_value"], errors="coerce").to_numpy(float)
    low = pd.to_numeric(aggregate["low_value"], errors="coerce").to_numpy(float)
    first = pd.to_numeric(aggregate["first_open"], errors="coerce").to_numpy(float)
    last = pd.to_numeric(aggregate["last_close"], errors="coerce").to_numpy(float)
    total_volume = pd.to_numeric(aggregate["intrahour_volume"], errors="coerce").to_numpy(float)
    first_two_volume = volumes.iloc[:, :2].sum(axis=1).to_numpy(float)
    last_two_volume = volumes.iloc[:, 2:].sum(axis=1).to_numpy(float)
    first_two_trades = trades.iloc[:, :2].sum(axis=1).to_numpy(float)
    last_two_trades = trades.iloc[:, 2:].sum(axis=1).to_numpy(float)
    result = pd.DataFrame(index=index)
    result.index.name = "as_of"
    result["intrahour_complete"] = aggregate["intrahour_complete"]
    with np.errstate(divide="ignore", invalid="ignore"):
        result["intrahour_return"] = np.log(np.divide(last, first, where=first != 0, out=np.full_like(last, np.nan)))
        finite_count = np.isfinite(return_array).sum(axis=1)
        safe_returns = np.nan_to_num(return_array, nan=0.0)
        mean_returns = np.divide(
            safe_returns.sum(axis=1), finite_count, where=finite_count > 0, out=np.full(len(result), np.nan)
        )
        mean_square = np.divide(
            (safe_returns * safe_returns).sum(axis=1),
            finite_count,
            where=finite_count > 0,
            out=np.full(len(result), np.nan),
        )
        result["intrahour_volatility"] = np.sqrt(np.maximum(mean_square - mean_returns**2, 0.0))
        result["intrahour_range"] = np.log(np.divide(high, low, where=low != 0, out=np.full_like(high, np.nan)))
    result["intrahour_drawdown"] = np.nanmin(drawdown, axis=1)
    result["intrahour_drawup"] = np.nanmax(drawup, axis=1)
    result["intrahour_close_position"] = np.divide(
        last - low,
        high - low,
        where=(high - low) != 0,
        out=np.full_like(last, np.nan),
    )
    result["intrahour_last_return"] = returns[3]
    result["intrahour_volume"] = aggregate["intrahour_volume"]
    result["intrahour_volume_concentration"] = np.divide(
        volumes.max(axis=1).to_numpy(float), total_volume, where=total_volume != 0, out=np.full(len(result), np.nan)
    )
    result["intrahour_volume_acceleration"] = np.divide(
        last_two_volume, first_two_volume, where=first_two_volume != 0, out=np.full(len(result), np.nan)
    )
    result["intrahour_trade_acceleration"] = np.divide(
        last_two_trades, first_two_trades, where=first_two_trades != 0, out=np.full(len(result), np.nan)
    )
    result["intrahour_taker_ratio"] = np.divide(
        aggregate["intrahour_taker_volume"].to_numpy(float),
        total_volume,
        where=total_volume != 0,
        out=np.full(len(result), np.nan),
    )
    return result.reset_index()


class V3FeatureBuilder:
    """Build point-in-time V3 features from official 1h and 15m candles."""

    def __init__(self, config: V3Config) -> None:
        self.config = config

    def build(
        self,
        *,
        asset: Asset,
        market: Mapping[str, pd.DataFrame],
        intrahour: Mapping[str, pd.DataFrame] | None = None,
    ) -> pd.DataFrame:
        if asset.value not in market:
            raise KeyError(f"missing target market frame for {asset.value}")
        prepared = {
            symbol: _market_features(_normalise_market(frame, 60), self.config)
            for symbol, frame in market.items()
        }
        target = prepared[asset.value].copy()
        target_prefix = target.rename(columns={column: column for column in target.columns})
        if intrahour is not None:
            for symbol, raw_intrahour in intrahour.items():
                intra = _intrahour_features(raw_intrahour)
                if symbol == asset.value:
                    target_prefix = target_prefix.merge(
                        intra, on="as_of", how="left", validate="one_to_one"
                    )
                else:
                    context = intra[
                        [
                            "as_of",
                            "intrahour_return",
                            "intrahour_volatility",
                            "intrahour_range",
                            "intrahour_close_position",
                            "intrahour_taker_ratio",
                            "intrahour_complete",
                        ]
                    ].rename(
                        columns={
                            column: f"ctx_{symbol}_{column}"
                            for column in intra.columns
                            if column != "as_of"
                        }
                    )
                    target_prefix = target_prefix.merge(
                        context, on="as_of", how="left", validate="one_to_one"
                    )
        else:
            target_prefix["intrahour_complete"] = 0.0
        target_prefix["asset"] = asset.value
        for symbol, context in prepared.items():
            if symbol == asset.value:
                continue
            ctx = context[["as_of", "return_1h", "return_6h", "return_24h", "ewma_volatility_1h"]].copy()
            ctx = ctx.rename(
                columns={
                    column: f"ctx_{symbol}_{column}"
                    for column in ctx.columns
                    if column != "as_of"
                }
            )
            target_prefix = target_prefix.merge(ctx, on="as_of", how="left", validate="one_to_one")
        context_columns = [column for column in target_prefix if column.startswith("ctx_")]
        target_prefix["market_context_complete"] = target_prefix[context_columns].notna().all(axis=1)
        target_prefix["market_context_complete"] = target_prefix["market_context_complete"].astype(float)
        intrahour_context_columns = [
            column for column in target_prefix if column.startswith("ctx_") and "intrahour" in column
        ]
        target_prefix["intrahour_context_complete"] = (
            target_prefix[intrahour_context_columns].notna().all(axis=1).astype(float)
            if intrahour_context_columns
            else 0.0
        )
        target_prefix["as_of"] = pd.to_datetime(target_prefix["as_of"], utc=True)
        return target_prefix.sort_values("as_of").reset_index(drop=True)
