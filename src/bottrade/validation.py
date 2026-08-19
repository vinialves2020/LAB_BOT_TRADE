from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta

import numpy as np
import pandas as pd


@dataclass(frozen=True, slots=True)
class WalkForwardFold:
    name: str
    train_indices: np.ndarray
    calibration_indices: np.ndarray
    test_indices: np.ndarray
    train_start: pd.Timestamp
    train_end: pd.Timestamp
    calibration_start: pd.Timestamp
    calibration_end: pd.Timestamp
    test_start: pd.Timestamp
    test_end: pd.Timestamp
    train_segments: tuple[str, ...] = ()
    calibration_segments: tuple[str, ...] = ()
    test_segments: tuple[str, ...] = ()
    coverage: float = 1.0


def _month_start(value: pd.Timestamp) -> pd.Timestamp:
    naive = value.tz_convert("UTC").tz_localize(None) if value.tzinfo else value
    return pd.Timestamp(naive.to_period("M").start_time, tz="UTC")


def walk_forward_folds(
    timestamps: pd.Series | pd.DatetimeIndex,
    *,
    train_months: int,
    calibration_months: int,
    test_months: int,
    purge_hours: int,
    test_start: pd.Timestamp | None = None,
    test_end: pd.Timestamp | None = None,
    segment_ids: pd.Series | pd.Index | None = None,
    minimum_coverage: float = 0.0,
) -> list[WalkForwardFold]:
    times = pd.DatetimeIndex(pd.to_datetime(timestamps, utc=True))
    if not times.is_monotonic_increasing:
        raise ValueError("timestamps must be sorted")
    if not 0.0 <= minimum_coverage <= 1.0:
        raise ValueError("minimum_coverage must be between zero and one")
    segments: pd.Series | None = None
    if segment_ids is not None:
        segments = pd.Series(segment_ids, index=np.arange(len(times)), dtype="string")
        if len(segments) != len(times):
            raise ValueError("segment_ids must have the same length as timestamps")
    earliest = times.min()
    latest = times.max()
    first_possible = _month_start(earliest) + pd.DateOffset(
        months=train_months + calibration_months + 1
    )
    cursor = _month_start(test_start) if test_start is not None else first_possible
    final = _month_start(test_end) + pd.DateOffset(months=1) if test_end is not None else latest
    purge = timedelta(hours=purge_hours)
    folds: list[WalkForwardFold] = []
    while cursor < final and cursor <= latest:
        fold_test_end = cursor + pd.DateOffset(months=test_months)
        calibration_start = cursor - pd.DateOffset(months=calibration_months)
        train_start = calibration_start - pd.DateOffset(months=train_months)
        train_end = calibration_start - purge
        calibration_end = cursor - purge
        train_mask = (times >= train_start) & (times < train_end)
        calibration_mask = (times >= calibration_start) & (times < calibration_end)
        test_mask = (times >= cursor) & (times < fold_test_end)
        if train_mask.any() and calibration_mask.any() and test_mask.any():
            expected_hours = max(
                int((fold_test_end - cursor).total_seconds() // 3600), 1
            )
            coverage = float(test_mask.sum()) / expected_hours
            if coverage < minimum_coverage:
                cursor = cursor + pd.DateOffset(months=test_months)
                continue
            def _segments(mask: np.ndarray) -> tuple[str, ...]:
                if segments is None:
                    return ()
                return tuple(sorted(set(segments.iloc[np.flatnonzero(mask)].dropna().tolist())))

            folds.append(
                WalkForwardFold(
                    name=cursor.strftime("%Y-%m"),
                    train_indices=np.flatnonzero(train_mask),
                    calibration_indices=np.flatnonzero(calibration_mask),
                    test_indices=np.flatnonzero(test_mask),
                    train_start=train_start,
                    train_end=pd.Timestamp(train_end),
                    calibration_start=pd.Timestamp(calibration_start),
                    calibration_end=pd.Timestamp(calibration_end),
                    test_start=cursor,
                    test_end=pd.Timestamp(fold_test_end),
                    train_segments=_segments(train_mask),
                    calibration_segments=_segments(calibration_mask),
                    test_segments=_segments(test_mask),
                    coverage=coverage,
                )
            )
        cursor = cursor + pd.DateOffset(months=test_months)
    return folds


def continuity_segments(
    timestamps: pd.Series | pd.DatetimeIndex,
    *,
    expected_frequency: str = "1h",
) -> pd.Series:
    """Return stable segment identifiers without filling missing observations."""

    times = pd.Series(pd.to_datetime(timestamps, utc=True)).reset_index(drop=True)
    if times.empty:
        return pd.Series(dtype="string")
    delta = times.diff().gt(pd.Timedelta(expected_frequency)).fillna(False)
    segment_number = delta.cumsum().astype(int)
    return segment_number.map(lambda value: f"segment-{int(value):04d}").astype("string")


def valid_continuity_mask(
    timestamps: pd.Series | pd.DatetimeIndex,
    *,
    lookback_hours: int,
    max_horizon_hours: int,
    expected_frequency: str = "1h",
) -> pd.Series:
    """Mark rows whose complete lookback and label windows remain in one segment."""

    times = pd.Series(pd.to_datetime(timestamps, utc=True)).reset_index(drop=True)
    segments = continuity_segments(times, expected_frequency=expected_frequency)
    expected = pd.Timedelta(expected_frequency)
    output = np.zeros(len(times), dtype=bool)
    for index in range(len(times)):
        start = index - lookback_hours + 1
        end = index + max_horizon_hours + 1
        if start < 0 or end > len(times):
            continue
        window = times.iloc[start:end]
        if (window.diff().dropna() > expected).any():
            continue
        output[index] = segments.iloc[start] == segments.iloc[end - 1]
    return pd.Series(output, index=getattr(timestamps, "index", None))


def require_minimum_folds(folds: list[WalkForwardFold], minimum: int) -> list[WalkForwardFold]:
    if minimum < 1:
        raise ValueError("minimum fold count must be positive")
    if len(folds) < minimum:
        raise ValueError(f"only {len(folds)} valid folds available; need at least {minimum}")
    return folds


def assert_purged(fold: WalkForwardFold, timestamps: pd.Series, purge_hours: int) -> None:
    times = pd.DatetimeIndex(pd.to_datetime(timestamps, utc=True))
    purge = pd.Timedelta(hours=purge_hours)
    if times[fold.train_indices].max() > fold.calibration_start - purge:
        raise AssertionError("train/calibration purge was violated")
    if times[fold.calibration_indices].max() > fold.test_start - purge:
        raise AssertionError("calibration/test purge was violated")
