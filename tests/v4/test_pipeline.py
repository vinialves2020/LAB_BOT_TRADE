from __future__ import annotations

import numpy as np
import pandas as pd

from bottrade.domain import Asset
from bottrade.v4.backtest import (
    Policy,
    fit_return_calibrator,
    select_stateful_trades,
    select_trades,
)
from bottrade.v4.config import load_v4_config
from bottrade.v4.features import build_direct_dataset, build_features
from bottrade.v4.model import XGBEnsemble


def _market(hours: int = 240, start: str = "2024-01-01") -> pd.DataFrame:
    open_time = pd.date_range(start, periods=hours, freq="1h", tz="UTC")
    close = 100.0 * np.exp(np.linspace(0.0, 0.25, hours))
    return pd.DataFrame(
        {
            "open_time": open_time,
            "open": close * 0.999,
            "high": close * 1.002,
            "low": close * 0.997,
            "close": close,
            "volume": 100.0,
            "quote_volume": 10_000.0,
            "trade_count": 100,
            "taker_buy_base_volume": 52.0,
            "taker_buy_quote_volume": 5_200.0,
            "is_closed": True,
        }
    )


def _intrahour(hours: int = 240, start: str = "2024-01-01") -> pd.DataFrame:
    open_time = pd.date_range(start, periods=hours * 4, freq="15min", tz="UTC")
    close = 100.0 * np.exp(np.linspace(0.0, 0.25, hours * 4))
    return pd.DataFrame(
        {
            "open_time": open_time,
            "open": close * 0.999,
            "high": close * 1.002,
            "low": close * 0.997,
            "close": close,
            "volume": 25.0,
            "quote_volume": 2_500.0,
            "trade_count": 25,
            "taker_buy_base_volume": 13.0,
            "taker_buy_quote_volume": 1_300.0,
            "is_closed": True,
        }
    )


def test_v4_feature_schema_excludes_lookahead_validity_mask() -> None:
    config = load_v4_config()
    market = {asset.value: _market() for asset in Asset}
    intra = {asset.value: _intrahour() for asset in Asset}
    features = build_features(
        asset=Asset.BTCUSDT,
        market=market,
        intrahour=intra,
        config=config,
    )
    assert "continuity_valid" not in features.columns
    assert "intrahour_close_position" in features.columns
    assert features["as_of"].is_monotonic_increasing


def test_v4_direct_label_uses_next_open_and_exact_12h_close() -> None:
    config = load_v4_config()
    market = {asset.value: _market() for asset in Asset}
    intra = {asset.value: _intrahour() for asset in Asset}
    features = build_features(
        asset=Asset.BTCUSDT,
        market=market,
        intrahour=intra,
        config=config,
    )
    dataset = build_direct_dataset(
        asset=Asset.BTCUSDT,
        features=features,
        market=market[Asset.BTCUSDT.value],
        config=config,
    )
    valid = dataset.frame[dataset.frame["label_valid"]].iloc[0]
    assert valid["entry_time"] == valid["as_of"]
    assert valid["exit_time"] - valid["entry_time"] == pd.Timedelta(hours=11)
    expected = float(valid["exit_price"] / valid["entry_price"] - 1.0)
    assert np.isclose(valid["gross_return"], expected)


def test_v4_gap_invalidates_label_without_interpolation() -> None:
    config = load_v4_config()
    market = {asset.value: _market() for asset in Asset}
    intra = {asset.value: _intrahour() for asset in Asset}
    gap_market = market[Asset.BTCUSDT.value].drop(index=100).reset_index(drop=True)
    features = build_features(
        asset=Asset.BTCUSDT,
        market={**market, Asset.BTCUSDT.value: gap_market},
        intrahour={**intra, Asset.BTCUSDT.value: _intrahour()},
        config=config,
    )
    dataset = build_direct_dataset(
        asset=Asset.BTCUSDT,
        features=features,
        market=gap_market,
        config=config,
    )
    invalid = dataset.frame[dataset.frame["invalid_reason"] == "market_gap_in_horizon"]
    assert not invalid.empty


def test_v4_xgb_ensemble_has_five_members_and_stable_schema() -> None:
    config = load_v4_config()
    rng = np.random.default_rng(11)
    x = rng.normal(size=(120, 4)).astype(np.float32)
    y = (x[:, 0] * 0.1 - x[:, 1] * 0.05).astype(np.float32)
    ensemble = XGBEnsemble.create(
        config=config,
        feature_names=("a", "b", "c", "d"),
        params={"n_estimators": 12, "max_depth": 3, "n_jobs": 1},
    )
    details = ensemble.fit(x, y, np.arange(100))
    mean, deviation = ensemble.predict_summary(x, np.arange(100, 120))
    assert details["members"] == 5
    assert mean.shape == (20,)
    assert deviation.shape == (20,)
    assert np.isfinite(mean).all()


def test_v4_xgb_onnx_members_match_native(tmp_path) -> None:
    import pytest

    pytest.importorskip("onnxmltools")
    pytest.importorskip("onnxruntime")
    config = load_v4_config()
    rng = np.random.default_rng(12)
    x = rng.normal(size=(80, 3)).astype(np.float32)
    y = (x[:, 0] * 0.1).astype(np.float32)
    ensemble = XGBEnsemble.create(
        config=config,
        feature_names=("a", "b", "c"),
        params={"n_estimators": 8, "max_depth": 3, "n_jobs": 1},
    )
    ensemble.fit(x, y, np.arange(60))
    paths = ensemble.export_onnx(tmp_path)
    assert len(paths) == 5
    assert ensemble.verify_onnx(paths, x, np.arange(60, 80)) < 1e-4


def test_v4_policy_deducts_cost_and_prevents_overlapping_positions() -> None:
    config = load_v4_config()
    frame = pd.DataFrame(
        {
            "as_of": pd.date_range("2024-01-01", periods=4, freq="1h", tz="UTC"),
            "entry_time": pd.date_range("2024-01-01", periods=4, freq="1h", tz="UTC"),
            "exit_time": pd.date_range("2024-01-01 04:00", periods=4, freq="1h", tz="UTC"),
            "gross_return": [0.01, 0.01, -0.01, 0.01],
            "label_valid": [True, True, True, True],
        }
    )
    trades = select_trades(
        frame,
        np.full(4, 0.01),
        np.zeros(4),
        config=config,
        policy=Policy(0),
    )
    assert len(trades) == 1
    assert np.isclose(trades.iloc[0]["net_return"], 0.01 - 0.0024)


def test_v4_return_calibration_never_inverts_a_negative_slope() -> None:
    predictions = np.linspace(-0.01, 0.01, 40)
    targets = -predictions
    calibrator = fit_return_calibrator(predictions, targets)
    assert calibrator.slope == 0.0


def test_v4_return_calibration_shrinks_overconfident_forecasts() -> None:
    predictions = np.linspace(-0.02, 0.04, 40)
    targets = 0.25 * predictions + 0.001
    calibrator = fit_return_calibrator(predictions, targets)
    assert 0.20 < calibrator.slope < 0.30


def test_v4_stateful_hourly_policy_closes_on_negative_forecast() -> None:
    config = load_v4_config()
    # A frozen dataclass replacement keeps the test explicit without changing
    # the official 12h configuration.
    from dataclasses import replace

    config = replace(config, stateful_hourly=True, horizon_hours=1)
    times = pd.date_range("2024-01-01", periods=5, freq="1h", tz="UTC")
    frame = pd.DataFrame(
        {
            "as_of": times,
            "entry_time": times,
            "exit_time": times,
            "entry_price": [100.0, 101.0, 102.0, 100.0, 100.0],
            "exit_price": [101.0, 102.0, 100.0, 100.0, 100.0],
            "gross_return": [0.01, 0.0099, -0.0196, 0.0, 0.0],
            "label_valid": [True, True, True, True, True],
        }
    )
    trades = select_stateful_trades(
        frame,
        np.array([0.004, 0.003, -0.004, 0.0, 0.0]),
        np.zeros(5),
        config=config,
        policy=Policy(0),
    )
    assert len(trades) == 1
    assert trades.iloc[0]["entry_price"] == 100.0
    assert trades.iloc[0]["exit_price"] == 102.0
