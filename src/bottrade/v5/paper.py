from __future__ import annotations

import contextlib
import json
import os
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from bottrade.alerts import TelegramAlerter
from bottrade.config import AppConfig
from bottrade.data.binance import BinanceClient
from bottrade.data.http import PublicHttpClient
from bottrade.domain import Asset, PaperFill, PaperOrder
from bottrade.storage import LedgerRow, Storage
from bottrade.utils import utc_now
from bottrade.v4.config import V4Config
from bottrade.v4.features import build_direct_dataset, build_features, load_raw_market
from bottrade.v5.config import V5Config


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
    pred_std_bps: float = 0.0
    member_preds_bps: list[float] = field(default_factory=list)
    flow_bps: float = 0.0
    cvd_6h: float = 0.0
    cvd_24h: float = 0.0
    close_to_ema_24: float = 0.0
    close_to_ema_72: float = 0.0
    close_to_ema_168: float = 0.0
    dist_high_24: float = 0.0
    vol_ratio: float = 1.0
    btc_24h_ret: float = 0.0
    filters: dict[str, bool] = field(default_factory=dict)


class PaperTradingV5:
    """Motor oficial de Paper Trading V5 (Horizonte Swing 12h + Microestrutura CVD)."""

    def __init__(
        self,
        v5_config: V5Config,
        app_config: AppConfig,
        ledger_name: str = "paper_1000",
        state_path: str | Path = "reports/paper_state.json",
    ) -> None:
        self.v5_config = v5_config
        self.app_config = app_config
        self.ledger_name = ledger_name
        self.state_path = Path(state_path)
        self.storage = Storage(app_config.runtime.database_url)
        self.storage.initialize(app_config)
        self.http_client = PublicHttpClient()
        self.binance_client = BinanceClient(app_config.market, self.http_client)
        self.models: dict[str, Any] = {}
        self.feature_columns: dict[str, list[str]] = {}

        token = os.environ.get("TELEGRAM_BOT_TOKEN") or app_config.runtime.telegram_bot_token
        chat_id = os.environ.get("TELEGRAM_CHAT_ID") or app_config.runtime.telegram_chat_id
        self.alerter = TelegramAlerter(token or "", chat_id or "")

    def _load_portfolio_state(self) -> dict[str, Any]:
        """Carrega o estado persistente da carteira (compatível com execução stateless no GitHub Actions)."""
        default_state: dict[str, Any] = {
            "ledger": self.ledger_name,
            "initial_cash": 1000.0,
            "cash": 1000.0,
            "realized_pnl_usdt": 0.0,
            "closed_trades_count": 0,
            "winning_trades_count": 0,
            "positions": {},
            "last_exit_times": {},
            "trade_history": [],
        }
        if self.state_path.exists():
            with contextlib.suppress(Exception):
                loaded = json.loads(self.state_path.read_text(encoding="utf-8"))
                if isinstance(loaded, dict):
                    default_state.update(loaded)
        return default_state

    def _save_portfolio_state(self, state: dict[str, Any]) -> None:
        """Persiste o estado da carteira em JSON versionado e sincroniza o caixa no SQLite."""
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        self.state_path.write_text(
            json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        with contextlib.suppress(Exception), self.storage.session() as session:
            ledger_obj = session.get(LedgerRow, self.ledger_name)
            if ledger_obj is not None:
                ledger_obj.cash = Decimal(f"{float(state['cash']):.6f}")
                session.commit()

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
                pass
        for asset in Asset:
            market[asset.value] = load_raw_market(self.app_config.project.data_dir, asset, "1h")
        return market

    def _ensure_models_trained(self, market: dict[str, pd.DataFrame]) -> None:
        """Garante que os modelos campeões de 12h estejam carregados para inferência."""
        v4_compat = V4Config(
            holdout_start=self.v5_config.holdout_start,
            holdout_end=self.v5_config.holdout_end,
            lookback_hours=self.v5_config.tf_lookback_hours,
            horizon_hours=self.v5_config.max_holding_hours,
            purge_hours=self.v5_config.purge_hours,
            round_trip_bps=self.v5_config.round_trip_bps,
            stationary_features=self.v5_config.stationary_features,
            include_intrahour_15m=False,
        )

        for asset in (Asset.BTCUSDT, Asset.ETHUSDT, Asset.SOLUSDT):
            if asset.value in self.models:
                continue

            onnx_dir = Path(f"artifacts/v5/champion/{asset.value}")
            features_file = onnx_dir / "features.json"
            if features_file.exists() and (onnx_dir / "member_00.onnx").exists():
                import onnxruntime as ort

                cols = json.loads(features_file.read_text(encoding="utf-8"))
                sessions = [
                    ort.InferenceSession(
                        str(onnx_dir / f"member_{i:02d}.onnx"),
                        providers=["CPUExecutionProvider"],
                    )
                    for i in range(5)
                ]
                self.models[asset.value] = sessions
                self.feature_columns[asset.value] = cols
                continue

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
                y = np.clip(frame[dataset.target_column].to_numpy(dtype=np.float32), -0.06, 0.06)
                window_rows = self.v5_config.train_months * 30 * 24
                train_idx = np.arange(max(0, len(frame) - window_rows), len(frame))
                from bottrade.v5.models.xgboost_ref import create_xgboost_reference

                ensemble = create_xgboost_reference(config=self.v5_config, feature_names=dataset.feature_columns)
                ensemble.fit(x, y, train_idx)
                self.models[asset.value] = ensemble
                self.feature_columns[asset.value] = list(dataset.feature_columns)

    def execute_cycle(self, live: bool = True) -> list[PaperSignal]:
        """Executa um ciclo completo de inferência 12h, sinalização e execução simulada persistente."""
        market = self._fetch_market_frames(live=live)
        self._ensure_models_trained(market)

        v4_compat = V4Config(
            holdout_start=self.v5_config.holdout_start,
            holdout_end=self.v5_config.holdout_end,
            lookback_hours=self.v5_config.tf_lookback_hours,
            horizon_hours=self.v5_config.max_holding_hours,
            purge_hours=self.v5_config.purge_hours,
            round_trip_bps=self.v5_config.round_trip_bps,
            stationary_features=self.v5_config.stationary_features,
            include_intrahour_15m=False,
        )

        signals: list[PaperSignal] = []
        now_utc = utc_now()
        state = self._load_portfolio_state()
        cash = float(state.get("cash", 1000.0))
        positions_state: dict[str, dict[str, Any]] = state.setdefault("positions", {})
        last_exits: dict[str, str] = state.setdefault("last_exit_times", {})
        trade_history: list[dict[str, Any]] = state.setdefault("trade_history", [])
        last_stop_str = str(state.get("last_stop_loss_at", ""))

        btc_features = build_features(asset=Asset.BTCUSDT, market=market, intrahour=None, config=v4_compat)
        btc_latest = btc_features.iloc[-1]
        btc_24h_ret = float(btc_latest.get("return_24h", 0.0))
        btc_cvd_24h = float(btc_latest.get("cvd_ratio_24h", 0.0))

        global_stop_cooldown = False
        if last_stop_str:
            with contextlib.suppress(Exception):
                stop_dt = datetime.fromisoformat(last_stop_str)
                if (now_utc - stop_dt).total_seconds() < 6.0 * 3600.0:
                    global_stop_cooldown = True

        for asset in (Asset.BTCUSDT, Asset.ETHUSDT, Asset.SOLUSDT):
            features = build_features(asset=asset, market=market, intrahour=None, config=v4_compat)
            latest_row = features.iloc[-1]
            cols = self.feature_columns[asset.value]
            x_sample = latest_row[cols].to_numpy(dtype=np.float32).reshape(1, -1)

            model = self.models[asset.value]
            if isinstance(model, list):
                preds = [
                    float(np.asarray(sess.run(None, {sess.get_inputs()[0].name: x_sample})[0]).flatten()[0])
                    for sess in model
                ]
            else:
                preds = [float(np.asarray(m.predict(x_sample)).flatten()[0]) for m in model.members]

            pred_mean_bps = float(np.mean(preds)) * 10_000.0
            pred_std_bps = float(np.std(preds)) * 10_000.0

            curr_price = float(market[asset.value].iloc[-1]["close"])
            vol_1h = float(latest_row.get("ewma_volatility_1h", 0.008))
            if not np.isfinite(vol_1h) or vol_1h <= 0:
                vol_1h = 0.008
            vol_ratio = float(latest_row.get("volatility_ratio_6h_168h", 1.0))
            close_to_ema_24 = float(latest_row.get("close_to_ema_24h", 0.0))
            close_to_ema_72 = float(latest_row.get("close_to_ema_72h", 0.0))
            close_to_ema_168 = float(latest_row.get("close_to_ema_168h", 0.0))
            dist_high_24 = float(latest_row.get("close_to_previous_high_24h", 0.0))
            cvd_6h = float(latest_row.get("cvd_ratio_6h", 0.0))
            cvd_24h = float(latest_row.get("cvd_ratio_24h", 0.0))

            # Alpha Composto Institucional V5.2 (Previsão Swing 12h + Impulso de Order Flow CVD)
            flow_bps = (cvd_24h * 120.0) + (cvd_6h * 80.0) + (btc_cvd_24h * 60.0)
            effective_bps = 0.55 * pred_mean_bps + 0.45 * flow_bps - 0.10 * pred_std_bps
            # Gate de Entrada V5.2: 24.0 bps (taxa) + 12.0 bps (margem líquida mínima de segurança) = 36.0 bps
            threshold_bps = float(self.v5_config.round_trip_bps + 12.0)

            # Filtros inteligentes V5.2: regime, fluxo institucional, divergência de ensemble, anti-topo e tendência macro
            vol_compressed = vol_ratio < 0.70
            btc_dumping = btc_24h_ret < 0.0005
            high_uncertainty = pred_std_bps > 20.0
            weak_order_flow = not (
                (cvd_24h >= 0.080)
                and (cvd_6h >= 0.090)
                and (btc_cvd_24h > -0.010)
                and (pred_mean_bps >= 30.0)
                and (flow_bps >= 22.0)
            )
            macro_downtrend = close_to_ema_168 < -0.002 and close_to_ema_72 > 0.0
            stretched_top = not (
                (dist_high_24 < -0.008)
                and (-0.015 < close_to_ema_24 <= 0.0090)
                and (close_to_ema_72 <= 0.0105)
                and (btc_24h_ret <= 0.0085)
            )

            cooldown_active = False
            last_exit_str = last_exits.get(asset.value)
            if last_exit_str:
                with contextlib.suppress(Exception):
                    last_dt = datetime.fromisoformat(last_exit_str)
                    if (now_utc - last_dt).total_seconds() < 4.0 * 3600.0:
                        cooldown_active = True

            pos_info = positions_state.get(asset.value)
            has_position = pos_info is not None and float(pos_info.get("quantity", 0.0)) > 0.0

            signal_label = "CASH"
            reason = f"Aguardando setup com assimetria (> {threshold_bps:.1f} bps)"

            if has_position and pos_info is not None:
                entry_p = float(pos_info["entry_price"])
                gross = curr_price / entry_p - 1.0 if entry_p > 0 else 0.0
                peak_p = max(float(pos_info.get("peak_price", entry_p)), curr_price)
                pos_info["peak_price"] = peak_p
                peak_gross = peak_p / entry_p - 1.0 if entry_p > 0 else 0.0

                opened_dt = now_utc
                with contextlib.suppress(Exception):
                    opened_dt = datetime.fromisoformat(str(pos_info.get("opened_at", now_utc.isoformat())))
                held_hours = max(0.0, (now_utc - opened_dt).total_seconds() / 3600.0)

                trailing_stop = peak_gross >= max(0.0135, 1.8 * vol_1h) and gross <= (peak_gross * 0.68)
                breakeven_lock = peak_gross >= 0.0095 and gross <= (peak_gross * 0.48)
                early_cut = held_hours >= 1.5 and peak_gross < 0.0030 and gross <= -0.0045
                hard_stop = gross <= -max(0.012, 1.9 * vol_1h)
                time_exit = held_hours >= float(self.v5_config.max_holding_hours)
                reversal_exit = effective_bps < 0.0 or (held_hours >= 1.0 and btc_24h_ret < -0.005 and gross < -0.002)

                if trailing_stop:
                    signal_label = "SELL"
                    reason = f"Trailing Stop acionado (pico {peak_gross*100:+.2f}%, realizou {gross*100:+.2f}%)"
                elif breakeven_lock:
                    signal_label = "SELL"
                    reason = f"Proteção de Lucro acionada (pico {peak_gross*100:+.2f}%, realizou {gross*100:+.2f}%)"
                elif early_cut:
                    signal_label = "SELL"
                    reason = f"Corte rápido de falha de impulso ({gross*100:+.2f}%)"
                elif hard_stop:
                    signal_label = "SELL"
                    reason = f"Stop Loss técnico acionado ({gross*100:+.2f}%)"
                elif reversal_exit:
                    signal_label = "SELL"
                    reason = f"Saída por reversão/fraqueza ({effective_bps:+.1f} bps)"
                elif time_exit:
                    signal_label = "SELL"
                    reason = f"Alvo temporal de {self.v5_config.max_holding_hours}h concluído ({gross*100:+.2f}%)"
                else:
                    signal_label = "HOLD"
                    reason = f"Posição ativa há {held_hours:.1f}h (PnL: {gross*100:+.2f}% | Pico: {peak_gross*100:+.2f}%)"
            else:
                if effective_bps >= threshold_bps:
                    if global_stop_cooldown:
                        reason = "Filtro: disjuntor global pós-Stop ativo (6h)"
                    elif cooldown_active:
                        reason = "Filtro: aguardando cooldown pós-trade (4h)"
                    elif vol_compressed:
                        reason = "Filtro: compressão de volatilidade (< 0.70)"
                    elif btc_dumping:
                        reason = "Filtro: Bitcoin sem tração positiva em 24h"
                    elif high_uncertainty:
                        reason = f"Filtro: divergência alta no ensemble ({pred_std_bps:.1f} bps > 20)"
                    elif weak_order_flow:
                        reason = "Filtro: absorção institucional CVD 24h/6h insuficiente"
                    elif macro_downtrend:
                        reason = "Filtro: armadilha de repique contra EMA semanal (168h)"
                    elif stretched_top:
                        reason = "Filtro: preço já esticado acima das EMAs 24h/72h"
                    else:
                        signal_label = "BUY"
                        reason = (
                            f"Entrada Swing V5.2 aprovada (Alpha {effective_bps:+.1f} bps >= "
                            f"{threshold_bps:.1f} bps | CVD 24h {cvd_24h:+.3f})"
                        )

            signals.append(
                PaperSignal(
                    asset=asset.value,
                    prediction_bps=pred_mean_bps,
                    effective_bps=effective_bps,
                    threshold_bps=threshold_bps,
                    signal=signal_label,
                    reason=reason,
                    current_price=curr_price,
                    ewma_volatility_1h=vol_1h,
                    pred_std_bps=pred_std_bps,
                    member_preds_bps=[float(p * 10_000.0) for p in preds],
                    flow_bps=flow_bps,
                    cvd_6h=cvd_6h,
                    cvd_24h=cvd_24h,
                    close_to_ema_24=close_to_ema_24,
                    close_to_ema_72=close_to_ema_72,
                    close_to_ema_168=close_to_ema_168,
                    dist_high_24=dist_high_24,
                    vol_ratio=vol_ratio,
                    btc_24h_ret=btc_24h_ret,
                    filters={
                        "global_stop_cooldown": bool(global_stop_cooldown),
                        "vol_compressed": bool(vol_compressed),
                        "btc_dumping": bool(btc_dumping),
                        "high_uncertainty": bool(high_uncertainty),
                        "weak_order_flow": bool(weak_order_flow),
                        "macro_downtrend": bool(macro_downtrend),
                        "stretched_top": bool(stretched_top),
                        "cooldown_active": bool(cooldown_active),
                    },
                )
            )

        # 2. Execução simulada das ordens (Estado JSON + SQLite)
        # Processar vendas primeiro para liberar caixa e acionar disjuntor se houve Stop
        order_fills: list[tuple[PaperOrder, PaperFill]] = []
        price_lookup = {s.asset: s.current_price for s in signals}

        for sig in signals:
            asset_enum = Asset(sig.asset)
            pos_info = positions_state.get(sig.asset)
            has_pos = pos_info is not None and float(pos_info.get("quantity", 0.0)) > 0.0

            if sig.signal == "SELL" and has_pos and pos_info is not None:
                qty = float(pos_info["quantity"])
                entry_p = float(pos_info["entry_price"])
                entry_notional = float(pos_info.get("notional_usdt", qty * entry_p))
                entry_fee = float(pos_info.get("entry_fee_usdt", entry_notional * 0.0012))
                notional = qty * sig.current_price
                exit_fee = notional * (self.v5_config.round_trip_bps / 20_000.0)
                order_id = f"v5-{asset_enum.value}-SELL-{now_utc.strftime('%Y%m%d%H%M%S')}"
                order = PaperOrder(
                    client_order_id=order_id,
                    ledger=self.ledger_name,
                    asset=asset_enum,
                    as_of=now_utc,
                    side="SELL",
                    quantity=Decimal(f"{qty:.6f}"),
                    reference_price=Decimal(f"{sig.current_price:.4f}"),
                    reason=sig.reason[:120],
                )
                fill = PaperFill(
                    client_order_id=order_id,
                    ledger=self.ledger_name,
                    asset=asset_enum,
                    as_of=now_utc,
                    side="SELL",
                    quantity=Decimal(f"{qty:.6f}"),
                    price=Decimal(f"{sig.current_price:.4f}"),
                    fee=Decimal(f"{exit_fee:.6f}"),
                    bid=Decimal(f"{sig.current_price * 0.9998:.4f}"),
                    ask=Decimal(f"{sig.current_price * 1.0002:.4f}"),
                    visible_depth_quantity=Decimal("10.0"),
                    visible_depth_notional=Decimal("500000.0"),
                    spread_bps=4.0,
                    impact_bps=0.0,
                )
                order_fills.append((order, fill))
                cash += notional - exit_fee

                net_pnl_usdt = (notional - exit_fee) - (entry_notional + entry_fee)
                gross_pct = (sig.current_price / entry_p - 1.0) * 100.0 if entry_p > 0 else 0.0
                net_pct = gross_pct - (self.v5_config.round_trip_bps / 100.0)

                state["realized_pnl_usdt"] = round(float(state.get("realized_pnl_usdt", 0.0)) + net_pnl_usdt, 4)
                state["closed_trades_count"] = int(state.get("closed_trades_count", 0)) + 1
                if net_pnl_usdt > 0:
                    state["winning_trades_count"] = int(state.get("winning_trades_count", 0)) + 1
                if gross_pct < -0.30 or "Stop Loss" in sig.reason or "Corte rápido" in sig.reason:
                    state["last_stop_loss_at"] = now_utc.isoformat()
                    global_stop_cooldown = True

                trade_record = {
                    "asset": sig.asset,
                    "opened_at": pos_info.get("opened_at", ""),
                    "closed_at": now_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
                    "entry_price": round(entry_p, 4),
                    "exit_price": round(sig.current_price, 4),
                    "quantity": round(qty, 6),
                    "gross_pnl_pct": round(gross_pct, 2),
                    "net_pnl_pct": round(net_pct, 2),
                    "net_pnl_usdt": round(net_pnl_usdt, 2),
                    "exit_reason": sig.reason,
                }
                trade_history.insert(0, trade_record)
                state["trade_history"] = trade_history[:50]
                last_exits[sig.asset] = now_utc.isoformat()
                positions_state.pop(sig.asset, None)

        # Processar compras ordenadas pelo maior Alpha, respeitando limite de correlação e disjuntor global
        buy_candidates = sorted(
            [s for s in signals if s.signal == "BUY"],
            key=lambda item: item.effective_bps,
            reverse=True,
        )
        for sig in buy_candidates:
            asset_enum = Asset(sig.asset)
            pos_info = positions_state.get(sig.asset)
            has_pos = pos_info is not None and float(pos_info.get("quantity", 0.0)) > 0.0
            active_pos_list = [p for p in positions_state.values() if float(p.get("quantity", 0.0)) > 0.0]

            if has_pos or cash < 100.0:
                continue
            if global_stop_cooldown:
                sig.signal = "CASH"
                sig.reason = "Filtro: disjuntor global pós-Stop acionado neste ciclo"
                continue
            if len(active_pos_list) >= 2:
                sig.signal = "CASH"
                sig.reason = "Filtro: limite máximo de 2 posições simultâneas"
                continue
            if len(active_pos_list) == 1:
                existing_p = active_pos_list[0]
                ex_asset = str(existing_p["asset"])
                ex_cur = price_lookup.get(ex_asset, float(existing_p["entry_price"]))
                ex_gross = ex_cur / float(existing_p["entry_price"]) - 1.0
                if ex_gross < 0.0020:
                    sig.signal = "CASH"
                    sig.reason = f"Filtro: aguardando 1ª posição ({ex_asset}) consolidar lucro (> +0.20%)"
                    continue

            open_notional = sum(
                float(p["quantity"]) * price_lookup.get(str(p["asset"]), float(p["entry_price"]))
                for p in active_pos_list
            )
            total_eq = cash + open_notional
            trade_notional = min(cash * 0.95, total_eq * 0.33, 330.0)
            if trade_notional < 100.0:
                continue

            qty = trade_notional / sig.current_price
            fee = trade_notional * (self.v5_config.round_trip_bps / 20_000.0)
            order_id = f"v5-{asset_enum.value}-BUY-{now_utc.strftime('%Y%m%d%H%M%S')}"
            order = PaperOrder(
                client_order_id=order_id,
                ledger=self.ledger_name,
                asset=asset_enum,
                as_of=now_utc,
                side="BUY",
                quantity=Decimal(f"{qty:.6f}"),
                reference_price=Decimal(f"{sig.current_price:.4f}"),
                reason=sig.reason[:120],
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
            cash -= trade_notional + fee
            positions_state[sig.asset] = {
                "asset": sig.asset,
                "quantity": round(qty, 6),
                "entry_price": round(sig.current_price, 4),
                "peak_price": round(sig.current_price, 4),
                "notional_usdt": round(trade_notional, 2),
                "entry_fee_usdt": round(fee, 4),
                "opened_at": now_utc.isoformat(),
                "entry_effective_bps": round(sig.effective_bps, 2),
                "entry_reason": sig.reason,
            }

        state["cash"] = round(cash, 4)
        self._save_portfolio_state(state)

        for o, f in order_fills:
            with contextlib.suppress(Exception):
                self.storage.apply_order_fill(o, f)

        return signals

    def get_status_summary(self, signals: list[PaperSignal]) -> str:
        """Gera o painel de telemetria em formato markdown/ASCII para terminal e Telegram."""
        state = self._load_portfolio_state()
        cash = float(state.get("cash", 1000.0))
        positions_state: dict[str, dict[str, Any]] = state.get("positions", {})
        closed_count = int(state.get("closed_trades_count", 0))
        win_count = int(state.get("winning_trades_count", 0))
        realized_pnl = float(state.get("realized_pnl_usdt", 0.0))
        win_rate = (win_count / closed_count * 100.0) if closed_count > 0 else 0.0

        now_str = utc_now().strftime("%Y-%m-%d %H:%M:%S UTC")
        price_map = {s.asset: s.current_price for s in signals}
        pos_value = sum(
            float(p["quantity"]) * price_map.get(asset_k, float(p["entry_price"]))
            for asset_k, p in positions_state.items()
            if float(p.get("quantity", 0.0)) > 0
        )
        total_equity = cash + pos_value
        pnl_pct = (total_equity / 1000.0 - 1.0) * 100.0

        lines = [
            "=" * 68,
            "  [BOT] BOTTRADE V5.2 - SWING 12H & CVD ENGINE (ONLINE)",
            f"  Timestamp: {now_str} | Ledger: {self.ledger_name}",
            "=" * 68,
            f"  Patrimonio Liquido Total: ${total_equity:,.2f} USDT ({pnl_pct:+.2f}%)",
            f"  Caixa Disponivel:        ${cash:,.2f} USDT",
            f"  Capital em Posicoes:     ${pos_value:,.2f} USDT",
            f"  Trades Fechados:         {closed_count} (Win Rate: {win_rate:.1f}% | PnL Realizado: ${realized_pnl:+.2f})",
            "-" * 68,
            "  SINAIS & ALPHA COMPOSTO 12H (XGBoost + Order Flow CVD):",
        ]

        for s in signals:
            icon = (
                "[COMPRA]"
                if s.signal == "BUY"
                else ("[VENDA]" if s.signal == "SELL" else ("[HOLD]" if s.signal == "HOLD" else "[CAIXA]"))
            )
            lines.append(
                f"  {icon:<8} {s.asset:<7} | Preco: ${s.current_price:>10,.2f} | Sinal: {s.signal:<4} | "
                f"Alpha: {s.effective_bps:>+5.1f} bps (ML:{s.prediction_bps:+.1f} Flow:{s.flow_bps:+.1f} Gate:{s.threshold_bps:.0f}) | {s.reason}"
            )

        lines.extend([
            "-" * 68,
            "  POSICOES ATIVAS NA CARTEIRA:",
        ])

        active_positions = [p for p in positions_state.values() if float(p.get("quantity", 0.0)) > 0]
        if not active_positions:
            lines.append("  (Nenhuma posicao aberta no momento; aguardando gatilho de assimetria)")
        else:
            for p in active_positions:
                asset_name = str(p["asset"])
                cur_p = price_map.get(asset_name, float(p["entry_price"]))
                entry_p = float(p["entry_price"])
                peak_p = float(p.get("peak_price", entry_p))
                gross_pnl = (cur_p / entry_p - 1.0) * 100.0 if entry_p > 0 else 0.0
                lines.append(
                    f"  [POS] {asset_name:<7} | Qtd: {float(p['quantity']):.4f} | Entrada: ${entry_p:,.2f} | "
                    f"Atual: ${cur_p:,.2f} | Pico: ${peak_p:,.2f} | PnL Aberto: {gross_pnl:+.2f}%"
                )

        lines.append("=" * 68)
        return "\n".join(lines)

    def notify_channels(self, signals: list[PaperSignal], text_summary: str) -> None:
        """Envia notificações via Telegram, GitHub Step Summary e grava reports/LIVE_DASHBOARD.md."""
        if self.alerter.configured:
            self.alerter.send(text_summary)

        state = self._load_portfolio_state()
        cash = float(state.get("cash", 1000.0))
        positions_state: dict[str, dict[str, Any]] = state.get("positions", {})
        trade_history: list[dict[str, Any]] = state.get("trade_history", [])
        closed_count = int(state.get("closed_trades_count", 0))
        win_count = int(state.get("winning_trades_count", 0))
        realized_pnl = float(state.get("realized_pnl_usdt", 0.0))
        win_rate = (win_count / closed_count * 100.0) if closed_count > 0 else 0.0

        now_str = utc_now().strftime("%Y-%m-%d %H:%M:%S UTC")
        price_map = {s.asset: s.current_price for s in signals}
        pos_value = sum(
            float(p["quantity"]) * price_map.get(asset_k, float(p["entry_price"]))
            for asset_k, p in positions_state.items()
            if float(p.get("quantity", 0.0)) > 0
        )
        total_equity = cash + pos_value
        pnl_pct = (total_equity / 1000.0 - 1.0) * 100.0

        md_lines = [
            "# 🤖 BOTTRADE V5.2 - Painel Oficial de Paper Trading (Swing 12h + CVD)",
            f"**Ultima Atualizacao**: `{now_str}` | **Ledger**: `{self.ledger_name}` | **Status**: 🟢 **ONLINE**",
            "",
            "## 💰 Resumo da Carteira",
            f"- **Patrimonio Liquido Total**: **${total_equity:,.2f} USDT** (`{pnl_pct:+.2f}%`)",
            f"- **Caixa Disponivel**: **${cash:,.2f} USDT**",
            f"- **Capital em Posicoes**: **${pos_value:,.2f} USDT**",
            f"- **Trades Realizados**: **{closed_count}** | **Taxa de Acerto (Win Rate)**: **{win_rate:.1f}%** | **PnL Realizado**: **${realized_pnl:+.2f} USDT**",
            "",
            "## 📊 Sinais e Previsoes em Tempo Real (Horizonte 12h + Order Flow CVD)",
            "",
            "| Ativo | Preco Atual | Sinal | Alpha Efetivo (12h) | ML 12h | Impulso CVD | Gate Custo | Status / Diagnostico |",
            "|:---|---:|:---:|---:|---:|---:|---:|:---|",
        ]

        for s in signals:
            badge = (
                "🟢 **BUY**"
                if s.signal == "BUY"
                else (
                    "🔴 **SELL**"
                    if s.signal == "SELL"
                    else ("🟡 **HOLD**" if s.signal == "HOLD" else "⚪ **CASH**")
                )
            )
            md_lines.append(
                f"| **{s.asset}** | ${s.current_price:,.2f} | {badge} | **{s.effective_bps:+.1f} bps** | "
                f"{s.prediction_bps:+.1f} bps | {s.flow_bps:+.1f} bps | {s.threshold_bps:.1f} bps | {s.reason} |"
            )

        md_lines.extend([
            "",
            "## 📈 Posicoes Abertas",
            "",
        ])

        active_positions = [p for p in positions_state.values() if float(p.get("quantity", 0.0)) > 0]
        if not active_positions:
            md_lines.append(
                "> *Nenhuma posicao aberta no momento. Aguardando alinhamento de Alpha 12h >= 36.0 bps com fluxo institucional CVD.*"
            )
        else:
            md_lines.append("| Ativo | Quantidade | Preco Entrada | Preco Atual | Pico Atingido | PnL Aberto (%) |")
            md_lines.append("|:---|---:|---:|---:|---:|---:|")
            for p in active_positions:
                asset_name = str(p["asset"])
                cur_p = price_map.get(asset_name, float(p["entry_price"]))
                entry_p = float(p["entry_price"])
                peak_p = float(p.get("peak_price", entry_p))
                gross_pnl = (cur_p / entry_p - 1.0) * 100.0 if entry_p > 0 else 0.0
                md_lines.append(
                    f"| **{asset_name}** | {float(p['quantity']):.4f} | ${entry_p:,.2f} | "
                    f"${cur_p:,.2f} | ${peak_p:,.2f} | `{gross_pnl:+.2f}%` |"
                )

        if trade_history:
            md_lines.extend([
                "",
                "## 🏆 Historico Recente de Operacoes Fechadas",
                "",
                "| Ativo | Abertura | Fechamento | Entrada | Saida | PnL Liquido (%) | PnL (USDT) | Motivo da Saida |",
                "|:---|:---|:---|---:|---:|---:|---:|:---|",
            ])
            for tr in trade_history[:10]:
                md_lines.append(
                    f"| **{tr['asset']}** | `{str(tr['opened_at'])[:16]}` | `{str(tr['closed_at'])[:16]}` | "
                    f"${float(tr['entry_price']):,.2f} | ${float(tr['exit_price']):,.2f} | "
                    f"**`{float(tr['net_pnl_pct']):+.2f}%`** | `${float(tr['net_pnl_usdt']):+.2f}` | {tr['exit_reason']} |"
                )

        md_content = "\n".join(md_lines) + "\n"

        dashboard_file = Path("reports/LIVE_DASHBOARD.md")
        dashboard_file.parent.mkdir(parents=True, exist_ok=True)
        dashboard_file.write_text(md_content, encoding="utf-8")

        self._save_decision_audit(
            signals=signals,
            now_str=now_str,
            total_equity=total_equity,
            cash=cash,
            active_positions=active_positions,
        )

        summary_env = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary_env:
            with open(summary_env, "a", encoding="utf-8") as f:
                f.write(md_content)

    def _save_decision_audit(
        self,
        signals: list[PaperSignal],
        now_str: str,
        total_equity: float,
        cash: float,
        active_positions: list[dict[str, Any]],
    ) -> None:
        """Salva histórico auditável completo em JSONL e Markdown detalhado."""
        reports_dir = Path("reports")
        reports_dir.mkdir(parents=True, exist_ok=True)

        jsonl_path = reports_dir / "decisions.jsonl"
        cycle_record = {
            "timestamp": now_str,
            "total_equity": round(total_equity, 2),
            "cash": round(cash, 2),
            "signals": [
                {
                    "asset": s.asset,
                    "price": round(s.current_price, 4),
                    "signal": s.signal,
                    "effective_bps": round(s.effective_bps, 2),
                    "pred_mean_bps": round(s.prediction_bps, 2),
                    "flow_bps": round(s.flow_bps, 2),
                    "pred_std_bps": round(s.pred_std_bps, 2),
                    "threshold_bps": round(s.threshold_bps, 2),
                    "member_preds_bps": [round(p, 2) for p in s.member_preds_bps],
                    "cvd_6h": round(s.cvd_6h, 4),
                    "cvd_24h": round(s.cvd_24h, 4),
                    "vol_1h": round(s.ewma_volatility_1h, 4),
                    "vol_ratio": round(s.vol_ratio, 2),
                    "close_to_ema_24": round(s.close_to_ema_24, 4),
                    "close_to_ema_72": round(s.close_to_ema_72, 4),
                    "close_to_ema_168": round(s.close_to_ema_168, 4),
                    "dist_high_24": round(s.dist_high_24, 4),
                    "btc_24h_ret": round(s.btc_24h_ret, 4),
                    "filters": s.filters,
                    "reason": s.reason,
                }
                for s in signals
            ],
            "active_positions": active_positions,
        }
        with open(jsonl_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(cycle_record, ensure_ascii=False) + "\n")

        audit_file = reports_dir / "DECISION_AUDIT.md"
        existing_content = audit_file.read_text(encoding="utf-8") if audit_file.exists() else ""

        header_marker = "<!-- AUDIT_START -->\n"
        old_body = existing_content.split(header_marker, 1)[1] if header_marker in existing_content else ""

        old_blocks = [b.strip() for b in old_body.split("\n---\n") if b.strip()]
        kept_blocks = old_blocks[:35]

        new_block_lines = [
            f"### 🕒 Ciclo `{now_str}` | Patrimônio: **${total_equity:,.2f} USDT** (Caixa: `${cash:,.2f}`)",
            "",
            "| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |",
            "|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|",
        ]
        for s in signals:
            badge = (
                "🟢 **BUY**"
                if s.signal == "BUY"
                else (
                    "🔴 **SELL**"
                    if s.signal == "SELL"
                    else ("🟡 **HOLD**" if s.signal == "HOLD" else "⚪ **CASH**")
                )
            )
            active_filters = [f"`{k}`" for k, v in s.filters.items() if v]
            flt_str = " ".join(active_filters) if active_filters else "Liberado ✅"
            new_block_lines.append(
                f"| **{s.asset}** | ${s.current_price:,.2f} | {badge} | **{s.effective_bps:+.1f} bps** (±{s.pred_std_bps:.1f}) | "
                f"`{s.prediction_bps:+.1f} bps` | `{s.cvd_24h:+.3f} / {s.cvd_6h:+.3f}` | `{s.ewma_volatility_1h*100:.2f}%/h` | {flt_str} | {s.reason} |"
            )

        new_block = "\n".join(new_block_lines)

        header = (
            "# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)\n\n"
            "Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.\n"
            "Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.\n\n"
            f"**Última Atualização**: `{now_str}` | **Ledger**: `{self.ledger_name}`\n\n"
            f"{header_marker}"
        )

        all_blocks = [new_block] + kept_blocks
        full_md = header + "\n\n---\n\n".join(all_blocks) + "\n"
        audit_file.write_text(full_md, encoding="utf-8")
