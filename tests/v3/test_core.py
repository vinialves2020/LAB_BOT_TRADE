from __future__ import annotations

import numpy as np
import pandas as pd

from bottrade.domain import Asset
from bottrade.v3.backtest import signal_ceiling_backtest
from bottrade.v3.candidates import build_candidates
from bottrade.v3.config import load_v3_config
from bottrade.v3.features import V3FeatureBuilder
from bottrade.v3.labels import label_candidates
from bottrade.v3.statistics import (
    autocorrelation_adjusted_sharpe,
    block_bootstrap_sharpe_ci,
    probability_of_backtest_overfitting,
)


def _market(hours: int = 260, start: str = "2024-01-01") -> pd.DataFrame:
    times = pd.date_range(start, periods=hours, freq="1h", tz="UTC")
    close = 100.0 * np.exp(np.linspace(0, 0.5, hours))
    return pd.DataFrame(
        {
            "open_time": times,
            "open": close * 0.999,
            "high": close * 1.002,
            "low": close * 0.997,
            "close": close,
            "volume": np.full(hours, 100.0),
            "quote_volume": np.full(hours, 10_000.0),
            "trade_count": np.full(hours, 100.0),
            "taker_buy_base_volume": np.full(hours, 52.0),
            "is_closed": True,
        }
    )


def _intrahour(hours: int = 260, start: str = "2024-01-01") -> pd.DataFrame:
    times = pd.date_range(start, periods=hours * 4, freq="15min", tz="UTC")
    close = 100.0 * np.exp(np.linspace(0, 0.5, hours * 4))
    return pd.DataFrame(
        {
            "open_time": times,
            "open": close * 0.999,
            "high": close * 1.002,
            "low": close * 0.997,
            "close": close,
            "volume": np.full(len(times), 25.0),
            "quote_volume": np.full(len(times), 2_500.0),
            "trade_count": np.full(len(times), 25.0),
            "taker_buy_base_volume": np.full(len(times), 13.0),
            "is_closed": True,
        }
    )


def test_v3_config_is_strict_and_holdout_is_fixed() -> None:
    config = load_v3_config("config/v3.yaml")
    assert config.protocol_version == "v3"
    assert config.seeds == (11, 23, 37, 53, 71)
    assert config.purge_hours == 12
    assert config.holdout_start.startswith("2025-08-01")
    assert config.holdout_end.startswith("2026-07-31")


def test_v3_features_use_four_closed_15m_bars_and_context() -> None:
    config = load_v3_config("config/v3.yaml")
    market = {asset.value: _market() for asset in Asset}
    intra = {asset.value: _intrahour() for asset in Asset}
    frame = V3FeatureBuilder(config).build(
        asset=Asset.BTCUSDT,
        market=market,
        intrahour=intra,
    )
    assert frame["intrahour_complete"].iloc[-1] == 1.0
    assert frame["market_context_complete"].iloc[-1] == 1.0
    assert {"intrahour_drawdown", "intrahour_close_position", "ctx_ETHUSDT_return_1h"}.issubset(frame.columns)


def test_v3_candidate_ids_are_stable_and_do_not_contain_labels() -> None:
    config = load_v3_config("config/v3.yaml")
    market = {asset.value: _market() for asset in Asset}
    intra = {asset.value: _intrahour() for asset in Asset}
    frame = V3FeatureBuilder(config).build(asset=Asset.BTCUSDT, market=market, intrahour=intra)
    candidates_a = build_candidates(frame, asset=Asset.BTCUSDT, config=config)
    candidates_b = build_candidates(frame, asset=Asset.BTCUSDT, config=config)
    assert candidates_a["candidate_id"].tolist() == candidates_b["candidate_id"].tolist()
    assert not {"future_close", "mfe", "mae", "net_return_1x"}.intersection(candidates_a.columns)


def test_v3_labels_apply_stop_first_and_cost_scenarios() -> None:
    config = load_v3_config("config/v3.yaml")
    as_of = pd.Timestamp("2024-02-01 00:00:00Z")
    candidates = pd.DataFrame(
        {
            "candidate_id": ["candidate-1"],
            "asset": [Asset.BTCUSDT.value],
            "strategy_family": ["reversal"],
            "variant_id": ["reversal_3h_z2_h3"],
            "horizon_hours": [3],
            "signal_strength": [2.0],
            "as_of": [as_of],
            "reference_price": [100.0],
            "ewma_volatility_1h": [0.01],
            "take_profit_return": [0.0075],
            "stop_loss_return": [-0.01],
            "continuity_segment_id": ["segment-0000"],
            "feature_schema_version": ["features-v5"],
            "cost_model_version": ["v3-cost-fallback-1"],
        }
    )
    times = pd.date_range(as_of, periods=12, freq="15min", tz="UTC")
    close = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
    bars = pd.DataFrame(
        {
            "open_time": times,
            "open": close,
            "high": [100.2, 100.2, 100.9, 100.9, 100.9, 100.9, 100.9, 100.9, 100.9, 100.9, 100.9, 100.9],
            "low": [99.8, 99.8, 98.8, 99.8, 99.8, 99.8, 99.8, 99.8, 99.8, 99.8, 99.8, 99.8],
            "close": close,
            "is_closed": True,
        }
    )
    labels = label_candidates(candidates, intrahour={Asset.BTCUSDT.value: bars}, config=config)
    assert labels.iloc[0]["outcome"] == "stop_loss"
    assert bool(labels.iloc[0]["label_valid"])
    assert labels.iloc[0]["net_return_2x"] < labels.iloc[0]["net_return_1x"]


def test_v3_statistics_are_deterministic() -> None:
    returns = np.array([0.01, -0.005, 0.003, 0.002, -0.001] * 20)
    assert np.isfinite(autocorrelation_adjusted_sharpe(returns))
    assert block_bootstrap_sharpe_ci(returns, samples=100, seed=11) == block_bootstrap_sharpe_ci(
        returns, samples=100, seed=11
    )
    matrix = np.vstack([returns, returns[::-1], returns * 0.5])
    assert 0.0 <= probability_of_backtest_overfitting(matrix) <= 1.0


def test_signal_ceiling_rejects_invalid_labels_without_trades() -> None:
    config = load_v3_config("config/v3.yaml")
    labels = pd.DataFrame(
        {
            "candidate_id": ["invalid"],
            "asset": ["BTCUSDT"],
            "label_valid": [False],
            "net_return_1x": [np.nan],
            "net_return_2x": [np.nan],
            "net_return_3x": [np.nan],
        }
    )
    result = signal_ceiling_backtest(labels, config=config)
    assert result.metrics["closed_trades"] == 0
