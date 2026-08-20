from __future__ import annotations

import json
from dataclasses import replace
from datetime import UTC, datetime
from pathlib import Path
from typing import Annotated

import typer

from bottrade.config import load_config
from bottrade.domain import Asset
from bottrade.v4.backtest import run_walk_forward
from bottrade.v4.config import load_v4_config
from bottrade.v4.features import build_direct_dataset, build_features, load_raw_market

v4_app = typer.Typer(
    name="v4",
    help="V4 XGBoost direto, cost-aware, sem abrir o holdout.",
    no_args_is_help=True,
)


def _assets(value: str | None) -> list[Asset]:
    return [Asset(value)] if value else list(Asset)


@v4_app.command("run")
def run(
    asset: Annotated[str | None, typer.Option(help="Ativo; vazio executa BTC, ETH e SOL.")] = None,
    max_folds: Annotated[
        int | None,
        typer.Option(help="Piloto usa os últimos N folds; vazio executa todos os folds válidos."),
    ] = 3,
    config_path: Annotated[
        Path, typer.Option("--v4-config", help="Configuração pré-registrada da V4.")
    ] = Path("config/v4.yaml"),
    app_config_path: Annotated[
        Path, typer.Option("--app-config", help="Configuração de dados do projeto.")
    ] = Path("config/default.yaml"),
    device: Annotated[
        str | None,
        typer.Option(help="cpu ou cuda; sobrescrever somente para experimento explícito."),
    ] = None,
    params: Annotated[
        Path | None, typer.Option(help="JSON opcional de parâmetros congelados do XGBoost.")
    ] = None,
) -> None:
    """Run the V4 pre-holdout walk-forward experiment."""

    v4_config = load_v4_config(config_path)
    if device is not None:
        if device not in {"cpu", "cuda"}:
            raise typer.BadParameter("device deve ser cpu ou cuda")
        v4_config = replace(v4_config, device=device).validate()
    app_config = load_config(app_config_path)
    frozen_params = json.loads(params.read_text(encoding="utf-8")) if params else None
    app_config.ensure_directories()
    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    output_dir = app_config.project.artifact_dir / "v4" / run_id
    output_dir.mkdir(parents=True, exist_ok=True)
    market = {
        item.value: load_raw_market(app_config.project.data_dir, item, "1h")
        for item in Asset
    }
    intrahour = (
        {
            item.value: load_raw_market(app_config.project.data_dir, item, "15m")
            for item in Asset
        }
        if v4_config.include_intrahour_15m
        else None
    )
    report: dict[str, object] = {
        "protocol": "docs/PROTOCOL_V4_XGB.md",
        "protocol_version": v4_config.protocol_version,
        "run_id": run_id,
        "holdout": {"start": v4_config.holdout_start, "end": v4_config.holdout_end},
        "config": {
            "horizon_hours": v4_config.horizon_hours,
            "seeds": list(v4_config.seeds),
            "device": v4_config.device,
            "objective": v4_config.objective,
            "stateful_hourly": v4_config.stateful_hourly,
            "max_folds": max_folds,
        },
        "assets": {},
    }
    for current_asset in _assets(asset):
        features = build_features(
            asset=current_asset,
            market=market,
            intrahour=intrahour,
            config=v4_config,
        )
        dataset = build_direct_dataset(
            asset=current_asset,
            features=features,
            market=market[current_asset.value],
            config=v4_config,
            pre_holdout_only=True,
        )
        result = run_walk_forward(
            dataset,
            config=v4_config,
            params=frozen_params,
            max_folds=max_folds,
        )
        asset_dir = output_dir / current_asset.value
        asset_dir.mkdir(parents=True, exist_ok=True)
        result.trades.to_parquet(asset_dir / "trades.parquet", index=False)
        payload = {
            "asset": current_asset.value,
            "rows": int(len(dataset.frame)),
            "valid_labels": int(dataset.frame["label_valid"].sum()),
            "features": len(dataset.feature_columns),
            "feature_names": list(dataset.feature_columns),
            "folds": [
                {
                    "name": fold.name,
                    "margin_bps": fold.policy.margin_bps,
                    "calibration": fold.calibration,
                    "metrics": fold.metrics,
                    "seed_metrics": fold.seed_metrics,
                }
                for fold in result.folds
            ],
            "metrics": result.metrics,
            "top_features": list(result.feature_importance.items())[:25],
        }
        (asset_dir / "result.json").write_text(
            json.dumps(payload, indent=2, sort_keys=True, default=str), encoding="utf-8"
        )
        report["assets"][current_asset.value] = payload  # type: ignore[index]
        typer.echo(
            f"{current_asset.value}: {result.metrics['closed_trades']} trades, "
            f"retorno={result.metrics['total_return']:.4%}, "
            f"Sharpe={result.metrics['sharpe_daily']:.2f}"
        )
    report_path = output_dir / "run.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True, default=str), encoding="utf-8")
    typer.echo(f"Relatório V4: {report_path}")
