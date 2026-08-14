from __future__ import annotations

import numpy as np
import pytest

from bottrade.domain import Asset
from bottrade.models.random_forest import RandomForestRegressorModel
from bottrade.models.registry import ModelRegistry


def test_registry_rejects_untrusted_path_components(app_config) -> None:
    registry = ModelRegistry(app_config)
    with pytest.raises(ValueError, match="invalid model registry slot"):
        registry.resolve(Asset.BTCUSDT, "../../outside")
    with pytest.raises(ValueError, match="invalid model version"):
        registry.load_version(Asset.BTCUSDT, "../../outside")


def test_random_forest_is_deterministic() -> None:
    rng = np.random.default_rng(1)
    x = rng.normal(size=(200, 8))
    y = x[:, 0] * 0.2 - x[:, 1] * 0.1
    indices = np.arange(180)
    params = {
        "n_estimators": 30,
        "max_depth": 5,
        "min_samples_leaf": 2,
        "max_features": 0.8,
        "n_jobs": 1,
    }
    first = RandomForestRegressorModel(params, seed=11)
    second = RandomForestRegressorModel(params, seed=11)
    first.fit(x, y, indices)
    second.fit(x, y, indices)
    assert np.allclose(first.predict(x, np.arange(180, 200)), second.predict(x, np.arange(180, 200)))


@pytest.mark.slow
def test_transformer_smoke_train_predict() -> None:
    pytest.importorskip("torch")
    from bottrade.models.transformer import TransformerRegressorModel

    rng = np.random.default_rng(2)
    x = rng.normal(size=(100, 5))
    y = x[:, 0] * 0.1
    model = TransformerRegressorModel(
        n_features=5,
        sequence_length=8,
        params={
            "d_model": 16,
            "nhead": 2,
            "num_layers": 1,
            "dim_feedforward": 32,
            "dropout": 0.0,
            "batch_size": 16,
            "epochs": 2,
            "patience": 1,
            "learning_rate": 0.001,
            "weight_decay": 0.0,
        },
        seed=11,
        device="cpu",
    )
    details = model.fit(x, y, np.arange(8, 80))
    predictions = model.predict(x, np.arange(80, 90))
    assert details["epochs_ran"] >= 1
    assert predictions.shape == (10,)
    assert np.isfinite(predictions).all()
