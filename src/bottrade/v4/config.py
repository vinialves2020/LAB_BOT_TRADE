from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True, slots=True)
class V4Config:
    protocol_version: str = "v4-xgb-12h-cost-aware"
    timezone: str = "UTC"
    holdout_start: str = "2025-08-01T00:00:00Z"
    holdout_end: str = "2026-07-31T23:59:59Z"
    family: str = "xgboost"
    horizon_hours: int = 12
    lookback_hours: int = 168
    seeds: tuple[int, ...] = (11, 23, 37, 53, 71)
    objective: str = "reg:pseudohubererror"
    device: str = "cpu"
    tree_method: str = "hist"
    max_trials: int = 20
    uncertainty_std_multiplier: float = 0.0
    calibrate_return_scale: bool = False
    stateful_hourly: bool = False
    max_holding_hours: int = 12
    exit_on_non_positive: bool = False
    normalized_return_target: bool = False
    classification_mode: str = "binary"
    round_trip_bps: float = 24.0
    stress_multiplier: float = 2.0
    entry_margins_bps: tuple[int, ...] = (0, 5, 10, 20, 30)
    train_months: int = 24
    calibration_months: int = 3
    test_months: int = 1
    purge_hours: int = 12
    minimum_pre_holdout_folds: int = 12
    max_round_trips_per_asset_day: int = 2
    minimum_calibration_trades: int = 20
    minimum_average_monthly_trades_portfolio: int = 20
    minimum_calibration_trades_portfolio: int = 60
    minimum_sharpe: float = 1.0
    minimum_profit_factor: float = 1.2
    maximum_drawdown: float = 0.08
    include_intrahour_15m: bool = True
    include_derivatives: bool = False
    include_onchain: bool = False
    include_sentiment: bool = False
    feature_schema_version: str = "v4-xgb-market-1h-15m"
    # V4.2 uses stationary transforms for scale-sensitive activity fields.
    # Keeping this explicit makes the feature change auditable and prevents a
    # refined run from being mistaken for the V4.1 baseline.
    stationary_features: bool = False

    def validate(self) -> V4Config:
        if self.timezone != "UTC":
            raise ValueError("V4 must use UTC")
        if self.family != "xgboost":
            raise ValueError("V4 first family must be xgboost")
        if self.horizon_hours <= 0 or self.lookback_hours < self.horizon_hours:
            raise ValueError("lookback and horizon must be positive and compatible")
        if self.max_holding_hours < self.horizon_hours:
            raise ValueError("max_holding_hours must cover the label horizon")
        if len(self.seeds) != 5:
            raise ValueError("V4 requires exactly five ensemble seeds")
        if self.purge_hours < self.horizon_hours:
            raise ValueError("purge_hours must cover the label horizon")
        if self.round_trip_bps < 0 or any(value < 0 for value in self.entry_margins_bps):
            raise ValueError("costs and margins cannot be negative")
        if not self.uncertainty_std_multiplier >= 0:
            raise ValueError("uncertainty_std_multiplier cannot be negative")
        if self.classification_mode not in {"binary", "ordinal"}:
            raise ValueError("classification_mode must be binary or ordinal")
        return self


def _section(raw: dict[str, Any], name: str) -> dict[str, Any]:
    section = raw.get(name, {})
    if not isinstance(section, dict):
        raise ValueError(f"config section {name!r} must be a mapping")
    return section


def load_v4_config(path: str | Path = "config/v4.yaml") -> V4Config:
    with Path(path).open("r", encoding="utf-8") as handle:
        raw = yaml.safe_load(handle) or {}
    defaults = V4Config()
    project = _section(raw, "project")
    model = _section(raw, "model")
    costs = _section(raw, "costs")
    validation = _section(raw, "validation")
    gates = _section(raw, "gates")
    data = _section(raw, "data")
    result = V4Config(
        protocol_version=str(project.get("protocol_version", defaults.protocol_version)),
        timezone=str(project.get("timezone", defaults.timezone)),
        holdout_start=str(project.get("holdout_start", defaults.holdout_start)),
        holdout_end=str(project.get("holdout_end", defaults.holdout_end)),
        family=str(model.get("family", defaults.family)),
        horizon_hours=int(model.get("horizon_hours", defaults.horizon_hours)),
        lookback_hours=int(model.get("lookback_hours", defaults.lookback_hours)),
        seeds=tuple(int(value) for value in model.get("seeds", defaults.seeds)),
        objective=str(model.get("objective", defaults.objective)),
        device=str(model.get("device", defaults.device)),
        tree_method=str(model.get("tree_method", defaults.tree_method)),
        max_trials=int(model.get("max_trials", defaults.max_trials)),
        uncertainty_std_multiplier=float(
            model.get("uncertainty_std_multiplier", defaults.uncertainty_std_multiplier)
        ),
        calibrate_return_scale=bool(
            model.get("calibrate_return_scale", defaults.calibrate_return_scale)
        ),
        stateful_hourly=bool(model.get("stateful_hourly", defaults.stateful_hourly)),
        max_holding_hours=int(model.get("max_holding_hours", defaults.max_holding_hours)),
        exit_on_non_positive=bool(model.get("exit_on_non_positive", defaults.exit_on_non_positive)),
        normalized_return_target=bool(
            model.get("normalized_return_target", defaults.normalized_return_target)
        ),
        classification_mode=str(model.get("classification_mode", defaults.classification_mode)),
        round_trip_bps=float(costs.get("round_trip_bps", defaults.round_trip_bps)),
        stress_multiplier=float(costs.get("stress_multiplier", defaults.stress_multiplier)),
        entry_margins_bps=tuple(
            int(value) for value in costs.get("entry_margins_bps", defaults.entry_margins_bps)
        ),
        train_months=int(validation.get("train_months", defaults.train_months)),
        calibration_months=int(
            validation.get("calibration_months", defaults.calibration_months)
        ),
        test_months=int(validation.get("test_months", defaults.test_months)),
        purge_hours=int(validation.get("purge_hours", defaults.purge_hours)),
        minimum_pre_holdout_folds=int(
            validation.get("minimum_pre_holdout_folds", defaults.minimum_pre_holdout_folds)
        ),
        max_round_trips_per_asset_day=int(
            validation.get(
                "max_round_trips_per_asset_day", defaults.max_round_trips_per_asset_day
            )
        ),
        minimum_calibration_trades=int(
            validation.get("minimum_calibration_trades", defaults.minimum_calibration_trades)
        ),
        minimum_average_monthly_trades_portfolio=int(
            gates.get(
                "minimum_average_monthly_trades_portfolio",
                defaults.minimum_average_monthly_trades_portfolio,
            )
        ),
        minimum_calibration_trades_portfolio=int(
            gates.get(
                "minimum_calibration_trades_portfolio",
                defaults.minimum_calibration_trades_portfolio,
            )
        ),
        minimum_sharpe=float(gates.get("minimum_sharpe", defaults.minimum_sharpe)),
        minimum_profit_factor=float(
            gates.get("minimum_profit_factor", defaults.minimum_profit_factor)
        ),
        maximum_drawdown=float(gates.get("maximum_drawdown", defaults.maximum_drawdown)),
        include_intrahour_15m=bool(
            data.get("include_intrahour_15m", defaults.include_intrahour_15m)
        ),
        include_derivatives=bool(data.get("include_derivatives", defaults.include_derivatives)),
        include_onchain=bool(data.get("include_onchain", defaults.include_onchain)),
        include_sentiment=bool(data.get("include_sentiment", defaults.include_sentiment)),
        feature_schema_version=str(
            data.get("feature_schema_version", defaults.feature_schema_version)
        ),
        stationary_features=bool(
            data.get("stationary_features", defaults.stationary_features)
        ),
    )
    return result.validate()
