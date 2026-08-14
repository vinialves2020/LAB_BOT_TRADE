from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from bottrade.backtest import select_entry_threshold, simulate_long_flat
from bottrade.config import load_config


def test_backtest_charges_both_legs_and_closes_sample() -> None:
    frame = pd.DataFrame(
        {
            "as_of": pd.date_range("2024-01-01", periods=5, freq="1h", tz="UTC"),
            "next_hour_return": [0.01] * 5,
        }
    )
    result = simulate_long_flat(
        frame,
        np.ones(5),
        threshold_return=0.1,
        cost_per_leg=0.0012,
        max_holding_hours=12,
    )
    assert result.metrics.closed_trades == 1
    assert result.metrics.turnover == 2
    assert result.timeline["transaction_cost"].sum() == pytest.approx(0.0024)
    assert result.timeline.iloc[-1]["position"] == 0


def test_threshold_candidates_include_round_trip_cost() -> None:
    config = load_config(create_dirs=False)
    config.backtest.minimum_calibration_trades = 0
    config.backtest.maximum_calibration_turnover_per_day = 100
    frame = pd.DataFrame(
        {
            "as_of": pd.date_range("2024-01-01", periods=100, freq="1h", tz="UTC"),
            "next_hour_return": np.sin(np.arange(100)) * 0.001,
        }
    )
    threshold, _ = select_entry_threshold(frame, np.full(100, 0.01), config.backtest)
    expected = [config.backtest.round_trip_cost + value / 10_000 for value in [0, 5, 10, 20, 30]]
    assert threshold in expected


def test_scaled_position_costs_and_circuit_breaker_are_applied() -> None:
    frame = pd.DataFrame(
        {
            "as_of": pd.date_range("2024-01-01", periods=6, freq="1h", tz="UTC"),
            "next_hour_return": [-0.10, 0.02, 0.02, 0.02, 0.02, 0.02],
        }
    )
    result = simulate_long_flat(
        frame,
        np.ones(len(frame)),
        threshold_return=0.1,
        cost_per_leg=0.0012,
        max_holding_hours=12,
        position_size=0.2,
        drawdown_circuit_breaker=0.01,
    )
    assert result.trades.iloc[0]["exit_reason"] == "drawdown_circuit_breaker"
    assert result.timeline.iloc[1:]["position"].sum() == 0
    assert result.metrics.turnover == pytest.approx(0.4)
    assert result.timeline["transaction_cost"].sum() == pytest.approx(0.00048)
