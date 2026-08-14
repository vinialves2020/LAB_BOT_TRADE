from __future__ import annotations

import json
import logging
from datetime import UTC, datetime, timedelta

import httpx
import pytest
import respx

from bottrade.alerts import TelegramAlerter
from bottrade.data.http import PublicHttpClient
from bottrade.domain import Asset, DataArm, Forecast, ModelFamily, RunStage
from bottrade.jobs import JobRunner
from bottrade.models.registry import ModelMetadata, ModelRegistry
from bottrade.paper import PaperTradingEngine
from bottrade.storage import Storage


def test_paper_engine_refuses_mutation_without_active_phase(app_config) -> None:
    storage = Storage(app_config.runtime.database_url)
    storage.initialize(app_config)
    engine = PaperTradingEngine(app_config, storage)
    with pytest.raises(RuntimeError, match="active canary or paper phase"):
        engine.signal_cycle(
            as_of=datetime.now(UTC),
            forecasts={},
            volatilities={},
            quotes={},
            rules={},
            enforce_clock=False,
        )
    assert storage.recent_orders() == []


def test_active_phase_rejects_forecast_for_cash_asset(app_config) -> None:
    storage = Storage(app_config.runtime.database_url)
    storage.initialize(app_config)
    storage.start_paper_phase(
        stage=RunStage.CANARY,
        started_at=datetime.now(UTC),
        duration_days=14,
        active_assets=[Asset.BTCUSDT],
    )
    forecast = Forecast(
        asset=Asset.ETHUSDT,
        as_of=datetime.now(UTC),
        horizon_hours=3,
        expected_return=0.01,
        model_family=ModelFamily.RANDOM_FOREST,
        model_version="eth-v1",
        data_version="d1",
        data_arm=DataArm.MARKET,
        threshold_return=0.0024,
    )
    with pytest.raises(RuntimeError, match="outside the frozen phase"):
        PaperTradingEngine(app_config, storage).signal_cycle(
            as_of=datetime.now(UTC),
            forecasts={Asset.ETHUSDT: forecast},
            volatilities={Asset.ETHUSDT: 0.01},
            quotes={},
            rules={},
            enforce_clock=False,
        )


def test_clock_divergence_stops_before_quote_or_rule_fetch(app_config, monkeypatch) -> None:
    runner = JobRunner(app_config)

    class DummyHttp:
        def __init__(self, *_args, **_kwargs) -> None:
            pass

        def __enter__(self):
            return self

        def __exit__(self, *_args) -> None:
            pass

    class ClockOnlyBinance:
        def __init__(self, *_args, **_kwargs) -> None:
            pass

        def server_time(self) -> datetime:
            return datetime.now(UTC) - timedelta(minutes=2)

        def market_quote(self, *_args, **_kwargs):
            raise AssertionError("quote must not be fetched after clock failure")

    monkeypatch.setattr("bottrade.jobs.PublicHttpClient", DummyHttp)
    monkeypatch.setattr("bottrade.jobs.BinanceClient", ClockOnlyBinance)
    with pytest.raises(RuntimeError, match="clock divergence"):
        runner._market_state()
    assert runner.storage.recent_orders() == []


@respx.mock
def test_binance_outage_exhausts_bounded_read_retries() -> None:
    url = "https://example.invalid/api/v3/time"
    route = respx.get(url).mock(return_value=httpx.Response(503))
    with (
        PublicHttpClient(timeout_seconds=1, max_retries=0) as client,
        pytest.raises(httpx.HTTPStatusError),
    ):
        client.get(url)
    assert route.call_count == 1


def test_telegram_failure_redacts_bot_token(monkeypatch, caplog) -> None:
    token = "123456:super-secret-token"

    class BrokenClient:
        def __init__(self, *_args, **_kwargs) -> None:
            pass

        def __enter__(self):
            return self

        def __exit__(self, *_args) -> None:
            pass

        def post(self, url: str, **_kwargs):
            request = httpx.Request("POST", url)
            raise httpx.ConnectError("offline", request=request)

    monkeypatch.setattr("bottrade.alerts.httpx.Client", BrokenClient)
    with caplog.at_level(logging.ERROR):
        assert TelegramAlerter(token, "1").send("test") is False
    assert token not in caplog.text
    assert "request details redacted" in caplog.text


def test_telegram_exception_alert_does_not_forward_arbitrary_error_text(
    monkeypatch,
) -> None:
    alerter = TelegramAlerter("token", "chat")
    delivered: list[str] = []
    monkeypatch.setattr(alerter, "send", lambda message: delivered.append(message) or True)
    assert alerter.exception("signal", RuntimeError("password=must-not-leak")) is True
    assert "must-not-leak" not in delivered[0]
    assert "RuntimeError" in delivered[0]


def test_corrupted_model_bundle_is_rejected_before_inference(app_config) -> None:
    registry = ModelRegistry(app_config)
    version = "btc-corrupt-v1"
    directory = registry.root / Asset.BTCUSDT.value / "versions" / version
    directory.mkdir(parents=True)
    model_bytes = b"not-an-onnx-model"
    (directory / "model.onnx").write_bytes(model_bytes)
    metadata = ModelMetadata(
        version=version,
        asset=Asset.BTCUSDT,
        family=ModelFamily.RANDOM_FOREST,
        data_arm=DataArm.MARKET,
        trained_at=datetime.now(UTC),
        training_end=datetime.now(UTC),
        horizon_hours=3,
        sequence_length=1,
        feature_names=["x"],
        feature_schema_version="features-v2",
        data_version="d1",
        threshold_return=0.0024,
        seed=11,
        parameters={},
        onnx_verified=True,
        onnx_max_abs_error=0.0,
        artifact_sha256="0" * 64,
    )
    (directory / "metadata.json").write_text(
        json.dumps(metadata.model_dump(mode="json")),
        encoding="utf-8",
    )
    pointer = registry.root / Asset.BTCUSDT.value / "champion.json"
    pointer.write_text(json.dumps({"version": version}), encoding="utf-8")
    with pytest.raises(ValueError, match="checksum mismatch"):
        registry.resolve(Asset.BTCUSDT, "champion")
