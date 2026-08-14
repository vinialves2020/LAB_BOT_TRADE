from __future__ import annotations

import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd

from bottrade.config import AppConfig
from bottrade.data.binance import validate_hourly_continuity
from bottrade.data.manifest import DatasetManifest, read_manifest
from bottrade.data.pipeline import DataPipeline
from bottrade.domain import Asset, DataArm
from bottrade.features import FEATURE_SCHEMA_VERSION, FeatureBuilder
from bottrade.utils import content_hash, sha256_file


@dataclass(frozen=True, slots=True)
class DatasetBundle:
    asset: Asset
    arm: DataArm
    frame: pd.DataFrame
    feature_columns: tuple[str, ...]
    data_version: str
    schema_version: str
    path: Path


class DatasetBuilder:
    def __init__(self, config: AppConfig) -> None:
        self.config = config
        self.pipeline = DataPipeline(config)
        self.feature_builder = FeatureBuilder(config.features)
        self.output_dir = config.project.data_dir / "processed"
        self.manifest_dir = config.project.data_dir / "manifests"

    def _continuous_market_history(
        self, market: dict[str, pd.DataFrame]
    ) -> tuple[dict[str, pd.DataFrame], dict[str, Any]]:
        if not market:
            raise ValueError("market history is empty")
        starts = {
            symbol: pd.to_datetime(frame["open_time"], utc=True).min()
            for symbol, frame in market.items()
        }
        ends = {
            symbol: pd.to_datetime(frame["open_time"], utc=True).max()
            for symbol, frame in market.items()
        }
        common_start = max(starts.values())
        common_end = min(ends.values())
        if common_start > common_end:
            raise ValueError("market histories have no common time range")

        gaps_by_symbol: dict[str, list[pd.Timestamp]] = {}
        all_gaps: set[pd.Timestamp] = set()
        for symbol, frame in market.items():
            common = frame.loc[
                (pd.to_datetime(frame["open_time"], utc=True) >= common_start)
                & (pd.to_datetime(frame["open_time"], utc=True) <= common_end)
            ]
            gaps = validate_hourly_continuity(common)
            gaps_by_symbol[symbol] = gaps
            all_gaps.update(gaps)

        continuous_start = max(all_gaps) + pd.Timedelta(hours=1) if all_gaps else common_start
        trimmed: dict[str, pd.DataFrame] = {}
        for symbol, frame in market.items():
            times = pd.to_datetime(frame["open_time"], utc=True)
            continuous = frame.loc[(times >= continuous_start) & (times <= common_end)].reset_index(
                drop=True
            )
            remaining = validate_hourly_continuity(continuous)
            if remaining:
                preview = ", ".join(str(value) for value in remaining[:5])
                raise ValueError(
                    f"market history for {symbol} is not continuous after trimming ({preview})"
                )
            trimmed[symbol] = continuous

        metadata = {
            "historical_gap_policy": self.config.features.historical_gap_policy,
            "common_market_start": common_start.isoformat(),
            "common_market_end": common_end.isoformat(),
            "continuous_market_start": continuous_start.isoformat(),
            "excluded_gap_count": len(all_gaps),
            "excluded_gaps": [value.isoformat() for value in sorted(all_gaps)],
            "gaps_by_symbol": {
                symbol: [value.isoformat() for value in values]
                for symbol, values in gaps_by_symbol.items()
            },
        }
        return trimmed, metadata

    def build(self, assets: list[Asset] | None = None) -> list[DatasetBundle]:
        selected_assets = assets or list(Asset)
        market, history_metadata = self._continuous_market_history(self.pipeline.load_market())
        onchain, sentiment = self.pipeline.load_alternatives()
        raw_manifest_path = self.manifest_dir / "latest.json"
        raw_manifest = read_manifest(raw_manifest_path) if raw_manifest_path.exists() else {}
        bundles: list[DatasetBundle] = []
        output_manifest = DatasetManifest(
            dataset="bottrade-feature-datasets",
            schema_version=FEATURE_SCHEMA_VERSION,
            metadata={
                "raw_data_version": raw_manifest.get("data_version", "unknown"),
                **history_metadata,
            },
        )
        for asset in selected_assets:
            for arm_name in self.config.features.arms:
                arm = DataArm(arm_name)
                featured = self.feature_builder.build(
                    asset=asset,
                    market=market,
                    onchain=onchain.get(asset.value),
                    sentiment=sentiment,
                    arm=arm,
                    include_labels=True,
                )
                directory = self.output_dir / asset.value
                directory.mkdir(parents=True, exist_ok=True)
                path = directory / f"{arm.value}.parquet"
                featured.frame.to_parquet(path, index=False)
                schema_core = {
                    "schema_version": featured.schema_version,
                    "asset": asset.value,
                    "arm": arm.value,
                    "feature_columns": list(featured.feature_columns),
                    "dtypes": {
                        column: str(featured.frame[column].dtype) for column in featured.frame
                    },
                    "market_history": history_metadata,
                }
                parquet_sha256 = sha256_file(path)
                data_version = content_hash(
                    [
                        raw_manifest.get("data_version", "unknown"),
                        schema_core,
                        parquet_sha256,
                    ]
                )[:20]
                schema = {
                    **schema_core,
                    "data_version": data_version,
                    "parquet_sha256": parquet_sha256,
                    "raw_data_version": raw_manifest.get("data_version", "unknown"),
                }
                schema_path = directory / f"{arm.value}.schema.json"
                schema_path.write_text(
                    json.dumps(schema, indent=2, sort_keys=True), encoding="utf-8"
                )
                version_directory = directory / "versions" / data_version
                version_directory.mkdir(parents=True, exist_ok=True)
                versioned_path = version_directory / f"{arm.value}.parquet"
                versioned_schema_path = version_directory / f"{arm.value}.schema.json"
                if not versioned_path.exists():
                    shutil.copy2(path, versioned_path)
                if sha256_file(versioned_path) != parquet_sha256:
                    raise ValueError(f"immutable dataset collision for {asset.value}/{arm.value}")
                versioned_schema_path.write_text(
                    json.dumps(schema, indent=2, sort_keys=True), encoding="utf-8"
                )
                output_manifest.add_file(
                    source=f"features_{asset.value}_{arm.value}",
                    url="local-feature-pipeline",
                    path=versioned_path,
                    rows=len(featured.frame),
                    min_event_time=featured.frame["as_of"].min().isoformat(),
                    max_event_time=featured.frame["as_of"].max().isoformat(),
                    schema={column: str(dtype) for column, dtype in featured.frame.dtypes.items()},
                )
                bundles.append(
                    DatasetBundle(
                        asset=asset,
                        arm=arm,
                        frame=featured.frame,
                        feature_columns=featured.feature_columns,
                        data_version=data_version,
                        schema_version=featured.schema_version,
                        path=versioned_path,
                    )
                )
        output_manifest.write(self.manifest_dir / "features-latest.json")
        return bundles

    def load(
        self,
        asset: Asset,
        arm: DataArm,
        *,
        data_version: str | None = None,
    ) -> DatasetBundle:
        directory = self.output_dir / asset.value
        if data_version:
            if re.fullmatch(r"[0-9a-f]{20}", data_version) is None:
                raise ValueError(f"invalid processed dataset version: {data_version!r}")
            directory = directory / "versions" / data_version
        path = directory / f"{arm.value}.parquet"
        schema_path = directory / f"{arm.value}.schema.json"
        if not path.exists() or not schema_path.exists():
            raise FileNotFoundError(
                f"processed dataset missing for {asset}/{arm}; run 'bottrade dataset build'"
            )
        schema: dict[str, Any] = json.loads(schema_path.read_text(encoding="utf-8"))
        actual_sha256 = sha256_file(path)
        if actual_sha256 != schema.get("parquet_sha256"):
            raise ValueError(f"processed dataset checksum mismatch: {path}")
        stored_version = str(schema.get("data_version", ""))
        schema_core = {
            key: schema[key]
            for key in (
                "schema_version",
                "asset",
                "arm",
                "feature_columns",
                "dtypes",
                "market_history",
            )
        }
        expected_version = content_hash(
            [schema.get("raw_data_version", "unknown"), schema_core, actual_sha256]
        )[:20]
        if (
            not stored_version
            or stored_version != expected_version
            or (data_version and stored_version != data_version)
        ):
            raise ValueError(f"processed dataset version mismatch: {path}")
        frame = pd.read_parquet(path)
        frame["as_of"] = pd.to_datetime(frame["as_of"], utc=True)
        if schema.get("asset") != asset.value or schema.get("arm") != arm.value:
            raise ValueError(f"processed dataset identity mismatch: {path}")
        missing_features = set(schema["feature_columns"]) - set(frame.columns)
        if missing_features:
            raise ValueError(
                f"processed dataset schema columns are missing: {sorted(missing_features)}"
            )
        return DatasetBundle(
            asset=asset,
            arm=arm,
            frame=frame,
            feature_columns=tuple(schema["feature_columns"]),
            data_version=stored_version,
            schema_version=schema["schema_version"],
            path=path,
        )
