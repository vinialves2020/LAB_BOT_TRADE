from __future__ import annotations

import numpy as np
import pytest

from bottrade.domain import ModelFamily
from bottrade.explainability import explain_model
from bottrade.models.random_forest import RandomForestRegressorModel


@pytest.mark.slow
def test_random_forest_onnx_and_explanations(tmp_path) -> None:
    rng = np.random.default_rng(7)
    x = rng.normal(size=(180, 6))
    x[5, 2] = np.nan
    y = 0.7 * np.nan_to_num(x[:, 0]) - 0.2 * np.nan_to_num(x[:, 3])
    model = RandomForestRegressorModel(
        params={
            "n_estimators": 20,
            "max_depth": 5,
            "min_samples_leaf": 2,
            "max_features": 0.8,
            "n_jobs": 1,
        },
        seed=11,
    )
    train = np.arange(120)
    evaluate = np.arange(120, 180)
    model.fit(x, y, train)
    path = tmp_path / "rf.onnx"
    model.export_onnx(path)
    assert model.verify_onnx(path, x, evaluate) < 1e-4
    explanation = explain_model(
        model=model,
        family=ModelFamily.RANDOM_FOREST,
        x=x,
        y=y,
        indices=evaluate,
        feature_names=[f"f{index}" for index in range(x.shape[1])],
        repeats=1,
        max_samples=32,
        integrated_gradient_steps=8,
        seed=11,
    )
    assert explanation["permutation_importance"][0]["feature"] == "f0"
    assert len(explanation["shap"]) == x.shape[1]


@pytest.mark.slow
def test_transformer_calendar_embeddings_onnx_and_explanations(tmp_path) -> None:
    pytest.importorskip("torch")
    from bottrade.models.transformer import TransformerRegressorModel

    rng = np.random.default_rng(13)
    rows = 110
    x = rng.normal(size=(rows, 6))
    x[:, 4] = np.arange(rows) % 24
    x[:, 5] = (np.arange(rows) // 24) % 7
    y = 0.2 * x[:, 0] + 0.05 * np.sin(2 * np.pi * x[:, 4] / 24)
    model = TransformerRegressorModel(
        n_features=6,
        sequence_length=12,
        params={
            "d_model": 8,
            "nhead": 2,
            "num_layers": 2,
            "dim_feedforward": 16,
            "dropout": 0.0,
            "batch_size": 16,
            "epochs": 2,
            "patience": 1,
            "validation_purge_hours": 3,
            "learning_rate": 0.001,
            "weight_decay": 0.0,
        },
        seed=17,
        device="cpu",
        calendar_hour_index=4,
        calendar_day_index=5,
    )
    model.fit(x, y, np.arange(12, 85))
    evaluate = np.arange(90, 100)
    path = tmp_path / "transformer.onnx"
    model.export_onnx(path)
    assert (tmp_path / "preprocessor.json").exists()
    assert model.verify_onnx(path, x, evaluate) < 1e-4
    explanation = explain_model(
        model=model,
        family=ModelFamily.TRANSFORMER,
        x=x,
        y=y,
        indices=evaluate,
        feature_names=[f"f{index}" for index in range(x.shape[1])],
        repeats=1,
        max_samples=4,
        integrated_gradient_steps=4,
        seed=17,
    )
    assert len(explanation["integrated_gradients"]) == x.shape[1]
    assert len(explanation["temporal_ablation"]) == x.shape[1]
