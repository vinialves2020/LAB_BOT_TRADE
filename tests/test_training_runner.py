from __future__ import annotations

import json

import numpy as np
import pandas as pd
import pytest

from bottrade.backtest import CalibrationEligibilityError
from bottrade.dataset import DatasetBundle
from bottrade.domain import Asset, DataArm, ModelFamily
from bottrade.training import (
    CandidateRejectedError,
    ExperimentRunner,
    HyperparameterSearchRejectedError,
)


def test_hyperparameter_search_rejects_an_all_failed_study(app_config, monkeypatch) -> None:
    runner = ExperimentRunner(app_config)
    monkeypatch.setattr(runner, "_score_params", lambda *args, **kwargs: -1_000_000.0)
    with pytest.raises(
        HyperparameterSearchRejectedError,
        match="no hyperparameter trial produced an eligible calibration strategy",
    ):
        runner.search(object(), ModelFamily.RANDOM_FOREST, [], trials=2)  # type: ignore[arg-type]


def test_official_market_search_rejection_is_protocol_eligible(app_config, tmp_path) -> None:
    dataset = DatasetBundle(
        asset=Asset.ETHUSDT,
        arm=DataArm.MARKET,
        frame=pd.DataFrame(),
        feature_columns=("feature",),
        data_version="c" * 20,
        schema_version="features-v3",
        path=tmp_path / "unused.parquet",
    )
    path = ExperimentRunner(app_config)._record_search_rejection(
        dataset=dataset,
        family=ModelFamily.RANDOM_FOREST,
        trials=app_config.training.max_trials,
        max_search_folds=None,
        source_control={"commit": "a" * 40, "dirty": False},
    )
    record = json.loads(path.read_text(encoding="utf-8"))
    assert record["protocol_rejection_eligible"] is True
    assert record["covers_arms"] == [arm.value for arm in DataArm]


def test_final_seed_rejection_is_recorded(app_config, monkeypatch, tmp_path) -> None:
    times = pd.date_range("2024-01-01", "2024-04-30", freq="1h", tz="UTC")
    frame = pd.DataFrame(
        {
            "as_of": times,
            "feature": np.zeros(len(times)),
            "target_normalized_return": np.zeros(len(times)),
            "target_volatility": 0.01,
            "next_hour_return": 0.0,
            "reference_close": 100.0,
        }
    )
    dataset = DatasetBundle(
        asset=Asset.BTCUSDT,
        arm=DataArm.MARKET,
        frame=frame,
        feature_columns=("feature",),
        data_version="b" * 20,
        schema_version="features-v3",
        path=tmp_path / "synthetic.parquet",
    )
    app_config.training.train_months = 1
    app_config.training.calibration_months = 1
    app_config.training.test_months = 1
    app_config.training.holdout_start = "2024-05-01T00:00:00Z"
    runner = ExperimentRunner(app_config)

    def reject(*args, **kwargs):
        raise CalibrationEligibilityError("activity gate failed")

    monkeypatch.setattr(runner, "_evaluate_fold", reject)
    with pytest.raises(CandidateRejectedError) as captured:
        runner.run(
            dataset,
            ModelFamily.RANDOM_FOREST,
            trials=1,
            seeds=[23],
            params_override={},
        )
    record = json.loads(captured.value.rejection_path.read_text(encoding="utf-8"))
    assert record["status"] == "rejected"
    assert record["failed_seed"] == 23
    assert record["failed_fold"] == "2024-04"


def test_random_forest_experiment_runner_writes_reproducible_bundle(app_config, tmp_path) -> None:
    app_config.training.train_months = 1
    app_config.training.calibration_months = 1
    app_config.training.test_months = 1
    app_config.training.holdout_start = "2024-06-01T00:00:00Z"
    app_config.training.holdout_end = "2024-06-30T23:59:59Z"
    app_config.training.explainability_samples = 16
    app_config.training.permutation_repeats = 1
    times = pd.date_range("2024-01-01", "2024-07-31", freq="1h", tz="UTC")
    regime = np.where((np.arange(len(times)) // 24) % 2 == 0, 1.0, -1.0)
    hourly_return = 0.002 * regime
    close = 100.0 * np.cumprod(1.0 + hourly_return)
    frame = pd.DataFrame(
        {
            "as_of": times,
            "feature_regime": regime,
            "feature_slow": pd.Series(regime).rolling(6, min_periods=1).mean().to_numpy(),
            "target_normalized_return": regime,
            "target_volatility": 0.01,
            "next_hour_return": hourly_return,
            "reference_close": close,
        }
    )
    dataset = DatasetBundle(
        asset=Asset.BTCUSDT,
        arm=DataArm.MARKET,
        frame=frame,
        feature_columns=("feature_regime", "feature_slow"),
        data_version="a" * 20,
        schema_version="features-v2",
        path=tmp_path / "synthetic.parquet",
    )
    result = ExperimentRunner(app_config).run(
        dataset,
        ModelFamily.RANDOM_FOREST,
        trials=1,
        max_search_folds=1,
        seeds=[11],
        params_override={
            "n_estimators": 10,
            "max_depth": 4,
            "min_samples_leaf": 2,
            "max_features": 1.0,
            "n_jobs": 1,
        },
    )
    metadata = json.loads((result.registry_path / "metadata.json").read_text("utf-8"))
    experiment = json.loads(
        (
            app_config.project.artifact_dir
            / "experiments"
            / Asset.BTCUSDT.value
            / DataArm.MARKET.value
            / ModelFamily.RANDOM_FOREST.value
            / result.run_id
            / "experiment.json"
        ).read_text("utf-8")
    )
    assert (result.registry_path / "model.onnx").exists()
    assert metadata["onnx_verified"] is True
    assert metadata["protocol_eligible"] is False
    assert experiment["source_control"]["commit"]
    assert experiment["seed_metrics"].keys() == {"11"}
