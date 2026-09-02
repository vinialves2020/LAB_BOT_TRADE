from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from typing import Annotated

import numpy as np
import typer

from bottrade.config import load_config
from bottrade.domain import Asset
from bottrade.v4.config import V4Config
from bottrade.v4.features import build_direct_dataset, build_features, load_raw_market
from bottrade.v5.backtest import ModelRunResult, run_ensemble_walk_forward
from bottrade.v5.config import load_v5_config
from bottrade.v5.reporting import (
    generate_benchmark_report,
    generate_comparative_table,
    generate_portfolio_report,
)

v5_app = typer.Typer(
    name="v5",
    help="V5 Benchmark: Random Forest vs. Transformer vs. XGBoost (com gates de swing spot).",
    no_args_is_help=True,
)


@v5_app.command("benchmark")
def benchmark(
    asset: Annotated[str, typer.Option(help="Ativo para benchmark (ex: BTCUSDT)")] = "BTCUSDT",
    folds: Annotated[int | None, typer.Option(help="Quantidade de folds recentes para avaliar (ex: 3 para teste rápido, vazio para todos)")] = 3,
    models: Annotated[str, typer.Option(help="Modelos a comparar separados por vírgula: rf,transformer,xgboost")] = "rf,transformer,xgboost",
    config_path: Annotated[Path, typer.Option("--config", help="Arquivo de configuração V5")] = Path("config/v5.yaml"),
    app_config_path: Annotated[Path, typer.Option("--app-config", help="Configuração geral")] = Path("config/default.yaml"),
) -> None:
    """Executa o benchmark comparativo entre Random Forest, Transformer e XGBoost."""
    v5_config = load_v5_config(config_path)
    app_config = load_config(app_config_path)
    app_config.ensure_directories()

    if asset.strip().lower() == "all":
        target_assets = [Asset.BTCUSDT, Asset.ETHUSDT, Asset.SOLUSDT]
    else:
        target_assets = [Asset(a.strip()) for a in asset.split(",") if a.strip()]

    typer.echo("=== Iniciando Benchmark V5 ===")
    typer.echo(f"Ativos: {[a.value for a in target_assets]}")
    typer.echo(f"Folds a avaliar: {folds if folds is not None else 'Todos'}")
    typer.echo(f"Modelos selecionados: {models}")

    market = {
        item.value: load_raw_market(app_config.project.data_dir, item, "1h")
        for item in Asset
    }
    intrahour = (
        {
            item.value: load_raw_market(app_config.project.data_dir, item, "15m")
            for item in Asset
        }
        if v5_config.include_intrahour_15m
        else None
    )

    v4_compat = V4Config(
        holdout_start=v5_config.holdout_start,
        holdout_end=v5_config.holdout_end,
        lookback_hours=v5_config.tf_lookback_hours,
        horizon_hours=1,
        purge_hours=v5_config.purge_hours,
        round_trip_bps=v5_config.round_trip_bps,
        stationary_features=v5_config.stationary_features,
        include_intrahour_15m=v5_config.include_intrahour_15m,
    )

    model_list = [m.strip().lower() for m in models.split(",") if m.strip()]
    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    all_asset_results: dict[str, list[ModelRunResult]] = {}

    for target_asset in target_assets:
        typer.echo(f"\n--- Processando {target_asset.value} ---")
        features = build_features(
            asset=target_asset,
            market=market,
            intrahour=intrahour,
            config=v4_compat,
        )
        dataset = build_direct_dataset(
            asset=target_asset,
            features=features,
            market=market[target_asset.value],
            config=v4_compat,
            pre_holdout_only=True,
        )
        typer.echo(f"Dataset {target_asset.value}: {len(dataset.frame)} linhas, {len(dataset.feature_columns)} features.")

        results: list[ModelRunResult] = []
        for m in model_list:
            if m in {"rf", "random_forest"}:
                typer.echo(f"--> Treinando Random Forest ({target_asset.value})...")
                res = run_ensemble_walk_forward("random_forest", dataset, config=v5_config, max_folds=folds)
                results.append(res)
                typer.echo(f"    RF concluído em {res.fit_time_seconds:.1f}s | Sharpe: {res.metrics.get('sharpe_daily', 0):.2f} | Trades: {res.metrics.get('closed_trades', 0)}")
            elif m in {"transformer", "tf"}:
                typer.echo(f"--> Treinando Patch-Transformer ({target_asset.value}, {v5_config.tf_device})...")
                res = run_ensemble_walk_forward("transformer", dataset, config=v5_config, max_folds=folds)
                results.append(res)
                typer.echo(f"    Transformer concluído em {res.fit_time_seconds:.1f}s | Sharpe: {res.metrics.get('sharpe_daily', 0):.2f} | Trades: {res.metrics.get('closed_trades', 0)}")
            elif m in {"xgboost", "xgb"}:
                typer.echo(f"--> Treinando XGBoost ({target_asset.value})...")
                res = run_ensemble_walk_forward("xgboost", dataset, config=v5_config, max_folds=folds)
                results.append(res)
                typer.echo(f"    XGBoost concluído em {res.fit_time_seconds:.1f}s | Sharpe: {res.metrics.get('sharpe_daily', 0):.2f} | Trades: {res.metrics.get('closed_trades', 0)}")

        output_dir = Path("reports/generated/v5") / target_asset.value / run_id
        report_path = generate_benchmark_report(target_asset.value, results, output_dir)
        all_asset_results[target_asset.value] = results
        typer.echo("\n" + "=" * 50)
        typer.echo(f"Resultado {target_asset.value}:")
        typer.echo(generate_comparative_table(results))
        typer.echo("=" * 50)
        typer.echo(f"Relatório gravado em: {report_path}")

    if len(target_assets) > 1:
        portfolio_dir = Path("reports/generated/v5/portfolio") / run_id
        portfolio_path = generate_portfolio_report(all_asset_results, portfolio_dir)
        typer.echo("\n" + "#" * 50)
        typer.echo(portfolio_path.read_text(encoding="utf-8"))
        typer.echo("#" * 50)


@v5_app.command("export")
def export_champion(
    model: Annotated[str, typer.Option(help="Modelo a exportar: random_forest, transformer ou xgboost")] = "random_forest",
    asset: Annotated[str, typer.Option(help="Ativo para exportar")] = "BTCUSDT",
    output_dir: Annotated[Path, typer.Option(help="Diretório de destino")] = Path("artifacts/v5/champion"),
    config_path: Annotated[Path, typer.Option("--config", help="Arquivo de configuração V5")] = Path("config/v5.yaml"),
    app_config_path: Annotated[Path, typer.Option("--app-config", help="Configuração geral")] = Path("config/default.yaml"),
) -> None:
    """Treina e exporta o bundle ONNX verificado do modelo vencedor."""
    v5_config = load_v5_config(config_path)
    app_config = load_config(app_config_path)
    target_asset = Asset(asset)

    market = {
        item.value: load_raw_market(app_config.project.data_dir, item, "1h")
        for item in Asset
    }
    intrahour = (
        {
            item.value: load_raw_market(app_config.project.data_dir, item, "15m")
            for item in Asset
        }
        if v5_config.include_intrahour_15m
        else None
    )

    v4_compat = V4Config(
        holdout_start=v5_config.holdout_start,
        holdout_end=v5_config.holdout_end,
        lookback_hours=v5_config.tf_lookback_hours,
        horizon_hours=1,
        purge_hours=v5_config.purge_hours,
        round_trip_bps=v5_config.round_trip_bps,
        stationary_features=v5_config.stationary_features,
        include_intrahour_15m=v5_config.include_intrahour_15m,
    )

    features = build_features(asset=target_asset, market=market, intrahour=intrahour, config=v4_compat)
    dataset = build_direct_dataset(
        asset=target_asset,
        features=features,
        market=market[target_asset.value],
        config=v4_compat,
        pre_holdout_only=True,
    )

    frame = dataset.frame[dataset.frame["label_valid"].astype(bool)].reset_index(drop=True)
    x = frame[list(dataset.feature_columns)].to_numpy(dtype=np.float32)
    y = frame[dataset.target_column].to_numpy(dtype=np.float32)
    train_idx = np.arange(len(frame))

    typer.echo(f"Treinando {model} em {len(train_idx)} amostras para exportação...")
    if model in {"random_forest", "rf"}:
        from bottrade.v5.models.random_forest import RFEnsemble
        ensemble = RFEnsemble.create(config=v5_config, feature_names=dataset.feature_columns)
        ensemble.fit(x, y, train_idx)
        ensemble.export_onnx(output_dir)
        err = ensemble.verify_onnx(output_dir, x[:128])
        typer.echo(f"RF exportado para {output_dir} com erro ONNX={err:.2e} (OK)")
    elif model in {"transformer", "tf"}:
        from bottrade.v5.models.transformer import PatchTransformerEnsemble
        ensemble = PatchTransformerEnsemble.create(config=v5_config, feature_names=dataset.feature_columns)
        ensemble.fit(x, y, train_idx)
        ensemble.export_onnx(output_dir)
        err = ensemble.verify_onnx(output_dir, x[:128])
        typer.echo(f"Transformer exportado para {output_dir} com erro ONNX={err:.2e} (OK)")
    elif model in {"xgboost", "xgb"}:
        from bottrade.v5.models.xgboost_ref import create_xgboost_reference
        ensemble = create_xgboost_reference(config=v5_config, feature_names=dataset.feature_columns)
        ensemble.fit(x, y, train_idx)
        paths = ensemble.export_onnx(output_dir)
        sample_idx = np.arange(min(128, len(x)))
        err = ensemble.verify_onnx(paths, x, sample_idx)
        typer.echo(f"XGBoost exportado para {output_dir} com erro ONNX={err:.2e} (OK)")
    else:
        raise typer.BadParameter(f"Modelo desconhecido {model}")


@v5_app.command("stress-test")
def run_stress_test_cli(
    asset: Annotated[str, typer.Option(help="Ativo para stress-test (BTCUSDT, ETHUSDT, SOLUSDT ou all)")] = "all",
    folds: Annotated[int, typer.Option(help="Número de folds mensais de walk-forward a auditar (ex: 6 ou 12)")] = 6,
    models: Annotated[str, typer.Option(help="Modelo a avaliar: xgboost (ou rf, transformer)")] = "xgboost",
    config_path: Annotated[Path, typer.Option("--config", help="Arquivo de configuração V5")] = Path("config/v5.yaml"),
    app_config_path: Annotated[Path, typer.Option("--app-config", help="Configuração geral")] = Path("config/default.yaml"),
) -> None:
    """Executa a auditoria completa de cenários, regimes de mercado, degradação de custos e anti-overfitting."""
    from bottrade.v5.stress_test import evaluate_asset_stress, generate_stress_test_report

    v5_config = load_v5_config(config_path)
    app_config = load_config(app_config_path)
    app_config.ensure_directories()

    if asset.strip().lower() == "all":
        target_assets = [Asset.BTCUSDT, Asset.ETHUSDT, Asset.SOLUSDT]
    else:
        target_assets = [Asset(a.strip()) for a in asset.split(",") if a.strip()]

    typer.echo("=== INICIANDO AUDITORIA QUANTITATIVA E TESTE DE ESTRESSE V5 ===")
    typer.echo(f"Ativos: {[a.value for a in target_assets]}")
    typer.echo(f"Folds a auditar: {folds} meses")
    typer.echo(f"Modelo: {models}")

    market = {
        item.value: load_raw_market(app_config.project.data_dir, item, "1h")
        for item in Asset
    }
    intrahour = (
        {
            item.value: load_raw_market(app_config.project.data_dir, item, "15m")
            for item in Asset
        }
        if v5_config.include_intrahour_15m
        else None
    )

    v4_compat = V4Config(
        holdout_start=v5_config.holdout_start,
        holdout_end=v5_config.holdout_end,
        lookback_hours=v5_config.tf_lookback_hours,
        horizon_hours=1,
        purge_hours=v5_config.purge_hours,
        round_trip_bps=v5_config.round_trip_bps,
        stationary_features=v5_config.stationary_features,
        include_intrahour_15m=v5_config.include_intrahour_15m,
    )

    audit_results = []
    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")

    for target_asset in target_assets:
        typer.echo(f"\n--- Auditando {target_asset.value} ({folds} folds) ---")
        features = build_features(
            asset=target_asset,
            market=market,
            intrahour=intrahour,
            config=v4_compat,
        )
        dataset = build_direct_dataset(
            asset=target_asset,
            features=features,
            market=market[target_asset.value],
            config=v4_compat,
            pre_holdout_only=True,
        )

        typer.echo(f"Executando walk-forward ({models})...")
        run_res = run_ensemble_walk_forward(models, dataset, config=v5_config, max_folds=folds)

        typer.echo(f"Decompondo regimes e calculando DSR, PBO e Monte Carlo ({target_asset.value})...")
        audit_res = evaluate_asset_stress(
            asset=target_asset,
            run_result=run_res,
            market_1h=market[target_asset.value],
            num_trials_tested=10,
        )
        audit_results.append(audit_res)

    output_dir = Path("reports/generated/v5/stress_tests") / run_id
    report_file = generate_stress_test_report(audit_results, output_dir)
    typer.echo("\n" + "=" * 60)
    typer.echo(report_file.read_text(encoding="utf-8"))
    typer.echo("=" * 60)
    typer.echo(f"Relatório de auditoria salvo em: {report_file}")


@v5_app.command("paper-run")
def paper_run_cli(
    live: Annotated[bool, typer.Option(help="Conectar na API pública da Binance para preços e candles ao vivo")] = True,
    ledger: Annotated[str, typer.Option(help="Nome do ledger no SQLite")] = "paper_1000",
    loop: Annotated[bool, typer.Option(help="Executar continuamente em loop periódico")] = False,
    interval_seconds: Annotated[int, typer.Option(help="Intervalo em segundos entre ciclos no modo loop")] = 60,
    config_path: Annotated[Path, typer.Option("--config", help="Arquivo de configuração V5")] = Path("config/v5.yaml"),
    app_config_path: Annotated[Path, typer.Option("--app-config", help="Configuração geral")] = Path("config/default.yaml"),
) -> None:
    """Executa o ciclo oficial de Paper Trading V5 com candles ao vivo e modelos institucionais."""
    import time

    from bottrade.v5.paper import PaperTradingV5

    v5_config = load_v5_config(config_path)
    app_config = load_config(app_config_path)
    app_config.ensure_directories()

    typer.echo(f"Iniciando Paper Trading V5 (Live={live}, Ledger={ledger}, Loop={loop})...")
    engine = PaperTradingV5(v5_config=v5_config, app_config=app_config, ledger_name=ledger)

    while True:
        signals = engine.execute_cycle(live=live)
        summary = engine.get_status_summary(signals)
        typer.echo(summary)
        engine.notify_channels(signals, summary)
        if not loop:
            break
        typer.echo(f"\n[Aguardando {interval_seconds}s para o próximo ciclo... Pressione Ctrl+C para pausar]\n")
        time.sleep(interval_seconds)
