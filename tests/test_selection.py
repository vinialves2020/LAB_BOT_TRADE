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


def _search_rejection(root: Path, *, asset: Asset, family: ModelFamily) -> None:
    path = root / asset.value / DataArm.MARKET.value / family.value / "rejections" / "r.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "status": "rejected",
                "stage": "hyperparameter_search",
                "scope": "family",
                "rejection_id": f"{family.value}-rejected",
                "created_at": "2025-07-31T00:00:00Z",
                "phase": "development",
                "asset": asset.value,
                "family": family.value,
                "data_arm": DataArm.MARKET.value,
                "protocol_rejection_eligible": True,
                "source_control": {"commit": "a" * 40, "dirty": False},
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


def test_selection_accepts_a_formally_rejected_family(app_config) -> None:
    root = app_config.project.artifact_dir / "experiments"
    _search_rejection(root, asset=Asset.ETHUSDT, family=ModelFamily.RANDOM_FOREST)
    for arm in DataArm:
        _record(
            root,
            asset=Asset.ETHUSDT,
            family=ModelFamily.TRANSFORMER,
            arm=arm,
            score=float(list(DataArm).index(arm) + 1),
        )
    lock = SelectionManager(app_config).select(Asset.ETHUSDT)
    assert lock.status == "selected"
    assert lock.family == ModelFamily.TRANSFORMER
    rejected = [item for item in lock.candidates if item["status"] == "rejected"]
    assert len(rejected) == 4
    assert {item["key"].split(":")[0] for item in rejected} == {
        ModelFamily.RANDOM_FOREST.value
    }


def test_selection_goes_to_cash_when_both_families_are_formally_rejected(app_config) -> None:
    root = app_config.project.artifact_dir / "experiments"
    for family in (ModelFamily.RANDOM_FOREST, ModelFamily.TRANSFORMER):
        _search_rejection(root, asset=Asset.SOLUSDT, family=family)
    lock = SelectionManager(app_config).select(Asset.SOLUSDT)
    assert lock.status == "cash"
    assert lock.chosen_run_id == ""
    assert all(item["status"] == "rejected" for item in lock.candidates)
