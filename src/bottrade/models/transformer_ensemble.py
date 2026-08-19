"""Mean ensemble of Transformer regressors for the frozen V2 artifact."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import torch
from torch import nn

from bottrade.models.base import ResearchRegressor
from bottrade.models.transformer import TransformerRegressorModel


class _MeanNetwork(nn.Module):
    def __init__(self, networks: list[nn.Module]) -> None:
        super().__init__()
        self.networks = nn.ModuleList(networks)

    def forward(self, sequence: torch.Tensor) -> torch.Tensor:
        predictions = [network(sequence) for network in self.networks]
        return torch.stack(predictions, dim=0).mean(dim=0)


class TransformerSeedEnsembleModel(ResearchRegressor):
    family = "transformer"

    def __init__(
        self,
        *,
        n_features: int,
        sequence_length: int,
        params: dict[str, Any],
        seeds: list[int],
        calendar_hour_index: int | None = None,
        calendar_day_index: int | None = None,
    ) -> None:
        if not seeds:
            raise ValueError("an ensemble requires at least one seed")
        self.seeds = tuple(int(seed) for seed in seeds)
        self.n_features = n_features
        self.sequence_length = sequence_length
        self.params = params.copy()
        self.models = [
            TransformerRegressorModel(
                n_features=n_features,
                sequence_length=sequence_length,
                params=params,
                seed=seed,
                calendar_hour_index=calendar_hour_index,
                calendar_day_index=calendar_day_index,
            )
            for seed in self.seeds
        ]
        self.network = _MeanNetwork([model.network for model in self.models])
        self.standardizer = self.models[0].standardizer
        self.device = self.models[0].device

    def fit(self, x: np.ndarray, y: np.ndarray, indices: np.ndarray) -> dict[str, Any]:
        details = [model.fit(x, y, indices) for model in self.models]
        self.standardizer = self.models[0].standardizer
        self.device = self.models[0].device
        return {
            "train_samples": int(min(item.get("train_samples", 0) for item in details)),
            "ensemble_seeds": list(self.seeds),
            "members": details,
            "device": str(self.device),
            "gpu_peak_memory_bytes": int(
                max(item.get("gpu_peak_memory_bytes", 0) for item in details)
            ),
        }

    def predict(self, x: np.ndarray, indices: np.ndarray) -> np.ndarray:
        predictions = [model.predict(x, indices) for model in self.models]
        return np.mean(np.stack(predictions), axis=0)

    def export_onnx(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        original_devices = [next(model.network.parameters()).device for model in self.models]
        self.network.eval()
        self.network.to("cpu")
        dummy = torch.zeros(1, self.sequence_length, self.n_features, dtype=torch.float32)
        torch.onnx.export(
            self.network,
            dummy,
            str(path),
            input_names=["sequence"],
            output_names=["prediction"],
            dynamic_axes={"sequence": {0: "batch"}, "prediction": {0: "batch"}},
            opset_version=18,
            dynamo=False,
        )
        for model, device in zip(self.models, original_devices, strict=True):
            model.network.to(device)
        self.network.to(original_devices[0])
        self.standardizer.write(path.with_name("preprocessor.json"))

    def verify_onnx(self, path: Path, x: np.ndarray, indices: np.ndarray) -> float:
        import onnxruntime as ort

        sample = np.asarray(indices, dtype=int)[:64]
        native = self.predict(x, sample)
        normalized = self.standardizer.transform(x)
        sequences = np.stack(
            [normalized[index - self.sequence_length + 1 : index + 1] for index in sample]
        ).astype(np.float32)
        session = ort.InferenceSession(str(path), providers=["CPUExecutionProvider"])
        deployed = np.asarray(session.run(None, {"sequence": sequences})[0]).reshape(-1)
        return float(np.max(np.abs(native - deployed))) if len(sample) else 0.0

    def save_native(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        torch.save(
            {
                "state_dict": self.network.state_dict(),
                "n_features": self.n_features,
                "sequence_length": self.sequence_length,
                "params": self.params,
                "seeds": self.seeds,
                "standardizer": {
                    "median": self.standardizer.median,
                    "mean": self.standardizer.mean,
                    "scale": self.standardizer.scale,
                },
            },
            path,
        )
