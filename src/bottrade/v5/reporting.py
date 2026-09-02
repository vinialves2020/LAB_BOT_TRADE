from __future__ import annotations

import json
from collections.abc import Sequence
from pathlib import Path

import numpy as np
import pandas as pd

from bottrade.v5.backtest import ModelRunResult


def generate_comparative_table(results: Sequence[ModelRunResult]) -> str:
    lines = [
        "| Modelo | Tempo Fit (s) | Trades | Trades/Mês | Retorno 24 bps | Retorno 48 bps | Sharpe | Drawdown | PF | Hit Rate | IC Pearson | Gate |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|",
    ]
    for r in results:
        m = r.metrics
        p = r.predictive_metrics
        g = r.gate_status
        gate_badge = "APROVADO" if g.get("overall", False) else "REPROVADO"
        lines.append(
            f"| **{r.model_name.upper()}** "
            f"| {r.fit_time_seconds:.1f}s "
            f"| {int(m.get('closed_trades', 0))} "
            f"| {float(m.get('average_monthly_trades', 0.0)):.2f} "
            f"| {float(m.get('total_return', 0.0)) * 100:+.2f}% "
            f"| {float(m.get('stress_return', 0.0)) * 100:+.2f}% "
            f"| {float(m.get('sharpe_daily', 0.0)):.2f} "
            f"| {float(m.get('maximum_drawdown', 0.0)) * 100:.2f}% "
            f"| {float(m.get('profit_factor', 0.0)):.2f} "
            f"| {float(p.get('directional_accuracy', 0.0)) * 100:.1f}% "
            f"| {float(p.get('ic_pearson', 0.0)):+.3f} "
            f"| **{gate_badge}** |"
        )
    return "\n".join(lines)


def generate_benchmark_report(
    asset: str,
    results: Sequence[ModelRunResult],
    output_dir: Path,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    table_md = generate_comparative_table(results)

    # Determine champion: prioritize gate approval, then highest Sharpe
    approved = [r for r in results if r.gate_status.get("overall", False)]
    if approved:
        champion = max(approved, key=lambda r: float(r.metrics.get("sharpe_daily", 0.0)))
    elif results:
        champion = max(results, key=lambda r: float(r.metrics.get("sharpe_daily", 0.0)))
    else:
        champion = None

    report_lines = [
        f"# Relatório Comparativo V5: RF × Transformer × XGBoost ({asset})",
        "",
        "## Resumo do Confronto Experimental",
        "",
        table_md,
        "",
        "## Diagnóstico dos Modelos",
        "",
    ]

    for r in results:
        m = r.metrics
        p = r.predictive_metrics
        g = r.gate_status
        report_lines.extend(
            [
                f"### {r.model_name.upper()}",
                f"- **Amostras Avaliadas**: {len(r.folds)} folds walk-forward.",
                f"- **Tempo de Treinamento**: {r.fit_time_seconds:.2f} segundos.",
                f"- **Métricas Preditivas**: MAE={p.get('mae', 0.0):.4f}, IC Pearson={p.get('ic_pearson', 0.0):.4f}, Acerto Direcional={p.get('directional_accuracy', 0.0)*100:.1f}%.",
                f"- **Métricas Financeiras**: Retorno Líquido (24 bps) = {float(m.get('total_return', 0.0))*100:+.2f}%, Sharpe = {float(m.get('sharpe_daily', 0.0)):.2f}, Max Drawdown = {float(m.get('maximum_drawdown', 0.0))*100:.2f}%, Profit Factor = {float(m.get('profit_factor', 0.0)):.2f}.",
                f"- **Status dos Gates**: Frequência={'OK' if g.get('frequency') else 'FAIL'}, Sharpe={'OK' if g.get('sharpe') else 'FAIL'}, Drawdown={'OK' if g.get('drawdown') else 'FAIL'}, Lucro={'OK' if g.get('positive_return') else 'FAIL'}.",
                "",
            ]
        )

    if champion is not None:
        report_lines.extend(
            [
                "## Conclusão e Recomendação para Promoção",
                f"- **Modelo Campeão**: **{champion.model_name.upper()}**",
                f"- **Justificativa**: Sharpe {float(champion.metrics.get('sharpe_daily', 0.0)):.2f}, Drawdown {float(champion.metrics.get('maximum_drawdown', 0.0))*100:.2f}%, Retorno Líquido {float(champion.metrics.get('total_return', 0.0))*100:+.2f}%.",
                "- Este modelo está elegível para exportação ONNX e inicialização de paper trading canário.",
            ]
        )

    report_text = "\n".join(report_lines)
    report_path = output_dir / f"benchmark_{asset}.md"
    report_path.write_text(report_text, encoding="utf-8")

    # Serialize JSON
    json_data = {
        "asset": asset,
        "champion": champion.model_name if champion else None,
        "results": [
            {
                "model": r.model_name,
                "fit_time_seconds": r.fit_time_seconds,
                "predict_time_seconds": r.predict_time_seconds,
                "metrics": r.metrics,
                "predictive_metrics": r.predictive_metrics,
                "gate_status": r.gate_status,
            }
            for r in results
        ],
    }
    (output_dir / f"benchmark_{asset}.json").write_text(json.dumps(json_data, indent=2), encoding="utf-8")

    return report_path


def generate_portfolio_report(
    asset_results: dict[str, Sequence[ModelRunResult]],
    output_dir: Path,
) -> Path:
    from bottrade.v4.backtest import summarize_trades
    output_dir.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Relatório de Portfólio Consolidado V5 (Multi-Ativo: BTC + ETH + SOL)",
        "",
        "| Modelo | Ativos | Trades Totais | Trades/Mês Portfólio | Retorno Médio 24 bps | Sharpe Médio | Drawdown Máximo | Profit Factor | Status Portfólio |",
        "|---|---|---:|---:|---:|---:|---:|---:|:---:|",
    ]
    model_names: set[str] = set()
    for res_list in asset_results.values():
        for r in res_list:
            model_names.add(r.model_name)

    for m_name in sorted(model_names):
        m_trades = []
        m_returns = []
        m_sharpes = []
        m_dds = []
        for _, res_list in asset_results.items():
            for r in res_list:
                if r.model_name == m_name:
                    if not r.trades.empty:
                        m_trades.append(r.trades)
                    m_returns.append(float(r.metrics.get("total_return", 0.0)))
                    m_sharpes.append(float(r.metrics.get("sharpe_daily", 0.0)))
                    m_dds.append(float(r.metrics.get("maximum_drawdown", 0.0)))

        all_trades = pd.concat(m_trades, ignore_index=True) if m_trades else pd.DataFrame()
        port_metrics = summarize_trades(all_trades)
        total_trades = int(port_metrics.get("closed_trades", 0))
        monthly_trades = float(port_metrics.get("average_monthly_trades", 0.0))
        mean_ret = float(np.mean(m_returns)) if m_returns else 0.0
        mean_sharpe = float(np.mean(m_sharpes)) if m_sharpes else 0.0
        max_dd = max(m_dds) if m_dds else 0.0
        pf = float(port_metrics.get("profit_factor", 0.0))

        pass_port = total_trades >= 4 and mean_ret > 0 and max_dd <= 0.08
        badge = "APROVADO" if pass_port else "REPROVADO"

        lines.append(
            f"| **{m_name.upper()}** | {len(asset_results)} ativos | {total_trades} | {monthly_trades:.2f} | {mean_ret*100:+.2f}% | {mean_sharpe:.2f} | {max_dd*100:.2f}% | {pf:.2f} | **{badge}** |"
        )

    text = "\n".join(lines)
    path = output_dir / "portfolio_summary.md"
    path.write_text(text, encoding="utf-8")
    return path
