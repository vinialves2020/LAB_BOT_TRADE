from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

from bottrade.v5.config import V5Config


class PatchTemporalModel(nn.Module):
    """PatchTST-inspired temporal encoder for financial tabular candles."""

    def __init__(
        self,
        n_features: int,
        lookback_hours: int,
        d_model: int = 64,
        nhead: int = 4,
        num_layers: int = 2,
        dim_feedforward: int = 128,
        dropout: float = 0.1,
        patch_length: int = 6,
        patch_stride: int = 3,
    ) -> None:
        super().__init__()
        self.n_features = n_features
        self.lookback_hours = lookback_hours
        self.patch_length = patch_length
        self.patch_stride = patch_stride

        self.n_patches = 1 + (lookback_hours - patch_length) // patch_stride
        patch_dim = n_features * patch_length

        self.patch_projection = nn.Linear(patch_dim, d_model)
        self.position = nn.Parameter(torch.zeros(1, self.n_patches, d_model))
        nn.init.trunc_normal_(self.position, std=0.02)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=dim_feedforward,
            dropout=dropout,
            activation="gelu",
            batch_first=True,
            norm_first=True,
        )
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.norm = nn.LayerNorm(d_model)
        self.head = nn.Sequential(
            nn.Linear(d_model, max(16, d_model // 2)),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(max(16, d_model // 2), 1),
        )

    def forward(self, sequence: torch.Tensor) -> torch.Tensor:
        # sequence: (batch_size, lookback_hours, n_features)
        # Instance normalization across the lookback window to handle non-stationarity
        mean = sequence.mean(dim=1, keepdim=True)
        std = sequence.std(dim=1, keepdim=True).clamp(min=1e-5)
        norm_seq = (sequence - mean) / std

        # Extract patches: unfold along dimension 1 (time)
        patches = norm_seq.unfold(1, self.patch_length, self.patch_stride)
        # patches: (batch, n_patches, n_features, patch_length) -> flatten to (batch, n_patches, patch_dim)
        batch_size = sequence.shape[0]
        tokens = patches.contiguous().view(batch_size, self.n_patches, -1)

        embedded = self.patch_projection(tokens) + self.position[:, : tokens.shape[1]]
        encoded = self.encoder(embedded)
        last_rep = self.norm(encoded[:, -1])
        output = self.head(last_rep)
        return output.squeeze(-1)


def build_causal_sequences(
    x: np.ndarray,
    lookback: int,
    indices: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Construct causal 3D sequence tensors for the requested row indices."""
    valid_indices = [idx for idx in indices if idx >= lookback - 1]
    if not valid_indices:
        return np.empty((0, lookback, x.shape[1]), dtype=np.float32), np.empty(0, dtype=int)

    sequences = np.empty((len(valid_indices), lookback, x.shape[1]), dtype=np.float32)
    for pos, idx in enumerate(valid_indices):
        sequences[pos] = x[idx - lookback + 1 : idx + 1]
    return sequences, np.asarray(valid_indices, dtype=int)


@dataclass(slots=True)
class PatchTransformerEnsemble:
    """Ensemble of PatchTemporalModels across five seeds with GPU acceleration."""

    config: V5Config
    feature_names: tuple[str, ...]
    seeds: tuple[int, ...]
    members: list[PatchTemporalModel]
    device: torch.device

    @classmethod
    def create(
        cls,
        *,
        config: V5Config,
        feature_names: tuple[str, ...],
        seeds: tuple[int, ...] | None = None,
    ) -> PatchTransformerEnsemble:
        dev_str = config.tf_device.lower()
        if dev_str == "cuda" and torch.cuda.is_available():
            device = torch.device("cuda")
        else:
            device = torch.device("cpu")
        return cls(
            config=config,
            feature_names=tuple(feature_names),
            seeds=tuple(config.seeds if seeds is None else seeds),
            members=[],
            device=device,
        )

    @property
    def ensemble_id(self) -> str:
        payload = json.dumps(
            {
                "lookback": self.config.tf_lookback_hours,
                "d_model": self.config.tf_d_model,
                "seeds": self.seeds,
                "features": self.feature_names,
            },
            sort_keys=True,
            default=str,
        ).encode("utf-8")
        return hashlib.sha256(payload).hexdigest()[:16]

    def fit(self, x: np.ndarray, y: np.ndarray, train_indices: np.ndarray) -> dict[str, Any]:
        x_clean = np.nan_to_num(x, nan=0.0)
        lookback = self.config.tf_lookback_hours
        seqs, valid_idx = build_causal_sequences(x_clean, lookback, train_indices)
        if len(valid_idx) == 0:
            raise ValueError("not enough historical rows to construct lookback sequences")

        targets = y[valid_idx].astype(np.float32)
        n_features = len(self.feature_names)
        self.members = []

        for seed in self.seeds:
            torch.manual_seed(seed)
            if self.device.type == "cuda":
                torch.cuda.manual_seed_all(seed)

            model = PatchTemporalModel(
                n_features=n_features,
                lookback_hours=lookback,
                d_model=self.config.tf_d_model,
                nhead=self.config.tf_nhead,
                num_layers=self.config.tf_num_layers,
                dim_feedforward=self.config.tf_dim_feedforward,
                dropout=self.config.tf_dropout,
                patch_length=self.config.tf_patch_length,
                patch_stride=self.config.tf_patch_stride,
            ).to(self.device)

            dataset = TensorDataset(torch.from_numpy(seqs), torch.from_numpy(targets))
            loader = DataLoader(dataset, batch_size=self.config.tf_batch_size, shuffle=True)

            optimizer = torch.optim.AdamW(
                model.parameters(), lr=self.config.tf_learning_rate, weight_decay=1e-3
            )
            scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
                optimizer, T_max=self.config.tf_epochs
            )
            loss_fn = nn.SmoothL1Loss(beta=0.005)

            model.train()
            for _ in range(self.config.tf_epochs):
                for batch_x, batch_y in loader:
                    batch_x = batch_x.to(self.device)
                    batch_y = batch_y.to(self.device)
                    optimizer.zero_grad()
                    pred = model(batch_x)
                    loss = loss_fn(pred, batch_y)
                    loss.backward()
                    nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                    optimizer.step()
                scheduler.step()

            model.eval()
            self.members.append(model)

        return {
            "train_samples": len(valid_idx),
            "members": len(self.members),
            "device": str(self.device),
            "ensemble_id": self.ensemble_id,
        }

    def predict_members(self, x: np.ndarray, indices: np.ndarray | None = None) -> np.ndarray:
        if not self.members:
            raise RuntimeError("ensemble must be fitted before prediction")
        lookback = self.config.tf_lookback_hours
        x_clean = np.nan_to_num(x, nan=0.0)
        target_indices = np.arange(len(x)) if indices is None else np.asarray(indices, dtype=int)
        seqs, valid_idx = build_causal_sequences(x_clean, lookback, target_indices)

        predictions = np.zeros((len(self.members), len(target_indices)), dtype=float)
        if len(valid_idx) == 0:
            return predictions

        idx_map = {orig_idx: pos for pos, orig_idx in enumerate(target_indices)}
        valid_positions = [idx_map[idx] for idx in valid_idx]

        with torch.no_grad():
            tensor_seqs = torch.from_numpy(seqs).to(self.device)
            for m_pos, model in enumerate(self.members):
                preds = model(tensor_seqs).cpu().numpy().astype(float)
                predictions[m_pos, valid_positions] = preds

        return predictions

    def predict_summary(
        self, x: np.ndarray, indices: np.ndarray | None = None
    ) -> tuple[np.ndarray, np.ndarray]:
        preds = self.predict_members(x, indices)
        return preds.mean(axis=0), preds.std(axis=0, ddof=0)

    def save_native(self, directory: str | Path) -> Path:
        if not self.members:
            raise RuntimeError("ensemble must be fitted before saving")
        destination = Path(directory)
        destination.mkdir(parents=True, exist_ok=True)
        files: list[str] = []
        for pos, model in enumerate(self.members):
            name = f"member_{pos:02d}.pt"
            torch.save(model.state_dict(), destination / name)
            files.append(name)
        metadata = {
            "format": "pytorch-patch-transformer",
            "ensemble_id": self.ensemble_id,
            "seeds": list(self.seeds),
            "feature_names": list(self.feature_names),
            "lookback_hours": self.config.tf_lookback_hours,
            "members": files,
        }
        (destination / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
        return destination

    def export_onnx(self, directory: str | Path) -> Path:
        if not self.members:
            raise RuntimeError("ensemble must be fitted before ONNX export")
        destination = Path(directory)
        destination.mkdir(parents=True, exist_ok=True)
        dummy_input = torch.zeros(
            (1, self.config.tf_lookback_hours, len(self.feature_names)),
            dtype=torch.float32,
            device=torch.device("cpu"),
        )
        onnx_files: list[str] = []
        for pos, model in enumerate(self.members):
            model.eval()
            orig_dev = next(model.parameters()).device
            model.to("cpu")
            file_name = f"member_{pos:02d}.onnx"
            output_path = destination / file_name
            torch.onnx.export(
                model,
                dummy_input,
                str(output_path),
                input_names=["sequence"],
                output_names=["prediction"],
                dynamic_axes={"sequence": {0: "batch_size"}, "prediction": {0: "batch_size"}},
                opset_version=18,
                dynamo=False,
            )
            model.to(orig_dev)
            onnx_files.append(file_name)

        manifest = {
            "format": "transformer-onnx-ensemble",
            "ensemble_id": self.ensemble_id,
            "feature_names": list(self.feature_names),
            "lookback_hours": self.config.tf_lookback_hours,
            "members": onnx_files,
        }
        (destination / "onnx_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        return destination

    def verify_onnx(self, directory: str | Path, x: np.ndarray, indices: np.ndarray | None = None) -> float:
        try:
            import onnxruntime as ort
        except ImportError as exc:
            raise RuntimeError("install the 'ml' extra to verify ONNX") from exc
        destination = Path(directory)
        manifest_path = destination / "onnx_manifest.json"
        if not manifest_path.exists():
            raise FileNotFoundError(manifest_path)
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

        target_indices = np.arange(len(x)) if indices is None else np.asarray(indices, dtype=int)
        seqs, valid_idx = build_causal_sequences(
            np.nan_to_num(x, nan=0.0), self.config.tf_lookback_hours, target_indices
        )
        if len(valid_idx) == 0:
            return 0.0

        sample_seqs = seqs[: min(32, len(seqs))].astype(np.float32)
        with torch.no_grad():
            tensor_seqs = torch.from_numpy(sample_seqs).to(self.device)
            native = np.vstack([m(tensor_seqs).cpu().numpy() for m in self.members])

        onnx_predictions: list[np.ndarray] = []
        for file_name in manifest["members"]:
            session = ort.InferenceSession(str(destination / file_name), providers=["CPUExecutionProvider"])
            input_name = session.get_inputs()[0].name
            pred = session.run(None, {input_name: sample_seqs})[0]
            onnx_predictions.append(np.asarray(pred, dtype=float).reshape(-1))

        onnx_array = np.vstack(onnx_predictions)
        max_err = float(np.max(np.abs(native - onnx_array)))
        if max_err > 1e-4:
            raise ValueError(f"Transformer ONNX parity check failed: {max_err:.2e} > 1e-4")
        return max_err
