from __future__ import annotations

from decimal import Decimal

from bottrade.domain import (
    ExchangeRules,
    MarketQuote,
    PaperFill,
    PaperOrder,
    PositionSnapshot,
    TargetPosition,
)
from bottrade.utils import deterministic_id, floor_to_step


class InsufficientDepthError(RuntimeError):
    pass


class PaperExecutionSimulator:
    def __init__(self, fee_bps_per_leg: float = 10.0) -> None:
        self.fee_rate = Decimal(str(fee_bps_per_leg)) / Decimal("10000")

    @staticmethod
    def _book_fill(
        levels: tuple[tuple[Decimal, Decimal], ...],
        quantity: Decimal,
        fallback_price: Decimal,
    ) -> tuple[Decimal, float]:
        if quantity <= 0:
            raise ValueError("fill quantity must be positive")
        if not levels:
            raise InsufficientDepthError("visible order book has no executable levels")
        remaining = quantity
        notional = Decimal("0")
        for price, available in levels:
            take = min(remaining, available)
            notional += take * price
            remaining -= take
            if remaining <= 0:
                break
        if remaining > 0:
            raise InsufficientDepthError(
                f"visible book cannot fill {quantity}; missing {remaining}"
            )
        average = notional / quantity
        impact = abs(float((average / fallback_price - 1) * Decimal("10000")))
        return average, impact

    def target_order(
        self,
        *,
        ledger: str,
        target: TargetPosition,
        position: PositionSnapshot,
        equity: Decimal,
        quote: MarketQuote,
        rules: ExchangeRules,
    ) -> PaperOrder | None:
        reference_price = quote.ask if target.target_weight >= position.weight else quote.bid
        target_value = equity * Decimal(str(target.target_weight))
        target_quantity = floor_to_step(target_value / reference_price, rules.step_size)
        delta = target_quantity - position.quantity
        if delta == 0:
            return None
        side = "BUY" if delta > 0 else "SELL"
        quantity = floor_to_step(abs(delta), rules.step_size)
        if side == "SELL":
            quantity = min(quantity, position.quantity)
        if quantity < rules.min_quantity or quantity <= 0:
            return None
        if quantity > rules.max_quantity:
            quantity = rules.max_quantity
        if quantity * reference_price < rules.min_notional:
            return None
        client_order_id = deterministic_id(
            "paper",
            ledger,
            target.asset.value,
            target.as_of.isoformat(),
            f"{target.target_weight:.10f}",
        )
        return PaperOrder(
            client_order_id=client_order_id,
            ledger=ledger,
            asset=target.asset,
            as_of=target.as_of,
            side=side,
            quantity=quantity,
            reference_price=reference_price,
            reason=target.reason,
        )

    def fill(self, order: PaperOrder, quote: MarketQuote) -> PaperFill:
        if order.side == "BUY":
            levels = quote.asks
            price, impact = self._book_fill(levels, order.quantity, quote.ask)
        elif order.side == "SELL":
            levels = quote.bids
            price, impact = self._book_fill(levels, order.quantity, quote.bid)
        else:
            raise ValueError(f"unsupported side: {order.side}")
        notional = order.quantity * price
        fee = notional * self.fee_rate
        return PaperFill(
            client_order_id=order.client_order_id,
            ledger=order.ledger,
            asset=order.asset,
            as_of=order.as_of,
            side=order.side,
            quantity=order.quantity,
            price=price,
            fee=fee,
            bid=quote.bid,
            ask=quote.ask,
            visible_depth_quantity=sum((quantity for _, quantity in levels), Decimal("0")),
            visible_depth_notional=sum(
                (level_price * quantity for level_price, quantity in levels), Decimal("0")
            ),
            spread_bps=quote.spread_bps,
            impact_bps=impact,
        )
