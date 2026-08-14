from __future__ import annotations

from datetime import UTC, datetime
from decimal import Decimal

import pytest

from bottrade.config import load_config
from bottrade.domain import (
    Asset,
    DataArm,
    EquitySnapshot,
    Forecast,
    ModelFamily,
    RiskState,
)
from bottrade.risk import PortfolioRiskEngine


def _forecast(asset: Asset, value: float = 0.01) -> Forecast:
    now = datetime.now(UTC)
    return Forecast(
        asset=asset,
        as_of=now,
        horizon_hours=3,
        expected_return=value,
        model_family=ModelFamily.RANDOM_FOREST,
        model_version="v1",
        data_version="d1",
        data_arm=DataArm.MARKET,
        threshold_return=0.0024,
    )


def test_inverse_volatility_targets_respect_both_caps() -> None:
    config = load_config(create_dirs=False)
    engine = PortfolioRiskEngine(config.paper)
    targets = engine.target_positions(
        forecasts={asset: _forecast(asset) for asset in Asset},
        volatilities={Asset.BTCUSDT: 0.01, Asset.ETHUSDT: 0.02, Asset.SOLUSDT: 0.03},
        current_weights={},
        as_of=datetime.now(UTC),
    )
    assert max(target.target_weight for target in targets) <= 0.20
    assert sum(target.target_weight for target in targets) == pytest.approx(0.50)


def test_drawdown_forces_all_open_assets_closed() -> None:
    config = load_config(create_dirs=False)
    engine = PortfolioRiskEngine(config.paper)
    equity = EquitySnapshot(
        ledger="paper_500",
        as_of=datetime.now(UTC),
        cash=Decimal("100"),
        positions_value=Decimal("350"),
        equity=Decimal("450"),
        peak_equity=Decimal("500"),
        drawdown=0.10,
        daily_return=-0.02,
    )
    assessment = engine.assess(
        status=RiskState.NORMAL,
        equity=equity,
        positions=[],
        as_of=datetime.now(UTC),
    )
    assert assessment.state == RiskState.CIRCUIT_BREAKER
    assert assessment.block_new_positions


def test_entry_threshold_is_hysteresis_but_nonpositive_forecast_exits() -> None:
    config = load_config(create_dirs=False)
    engine = PortfolioRiskEngine(config.paper)
    now = datetime.now(UTC)
    held = engine.target_positions(
        forecasts={Asset.BTCUSDT: _forecast(Asset.BTCUSDT, value=0.001)},
        volatilities={Asset.BTCUSDT: 0.01},
        current_weights={Asset.BTCUSDT: 0.20},
        as_of=now,
    )
    assert next(item for item in held if item.asset == Asset.BTCUSDT).target_weight > 0

    exited = engine.target_positions(
        forecasts={Asset.BTCUSDT: _forecast(Asset.BTCUSDT, value=0.0)},
        volatilities={Asset.BTCUSDT: 0.01},
        current_weights={Asset.BTCUSDT: 0.01},
        as_of=now,
    )
    btc = next(item for item in exited if item.asset == Asset.BTCUSDT)
    assert btc.target_weight == 0.0
    assert btc.reason == "forecast_exit_non_positive"
