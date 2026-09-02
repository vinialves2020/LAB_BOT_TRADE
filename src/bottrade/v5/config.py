from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True, slots=True)
class V5Config:
    protocol_version: str = "v5-rf-transformer-benchmark"
    timezone: str = "UTC"
    holdout_start: str = "2025-08-01T00:00:00Z"
    holdout_end: str = "2026-07-31T23:59:59Z"
    seeds: tuple[int, ...] = (11, 23, 37, 53, 71)

    # Random Forest
    rf_n_estimators: int = 100
    rf_max_depth: int = 10
    rf_max_samples: float = 0.5
    rf_max_features: float = 0.4
    rf_min_samples_leaf: int = 5
    rf_n_jobs: int = -1

    # Transformer
    tf_d_model: int = 64
    tf_nhead: int = 4
    tf_num_layers: int = 2
    tf_dim_feedforward: int = 128
    tf_dropout: float = 0.1
    tf_patch_length: int = 6
    tf_patch_stride: int = 3
    tf_lookback_hours: int = 72
    tf_learning_rate: float = 0.001
    tf_epochs: int = 25
    tf_batch_size: int = 64
    tf_device: str = "cuda"

    # XGBoost
    xgb_max_depth: int = 4
    xgb_learning_rate: float = 0.05
    xgb_n_estimators: int = 150
    xgb_subsample: float = 0.8
    xgb_colsample_bytree: float = 0.8
    xgb_objective: str = "reg:squarederror"
    xgb_tree_method: str = "hist"

    # Costs
    round_trip_bps: float = 24.0
    stress_multiplier: float = 2.0
    entry_margins_bps: tuple[int, ...] = (0, 5, 10, 20, 30)

    # Policy
    stateful_hourly: bool = True
    max_holding_hours: int = 12
    exit_on_non_positive: bool = False
    uncertainty_std_multiplier: float = 0.0

    # Validation
    train_months: int = 24
    calibration_months: int = 3
    test_months: int = 1
    purge_hours: int = 12
    minimum_pre_holdout_folds: int = 12
    max_round_trips_per_asset_day: int = 2
    minimum_calibration_trades: int = 10

    # Gates
    minimum_asset_monthly_trades: int = 4
    minimum_portfolio_monthly_trades: int = 12
    minimum_sharpe: float = 1.0
    minimum_profit_factor: float = 1.2
    maximum_drawdown: float = 0.08

    # Data
    include_intrahour_15m: bool = True
    stationary_features: bool = True
    feature_schema_version: str = "v5-rf-transformer-stationary"

    def validate(self) -> V5Config:
        if self.timezone != "UTC":
            raise ValueError("V5 must use UTC")
        if len(self.seeds) != 5:
            raise ValueError("V5 requires exactly five ensemble seeds")
        if self.rf_n_estimators <= 0 or self.rf_max_depth <= 0:
            raise ValueError("RF n_estimators and max_depth must be positive")
        if not (0.0 < self.rf_max_samples <= 1.0):
            raise ValueError("RF max_samples must be in (0, 1]")
        if self.tf_patch_length < 1 or self.tf_patch_stride < 1:
            raise ValueError("Transformer patch settings must be positive")
        if self.tf_lookback_hours < self.tf_patch_length:
            raise ValueError("Transformer lookback must cover patch_length")
        if self.round_trip_bps < 0 or any(m < 0 for m in self.entry_margins_bps):
            raise ValueError("Costs and margins cannot be negative")
        return self


def _section(raw: dict[str, Any], name: str) -> dict[str, Any]:
    section = raw.get(name, {})
    return section if isinstance(section, dict) else {}


def load_v5_config(path: str | Path = "config/v5.yaml") -> V5Config:
    with Path(path).open("r", encoding="utf-8") as handle:
        raw = yaml.safe_load(handle) or {}
    defaults = V5Config()
    project = _section(raw, "project")
    models = _section(raw, "models")
    rf = _section(models, "random_forest")
    tf = _section(models, "transformer")
    xgb = _section(models, "xgboost")
    costs = _section(raw, "costs")
    policy = _section(raw, "policy")
    validation = _section(raw, "validation")
    gates = _section(raw, "gates")
    data = _section(raw, "data")

    seeds_val = models.get("seeds", defaults.seeds)
    seeds = tuple(int(v) for v in seeds_val) if isinstance(seeds_val, (list, tuple)) else defaults.seeds
    margins_val = costs.get("entry_margins_bps", defaults.entry_margins_bps)
    entry_margins = tuple(int(v) for v in margins_val) if isinstance(margins_val, (list, tuple)) else defaults.entry_margins_bps

    return V5Config(
        protocol_version=str(project.get("protocol_version", defaults.protocol_version)),
        timezone=str(project.get("timezone", defaults.timezone)),
        holdout_start=str(project.get("holdout_start", defaults.holdout_start)),
        holdout_end=str(project.get("holdout_end", defaults.holdout_end)),
        seeds=seeds,
        rf_n_estimators=int(rf.get("n_estimators", defaults.rf_n_estimators)),
        rf_max_depth=int(rf.get("max_depth", defaults.rf_max_depth)),
        rf_max_samples=float(rf.get("max_samples", defaults.rf_max_samples)),
        rf_max_features=float(rf.get("max_features", defaults.rf_max_features)),
        rf_min_samples_leaf=int(rf.get("min_samples_leaf", defaults.rf_min_samples_leaf)),
        rf_n_jobs=int(rf.get("n_jobs", defaults.rf_n_jobs)),
        tf_d_model=int(tf.get("d_model", defaults.tf_d_model)),
        tf_nhead=int(tf.get("nhead", defaults.tf_nhead)),
        tf_num_layers=int(tf.get("num_layers", defaults.tf_num_layers)),
        tf_dim_feedforward=int(tf.get("dim_feedforward", defaults.tf_dim_feedforward)),
        tf_dropout=float(tf.get("dropout", defaults.tf_dropout)),
        tf_patch_length=int(tf.get("patch_length", defaults.tf_patch_length)),
        tf_patch_stride=int(tf.get("patch_stride", defaults.tf_patch_stride)),
        tf_lookback_hours=int(tf.get("lookback_hours", defaults.tf_lookback_hours)),
        tf_learning_rate=float(tf.get("learning_rate", defaults.tf_learning_rate)),
        tf_epochs=int(tf.get("epochs", defaults.tf_epochs)),
        tf_batch_size=int(tf.get("batch_size", defaults.tf_batch_size)),
        tf_device=str(tf.get("device", defaults.tf_device)),
        xgb_max_depth=int(xgb.get("max_depth", defaults.xgb_max_depth)),
        xgb_learning_rate=float(xgb.get("learning_rate", defaults.xgb_learning_rate)),
        xgb_n_estimators=int(xgb.get("n_estimators", defaults.xgb_n_estimators)),
        xgb_subsample=float(xgb.get("subsample", defaults.xgb_subsample)),
        xgb_colsample_bytree=float(xgb.get("colsample_bytree", defaults.xgb_colsample_bytree)),
        xgb_objective=str(xgb.get("objective", defaults.xgb_objective)),
        xgb_tree_method=str(xgb.get("tree_method", defaults.xgb_tree_method)),
        round_trip_bps=float(costs.get("round_trip_bps", defaults.round_trip_bps)),
        stress_multiplier=float(costs.get("stress_multiplier", defaults.stress_multiplier)),
        entry_margins_bps=entry_margins,
        stateful_hourly=bool(policy.get("stateful_hourly", defaults.stateful_hourly)),
        max_holding_hours=int(policy.get("max_holding_hours", defaults.max_holding_hours)),
        exit_on_non_positive=bool(policy.get("exit_on_non_positive", defaults.exit_on_non_positive)),
        uncertainty_std_multiplier=float(policy.get("uncertainty_std_multiplier", defaults.uncertainty_std_multiplier)),
        train_months=int(validation.get("train_months", defaults.train_months)),
        calibration_months=int(validation.get("calibration_months", defaults.calibration_months)),
        test_months=int(validation.get("test_months", defaults.test_months)),
        purge_hours=int(validation.get("purge_hours", defaults.purge_hours)),
        minimum_pre_holdout_folds=int(validation.get("minimum_pre_holdout_folds", defaults.minimum_pre_holdout_folds)),
        max_round_trips_per_asset_day=int(validation.get("max_round_trips_per_asset_day", defaults.max_round_trips_per_asset_day)),
        minimum_calibration_trades=int(validation.get("minimum_calibration_trades", defaults.minimum_calibration_trades)),
        minimum_asset_monthly_trades=int(gates.get("minimum_asset_monthly_trades", defaults.minimum_asset_monthly_trades)),
        minimum_portfolio_monthly_trades=int(gates.get("minimum_portfolio_monthly_trades", defaults.minimum_portfolio_monthly_trades)),
        minimum_sharpe=float(gates.get("minimum_sharpe", defaults.minimum_sharpe)),
        minimum_profit_factor=float(gates.get("minimum_profit_factor", defaults.minimum_profit_factor)),
        maximum_drawdown=float(gates.get("maximum_drawdown", defaults.maximum_drawdown)),
        include_intrahour_15m=bool(data.get("include_intrahour_15m", defaults.include_intrahour_15m)),
        stationary_features=bool(data.get("stationary_features", defaults.stationary_features)),
        feature_schema_version=str(data.get("feature_schema_version", defaults.feature_schema_version)),
    ).validate()
