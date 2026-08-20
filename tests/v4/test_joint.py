from __future__ import annotations

from dataclasses import replace

import numpy as np
import pandas as pd

from bottrade.v4.config import load_v4_config
from bottrade.v4.joint import (
    JointEnsemble,
    JointPolicy,
    fit_probability_calibrator,
    select_joint_stateful_trades,
)


def test_probability_calibrator_is_monotone_and_bounded() -> None:
    probabilities = np.linspace(0.05, 0.95, 40)
    labels = (probabilities > 0.55).astype(int)
    calibrator = fit_probability_calibrator(probabilities, labels)
    transformed = calibrator.transform(probabilities)
    assert np.isfinite(transformed).all()
    assert ((transformed >= 0.0) & (transformed <= 1.0)).all()
    assert np.all(np.diff(transformed) >= -1e-9)


def test_joint_ensemble_has_five_members_for_hgb() -> None:
    config = load_v4_config()
    rng = np.random.default_rng(22)
    x = rng.normal(size=(100, 4)).astype(np.float32)
    target_return = (x[:, 0] * 0.01 - x[:, 1] * 0.005).astype(np.float32)
    target_class = (target_return > 0.0024).astype(int)
    ensemble = JointEnsemble.create(
        family="hist_gradient_boosting",
        config=config,
        feature_names=("a", "b", "c", "d"),
        params={"max_iter": 12, "max_leaf_nodes": 7, "min_samples_leaf": 5},
    )
    details = ensemble.fit(x, target_return, target_class, np.arange(80))
    regression = ensemble.predict_reg_members(x, np.arange(80, 100))
    probabilities = ensemble.predict_prob_members(x, np.arange(80, 100))
    assert details["members"] == 5
    assert regression.shape == (5, 20)
    assert probabilities.shape == (5, 20)
    assert ((probabilities >= 0.0) & (probabilities <= 1.0)).all()


def test_joint_policy_requires_probability_and_return() -> None:
    config = replace(load_v4_config(), stateful_hourly=True, horizon_hours=1)
    times = pd.date_range("2024-01-01", periods=5, freq="1h", tz="UTC")
    frame = pd.DataFrame(
        {
            "as_of": times,
            "entry_time": times,
            "exit_time": times,
            "entry_price": [100.0, 101.0, 101.0, 101.0, 101.0],
            "exit_price": [101.0, 101.0, 102.0, 102.0, 102.0],
            "gross_return": [0.01, 0.0, 0.01, 0.0, 0.0],
            "label_valid": [True] * 5,
        }
    )
    predictions = np.array([0.004, 0.004, 0.004, 0.0, 0.0])
    probabilities = np.array([0.40, 0.70, 0.70, 0.0, 0.0])
    trades = select_joint_stateful_trades(
        frame,
        predictions,
        np.zeros(5),
        probabilities,
        config=config,
        policy=JointPolicy(probability_threshold=0.55, margin_bps=0),
    )
    assert len(trades) == 1
    assert trades.iloc[0]["entry_time"] == times[1]

