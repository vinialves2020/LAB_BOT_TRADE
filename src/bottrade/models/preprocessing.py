from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass(slots=True)
class RobustStandardizer:
    median: np.ndarray | None = None
    mean: np.ndarray | None = None
    scale: np.ndarray | None = None
    passthrough_indices: tuple[int, ...] = ()

    def fit(self, x: np.ndarray) -> RobustStandardizer:
        self.median = np.nanmedian(x, axis=0)
        self.median = np.where(np.isfinite(self.median), self.median, 0.0)
        filled = np.where(np.isfinite(x), x, self.median)
        self.mean = filled.mean(axis=0)
        self.scale = filled.std(axis=0)
        self.scale = np.where((self.scale > 1e-12) & np.isfinite(self.scale), self.scale, 1.0)
        if self.passthrough_indices:
            self.mean[list(self.passthrough_indices)] = 0.0
            self.scale[list(self.passthrough_indices)] = 1.0
        return self

    def transform(self, x: np.ndarray) -> np.ndarray:
        if self.median is None or self.mean is None or self.scale is None:
            raise RuntimeError("standardizer has not been fitted")
        filled = np.where(np.isfinite(x), x, self.median)
        return ((filled - self.mean) / self.scale).astype(np.float32)

    def write(self, path: Path) -> None:
        if self.median is None or self.mean is None or self.scale is None:
            raise RuntimeError("standardizer has not been fitted")
        payload = {
            "median": self.median.tolist(),
            "mean": self.mean.tolist(),
            "scale": self.scale.tolist(),
            "passthrough_indices": list(self.passthrough_indices),
        }
        path.write_text(json.dumps(payload, separators=(",", ":")), encoding="utf-8")

    @classmethod
    def read(cls, path: Path) -> RobustStandardizer:
        payload = json.loads(path.read_text(encoding="utf-8"))
        return cls(
            median=np.asarray(payload["median"], dtype=float),
            mean=np.asarray(payload["mean"], dtype=float),
            scale=np.asarray(payload["scale"], dtype=float),
            passthrough_indices=tuple(int(value) for value in payload.get("passthrough_indices", [])),
        )
