from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


def _as_int_list(value: Any, default: list[int]) -> list[int]:
    if value is None:
        return list(default)
    return [int(item) for item in value]


def _as_float_list(value: Any, default: list[float]) -> list[float]:
    if value is None:
        return list(default)
    return [float(item) for item in value]


@dataclass(frozen=True, slots=True)
class V3Config:
    protocol_version: str = "v3"
    timezone: str = "UTC"
    holdout_start: str = "2025-08-01T00:00:00Z"
    holdout_end: str = "2026-07-31T23:59:59Z"
    train_months: int = 24
    calibration_months: int = 3
    test_months: int = 1
    purge_hours: int = 12
    minimum_pre_holdout_folds: int = 12
    seeds: tuple[int, ...] = (11, 23, 37, 53, 71)
    decision_interval: str = "1h"
    execution_interval: str = "15m"
    lookback_hours: int = 168
    horizons: tuple[int, ...] = (3, 6, 12)
    max_variants_per_family: int = 12
    probability_thresholds: tuple[float, ...] = (0.50, 0.55, 0.60)
    margin_bps: tuple[int, ...] = (0, 5, 10, 20, 30)
    take_profit_vol_multiplier: float = 0.75
    stop_loss_vol_multiplier: float = 1.0
    fallback_fee_bps_per_leg: float = 10.0
    fallback_spread_bps: float = 2.0
    fallback_slippage_bps: float = 1.0
    stress_multipliers: tuple[float, ...] = (1.0, 2.0, 3.0)
    minimum_portfolio_trades_holdout: int = 240
    minimum_portfolio_trades_paper: int = 120
    minimum_asset_oos_trades: int = 60
    minimum_trades_per_month: int = 20
    minimum_trades_per_complete_month: int = 10
    minimum_calibration_trades: int = 60
    minimum_sharpe: float = 1.0
    minimum_sharpe_ci_lower: float = 0.0
    minimum_profit_factor: float = 1.2
    maximum_drawdown: float = 0.08
    minimum_dsr_probability: float = 0.95
    maximum_pbo: float = 0.20
    minimum_nonnegative_folds: int = 7
    max_asset_weight: float = 0.20
    max_gross_weight: float = 0.50
    rebalance_band: float = 0.02
    daily_loss_limit: float = 0.01
    position_loss_limit: float = 0.005
    drawdown_circuit_breaker: float = 0.08
    maximum_round_trips_per_asset_day: int = 2
    random_forest_trials: int = 8
    hist_gradient_boosting_trials: int = 12
    transformer_trials: int = 6
    optuna_storage: str = "data/optuna_v3.db"
    feature_schema_version: str = "features-v5"
    strategy_variants: dict[str, tuple[str, ...]] = field(
        default_factory=lambda: {
            "trend": (
                "trend_ema_6_24_h6",
                "trend_ema_12_48_h12",
                "trend_ema_24_72_h12",
            ),
            "reversal": (
                "reversal_3h_z2_h3",
                "reversal_3h_z25_h3",
                "reversal_6h_z2_h6",
                "reversal_6h_z25_h6",
            ),
            "breakout": (
                "breakout_24h_h6",
                "breakout_24h_h12",
                "breakout_72h_h6",
                "breakout_72h_h12",
            ),
        }
    )

    def validate(self) -> V3Config:
        if self.protocol_version != "v3":
            raise ValueError("V3Config requires protocol_version=v3")
        if self.timezone != "UTC":
            raise ValueError("V3 processing must use UTC")
        if self.purge_hours < max(self.horizons):
            raise ValueError("purge_hours must cover the largest label horizon")
        if len(self.seeds) != 5:
            raise ValueError("V3 requires exactly five final seeds")
        if self.max_asset_weight > self.max_gross_weight:
            raise ValueError("max_asset_weight cannot exceed max_gross_weight")
        if not 0 < self.daily_loss_limit < self.drawdown_circuit_breaker < 1:
            raise ValueError("risk limits must satisfy daily < drawdown < 1")
        if self.minimum_nonnegative_folds < 1 or self.minimum_nonnegative_folds > 12:
            raise ValueError("minimum_nonnegative_folds must be between 1 and 12")
        if any(
            value < 1
            for value in (
                self.minimum_trades_per_month,
                self.minimum_trades_per_complete_month,
                self.minimum_calibration_trades,
            )
        ):
            raise ValueError("trade frequency gates must be positive")
        if any(value <= 0 for value in self.horizons):
            raise ValueError("horizons must be positive")
        if any(not 0 < value <= 1 for value in self.probability_thresholds):
            raise ValueError("probability thresholds must be in (0, 1]")
        if any(value < 0 for value in self.margin_bps):
            raise ValueError("margins cannot be negative")
        for family, variants in self.strategy_variants.items():
            if len(variants) > self.max_variants_per_family:
                raise ValueError(f"too many variants for {family}")
        if any(value < 1 for value in self.stress_multipliers):
            raise ValueError("stress multipliers must be at least one")
        return self


def _section(raw: dict[str, Any], name: str) -> dict[str, Any]:
    value = raw.get(name, {})
    if not isinstance(value, dict):
        raise ValueError(f"config section {name!r} must be a mapping")
    return value


def load_v3_config(path: str | Path = "config/v3.yaml") -> V3Config:
    config_path = Path(path)
    with config_path.open("r", encoding="utf-8") as handle:
        raw = yaml.safe_load(handle) or {}
    training = _section(raw, "training")
    strategies = _section(raw, "strategies")
    labels = _section(raw, "event_labels")
    policy = _section(raw, "meta_policy")
    search = _section(raw, "search")
    costs = _section(raw, "costs")
    portfolio = _section(raw, "portfolio")
    gates = _section(raw, "gates")
    defaults = V3Config()
    variants = strategies.get("variants", defaults.strategy_variants)
    parsed_variants = {str(key): tuple(str(item) for item in value) for key, value in variants.items()}
    config = V3Config(
        protocol_version=str(training.get("protocol_version", defaults.protocol_version)),
        timezone=str(raw.get("project", {}).get("timezone", defaults.timezone)),
        holdout_start=str(training.get("holdout_start", defaults.holdout_start)),
        holdout_end=str(training.get("holdout_end", defaults.holdout_end)),
        train_months=int(training.get("train_months", defaults.train_months)),
        calibration_months=int(training.get("calibration_months", defaults.calibration_months)),
        test_months=int(training.get("test_months", defaults.test_months)),
        purge_hours=int(training.get("purge_hours", defaults.purge_hours)),
        minimum_pre_holdout_folds=int(
            training.get("minimum_pre_holdout_folds", defaults.minimum_pre_holdout_folds)
        ),
        seeds=tuple(_as_int_list(training.get("seeds"), list(defaults.seeds))),
        decision_interval=str(strategies.get("decision_interval", defaults.decision_interval)),
        execution_interval=str(strategies.get("execution_interval", defaults.execution_interval)),
        lookback_hours=int(strategies.get("lookback_hours", defaults.lookback_hours)),
        horizons=tuple(_as_int_list(labels.get("horizons"), list(defaults.horizons))),
        max_variants_per_family=int(
            strategies.get("max_variants_per_family", defaults.max_variants_per_family)
        ),
        probability_thresholds=tuple(
            _as_float_list(policy.get("probability_thresholds"), list(defaults.probability_thresholds))
        ),
        margin_bps=tuple(_as_int_list(policy.get("margin_bps"), list(defaults.margin_bps))),
        take_profit_vol_multiplier=float(
            labels.get("take_profit_vol_multiplier", defaults.take_profit_vol_multiplier)
        ),
        stop_loss_vol_multiplier=float(
            labels.get("stop_loss_vol_multiplier", defaults.stop_loss_vol_multiplier)
        ),
        fallback_fee_bps_per_leg=float(
            costs.get("fallback_fee_bps_per_leg", defaults.fallback_fee_bps_per_leg)
        ),
        fallback_spread_bps=float(costs.get("fallback_spread_bps", defaults.fallback_spread_bps)),
        fallback_slippage_bps=float(
            costs.get("fallback_slippage_bps", defaults.fallback_slippage_bps)
        ),
        stress_multipliers=tuple(
            _as_float_list(costs.get("stress_multipliers"), list(defaults.stress_multipliers))
        ),
        minimum_portfolio_trades_holdout=int(
            gates.get("minimum_portfolio_trades_holdout", defaults.minimum_portfolio_trades_holdout)
        ),
        minimum_portfolio_trades_paper=int(
            gates.get("minimum_portfolio_trades_paper", defaults.minimum_portfolio_trades_paper)
        ),
        minimum_asset_oos_trades=int(
            gates.get("minimum_asset_oos_trades", defaults.minimum_asset_oos_trades)
        ),
        minimum_trades_per_month=int(
            gates.get("minimum_trades_per_month", defaults.minimum_trades_per_month)
        ),
        minimum_trades_per_complete_month=int(
            gates.get(
                "minimum_trades_per_complete_month",
                defaults.minimum_trades_per_complete_month,
            )
        ),
        minimum_calibration_trades=int(
            gates.get("minimum_calibration_trades", defaults.minimum_calibration_trades)
        ),
        minimum_sharpe=float(gates.get("minimum_sharpe", defaults.minimum_sharpe)),
        minimum_sharpe_ci_lower=float(
            gates.get("minimum_sharpe_ci_lower", defaults.minimum_sharpe_ci_lower)
        ),
        minimum_profit_factor=float(
            gates.get("minimum_profit_factor", defaults.minimum_profit_factor)
        ),
        maximum_drawdown=float(gates.get("maximum_drawdown", defaults.maximum_drawdown)),
        minimum_dsr_probability=float(
            gates.get("minimum_dsr_probability", defaults.minimum_dsr_probability)
        ),
        maximum_pbo=float(gates.get("maximum_pbo", defaults.maximum_pbo)),
        minimum_nonnegative_folds=int(
            gates.get("minimum_nonnegative_folds", defaults.minimum_nonnegative_folds)
        ),
        max_asset_weight=float(portfolio.get("max_asset_weight", defaults.max_asset_weight)),
        max_gross_weight=float(portfolio.get("max_gross_weight", defaults.max_gross_weight)),
        rebalance_band=float(portfolio.get("rebalance_band", defaults.rebalance_band)),
        daily_loss_limit=float(portfolio.get("daily_loss_limit", defaults.daily_loss_limit)),
        position_loss_limit=float(
            portfolio.get("position_loss_limit", defaults.position_loss_limit)
        ),
        drawdown_circuit_breaker=float(
            portfolio.get("drawdown_circuit_breaker", defaults.drawdown_circuit_breaker)
        ),
        maximum_round_trips_per_asset_day=int(
            portfolio.get(
                "maximum_round_trips_per_asset_day",
                defaults.maximum_round_trips_per_asset_day,
            )
        ),
        random_forest_trials=int(search.get("random_forest_trials", defaults.random_forest_trials)),
        hist_gradient_boosting_trials=int(
            search.get("hist_gradient_boosting_trials", defaults.hist_gradient_boosting_trials)
        ),
        transformer_trials=int(search.get("transformer_trials", defaults.transformer_trials)),
        optuna_storage=str(search.get("persistent_storage", defaults.optuna_storage)),
        feature_schema_version=str(raw.get("features", {}).get("schema_version", defaults.feature_schema_version)),
        strategy_variants=parsed_variants,
    )
    return config.validate()
