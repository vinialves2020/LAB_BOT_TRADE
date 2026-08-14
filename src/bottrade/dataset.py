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

    def build(self, assets: list[Asset] | None = None) -> list[DatasetBundle]:
        selected_assets = assets or list(Asset)
        market = self.pipeline.load_market()
        for symbol, frame in market.items():
            missing = validate_hourly_continuity(frame)
            if missing:
                preview = ", ".join(str(value) for value in missing[:5])
                raise ValueError(
                    f"market history for {symbol} has {len(missing)} gap(s); "
                    f"dataset build aborted ({preview})"
                )
        onchain, sentiment = self.pipeline.load_alternatives()
        raw_manifest_path = self.manifest_dir / "latest.json"
        raw_manifest = read_manifest(raw_manifest_path) if raw_manifest_path.exists() else {}
        bundles: list[DatasetBundle] = []
        output_manifest = DatasetManifest(
            dataset="bottrade-feature-datasets",
            schema_version=FEATURE_SCHEMA_VERSION,
            metadata={"raw_data_version": raw_manifest.get("data_version", "unknown")},
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
                    "dtypes": {column: str(featured.frame[column].dtype) for column in featured.frame},
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
                    schema={
                        column: str(dtype)
                        for column, dtype in featured.frame.dtypes.items()
                    },
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
            for key in ("schema_version", "asset", "arm", "feature_columns", "dtypes")
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
