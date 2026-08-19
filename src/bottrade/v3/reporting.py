from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd

from bottrade.v3.training import MetaExperimentResult


def write_preholdout_report(
    results: list[MetaExperimentResult],
    *,
    output_dir: str | Path,
    protocol_version: str = "v3",
) -> Path:
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []
    trade_frames: list[pd.DataFrame] = []
    for result in results:
        rows.append(
            {
                "family": result.family,
                "asset": result.asset.value,
                **result.metrics,
                "folds": len(result.folds),
            }
        )
        if not result.trades.empty:
            trade_frames.append(result.trades.assign(family=result.family, asset=result.asset.value))
    metrics_path = destination / "metrics.json"
    metrics_path.write_text(json.dumps(rows, indent=2, default=str), encoding="utf-8")
    if trade_frames:
        pd.concat(trade_frames, ignore_index=True).to_parquet(destination / "trades.parquet", index=False)
    report = destination / "summary.md"
    lines = [f"# Relatório pré-holdout {protocol_version}", "", "O holdout não foi aberto.", "", "## Resultados"]
    if rows:
        lines.extend(
            [
                "",
                "| Família | Ativo | Retorno | Sharpe HAC | Drawdown | PF | Trades | Folds |",
                "|---|---|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for row in rows:
            lines.append(
                f"| {row['family']} | {row['asset']} | {float(row.get('total_return', 0.0)):.4f} | "
                f"{float(row.get('sharpe_hac', 0.0)):.3f} | {float(row.get('max_drawdown', 0.0)):.4f} | "
                f"{float(row.get('profit_factor', 0.0)):.3f} | {int(row.get('closed_trades', 0))} | {row['folds']} |"
            )
    else:
        lines.extend(["", "Nenhum resultado elegível foi produzido."])
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report
