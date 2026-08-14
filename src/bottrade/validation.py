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
) -> list[WalkForwardFold]:
    times = pd.DatetimeIndex(pd.to_datetime(timestamps, utc=True))
    if not times.is_monotonic_increasing:
        raise ValueError("timestamps must be sorted")
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
                )
            )
        cursor = cursor + pd.DateOffset(months=test_months)
    return folds


def assert_purged(fold: WalkForwardFold, timestamps: pd.Series, purge_hours: int) -> None:
    times = pd.DatetimeIndex(pd.to_datetime(timestamps, utc=True))
    purge = pd.Timedelta(hours=purge_hours)
    if times[fold.train_indices].max() > fold.calibration_start - purge:
        raise AssertionError("train/calibration purge was violated")
    if times[fold.calibration_indices].max() > fold.test_start - purge:
        raise AssertionError("calibration/test purge was violated")
