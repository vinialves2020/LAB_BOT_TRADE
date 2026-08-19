"""Cost-aware multi-horizon target and decision utilities for protocol V2.

The training runner can use these pure functions with any model family.  Keeping
the target construction and trading policy independent of a particular model
prevents RF, boosting and Transformer implementations from silently receiving
different labels.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

import numpy as np
import pandas as pd

from bottrade.domain import HorizonForecast


@dataclass(frozen=True, slots=True)
class HorizonTargets:
    horizons: tuple[int, ...]
    raw_returns: dict[int, np.ndarray]
    normalized_returns: dict[int, np.ndarray]
    tradeable: dict[int, np.ndarray]


def build_horizon_targets(
    frame: pd.DataFrame,
    *,
    horizons: Iterable[int] = (3, 6, 12),
    cost_bps: float = 24.0,
    execution_open_column: str = "execution_open",
    close_column: str = "reference_close",
    volatility_column: str = "target_volatility",
) -> HorizonTargets:
    """Build labels from already point-in-time aligned dataset columns.

    The function accepts either the raw close series or the feature frame's
    `future_close_{h}h` columns.  It never forward-fills a missing future value.
    """

    selected = tuple(sorted({int(value) for value in horizons}))
    if not selected or any(value <= 0 for value in selected):
        raise ValueError("horizons must contain positive integers")
    execution = pd.to_numeric(frame[execution_open_column], errors="coerce")
    close = pd.to_numeric(frame[close_column], errors="coerce")
    volatility = pd.to_numeric(frame[volatility_column], errors="coerce").replace(0, np.nan)
    raw: dict[int, np.ndarray] = {}
    normalized: dict[int, np.ndarray] = {}
    tradeable: dict[int, np.ndarray] = {}
    threshold = float(cost_bps) / 10_000.0
    for horizon in selected:
        future_name = f"future_close_{horizon}h"
        if future_name in frame:
            future = pd.to_numeric(frame[future_name], errors="coerce")
        else:
            future = close.shift(-horizon)
        returns = np.log(future / execution)
        normalized_return = returns / volatility
        raw[horizon] = returns.to_numpy(dtype=float)
        normalized[horizon] = normalized_return.to_numpy(dtype=float)
        tradeable[horizon] = (returns > threshold).astype(float).to_numpy()
    return HorizonTargets(selected, raw, normalized, tradeable)


class SigmoidCalibrator:
    """Small serializable Platt calibrator for probability outputs."""

    def __init__(self) -> None:
        self._model: object | None = None
        self.constant: float | None = None

    def fit(self, probabilities: np.ndarray, labels: np.ndarray) -> SigmoidCalibrator:
        values = np.asarray(probabilities, dtype=float)
        targets = np.asarray(labels, dtype=int)
        finite = np.isfinite(values) & np.isfinite(targets)
        values = np.clip(values[finite], 1e-6, 1.0 - 1e-6)
        targets = targets[finite]
        if len(values) == 0:
            raise ValueError("cannot calibrate an empty probability vector")
        if np.unique(targets).size < 2:
            self.constant = float(np.mean(targets))
            self._model = None
            return self
        from sklearn.linear_model import LogisticRegression

        logits = np.log(values / (1.0 - values)).reshape(-1, 1)
        model = LogisticRegression(solver="lbfgs", random_state=0)
        model.fit(logits, targets)
        self._model = model
        self.constant = None
        return self

    def predict(self, probabilities: np.ndarray) -> np.ndarray:
        values = np.asarray(probabilities, dtype=float)
        safe = np.clip(values, 1e-6, 1.0 - 1e-6)
        if self._model is None:
            if self.constant is None:
                raise RuntimeError("calibrator has not been fitted")
            return np.full(values.shape, self.constant, dtype=float)
        logits = np.log(safe / (1.0 - safe)).reshape(-1, 1)
        return np.asarray(self._model.predict_proba(logits)[:, 1], dtype=float)


def select_horizon_forecast(
    *,
    horizons: Iterable[int],
    expected_gross_returns: Iterable[float],
    probabilities: Iterable[float],
    round_trip_cost: float,
    probability_threshold: float,
    margin_bps: float,
) -> HorizonForecast | None:
    """Select the best tradable horizon using only frozen calibration values."""

    candidates: list[HorizonForecast] = []
    margin = float(margin_bps) / 10_000.0
    for horizon, gross, probability in zip(
        horizons, expected_gross_returns, probabilities, strict=True
    ):
        gross = float(gross)
        probability = float(probability)
        if not np.isfinite(gross) or not np.isfinite(probability):
            continue
        net = gross - float(round_trip_cost)
        if probability < probability_threshold or gross <= round_trip_cost + margin:
            continue
        candidates.append(
            HorizonForecast(
                horizon_hours=int(horizon),
                expected_gross_return=gross,
                expected_net_return=net,
                probability_net_positive=probability,
                threshold_probability=float(probability_threshold),
                cost_margin_bps=float(margin_bps),
                lower_bound_return=None,
            )
        )
    if not candidates:
        return None
    return max(candidates, key=lambda item: (item.expected_net_return, -item.horizon_hours))


def monthly_trade_gate(
    trades: pd.DataFrame,
    *,
    minimum_average: int = 20,
    minimum_month: int = 10,
    start_time: pd.Timestamp | str | None = None,
    end_time: pd.Timestamp | str | None = None,
) -> dict[str, float | int | bool]:
    """Return an auditable frequency gate without turning it into an entry rule."""

    if trades.empty or "exit_time" not in trades:
        return {
            "average_monthly_trades": 0.0,
            "minimum_monthly_trades": 0,
            "months": 0,
            "passed": False,
        }
    dates = pd.to_datetime(trades["exit_time"], utc=True)
    counts = dates.dt.to_period("M").value_counts().sort_index()
    if start_time is not None or end_time is not None:
        start = pd.Timestamp(start_time if start_time is not None else dates.min())
        end = pd.Timestamp(end_time if end_time is not None else dates.max())
        start = start.tz_localize("UTC") if start.tzinfo is None else start.tz_convert("UTC")
        end = end.tz_localize("UTC") if end.tzinfo is None else end.tz_convert("UTC")
        complete_months = pd.period_range(start=start.to_period("M"), end=end.to_period("M"), freq="M")
        counts = counts.reindex(complete_months, fill_value=0)
    average = float(counts.mean()) if len(counts) else 0.0
    minimum = int(counts.min()) if len(counts) else 0
    return {
        "average_monthly_trades": average,
        "minimum_monthly_trades": minimum,
        "months": int(len(counts)),
        "passed": bool(average >= minimum_average and minimum >= minimum_month),
    }
