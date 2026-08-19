"""Patch-based Transformer with joint V2 regression/classification heads."""

from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset

from bottrade.models.preprocessing import RobustStandardizer
from bottrade.models.transformer import TemporalTransformer
from bottrade.utils import set_global_seed


class _MultiTaskDataset(Dataset[tuple[torch.Tensor, torch.Tensor, torch.Tensor]]):
    def __init__(
        self,
        x: np.ndarray,
        regression: np.ndarray,
        classification: np.ndarray,
        indices: np.ndarray,
        sequence_length: int,
    ) -> None:
        self.x = x
        self.regression = regression
        self.classification = classification
        self.sequence_length = sequence_length
        self.indices = np.asarray(
            [
                int(index)
                for index in indices
                if index >= sequence_length - 1
                and np.isfinite(regression[index]).all()
                and np.isfinite(classification[index]).all()
            ],
            dtype=int,
        )

    def __len__(self) -> int:
        return len(self.indices)

    def __getitem__(self, item: int) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        index = int(self.indices[item])
        start = index - self.sequence_length + 1
        return (
            torch.from_numpy(self.x[start : index + 1]),
            torch.from_numpy(self.regression[index].astype(np.float32)),
            torch.from_numpy(self.classification[index].astype(np.float32)),
        )


class TransformerMultiHorizonModel:
    """Shared temporal encoder with three simultaneous forecast heads.

    The model is deliberately separate from the V1 ``ResearchRegressor``
    interface because ONNX exposes two outputs.  It is used by V2 orchestration
    and can be tested without changing the legacy runtime contract.
    """

    def __init__(
        self,
        *,
        n_features: int,
        sequence_length: int,
        horizons: tuple[int, ...] = (3, 6, 12),
        params: dict[str, Any],
        seed: int,
        device: str | None = None,
        calendar_hour_index: int | None = None,
        calendar_day_index: int | None = None,
    ) -> None:
        set_global_seed(seed)
        self.n_features = int(n_features)
        self.sequence_length = int(sequence_length)
        self.horizons = tuple(sorted({int(item) for item in horizons}))
        if not self.horizons:
            raise ValueError("horizons cannot be empty")
        self.params = dict(params)
        self.seed = int(seed)
        self.device = torch.device(device or ("cuda" if torch.cuda.is_available() else "cpu"))
        self.calendar_hour_index = calendar_hour_index
        self.calendar_day_index = calendar_day_index
        self.network = TemporalTransformer(
            n_features=self.n_features,
            sequence_length=self.sequence_length,
            d_model=int(self.params.get("d_model", 64)),
            nhead=int(self.params.get("nhead", 4)),
            num_layers=int(self.params.get("num_layers", 2)),
            dim_feedforward=int(self.params.get("dim_feedforward", 128)),
            dropout=float(self.params.get("dropout", 0.15)),
            calendar_hour_index=calendar_hour_index,
            calendar_day_index=calendar_day_index,
            patch_length=int(self.params.get("patch_length", 12)),
            patch_stride=int(self.params.get("patch_stride", 6)),
            horizon_count=len(self.horizons),
        ).to(self.device)
        passthrough = tuple(
            item for item in (calendar_hour_index, calendar_day_index) if item is not None
        )
        self.standardizer = RobustStandardizer(passthrough_indices=passthrough)

    def fit(
        self,
        x: np.ndarray,
        regression: np.ndarray,
        classification: np.ndarray,
        indices: np.ndarray,
    ) -> dict[str, Any]:
        if regression.ndim != 2 or regression.shape[1] != len(self.horizons):
            raise ValueError("regression labels must have one column per horizon")
        if classification.shape != regression.shape:
            raise ValueError("classification and regression labels must have the same shape")
        eligible = np.asarray(indices, dtype=int)
        eligible = eligible[eligible >= self.sequence_length - 1]
        if len(eligible) < 16:
            raise ValueError("not enough samples for the configured Transformer lookback")
        split = max(1, int(len(eligible) * 0.9))
        purge = int(self.params.get("validation_purge_hours", 12))
        train_indices = eligible[: max(1, split - purge)]
        validation_indices = eligible[split:]
        if len(validation_indices) == 0:
            validation_indices = train_indices[-1:]
            train_indices = train_indices[:-1]
        self.standardizer.fit(x[train_indices])
        normalized = self.standardizer.transform(x)
        train = _MultiTaskDataset(
            normalized, regression, classification, train_indices, self.sequence_length
        )
        validation = _MultiTaskDataset(
            normalized, regression, classification, validation_indices, self.sequence_length
        )
        if not len(train):
            raise ValueError("no valid sequence samples remain after lookback filtering")
        batch_size = int(self.params.get("batch_size", 256))
        generator = torch.Generator().manual_seed(self.seed)
        train_loader = DataLoader(
            train, batch_size=batch_size, shuffle=True, generator=generator, num_workers=0
        )
        validation_loader = DataLoader(
            validation, batch_size=batch_size, shuffle=False, num_workers=0
        )
        optimizer = torch.optim.AdamW(
            self.network.parameters(),
            lr=float(self.params.get("learning_rate", 5e-4)),
            weight_decay=float(self.params.get("weight_decay", 1e-4)),
        )
        regression_loss = nn.SmoothL1Loss(beta=0.5)
        classification_loss = nn.BCEWithLogitsLoss()
        epochs = int(self.params.get("epochs", 40))
        patience = int(self.params.get("patience", 6))
        best_loss = float("inf")
        best_state: dict[str, torch.Tensor] | None = None
        stale = 0
        history: list[dict[str, float]] = []
        for epoch in range(epochs):
            self.network.train()
            train_losses: list[float] = []
            for sequences, targets, labels in train_loader:
                sequences = sequences.to(self.device)
                targets = targets.to(self.device)
                labels = labels.to(self.device)
                optimizer.zero_grad(set_to_none=True)
                predicted, logits = self.network(sequences)
                loss = regression_loss(predicted, targets) + classification_loss(logits, labels)
                loss.backward()
                nn.utils.clip_grad_norm_(self.network.parameters(), max_norm=1.0)
                optimizer.step()
                train_losses.append(float(loss.detach().cpu()))
            self.network.eval()
            validation_losses: list[float] = []
            with torch.no_grad():
                for sequences, targets, labels in validation_loader:
                    predicted, logits = self.network(sequences.to(self.device))
                    validation_losses.append(
                        float(
                            (
                                regression_loss(predicted, targets.to(self.device))
                                + classification_loss(logits, labels.to(self.device))
                            ).cpu()
                        )
                    )
            train_loss = float(np.mean(train_losses)) if train_losses else float("inf")
            validation_loss = float(np.mean(validation_losses)) if validation_losses else train_loss
            history.append(
                {
                    "epoch": float(epoch + 1),
                    "train_loss": train_loss,
                    "validation_loss": validation_loss,
                }
            )
            if validation_loss < best_loss - 1e-6:
                best_loss = validation_loss
                best_state = copy.deepcopy(self.network.state_dict())
                stale = 0
            else:
                stale += 1
                if stale >= patience:
                    break
        if best_state is not None:
            self.network.load_state_dict(best_state)
        return {
            "train_samples": len(train),
            "validation_samples": len(validation),
            "best_validation_loss": best_loss,
            "epochs_ran": len(history),
            "device": str(self.device),
            "history": history,
        }

    def predict(self, x: np.ndarray, indices: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        selected = np.asarray(indices, dtype=int)
        if np.any(selected < self.sequence_length - 1):
            raise ValueError("all prediction indices must have a full lookback sequence")
        normalized = self.standardizer.transform(x)
        dummy = np.zeros((len(normalized), len(self.horizons)), dtype=np.float32)
        dataset = _MultiTaskDataset(
            normalized, dummy, dummy, selected, self.sequence_length
        )
        loader = DataLoader(
            dataset,
            batch_size=int(self.params.get("batch_size", 256)),
            shuffle=False,
            num_workers=0,
        )
        self.network.eval()
        regressions: list[np.ndarray] = []
        probabilities: list[np.ndarray] = []
        with torch.no_grad():
            for sequences, _, _ in loader:
                predicted, logits = self.network(sequences.to(self.device))
                regressions.append(predicted.cpu().numpy())
                probabilities.append(torch.sigmoid(logits).cpu().numpy())
        if not regressions:
            return np.empty((0, len(self.horizons))), np.empty((0, len(self.horizons)))
        return np.concatenate(regressions), np.concatenate(probabilities)

    def export_onnx(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.network.eval()
        original_device = next(self.network.parameters()).device
        self.network.to("cpu")
        dummy = torch.zeros(1, self.sequence_length, self.n_features, dtype=torch.float32)
        torch.onnx.export(
            self.network,
            dummy,
            str(path),
            input_names=["sequence"],
            output_names=["regression", "classification_logits"],
            dynamic_axes={
                "sequence": {0: "batch"},
                "regression": {0: "batch"},
                "classification_logits": {0: "batch"},
            },
            opset_version=18,
            dynamo=False,
        )
        self.network.to(original_device)
        self.standardizer.write(path.with_name("preprocessor.json"))

    def verify_onnx(self, path: Path, x: np.ndarray, indices: np.ndarray) -> float:
        import onnxruntime as ort

        selected = np.asarray(indices, dtype=int)[:64]
        native_regression, native_probability = self.predict(x, selected)
        normalized = self.standardizer.transform(x)
        sequences = np.stack(
            [normalized[index - self.sequence_length + 1 : index + 1] for index in selected]
        ).astype(np.float32)
        session = ort.InferenceSession(str(path), providers=["CPUExecutionProvider"])
        outputs = session.run(None, {"sequence": sequences})
        deployed_regression = np.asarray(outputs[0])
        deployed_probability = 1.0 / (1.0 + np.exp(-np.asarray(outputs[1])))
        if not len(selected):
            return 0.0
        return float(
            max(
                np.max(np.abs(native_regression - deployed_regression)),
                np.max(np.abs(native_probability - deployed_probability)),
            )
        )

    def save_native(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        torch.save(
            {
                "state_dict": self.network.state_dict(),
                "n_features": self.n_features,
                "sequence_length": self.sequence_length,
                "horizons": self.horizons,
                "params": self.params,
                "seed": self.seed,
            },
            path,
        )
