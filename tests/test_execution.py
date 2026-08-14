from __future__ import annotations

from datetime import UTC, datetime
from decimal import Decimal

import pytest

from bottrade.domain import (
    Asset,
    ExchangeRules,
    MarketQuote,
    PositionSnapshot,
    TargetPosition,
)
from bottrade.execution import InsufficientDepthError, PaperExecutionSimulator


def test_target_order_rounds_down_and_book_fill_records_impact() -> None:
    now = datetime.now(UTC)
    simulator = PaperExecutionSimulator(10)
    rules = ExchangeRules(
        symbol="BTCUSDT",
        min_quantity=Decimal("0.00001"),
        max_quantity=Decimal("100"),
        step_size=Decimal("0.00001"),
        tick_size=Decimal("0.01"),
        min_notional=Decimal("5"),
    )
    quote = MarketQuote(
        asset=Asset.BTCUSDT,
        as_of=now,
        bid=Decimal("9990"),
        ask=Decimal("10000"),
        bid_quantity=Decimal("1"),
        ask_quantity=Decimal("0.005"),
        bids=((Decimal("9990"), Decimal("1")),),
        asks=((Decimal("10000"), Decimal("0.005")), (Decimal("10010"), Decimal("1"))),
    )
    position = PositionSnapshot(
        ledger="paper_500",
        asset=Asset.BTCUSDT,
        as_of=now,
        quantity=Decimal("0"),
        average_price=Decimal("0"),
        market_price=Decimal("0"),
        market_value=Decimal("0"),
        unrealized_pnl=Decimal("0"),
        weight=0,
    )
    target = TargetPosition(Asset.BTCUSDT, now, 0.20, "test")
    order = simulator.target_order(
        ledger="paper_500",
        target=target,
        position=position,
        equity=Decimal("500"),
        quote=quote,
        rules=rules,
    )
    assert order is not None
    assert order.quantity == Decimal("0.01000")
    fill = simulator.fill(order, quote)
    assert fill.price == Decimal("10005")
    assert fill.impact_bps == pytest.approx(5.0)
    assert fill.fee == Decimal("0.10005000")


def test_empty_visible_book_is_never_filled_at_ticker_price() -> None:
    simulator = PaperExecutionSimulator(10)
    now = datetime.now(UTC)
    quote = MarketQuote(
        asset=Asset.BTCUSDT,
        as_of=now,
        bid=Decimal("9990"),
        ask=Decimal("10000"),
        bid_quantity=Decimal("0"),
        ask_quantity=Decimal("0"),
    )
    order = simulator.target_order(
        ledger="paper_500",
        target=TargetPosition(Asset.BTCUSDT, now, 0.20, "test"),
        position=PositionSnapshot(
            ledger="paper_500",
            asset=Asset.BTCUSDT,
            as_of=now,
            quantity=Decimal("0"),
            average_price=Decimal("0"),
            market_price=Decimal("0"),
            market_value=Decimal("0"),
            unrealized_pnl=Decimal("0"),
            weight=0,
        ),
        equity=Decimal("500"),
        quote=quote,
        rules=ExchangeRules(
            symbol="BTCUSDT",
            min_quantity=Decimal("0.00001"),
            max_quantity=Decimal("100"),
            step_size=Decimal("0.00001"),
            tick_size=Decimal("0.01"),
            min_notional=Decimal("5"),
        ),
    )
    assert order is not None
    with pytest.raises(InsufficientDepthError, match="no executable levels"):
        simulator.fill(order, quote)
