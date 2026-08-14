from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from bottrade.config import load_config
from bottrade.domain import Asset, DataArm
from bottrade.features import (
    FeatureBuilder,
    merge_point_in_time,
    prepare_daily_alternative,
    truncated_ewma_std,
)


def test_point_in_time_join_never_uses_unavailable_value() -> None:
    base = pd.DataFrame(
        {"as_of": pd.to_datetime(["2024-01-02T12:00:00Z", "2024-01-03T01:00:00Z"])}
    )
    raw = pd.DataFrame(
        {
            "event_time": pd.to_datetime(["2024-01-02T00:00:00Z"]),
            "available_at": pd.to_datetime(["2024-01-03T00:00:00Z"]),
            "onchain_value": [10.0],
        }
    )
    joined = merge_point_in_time(
        base,
        prepare_daily_alternative(raw, "onchain"),
        prefix="onchain",
        stale_hours=72,
    )
    assert np.isnan(joined.loc[0, "onchain_value"])
    assert joined.loc[0, "onchain_missing"] == 1
    assert joined.loc[1, "onchain_value"] == 10
    assert joined.loc[1, "onchain_event_time"] == raw.loc[0, "event_time"]
    assert joined.loc[1, "onchain_available_at"] == raw.loc[0, "available_at"]


def test_empty_alternative_keeps_auditable_timestamps_and_missing_flags() -> None:
    base = pd.DataFrame({"as_of": pd.to_datetime(["2024-01-02T12:00:00Z"])})
    joined = merge_point_in_time(
        base,
        pd.DataFrame(),
        prefix="sentiment",
        stale_hours=72,
    )
    assert pd.isna(joined.loc[0, "sentiment_event_time"])
    assert pd.isna(joined.loc[0, "sentiment_available_at"])
    assert joined.loc[0, "sentiment_missing"] == 1
    assert joined.loc[0, "sentiment_stale"] == 1


def test_label_is_next_open_to_three_hour_close(market_frames: dict[str, pd.DataFrame]) -> None:
    config = load_config(create_dirs=False)
    featured = FeatureBuilder(config.features).build(
        asset=Asset.BTCUSDT,
        market=market_frames,
        arm=DataArm.MARKET,
    )
    row = featured.frame.iloc[10]
    original_index = market_frames["BTCUSDT"].index[
        market_frames["BTCUSDT"]["as_of"] == row["as_of"]
    ][0]
    expected = np.log(
        market_frames["BTCUSDT"].loc[original_index + 3, "close"]
        / market_frames["BTCUSDT"].loc[original_index + 1, "open"]
    )
    assert row["target_raw_return"] == pytest.approx(expected)
    assert all(column.startswith(("market_", "calendar_")) for column in featured.feature_columns)


def test_all_arm_exposes_staleness_flags(market_frames: dict[str, pd.DataFrame]) -> None:
    config = load_config(create_dirs=False)
    days = pd.date_range("2023-12-01", periods=60, freq="1D", tz="UTC")
    onchain = pd.DataFrame(
        {
            "event_time": days,
            "available_at": days + pd.Timedelta(hours=24),
            "onchain_active_addresses": np.arange(60, dtype=float) + 1,
        }
    )
    sentiment = pd.DataFrame(
        {
            "event_time": days,
            "available_at": days + pd.Timedelta(hours=24),
            "sentiment_fear_greed": np.linspace(20, 80, 60),
        }
    )
    featured = FeatureBuilder(config.features).build(
        asset=Asset.BTCUSDT,
        market=market_frames,
        onchain=onchain,
        sentiment=sentiment,
        arm=DataArm.MARKET_ALL,
    )
    assert "onchain_stale" in featured.feature_columns
    assert "sentiment_stale" in featured.feature_columns


def test_label_volatility_has_a_hard_168_hour_memory() -> None:
    rng = np.random.default_rng(123)
    tail = rng.normal(0, 0.01, 168)
    first = pd.Series(np.r_[rng.normal(0, 0.2, 100), tail])
    second = pd.Series(np.r_[rng.normal(0, 2.0, 100), tail])
    first_value = truncated_ewma_std(first, 168).iloc[-1]
    second_value = truncated_ewma_std(second, 168).iloc[-1]
    expected = pd.Series(tail).ewm(span=168, adjust=True).std(bias=False).iloc[-1]
    assert first_value == pytest.approx(second_value, abs=1e-12)
    assert first_value == pytest.approx(expected, rel=1e-10)


def test_label_never_uses_an_incomplete_future_candle(
    market_frames: dict[str, pd.DataFrame],
) -> None:
    config = load_config(create_dirs=False)
    for frame in market_frames.values():
        frame.loc[frame.index[-1], "is_closed"] = False
    featured = FeatureBuilder(config.features).build(
        asset=Asset.BTCUSDT,
        market=market_frames,
        arm=DataArm.MARKET,
    )
    incomplete_as_of = market_frames["BTCUSDT"].iloc[-1]["as_of"]
    latest_allowed = incomplete_as_of - pd.Timedelta(hours=config.features.horizon_hours)
    assert featured.frame["as_of"].max() < latest_allowed
    assert featured.frame["label_window_closed"].all()
