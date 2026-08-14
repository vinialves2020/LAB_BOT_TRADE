from __future__ import annotations

import hmac

import pandas as pd
import plotly.express as px
import streamlit as st

from bottrade.config import load_config
from bottrade.storage import Storage

st.set_page_config(page_title="BOT_TRADE Paper", page_icon="📈", layout="wide")
config = load_config()


def authenticated() -> bool:
    expected = config.runtime.dashboard_password
    if not expected:
        st.error("Dashboard bloqueado: configure BOTTRADE_DASHBOARD_PASSWORD.")
        return False
    if st.session_state.get("authenticated"):
        return True
    st.title("BOT_TRADE — acesso privado")
    supplied = st.text_input("Senha", type="password")
    if supplied and hmac.compare_digest(supplied, expected):
        st.session_state["authenticated"] = True
        st.rerun()
    elif supplied:
        st.error("Senha inválida")
    return False


if not authenticated():
    st.stop()

storage = Storage(config.runtime.database_url)
storage.initialize(config)
st.title("📈 BOT_TRADE — Paper Trading")
st.caption("Spot long/flat · BTC/ETH/SOL · nenhum envio de ordem real")

equity = pd.DataFrame(storage.recent_equity())
forecasts = pd.DataFrame(storage.recent_forecasts())
positions = pd.DataFrame(storage.recent_position_snapshots(limit=2_000))
orders = pd.DataFrame(storage.recent_orders())
fills = pd.DataFrame(storage.recent_fills())
risk = pd.DataFrame(storage.recent_risk_events())
daily_reports = storage.recent_daily_reports(limit=7)
phase = storage.active_paper_phase()
reconciliation = storage.reconcile(config)

phase_name = phase["phase"] if phase else "não iniciado"
active_asset_names = ", ".join(phase.get("active_assets", [])) if phase else "nenhum"
st.caption(f"Fase operacional: {phase_name} · ativos habilitados: {active_asset_names or 'nenhum'}")
if reconciliation["ok"]:
    st.success("Ledgers reconciliados", icon="✅")
else:
    st.error("Reconciliação falhou: " + "; ".join(reconciliation["violations"]))

if equity.empty:
    st.info("Ainda não há snapshots. Inicialize e execute o primeiro job paper.")
else:
    latest = equity.sort_values("as_of").groupby("ledger", as_index=False).tail(1)
    columns = st.columns(len(latest))
    for column, row in zip(columns, latest.itertuples(index=False), strict=False):
        column.metric(
            row.ledger,
            f"{row.equity:,.2f} USDT",
            f"{row.daily_return * 100:.2f}% hoje",
        )
        column.caption(f"Drawdown: {row.drawdown * 100:.2f}%")
    figure = px.line(
        equity,
        x="as_of",
        y="equity",
        color="ledger",
        title="Patrimônio paper",
    )
    st.plotly_chart(figure, use_container_width=True)

left, right = st.columns(2)
with left:
    st.subheader("Previsões mais recentes")
    if forecasts.empty:
        st.info("Ainda não há previsões.")
    else:
        latest_forecasts = (
            forecasts.sort_values("as_of")
            .groupby(["asset", "is_shadow"], as_index=False)
            .tail(1)
        )
        st.dataframe(latest_forecasts, use_container_width=True, hide_index=True)
with right:
    st.subheader("Posições mais recentes")
    if positions.empty:
        st.info("Ainda não há snapshots de posição.")
    else:
        latest_positions = (
            positions.sort_values("as_of")
            .groupby(["ledger", "asset"], as_index=False)
            .tail(1)
        )
        st.dataframe(latest_positions, use_container_width=True, hide_index=True)

left, right = st.columns(2)
with left:
    st.subheader("Ordens paper recentes")
    st.dataframe(orders, use_container_width=True, hide_index=True)
with right:
    st.subheader("Eventos de risco")
    st.dataframe(risk, use_container_width=True, hide_index=True)

st.subheader("Fills hipotéticos e profundidade observada")
st.dataframe(fills, use_container_width=True, hide_index=True)

if daily_reports:
    latest_report = daily_reports[0]
    with st.expander(
        f"Último relatório diário · {latest_report['report_date']} · {latest_report['sha256'][:12]}"
    ):
        st.markdown(latest_report["report_markdown"])

st.caption("Horários em UTC. Conversões para BRL são apenas informativas e não entram nos sinais.")
