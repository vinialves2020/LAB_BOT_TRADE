from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import pandas as pd

from bottrade.config import AppConfig
from bottrade.evaluation import FinalGateEvaluator
from bottrade.storage import Storage
from bottrade.utils import utc_now


def _format_percent(value: float) -> str:
    return f"{value * 100:.2f}%"


class ReportGenerator:
    def __init__(self, config: AppConfig, storage: Storage | None = None) -> None:
        self.config = config
        self.storage = storage

    def experiment_records(self) -> list[dict[str, Any]]:
        records: list[dict[str, Any]] = []
        for directory in ("experiments", "refits"):
            root = self.config.project.artifact_dir / directory
            if not root.exists():
                continue
            for path in root.rglob("experiment.json"):
                record = json.loads(path.read_text(encoding="utf-8"))
                record["path"] = str(path)
                records.append(record)
        return sorted(records, key=lambda item: item.get("version", ""))

    def daily_summary(self) -> str:
        if self.storage is None:
            return "BOT_TRADE: armazenamento não configurado."
        rows = self.storage.recent_equity(limit=500)
        if not rows:
            return "BOT_TRADE: ainda não há snapshots de patrimônio."
        frame = pd.DataFrame(rows)
        latest = frame.sort_values("as_of").groupby("ledger", as_index=False).tail(1)
        lines = [f"📊 BOT_TRADE — resumo {utc_now().date().isoformat()} UTC"]
        for row in latest.itertuples(index=False):
            lines.append(
                f"{row.ledger}: {row.equity:.2f} USDT | "
                f"dia {_format_percent(row.daily_return)} | DD {_format_percent(row.drawdown)}"
            )
        recent_risk = self.storage.recent_risk_events(limit=20)
        today_risk = [
            item
            for item in recent_risk
            if _as_utc(item["as_of"]).date() == utc_now().date()
        ]
        lines.append(f"Eventos de risco hoje: {len(today_risk)}")
        return "\n".join(lines)

    def generate(self, output: Path | None = None) -> Path:
        path = output or (
            self.config.project.report_dir
            / f"relatorio-{utc_now().strftime('%Y%m%dT%H%M%SZ')}.md"
        )
        path.parent.mkdir(parents=True, exist_ok=True)
        experiments = self.experiment_records()
        lines = [
            "# Relatório técnico — RF × Transformer",
            "",
            f"Gerado em: {utc_now().isoformat()}",
            "",
            "## Protocolo",
            "",
            "- Mercado spot long/flat: BTCUSDT, ETHUSDT e SOLUSDT.",
            "- Candle de 1h e horizonte de previsão de 3h.",
            "- Holdout congelado: 2025-08-01 a 2026-07-31 UTC.",
            "- Custos-base: 24 bps por round trip; estresse: 48 bps.",
            "",
            "## Catálogo de experimentos",
            "",
        ]
        if not experiments:
            lines.append("Nenhum experimento concluído. O protocolo permanece em estado pré-registro.")
        else:
            lines.append(
                "| Ativo | Fase | Família | Braço | Retorno | Sharpe | Sortino | Drawdown | Custos | Trades |"
            )
            lines.append("|---|---|---|---|---:|---:|---:|---:|---:|---:|")
            for item in experiments:
                metrics = (
                    item.get("holdout_metrics")
                    or item.get("holdout_metrics_frozen")
                    or item.get("selection_metrics", {})
                )
                lines.append(
                    "| {asset} | {phase} | {family} | {arm} | {ret} | {sharpe:.2f} | "
                    "{sortino:.2f} | {dd} | {cost} | {trades} |".format(
                        asset=item["asset"],
                        phase=item.get("phase", "legacy"),
                        family=item["family"],
                        arm=item["arm"],
                        ret=_format_percent(float(metrics.get("total_return", 0))),
                        sharpe=float(metrics.get("sharpe", 0)),
                        sortino=float(metrics.get("sortino", 0)),
                        dd=_format_percent(float(metrics.get("max_drawdown", 0))),
                        cost=_format_percent(float(metrics.get("transaction_cost", 0))),
                        trades=int(metrics.get("closed_trades", 0)),
                    )
                )
            lines.extend(
                [
                    "",
                    "## Matriz de ablação e previsão",
                    "",
                    "A tabela acima é a matriz ativo × família × braço. Comparações válidas "
                    "são feitas dentro do mesmo ativo; SOL on-chain descreve atividade do "
                    "ecossistema e não é equivalente causal às métricas BTC/ETH.",
                    "",
                    "| Ativo | Família | Braço | MAE | RMSE | Spearman | Direção |",
                    "|---|---|---|---:|---:|---:|---:|",
                ]
            )
            for item in experiments:
                predictive = item.get("predictive_metrics") or item.get(
                    "calibration_predictive_metrics", {}
                )
                lines.append(
                    "| {asset} | {family} | {arm} | {mae:.4f} | {rmse:.4f} | "
                    "{spearman:.3f} | {direction:.1%} |".format(
                        asset=item["asset"],
                        family=item["family"],
                        arm=item["arm"],
                        mae=float(predictive.get("mae", 0)),
                        rmse=float(predictive.get("rmse", 0)),
                        spearman=float(predictive.get("spearman", 0)),
                        direction=float(predictive.get("directional_accuracy", 0)),
                    )
                )
            lines.extend(
                [
                    "",
                    "## Custos computacionais",
                    "",
                    "| Ativo | Família | Treino (s) | Inferência (ms/amostra) | Memória Python | Memória GPU | ONNX |",
                    "|---|---|---:|---:|---:|---:|---:|",
                ]
            )
            for item in experiments:
                operation = item.get("operational_metrics", {})
                lines.append(
                    "| {asset} | {family} | {fit:.2f} | {latency:.4f} | {memory} | {gpu_memory} | {onnx} |".format(
                        asset=item["asset"],
                        family=item["family"],
                        fit=float(operation.get("fit_seconds", 0)),
                        latency=float(operation.get("onnx_inference_ms_per_sample", 0)),
                        memory=int(operation.get("peak_python_memory_bytes", 0)),
                        gpu_memory=int(operation.get("gpu_peak_memory_bytes", 0)),
                        onnx=int(operation.get("onnx_size_bytes", 0)),
                    )
                )
            lines.extend(
                [
                    "",
                    "## Análise por regime",
                    "",
                    "| Ativo | Família | Braço | Regime | Horas | Retorno mediano por fold | Exposição |",
                    "|---|---|---|---|---:|---:|---:|",
                ]
            )
            for item in experiments:
                for regime, values in item.get("regime_metrics", {}).items():
                    lines.append(
                        "| {asset} | {family} | {arm} | {regime} | {hours} | {ret} | {exposure} |".format(
                            asset=item["asset"],
                            family=item["family"],
                            arm=item["arm"],
                            regime=regime,
                            hours=int(values.get("hours", 0)),
                            ret=_format_percent(float(values.get("median_total_return", 0))),
                            exposure=_format_percent(float(values.get("median_exposure", 0))),
                        )
                    )
            lines.extend(
                [
                    "",
                    "## Catálogo objetivo de forças e fraquezas",
                    "",
                    "| Família | Forças | Fraquezas |",
                    "|---|---|---|",
                    "| Random Forest | Treino/inferência simples; robusto em amostras tabulares; SHAP direto; baixo custo operacional. | Depende mais de lags/estatísticas desenhados; extrapola mal; representação temporal menos natural. |",
                    "| Transformer | Janela temporal conjunta de 168h; embeddings de calendário; interações sequenciais. | Mais dados, memória e tempo; maior variância entre seeds; explicação e depuração mais difíceis. |",
                    "",
                    "Atenção é apenas diagnóstico qualitativo, nunca explicação causal.",
                ]
            )
        lines.extend(["", "## Operação paper", ""])
        if self.storage is None:
            lines.append("Banco operacional não consultado.")
        else:
            lines.append(self.daily_summary())
            failures = self.storage.recent_risk_events(limit=1_000_000)
            lines.extend(
                [
                    "",
                    "## Falhas e eventos observados",
                    "",
                    f"Eventos de risco/auditoria registrados: {len(failures)}.",
                ]
            )
            for event in failures[-20:]:
                lines.append(
                    f"- {event['as_of']} · {event['ledger']} · {event['severity']} · "
                    f"{event['state']}: {event['message']}"
                )
            evaluation = FinalGateEvaluator(self.config, self.storage).evaluate()
            lines.extend(
                [
                    "",
                    "## Gates finais",
                    "",
                    f"Elegível apenas para futura revisão: **{evaluation['eligible_for_future_real_review']}**",
                    "",
                    "Motivos globais: "
                    + (", ".join(evaluation.get("global_reasons", [])) or "nenhum"),
                    "",
                ]
            )
            for asset, result in evaluation.get("assets", {}).items():
                reasons = ", ".join(result.get("reasons", [])) or "nenhum"
                lines.append(f"- {asset}: passou={result.get('passed')} — {reasons}")
        lines.extend(
            [
                "",
                "## Limitações e decisão",
                "",
                "Este relatório não autoriza negociação com dinheiro real. A decisão só poderá ser "
                "reavaliada depois do holdout, canário e seis meses oficiais de paper, sem alteração "
                "retroativa do protocolo.",
            ]
        )
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return path


def _as_utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=UTC)
    return value.astimezone(UTC)


def write_model_card(metadata: dict[str, Any], output: Path) -> Path:
    metrics = metadata.get("holdout_metrics") or metadata.get("selection_metrics", {})
    stress = metadata.get("stress_metrics") or metadata.get("selection_stress_metrics", {})
    predictive = metadata.get("predictive_metrics", {})
    operational = metadata.get("operational_metrics", {})
    source_control = metadata.get("source_control", {})
    lines = [
        f"# Model card — {metadata.get('asset')} / {metadata.get('family')}",
        "",
        f"- Versão: {metadata.get('version')}",
        f"- Braço de dados: {metadata.get('data_arm')}",
        f"- Dataset: {metadata.get('data_version')}",
        f"- Commit: {source_control.get('commit', 'unavailable')} (dirty={source_control.get('dirty', 'unknown')})",
        f"- Fase do protocolo: {metadata.get('protocol_phase')}",
        f"- Seleção pré-holdout: {metadata.get('selection_id') or 'ainda não congelada'}",
        f"- Papel congelado: {metadata.get('selection_role') or 'candidato'}",
        f"- Horizonte: {metadata.get('horizon_hours')}h",
        f"- ONNX verificado: {metadata.get('onnx_verified')}",
        f"- Erro máximo ONNX: {float(metadata.get('onnx_max_abs_error', 0)):.8f}",
        f"- Explicabilidade completa: {metadata.get('explainability_complete')}",
        "",
        "## Holdout",
        "",
        f"- Retorno líquido: {_format_percent(float(metrics.get('total_return', 0)))}",
        f"- Sharpe: {float(metrics.get('sharpe', 0)):.3f}",
        f"- Sortino: {float(metrics.get('sortino', 0)):.3f}",
        f"- Drawdown máximo: {_format_percent(float(metrics.get('max_drawdown', 0)))}",
        f"- Custos acumulados: {_format_percent(float(metrics.get('transaction_cost', 0)))}",
        f"- Trades fechados: {int(metrics.get('closed_trades', 0))}",
        "",
        "## Estresse de custos",
        "",
        f"- Retorno com custos 2×: {_format_percent(float(stress.get('total_return', 0)))}",
        "",
        "## Qualidade preditiva e operação",
        "",
        f"- MAE normalizado: {float(predictive.get('mae', 0)):.4f}",
        f"- RMSE normalizado: {float(predictive.get('rmse', 0)):.4f}",
        f"- Spearman: {float(predictive.get('spearman', 0)):.4f}",
        f"- Acerto direcional: {_format_percent(float(predictive.get('directional_accuracy', 0)))}",
        f"- Tempo de treino final: {float(operational.get('fit_seconds', 0)):.2f}s",
        f"- Inferência nativa: {float(operational.get('native_inference_ms_per_sample', 0)):.4f} ms/amostra",
        f"- Inferência ONNX: {float(operational.get('onnx_inference_ms_per_sample', 0)):.4f} ms/amostra",
        f"- Pico de memória Python/GPU: {int(operational.get('peak_python_memory_bytes', 0))} / {int(operational.get('gpu_peak_memory_bytes', 0))} bytes",
        "",
        "## Uso pretendido",
        "",
        "Somente pesquisa e paper trading spot long/flat. Não aprovado para ordens reais.",
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output
