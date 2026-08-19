from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, model_validator


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class ProjectConfig(StrictModel):
    name: str
    timezone: str = "UTC"
    data_dir: Path = Path("data")
    artifact_dir: Path = Path("artifacts")
    report_dir: Path = Path("reports/generated")


class MarketConfig(StrictModel):
    symbols: dict[str, str]
    interval: str = "1h"
    additional_intervals: list[str] = Field(default_factory=list)
    quote_asset: str = "USDT"
    archive_base_url: str
    rest_base_url: str
    api_base_url: str
    request_timeout_seconds: int = 30
    max_retries: int = 4


class FeatureConfig(StrictModel):
    horizon_hours: int = 3
    forecast_horizons: list[int] = Field(default_factory=lambda: [3, 6, 12])
    lookback_hours: int = 168
    alternative_delay_hours: int = 24
    alternative_stale_hours: int = 72
    market_stale_minutes: int = 75
    historical_gap_policy: Literal["trim_after_latest_gap", "gap_aware_segments"] = (
        "trim_after_latest_gap"
    )
    intrahour_interval: str = "15m"
    derivatives_stale_hours: int = 72
    label_cost_bps: float = 24.0
    lag_hours: list[int] = Field(default_factory=lambda: [1, 3, 6, 12, 24, 72, 168])
    arms: list[str]

    @model_validator(mode="after")
    def validate_horizons(self) -> FeatureConfig:
        if not self.forecast_horizons or any(value <= 0 for value in self.forecast_horizons):
            raise ValueError("forecast_horizons must contain positive hours")
        if self.horizon_hours not in self.forecast_horizons:
            raise ValueError("horizon_hours must be one of forecast_horizons")
        if self.lookback_hours < max(self.forecast_horizons):
            raise ValueError("lookback_hours must cover the largest forecast horizon")
        if self.label_cost_bps < 0:
            raise ValueError("label_cost_bps cannot be negative")
        return self


class TransformerConfig(StrictModel):
    d_model: int = 64
    nhead: int = 4
    num_layers: int = 2
    dim_feedforward: int = 128
    dropout: float = 0.15
    batch_size: int = 256
    epochs: int = 40
    patience: int = 6
    validation_purge_hours: int = 3
    learning_rate: float = 5e-4
    weight_decay: float = 1e-4
    patch_length: int = 1
    patch_stride: int = 1


class RandomForestConfig(StrictModel):
    n_estimators: int = 500
    max_depth: int | None = 14
    min_samples_leaf: int = 8
    max_features: float | str = 0.7
    n_jobs: int = -1


class HistGradientBoostingConfig(StrictModel):
    learning_rate: float = 0.05
    max_iter: int = 300
    max_leaf_nodes: int = 31
    max_depth: int | None = None
    min_samples_leaf: int = 30
    l2_regularization: float = 1.0
    max_bins: int = 255
    early_stopping: bool = False
    n_jobs: int = -1


class TrainingConfig(StrictModel):
    holdout_start: str
    holdout_end: str
    train_months: int = 24
    calibration_months: int = 3
    test_months: int = 1
    purge_hours: int = 3
    max_trials: int = 30
    seeds: list[int]
    onnx_tolerance: float = 1e-4
    explainability_samples: int = 256
    permutation_repeats: int = 3
    integrated_gradient_steps: int = 32
    protocol_version: str = "v1"
    minimum_pre_holdout_folds: int = 1
    frozen_core_arm: str = "market"
    probability_thresholds: list[float] = Field(default_factory=lambda: [0.50, 0.55, 0.60])
    search_families: list[str] = Field(
        default_factory=lambda: ["random_forest", "transformer"]
    )
    transformer: TransformerConfig = Field(default_factory=TransformerConfig)
    random_forest: RandomForestConfig = Field(default_factory=RandomForestConfig)
    hist_gradient_boosting: HistGradientBoostingConfig = Field(
        default_factory=HistGradientBoostingConfig
    )

    @model_validator(mode="after")
    def validate_protocol(self) -> TrainingConfig:
        if len(self.seeds) < 1:
            raise ValueError("at least one training seed is required")
        if self.protocol_version == "v2" and len(self.seeds) < 5:
            raise ValueError("V2 requires five final seeds")
        if self.purge_hours < 0:
            raise ValueError("purge_hours cannot be negative")
        if any(
            threshold < 0.0 or threshold > 1.0
            for threshold in self.probability_thresholds
        ):
            raise ValueError("probability thresholds must be between zero and one")
        allowed_families = {
            "random_forest",
            "hist_gradient_boosting",
            "transformer",
        }
        unknown = set(self.search_families) - allowed_families
        if unknown:
            raise ValueError(f"unsupported search family: {sorted(unknown)}")
        return self


class BacktestConfig(StrictModel):
    fee_bps_per_leg: float = 10.0
    friction_bps_per_leg: float = 2.0
    stress_multiplier: float = 2.0
    threshold_margin_bps: list[int]
    probability_thresholds: list[float] = Field(default_factory=lambda: [0.50, 0.55, 0.60])
    max_holding_hours: int = 12
    minimum_calibration_trades: int = 20
    minimum_calibration_trades_per_asset: int = 60
    minimum_monthly_trades: int = 10
    minimum_average_monthly_trades: int = 20
    maximum_reference_monthly_trades: int = 40
    maximum_calibration_turnover_per_day: float = 2.0
    annualization_days: int = 365

    @property
    def cost_per_leg(self) -> float:
        return (self.fee_bps_per_leg + self.friction_bps_per_leg) / 10_000

    @property
    def round_trip_cost(self) -> float:
        return 2 * self.cost_per_leg


class LedgerConfig(StrictModel):
    name: str
    initial_cash: float


class PaperConfig(StrictModel):
    ledgers: list[LedgerConfig]
    max_asset_weight: float = 0.20
    max_gross_weight: float = 0.50
    rebalance_band: float = 0.02
    daily_loss_limit: float = 0.01
    position_loss_limit: float = 0.005
    drawdown_circuit_breaker: float = 0.08
    max_holding_hours: int = 12
    quote_depth_levels: int = 20
    canary_days: int = 14
    official_paper_days: int = 183

    @model_validator(mode="after")
    def validate_risk_limits(self) -> PaperConfig:
        if self.max_asset_weight > self.max_gross_weight:
            raise ValueError("max_asset_weight cannot exceed max_gross_weight")
        if not 0 < self.daily_loss_limit < self.drawdown_circuit_breaker < 1:
            raise ValueError("risk limits must satisfy daily < drawdown < 1")
        return self


class RuntimeConfig(StrictModel):
    database_url: str = "sqlite:///data/bottrade.db"
    log_level: str = "INFO"
    model_bucket: str = ""
    model_prefix: str = "registry"
    telegram_bot_token: str = ""
    telegram_chat_id: str = ""
    dashboard_password: str = ""
    clock_tolerance_seconds: int = 15


class GateConfig(StrictModel):
    min_sharpe: float = 1.0
    max_drawdown: float = 0.08
    min_profit_factor: float = 1.2
    min_closed_trades: int = 100
    require_positive_stress_return: bool = True
    incident_free_days: int = 90
    minimum_pre_holdout_folds: int = 12
    minimum_seed_passes: int = 4
    maximum_pbo: float = 0.20
    minimum_dsr_probability: float = 0.95


class AppConfig(StrictModel):
    project: ProjectConfig
    market: MarketConfig
    features: FeatureConfig
    training: TrainingConfig
    backtest: BacktestConfig
    paper: PaperConfig
    runtime: RuntimeConfig
    gates: GateConfig

    def ensure_directories(self) -> None:
        for path in (
            self.project.data_dir,
            self.project.artifact_dir,
            self.project.report_dir,
        ):
            path.mkdir(parents=True, exist_ok=True)


ENV_OVERRIDES: dict[str, tuple[str, str]] = {
    "BOTTRADE_DATABASE_URL": ("runtime", "database_url"),
    "BOTTRADE_TELEGRAM_BOT_TOKEN": ("runtime", "telegram_bot_token"),
    "BOTTRADE_TELEGRAM_CHAT_ID": ("runtime", "telegram_chat_id"),
    "BOTTRADE_DASHBOARD_PASSWORD": ("runtime", "dashboard_password"),
    "BOTTRADE_MODEL_BUCKET": ("runtime", "model_bucket"),
}


def _apply_env_overrides(raw: dict[str, Any]) -> dict[str, Any]:
    for env_name, (section, key) in ENV_OVERRIDES.items():
        value = os.getenv(env_name)
        if value is not None and value != "":
            raw.setdefault(section, {})[key] = value
    return raw


def load_config(path: str | Path | None = None, *, create_dirs: bool = True) -> AppConfig:
    config_path = Path(path or os.getenv("BOTTRADE_CONFIG", "config/default.yaml"))
    with config_path.open("r", encoding="utf-8") as handle:
        raw = yaml.safe_load(handle)
    config = AppConfig.model_validate(_apply_env_overrides(raw))
    if create_dirs:
        config.ensure_directories()
    return config
