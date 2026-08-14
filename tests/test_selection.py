from __future__ import annotations

import json
from pathlib import Path

import pytest

from bottrade.domain import Asset, DataArm, ModelFamily
from bottrade.selection import SelectionManager


def _record(
    root: Path,
    *,
    asset: Asset,
    family: ModelFamily,
    arm: DataArm,
    score: float,
) -> None:
    run_id = f"{family.value}-{arm.value}"
    path = root / asset.value / arm.value / family.value / run_id / "experiment.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    metrics = {
        "total_return": 0.25,
        "sharpe": 1.5,
        "sortino": score,
        "max_drawdown": 0.04,
        "profit_factor": 1.5,
        "closed_trades": 150,
    }
    path.write_text(
        json.dumps(
            {
                "run_id": run_id,
                "version": f"{run_id}-v1",
                "created_at": "2025-07-31T00:00:00Z",
                "phase": "development",
                "protocol_eligible": True,
                "source_control": {"commit": "a" * 40, "dirty": False},
                "explainability_complete": True,
                "onnx_max_abs_error": 0.0,
                "onnx_tolerance": 0.0001,
                "asset": asset.value,
                "family": family.value,
                "arm": arm.value,
                "data_version": "frozen-data-v1",
                "feature_schema_version": "features-v2",
                "parameters": {"family": family.value},
                "selection_metrics": metrics,
                "selection_stress_metrics": {**metrics, "total_return": 0.10},
                "benchmark_metrics": {"ridge": {"sortino": 0.5}},
                "median_fold_sortino": score,
            },
            sort_keys=True,
        ),
        encoding="utf-8",
    )


def test_selection_freezes_roles_before_holdout(app_config) -> None:
    scores = iter(range(1, 9))
    for family in (ModelFamily.RANDOM_FOREST, ModelFamily.TRANSFORMER):
        for arm in DataArm:
            _record(
                app_config.project.artifact_dir / "experiments",
                asset=Asset.BTCUSDT,
                family=family,
                arm=arm,
                score=float(next(scores)),
            )
    manager = SelectionManager(app_config)
    lock = manager.select(Asset.BTCUSDT)
    assert lock.status == "selected"
    assert lock.roles["champion"]["family"] == ModelFamily.TRANSFORMER.value
    assert lock.roles["champion"]["data_arm"] == DataArm.MARKET_ALL.value
    assert lock.roles["market_fallback"]["data_arm"] == DataArm.MARKET.value
    assert lock.roles["challenger"]["run_id"] != lock.roles["champion"]["run_id"]
    with pytest.raises(FileExistsError):
        manager.select(Asset.BTCUSDT)

    claimed = manager.claim_holdout(Asset.BTCUSDT, role="champion")
    assert "champion" in claimed.holdout_opened_at
    completed = manager.complete_holdout(Asset.BTCUSDT, "champion", "holdout-v1")
    assert completed.holdout_versions["champion"] == "holdout-v1"
    with pytest.raises(ValueError, match="already completed"):
        manager.claim_holdout(Asset.BTCUSDT, role="champion")


def test_selection_refuses_incomplete_candidate_matrix(app_config) -> None:
    _record(
        app_config.project.artifact_dir / "experiments",
        asset=Asset.ETHUSDT,
        family=ModelFamily.RANDOM_FOREST,
        arm=DataArm.MARKET,
        score=2.0,
    )
    with pytest.raises(ValueError, match="all eight"):
        SelectionManager(app_config).select(Asset.ETHUSDT)
