from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np

from bottrade.domain import ModelFamily
from bottrade.models.base import ResearchRegressor


def _ranked(feature_names: list[str], values: np.ndarray) -> list[dict[str, float | str]]:
    rows = [
        {"feature": name, "importance": float(value)}
        for name, value in zip(feature_names, values, strict=True)
    ]
    return sorted(rows, key=lambda row: float(row["importance"]), reverse=True)


def permutation_importance(
    model: ResearchRegressor,
    x: np.ndarray,
    y: np.ndarray,
    indices: np.ndarray,
    feature_names: list[str],
    *,
    repeats: int,
    max_samples: int,
    seed: int,
) -> list[dict[str, float | str]]:
    """Model-agnostic MAE increase using only an already-frozen evaluation slice."""

    selected = np.asarray(indices[-min(max_samples, len(indices)) :], dtype=int)
    if not len(selected):
        return []
    truth = y[selected]
    baseline = model.predict(x, selected)
    baseline_mae = float(np.mean(np.abs(truth - baseline)))
    rng = np.random.default_rng(seed)
    sequence_length = int(getattr(model, "sequence_length", 1))
    coverage_start = max(0, int(selected.min()) - sequence_length + 1)
    coverage = np.arange(coverage_start, int(selected.max()) + 1)
    importances = np.zeros(x.shape[1], dtype=float)
    for feature in range(x.shape[1]):
        scores: list[float] = []
        for _ in range(repeats):
            shuffled = np.array(x, copy=True)
            permutation = rng.permutation(coverage)
            shuffled[coverage, feature] = x[permutation, feature]
            predictions = model.predict(shuffled, selected)
            scores.append(float(np.mean(np.abs(truth - predictions))) - baseline_mae)
        importances[feature] = float(np.mean(scores))
    return _ranked(feature_names, importances)


def random_forest_shap(
    model: ResearchRegressor,
    x: np.ndarray,
    indices: np.ndarray,
    feature_names: list[str],
    *,
    max_samples: int,
) -> list[dict[str, float | str]]:
    try:
        import shap
    except ImportError as exc:
        raise RuntimeError("install the 'explain' extra to calculate RF SHAP values") from exc
    pipeline = getattr(model, "pipeline", None)
    if pipeline is None or "regressor" not in pipeline.named_steps:
        raise TypeError("SHAP explanation requires a fitted sklearn pipeline")
    selected = np.asarray(indices[-min(max_samples, len(indices)) :], dtype=int)
    transformed = pipeline.named_steps["imputer"].transform(x[selected])
    explainer = shap.TreeExplainer(pipeline.named_steps["regressor"])
    values = np.asarray(explainer.shap_values(transformed), dtype=float)
    if values.ndim == 3:
        values = values[..., 0]
    return _ranked(feature_names, np.mean(np.abs(values), axis=0))


def _transformer_sequences(
    model: ResearchRegressor,
    x: np.ndarray,
    indices: np.ndarray,
    max_samples: int,
) -> tuple[Any, np.ndarray]:
    try:
        import torch
    except ImportError as exc:
        raise RuntimeError("PyTorch is required for Transformer explanations") from exc
    sequence_length = int(model.sequence_length)
    standardizer = model.standardizer
    selected = np.asarray(indices[-min(max_samples, len(indices)) :], dtype=int)
    normalized = standardizer.transform(x)
    sequences = np.stack(
        [normalized[index - sequence_length + 1 : index + 1] for index in selected]
    ).astype(np.float32)
    device = model.device
    return torch.from_numpy(sequences).to(device), selected


def transformer_integrated_gradients(
    model: ResearchRegressor,
    x: np.ndarray,
    indices: np.ndarray,
    feature_names: list[str],
    *,
    max_samples: int,
    steps: int,
) -> list[dict[str, float | str]]:
    try:
        from captum.attr import IntegratedGradients
    except ImportError as exc:
        raise RuntimeError(
            "install the 'explain' extra to calculate integrated gradients"
        ) from exc
    sequences, _ = _transformer_sequences(model, x, indices, max_samples)
    network = model.network
    network.eval()
    baseline = sequences.new_zeros(sequences.shape)
    attributes = IntegratedGradients(network).attribute(
        sequences,
        baselines=baseline,
        n_steps=steps,
        internal_batch_size=max(1, len(sequences)),
    )
    values = attributes.detach().abs().mean(dim=(0, 1)).cpu().numpy()
    return _ranked(feature_names, values)


def transformer_ablation(
    model: ResearchRegressor,
    x: np.ndarray,
    indices: np.ndarray,
    feature_names: list[str],
    *,
    max_samples: int,
) -> list[dict[str, float | str]]:
    try:
        import torch
    except ImportError as exc:
        raise RuntimeError("PyTorch is required for Transformer ablation") from exc
    sequences, _ = _transformer_sequences(model, x, indices, max_samples)
    network = model.network
    network.eval()
    with torch.no_grad():
        baseline_prediction = network(sequences)
        values: list[float] = []
        for feature in range(sequences.shape[-1]):
            ablated = sequences.clone()
            ablated[:, :, feature] = 0.0
            values.append(float((network(ablated) - baseline_prediction).abs().mean().cpu()))
    return _ranked(feature_names, np.asarray(values))


def explain_model(
    *,
    model: ResearchRegressor,
    family: ModelFamily,
    x: np.ndarray,
    y: np.ndarray,
    indices: np.ndarray,
    feature_names: list[str],
    repeats: int,
    max_samples: int,
    integrated_gradient_steps: int,
    seed: int,
) -> dict[str, Any]:
    output: dict[str, Any] = {
        "evaluation_samples": int(min(max_samples, len(indices))),
        "permutation_importance": permutation_importance(
            model,
            x,
            y,
            indices,
            feature_names,
            repeats=repeats,
            max_samples=max_samples,
            seed=seed,
        ),
    }
    if family == ModelFamily.RANDOM_FOREST:
        output["shap"] = random_forest_shap(
            model, x, indices, feature_names, max_samples=max_samples
        )
    elif family == ModelFamily.TRANSFORMER:
        output["integrated_gradients"] = transformer_integrated_gradients(
            model,
            x,
            indices,
            feature_names,
            max_samples=max_samples,
            steps=integrated_gradient_steps,
        )
        output["temporal_ablation"] = transformer_ablation(
            model, x, indices, feature_names, max_samples=max_samples
        )
    return output


def write_explanations(explanations: dict[str, Any], path: Path) -> Path:
    import json

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(explanations, indent=2, sort_keys=True), encoding="utf-8")
    return path
