from __future__ import annotations

import json

import pandas as pd
import pytest

from bottrade.dataset import DatasetBuilder
from bottrade.domain import Asset, DataArm


def test_dataset_build_refuses_market_gaps(app_config, market_frames, monkeypatch) -> None:
    builder = DatasetBuilder(app_config)
    market_frames["ETHUSDT"] = market_frames["ETHUSDT"].drop(index=100).reset_index(drop=True)
    monkeypatch.setattr(builder.pipeline, "load_market", lambda: market_frames)
    with pytest.raises(ValueError, match="dataset build aborted"):
        builder.build([Asset.BTCUSDT])


def test_processed_dataset_keeps_content_addressed_holdout_copy(
    app_config, market_frames, monkeypatch
) -> None:
    builder = DatasetBuilder(app_config)
    monkeypatch.setattr(builder.pipeline, "load_market", lambda: market_frames)
    monkeypatch.setattr(
        builder.pipeline,
        "load_alternatives",
        lambda: ({asset.value: pd.DataFrame() for asset in Asset}, pd.DataFrame()),
    )

    bundles = builder.build([Asset.BTCUSDT])
    market = next(item for item in bundles if item.arm == DataArm.MARKET)
    frozen = builder.load(
        Asset.BTCUSDT,
        DataArm.MARKET,
        data_version=market.data_version,
    )
    assert frozen.path.parent.name == market.data_version
    assert frozen.data_version == market.data_version

    latest = app_config.project.data_dir / "processed" / "BTCUSDT" / "market.parquet"
    changed = pd.read_parquet(latest)
    changed.loc[0, "reference_close"] = float(changed.loc[0, "reference_close"]) + 1.0
    changed.to_parquet(latest, index=False)
    with pytest.raises(ValueError, match="checksum mismatch"):
        builder.load(Asset.BTCUSDT, DataArm.MARKET)
    assert builder.load(
        Asset.BTCUSDT,
        DataArm.MARKET,
        data_version=market.data_version,
    ).data_version == market.data_version
    manifest = json.loads(
        (app_config.project.data_dir / "manifests" / "features-latest.json").read_text(
            encoding="utf-8"
        )
    )
    assert manifest["schema_version"] == "features-v3"
    assert manifest["sources"][0]["schema"]["as_of"].startswith("datetime64")
    with pytest.raises(ValueError, match="invalid processed dataset version"):
        builder.load(
            Asset.BTCUSDT,
            DataArm.MARKET,
            data_version="../../outside",
        )
