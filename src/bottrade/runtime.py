from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import timedelta

import numpy as np
import pandas as pd

from bottrade.config import AppConfig
from bottrade.data.binance import validate_hourly_continuity
from bottrade.data.pipeline import DataPipeline
from bottrade.domain import Asset, DataArm, DataArmSpec, Forecast
from bottrade.features import FeatureBuilder, FeatureFrame
from bottrade.models.registry import ModelMetadata, ModelRegistry, OnnxPredictor
from bottrade.multihorizon import select_horizon_forecast
from bottrade.utils import sha256_bytes, utc_now

LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class RuntimeSignalBatch:
    forecasts: dict[Asset, Forecast]
    shadow_forecasts: dict[Asset, Forecast]
    volatilities: dict[Asset, float]
    as_of: pd.Timestamp


class RuntimeInferenceService:
    def __init__(self, config: AppConfig) -> None:
        self.config = config
        self.pipeline = DataPipeline(config)
        self.features = FeatureBuilder(config.features)
        self.registry = ModelRegistry(config)

    def _active_bundle(self, asset: Asset, slot: str) -> tuple[ModelMetadata, OnnxPredictor]:
        self.registry.hydrate_active(asset, slot)
        directory, metadata = self.registry.resolve(asset, slot)
        return metadata, OnnxPredictor(directory, metadata)

    @staticmethod
    def _alternative_is_stale(
        feature_frame: FeatureFrame, arm: DataArm | DataArmSpec | str
    ) -> bool:
        spec = DataArmSpec.from_id(arm)
        latest = feature_frame.frame.iloc[-1]
        if spec.include_intrahour:
            completeness = [
                column
                for column in feature_frame.frame.columns
                if column.endswith("_intrahour_complete")
            ]
            if completeness and any(float(latest.get(column, 0.0)) < 1.0 for column in completeness):
                return True
        if (
            spec.include_onchain
            and float(latest.get("onchain_stale", 1.0)) >= 1.0
        ):
            return True
        if (
            spec.include_derivatives
            and float(latest.get("derivatives_stale", 1.0)) >= 1.0
        ):
            return True
        return bool(
            spec.include_sentiment
            and float(latest.get("sentiment_stale", 1.0)) >= 1.0
        )

    @staticmethod
    def _live_data_version(feature_frame: FeatureFrame, feature_names: list[str]) -> str:
        sample = feature_frame.frame[["as_of", *feature_names]].tail(168)
        hashes = pd.util.hash_pandas_object(sample, index=False).to_numpy(dtype=np.uint64)
        return sha256_bytes(hashes.tobytes())[:20]

    def generate(self, *, active_assets: set[Asset] | None = None) -> RuntimeSignalBatch:
        enabled = set(Asset) if active_assets is None else set(active_assets)
        raw_limit = max(500, self.config.features.lookback_hours * 3)
        market = self.pipeline.recent_market(limit=raw_limit)
        intrahour: dict[str, pd.DataFrame] = {}
        derivatives: dict[str, pd.DataFrame] = {}
        market_timestamps: list[pd.Timestamp] = []
        for symbol, frame in market.items():
            required_history = (
                self.config.features.lookback_hours
                + max(self.config.features.lag_hours, default=0)
            )
            closed = frame[frame["is_closed"].astype(bool)].tail(
                required_history
            )
            if len(closed) < required_history:
                raise ValueError(
                    f"{symbol} has only {len(closed)} closed candles; "
                    f"{required_history} are required"
                )
            missing = validate_hourly_continuity(closed)
            if missing:
                raise ValueError(
                    f"{symbol} has {len(missing)} missing market candle(s); refusing new positions"
                )
            market_timestamps.append(pd.Timestamp(closed.iloc[-1]["as_of"]))
        if not market_timestamps or len(set(market_timestamps)) != 1:
            raise ValueError(
                f"assets are not aligned on one closed candle: {market_timestamps}"
            )
        market_as_of = market_timestamps[0]
        if market_as_of.tzinfo is None:
            market_as_of = market_as_of.tz_localize("UTC")
        now = utc_now()
        alternatives_start = now - timedelta(days=120)
        try:
            onchain, sentiment = self.pipeline.recent_alternatives(alternatives_start, now)
        except Exception as exc:
            LOGGER.warning("Alternative sources unavailable; forcing market-only fallback: %s", exc)
            onchain = {asset.value: pd.DataFrame() for asset in Asset}
            sentiment = pd.DataFrame()
        forecasts: dict[Asset, Forecast] = {}
        shadow_forecasts: dict[Asset, Forecast] = {}
        volatilities: dict[Asset, float] = {}
        timestamps: list[pd.Timestamp] = []
        for asset in Asset:
            if asset not in enabled:
                continue
            try:
                metadata, predictor = self._active_bundle(asset, "champion")
            except FileNotFoundError:
                LOGGER.warning("No active champion for %s; asset remains cash", asset.value)
                continue
            arm_spec = DataArmSpec.from_id(metadata.data_arm)
            if arm_spec.include_intrahour and not intrahour:
                try:
                    intrahour = self.pipeline.recent_intrahour(limit=4 * raw_limit)
                except (AttributeError, OSError, RuntimeError, ValueError) as exc:
                    LOGGER.warning("15m source unavailable; V2 arm will fail closed: %s", exc)
                    intrahour = {symbol: pd.DataFrame() for symbol in self.config.market.symbols}
            if arm_spec.include_derivatives and not derivatives:
                try:
                    derivatives = self.pipeline.load_derivatives()
                except (AttributeError, OSError, RuntimeError, ValueError) as exc:
                    LOGGER.warning("derivative archive unavailable; V2 arm will fail closed: %s", exc)
                    derivatives = {symbol: pd.DataFrame() for symbol in self.config.market.symbols}
            featured = self.features.build(
                asset=asset,
                market=market,
                onchain=onchain.get(asset.value),
                sentiment=sentiment,
                arm=metadata.data_arm,
                include_labels=False,
                intrahour=intrahour,
                derivatives=derivatives,
            )
            fallback = False
            if self._alternative_is_stale(featured, metadata.data_arm):
                metadata, predictor = self._active_bundle(asset, "market_fallback")
                featured = self.features.build(
                    asset=asset,
                    market=market,
                    arm=DataArm.MARKET,
                    include_labels=False,
                )
                fallback = True
            if featured.schema_version != metadata.feature_schema_version:
                raise ValueError(
                    f"feature schema mismatch for {asset.value}: "
                    f"{featured.schema_version} != {metadata.feature_schema_version}"
                )
            missing_features = set(metadata.feature_names) - set(featured.frame.columns)
            if missing_features:
                raise ValueError(
                    f"runtime features missing for {asset.value}: {sorted(missing_features)}"
                )
            values = featured.frame.loc[:, metadata.feature_names].to_numpy(dtype=float)
            normalized_prediction = predictor.predict_latest(values)
            if not np.isfinite(normalized_prediction):
                raise ValueError(f"non-finite model prediction for {asset.value}")
            latest = featured.frame.iloc[-1]
            volatility = float(latest["target_volatility"])
            if not np.isfinite(volatility) or volatility <= 0:
                raise ValueError(f"invalid live volatility for {asset.value}")
            expected_return = normalized_prediction * volatility
            horizon_forecasts = ()
            selected_horizon = None
            if predictor.horizon_sessions:
                horizon_forecasts = predictor.predict_horizons(
                    values,
                    volatility=volatility,
                    round_trip_cost=self.config.backtest.round_trip_cost,
                    probability_threshold=metadata.probability_threshold,
                    margin_bps=metadata.cost_margin_bps,
                )
                selected_horizon = select_horizon_forecast(
                    horizons=(item.horizon_hours for item in horizon_forecasts),
                    expected_gross_returns=(
                        item.expected_gross_return for item in horizon_forecasts
                    ),
                    probabilities=(
                        item.probability_net_positive for item in horizon_forecasts
                    ),
                    round_trip_cost=self.config.backtest.round_trip_cost,
                    probability_threshold=metadata.probability_threshold,
                    margin_bps=metadata.cost_margin_bps,
                )
                expected_return = (
                    selected_horizon.expected_gross_return if selected_horizon else 0.0
                )
            as_of = pd.Timestamp(latest["as_of"])
            if as_of.tzinfo is None:
                as_of = as_of.tz_localize("UTC")
            timestamps.append(as_of)
            volatilities[asset] = volatility
            forecasts[asset] = Forecast(
                asset=asset,
                as_of=as_of.to_pydatetime(),
                horizon_hours=(
                    selected_horizon.horizon_hours
                    if selected_horizon is not None
                    else metadata.horizon_hours
                ),
                expected_return=expected_return,
                model_family=metadata.family,
                model_version=metadata.version,
                data_version=self._live_data_version(featured, metadata.feature_names),
                data_arm=metadata.data_arm,
                threshold_return=metadata.threshold_return,
                is_fallback=fallback,
                horizons=tuple(horizon_forecasts),
                selected_horizon_hours=(
                    selected_horizon.horizon_hours if selected_horizon is not None else None
                ),
                policy_version=metadata.policy_version,
                ensemble_id=metadata.ensemble_id or None,
            )
            try:
                shadow_metadata, shadow_predictor = self._active_bundle(asset, "challenger")
                shadow_featured = self.features.build(
                    asset=asset,
                    market=market,
                    onchain=onchain.get(asset.value),
                    sentiment=sentiment,
                    arm=shadow_metadata.data_arm,
                    include_labels=False,
                    intrahour=intrahour,
                    derivatives=derivatives,
                )
                if self._alternative_is_stale(shadow_featured, shadow_metadata.data_arm):
                    raise ValueError("challenger alternative data is stale")
                if shadow_featured.schema_version != shadow_metadata.feature_schema_version:
                    raise ValueError("challenger feature schema mismatch")
                shadow_values = shadow_featured.frame.loc[
                    :, shadow_metadata.feature_names
                ].to_numpy(dtype=float)
                shadow_latest = shadow_featured.frame.iloc[-1]
                shadow_as_of = pd.Timestamp(shadow_latest["as_of"])
                if shadow_as_of.tzinfo is None:
                    shadow_as_of = shadow_as_of.tz_localize("UTC")
                if shadow_as_of != as_of:
                    raise ValueError("challenger candle is not aligned with champion")
                shadow_volatility = float(shadow_latest["target_volatility"])
                if not np.isfinite(shadow_volatility) or shadow_volatility <= 0:
                    raise ValueError("challenger volatility is invalid")
                shadow_prediction = shadow_predictor.predict_latest(shadow_values)
                if not np.isfinite(shadow_prediction):
                    raise ValueError("challenger prediction is non-finite")
                shadow_forecasts[asset] = Forecast(
                    asset=asset,
                    as_of=as_of.to_pydatetime(),
                    horizon_hours=shadow_metadata.horizon_hours,
                    expected_return=(
                        shadow_prediction * shadow_volatility
                    ),
                    model_family=shadow_metadata.family,
                    model_version=shadow_metadata.version,
                    data_version=self._live_data_version(
                        shadow_featured, shadow_metadata.feature_names
                    ),
                    data_arm=shadow_metadata.data_arm,
                    threshold_return=shadow_metadata.threshold_return,
                    is_shadow=True,
                )
            except (FileNotFoundError, KeyError, RuntimeError, ValueError) as exc:
                LOGGER.warning("Challenger shadow unavailable for %s: %s", asset.value, exc)
        if timestamps and (
            len(set(timestamps)) != 1 or timestamps[0] != market_as_of
        ):
            raise ValueError(
                f"model forecasts are not aligned with market candle {market_as_of}: {timestamps}"
            )
        latest_as_of = market_as_of
        age_minutes = (pd.Timestamp(now) - latest_as_of).total_seconds() / 60
        if age_minutes > self.config.features.market_stale_minutes:
            raise ValueError(f"latest closed market candle is stale by {age_minutes:.1f} minutes")
        return RuntimeSignalBatch(
            forecasts=forecasts,
            shadow_forecasts=shadow_forecasts,
            volatilities=volatilities,
            as_of=latest_as_of,
        )
