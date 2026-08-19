from __future__ import annotations

import json
from pathlib import Path
from typing import Annotated, Any

import pandas as pd
import typer

from bottrade.domain import Asset
from bottrade.v3.backtest import signal_ceiling_backtest
from bottrade.v3.candidates import build_candidates
from bottrade.v3.config import V3Config, load_v3_config
from bottrade.v3.datasets import (
    ensure_preholdout,
    manifest_for,
    read_versioned_table,
    write_versioned_table,
)
from bottrade.v3.features import V3FeatureBuilder
from bottrade.v3.labels import label_candidates
from bottrade.v3.meta_models import fit_meta_model
from bottrade.v3.portfolio import portfolio_backtest
from bottrade.v3.selection import claim_holdout, create_selection_lock, load_selection_lock
from bottrade.v3.tracking import TrialLedger
from bottrade.v3.training import (
    build_meta_table,
    build_transformer_sequences,
    prepare_targets,
    walk_forward_meta_experiment,
)

v3_app = typer.Typer(
    name="v3",
    help="Protocolo V3: estratégias, rótulos cost-aware, meta-modelos e paper spot.",
    no_args_is_help=True,
)


def _config(path: Path) -> V3Config:
    return load_v3_config(path)


def _asset(value: str) -> Asset:
    try:
        return Asset(value.upper())
    except ValueError as exc:
        raise typer.BadParameter("ativo deve ser BTCUSDT, ETHUSDT ou SOLUSDT") from exc


def _emit(payload: Any, output: Path | None = None) -> None:
    text = json.dumps(payload, indent=2, sort_keys=True, default=str)
    if output is None:
        typer.echo(text)
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text + "\n", encoding="utf-8")
        typer.echo(str(output))


def _raw_path(directory: Path, asset: Asset, interval: str) -> Path:
    path = directory / f"{asset.value}_{interval}.parquet"
    if not path.exists():
        raise typer.BadParameter(f"fonte não encontrada: {path}")
    return path


@v3_app.command("preflight")
def preflight(
    config_path: Annotated[Path, typer.Option("--config")] = Path("config/v3.yaml"),
    raw_market_dir: Annotated[Path, typer.Option("--raw-market-dir")] = Path("data/raw/market"),
    protocol_path: Annotated[Path, typer.Option("--protocol")] = Path("docs/PROTOCOL_V3.md"),
) -> None:
    """Validate the locked protocol and required official raw files."""

    config = _config(config_path)
    files = {
        f"{asset.value}_{interval}": str(_raw_path(raw_market_dir, asset, interval))
        for asset in Asset
        for interval in ("1h", "15m")
    }
    _emit(
        {
            "status": "ok",
            "protocol_version": config.protocol_version,
            "protocol_path": str(protocol_path),
            "holdout": {"start": config.holdout_start, "end": config.holdout_end, "opened": False},
            "fold_requirement": config.minimum_pre_holdout_folds,
            "seeds": list(config.seeds),
            "raw_files": files,
        }
    )


@v3_app.command("features")
def features(
    asset: Annotated[str, typer.Option("--asset")],
    output: Annotated[Path, typer.Option("--output")],
    config_path: Annotated[Path, typer.Option("--config")] = Path("config/v3.yaml"),
    raw_market_dir: Annotated[Path, typer.Option("--raw-market-dir")] = Path("data/raw/market"),
) -> None:
    """Build point-in-time 1h + intrahour 15m features before the holdout."""

    target = _asset(asset)
    config = _config(config_path)
    market = {item.value: pd.read_parquet(_raw_path(raw_market_dir, item, "1h")) for item in Asset}
    intrahour = {item.value: pd.read_parquet(_raw_path(raw_market_dir, item, "15m")) for item in Asset}
    frame = V3FeatureBuilder(config).build(asset=target, market=market, intrahour=intrahour)
    frame = ensure_preholdout(frame, config=config)
    path = write_versioned_table(
        frame,
        output,
        config=config,
        table_type=f"features-{target.value}",
        source_paths=tuple(_raw_path(raw_market_dir, item, interval) for item in Asset for interval in ("1h", "15m")),
    )
    _emit({"path": str(path), "rows": len(frame), "columns": len(frame.columns), "manifest": str(manifest_for(path))})


@v3_app.command("candidates")
def candidates(
    features_path: Annotated[Path, typer.Option("--features")],
    asset: Annotated[str, typer.Option("--asset")],
    output: Annotated[Path, typer.Option("--output")],
    config_path: Annotated[Path, typer.Option("--config")] = Path("config/v3.yaml"),
) -> None:
    """Emit all pre-registered candidate signals without selecting winners."""

    target = _asset(asset)
    config = _config(config_path)
    frame = read_versioned_table(features_path, config=config)
    result = build_candidates(frame, asset=target, config=config)
    path = write_versioned_table(
        result,
        output,
        config=config,
        table_type=f"candidates-{target.value}",
        source_paths=(features_path,),
    )
    _emit({"path": str(path), "rows": len(result), "variants": sorted(result["variant_id"].unique().tolist()) if not result.empty else []})


@v3_app.command("labels")
def labels(
    candidates_path: Annotated[Path, typer.Option("--candidates")],
    intrahour_path: Annotated[Path, typer.Option("--intrahour")],
    output: Annotated[Path, typer.Option("--output")],
    config_path: Annotated[Path, typer.Option("--config")] = Path("config/v3.yaml"),
) -> None:
    """Create next-open TP/SL/timeout labels from official 15m candles."""

    config = _config(config_path)
    candidates_frame = read_versioned_table(candidates_path, config=config)
    if candidates_frame.empty:
        raise typer.BadParameter("candidates file is empty")
    symbols = candidates_frame["asset"].astype(str).unique().tolist()
    if len(symbols) != 1:
        raise typer.BadParameter("labels command accepts exactly one asset per file")
    result = label_candidates(
        candidates_frame,
        intrahour={symbols[0]: pd.read_parquet(intrahour_path)},
        config=config,
    )
    path = write_versioned_table(
        result,
        output,
        config=config,
        table_type=f"labels-{symbols[0]}",
        source_paths=(candidates_path, intrahour_path),
        time_columns=("as_of", "entry_time", "exit_time"),
    )
    valid = int(result["label_valid"].astype(bool).sum()) if not result.empty else 0
    _emit({"path": str(path), "rows": len(result), "valid_labels": valid})


@v3_app.command("deterministic")
def deterministic(
    labels_path: Annotated[Path, typer.Option("--labels")],
    output_dir: Annotated[Path, typer.Option("--output-dir")],
    config_path: Annotated[Path, typer.Option("--config")] = Path("config/v3.yaml"),
) -> None:
    """Run the transparent signal-ceiling replay at 1x/2x/3x costs."""

    config = _config(config_path)
    labels_frame = read_versioned_table(labels_path, config=config)
    output_dir.mkdir(parents=True, exist_ok=True)
    summaries: list[dict[str, Any]] = []
    for multiplier in config.stress_multipliers:
        result = signal_ceiling_backtest(labels_frame, config=config, cost_multiplier=float(multiplier))
        trades_path = output_dir / f"trades_{int(multiplier)}x.parquet"
        write_versioned_table(
            result.trades,
            trades_path,
            config=config,
            table_type=f"deterministic-trades-{int(multiplier)}x",
            source_paths=(labels_path,),
            time_columns=("as_of", "entry_time", "exit_time"),
        )
        summaries.append({"cost_multiplier": multiplier, **result.metrics, "trades_path": str(trades_path)})
    _emit(summaries, output_dir / "metrics.json")


@v3_app.command("meta-train")
def meta_train(
    features_path: Annotated[Path, typer.Option("--features")],
    candidates_path: Annotated[Path, typer.Option("--candidates")],
    labels_path: Annotated[Path, typer.Option("--labels")],
    asset: Annotated[str, typer.Option("--asset")],
    family: Annotated[str, typer.Option("--family")],
    output_dir: Annotated[Path, typer.Option("--output-dir")],
    config_path: Annotated[Path, typer.Option("--config")] = Path("config/v3.yaml"),
    seeds: Annotated[str | None, typer.Option("--seeds", help="Lista; padrão são as cinco seeds V3.")] = None,
    development_end: Annotated[str | None, typer.Option("--development-end")] = None,
    params_json: Annotated[str | None, typer.Option("--params-json", help="JSON de hiperparâmetros congelados.")] = None,
) -> None:
    """Run gap-aware walk-forward and fit the five-member pre-holdout ensemble."""

    target = _asset(asset)
    config = _config(config_path)
    feature_frame = read_versioned_table(features_path, config=config)
    candidate_frame = read_versioned_table(candidates_path, config=config)
    label_frame = read_versioned_table(labels_path, config=config)
    table, feature_columns = build_meta_table(feature_frame, candidate_frame, label_frame)
    table = prepare_targets(table)
    if table.empty:
        raise typer.BadParameter("meta table is empty after point-in-time joins")
    sequence_values: Any | None = None
    if family == "transformer":
        sequence_values, sequence_valid = build_transformer_sequences(
            table,
            feature_frame,
            feature_columns,
            lookback=config.lookback_hours,
        )
        table = table.loc[sequence_valid].reset_index(drop=True)
        sequence_values = sequence_values[sequence_valid]
        if table.empty:
            raise typer.BadParameter("no complete 168h sequences remain after gap filtering")
    seed_values = config.seeds if not seeds else tuple(int(item.strip()) for item in seeds.split(","))
    params = json.loads(params_json) if params_json else None
    if params is not None and not isinstance(params, dict):
        raise typer.BadParameter("params-json deve ser um objeto JSON")
    output_dir.mkdir(parents=True, exist_ok=True)
    ledger = TrialLedger(output_dir / "trial_ledger.jsonl")
    summaries: list[dict[str, Any]] = []
    for seed in seed_values:
        result = walk_forward_meta_experiment(
            table,
            feature_columns,
            family=family,
            asset=target,
            config=config,
            seed=seed,
            params=params,
            development_end=development_end or config.holdout_start,
            sequence_values=sequence_values,
        )
        member_dir = output_dir / f"seed_{seed}"
        member_dir.mkdir(parents=True, exist_ok=True)
        final_values = (
            sequence_values
            if sequence_values is not None
            else table[feature_columns].to_numpy(dtype="float32")
        )
        final = fit_meta_model(
            family,
            final_values,
            table["y_class"].to_numpy(dtype=int),
            table["net_return_1x"].to_numpy(dtype=float),
            table["mae"].to_numpy(dtype=float),
            seed=seed,
            params=params,
        )
        final.save_native(member_dir)
        ledger.append(
            {
                "protocol_version": config.protocol_version,
                "stage": "pre_holdout",
                "asset": target.value,
                "family": family,
                "seed": seed,
                "params": params or {},
                "rows": len(table),
                "feature_count": len(feature_columns),
                "folds": len(result.folds),
                "metrics": result.metrics,
                "artifact": str(member_dir),
                "holdout_claimed": False,
            }
        )
        summaries.append({"seed": seed, "folds": len(result.folds), **result.metrics, "artifact": str(member_dir)})
    _emit(
        {"family": family, "asset": target.value, "rows": len(table), "features": len(feature_columns), "members": summaries},
        output_dir / "metrics.json",
    )


@v3_app.command("portfolio")
def portfolio(
    decisions_path: Annotated[Path, typer.Option("--decisions")],
    output_dir: Annotated[Path, typer.Option("--output-dir")],
    config_path: Annotated[Path, typer.Option("--config")] = Path("config/v3.yaml"),
) -> None:
    """Replay decisions in both independent paper ledgers."""

    config = _config(config_path)
    decisions = read_versioned_table(decisions_path, config=config)
    output_dir.mkdir(parents=True, exist_ok=True)
    payload: dict[str, Any] = {}
    for ledger, cash in (("paper_500", 500.0), ("paper_1000", 1000.0)):
        result = portfolio_backtest(decisions, config=config, ledger_name=ledger, initial_cash=cash)
        trades_path = output_dir / f"{ledger}_trades.parquet"
        write_versioned_table(
            result.trades,
            trades_path,
            config=config,
            table_type=f"portfolio-{ledger}",
            source_paths=(decisions_path,),
            time_columns=("entry_time", "exit_time"),
        )
        payload[ledger] = {**result.metrics, "trades_path": str(trades_path)}
    _emit(payload, output_dir / "metrics.json")


@v3_app.command("select")
def select(
    records_path: Annotated[Path, typer.Option("--records")],
    output: Annotated[Path, typer.Option("--output")],
    config_path: Annotated[Path, typer.Option("--config")] = Path("config/v3.yaml"),
    protocol_path: Annotated[Path, typer.Option("--protocol")] = Path("docs/PROTOCOL_V3.md"),
) -> None:
    """Create the immutable pre-holdout selection lock; never opens holdout."""

    config = _config(config_path)
    records = json.loads(records_path.read_text(encoding="utf-8"))
    if not isinstance(records, dict):
        raise typer.BadParameter("records must be a JSON object keyed by asset")
    for asset, record in records.items():
        if not isinstance(record, dict):
            raise typer.BadParameter(f"record for {asset} must be an object")
        record["holdout_opened"] = False
    path = create_selection_lock(
        path=output,
        protocol_path=protocol_path,
        config_path=config_path,
        holdout_start=config.holdout_start,
        holdout_end=config.holdout_end,
        assets=records,
    )
    _emit({"path": str(path), "holdout_claimed": False})


@v3_app.command("holdout")
def holdout(
    lock: Annotated[Path, typer.Option("--lock")],
    confirm: Annotated[str | None, typer.Option("--confirm")] = None,
) -> None:
    """Claim the holdout only with the exact explicit confirmation string."""

    current = load_selection_lock(lock)
    if confirm != "OPEN-V3-HOLDOUT":
        _emit({"status": "closed", "holdout_claimed": bool(current["holdout_claimed"])})
        raise typer.Exit(code=2)
    _emit(claim_holdout(lock))


@v3_app.command("report")
def report(
    metrics_path: Annotated[Path, typer.Option("--metrics")],
    output_dir: Annotated[Path, typer.Option("--output-dir")],
) -> None:
    """Render a compact pre-holdout report from saved metrics JSON."""

    raw = json.loads(metrics_path.read_text(encoding="utf-8"))
    rows = raw if isinstance(raw, list) else raw.get("members", []) if isinstance(raw, dict) else []
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "summary.md"
    lines = ["# Relatório V3 pré-holdout", "", "O holdout continua fechado.", "", "## Métricas brutas", ""]
    lines.append("```json")
    lines.append(json.dumps(rows, indent=2, sort_keys=True, default=str))
    lines.extend(["```", ""])
    report_path.write_text("\n".join(lines), encoding="utf-8")
    typer.echo(str(report_path))
