from __future__ import annotations

import numpy as np
import pandas as pd

from bottrade.config import load_config
from bottrade.domain import Asset, DataArmSpec, ModelFamily
from bottrade.features import FeatureBuilder
from bottrade.models.transformer import TemporalTransformer
from bottrade.multihorizon import select_horizon_forecast
from bottrade.statistics import probability_of_backtest_overfitting
from bottrade.validation import continuity_segments, valid_continuity_mask, walk_forward_folds


def _market(hours: int = 240) -> pd.DataFrame:
    start = pd.Timestamp("2024-01-01", tz="UTC")
    open_time = pd.date_range(start, periods=hours, freq="1h", tz="UTC")
    close = 100.0 + np.arange(hours, dtype=float) * 0.01
    return pd.DataFrame(
        {
            "open_time": open_time,
            "close_time": open_time + pd.Timedelta(hours=1) - pd.Timedelta(milliseconds=1),
            "as_of": open_time + pd.Timedelta(hours=1),
            "open": close,
            "high": close + 0.1,
            "low": close - 0.1,
            "close": close + 0.02,
            "volume": np.full(hours, 10.0),
            "quote_volume": np.full(hours, 1000.0),
            "trade_count": np.full(hours, 20.0),
            "taker_buy_base_volume": np.full(hours, 5.0),
            "taker_buy_quote_volume": np.full(hours, 500.0),
            "is_closed": True,
        }
    )


def test_v2_config_and_composable_arms() -> None:
    config = load_config("config/v2.yaml", create_dirs=False)
    assert config.training.protocol_version == "v2"
    assert config.training.seeds == [11, 23, 37, 53, 71]
    assert config.features.forecast_horizons == [3, 6, 12]
    spec = DataArmSpec.from_id("market_1h_15m_derivatives_all")
    assert spec.include_intrahour and spec.include_derivatives
    assert spec.include_onchain and spec.include_sentiment
    assert spec.components == (
        "market_1h",
        "intrahour_15m",
        "derivatives",
        "onchain",
        "sentiment",
    )
    assert ModelFamily.HIST_GRADIENT_BOOSTING.value == "hist_gradient_boosting"


def test_gap_segments_reject_lookback_or_label_crossing() -> None:
    timestamps = pd.date_range("2024-01-01", periods=30, freq="1h", tz="UTC").delete(15)
    segments = continuity_segments(timestamps)
    valid = valid_continuity_mask(
        timestamps, lookback_hours=4, max_horizon_hours=3
    )
    assert segments.nunique() == 2
    assert not bool(valid.iloc[14])
    assert bool(valid.iloc[22])


def test_v2_labels_include_all_horizons_and_15m_completion() -> None:
    base = _market()
    market = {"BTCUSDT": base, "ETHUSDT": base.copy(), "SOLUSDT": base.copy()}
    quarter = []
    for row in base.itertuples(index=False):
        for offset in (0, 15, 30, 45):
            open_time = row.open_time + pd.Timedelta(minutes=offset)
            quarter.append(
                {
                    "open_time": open_time,
                    "as_of": open_time + pd.Timedelta(minutes=15),
                    "open": row.open,
                    "high": row.high,
                    "low": row.low,
                    "close": row.close,
                    "volume": 2.0,
                    "quote_volume": 200.0,
                    "trade_count": 4.0,
                    "taker_buy_base_volume": 1.0,
                    "is_closed": True,
                }
            )
    config = load_config("config/v2.yaml", create_dirs=False)
    builder = FeatureBuilder(config.features)
    featured = builder.build(
        asset=Asset.BTCUSDT,
        market=market,
        arm="market_1h_15m",
        intrahour={symbol: pd.DataFrame(quarter) for symbol in market},
    )
    assert {"target_normalized_return_3h", "target_normalized_return_6h", "target_normalized_return_12h"}.issubset(featured.frame)
    assert any("intrahour_complete" in name for name in featured.feature_columns)
    assert featured.schema_version == "features-v4"


def test_horizon_selection_and_pbo_are_deterministic() -> None:
    choice = select_horizon_forecast(
        horizons=(3, 6, 12),
        expected_gross_returns=(0.004, 0.010, 0.007),
        probabilities=(0.70, 0.72, 0.80),
        round_trip_cost=0.0024,
        probability_threshold=0.60,
        margin_bps=10,
    )
    assert choice is not None and choice.horizon_hours == 6
    matrix = np.asarray([[0.1, 0.2, 0.0, 0.1], [0.0, 0.0, 0.1, 0.0]])
    assert 0.0 <= probability_of_backtest_overfitting(matrix) <= 1.0


def test_transformer_patch_encoder_has_joint_v2_heads() -> None:
    import torch

    model = TemporalTransformer(
        n_features=4,
        sequence_length=24,
        d_model=8,
        nhead=2,
        num_layers=1,
        dim_feedforward=16,
        dropout=0.1,
        patch_length=4,
        patch_stride=2,
        horizon_count=3,
    )
    regression, classification_logits = model(torch.zeros(2, 24, 4))
    assert regression.shape == (2, 3)
    assert classification_logits.shape == (2, 3)
    assert model.n_patches == 11


def test_v2_walk_forward_exposes_segment_coverage() -> None:
    timestamps = pd.date_range("2020-01-01", periods=24 * 30 * 31, freq="1h", tz="UTC")
    folds = walk_forward_folds(
        timestamps,
        train_months=24,
        calibration_months=3,
        test_months=1,
        purge_hours=12,
        segment_ids=pd.Series(["segment-0000"] * len(timestamps)),
        minimum_coverage=0.95,
    )
    assert folds
    assert folds[0].coverage >= 0.95
    assert folds[0].train_segments == ("segment-0000",)
