from __future__ import annotations

import logging
import uuid
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import UTC, date, datetime, timedelta
from decimal import Decimal
from pathlib import Path
from typing import Any

from sqlalchemy import (
    JSON,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    UniqueConstraint,
    create_engine,
    inspect,
    select,
    text,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

from bottrade.config import AppConfig
from bottrade.domain import (
    Asset,
    EquitySnapshot,
    Forecast,
    PaperFill,
    PaperOrder,
    PositionSnapshot,
    RiskEvent,
    RiskState,
    RunStage,
)
from bottrade.utils import sha256_bytes, utc_now

LOGGER = logging.getLogger(__name__)
MONEY = Numeric(28, 12)
CYCLE_LEASE = timedelta(minutes=15)


class Base(DeclarativeBase):
    pass


class SchemaVersionRow(Base):
    __tablename__ = "schema_version"
    version: Mapped[int] = mapped_column(Integer, primary_key=True)
    applied_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)


class LedgerRow(Base):
    __tablename__ = "ledger"
    name: Mapped[str] = mapped_column(String(64), primary_key=True)
    initial_cash: Mapped[Decimal] = mapped_column(MONEY)
    cash: Mapped[Decimal] = mapped_column(MONEY)
    peak_equity: Mapped[Decimal] = mapped_column(MONEY)
    day_start_equity: Mapped[Decimal] = mapped_column(MONEY)
    day_start_date: Mapped[date] = mapped_column(Date)
    status: Mapped[str] = mapped_column(String(32), default=RiskState.NORMAL.value)
    stage: Mapped[str] = mapped_column(String(32), default=RunStage.DEVELOPMENT.value)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utc_now, onupdate=utc_now
    )


class PositionRow(Base):
    __tablename__ = "position"
    ledger_name: Mapped[str] = mapped_column(
        ForeignKey("ledger.name", ondelete="CASCADE"), primary_key=True
    )
    asset: Mapped[str] = mapped_column(String(24), primary_key=True)
    quantity: Mapped[Decimal] = mapped_column(MONEY, default=Decimal("0"))
    average_price: Mapped[Decimal] = mapped_column(MONEY, default=Decimal("0"))
    last_price: Mapped[Decimal] = mapped_column(MONEY, default=Decimal("0"))
    realized_pnl: Mapped[Decimal] = mapped_column(MONEY, default=Decimal("0"))
    opened_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utc_now, onupdate=utc_now
    )


class ForecastRow(Base):
    __tablename__ = "forecast"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    asset: Mapped[str] = mapped_column(String(24), index=True)
    as_of: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    horizon_hours: Mapped[int] = mapped_column(Integer)
    expected_return: Mapped[float] = mapped_column(Float)
    threshold_return: Mapped[float] = mapped_column(Float)
    model_family: Mapped[str] = mapped_column(String(32))
    model_version: Mapped[str] = mapped_column(String(160))
    data_version: Mapped[str] = mapped_column(String(64))
    data_arm: Mapped[str] = mapped_column(String(32))
    is_fallback: Mapped[bool] = mapped_column(default=False)
    is_shadow: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    __table_args__ = (
        UniqueConstraint("asset", "as_of", "model_version", name="uq_forecast_cycle_model"),
    )


class PaperOrderRow(Base):
    __tablename__ = "paper_order"
    client_order_id: Mapped[str] = mapped_column(String(64), primary_key=True)
    ledger_name: Mapped[str] = mapped_column(ForeignKey("ledger.name"), index=True)
    asset: Mapped[str] = mapped_column(String(24), index=True)
    as_of: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    side: Mapped[str] = mapped_column(String(8))
    quantity: Mapped[Decimal] = mapped_column(MONEY)
    reference_price: Mapped[Decimal] = mapped_column(MONEY)
    reason: Mapped[str] = mapped_column(String(128))
    status: Mapped[str] = mapped_column(String(24), default="created")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)


class PaperFillRow(Base):
    __tablename__ = "paper_fill"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    client_order_id: Mapped[str] = mapped_column(
        ForeignKey("paper_order.client_order_id"), unique=True
    )
    ledger_name: Mapped[str] = mapped_column(String(64), index=True)
    asset: Mapped[str] = mapped_column(String(24), index=True)
    as_of: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    side: Mapped[str] = mapped_column(String(8))
    quantity: Mapped[Decimal] = mapped_column(MONEY)
    price: Mapped[Decimal] = mapped_column(MONEY)
    fee: Mapped[Decimal] = mapped_column(MONEY)
    bid: Mapped[Decimal] = mapped_column(MONEY, default=Decimal("0"))
    ask: Mapped[Decimal] = mapped_column(MONEY, default=Decimal("0"))
    visible_depth_quantity: Mapped[Decimal] = mapped_column(MONEY, default=Decimal("0"))
    visible_depth_notional: Mapped[Decimal] = mapped_column(MONEY, default=Decimal("0"))
    spread_bps: Mapped[float] = mapped_column(Float)
    impact_bps: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)


class EquityRow(Base):
    __tablename__ = "equity_snapshot"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ledger_name: Mapped[str] = mapped_column(ForeignKey("ledger.name"), index=True)
    as_of: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    cash: Mapped[Decimal] = mapped_column(MONEY)
    positions_value: Mapped[Decimal] = mapped_column(MONEY)
    equity: Mapped[Decimal] = mapped_column(MONEY)
    peak_equity: Mapped[Decimal] = mapped_column(MONEY)
    drawdown: Mapped[float] = mapped_column(Float)
    daily_return: Mapped[float] = mapped_column(Float)
    __table_args__ = (
        UniqueConstraint("ledger_name", "as_of", name="uq_equity_ledger_asof"),
    )


class PositionSnapshotRow(Base):
    __tablename__ = "position_snapshot"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ledger_name: Mapped[str] = mapped_column(ForeignKey("ledger.name"), index=True)
    asset: Mapped[str] = mapped_column(String(24), index=True)
    as_of: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    quantity: Mapped[Decimal] = mapped_column(MONEY)
    average_price: Mapped[Decimal] = mapped_column(MONEY)
    market_price: Mapped[Decimal] = mapped_column(MONEY)
    market_value: Mapped[Decimal] = mapped_column(MONEY)
    realized_pnl: Mapped[Decimal] = mapped_column(MONEY)
    unrealized_pnl: Mapped[Decimal] = mapped_column(MONEY)
    weight: Mapped[float] = mapped_column(Float)
    __table_args__ = (
        UniqueConstraint(
            "ledger_name", "asset", "as_of", name="uq_position_snapshot_ledger_asset_asof"
        ),
    )


class RiskEventRow(Base):
    __tablename__ = "risk_event"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ledger_name: Mapped[str] = mapped_column(ForeignKey("ledger.name"), index=True)
    as_of: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    state: Mapped[str] = mapped_column(String(32))
    severity: Mapped[str] = mapped_column(String(16))
    message: Mapped[str] = mapped_column(Text)
    event_metadata: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)


class ProcessedCycleRow(Base):
    __tablename__ = "processed_cycle"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    job: Mapped[str] = mapped_column(String(32))
    cycle_key: Mapped[str] = mapped_column(String(160))
    status: Mapped[str] = mapped_column(String(16), default="started")
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    error: Mapped[str | None] = mapped_column(Text, nullable=True)
    __table_args__ = (UniqueConstraint("job", "cycle_key", name="uq_job_cycle"),)


class PaperPhaseRow(Base):
    __tablename__ = "paper_phase"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    phase: Mapped[str] = mapped_column(String(32), index=True)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    planned_end_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    ended_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    status: Mapped[str] = mapped_column(String(24), default="active")
    note: Mapped[str] = mapped_column(Text, default="")
    active_assets: Mapped[list[str]] = mapped_column(JSON, default=list)


class DailyReportRow(Base):
    __tablename__ = "daily_report"
    report_date: Mapped[date] = mapped_column(Date, primary_key=True)
    as_of: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    summary: Mapped[str] = mapped_column(Text)
    report_markdown: Mapped[str] = mapped_column(Text)
    sha256: Mapped[str] = mapped_column(String(64))


class OperationLockRow(Base):
    __tablename__ = "operation_lock"
    name: Mapped[str] = mapped_column(String(64), primary_key=True)
    owner: Mapped[str] = mapped_column(String(64))
    acquired_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)


class Storage:
    SCHEMA_VERSION = 8

    def __init__(self, database_url: str) -> None:
        if database_url.startswith("sqlite:///"):
            path = Path(database_url.removeprefix("sqlite:///"))
            path.parent.mkdir(parents=True, exist_ok=True)
        connect_args = {"check_same_thread": False} if database_url.startswith("sqlite") else {}
        self.engine = create_engine(
            database_url,
            future=True,
            pool_pre_ping=True,
            connect_args=connect_args,
        )
        self.sessions = sessionmaker(self.engine, expire_on_commit=False)

    @contextmanager
    def session(self) -> Iterator[Session]:
        session = self.sessions()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def initialize(self, config: AppConfig) -> None:
        Base.metadata.create_all(self.engine)
        existing_fill_columns = {
            column["name"] for column in inspect(self.engine).get_columns("paper_fill")
        }
        additions = {
            "bid": "NUMERIC(28, 12) NOT NULL DEFAULT 0",
            "ask": "NUMERIC(28, 12) NOT NULL DEFAULT 0",
            "visible_depth_quantity": "NUMERIC(28, 12) NOT NULL DEFAULT 0",
            "visible_depth_notional": "NUMERIC(28, 12) NOT NULL DEFAULT 0",
        }
        with self.engine.begin() as connection:
            for column, declaration in additions.items():
                if column not in existing_fill_columns:
                    connection.execute(
                        text(f"ALTER TABLE paper_fill ADD COLUMN {column} {declaration}")
                    )
            existing_forecast_columns = {
                column["name"] for column in inspect(self.engine).get_columns("forecast")
            }
            if "is_shadow" not in existing_forecast_columns:
                connection.execute(
                    text("ALTER TABLE forecast ADD COLUMN is_shadow BOOLEAN NOT NULL DEFAULT 0")
                )
            existing_phase_columns = {
                column["name"] for column in inspect(self.engine).get_columns("paper_phase")
            }
            if "active_assets" not in existing_phase_columns:
                connection.execute(
                    text("ALTER TABLE paper_phase ADD COLUMN active_assets JSON NOT NULL DEFAULT '[]'")
                )
        today = utc_now().date()
        with self.session() as session:
            if session.get(SchemaVersionRow, self.SCHEMA_VERSION) is None:
                session.add(SchemaVersionRow(version=self.SCHEMA_VERSION))
            for ledger_config in config.paper.ledgers:
                ledger = session.get(LedgerRow, ledger_config.name)
                initial = Decimal(str(ledger_config.initial_cash))
                if ledger is None:
                    session.add(
                        LedgerRow(
                            name=ledger_config.name,
                            initial_cash=initial,
                            cash=initial,
                            peak_equity=initial,
                            day_start_equity=initial,
                            day_start_date=today,
                        )
                    )
                for asset in Asset:
                    position = session.get(PositionRow, (ledger_config.name, asset.value))
                    if position is None:
                        session.add(PositionRow(ledger_name=ledger_config.name, asset=asset.value))

    def claim_cycle(self, job: str, cycle_key: str) -> bool:
        with self.session() as session:
            existing = session.scalar(
                select(ProcessedCycleRow).where(
                    ProcessedCycleRow.job == job,
                    ProcessedCycleRow.cycle_key == cycle_key,
                )
            )
            if existing is not None:
                if existing.status == "completed":
                    return False
                if existing.status == "started":
                    started_at = existing.started_at
                    if started_at.tzinfo is None:
                        started_at = started_at.replace(tzinfo=UTC)
                    if utc_now() - started_at < CYCLE_LEASE:
                        return False
                    LOGGER.warning(
                        "Reclaiming abandoned cycle %s/%s after %s",
                        job,
                        cycle_key,
                        CYCLE_LEASE,
                    )
                existing.status = "started"
                existing.started_at = utc_now()
                existing.finished_at = None
                existing.error = None
                return True
            session.add(ProcessedCycleRow(job=job, cycle_key=cycle_key))
            try:
                session.flush()
            except IntegrityError:
                session.rollback()
                return False
            return True

    def finish_cycle(self, job: str, cycle_key: str, *, error: str | None = None) -> None:
        with self.session() as session:
            row = session.scalar(
                select(ProcessedCycleRow).where(
                    ProcessedCycleRow.job == job,
                    ProcessedCycleRow.cycle_key == cycle_key,
                )
            )
            if row is None:
                raise KeyError(f"cycle was not claimed: {job}/{cycle_key}")
            row.status = "failed" if error else "completed"
            row.finished_at = utc_now()
            row.error = error

    def ledger_names(self) -> list[str]:
        with self.session() as session:
            return list(session.scalars(select(LedgerRow.name).order_by(LedgerRow.name)))

    def ledger_status(self, name: str) -> RiskState:
        with self.session() as session:
            ledger = session.get(LedgerRow, name)
            if ledger is None:
                raise KeyError(name)
            return RiskState(ledger.status)

    def set_ledger_status(self, name: str, state: RiskState) -> None:
        with self.session() as session:
            ledger = session.get(LedgerRow, name)
            if ledger is None:
                raise KeyError(name)
            ledger.status = state.value
            ledger.updated_at = utc_now()

    def set_stage(self, name: str, stage: RunStage) -> None:
        with self.session() as session:
            ledger = session.get(LedgerRow, name)
            if ledger is None:
                raise KeyError(name)
            ledger.stage = stage.value

    @contextmanager
    def operation_lock(
        self,
        name: str = "paper_mutation",
        *,
        lease: timedelta = timedelta(minutes=5),
    ) -> Iterator[None]:
        owner = uuid.uuid4().hex
        now = utc_now()
        acquired = False
        try:
            with self.session() as session:
                row = session.get(OperationLockRow, name, with_for_update=True)
                if row is None:
                    session.add(
                        OperationLockRow(
                            name=name,
                            owner=owner,
                            acquired_at=now,
                            expires_at=now + lease,
                        )
                    )
                    try:
                        session.flush()
                    except IntegrityError:
                        session.rollback()
                        raise RuntimeError(
                            "another paper mutation owns the operation lock"
                        ) from None
                    acquired = True
                else:
                    expires_at = row.expires_at
                    if expires_at.tzinfo is None:
                        expires_at = expires_at.replace(tzinfo=UTC)
                    if row.owner and expires_at > now:
                        raise RuntimeError("another paper mutation owns the operation lock")
                    row.owner = owner
                    row.acquired_at = now
                    row.expires_at = now + lease
                    acquired = True
            yield
        finally:
            if acquired:
                with self.session() as session:
                    row = session.get(OperationLockRow, name, with_for_update=True)
                    if row is not None and row.owner == owner:
                        row.owner = ""
                        row.expires_at = utc_now()

    def start_paper_phase(
        self,
        stage: RunStage,
        *,
        started_at: datetime,
        duration_days: int,
        note: str = "",
        active_assets: list[Asset] | None = None,
    ) -> dict[str, Any]:
        if stage not in {RunStage.CANARY, RunStage.PAPER}:
            raise ValueError("paper program phase must be canary or paper")
        started = started_at.astimezone(UTC)
        with self.session() as session:
            active = session.scalar(
                select(PaperPhaseRow)
                .where(PaperPhaseRow.status == "active")
                .order_by(PaperPhaseRow.started_at.desc())
            )
            if active is not None:
                raise ValueError(f"paper phase {active.phase} is already active")
            planned_end = started + timedelta(days=duration_days)
            session.add(
                PaperPhaseRow(
                    phase=stage.value,
                    started_at=started,
                    planned_end_at=planned_end,
                    status="active",
                    note=note,
                    active_assets=[asset.value for asset in (active_assets or [])],
                )
            )
            for ledger in session.scalars(select(LedgerRow)):
                ledger.stage = stage.value
            return {
                "phase": stage.value,
                "started_at": started,
                "planned_end_at": planned_end,
                "status": "active",
                "active_assets": [asset.value for asset in (active_assets or [])],
            }

    def finish_paper_phase(self, stage: RunStage, *, ended_at: datetime) -> None:
        with self.session() as session:
            active = session.scalar(
                select(PaperPhaseRow)
                .where(
                    PaperPhaseRow.status == "active",
                    PaperPhaseRow.phase == stage.value,
                )
                .order_by(PaperPhaseRow.started_at.desc())
            )
            if active is None:
                raise ValueError(f"no active {stage.value} phase")
            active.status = "completed"
            active.ended_at = ended_at.astimezone(UTC)

    def paper_phase_history(self) -> list[dict[str, Any]]:
        with self.session() as session:
            rows = list(
                session.scalars(select(PaperPhaseRow).order_by(PaperPhaseRow.started_at))
            )
            return [
                {
                    "phase": row.phase,
                    "started_at": row.started_at,
                    "planned_end_at": row.planned_end_at,
                    "ended_at": row.ended_at,
                    "status": row.status,
                    "note": row.note,
                    "active_assets": list(row.active_assets or []),
                }
                for row in rows
            ]

    def active_paper_phase(self) -> dict[str, Any] | None:
        history = self.paper_phase_history()
        active = [item for item in history if item["status"] == "active"]
        return active[-1] if active else None

    def pristine_paper_state(self, config: AppConfig) -> dict[str, Any]:
        violations: list[str] = []
        configured = {
            item.name: Decimal(str(item.initial_cash)) for item in config.paper.ledgers
        }
        with self.session() as session:
            for name, initial in configured.items():
                ledger = session.get(LedgerRow, name)
                if ledger is None:
                    violations.append(f"missing_ledger:{name}")
                elif ledger.cash != initial:
                    violations.append(f"cash_not_initial:{name}")
                elif (
                    ledger.peak_equity != initial
                    or ledger.status != RiskState.NORMAL.value
                ):
                    violations.append(f"ledger_state_not_initial:{name}")
            for position in session.scalars(select(PositionRow)):
                if (
                    position.quantity != 0
                    or position.average_price != 0
                    or position.realized_pnl != 0
                ):
                    violations.append(
                        f"open_position:{position.ledger_name}:{position.asset}"
                    )
            if session.scalar(select(PaperOrderRow.id).limit(1)) is not None:
                violations.append("paper_orders_already_exist")
            if session.scalar(select(PaperFillRow.id).limit(1)) is not None:
                violations.append("paper_fills_already_exist")
        return {"ok": not violations, "violations": violations}

    def reconcile(self, config: AppConfig) -> dict[str, Any]:
        """Recompute cash and quantities from immutable fills for the latest paper phase."""

        history = self.paper_phase_history()
        phase_start = history[-1]["started_at"] if history else None
        tolerance = Decimal("0.00000001")
        violations: list[str] = []
        configured = {
            item.name: Decimal(str(item.initial_cash)) for item in config.paper.ledgers
        }
        with self.session() as session:
            fills_query = select(PaperFillRow).order_by(PaperFillRow.as_of, PaperFillRow.id)
            if phase_start is not None:
                fills_query = fills_query.where(PaperFillRow.as_of >= phase_start)
            fills = list(session.scalars(fills_query))
            expected_cash = dict(configured)
            expected_quantity = {
                (ledger, asset.value): Decimal("0")
                for ledger in configured
                for asset in Asset
            }
            expected_average = dict.fromkeys(expected_quantity, Decimal("0"))
            expected_realized = dict.fromkeys(expected_quantity, Decimal("0"))
            for fill in fills:
                key = (fill.ledger_name, fill.asset)
                if fill.ledger_name not in expected_cash or key not in expected_quantity:
                    violations.append(
                        f"fill_outside_configured_universe:{fill.client_order_id}"
                    )
                    continue
                notional = fill.quantity * fill.price
                if fill.side == "BUY":
                    expected_cash[fill.ledger_name] -= notional + fill.fee
                    old_quantity = expected_quantity[key]
                    new_quantity = old_quantity + fill.quantity
                    expected_average[key] = (
                        old_quantity * expected_average[key] + notional + fill.fee
                    ) / new_quantity
                    expected_quantity[key] = new_quantity
                elif fill.side == "SELL":
                    if fill.quantity > expected_quantity[key] + tolerance:
                        violations.append(f"oversell_fill:{fill.client_order_id}")
                    expected_cash[fill.ledger_name] += notional - fill.fee
                    expected_realized[key] += (
                        fill.quantity * (fill.price - expected_average[key]) - fill.fee
                    )
                    expected_quantity[key] -= fill.quantity
                    if abs(expected_quantity[key]) <= tolerance:
                        expected_quantity[key] = Decimal("0")
                        expected_average[key] = Decimal("0")
                else:
                    violations.append(f"invalid_fill_side:{fill.client_order_id}:{fill.side}")
            for ledger_name, expected in expected_cash.items():
                ledger = session.get(LedgerRow, ledger_name)
                if ledger is None:
                    violations.append(f"missing_ledger:{ledger_name}")
                    continue
                if abs(ledger.cash - expected) > tolerance:
                    violations.append(
                        f"cash_mismatch:{ledger_name}:stored={ledger.cash}:expected={expected}"
                    )
                for asset in Asset:
                    position = session.get(PositionRow, (ledger_name, asset.value))
                    expected_qty = expected_quantity[(ledger_name, asset.value)]
                    if position is None:
                        violations.append(f"missing_position:{ledger_name}:{asset.value}")
                    elif abs(position.quantity - expected_qty) > tolerance:
                        violations.append(
                            f"quantity_mismatch:{ledger_name}:{asset.value}:"
                            f"stored={position.quantity}:expected={expected_qty}"
                        )
                    elif abs(position.average_price - expected_average[(ledger_name, asset.value)]) > tolerance:
                        violations.append(
                            f"average_price_mismatch:{ledger_name}:{asset.value}:"
                            f"stored={position.average_price}:"
                            f"expected={expected_average[(ledger_name, asset.value)]}"
                        )
                    if (
                        position is not None
                        and abs(
                            position.realized_pnl
                            - expected_realized[(ledger_name, asset.value)]
                        )
                        > tolerance
                    ):
                        violations.append(
                            f"realized_pnl_mismatch:{ledger_name}:{asset.value}:"
                            f"stored={position.realized_pnl}:"
                            f"expected={expected_realized[(ledger_name, asset.value)]}"
                        )
                latest_equity = session.scalar(
                    select(EquityRow)
                    .where(EquityRow.ledger_name == ledger_name)
                    .order_by(EquityRow.as_of.desc())
                    .limit(1)
                )
                if (
                    latest_equity is not None
                    and abs(
                        latest_equity.cash
                        + latest_equity.positions_value
                        - latest_equity.equity
                    )
                    > tolerance
                ):
                    violations.append(f"equity_identity_mismatch:{ledger_name}")
            orders = set(session.scalars(select(PaperOrderRow.client_order_id)))
            fill_orders = set(session.scalars(select(PaperFillRow.client_order_id)))
            orphaned = fill_orders - orders
            unfilled = orders - fill_orders
            violations.extend(f"orphan_fill:{value}" for value in sorted(orphaned))
            violations.extend(f"unfilled_order:{value}" for value in sorted(unfilled))
        return {
            "ok": not violations,
            "phase_started_at": phase_start,
            "fills_checked": len(fills),
            "violations": violations,
        }

    def record_forecast(self, forecast: Forecast) -> None:
        with self.session() as session:
            row = ForecastRow(
                asset=forecast.asset.value,
                as_of=forecast.as_of,
                horizon_hours=forecast.horizon_hours,
                expected_return=forecast.expected_return,
                threshold_return=forecast.threshold_return,
                model_family=forecast.model_family.value,
                model_version=forecast.model_version,
                data_version=forecast.data_version,
                data_arm=forecast.data_arm.value,
                is_fallback=forecast.is_fallback,
                is_shadow=forecast.is_shadow,
            )
            session.add(row)
            try:
                session.flush()
            except IntegrityError:
                session.rollback()

    def positions(self, ledger_name: str, as_of: datetime | None = None) -> list[PositionSnapshot]:
        timestamp = as_of or utc_now()
        with self.session() as session:
            ledger = session.get(LedgerRow, ledger_name)
            if ledger is None:
                raise KeyError(ledger_name)
            rows = list(
                session.scalars(
                    select(PositionRow).where(PositionRow.ledger_name == ledger_name)
                )
            )
            positions_value = sum((row.quantity * row.last_price for row in rows), Decimal("0"))
            equity = ledger.cash + positions_value
            snapshots: list[PositionSnapshot] = []
            for row in rows:
                value = row.quantity * row.last_price
                unrealized = row.quantity * (row.last_price - row.average_price)
                snapshots.append(
                    PositionSnapshot(
                        ledger=ledger_name,
                        asset=Asset(row.asset),
                        as_of=timestamp,
                        quantity=row.quantity,
                        average_price=row.average_price,
                        market_price=row.last_price,
                        market_value=value,
                        unrealized_pnl=unrealized,
                        weight=float(value / equity) if equity > 0 else 0.0,
                        opened_at=row.opened_at,
                    )
                )
            return snapshots

    @staticmethod
    def _validate_order_fill(order: PaperOrder, fill: PaperFill) -> None:
        if order.client_order_id != fill.client_order_id:
            raise ValueError("order and fill identifiers differ")
        if order.quantity != fill.quantity or order.side != fill.side:
            raise ValueError("fill does not match order")

    @staticmethod
    def _apply_order_fill_in_session(
        session: Session, order: PaperOrder, fill: PaperFill
    ) -> None:
        ledger = session.get(LedgerRow, order.ledger)
        position = session.get(PositionRow, (order.ledger, order.asset.value))
        if ledger is None or position is None:
            raise KeyError(f"ledger/position missing: {order.ledger}/{order.asset}")
        notional = fill.quantity * fill.price
        if fill.side == "BUY":
            total = notional + fill.fee
            if total > ledger.cash:
                raise ValueError("paper ledger has insufficient cash")
            old_cost = position.quantity * position.average_price
            new_quantity = position.quantity + fill.quantity
            position.average_price = (
                (old_cost + notional + fill.fee) / new_quantity
                if new_quantity > 0
                else Decimal("0")
            )
            position.quantity = new_quantity
            position.opened_at = position.opened_at or fill.as_of
            ledger.cash -= total
        elif fill.side == "SELL":
            if fill.quantity > position.quantity:
                raise ValueError("paper sell exceeds current position")
            ledger.cash += notional - fill.fee
            position.realized_pnl += (
                fill.quantity * (fill.price - position.average_price) - fill.fee
            )
            position.quantity -= fill.quantity
            if position.quantity == 0:
                position.average_price = Decimal("0")
                position.opened_at = None
        else:
            raise ValueError(f"unsupported paper side: {fill.side}")
        position.last_price = fill.price
        session.add(
            PaperOrderRow(
                client_order_id=order.client_order_id,
                ledger_name=order.ledger,
                asset=order.asset.value,
                as_of=order.as_of,
                side=order.side,
                quantity=order.quantity,
                reference_price=order.reference_price,
                reason=order.reason,
                status="filled",
            )
        )
        session.flush()
        session.add(
            PaperFillRow(
                client_order_id=fill.client_order_id,
                ledger_name=fill.ledger,
                asset=fill.asset.value,
                as_of=fill.as_of,
                side=fill.side,
                quantity=fill.quantity,
                price=fill.price,
                fee=fill.fee,
                bid=fill.bid,
                ask=fill.ask,
                visible_depth_quantity=fill.visible_depth_quantity,
                visible_depth_notional=fill.visible_depth_notional,
                spread_bps=fill.spread_bps,
                impact_bps=fill.impact_bps,
            )
        )
        ledger.updated_at = utc_now()

    def apply_order_fill(self, order: PaperOrder, fill: PaperFill) -> bool:
        self._validate_order_fill(order, fill)
        with self.session() as session:
            existing_fill = session.scalar(
                select(PaperFillRow).where(
                    PaperFillRow.client_order_id == fill.client_order_id
                )
            )
            if existing_fill is not None:
                return False
            self._apply_order_fill_in_session(session, order, fill)
            return True

    def apply_order_fills(
        self, order_fills: list[tuple[PaperOrder, PaperFill]]
    ) -> int:
        """Apply one paper cycle atomically across ledgers.

        Existing complete batches are treated as idempotent. A partially existing batch is
        rejected because it signals an invariant violation that needs reconciliation.
        """

        if not order_fills:
            return 0
        identifiers = [order.client_order_id for order, _ in order_fills]
        if len(identifiers) != len(set(identifiers)):
            raise ValueError("duplicate client order identifiers inside one batch")
        for order, fill in order_fills:
            self._validate_order_fill(order, fill)
        with self.session() as session:
            existing = set(
                session.scalars(
                    select(PaperFillRow.client_order_id).where(
                        PaperFillRow.client_order_id.in_(identifiers)
                    )
                )
            )
            if len(existing) == len(identifiers):
                return 0
            if existing:
                raise RuntimeError("partially applied paper batch requires reconciliation")
            for order, fill in sorted(
                order_fills, key=lambda pair: 0 if pair[0].side == "SELL" else 1
            ):
                self._apply_order_fill_in_session(session, order, fill)
            return len(order_fills)

    def equity_snapshot(
        self,
        ledger_name: str,
        as_of: datetime,
        prices: dict[Asset, Decimal],
    ) -> EquitySnapshot:
        as_of_utc = as_of.astimezone(UTC)
        with self.session() as session:
            ledger = session.get(LedgerRow, ledger_name)
            if ledger is None:
                raise KeyError(ledger_name)
            rows = list(
                session.scalars(
                    select(PositionRow).where(PositionRow.ledger_name == ledger_name)
                )
            )
            for row in rows:
                price = prices.get(Asset(row.asset))
                if price is not None:
                    row.last_price = price
            positions_value = sum((row.quantity * row.last_price for row in rows), Decimal("0"))
            equity = ledger.cash + positions_value
            if as_of_utc.date() != ledger.day_start_date:
                ledger.day_start_date = as_of_utc.date()
                ledger.day_start_equity = equity
                if ledger.status == RiskState.DAILY_STOP.value:
                    ledger.status = RiskState.NORMAL.value
            ledger.peak_equity = max(ledger.peak_equity, equity)
            drawdown = (
                float((ledger.peak_equity - equity) / ledger.peak_equity)
                if ledger.peak_equity > 0
                else 0.0
            )
            daily_return = (
                float(equity / ledger.day_start_equity - 1)
                if ledger.day_start_equity > 0
                else 0.0
            )
            snapshot = EquitySnapshot(
                ledger=ledger_name,
                as_of=as_of_utc,
                cash=ledger.cash,
                positions_value=positions_value,
                equity=equity,
                peak_equity=ledger.peak_equity,
                drawdown=drawdown,
                daily_return=daily_return,
            )
            existing = session.scalar(
                select(EquityRow).where(
                    EquityRow.ledger_name == ledger_name,
                    EquityRow.as_of == as_of_utc,
                )
            )
            if existing is None:
                session.add(
                    EquityRow(
                        ledger_name=ledger_name,
                        as_of=as_of_utc,
                        cash=snapshot.cash,
                        positions_value=snapshot.positions_value,
                        equity=snapshot.equity,
                        peak_equity=snapshot.peak_equity,
                        drawdown=snapshot.drawdown,
                        daily_return=snapshot.daily_return,
                    )
                )
            else:
                existing.cash = snapshot.cash
                existing.positions_value = snapshot.positions_value
                existing.equity = snapshot.equity
                existing.peak_equity = snapshot.peak_equity
                existing.drawdown = snapshot.drawdown
                existing.daily_return = snapshot.daily_return
            for row in rows:
                value = row.quantity * row.last_price
                unrealized = row.quantity * (row.last_price - row.average_price)
                weight = float(value / equity) if equity > 0 else 0.0
                position_snapshot = session.scalar(
                    select(PositionSnapshotRow).where(
                        PositionSnapshotRow.ledger_name == ledger_name,
                        PositionSnapshotRow.asset == row.asset,
                        PositionSnapshotRow.as_of == as_of_utc,
                    )
                )
                if position_snapshot is None:
                    session.add(
                        PositionSnapshotRow(
                            ledger_name=ledger_name,
                            asset=row.asset,
                            as_of=as_of_utc,
                            quantity=row.quantity,
                            average_price=row.average_price,
                            market_price=row.last_price,
                            market_value=value,
                            realized_pnl=row.realized_pnl,
                            unrealized_pnl=unrealized,
                            weight=weight,
                        )
                    )
                else:
                    position_snapshot.quantity = row.quantity
                    position_snapshot.average_price = row.average_price
                    position_snapshot.market_price = row.last_price
                    position_snapshot.market_value = value
                    position_snapshot.realized_pnl = row.realized_pnl
                    position_snapshot.unrealized_pnl = unrealized
                    position_snapshot.weight = weight
            return snapshot

    def record_risk_event(self, event: RiskEvent) -> None:
        with self.session() as session:
            session.add(
                RiskEventRow(
                    ledger_name=event.ledger,
                    as_of=event.as_of,
                    state=event.state.value,
                    severity=event.severity,
                    message=event.message,
                    event_metadata=event.metadata,
                )
            )

    def recent_forecasts(self, limit: int = 500) -> list[dict[str, Any]]:
        with self.session() as session:
            rows = list(
                session.scalars(
                    select(ForecastRow).order_by(ForecastRow.as_of.desc()).limit(limit)
                )
            )
            return [
                {
                    "asset": row.asset,
                    "as_of": row.as_of,
                    "horizon_hours": row.horizon_hours,
                    "expected_return": row.expected_return,
                    "threshold_return": row.threshold_return,
                    "model_family": row.model_family,
                    "model_version": row.model_version,
                    "data_version": row.data_version,
                    "data_arm": row.data_arm,
                    "is_fallback": row.is_fallback,
                    "is_shadow": row.is_shadow,
                }
                for row in reversed(rows)
            ]

    def record_daily_report(
        self,
        *,
        as_of: datetime,
        summary: str,
        report_markdown: str,
    ) -> None:
        timestamp = as_of.astimezone(UTC)
        checksum = sha256_bytes(report_markdown.encode("utf-8"))
        with self.session() as session:
            row = session.get(DailyReportRow, timestamp.date())
            if row is None:
                session.add(
                    DailyReportRow(
                        report_date=timestamp.date(),
                        as_of=timestamp,
                        summary=summary,
                        report_markdown=report_markdown,
                        sha256=checksum,
                    )
                )
            else:
                row.as_of = timestamp
                row.summary = summary
                row.report_markdown = report_markdown
                row.sha256 = checksum

    def recent_daily_reports(self, limit: int = 30) -> list[dict[str, Any]]:
        with self.session() as session:
            rows = list(
                session.scalars(
                    select(DailyReportRow)
                    .order_by(DailyReportRow.as_of.desc())
                    .limit(limit)
                )
            )
            return [
                {
                    "report_date": row.report_date,
                    "as_of": row.as_of,
                    "summary": row.summary,
                    "report_markdown": row.report_markdown,
                    "sha256": row.sha256,
                }
                for row in rows
            ]

    def recent_equity(self, limit: int = 10_000) -> list[dict[str, Any]]:
        with self.session() as session:
            rows = list(
                session.scalars(select(EquityRow).order_by(EquityRow.as_of.desc()).limit(limit))
            )
            return [
                {
                    "ledger": row.ledger_name,
                    "as_of": row.as_of,
                    "cash": float(row.cash),
                    "positions_value": float(row.positions_value),
                    "equity": float(row.equity),
                    "drawdown": row.drawdown,
                    "daily_return": row.daily_return,
                }
                for row in reversed(rows)
            ]

    def recent_orders(self, limit: int = 200) -> list[dict[str, Any]]:
        with self.session() as session:
            rows = list(
                session.scalars(
                    select(PaperOrderRow).order_by(PaperOrderRow.as_of.desc()).limit(limit)
                )
            )
            return [
                {
                    "client_order_id": row.client_order_id,
                    "ledger": row.ledger_name,
                    "asset": row.asset,
                    "as_of": row.as_of,
                    "side": row.side,
                    "quantity": float(row.quantity),
                    "reference_price": float(row.reference_price),
                    "reason": row.reason,
                    "status": row.status,
                }
                for row in rows
            ]

    def recent_fills(self, limit: int = 200) -> list[dict[str, Any]]:
        with self.session() as session:
            rows = list(
                session.scalars(
                    select(PaperFillRow).order_by(PaperFillRow.as_of.desc()).limit(limit)
                )
            )
            return [
                {
                    "client_order_id": row.client_order_id,
                    "ledger": row.ledger_name,
                    "asset": row.asset,
                    "as_of": row.as_of,
                    "side": row.side,
                    "quantity": float(row.quantity),
                    "price": float(row.price),
                    "fee": float(row.fee),
                    "bid": float(row.bid),
                    "ask": float(row.ask),
                    "visible_depth_quantity": float(row.visible_depth_quantity),
                    "visible_depth_notional": float(row.visible_depth_notional),
                    "spread_bps": row.spread_bps,
                    "impact_bps": row.impact_bps,
                }
                for row in rows
            ]

    def recent_position_snapshots(self, limit: int = 1_000_000) -> list[dict[str, Any]]:
        with self.session() as session:
            rows = list(
                session.scalars(
                    select(PositionSnapshotRow)
                    .order_by(PositionSnapshotRow.as_of.desc())
                    .limit(limit)
                )
            )
            return [
                {
                    "ledger": row.ledger_name,
                    "asset": row.asset,
                    "as_of": row.as_of,
                    "quantity": float(row.quantity),
                    "average_price": float(row.average_price),
                    "market_price": float(row.market_price),
                    "market_value": float(row.market_value),
                    "realized_pnl": float(row.realized_pnl),
                    "unrealized_pnl": float(row.unrealized_pnl),
                    "weight": row.weight,
                }
                for row in reversed(rows)
            ]

    def recent_risk_events(self, limit: int = 200) -> list[dict[str, Any]]:
        with self.session() as session:
            rows = list(
                session.scalars(
                    select(RiskEventRow).order_by(RiskEventRow.as_of.desc()).limit(limit)
                )
            )
            return [
                {
                    "ledger": row.ledger_name,
                    "as_of": row.as_of,
                    "state": row.state,
                    "severity": row.severity,
                    "message": row.message,
                    "metadata": row.event_metadata,
                }
                for row in rows
            ]

    def critical_events_since(self, since: datetime) -> int:
        with self.session() as session:
            rows = list(
                session.scalars(
                    select(RiskEventRow.id).where(
                        RiskEventRow.as_of >= since,
                        RiskEventRow.severity == "critical",
                    )
                )
            )
            return len(rows)

    def reset_paper_state(self, config: AppConfig) -> None:
        """Reset balances after canary while preserving the immutable audit trail."""
        with self.session() as session:
            today = utc_now().date()
            configured = {item.name: Decimal(str(item.initial_cash)) for item in config.paper.ledgers}
            for ledger in session.scalars(select(LedgerRow)):
                initial = configured[ledger.name]
                ledger.initial_cash = initial
                ledger.cash = initial
                ledger.peak_equity = initial
                ledger.day_start_equity = initial
                ledger.day_start_date = today
                ledger.status = RiskState.NORMAL.value
                ledger.updated_at = utc_now()
            for position in session.scalars(select(PositionRow)):
                position.quantity = Decimal("0")
                position.average_price = Decimal("0")
                position.last_price = Decimal("0")
                position.realized_pnl = Decimal("0")
                position.opened_at = None
