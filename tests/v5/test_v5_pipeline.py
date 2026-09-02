from __future__ import annotations

from pathlib import Path

import numpy as np

from bottrade.v5.backtest import compute_predictive_metrics, evaluate_gates
from bottrade.v5.config import V5Config, load_v5_config
from bottrade.v5.models.random_forest import RFEnsemble
from bottrade.v5.models.transformer import PatchTransformerEnsemble


def test_v5_config_defaults_and_load(tmp_path: Path) -> None:
    config = V5Config()
    assert config.rf_n_estimators == 100
    assert config.tf_patch_length == 6
    assert config.tf_patch_stride == 3
    assert config.minimum_asset_monthly_trades == 4

    yaml_content = """
project:
  protocol_version: test-v5
models:
  random_forest:
    n_estimators: 50
    max_depth: 8
  transformer:
    d_model: 32
    epochs: 2
"""
    yaml_file = tmp_path / "test_v5.yaml"
    yaml_file.write_text(yaml_content, encoding="utf-8")
    loaded = load_v5_config(yaml_file)
    assert loaded.protocol_version == "test-v5"
    assert loaded.rf_n_estimators == 50
    assert loaded.rf_max_depth == 8
    assert loaded.tf_d_model == 32
    assert loaded.tf_epochs == 2


def test_rf_ensemble_fit_predict_onnx(tmp_path: Path) -> None:
    config = V5Config(
        rf_n_estimators=10,
        rf_max_depth=4,
        rf_max_samples=0.8,
        seeds=(11, 23),
        rf_n_jobs=1,
    )
    feature_names = ("f1", "f2", "f3", "f4")
    ensemble = RFEnsemble.create(
        config=config,
        feature_names=feature_names,
        seeds=(11, 23),
    )

    rng = np.random.default_rng(42)
    n_samples = 150
    x = rng.normal(size=(n_samples, 4)).astype(np.float32)
    y = (0.5 * x[:, 0] - 0.2 * x[:, 1] + rng.normal(scale=0.1, size=n_samples)).astype(np.float32)
    train_idx = np.arange(100)

    fit_info = ensemble.fit(x, y, train_idx)
    assert fit_info["train_samples"] == 100
    assert fit_info["members"] == 2

    test_idx = np.arange(100, 150)
    mean_preds, std_preds = ensemble.predict_summary(x, test_idx)
    assert len(mean_preds) == 50
    assert len(std_preds) == 50
    assert np.all(np.isfinite(mean_preds))

    # Test ONNX export & verification
    onnx_dir = tmp_path / "rf_onnx"
    ensemble.export_onnx(onnx_dir)
    max_err = ensemble.verify_onnx(onnx_dir, x[test_idx])
    assert max_err < 1e-4


def test_patch_transformer_fit_predict_onnx(tmp_path: Path) -> None:
    config = V5Config(
        tf_d_model=16,
        tf_nhead=2,
        tf_num_layers=1,
        tf_dim_feedforward=32,
        tf_patch_length=4,
        tf_patch_stride=2,
        tf_lookback_hours=12,
        tf_epochs=2,
        tf_batch_size=16,
        tf_device="cpu",
        seeds=(11,),
    )
    feature_names = ("f1", "f2", "f3")
    ensemble = PatchTransformerEnsemble.create(
        config=config,
        feature_names=feature_names,
        seeds=(11,),
    )

    rng = np.random.default_rng(42)
    n_samples = 60
    x = rng.normal(size=(n_samples, 3)).astype(np.float32)
    y = (0.3 * x[:, 0] + rng.normal(scale=0.05, size=n_samples)).astype(np.float32)
    train_idx = np.arange(12, 45)

    fit_info = ensemble.fit(x, y, train_idx)
    assert fit_info["train_samples"] == len(train_idx)
    assert fit_info["members"] == 1

    test_idx = np.arange(45, 60)
    mean_preds, std_preds = ensemble.predict_summary(x, test_idx)
    assert len(mean_preds) == len(test_idx)
    assert np.all(np.isfinite(mean_preds))

    # Test ONNX export & verification
    onnx_dir = tmp_path / "tf_onnx"
    ensemble.export_onnx(onnx_dir)
    max_err = ensemble.verify_onnx(onnx_dir, x[test_idx])
    assert max_err < 1e-4


def test_predictive_metrics_and_gate_evaluation() -> None:
    y_true = np.array([0.02, -0.01, 0.03, -0.02, 0.01])
    y_pred = np.array([0.015, -0.008, 0.025, -0.018, 0.012])
    metrics = compute_predictive_metrics(y_true, y_pred)

    assert metrics["mae"] > 0
    assert metrics["ic_pearson"] > 0.95
    assert metrics["directional_accuracy"] == 1.0

    good_backtest = {
        "average_monthly_trades": 6.5,
        "sharpe_daily": 2.1,
        "profit_factor": 1.45,
        "maximum_drawdown": 0.05,
        "total_return": 0.18,
    }
    config = V5Config()
    gates = evaluate_gates(good_backtest, config)
    assert gates["overall"] is True

    bad_backtest = {
        "average_monthly_trades": 2.0,  # Below 4
        "sharpe_daily": 0.5,
        "profit_factor": 0.9,
        "maximum_drawdown": 0.15,
        "total_return": -0.05,
    }
    gates_bad = evaluate_gates(bad_backtest, config)
    assert gates_bad["overall"] is False
    assert gates_bad["frequency"] is False
