from __future__ import annotations

import pandas as pd

from bottrade.validation import assert_purged, walk_forward_folds


def test_walk_forward_is_monthly_and_purged() -> None:
    times = pd.Series(pd.date_range("2020-01-01", "2024-12-31 23:00", freq="1h", tz="UTC"))
    folds = walk_forward_folds(
        times,
        train_months=24,
        calibration_months=3,
        test_months=1,
        purge_hours=3,
        test_start=pd.Timestamp("2023-01-01", tz="UTC"),
        test_end=pd.Timestamp("2023-03-31", tz="UTC"),
    )
    assert [fold.name for fold in folds] == ["2023-01", "2023-02", "2023-03"]
    for fold in folds:
        assert_purged(fold, times, 3)
        assert len(fold.train_indices) > len(fold.calibration_indices) > len(fold.test_indices)
