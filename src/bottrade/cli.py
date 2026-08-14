from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import TYPE_CHECKING, Annotated

import typer

from bottrade.config import AppConfig, load_config
from bottrade.data.binance import BinanceClient
from bottrade.data.http import PublicHttpClient
from bottrade.data.pipeline import DataPipeline
from bottrade.dataset import DatasetBuilder
from bottrade.domain import Asset, DataArm, ModelFamily, RiskState, RunStage
from bottrade.evaluation import FinalGateEvaluator
from bottrade.jobs import JobRunner
from bottrade.logging_utils import configure_logging
from bottrade.models.registry import ModelMetadata, ModelRegistry
from bottrade.reporting import ReportGenerator, write_model_card
from bottrade.selection import SelectionLock, SelectionManager
from bottrade.storage import Storage
from bottrade.utils import ensure_utc, utc_now

if TYPE_CHECKING:
    from bottrade.training import ExperimentResult

app = typer.Typer(
    name="bottrade",
    help="Laboratório RF × Transformer e bot paper spot long/flat.",
    no_args_is_help=True,
)
data_app = typer.Typer(help="Coleta e validação de fontes públicas.")
dataset_app = typer.Typer(help="Construção point-in-time dos braços de dados.")
paper_app = typer.Typer(help="Ledger e jobs de paper trading; nunca envia ordens reais.")
models_app = typer.Typer(help="Registro, promoção e publicação de modelos ONNX.")
app.add_typer(data_app, name="data")
app.add_typer(dataset_app, name="dataset")
app.add_typer(paper_app, name="paper")
app.add_typer(models_app, name="models")

ConfigOption = Annotated[
    str | None,
    typer.Option("--config", help="Arquivo YAML; padrão BOTTRADE_CONFIG/config/default.yaml."),
]


def _config(path: str | None) -> AppConfig:
    config = load_config(path)
    configure_logging(config.runtime.log_level)
    return config


def _datetime(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return parsed.replace(tzinfo=UTC) if parsed.tzinfo is None else parsed.astimezone(UTC)


def _seeds(value: str | None, config: AppConfig) -> list[int]:
    return config.training.seeds if not value else [int(item.strip()) for item in value.split(",")]


def _active_slots_or_cash(
    config: AppConfig,
    registry: ModelRegistry,
    asset: Asset,
) -> tuple[list[tuple[str, ModelMetadata]], str | None]:
    try:
        lock = SelectionManager(config).load(asset)
    except FileNotFoundError as exc:
        raise typer.BadParameter(
            f"{asset.value} não tem modelo nem seleção que justifique caixa"
        ) from exc
    if lock.status == "cash":
        return [], "nenhum candidato tecnicamente válido antes do holdout"

    approved_versions: dict[str, str] = {}
    for role in ("champion", "market_fallback"):
        version = lock.holdout_versions.get(role)
        if not version:
            raise typer.BadParameter(f"{asset.value} ainda não concluiu o holdout de {role}")
        try:
            _, holdout_metadata = registry.load_version(asset, version)
        except FileNotFoundError as exc:
            raise typer.BadParameter(
                f"artefato holdout {asset.value}/{role} não está disponível"
            ) from exc
        reasons = registry.offline_gate_reasons(holdout_metadata)
        if reasons:
            return [], f"{role} reprovado no holdout: " + ",".join(reasons)
        approved_versions[role] = version

    slots: list[tuple[str, ModelMetadata]] = []
    for role in ("champion", "market_fallback"):
        try:
            _, metadata = registry.resolve(asset, role)
        except FileNotFoundError as exc:
            raise typer.BadParameter(
                f"{asset.value}/{role} passou o holdout, mas não foi promovido"
            ) from exc
        if metadata.version != approved_versions[role]:
            raise typer.BadParameter(
                f"{asset.value}/{role} não aponta para a versão holdout congelada"
            )
        slots.append((role, metadata))

    challenger_version = lock.holdout_versions.get("challenger")
    if challenger_version:
        _, challenger_holdout = registry.load_version(asset, challenger_version)
        challenger_reasons = registry.offline_gate_reasons(challenger_holdout)
        if not challenger_reasons:
            try:
                _, challenger = registry.resolve(asset, "challenger")
            except FileNotFoundError as exc:
                raise typer.BadParameter(
                    f"{asset.value}/challenger passou o holdout, mas não foi promovido"
                ) from exc
            if challenger.version != challenger_version:
                raise typer.BadParameter(
                    f"{asset.value}/challenger não aponta para o holdout congelado"
                )
            slots.append(("challenger", challenger))
    return slots, None


@data_app.command("sync")
def data_sync(
    config_path: ConfigOption = None,
    start: Annotated[
        str | None, typer.Option(help="ISO-8601 UTC; padrão início mais antigo.")
    ] = None,
    end: Annotated[str | None, typer.Option(help="ISO-8601 UTC; padrão agora.")] = None,
    market_only: Annotated[bool, typer.Option(help="Não coleta on-chain/sentimento.")] = False,
) -> None:
    config = _config(config_path)
    default_start = min(config.market.symbols.values())
    manifest = DataPipeline(config).sync(
        start=_datetime(start or default_start),
        end=_datetime(end) if end else utc_now(),
        include_alternatives=not market_only,
    )
    typer.echo(
        json.dumps({"data_version": manifest.data_version, "sources": len(manifest.sources)})
    )


@dataset_app.command("build")
def dataset_build(
    config_path: ConfigOption = None,
    asset: Annotated[str | None, typer.Option(help="BTCUSDT, ETHUSDT ou SOLUSDT.")] = None,
) -> None:
    config = _config(config_path)
    assets = [Asset(asset)] if asset else None
    bundles = DatasetBuilder(config).build(assets)
    typer.echo(f"{len(bundles)} datasets construídos e versionados.")


def _run_experiment(
    *,
    config: AppConfig,
    asset: str,
    arm: str,
    family: str,
    trials: int,
    max_folds: int | None,
    seeds: str | None,
    params_override: dict | None = None,
    phase: str = "development",
    selection_lock: SelectionLock | None = None,
    selection_role: str = "champion",
) -> ExperimentResult:
    # Training dependencies (PyTorch, scikit-learn and explainers) are intentionally
    # absent from the small Cloud Run runtime image. Keep them behind training CLIs.
    from bottrade.training import (
        CandidateRejectedError,
        ExperimentRunner,
        HyperparameterSearchRejectedError,
    )

    bundle = DatasetBuilder(config).load(Asset(asset), DataArm(arm))
    try:
        result = ExperimentRunner(config).run(
            bundle,
            ModelFamily(family),
            trials=trials,
            max_search_folds=max_folds,
            seeds=_seeds(seeds, config),
            params_override=params_override,
            phase=phase,
            selection_lock=selection_lock,
            selection_role=selection_role,
        )
    except CandidateRejectedError as exc:
        typer.echo(
            json.dumps(
                {
                    "status": "rejected",
                    "reason": str(exc),
                    "record": str(exc.rejection_path),
                },
                indent=2,
            ),
            err=True,
        )
        raise typer.Exit(code=2) from exc
    except HyperparameterSearchRejectedError as exc:
        typer.echo(
            json.dumps(
                {
                    "status": "rejected",
                    "stage": "hyperparameter_search",
                    "reason": str(exc),
                },
                indent=2,
            ),
            err=True,
        )
        raise typer.Exit(code=2) from exc
    metadata_path = result.registry_path / "metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    write_model_card(metadata, result.registry_path / "MODEL_CARD.md")
    typer.echo(
        json.dumps(
            {
                "run_id": result.run_id,
                "version": result.version,
                "phase": result.phase,
                "selection": result.selection_metrics,
                "holdout": result.holdout_metrics,
                "stress": result.stress_metrics,
                "registry": str(result.registry_path),
            },
            indent=2,
            default=str,
        )
    )
    return result


@app.command("train")
def train(
    asset: Annotated[str, typer.Option(help="BTCUSDT, ETHUSDT ou SOLUSDT.")],
    family: Annotated[str, typer.Option(help="random_forest ou transformer.")],
    arm: Annotated[str, typer.Option(help="Braço de dados.")] = "market",
    trials: Annotated[int, typer.Option(min=1, max=30)] = 30,
    max_folds: Annotated[
        int | None, typer.Option(help="Limite opcional para pesquisa rápida.")
    ] = None,
    seeds: Annotated[str | None, typer.Option(help="Seeds separadas por vírgula.")] = None,
    config_path: ConfigOption = None,
) -> None:
    config = _config(config_path)
    _run_experiment(
        config=config,
        asset=asset,
        arm=arm,
        family=family,
        trials=trials,
        max_folds=max_folds,
        seeds=seeds,
    )


@app.command("backtest")
def backtest(
    asset: Annotated[str, typer.Option(help="BTCUSDT, ETHUSDT ou SOLUSDT.")],
    family: Annotated[str, typer.Option(help="random_forest ou transformer.")],
    arm: Annotated[str, typer.Option(help="Braço de dados.")] = "market",
    params: Annotated[Path | None, typer.Option(help="JSON de parâmetros congelados.")] = None,
    max_folds: Annotated[int | None, typer.Option()] = None,
    seeds: Annotated[str | None, typer.Option()] = None,
    config_path: ConfigOption = None,
) -> None:
    config = _config(config_path)
    family_enum = ModelFamily(family)
    if params:
        frozen = json.loads(params.read_text(encoding="utf-8"))
    else:
        candidate = (
            config.project.artifact_dir
            / "experiments"
            / asset
            / DataArm.MARKET.value
            / family_enum.value
            / "best_params.json"
        )
        if candidate.exists():
            frozen = json.loads(candidate.read_text(encoding="utf-8"))
        elif family_enum == ModelFamily.RANDOM_FOREST:
            frozen = config.training.random_forest.model_dump()
        else:
            frozen = config.training.transformer.model_dump()
    _run_experiment(
        config=config,
        asset=asset,
        arm=arm,
        family=family,
        trials=1,
        max_folds=max_folds,
        seeds=seeds,
        params_override=frozen,
    )


@models_app.command("select")
def select_champion(
    asset: Annotated[str, typer.Option(help="BTCUSDT, ETHUSDT ou SOLUSDT.")],
    config_path: ConfigOption = None,
) -> None:
    """Freeze family, data arm and parameters before any holdout evaluation."""

    config = _config(config_path)
    lock = SelectionManager(config).select(Asset(asset))
    typer.echo(json.dumps(lock.model_dump(mode="json"), indent=2, sort_keys=True))


@app.command("holdout")
def holdout(
    asset: Annotated[str, typer.Option(help="Ativo cuja seleção já foi congelada.")],
    role: Annotated[
        str,
        typer.Option(help="champion, market_fallback ou challenger pré-congelado."),
    ] = "champion",
    resume: Annotated[
        bool,
        typer.Option(help="Recupera a mesma execução congelada após falha operacional."),
    ] = False,
    config_path: ConfigOption = None,
) -> None:
    """Open the frozen holdout exactly once for the pre-selected candidate."""

    from bottrade.training import ExperimentRunner

    config = _config(config_path)
    asset_enum = Asset(asset)
    manager = SelectionManager(config)
    lock = manager.claim_holdout(asset_enum, role=role, resume=resume)
    selected = manager.role(lock, role)
    family = ModelFamily(selected["family"])
    data_arm = DataArm(selected["data_arm"])
    bundle = DatasetBuilder(config).load(
        asset_enum,
        data_arm,
        data_version=str(selected["data_version"]),
    )
    result = ExperimentRunner(config).run(
        bundle,
        family,
        seeds=config.training.seeds,
        phase="holdout",
        selection_lock=lock,
        selection_role=role,
    )
    manager.complete_holdout(asset_enum, role, result.version)
    metadata = json.loads((result.registry_path / "metadata.json").read_text(encoding="utf-8"))
    write_model_card(metadata, result.registry_path / "MODEL_CARD.md")
    typer.echo(
        json.dumps(
            {
                "selection_id": lock.selection_id,
                "version": result.version,
                "holdout": result.holdout_metrics,
                "stress": result.stress_metrics,
                "registry": str(result.registry_path),
            },
            indent=2,
            default=str,
        )
    )


@models_app.command("promote")
def promote(
    asset: Annotated[str, typer.Option()],
    version: Annotated[str, typer.Option()],
    slot: Annotated[
        str, typer.Option(help="champion, challenger ou market_fallback.")
    ] = "champion",
    stage: Annotated[str, typer.Option(help="development, canary ou paper.")] = "canary",
    config_path: ConfigOption = None,
) -> None:
    config = _config(config_path)
    pointer = ModelRegistry(config).promote(
        asset=Asset(asset), version=version, slot=slot, stage=RunStage(stage)
    )
    typer.echo(f"Ponteiro promovido: {pointer}")


@models_app.command("publish")
def publish(
    asset: Annotated[str, typer.Option()],
    slot: Annotated[str, typer.Option()] = "champion",
    bucket: Annotated[
        str | None,
        typer.Option(help="Bucket GCS; permite publicar o registry local sem trocar config."),
    ] = None,
    config_path: ConfigOption = None,
) -> None:
    config = _config(config_path)
    if bucket:
        config.runtime.model_bucket = bucket
    uri = ModelRegistry(config).publish_active(Asset(asset), slot)
    typer.echo(uri)


@models_app.command("refit")
def refit(
    asset: Annotated[str, typer.Option()],
    slot: Annotated[
        str,
        typer.Option(help="champion, challenger ou market_fallback."),
    ] = "champion",
    activate: Annotated[
        bool,
        typer.Option(help="Troca o ponteiro paper somente após todas as verificações."),
    ] = False,
    config_path: ConfigOption = None,
) -> None:
    from bottrade.training import ExperimentRunner

    config = _config(config_path)
    asset_enum = Asset(asset)
    registry = ModelRegistry(config)
    parent_directory, parent = registry.resolve(asset_enum, slot)
    bundle = DatasetBuilder(config).load(asset_enum, parent.data_arm)
    result = ExperimentRunner(config).refit(
        bundle,
        parent_directory=parent_directory,
        parent=parent,
        slot=slot,
    )
    metadata = json.loads((result.registry_path / "metadata.json").read_text(encoding="utf-8"))
    write_model_card(metadata, result.registry_path / "MODEL_CARD.md")
    activated = False
    if activate:
        registry.promote(
            asset=asset_enum,
            version=result.version,
            slot=slot,
            stage=RunStage.PAPER,
        )
        activated = True
    typer.echo(
        json.dumps(
            {
                "version": result.version,
                "parent": parent.version,
                "activated": activated,
                "registry": str(result.registry_path),
            },
            indent=2,
        )
    )


@paper_app.command("init")
def paper_init(config_path: ConfigOption = None) -> None:
    config = _config(config_path)
    storage = Storage(config.runtime.database_url)
    storage.initialize(config)
    typer.echo(f"Ledgers inicializados: {', '.join(storage.ledger_names())}")


@paper_app.command("canary-start")
def paper_canary_start(config_path: ConfigOption = None) -> None:
    config = _config(config_path)
    registry = ModelRegistry(config)
    checked: list[str] = []
    active_assets: list[Asset] = []
    for asset in Asset:
        slots, cash_reason = _active_slots_or_cash(config, registry, asset)
        if cash_reason:
            checked.append(f"{asset.value}:cash:{cash_reason}")
            continue
        active_assets.append(asset)
        for slot, metadata in slots:
            if metadata.stage != RunStage.CANARY or metadata.canary_started_at is None:
                raise typer.BadParameter(
                    f"{asset.value}/{slot} ainda não foi promovido para canário"
                )
            checked.append(f"{asset.value}/{slot}:{metadata.version}")
    if not active_assets:
        raise typer.BadParameter(
            "nenhum ativo passou o holdout; não há estratégia para executar no canário"
        )
    storage = Storage(config.runtime.database_url)
    storage.initialize(config)
    if storage.paper_phase_history():
        raise typer.BadParameter("este banco já possui histórico de fase paper")
    pristine = storage.pristine_paper_state(config)
    if not pristine["ok"]:
        raise typer.BadParameter(
            "canário exige ledgers novos: " + "; ".join(pristine["violations"])
        )
    phase = storage.start_paper_phase(
        RunStage.CANARY,
        started_at=utc_now(),
        duration_days=config.paper.canary_days,
        note=";".join(checked),
        active_assets=active_assets,
    )
    typer.echo(json.dumps(phase, indent=2, default=str))


@paper_app.command("canary-complete")
def paper_canary_complete(config_path: ConfigOption = None) -> None:
    config = _config(config_path)
    storage = Storage(config.runtime.database_url)
    storage.initialize(config)
    active = storage.active_paper_phase()
    if active is None or active["phase"] != RunStage.CANARY.value:
        raise typer.BadParameter("não há canário ativo")
    started_at = ensure_utc(active["started_at"])
    elapsed_days = (utc_now() - started_at).total_seconds() / 86_400
    if elapsed_days < config.paper.canary_days:
        raise typer.BadParameter(
            f"canário tem {elapsed_days:.2f} dias; mínimo é {config.paper.canary_days}"
        )
    if storage.critical_events_since(started_at) > 0:
        raise typer.BadParameter("há incidente crítico durante o canário")
    registry = ModelRegistry(config)
    current_slots: dict[Asset, list[tuple[str, ModelMetadata]]] = {}
    current_active_assets: set[Asset] = set()
    for asset in Asset:
        slots, cash_reason = _active_slots_or_cash(config, registry, asset)
        if cash_reason:
            continue
        current_slots[asset] = slots
        current_active_assets.add(asset)
    frozen_active_assets = {Asset(value) for value in active.get("active_assets", [])}
    if current_active_assets != frozen_active_assets:
        raise typer.BadParameter(
            "ativos/modelos atuais diferem do conjunto congelado no início do canário"
        )
    marked: set[tuple[Asset, str]] = set()
    for asset in sorted(frozen_active_assets, key=lambda item: item.value):
        for _, metadata in current_slots[asset]:
            key = (asset, metadata.version)
            if key not in marked:
                registry.mark_canary_passed(asset, metadata.version)
                marked.add(key)
    storage.finish_paper_phase(RunStage.CANARY, ended_at=utc_now())
    typer.echo("Canário concluído e preservado no histórico de auditoria.")


@paper_app.command("run")
def paper_run(
    job: Annotated[str, typer.Argument(help="signal, risk ou daily")],
    config_path: ConfigOption = None,
) -> None:
    config = _config(config_path)
    result = JobRunner(config).run(job)
    typer.echo(json.dumps(result, default=str))


@paper_app.command("official-complete")
def paper_official_complete(config_path: ConfigOption = None) -> None:
    config = _config(config_path)
    storage = Storage(config.runtime.database_url)
    storage.initialize(config)
    active = storage.active_paper_phase()
    if active is None or active["phase"] != RunStage.PAPER.value:
        raise typer.BadParameter("não há paper oficial ativo")
    started_at = ensure_utc(active["started_at"])
    elapsed_days = (utc_now() - started_at).total_seconds() / 86_400
    if elapsed_days < config.paper.official_paper_days:
        raise typer.BadParameter(
            f"paper tem {elapsed_days:.2f} dias; mínimo é {config.paper.official_paper_days}"
        )
    open_positions = [
        f"{ledger}/{position.asset.value}"
        for ledger in storage.ledger_names()
        for position in storage.positions(ledger)
        if position.quantity > 0
    ]
    if open_positions:
        raise typer.BadParameter(
            "paper oficial só fecha após posições zeradas pelos jobs normais: "
            + ", ".join(open_positions)
        )
    reconciliation = storage.reconcile(config)
    if not reconciliation["ok"]:
        raise typer.BadParameter(
            "reconciliação final falhou: " + "; ".join(reconciliation["violations"])
        )
    storage.finish_paper_phase(RunStage.PAPER, ended_at=utc_now())
    typer.echo("Paper oficial concluído; os gates finais já podem ser avaliados.")


@paper_app.command("evaluate")
def paper_evaluate(config_path: ConfigOption = None) -> None:
    config = _config(config_path)
    storage = Storage(config.runtime.database_url)
    storage.initialize(config)
    typer.echo(
        json.dumps(
            FinalGateEvaluator(config, storage).evaluate(),
            indent=2,
            default=str,
        )
    )


@paper_app.command("reconcile")
def paper_reconcile(config_path: ConfigOption = None) -> None:
    config = _config(config_path)
    storage = Storage(config.runtime.database_url)
    storage.initialize(config)
    result = storage.reconcile(config)
    typer.echo(json.dumps(result, indent=2, default=str))
    if not result["ok"]:
        raise typer.Exit(code=2)


@paper_app.command("resume")
def paper_resume(
    ledger: Annotated[str, typer.Option()],
    confirmation: Annotated[str, typer.Option(help="Digite RESUME-PAPER.")],
    config_path: ConfigOption = None,
) -> None:
    if confirmation != "RESUME-PAPER":
        raise typer.BadParameter("confirmação inválida")
    config = _config(config_path)
    storage = Storage(config.runtime.database_url)
    storage.initialize(config)
    status = storage.ledger_status(ledger)
    if status not in {RiskState.CIRCUIT_BREAKER, RiskState.MANUAL_PAUSE}:
        raise typer.BadParameter(
            f"ledger {ledger} está em {status.value}; apenas circuit breaker ou pausa manual "
            "admitem retomada explícita"
        )
    reconciliation = storage.reconcile(config)
    if not reconciliation["ok"]:
        raise typer.BadParameter(
            "retomada recusada por falha de reconciliação: "
            + "; ".join(reconciliation["violations"])
        )
    storage.set_ledger_status(ledger, RiskState.NORMAL)
    typer.echo(f"Ledger {ledger} retomado manualmente em modo paper.")


@paper_app.command("reset-after-canary")
def paper_reset(
    confirmation: Annotated[str, typer.Option(help="Digite RESET-PAPER-AFTER-CANARY.")],
    bucket: Annotated[
        str | None,
        typer.Option(help="Bucket GCS para publicar os ponteiros paper promovidos."),
    ] = None,
    config_path: ConfigOption = None,
) -> None:
    if confirmation != "RESET-PAPER-AFTER-CANARY":
        raise typer.BadParameter("confirmação inválida")
    config = _config(config_path)
    if bucket:
        config.runtime.model_bucket = bucket
    storage = Storage(config.runtime.database_url)
    storage.initialize(config)
    history = storage.paper_phase_history()
    completed_canary = [
        item
        for item in history
        if item["phase"] == RunStage.CANARY.value and item["status"] == "completed"
    ]
    if not completed_canary:
        raise typer.BadParameter("o canário de 14 dias ainda não foi concluído")
    registry = ModelRegistry(config)
    promoted: list[tuple[Asset, str]] = []
    active_assets: list[Asset] = []
    for asset in Asset:
        slots, cash_reason = _active_slots_or_cash(config, registry, asset)
        if cash_reason:
            continue
        active_assets.append(asset)
        for slot, metadata in slots:
            if metadata.canary_passed_at is None:
                raise typer.BadParameter(f"{asset.value}/{slot} não passou no canário")
            registry.promote(
                asset=asset,
                version=metadata.version,
                slot=slot,
                stage=RunStage.PAPER,
            )
            promoted.append((asset, slot))
    canary_assets = set(completed_canary[-1].get("active_assets", []))
    if {asset.value for asset in active_assets} != canary_assets:
        raise typer.BadParameter("ativos do paper diferem dos ativos congelados no canário")
    if bucket:
        for asset, slot in promoted:
            registry.publish_active(asset, slot)
    storage.reset_paper_state(config)
    phase = storage.start_paper_phase(
        RunStage.PAPER,
        started_at=utc_now(),
        duration_days=config.paper.official_paper_days,
        note="official-paper-v1",
        active_assets=active_assets,
    )
    typer.echo(
        "Ledgers resetados, auditoria do canário preservada e paper oficial iniciado: "
        + json.dumps(phase, default=str)
    )


@app.command("report")
def report(
    output: Annotated[Path | None, typer.Option()] = None,
    config_path: ConfigOption = None,
) -> None:
    config = _config(config_path)
    storage = Storage(config.runtime.database_url)
    storage.initialize(config)
    path = ReportGenerator(config, storage).generate(output)
    typer.echo(str(path))


@app.command("doctor")
def doctor(config_path: ConfigOption = None) -> None:
    config = _config(config_path)
    checks: dict[str, str] = {}
    storage = Storage(config.runtime.database_url)
    storage.initialize(config)
    checks["database"] = "ok"
    reconciliation = storage.reconcile(config)
    checks["ledger_reconciliation"] = (
        "ok" if reconciliation["ok"] else "failed:" + ";".join(reconciliation["violations"])
    )
    with PublicHttpClient(config.market.request_timeout_seconds, config.market.max_retries) as http:
        client = BinanceClient(config.market, http=http)
        server = client.server_time()
        divergence = abs((utc_now() - server).total_seconds())
        checks["binance_clock"] = (
            f"ok:{divergence:.2f}s"
            if divergence <= config.runtime.clock_tolerance_seconds
            else f"failed:{divergence:.2f}s"
        )
        for asset in Asset:
            rules = client.exchange_rules(asset.value)
            checks[f"rules_{asset.value}"] = (
                f"ok:step={rules.step_size}:min_notional={rules.min_notional}"
            )
    registry = ModelRegistry(config)
    for asset in Asset:
        for slot in ("champion", "market_fallback", "challenger"):
            try:
                _, metadata = registry.resolve(asset, slot)
                checks[f"model_{asset.value}_{slot}"] = f"ok:{metadata.version}"
            except (FileNotFoundError, ValueError) as exc:
                status = "optional_not_ready" if slot == "challenger" else "not_ready"
                checks[f"model_{asset.value}_{slot}"] = f"{status}:{exc}"
    checks["telegram"] = (
        "configured"
        if (config.runtime.telegram_bot_token and config.runtime.telegram_chat_id)
        else "not_configured"
    )
    checks["dashboard_password"] = (
        "configured" if config.runtime.dashboard_password else "not_configured"
    )
    checks["model_bucket"] = config.runtime.model_bucket or "local_only"
    phase = storage.active_paper_phase()
    checks["paper_phase"] = str(phase["phase"]) if phase else "not_started"
    typer.echo(json.dumps(checks, indent=2))
