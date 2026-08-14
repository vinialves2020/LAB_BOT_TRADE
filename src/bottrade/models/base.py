from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

import numpy as np


class ResearchRegressor(ABC):
    family: str

    @abstractmethod
    def fit(self, x: np.ndarray, y: np.ndarray, indices: np.ndarray) -> dict[str, Any]:
        raise NotImplementedError
    @abstractmethod
    def predict(self, x: np.ndarray, indices: np.ndarray) -> np.ndarray:
        raise NotImplementedError

    @abstractmethod
    def export_onnx(self, path: Path) -> None:
        raise NotImplementedError

    @abstractmethod
    def verify_onnx(self, path: Path, x: np.ndarray, indices: np.ndarray) -> float:
        raise NotImplementedError

    @abstractmethod
    def save_native(self, path: Path) -> None:
        raise NotImplementedError
