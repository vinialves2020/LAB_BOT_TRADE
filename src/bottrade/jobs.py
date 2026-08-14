from __future__ import annotations

import logging

from bottrade.alerts import TelegramAlerter
from bottrade.config import AppConfig, load_config
from bottrade.data.binance import BinanceClient
from bottrade.data.http import PublicHttpClient
from bottrade.domain import Asset, RiskEvent, RiskState, RunStage
from bottrade.logging_utils import configure_logging
from bottrade.paper import PaperTradingEngine
from bottrade.reporting import ReportGenerator
from bottrade.runtime import RuntimeInferenceService
from bottrade.storage import Storage
from bottrade.utils import utc_now

LOGGER = logging.getLogger(__name__)


class JobRunner:
    def __init__(self, config: AppConfig) -> None:
        self.config = config
        self.storage = Storage(config.runtime.database_url)
        self.storage.initialize(config)
        self.paper = PaperTradingEngine(config, self.storage)
        self.alerter = TelegramAlerter(
            config.runtime.telegram_bot_token, config.runtime.telegram_chat_id
        )

    def _record_operational_event(
        self,
        *,
        job: str,
        state: RiskState,
        severity: str,
        message: str,
        metadata: dict | None = None,
    ) -> None:
        for ledger in self.storage.ledger_names():
            self.storage.record_risk_event(
                RiskEvent(
                    ledger=ledger,
                    as_of=utc_now(),
                    state=state,
                    severity=severity,
                    message=message,
                    metadata={"job": job, **(metadata or {})},
                )
            )

    def _record_job_failure(self, job: str, exc: Exception, alert_delivered: bool) -> None:
        lowered = str(exc).lower()
        error_type = type(exc).__name__
        if (
            "ledger reconciliation failed" in lowered
            or "requires an active canary or paper phase" in lowered
        ):
            return
        if any(token in lowered for token in ("model", "onnx", "schema", "checksum")):
            state = RiskState.MODEL_INVALID
            severity = "critical"
        elif any(
            token in lowered
            for token in ("clock", "candle", "stale", "binance", "depth", "operation lock")
        ):
            state = RiskState.DATA_STALE
            severity = "warning"
        else:
            state = RiskState.OPERATIONAL_ERROR
            severity = "critical"
        try:
            self._record_operational_event(
                job=job,
                state=state,
                severity=severity,
                message=f"{job}_job_failed:{error_type}",
                metadata={"alert_delivered": alert_delivered},
            )
        except Exception:
            LOGGER.exception("Could not persist the redacted operational failure event")

    def _record_telegram_failure(self, job: str) -> None:
        try:
            self._record_operational_event(
                job=job,
                state=RiskState.OPERATIONAL_ERROR,
                severity="warning",
                message="telegram_delivery_failed",
            )
        except Exception:
            LOGGER.exception("Could not persist Telegram delivery failure")

    def _require_reconciled(self) -> None:
        reconciliation = self.storage.reconcile(self.config)
        if reconciliation["ok"]:
            return
        message = "ledger reconciliation failed: " + "; ".join(
            reconciliation["violations"]
        )
        for ledger in self.storage.ledger_names():
            self.storage.set_ledger_status(ledger, RiskState.MANUAL_PAUSE)
            self.storage.record_risk_event(
                RiskEvent(
                    ledger=ledger,
                    as_of=utc_now(),
                    state=RiskState.MANUAL_PAUSE,
                    severity="critical",
                    message=message,
                )
            )
        raise RuntimeError(message)

    def _require_active_phase(self) -> set[Asset]:
        phase = self.storage.active_paper_phase()
        if phase is None or phase["phase"] not in {
            RunStage.CANARY.value,
            RunStage.PAPER.value,
        }:
            raise RuntimeError("paper signal/risk mutation requires an active canary or paper phase")
        return {Asset(value) for value in phase.get("active_assets", [])}

    def _market_state(self) -> tuple[dict, dict]:
        with PublicHttpClient(
            timeout_seconds=self.config.market.request_timeout_seconds,
            max_retries=self.config.market.max_retries,
        ) as http:
            client = BinanceClient(self.config.market, http=http)
            server_time = client.server_time()
            divergence = abs((utc_now() - server_time).total_seconds())
            if divergence > self.config.runtime.clock_tolerance_seconds:
                raise RuntimeError(
                    f"local/Binance clock divergence is {divergence:.1f}s; refusing paper mutation"
                )
            quotes = {
                asset: client.market_quote(asset, self.config.paper.quote_depth_levels)
                for asset in Asset
            }
            rules = {asset: client.exchange_rules(asset.value) for asset in Asset}
            return quotes, rules

    def signal(self) -> dict[str, int | str]:
        active_assets = self._require_active_phase()
        self._require_reconciled()
        batch = RuntimeInferenceService(self.config).generate(active_assets=active_assets)
        missing_models = active_assets - set(batch.forecasts)
        if missing_models:
            self._record_operational_event(
                job="signal",
                state=RiskState.MODEL_INVALID,
                severity="critical",
                message="active_model_unavailable",
                metadata={"assets": sorted(asset.value for asset in missing_models)},
            )
        quotes, rules = self._market_state()
        with self.storage.operation_lock():
            result = self.paper.signal_cycle(
                as_of=batch.as_of.to_pydatetime(),
                forecasts=batch.forecasts,
                shadow_forecasts=batch.shadow_forecasts,
                volatilities=batch.volatilities,
                quotes=quotes,
                rules=rules,
            )
        LOGGER.info("Signal job completed: %s", result)
        return result

    def risk(self) -> dict[str, int | str]:
        self._require_active_phase()
        self._require_reconciled()
        quotes, rules = self._market_state()
        now = utc_now().replace(second=0, microsecond=0)
        with self.storage.operation_lock():
            result = self.paper.risk_cycle(as_of=now, quotes=quotes, rules=rules)
        if int(result.get("orders", 0)) > 0:
            delivered = self.alerter.send(
                f"⚠️ BOT_TRADE — risco executou {result['orders']} saída(s) paper."
            )
            if not delivered:
                self._record_telegram_failure("risk")
        LOGGER.info("Risk job completed: %s", result)
        return result

    def daily(self) -> dict[str, str]:
        generator = ReportGenerator(self.config, self.storage)
        path = generator.generate()
        summary = generator.daily_summary()
        self.storage.record_daily_report(
            as_of=utc_now(),
            summary=summary,
            report_markdown=path.read_text(encoding="utf-8"),
        )
        if not self.alerter.send(summary):
            self._record_telegram_failure("daily")
        LOGGER.info("Daily report generated at %s", path)
        return {"status": "completed", "report": str(path)}

    def run(self, job: str) -> dict:
        methods = {"signal": self.signal, "risk": self.risk, "daily": self.daily}
        if job not in methods:
            raise ValueError(f"unknown job: {job}")
        try:
            return methods[job]()
        except Exception as exc:
            delivered = self.alerter.exception(job, exc)
            self._record_job_failure(job, exc, delivered)
            LOGGER.exception("Job failed: %s", job)
            raise


def run_job(job: str, config_path: str | None = None) -> dict:
    config = load_config(config_path)
    configure_logging(config.runtime.log_level, json_logs=True)
    return JobRunner(config).run(job)
