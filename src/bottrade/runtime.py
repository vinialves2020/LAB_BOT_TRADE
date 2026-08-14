from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import timedelta

import numpy as np
import pandas as pd

from bottrade.config import AppConfig
from bottrade.data.binance import validate_hourly_continuity
from bottrade.data.pipeline import DataPipeline
from bottrade.domain import Asset, DataArm, Forecast
from bottrade.features import FeatureBuilder, FeatureFrame
from bottrade.models.registry import ModelMetadata, ModelRegistry, OnnxPredictor
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
    def _alternative_is_stale(feature_frame: FeatureFrame, arm: DataArm) -> bool:
        latest = feature_frame.frame.iloc[-1]
        if (
            arm in {DataArm.MARKET_ONCHAIN, DataArm.MARKET_ALL}
            and float(latest.get("onchain_stale", 1.0)) >= 1.0
        ):
            return True
        return bool(
            arm in {DataArm.MARKET_SENTIMENT, DataArm.MARKET_ALL}
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
            featured = self.features.build(
                asset=asset,
                market=market,
                onchain=onchain.get(asset.value),
                sentiment=sentiment,
                arm=metadata.data_arm,
                include_labels=False,
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
            as_of = pd.Timestamp(latest["as_of"])
            if as_of.tzinfo is None:
                as_of = as_of.tz_localize("UTC")
            timestamps.append(as_of)
            volatilities[asset] = volatility
            forecasts[asset] = Forecast(
                asset=asset,
                as_of=as_of.to_pydatetime(),
                horizon_hours=metadata.horizon_hours,
                expected_return=expected_return,
                model_family=metadata.family,
                model_version=metadata.version,
                data_version=self._live_data_version(featured, metadata.feature_names),
                data_arm=metadata.data_arm,
                threshold_return=metadata.threshold_return,
                is_fallback=fallback,
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
