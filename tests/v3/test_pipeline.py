from __future__ import annotations

import json

import numpy as np
import pandas as pd
from typer.testing import CliRunner

from bottrade.v3.cli import v3_app
from bottrade.v3.config import load_v3_config
from bottrade.v3.datasets import ensure_preholdout, write_versioned_table
from bottrade.v3.portfolio import portfolio_backtest
from bottrade.v3.statistics import monthly_trade_frequency
from bottrade.v3.training import build_meta_table, build_transformer_sequences


def test_preholdout_filters_rows_and_keeps_manifest(tmp_path) -> None:
    config = load_v3_config("config/v3.yaml")
    frame = pd.DataFrame(
        {
            "as_of": pd.to_datetime(["2025-07-31T23:00:00Z", "2025-08-01T00:00:00Z"]),
            "value": [1.0, 2.0],
        }
    )
    filtered = ensure_preholdout(frame, config=config)
    assert len(filtered) == 1
    output = write_versioned_table(frame, tmp_path / "table.parquet", config=config, table_type="test")
    manifest = json.loads((output.parent / "table.parquet.manifest.json").read_text())
    assert manifest["rows"] == 1
    assert manifest["holdout_safe"] is True


def test_v3_policy_grid_matches_preregistered_protocol() -> None:
    config = load_v3_config("config/v3.yaml")
    assert config.probability_thresholds == (0.50, 0.55, 0.60)
    assert config.margin_bps == (0, 5, 10, 20, 30)


def test_transformer_sequences_are_causal_and_gap_aware() -> None:
    times = pd.date_range("2024-01-01", periods=170, freq="1h", tz="UTC")
    features = pd.DataFrame(
        {
            "as_of": times,
            "return_1h": np.arange(len(times), dtype=float),
            "continuity_segment_id": ["a"] * len(times),
        }
    )
    table = pd.DataFrame(
        {
            "candidate_id": ["c1", "c2"],
            "as_of": [times[167], times[168]],
            "return_1h": [167.0, 168.0],
            "signal_strength": [1.0, 2.0],
        }
    )
    values, valid = build_transformer_sequences(
        table, features, ["return_1h", "signal_strength"], lookback=168
    )
    assert valid.tolist() == [True, True]
    assert values.shape == (2, 168, 2)
    assert values[0, -1, 0] == 167.0
    assert values[0, -1, 1] == 1.0


def test_meta_table_excludes_event_outcomes_from_features() -> None:
    times = pd.date_range("2024-01-01", periods=3, freq="1h", tz="UTC")
    features = pd.DataFrame(
        {
            "as_of": times,
            "close": [100.0, 101.0, 102.0],
            "continuity_segment_id": ["a"] * 3,
        }
    )
    candidates = pd.DataFrame(
        {
            "candidate_id": ["c1"],
            "asset": ["BTCUSDT"],
            "as_of": [times[1]],
            "strategy_family": ["trend"],
            "variant_id": ["trend_ema_6_24_h6"],
            "horizon_hours": [6],
            "signal_strength": [1.0],
            "reference_price": [101.0],
            "ewma_volatility_1h": [0.01],
            "take_profit_return": [0.01],
            "stop_loss_return": [-0.01],
        }
    )
    labels = pd.DataFrame(
        {
            "candidate_id": ["c1"],
            "asset": ["BTCUSDT"],
            "as_of": [times[1]],
            "entry_price": [101.0],
            "exit_price": [102.0],
            "gross_return": [0.01],
            "net_return_1x": [0.0076],
            "net_return_2x": [0.0052],
            "net_return_3x": [0.0028],
            "mae": [-0.001],
            "label_valid": [True],
        }
    )
    _, columns = build_meta_table(features, candidates, labels)
    assert not {"entry_price", "exit_price", "gross_return", "label_valid", "net_return_1x"}.intersection(columns)


def test_portfolio_has_two_independent_ledgers_and_caps() -> None:
    config = load_v3_config("config/v3.yaml")
    times = pd.date_range("2024-01-01", periods=2, freq="1h", tz="UTC")
    decisions = pd.DataFrame(
        {
            "candidate_id": ["a", "b", "c"],
            "asset": ["BTCUSDT", "ETHUSDT", "BTCUSDT"],
            "entry_time": [times[0], times[0], times[1]],
            "exit_time": [times[1], times[1], times[1] + pd.Timedelta(hours=1)],
            "ewma_volatility_1h": [0.01, 0.02, 0.01],
            "expected_net_return": [0.01, 0.02, 0.03],
            "net_return_1x": [0.01, 0.02, -0.01],
            "approved": [True, True, True],
            "outcome": ["timeout", "timeout", "timeout"],
        }
    )
    first = portfolio_backtest(decisions, config=config, ledger_name="paper_500", initial_cash=500.0)
    second = portfolio_backtest(decisions, config=config, ledger_name="paper_1000", initial_cash=1000.0)
    assert first.ledger_name != second.ledger_name
    assert first.metrics["initial_cash"] == 500.0
    assert second.metrics["initial_cash"] == 1000.0
    assert first.trades["weight"].max() <= config.max_asset_weight


def test_v3_cli_preflight_reports_closed_holdout() -> None:
    from pathlib import Path

    import pytest

    if not Path("data/raw/market/BTCUSDT_1h.parquet").exists():
        pytest.skip("data/raw/market/BTCUSDT_1h.parquet not available in CI environment")
    runner = CliRunner()
    result = runner.invoke(v3_app, ["preflight", "--config", "config/v3.yaml"])
    assert result.exit_code == 0, result.output
    assert '"opened": false' in result.output


def test_monthly_frequency_ignores_partial_edge_months() -> None:
    exits = pd.date_range("2024-01-31", periods=5, freq="31D", tz="UTC")
    trades = pd.DataFrame({"exit_time": exits})
    frequency = monthly_trade_frequency(trades)
    assert frequency["complete_months"] == 3
    assert frequency["trades_per_month_min"] == 1
