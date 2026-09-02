from __future__ import annotations

import contextlib
from dataclasses import dataclass
from decimal import Decimal
from typing import Any

import numpy as np
import pandas as pd

from bottrade.config import AppConfig
from bottrade.data.binance import BinanceClient
from bottrade.data.http import PublicHttpClient
from bottrade.domain import Asset
from bottrade.storage import Storage
from bottrade.utils import utc_now
from bottrade.v4.config import V4Config
from bottrade.v4.features import build_direct_dataset, build_features, load_raw_market
from bottrade.v5.config import V5Config
from bottrade.v5.models.xgboost_ref import create_xgboost_reference


@dataclass
class PaperSignal:
    asset: str
    prediction_bps: float
    effective_bps: float
    threshold_bps: float
    signal: str  # "BUY", "SELL", "HOLD", "CASH"
    reason: str
    current_price: float
    ewma_volatility_1h: float


class PaperTradingV5:
    """Motor oficial de Paper Trading V5 com dados em tempo real da Binance."""

    def __init__(
        self,
        v5_config: V5Config,
        app_config: AppConfig,
        ledger_name: str = "paper_1000",
    ) -> None:
        self.v5_config = v5_config
        self.app_config = app_config
        self.ledger_name = ledger_name
        self.storage = Storage(app_config.runtime.database_url)
        self.storage.initialize(app_config)
        self.http_client = PublicHttpClient()
        self.binance_client = BinanceClient(app_config.market, self.http_client)
        self.models: dict[str, Any] = {}
        self.feature_columns: dict[str, list[str]] = {}

        import os

        from bottrade.alerts import TelegramAlerter
        token = os.environ.get("TELEGRAM_BOT_TOKEN") or app_config.runtime.telegram_bot_token
        chat_id = os.environ.get("TELEGRAM_CHAT_ID") or app_config.runtime.telegram_chat_id
        self.alerter = TelegramAlerter(token or "", chat_id or "")

    def _fetch_market_frames(self, live: bool = True) -> dict[str, pd.DataFrame]:
        """Obtém os candles horários mais recentes de BTC, ETH e SOL."""
        market: dict[str, pd.DataFrame] = {}
        if live:
            try:
                for asset in Asset:
                    df = self.binance_client.fetch_recent_klines(asset.value, limit=350, interval="1h")
                    market[asset.value] = df
                return market
            except Exception:
                pass  # Fallback para dados locais se offline
        for asset in Asset:
            market[asset.value] = load_raw_market(self.app_config.project.data_dir, asset, "1h")
        return market

    def _ensure_models_trained(self, market: dict[str, pd.DataFrame]) -> None:
        """Garante que os modelos campeões estejam carregados para inferência."""
        v4_compat = V4Config(
            holdout_start=self.v5_config.holdout_start,
            holdout_end=self.v5_config.holdout_end,
            lookback_hours=self.v5_config.tf_lookback_hours,
            horizon_hours=1,
            purge_hours=self.v5_config.purge_hours,
            round_trip_bps=self.v5_config.round_trip_bps,
            stationary_features=self.v5_config.stationary_features,
            include_intrahour_15m=False,
        )

        import json
        from pathlib import Path

        for asset in (Asset.BTCUSDT, Asset.ETHUSDT, Asset.SOLUSDT):
            if asset.value in self.models:
                continue

            # 1. Tenta carregar os modelos ONNX exportados
            onnx_dir = Path(f"artifacts/v5/champion/{asset.value}")
            features_file = onnx_dir / "features.json"
            if features_file.exists() and (onnx_dir / "member_00.onnx").exists():
                import onnxruntime as ort
                cols = json.loads(features_file.read_text(encoding="utf-8"))
                sessions = [
                    ort.InferenceSession(str(onnx_dir / f"member_{i:02d}.onnx"), providers=["CPUExecutionProvider"])
                    for i in range(5)
                ]
                self.models[asset.value] = sessions
                self.feature_columns[asset.value] = cols
                continue

            # 2. Fallback: treina modelo se os dados locais existirem
            with contextlib.suppress(Exception):
                local_market = {
                    item.value: load_raw_market(self.app_config.project.data_dir, item, "1h")
                    for item in Asset
                }
                features = build_features(asset=asset, market=local_market, intrahour=None, config=v4_compat)
                dataset = build_direct_dataset(
                    asset=asset,
                    features=features,
                    market=local_market[asset.value],
                    config=v4_compat,
                    pre_holdout_only=True,
                )
                frame = dataset.frame[dataset.frame["label_valid"].astype(bool)].reset_index(drop=True)
                x = frame[list(dataset.feature_columns)].to_numpy(dtype=np.float32)
                y = frame[dataset.target_column].to_numpy(dtype=np.float32)
                ensemble = create_xgboost_reference(config=self.v5_config, feature_names=dataset.feature_columns)
                ensemble.fit(x, y, np.arange(len(frame)))
                self.models[asset.value] = ensemble
                self.feature_columns[asset.value] = list(dataset.feature_columns)

    def execute_cycle(self, live: bool = True) -> list[PaperSignal]:
        """Executa um ciclo completo de inferência, sinalização e execução simulada."""
        market = self._fetch_market_frames(live=live)
        self._ensure_models_trained(market)

        v4_compat = V4Config(
            holdout_start=self.v5_config.holdout_start,
            holdout_end=self.v5_config.holdout_end,
            lookback_hours=self.v5_config.tf_lookback_hours,
            horizon_hours=1,
            purge_hours=self.v5_config.purge_hours,
            round_trip_bps=self.v5_config.round_trip_bps,
            stationary_features=self.v5_config.stationary_features,
            include_intrahour_15m=False,
        )

        signals: list[PaperSignal] = []
        now_utc = utc_now()

        # Obter posições atuais no ledger
        positions = {p.asset: p for p in self.storage.positions(self.ledger_name)}
        from bottrade.storage import LedgerRow
        with self.storage.session() as session:
            ledger_obj = session.get(LedgerRow, self.ledger_name)
            cash = float(ledger_obj.cash) if ledger_obj else 1000.0

        # 1. Inferência para cada ativo
        btc_features = build_features(asset=Asset.BTCUSDT, market=market, intrahour=None, config=v4_compat)
        btc_latest = btc_features.iloc[-1]
        btc_24h_ret = float(btc_latest.get("return_24h", 0.0))

        for asset in (Asset.BTCUSDT, Asset.ETHUSDT, Asset.SOLUSDT):
            features = build_features(asset=asset, market=market, intrahour=None, config=v4_compat)
            latest_row = features.iloc[-1]
            cols = self.feature_columns[asset.value]
            x_sample = latest_row[cols].to_numpy(dtype=np.float32).reshape(1, -1)

            model = self.models[asset.value]
            if isinstance(model, list):
                preds = [float(sess.run(None, {sess.get_inputs()[0].name: x_sample})[0][0]) for sess in model]
            else:
                preds = [float(m.predict(x_sample)[0]) for m in model.members]
            pred_mean = float(np.mean(preds))
            pred_std = float(np.std(preds))
            effective = pred_mean - 0.5 * pred_std

            curr_price = float(market[asset.value].iloc[-1]["close"])
            vol_1h = float(latest_row.get("ewma_volatility_1h", 0.008))
            vol_ratio = float(latest_row.get("volatility_ratio_6h_168h", 1.0))
            close_to_ema_72 = float(latest_row.get("close_to_ema_72h", 0.0))
            close_to_ema_168 = float(latest_row.get("close_to_ema_168h", 0.0))
            cvd_6h = float(latest_row.get("cvd_ratio_6h", 0.0))

            # Filtros quantitativos
            threshold = (self.v5_config.round_trip_bps + self.v5_config.entry_margins_bps[0]) / 10_000.0
            vol_compressed = vol_ratio < 0.65
            btc_dumping = (asset != Asset.BTCUSDT) and (btc_24h_ret < -0.018)
            alt_downtrend = (asset != Asset.BTCUSDT) and (close_to_ema_168 < -0.020) and (btc_24h_ret < 0.0)
            in_sideways = abs(close_to_ema_72) < 0.020 and vol_ratio >= 0.95
            turbulent_chop = in_sideways and (cvd_6h <= 0.02)
            sol_sideways = (asset == Asset.SOLUSDT) and (abs(close_to_ema_72) < 0.025)

            current_pos = positions.get(asset)
            has_position = current_pos is not None and float(current_pos.quantity) > 0

            signal_label = "CASH"
            reason = "Aguardando sinal com assimetria"

            if has_position:
                entry_p = float(current_pos.entry_price)
                gross = curr_price / entry_p - 1.0 if entry_p > 0 else 0.0
                peak_p = float(getattr(current_pos, "peak_price", entry_p))
                peak_p = max(peak_p, curr_price)
                peak_gross = peak_p / entry_p - 1.0 if entry_p > 0 else 0.0

                trailing_stop = peak_gross >= (2.0 * vol_1h) and gross <= (peak_gross * 0.50)
                hard_stop = gross <= (-3.0 * vol_1h)

                if effective <= 0.0:
                    signal_label = "SELL"
                    reason = "Previsão virou negativa (saída técnica)"
                elif trailing_stop:
                    signal_label = "SELL"
                    reason = f"Trailing Stop acionado (travou lucro em {gross*100:+.2f}%)"
                elif hard_stop:
                    signal_label = "SELL"
                    reason = f"Stop Loss acionado (proteção de capital em {gross*100:+.2f}%)"
                else:
                    signal_label = "HOLD"
                    reason = f"Posição mantida (PnL aberto: {gross*100:+.2f}%)"
            else:
                if effective > threshold:
                    if vol_compressed:
                        reason = "Filtro: compressão extrema de volatilidade"
                    elif btc_dumping:
                        reason = "Filtro: queda macro abrupta no Bitcoin"
                    elif alt_downtrend:
                        reason = "Filtro: tendência de baixa estrutural"
                    elif turbulent_chop:
                        reason = "Filtro: ruído lateral turbulento sem CVD"
                    elif sol_sideways:
                        reason = "Filtro: Solana em range lateral sem momentum"
                    else:
                        signal_label = "BUY"
                        reason = f"Assimetria favorável ({effective*10_000:.1f} bps > {threshold*10_000:.1f} bps)"

            signals.append(
                PaperSignal(
                    asset=asset.value,
                    prediction_bps=pred_mean * 10_000,
                    effective_bps=effective * 10_000,
                    threshold_bps=threshold * 10_000,
                    signal=signal_label,
                    reason=reason,
                    current_price=curr_price,
                    ewma_volatility_1h=vol_1h,
                )
            )

        # 2. Execução simulada das ordens no banco de dados SQLite
        from bottrade.domain import PaperFill, PaperOrder
        order_fills: list[tuple[PaperOrder, PaperFill]] = []

        for sig in signals:
            asset_enum = Asset(sig.asset)
            pos = positions.get(asset_enum)
            has_pos = pos is not None and float(pos.quantity) > 0

            if sig.signal == "BUY" and not has_pos and cash >= 100.0:
                trade_notional = min(cash * 0.30, 300.0)
                qty = trade_notional / sig.current_price
                fee = trade_notional * (self.v5_config.round_trip_bps / 20_000.0)  # 12 bps taker entry
                order_id = f"v5-{asset_enum.value}-BUY-{now_utc.strftime('%Y%m%d%H%M%S')}"
                order = PaperOrder(
                    client_order_id=order_id,
                    ledger=self.ledger_name,
                    asset=asset_enum,
                    as_of=now_utc,
                    side="BUY",
                    quantity=Decimal(f"{qty:.6f}"),
                    reference_price=Decimal(f"{sig.current_price:.4f}"),
                    reason=sig.reason,
                )
                fill = PaperFill(
                    client_order_id=order_id,
                    ledger=self.ledger_name,
                    asset=asset_enum,
                    as_of=now_utc,
                    side="BUY",
                    quantity=Decimal(f"{qty:.6f}"),
                    price=Decimal(f"{sig.current_price:.4f}"),
                    fee=Decimal(f"{fee:.6f}"),
                    bid=Decimal(f"{sig.current_price * 0.9998:.4f}"),
                    ask=Decimal(f"{sig.current_price * 1.0002:.4f}"),
                    visible_depth_quantity=Decimal("10.0"),
                    visible_depth_notional=Decimal("500000.0"),
                    spread_bps=4.0,
                    impact_bps=0.0,
                )
                order_fills.append((order, fill))
                cash -= (trade_notional + fee)
            elif sig.signal == "SELL" and has_pos:
                qty = float(pos.quantity)
                notional = qty * sig.current_price
                fee = notional * (self.v5_config.round_trip_bps / 20_000.0)  # 12 bps taker exit
                order_id = f"v5-{asset_enum.value}-SELL-{now_utc.strftime('%Y%m%d%H%M%S')}"
                order = PaperOrder(
                    client_order_id=order_id,
                    ledger=self.ledger_name,
                    asset=asset_enum,
                    as_of=now_utc,
                    side="SELL",
                    quantity=Decimal(f"{qty:.6f}"),
                    reference_price=Decimal(f"{sig.current_price:.4f}"),
                    reason=sig.reason,
                )
                fill = PaperFill(
                    client_order_id=order_id,
                    ledger=self.ledger_name,
                    asset=asset_enum,
                    as_of=now_utc,
                    side="SELL",
                    quantity=Decimal(f"{qty:.6f}"),
                    price=Decimal(f"{sig.current_price:.4f}"),
                    fee=Decimal(f"{fee:.6f}"),
                    bid=Decimal(f"{sig.current_price * 0.9998:.4f}"),
                    ask=Decimal(f"{sig.current_price * 1.0002:.4f}"),
                    visible_depth_quantity=Decimal("10.0"),
                    visible_depth_notional=Decimal("500000.0"),
                    spread_bps=4.0,
                    impact_bps=0.0,
                )
                order_fills.append((order, fill))
                cash += (notional - fee)

        for o, f in order_fills:
            with contextlib.suppress(Exception):
                self.storage.apply_order_fill(o, f)

        return signals

    def get_status_summary(self, signals: list[PaperSignal]) -> str:
        """Gera o painel de telemetria em formato markdown/ASCII para terminal."""
        from bottrade.storage import LedgerRow
        with self.storage.session() as session:
            ledger_obj = session.get(LedgerRow, self.ledger_name)
            cash = float(ledger_obj.cash) if ledger_obj else 1000.0
        pos_list = self.storage.positions(self.ledger_name)
        now_str = utc_now().strftime("%Y-%m-%d %H:%M:%S UTC")

        price_map = {s.asset: s.current_price for s in signals}
        pos_value = sum(float(p.quantity) * price_map.get(p.asset.value, float(p.average_price)) for p in pos_list)
        total_equity = cash + pos_value
        pnl_pct = (total_equity / 1000.0 - 1.0) * 100.0

        lines = [
            "=" * 65,
            "  [BOT] BOTTRADE V5 - PAPER TRADING ENGINE (ONLINE)",
            f"  Timestamp: {now_str} | Ledger: {self.ledger_name}",
            "=" * 65,
            f"  Patrimonio Liquido Total: ${total_equity:,.2f} USDT ({pnl_pct:+.2f}%)",
            f"  Caixa Disponivel:        ${cash:,.2f} USDT",
            f"  Capital em Posicoes:     ${pos_value:,.2f} USDT",
            "-" * 65,
            "  SINAIS & MODELOS EM TEMPO REAL (XGBoost Institucional):",
        ]

        for s in signals:
            icon = "[COMPRA]" if s.signal == "BUY" else ("[VENDA]" if s.signal == "SELL" else ("[HOLD]" if s.signal == "HOLD" else "[CAIXA]"))
            lines.append(
                f"  {icon:<8} {s.asset:<7} | Preco: ${s.current_price:>10,.2f} | Sinal: {s.signal:<4} | "
                f"Pred: {s.effective_bps:>+5.1f} bps (Gate: {s.threshold_bps:.1f}) | {s.reason}"
            )

        lines.extend([
            "-" * 65,
            "  POSICOES ATIVAS NA CARTEIRA:",
        ])

        active_positions = [p for p in pos_list if float(p.quantity) > 0]
        if not active_positions:
            lines.append("  (Nenhuma posicao aberta; capital 100% preservado em caixa USDT)")
        else:
            for p in active_positions:
                cur_p = price_map.get(p.asset.value, float(p.average_price))
                entry_p = float(p.average_price)
                gross_pnl = (cur_p / entry_p - 1.0) * 100.0 if entry_p > 0 else 0.0
                lines.append(
                    f"  [POS] {p.asset.value:<7} | Qtd: {float(p.quantity):.4f} | Entrada: ${entry_p:,.2f} | "
                    f"Atual: ${cur_p:,.2f} | PnL Aberto: {gross_pnl:+.2f}%"
                )

        lines.append("=" * 65)
        return "\n".join(lines)

    def notify_channels(self, signals: list[PaperSignal], text_summary: str) -> None:
        """Envia notificações via Telegram, GitHub Step Summary e grava reports/LIVE_DASHBOARD.md."""
        import os
        from pathlib import Path

        # 1. Enviar mensagem de texto no Telegram se configurado
        if self.alerter.configured:
            self.alerter.send(text_summary)

        # 2. Gerar relatório visual em Markdown
        cash = 1000.0
        with self.storage.session() as session:
            from bottrade.storage import LedgerRow
            ledger_obj = session.get(LedgerRow, self.ledger_name)
            if ledger_obj:
                cash = float(ledger_obj.cash)

        pos_list = self.storage.positions(self.ledger_name)
        now_str = utc_now().strftime("%Y-%m-%d %H:%M:%S UTC")
        price_map = {s.asset: s.current_price for s in signals}
        pos_value = sum(float(p.quantity) * price_map.get(p.asset.value, float(p.average_price)) for p in pos_list)
        total_equity = cash + pos_value
        pnl_pct = (total_equity / 1000.0 - 1.0) * 100.0

        md_lines = [
            "# 🤖 BOTTRADE V5 - Painel Oficial de Paper Trading",
            f"**Ultima Atualizacao**: `{now_str}` | **Ledger**: `{self.ledger_name}` | **Status**: 🟢 **ONLINE**",
            "",
            "## 💰 Resumo da Carteira",
            f"- **Patrimonio Liquido Total**: **${total_equity:,.2f} USDT** (`{pnl_pct:+.2f}%`)",
            f"- **Caixa Disponivel**: **${cash:,.2f} USDT**",
            f"- **Capital em Posicoes**: **${pos_value:,.2f} USDT**",
            "",
            "## 📊 Sinais e Previsoes em Tempo Real (XGBoost Institucional)",
            "",
            "| Ativo | Preco Atual | Sinal | Previsao | Gate Custo | Status / Diagnostico |",
            "|:---|---:|:---:|---:|---:|:---|",
        ]

        for s in signals:
            badge = "🟢 **BUY**" if s.signal == "BUY" else ("🔴 **SELL**" if s.signal == "SELL" else ("🟡 **HOLD**" if s.signal == "HOLD" else "⚪ **CASH**"))
            md_lines.append(
                f"| **{s.asset}** | ${s.current_price:,.2f} | {badge} | {s.effective_bps:+.1f} bps | {s.threshold_bps:.1f} bps | {s.reason} |"
            )

        md_lines.extend([
            "",
            "## 📈 Posicoes Abertas",
            "",
        ])

        active_positions = [p for p in pos_list if float(p.quantity) > 0]
        if not active_positions:
            md_lines.append("> *Nenhuma posicao aberta no momento. Capital 100% preservado em caixa USDT aguardando assimetria favoravel.*")
        else:
            md_lines.append("| Ativo | Quantidade | Preco Entrada | Preco Atual | PnL Aberto (%) |")
            md_lines.append("|:---|---:|---:|---:|---:|")
            for p in active_positions:
                cur_p = price_map.get(p.asset.value, float(p.average_price))
                entry_p = float(p.average_price)
                gross_pnl = (cur_p / entry_p - 1.0) * 100.0 if entry_p > 0 else 0.0
                md_lines.append(
                    f"| **{p.asset.value}** | {float(p.quantity):.4f} | ${entry_p:,.2f} | ${cur_p:,.2f} | `{gross_pnl:+.2f}%` |"
                )

        md_content = "\n".join(md_lines) + "\n"

        dashboard_file = Path("reports/LIVE_DASHBOARD.md")
        dashboard_file.parent.mkdir(parents=True, exist_ok=True)
        dashboard_file.write_text(md_content, encoding="utf-8")

        summary_env = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary_env:
            with open(summary_env, "a", encoding="utf-8") as f:
                f.write(md_content)
