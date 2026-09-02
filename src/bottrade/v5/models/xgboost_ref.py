from __future__ import annotations

from typing import Any

from bottrade.v4.config import V4Config
from bottrade.v4.model import XGBEnsemble
from bottrade.v5.config import V5Config


def create_xgboost_reference(
    *,
    config: V5Config,
    feature_names: tuple[str, ...],
    seeds: tuple[int, ...] | None = None,
) -> XGBEnsemble:
    """Create the reference XGBoost ensemble matching V4.2/V4.3 configuration."""
    v4_cfg = V4Config(
        seeds=config.seeds if seeds is None else seeds,
        objective=config.xgb_objective,
        tree_method=config.xgb_tree_method,
        device="cpu",
    )
    params: dict[str, Any] = {
        "max_depth": config.xgb_max_depth,
        "learning_rate": config.xgb_learning_rate,
        "n_estimators": config.xgb_n_estimators,
        "subsample": config.xgb_subsample,
        "colsample_bytree": config.xgb_colsample_bytree,
        "objective": config.xgb_objective,
        "tree_method": config.xgb_tree_method,
    }
    return XGBEnsemble.create(
        config=v4_cfg,
        feature_names=feature_names,
        params=params,
        seeds=seeds,
    )
