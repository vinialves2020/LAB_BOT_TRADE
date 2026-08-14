from __future__ import annotations

from bottrade.config import load_config


def test_default_config_locks_research_protocol() -> None:
    config = load_config(create_dirs=False)
    assert config.market.interval == "1h"
    assert config.features.horizon_hours == 3
    assert config.features.lookback_hours == 168
    assert config.backtest.round_trip_cost == 0.0024
    assert [ledger.initial_cash for ledger in config.paper.ledgers] == [500.0, 1000.0]
    assert config.paper.max_asset_weight == 0.20
    assert config.paper.max_gross_weight == 0.50
