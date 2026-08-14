from __future__ import annotations

from datetime import UTC, datetime, timedelta
from decimal import Decimal

import pytest

from bottrade.domain import (
    Asset,
    DataArm,
    ExchangeRules,
    Forecast,
    MarketQuote,
    ModelFamily,
)
from bottrade.paper import PaperTradingEngine
from bottrade.storage import PositionRow, Storage


def _rules(asset: Asset) -> ExchangeRules:
    return ExchangeRules(
        symbol=asset.value,
        min_quantity=Decimal("0.00001"),
        max_quantity=Decimal("100000"),
        step_size=Decimal("0.00001"),
        tick_size=Decimal("0.00001"),
        min_notional=Decimal("5"),
    )


def _quote(asset: Asset, price: str, now: datetime) -> MarketQuote:
    mid = Decimal(price)
    bid = mid * Decimal("0.9999")
    ask = mid * Decimal("1.0001")
    return MarketQuote(
        asset=asset,
        as_of=now,
        bid=bid,
        ask=ask,
        bid_quantity=Decimal("10000"),
        ask_quantity=Decimal("10000"),
        bids=((bid, Decimal("10000")),),
        asks=((ask, Decimal("10000")),),
    )


def test_signal_cycle_is_idempotent_and_reconciles(app_config) -> None:
    storage = Storage(app_config.runtime.database_url)
    storage.initialize(app_config)
    engine = PaperTradingEngine(app_config, storage)
    now = datetime.now(UTC).replace(microsecond=0)
    forecasts = {
        asset: Forecast(
            asset=asset,
            as_of=now,
            horizon_hours=3,
            expected_return=0.02,
            model_family=ModelFamily.RANDOM_FOREST,
            model_version=f"{asset.value}-v1",
            data_version="d1",
            data_arm=DataArm.MARKET,
            threshold_return=0.0024,
        )
        for asset in Asset
    }
    quotes = {
        Asset.BTCUSDT: _quote(Asset.BTCUSDT, "10000", now),
        Asset.ETHUSDT: _quote(Asset.ETHUSDT, "1000", now),
        Asset.SOLUSDT: _quote(Asset.SOLUSDT, "100", now),
    }
    shadow = {
        asset: Forecast(
            asset=asset,
            as_of=now,
            horizon_hours=3,
            expected_return=0.01,
            model_family=ModelFamily.TRANSFORMER,
            model_version=f"{asset.value}-shadow-v1",
            data_version="d1",
            data_arm=DataArm.MARKET,
            threshold_return=0.0024,
            is_shadow=True,
        )
        for asset in Asset
    }
    rules = {asset: _rules(asset) for asset in Asset}
    result = engine.signal_cycle(
        as_of=now,
        forecasts=forecasts,
        shadow_forecasts=shadow,
        volatilities={asset: 0.01 for asset in Asset},
        quotes=quotes,
        rules=rules,
        enforce_clock=False,
        enforce_phase=False,
    )
    duplicate = engine.signal_cycle(
        as_of=now,
        forecasts=forecasts,
        volatilities={asset: 0.01 for asset in Asset},
        quotes=quotes,
        rules=rules,
        enforce_clock=False,
        enforce_phase=False,
    )
    assert result["orders"] == 6
    assert duplicate == {"status": "duplicate", "orders": 0}
    assert len(storage.recent_orders()) == 6
    assert sum(item["is_shadow"] for item in storage.recent_forecasts()) == 3
    assert storage.reconcile(app_config)["ok"] is True
    for ledger in storage.ledger_names():
        snapshot = storage.equity_snapshot(
            ledger, now, {asset: quote.mid for asset, quote in quotes.items()}
        )
        assert snapshot.cash + snapshot.positions_value == snapshot.equity
        assert sum(position.weight for position in storage.positions(ledger, now)) <= 0.501
    with storage.session() as session:
        position = session.get(PositionRow, ("paper_500", Asset.BTCUSDT.value))
        assert position is not None
        position.average_price += Decimal("1")
    corrupted = storage.reconcile(app_config)
    assert corrupted["ok"] is False
    assert any(
        value.startswith("average_price_mismatch:paper_500:BTCUSDT")
        for value in corrupted["violations"]
    )


def test_reset_preserves_ledgers_and_clears_positions(app_config) -> None:
    storage = Storage(app_config.runtime.database_url)
    storage.initialize(app_config)
    storage.reset_paper_state(app_config)
    assert storage.ledger_names() == ["paper_1000", "paper_500"]
    assert all(
        position.quantity == 0
        for ledger in storage.ledger_names()
        for position in storage.positions(ledger)
    )


def test_daily_report_is_idempotently_persisted(app_config) -> None:
    storage = Storage(app_config.runtime.database_url)
    storage.initialize(app_config)
    now = datetime.now(UTC).replace(microsecond=0)
    storage.record_daily_report(as_of=now, summary="first", report_markdown="# first")
    storage.record_daily_report(as_of=now, summary="second", report_markdown="# second")
    reports = storage.recent_daily_reports()
    assert len(reports) == 1
    assert reports[0]["summary"] == "second"
    assert len(reports[0]["sha256"]) == 64


def test_operation_lock_serializes_signal_and_risk_mutations(app_config) -> None:
    storage = Storage(app_config.runtime.database_url)
    storage.initialize(app_config)
    with (
        storage.operation_lock(),
        pytest.raises(RuntimeError, match="operation lock"),
        storage.operation_lock(),
    ):
        pass
    with storage.operation_lock():
        pass


def test_abandoned_cycle_can_be_reclaimed_after_runtime_timeout(
    app_config, monkeypatch
) -> None:
    storage = Storage(app_config.runtime.database_url)
    storage.initialize(app_config)
    started = datetime.now(UTC).replace(microsecond=0)
    monkeypatch.setattr("bottrade.storage.utc_now", lambda: started)
    assert storage.claim_cycle("signal", "2026-08-14T12:00:00+00:00") is True
    assert storage.claim_cycle("signal", "2026-08-14T12:00:00+00:00") is False
    monkeypatch.setattr(
        "bottrade.storage.utc_now", lambda: started + timedelta(minutes=16)
    )
    assert storage.claim_cycle("signal", "2026-08-14T12:00:00+00:00") is True


def test_failed_fill_batch_rolls_back_every_buy(app_config, monkeypatch) -> None:
    storage = Storage(app_config.runtime.database_url)
    storage.initialize(app_config)
    engine = PaperTradingEngine(app_config, storage)
    now = datetime.now(UTC).replace(microsecond=0)
    forecasts = {
        asset: Forecast(
            asset=asset,
            as_of=now,
            horizon_hours=3,
            expected_return=0.02,
            model_family=ModelFamily.RANDOM_FOREST,
            model_version=f"{asset.value}-v1",
            data_version="d1",
            data_arm=DataArm.MARKET,
            threshold_return=0.0024,
        )
        for asset in Asset
    }
    quotes = {
        Asset.BTCUSDT: _quote(Asset.BTCUSDT, "10000", now),
        Asset.ETHUSDT: _quote(Asset.ETHUSDT, "1000", now),
        Asset.SOLUSDT: _quote(Asset.SOLUSDT, "100", now),
    }
    original = Storage._apply_order_fill_in_session
    calls = 0

    def injected_failure(session, order, fill) -> None:
        nonlocal calls
        calls += 1
        if calls == 2:
            raise RuntimeError("injected database failure")
        original(session, order, fill)

    monkeypatch.setattr(
        Storage, "_apply_order_fill_in_session", staticmethod(injected_failure)
    )
    with pytest.raises(RuntimeError, match="injected"):
        engine.signal_cycle(
            as_of=now,
            forecasts=forecasts,
            volatilities={asset: 0.01 for asset in Asset},
            quotes=quotes,
            rules={asset: _rules(asset) for asset in Asset},
            enforce_clock=False,
            enforce_phase=False,
        )
    assert storage.recent_orders() == []
    assert storage.reconcile(app_config)["ok"] is True
    assert all(
        position.quantity == 0
        for ledger in storage.ledger_names()
        for position in storage.positions(ledger)
    )
