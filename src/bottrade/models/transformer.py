from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset

from bottrade.models.base import ResearchRegressor
from bottrade.models.preprocessing import RobustStandardizer
from bottrade.utils import set_global_seed


class SequenceDataset(Dataset[tuple[torch.Tensor, torch.Tensor]]):
    def __init__(
        self,
        x: np.ndarray,
        y: np.ndarray,
        indices: np.ndarray,
        sequence_length: int,
    ) -> None:
        self.x = x
        self.y = y
        self.indices = np.asarray(
            [index for index in indices if index >= sequence_length - 1 and np.isfinite(y[index])],
            dtype=int,
        )
        self.sequence_length = sequence_length

    def __len__(self) -> int:
        return len(self.indices)

    def __getitem__(self, item: int) -> tuple[torch.Tensor, torch.Tensor]:
        index = int(self.indices[item])
        start = index - self.sequence_length + 1
        sequence = torch.from_numpy(self.x[start : index + 1])
        target = torch.tensor(self.y[index], dtype=torch.float32)
        return sequence, target


class TemporalTransformer(nn.Module):
    def __init__(
        self,
        *,
        n_features: int,
        sequence_length: int,
        d_model: int,
        nhead: int,
        num_layers: int,
        dim_feedforward: int,
        dropout: float,
        calendar_hour_index: int | None = None,
        calendar_day_index: int | None = None,
    ) -> None:
        super().__init__()
        self.sequence_length = sequence_length
        self.calendar_hour_index = calendar_hour_index
        self.calendar_day_index = calendar_day_index
        self.input_projection = nn.Linear(n_features, d_model)
        if calendar_hour_index is not None and calendar_day_index is not None:
            mask = torch.ones(n_features, dtype=torch.float32)
            mask[calendar_hour_index] = 0.0
            mask[calendar_day_index] = 0.0
            self.register_buffer("numeric_feature_mask", mask)
            self.hour_embedding: nn.Embedding | None = nn.Embedding(24, d_model)
            self.day_embedding: nn.Embedding | None = nn.Embedding(7, d_model)
        else:
            self.register_buffer("numeric_feature_mask", torch.ones(n_features))
            self.hour_embedding = None
            self.day_embedding = None
        self.position = nn.Parameter(torch.zeros(1, sequence_length, d_model))
        nn.init.trunc_normal_(self.position, std=0.02)
        layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=dim_feedforward,
            dropout=dropout,
            activation="gelu",
            batch_first=True,
            norm_first=True,
        )
        self.encoder = nn.TransformerEncoder(layer, num_layers=num_layers)
        self.normalization = nn.LayerNorm(d_model)
        self.head = nn.Sequential(
            nn.Linear(d_model, max(16, d_model // 2)),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(max(16, d_model // 2), 1),
        )

    def forward(self, sequence: torch.Tensor) -> torch.Tensor:
        numeric = sequence * self.numeric_feature_mask
        encoded = self.input_projection(numeric) + self.position[:, : sequence.shape[1]]
        if self.hour_embedding is not None and self.day_embedding is not None:
            if self.calendar_hour_index is None or self.calendar_day_index is None:
                raise RuntimeError("calendar embedding indices are not configured")
            hour = sequence[:, :, self.calendar_hour_index].round().long().clamp(0, 23)
            day = sequence[:, :, self.calendar_day_index].round().long().clamp(0, 6)
            encoded = encoded + self.hour_embedding(hour) + self.day_embedding(day)
        encoded = self.encoder(encoded)
        last = self.normalization(encoded[:, -1])
        return self.head(last).squeeze(-1)


class TransformerRegressorModel(ResearchRegressor):
    family = "transformer"

    def __init__(
        self,
        *,
        n_features: int,
        sequence_length: int,
        params: dict[str, Any],
        seed: int,
        device: str | None = None,
        calendar_hour_index: int | None = None,
        calendar_day_index: int | None = None,
    ) -> None:
        set_global_seed(seed)
        self.seed = seed
        self.params = params.copy()
        self.sequence_length = sequence_length
        self.n_features = n_features
        self.calendar_hour_index = calendar_hour_index
        self.calendar_day_index = calendar_day_index
        self.device = torch.device(device or ("cuda" if torch.cuda.is_available() else "cpu"))
        architecture_keys = {
            "d_model",
            "nhead",
            "num_layers",
            "dim_feedforward",
            "dropout",
        }
        architecture = {key: self.params[key] for key in architecture_keys}
        if architecture["d_model"] % architecture["nhead"] != 0:
            raise ValueError("d_model must be divisible by nhead")
        self.network = TemporalTransformer(
            n_features=n_features,
            sequence_length=sequence_length,
            calendar_hour_index=calendar_hour_index,
            calendar_day_index=calendar_day_index,
            **architecture,
        ).to(self.device)
        passthrough = tuple(
            index
            for index in (calendar_hour_index, calendar_day_index)
            if index is not None
        )
        self.standardizer = RobustStandardizer(passthrough_indices=passthrough)

    def fit(self, x: np.ndarray, y: np.ndarray, indices: np.ndarray) -> dict[str, Any]:
        if len(indices) < self.sequence_length + 16:
            raise ValueError("not enough samples for the configured Transformer lookback")
        if self.device.type == "cuda":
            torch.cuda.reset_peak_memory_stats(self.device)
        eligible = indices[indices >= self.sequence_length - 1]
        split = max(1, int(len(eligible) * 0.9))
        purge = int(self.params.get("validation_purge_hours", 3))
        train_indices = eligible[: max(1, split - purge)]
        validation_indices = eligible[split:]
        if len(validation_indices) == 0:
            validation_indices = train_indices[-1:]
            train_indices = train_indices[:-1]
        self.standardizer.fit(x[train_indices])
        normalized = self.standardizer.transform(x)
        train_dataset = SequenceDataset(
            normalized, y, train_indices, self.sequence_length
        )
        validation_dataset = SequenceDataset(
            normalized, y, validation_indices, self.sequence_length
        )
        generator = torch.Generator().manual_seed(self.seed)
        train_loader = DataLoader(
            train_dataset,
            batch_size=int(self.params.get("batch_size", 256)),
            shuffle=True,
            generator=generator,
            num_workers=0,
        )
        validation_loader = DataLoader(
            validation_dataset,
            batch_size=int(self.params.get("batch_size", 256)),
            shuffle=False,
            num_workers=0,
        )
        optimizer = torch.optim.AdamW(
            self.network.parameters(),
            lr=float(self.params.get("learning_rate", 5e-4)),
            weight_decay=float(self.params.get("weight_decay", 1e-4)),
        )
        loss_function = nn.SmoothL1Loss(beta=0.5)
        epochs = int(self.params.get("epochs", 40))
        patience = int(self.params.get("patience", 6))
        best_loss = float("inf")
        best_state: dict[str, torch.Tensor] | None = None
        stale_epochs = 0
        history: list[dict[str, float]] = []
        for epoch in range(epochs):
            self.network.train()
            train_losses: list[float] = []
            for sequences, targets in train_loader:
                sequences = sequences.to(self.device)
                targets = targets.to(self.device)
                optimizer.zero_grad(set_to_none=True)
                predictions = self.network(sequences)
                loss = loss_function(predictions, targets)
                loss.backward()
                nn.utils.clip_grad_norm_(self.network.parameters(), max_norm=1.0)
                optimizer.step()
                train_losses.append(float(loss.detach().cpu()))
            self.network.eval()
            validation_losses: list[float] = []
            with torch.no_grad():
                for sequences, targets in validation_loader:
                    sequences = sequences.to(self.device)
                    targets = targets.to(self.device)
                    validation_losses.append(
                        float(loss_function(self.network(sequences), targets).cpu())
                    )
            train_loss = float(np.mean(train_losses)) if train_losses else float("inf")
            validation_loss = (
                float(np.mean(validation_losses)) if validation_losses else train_loss
            )
            history.append(
                {"epoch": float(epoch + 1), "train_loss": train_loss, "validation_loss": validation_loss}
            )
            if validation_loss < best_loss - 1e-6:
                best_loss = validation_loss
                best_state = copy.deepcopy(self.network.state_dict())
                stale_epochs = 0
            else:
                stale_epochs += 1
                if stale_epochs >= patience:
                    break
        if best_state is not None:
            self.network.load_state_dict(best_state)
        return {
            "train_samples": len(train_dataset),
            "validation_samples": len(validation_dataset),
            "best_validation_loss": best_loss,
            "epochs_ran": len(history),
            "device": str(self.device),
            "gpu_peak_memory_bytes": (
                int(torch.cuda.max_memory_allocated(self.device))
                if self.device.type == "cuda"
                else 0
            ),
            "history": history,
        }

    def _predict_normalized(self, normalized: np.ndarray, indices: np.ndarray) -> np.ndarray:
        dummy_y = np.zeros(len(normalized), dtype=np.float32)
        dataset = SequenceDataset(normalized, dummy_y, indices, self.sequence_length)
        loader = DataLoader(
            dataset,
            batch_size=int(self.params.get("batch_size", 256)),
            shuffle=False,
            num_workers=0,
        )
        self.network.eval()
        predictions: list[np.ndarray] = []
        with torch.no_grad():
            for sequences, _ in loader:
                output = self.network(sequences.to(self.device)).detach().cpu().numpy()
                predictions.append(output)
        return np.concatenate(predictions) if predictions else np.array([], dtype=float)

    def predict(self, x: np.ndarray, indices: np.ndarray) -> np.ndarray:
        valid = indices[indices >= self.sequence_length - 1]
        if len(valid) != len(indices):
            raise ValueError("all prediction indices must have a full lookback sequence")
        return self._predict_normalized(self.standardizer.transform(x), valid)

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
            output_names=["prediction"],
            dynamic_axes={"sequence": {0: "batch"}, "prediction": {0: "batch"}},
            opset_version=18,
            dynamo=False,
        )
        self.network.to(original_device)
        self.standardizer.write(path.with_name("preprocessor.json"))

    def verify_onnx(self, path: Path, x: np.ndarray, indices: np.ndarray) -> float:
        try:
            import onnxruntime as ort
        except ImportError as exc:
            raise RuntimeError("install the 'ml' extra to verify ONNX models") from exc
        sample_indices = indices[: min(64, len(indices))]
        native = self.predict(x, sample_indices)
        normalized = self.standardizer.transform(x)
        sequences = np.stack(
            [normalized[index - self.sequence_length + 1 : index + 1] for index in sample_indices]
        ).astype(np.float32)
        session = ort.InferenceSession(str(path), providers=["CPUExecutionProvider"])
        deployed = np.asarray(session.run(None, {"sequence": sequences})[0]).reshape(-1)
        return float(np.max(np.abs(native - deployed))) if len(native) else 0.0

    def save_native(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        torch.save(
            {
                "state_dict": self.network.state_dict(),
                "n_features": self.n_features,
                "sequence_length": self.sequence_length,
                "params": self.params,
                "seed": self.seed,
                "calendar_hour_index": self.calendar_hour_index,
                "calendar_day_index": self.calendar_day_index,
                "standardizer": {
                    "median": self.standardizer.median,
                    "mean": self.standardizer.mean,
                    "scale": self.standardizer.scale,
                },
            },
            path,
        )
