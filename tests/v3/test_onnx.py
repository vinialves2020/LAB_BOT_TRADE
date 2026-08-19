from __future__ import annotations

import numpy as np
import pytest

from bottrade.v3.meta_models import fit_meta_model


@pytest.mark.slow
@pytest.mark.parametrize("family", ["random_forest", "hist_gradient_boosting"])
def test_tabular_onnx_matches_native(tmp_path, family: str) -> None:
    pytest.importorskip("skl2onnx")
    pytest.importorskip("onnxruntime")
    rng = np.random.default_rng(11)
    x = rng.normal(size=(80, 5)).astype(np.float32)
    y = (x[:, 0] > 0).astype(int)
    bundle = fit_meta_model(
        family,
        x,
        y,
        x[:, 0] * 0.01,
        np.abs(x[:, 1]) * 0.01,
        seed=11,
        params={"n_estimators": 16, "max_iter": 16, "max_leaf_nodes": 7, "min_samples_leaf": 2},
    )
    result = bundle.export_onnx(tmp_path / family, x[:10])
    assert result["max_abs_error"] <= 1e-4


@pytest.mark.slow
def test_transformer_onnx_matches_native(tmp_path) -> None:
    pytest.importorskip("torch")
    pytest.importorskip("onnxruntime")
    rng = np.random.default_rng(11)
    x = rng.normal(size=(40, 5)).astype(np.float32)
    y = (x[:, 0] > 0).astype(int)
    bundle = fit_meta_model(
        "transformer",
        x,
        y,
        x[:, 0] * 0.01,
        np.abs(x[:, 1]) * 0.01,
        seed=11,
        params={"epochs": 1, "sequence_length": 1, "patch_length": 1, "patch_stride": 1, "d_model": 8, "nhead": 2, "num_layers": 1},
    )
    result = bundle.export_onnx(tmp_path / "transformer", x[:5])
    assert result["max_abs_error"] <= 1e-4
