from __future__ import annotations

import numpy as np
import pandas as pd

from bottrade.backtest import simulate_long_flat


def test_golden_replay_across_four_regimes_remains_finite() -> None:
    rng = np.random.default_rng(7)
    regimes = np.concatenate(
        [
            np.full(100, 0.001),
            np.full(100, -0.001),
            np.sin(np.arange(100)) * 0.0005,
            rng.normal(0, 0.01, 100),
        ]
    )
    frame = pd.DataFrame(
        {
            "as_of": pd.date_range("2024-01-01", periods=400, freq="1h", tz="UTC"),
            "next_hour_return": regimes,
        }
    )
    predictions = pd.Series(regimes).rolling(3, min_periods=1).mean().to_numpy() * 3
    result = simulate_long_flat(
        frame,
        predictions,
        threshold_return=0.0024,
        cost_per_leg=0.0012,
        max_holding_hours=12,
    )
    values = result.metrics.to_dict().values()
    assert all(np.isfinite(float(value)) for value in values)
    assert (result.timeline["equity"] > 0).all()
