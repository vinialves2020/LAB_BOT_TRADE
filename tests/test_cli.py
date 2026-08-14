from __future__ import annotations

from datetime import UTC, datetime, timedelta
from types import SimpleNamespace

from typer.testing import CliRunner

from bottrade.cli import app
from bottrade.domain import Asset, RiskState, RunStage
from bottrade.storage import Storage


def test_cli_exposes_required_workflow_commands() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    for command in ["data", "dataset", "train", "backtest", "paper", "report"]:
        assert command in result.stdout


def test_canary_refuses_to_start_when_every_asset_is_cash(app_config, monkeypatch) -> None:
    monkeypatch.setattr("bottrade.cli._config", lambda _path: app_config)
    monkeypatch.setattr(
        "bottrade.cli._active_slots_or_cash",
        lambda _config, _registry, asset: ([], f"{asset.value} failed holdout"),
    )
    result = CliRunner().invoke(app, ["paper", "canary-start"])
    assert result.exit_code != 0
    assert "nenhum ativo passou o holdout" in result.stderr


def test_canary_completion_rejects_mid_phase_asset_activation(
    app_config, monkeypatch
) -> None:
    storage = Storage(app_config.runtime.database_url)
    storage.initialize(app_config)
    storage.start_paper_phase(
        RunStage.CANARY,
        started_at=datetime.now(UTC) - timedelta(days=15),
        duration_days=app_config.paper.canary_days,
        active_assets=[Asset.BTCUSDT],
    )
    marked: list[tuple[Asset, str]] = []

    class DummyRegistry:
        def mark_canary_passed(self, asset: Asset, version: str) -> None:
            marked.append((asset, version))

    metadata = SimpleNamespace(version="holdout-v1")

    def slots(_config, _registry, asset):
        if asset in {Asset.BTCUSDT, Asset.ETHUSDT}:
            return [("champion", metadata)], None
        return [], "cash"

    monkeypatch.setattr("bottrade.cli._config", lambda _path: app_config)
    monkeypatch.setattr("bottrade.cli.ModelRegistry", lambda _config: DummyRegistry())
    monkeypatch.setattr("bottrade.cli._active_slots_or_cash", slots)
    result = CliRunner().invoke(app, ["paper", "canary-complete"])
    assert result.exit_code != 0
    assert "conjunto congelado" in result.stderr
    assert marked == []
    assert storage.active_paper_phase() is not None


def test_manual_resume_cannot_bypass_same_day_daily_stop(app_config, monkeypatch) -> None:
    storage = Storage(app_config.runtime.database_url)
    storage.initialize(app_config)
    storage.set_ledger_status("paper_500", RiskState.DAILY_STOP)
    monkeypatch.setattr("bottrade.cli._config", lambda _path: app_config)
    result = CliRunner().invoke(
        app,
        [
            "paper",
            "resume",
            "--ledger",
            "paper_500",
            "--confirmation",
            "RESUME-PAPER",
        ],
    )
    assert result.exit_code != 0
    assert "daily_stop" in result.stderr
    assert storage.ledger_status("paper_500") == RiskState.DAILY_STOP
