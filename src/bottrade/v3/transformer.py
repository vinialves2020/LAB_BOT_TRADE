from __future__ import annotations

from typing import Any

import numpy as np

from bottrade.v3.meta_models import ChronologicalProbabilityCalibrator, MetaModelBundle


class _TransformerNet:
    def __init__(self, input_size: int, seed: int, params: dict[str, Any]) -> None:
        import torch
        from torch import nn

        torch.manual_seed(seed)
        self.input_size = input_size
        self.sequence_length = int(params.get("sequence_length", 168))
        self.patch_length = int(params.get("patch_length", 12))
        self.patch_stride = int(params.get("patch_stride", 6))
        d_model = int(params.get("d_model", 32))
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=int(params.get("nhead", 4)),
            dim_feedforward=int(params.get("dim_feedforward", 64)),
            dropout=float(params.get("dropout", 0.1)),
            batch_first=True,
            norm_first=True,
        )
        self.module = nn.ModuleDict(
            {
                "projection": nn.Linear(input_size * self.patch_length, d_model),
                "encoder": nn.TransformerEncoder(encoder_layer, num_layers=int(params.get("num_layers", 2))),
                "classification": nn.Linear(d_model, 1),
                "return": nn.Linear(d_model, 1),
                "mae": nn.Linear(d_model, 1),
            }
        )
        self.module.float()

    def forward(self, sequence: Any) -> tuple[Any, Any, Any]:

        patches = sequence.unfold(1, self.patch_length, self.patch_stride)
        patches = patches.transpose(2, 3).contiguous().flatten(2)
        encoded = self.module["projection"](patches)
        encoded = self.module["encoder"](encoded).mean(dim=1)
        return (
            self.module["classification"](encoded).squeeze(-1),
            self.module["return"](encoded).squeeze(-1),
            self.module["mae"](encoded).squeeze(-1),
        )

    def predict(self, values: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        import torch

        self.module.eval()
        with torch.no_grad():
            logits, returns, mae = self.forward(torch.from_numpy(values.astype(np.float32)))
        probability = torch.sigmoid(logits).numpy()
        return probability, returns.numpy(), mae.numpy()

    def export_onnx(self, path: Any, sample: np.ndarray) -> None:
        import torch

        self.module.eval()
        example = torch.from_numpy(sample.astype(np.float32))
        wrapper = self.module_wrapper()
        wrapper.eval()
        torch.onnx.export(
            wrapper,
            example,
            str(path),
            input_names=["sequence"],
            output_names=["classification_logit", "expected_return", "expected_mae"],
            dynamic_axes={"sequence": {0: "batch"}},
            opset_version=17,
            dynamo=False,
        )

    def module_wrapper(self) -> Any:
        import torch.nn as nn

        owner = self

        class Wrapper(nn.Module):
            def __init__(self) -> None:
                super().__init__()
                self.owner_module = owner.module

            def forward(self, sequence: Any) -> tuple[Any, Any, Any]:
                patches = sequence.unfold(1, owner.patch_length, owner.patch_stride)
                patches = patches.transpose(2, 3).contiguous().flatten(2)
                encoded = self.owner_module["projection"](patches)
                encoded = self.owner_module["encoder"](encoded).mean(dim=1)
                return (
                    self.owner_module["classification"](encoded).squeeze(-1),
                    self.owner_module["return"](encoded).squeeze(-1),
                    self.owner_module["mae"](encoded).squeeze(-1),
                )

        return Wrapper()


def fit_transformer_meta_model(
    x: np.ndarray,
    y_class: np.ndarray,
    y_return: np.ndarray,
    y_mae: np.ndarray | None,
    *,
    seed: int,
    params: dict[str, Any] | None = None,
) -> MetaModelBundle:
    import torch
    from torch import nn

    parameters = dict(params or {})
    sequence_length = int(parameters.get("sequence_length", 168))
    if x.shape[1] < sequence_length:
        # The caller supplied tabular rows.  Build a one-step sequence rather
        # than silently inventing historical values.
        sequence_length = 1
        parameters["sequence_length"] = 1
        parameters["patch_length"] = 1
        parameters["patch_stride"] = 1
    values = np.asarray(x, dtype=np.float32)
    if values.ndim == 2:
        values = values[:, None, :]
    mean = values.mean(axis=(0, 1), keepdims=True)
    scale = values.std(axis=(0, 1), keepdims=True)
    scale[scale < 1e-6] = 1.0
    normalized = (values - mean) / scale
    net = _TransformerNet(values.shape[2], seed, parameters)
    module = net.module
    optimizer = torch.optim.AdamW(
        module.parameters(),
        lr=float(parameters.get("learning_rate", 5e-4)),
        weight_decay=float(parameters.get("weight_decay", 1e-4)),
    )
    bce = nn.BCEWithLogitsLoss()
    mse = nn.MSELoss()
    tensor_x = torch.from_numpy(normalized.astype(np.float32))
    tensor_class = torch.from_numpy(np.asarray(y_class, dtype=np.float32))
    tensor_return = torch.from_numpy(np.asarray(y_return, dtype=np.float32))
    tensor_mae = torch.from_numpy(np.asarray(y_mae if y_mae is not None else np.zeros(len(x)), dtype=np.float32))
    epochs = int(parameters.get("epochs", 20))
    for _ in range(epochs):
        module.train()
        optimizer.zero_grad()
        logits, predicted_return, predicted_mae = net.forward(tensor_x)
        loss = bce(logits, tensor_class) + mse(predicted_return, tensor_return) + 0.25 * mse(predicted_mae, tensor_mae)
        loss.backward()
        optimizer.step()
    # The MetaModelBundle expects a sequence model object in classifier.
    bundle = MetaModelBundle(
        family="transformer",
        feature_columns=tuple(f"feature_{index}" for index in range(x.shape[-1])),
        classifier=net,
        regressor=None,
        mae_model=None,
        calibrator=ChronologicalProbabilityCalibrator(),
        model_version=f"v3-transformer-seed-{seed}",
        sequence_model=True,
        sequence_length=sequence_length,
        feature_mean=mean.reshape(-1),
        feature_scale=scale.reshape(-1),
    )
    return bundle
