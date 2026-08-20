"""Small, pre-registered V4.2 XGBoost search.

This is deliberately a fixed candidate list rather than an open-ended
optimizer.  The search is run on the earliest development folds with one
seed, then the chosen parameters are frozen before the 12-fold/five-seed
evaluation.  That keeps the refinement reproducible and limits multiple
testing.
"""

from __future__ import annotations

from typing import Any

from bottrade.v4.backtest import WalkForwardResult, run_walk_forward
from bottrade.v4.config import V4Config
from bottrade.v4.features import DirectDataset


def refined_candidate_grid() -> tuple[dict[str, Any], ...]:
    """Return the eight V4.2 candidates registered in the protocol."""

    return (
        {
            "candidate_id": "xgb_01_baseline",
            "n_estimators": 400,
            "max_depth": 5,
            "learning_rate": 0.03,
            "min_child_weight": 20.0,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "reg_lambda": 5.0,
        },
        {
            "candidate_id": "xgb_02_shallow",
            "n_estimators": 600,
            "max_depth": 3,
            "learning_rate": 0.03,
            "min_child_weight": 10.0,
            "subsample": 0.8,
            "colsample_bytree": 0.9,
            "reg_lambda": 10.0,
        },
        {
            "candidate_id": "xgb_03_low_lr",
            "n_estimators": 700,
            "max_depth": 4,
            "learning_rate": 0.02,
            "min_child_weight": 20.0,
            "subsample": 0.9,
            "colsample_bytree": 0.8,
            "reg_lambda": 20.0,
        },
        {
            "candidate_id": "xgb_04_regularized",
            "n_estimators": 400,
            "max_depth": 4,
            "learning_rate": 0.05,
            "min_child_weight": 30.0,
            "subsample": 0.8,
            "colsample_bytree": 0.7,
            "reg_lambda": 20.0,
        },
        {
            "candidate_id": "xgb_05_conservative",
            "n_estimators": 300,
            "max_depth": 3,
            "learning_rate": 0.05,
            "min_child_weight": 40.0,
            "subsample": 1.0,
            "colsample_bytree": 0.8,
            "reg_lambda": 20.0,
        },
        {
            "candidate_id": "xgb_06_deeper",
            "n_estimators": 300,
            "max_depth": 6,
            "learning_rate": 0.03,
            "min_child_weight": 30.0,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "reg_lambda": 20.0,
        },
        {
            "candidate_id": "xgb_07_high_min_child",
            "n_estimators": 500,
            "max_depth": 4,
            "learning_rate": 0.03,
            "min_child_weight": 60.0,
            "subsample": 0.9,
            "colsample_bytree": 1.0,
            "reg_lambda": 10.0,
        },
        {
            "candidate_id": "xgb_08_fast",
            "n_estimators": 250,
            "max_depth": 5,
            "learning_rate": 0.05,
            "min_child_weight": 30.0,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "reg_lambda": 5.0,
        },
    )


def _xgb_params(candidate: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in candidate.items() if key != "candidate_id"}


def tuning_score(metrics: dict[str, float | int], *, minimum_trades: int = 5) -> float:
    """Risk-aware, cost-aware score fixed before looking at candidate results."""

    trades = int(metrics.get("closed_trades", 0))
    if trades < minimum_trades:
        # Keep rejected candidates visible while making them ineligible to win.
        return -1_000_000.0 + float(trades)
    base = float(metrics.get("total_return", 0.0))
    stress = float(metrics.get("stress_total_return", 0.0))
    drawdown = float(metrics.get("maximum_drawdown", 0.0))
    return 0.5 * base + 0.5 * stress - drawdown


def run_parameter_search(
    dataset: DirectDataset,
    *,
    config: V4Config,
    max_folds: int = 3,
    seeds: tuple[int, ...] = (11,),
    candidates: tuple[dict[str, Any], ...] | None = None,
) -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, WalkForwardResult]]:
    """Search fixed candidates on early development folds.

    Returns the winning parameter JSON (without the human-readable id), a
    serializable ranking, and the raw walk-forward results for diagnostics.
    """

    if max_folds < 1:
        raise ValueError("max_folds must be positive")
    registered = refined_candidate_grid() if candidates is None else candidates
    ranking: list[dict[str, Any]] = []
    results: dict[str, WalkForwardResult] = {}
    for candidate in registered:
        candidate_id = str(candidate["candidate_id"])
        result = run_walk_forward(
            dataset,
            config=config,
            params=_xgb_params(candidate),
            max_folds=max_folds,
            seeds_override=seeds,
            fold_selection="first",
            evaluation_split="calibration",
        )
        results[candidate_id] = result
        metrics = result.metrics
        ranking.append(
            {
                "candidate_id": candidate_id,
                "params": _xgb_params(candidate),
                "score": tuning_score(metrics),
                "metrics": metrics,
            }
        )
    ranking.sort(key=lambda row: (float(row["score"]), str(row["candidate_id"])), reverse=True)
    if not ranking or float(ranking[0]["score"]) <= -1_000_000.0:
        # The best predictive candidate is still useful for feature ablations,
        # but the report marks it as not economically approved.
        winner = max(ranking, key=lambda row: float(row["score"]))
    else:
        winner = ranking[0]
    return dict(winner["params"]), ranking, results
