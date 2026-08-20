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
from bottrade.v4.joint import run_joint_walk_forward
from bottrade.v4.search import run_parameter_search

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
        "protocol": (
            "docs/PROTOCOL_V4_3_EXIT_FILTER.md"
            if v4_config.protocol_version.startswith("v4.3")
            else "docs/PROTOCOL_V4_2_XGB_REFINEMENT.md"
            if v4_config.protocol_version.startswith("v4.2")
            else "docs/PROTOCOL_V4_XGB.md"
        ),
        "protocol_version": v4_config.protocol_version,
        "run_id": run_id,
        "holdout": {"start": v4_config.holdout_start, "end": v4_config.holdout_end},
        "config": {
            "horizon_hours": v4_config.horizon_hours,
            "seeds": list(v4_config.seeds),
            "device": v4_config.device,
            "objective": v4_config.objective,
            "stateful_hourly": v4_config.stateful_hourly,
            "max_holding_hours": v4_config.max_holding_hours,
            "exit_on_non_positive": v4_config.exit_on_non_positive,
            "stationary_features": v4_config.stationary_features,
            "frozen_params": frozen_params,
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


@v4_app.command("tune")
def tune(
    asset: Annotated[str | None, typer.Option(help="Ativo; vazio executa BTC, ETH e SOL.")] = None,
    search_folds: Annotated[
        int, typer.Option(help="Número de folds iniciais de desenvolvimento (pré-registrado: 3).")
    ] = 3,
    config_path: Annotated[
        Path, typer.Option("--v4-config", help="Configuração V4.2 refinada.")
    ] = Path("config/v4_refined.yaml"),
    app_config_path: Annotated[
        Path, typer.Option("--app-config", help="Configuração de dados do projeto.")
    ] = Path("config/default.yaml"),
    device: Annotated[
        str | None,
        typer.Option(help="cpu ou cuda; sobrescrever somente para experimento explícito."),
    ] = None,
) -> None:
    """Tune the fixed V4.2 candidate list on early pre-holdout folds."""

    if search_folds < 1:
        raise typer.BadParameter("search_folds deve ser positivo")
    v4_config = load_v4_config(config_path)
    if device is not None:
        if device not in {"cpu", "cuda"}:
            raise typer.BadParameter("device deve ser cpu ou cuda")
        v4_config = replace(v4_config, device=device).validate()
    app_config = load_config(app_config_path)
    app_config.ensure_directories()
    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    output_dir = app_config.project.artifact_dir / "v4" / "tuning" / run_id
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
        "protocol": (
            "docs/PROTOCOL_V4_3_EXIT_FILTER.md"
            if v4_config.protocol_version.startswith("v4.3")
            else "docs/PROTOCOL_V4_2_XGB_REFINEMENT.md"
        ),
        "protocol_version": v4_config.protocol_version,
        "run_id": run_id,
        "search_folds": search_folds,
        "search_seeds": [11],
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
        best_params, ranking, _ = run_parameter_search(
            dataset,
            config=v4_config,
            max_folds=search_folds,
            seeds=(11,),
        )
        asset_dir = output_dir / current_asset.value
        asset_dir.mkdir(parents=True, exist_ok=True)
        (asset_dir / "best_params.json").write_text(
            json.dumps(best_params, indent=2, sort_keys=True), encoding="utf-8"
        )
        payload = {
            "asset": current_asset.value,
            "rows": int(len(dataset.frame)),
            "valid_labels": int(dataset.frame["label_valid"].sum()),
            "features": len(dataset.feature_columns),
            "feature_names": list(dataset.feature_columns),
            "best_params": best_params,
            "ranking": ranking,
        }
        (asset_dir / "tuning.json").write_text(
            json.dumps(payload, indent=2, sort_keys=True, default=str), encoding="utf-8"
        )
        report["assets"][current_asset.value] = payload  # type: ignore[index]
        best = ranking[0]
        typer.echo(
            f"{current_asset.value}: melhor={best['candidate_id']} "
            f"score={float(best['score']):.5f} "
            f"retorno={float(best['metrics']['total_return']):.4%}"
        )
    report_path = output_dir / "tuning.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True, default=str), encoding="utf-8")
    typer.echo(f"Relatório de tuning {v4_config.protocol_version}: {report_path}")


@v4_app.command("joint")
def joint(
    asset: Annotated[
        str, typer.Option(help="Ativo de desenvolvimento; V4.4 usa BTCUSDT por padrão.")
    ] = "BTCUSDT",
    family: Annotated[
        str, typer.Option(help="xgboost ou hist_gradient_boosting.")
    ] = "xgboost",
    max_folds: Annotated[
        int | None,
        typer.Option(help="Piloto usa os últimos N folds; vazio executa todos os folds válidos."),
    ] = 12,
    config_path: Annotated[
        Path, typer.Option("--v4-config", help="Configuração V4.4 conjunta.")
    ] = Path("config/v4_joint.yaml"),
    app_config_path: Annotated[
        Path, typer.Option("--app-config", help="Configuração de dados do projeto.")
    ] = Path("config/default.yaml"),
    device: Annotated[
        str | None,
        typer.Option(help="cpu ou cuda; sobrescrever somente para experimento explícito."),
    ] = None,
) -> None:
    """Run the V4.4 classification + regression challenger for one asset."""

    try:
        current_asset = Asset(asset)
    except ValueError as exc:
        raise typer.BadParameter("asset deve ser BTCUSDT, ETHUSDT ou SOLUSDT") from exc
    if family not in {"xgboost", "hist_gradient_boosting"}:
        raise typer.BadParameter("family deve ser xgboost ou hist_gradient_boosting")
    if max_folds is not None and max_folds < 1:
        raise typer.BadParameter("max_folds deve ser positivo")
    v4_config = load_v4_config(config_path)
    if device is not None:
        if device not in {"cpu", "cuda"}:
            raise typer.BadParameter("device deve ser cpu ou cuda")
        v4_config = replace(v4_config, device=device).validate()
    app_config = load_config(app_config_path)
    app_config.ensure_directories()
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
    result = run_joint_walk_forward(
        dataset,
        config=v4_config,
        family=family,  # type: ignore[arg-type]
        max_folds=max_folds,
    )
    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    output_dir = app_config.project.artifact_dir / "v4" / "joint" / run_id / family / current_asset.value
    output_dir.mkdir(parents=True, exist_ok=True)
    result.trades.to_parquet(output_dir / "trades.parquet", index=False)
    protocol_doc = (
        "docs/PROTOCOL_V4_5_NORMALIZED.md"
        if v4_config.protocol_version.startswith("v4.5")
        else "docs/PROTOCOL_V4_4_JOINT.md"
    )
    payload = {
        "protocol": protocol_doc,
        "protocol_version": v4_config.protocol_version,
        "run_id": run_id,
        "asset": current_asset.value,
        "family": family,
        "classification_mode": v4_config.classification_mode,
        "normalized_return_target": v4_config.normalized_return_target,
        "rows": int(len(dataset.frame)),
        "valid_labels": int(dataset.frame["label_valid"].sum()),
        "features": len(dataset.feature_columns),
        "feature_names": list(dataset.feature_columns),
        "folds": [
            {
                "name": fold.name,
                "probability_threshold": fold.policy.probability_threshold,
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
    report_path = output_dir / "result.json"
    report_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, default=str), encoding="utf-8"
    )
    typer.echo(
        f"{current_asset.value}/{family}: {result.metrics['closed_trades']} trades, "
        f"retorno={result.metrics['total_return']:.4%}, "
        f"Sharpe={result.metrics['sharpe_daily']:.2f}"
    )
    typer.echo(f"Relatório {v4_config.protocol_version}: {report_path}")
