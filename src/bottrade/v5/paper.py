from __future__ import annotations

import contextlib
import json
import math
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

# Parâmetros Institucionais V6.0 (Regime-Weighted TSMOM CTA Long/Short 1x)
# Validados em 5,5 anos (2021-2026: +144.1%, MaxDD -13.4%, Sharpe +1.15, todos os anos positivos)
V6_PERP_FEE_RT_BPS = 16.0  # 10 bps Binance Futures Taker RT + 6 bps slippage conservador
V6_EMA_FAST = 48  # Tendência 2 dias (48h)
V6_EMA_SLOW = 168  # Tendência 7 dias (168h)
V6_EMA_MACRO = 720  # Regime macro 30 dias (720h)
V6_TREND_BUFFER = 0.008  # Histerese de 0.80% para eliminar ruído lateral
V6_FLAT_BUFFER = 0.0024  # Zona neutra (0.30 * buffer) para saída limpa
V6_ATR_WINDOW = 72  # ATR de 72h para Chandelier Trailing Stop
V6_ATR_STOP_MULT = 5.5  # Chandelier Stop 5.5x ATR(72h)
V6_HARD_STOP_PCT = 0.10  # Trava catastrófica máxima de -10% no ativo (~ -3.3% na carteira)
V6_TARGET_ANN_VOL = 0.30  # Alvo de volatilidade anualizada da carteira (30% a.a. / 1x sem alavancagem)
V6_COUNTER_TREND_SCALE = 0.45  # Peso reduzido (45%) quando contra o regime macro de 30 dias
V6_MAX_ASSET_WEIGHT = 0.33  # Limite máximo de 33% do patrimônio por ativo (1x)


@dataclass
class PaperSignal:
    asset: str
    prediction_bps: float
    effective_bps: float
    threshold_bps: float
    signal: str  # "LONG", "SHORT", "CLOSE", "HOLD_LONG", "HOLD_SHORT", "CASH"
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
    macro_regime: str = "NEUTRAL"
    trend_spread_pct: float = 0.0
    ann_vol_pct: float = 0.0
    atr_stop_price: float = 0.0
    target_weight_pct: float = 0.0
    filters: dict[str, bool] = field(default_factory=dict)


class PaperTradingV5:
    """Motor oficial de Paper Trading V6.0 (Institutional Regime-Weighted CTA Long/Short 1x + ML Tilt)."""

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
            "engine_version": "V6.0-CTA-LS1x",
            "initial_cash": 1000.0,
            "cash": 1000.0,
            "realized_pnl_usdt": 0.0,
            "closed_trades_count": 0,
            "winning_trades_count": 0,
            "positions": {},
            "stopped_sides": {},
            "last_exit_times": {},
            "trade_history": [],
        }
        if self.state_path.exists():
            with contextlib.suppress(Exception):
                loaded = json.loads(self.state_path.read_text(encoding="utf-8"))
                if isinstance(loaded, dict):
                    default_state.update(loaded)
        default_state.setdefault("stopped_sides", {})
        default_state["engine_version"] = "V6.0-CTA-LS1x"
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
        """Obtém os últimos 1.000 candles horários (41,6 dias) de BTC, ETH e SOL para aquecer EMA 720h."""
        market: dict[str, pd.DataFrame] = {}
        if live:
            try:
                for asset in Asset:
                    df = self.binance_client.fetch_recent_klines(asset.value, limit=1000, interval="1h")
                    market[asset.value] = df
                return market
            except Exception:
                pass
        for asset in Asset:
            market[asset.value] = load_raw_market(self.app_config.project.data_dir, asset, "1h").tail(1000).reset_index(drop=True)
        return market

    def _ensure_models_trained(self, market: dict[str, pd.DataFrame]) -> None:
        """Garante que os modelos campeões ONNX de 12h estejam carregados para telemetria e sizing tilt."""
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

    @staticmethod
    def _position_gross_return(pos: dict[str, Any], cur_price: float) -> float:
        entry_p = float(pos.get("entry_price", 0.0))
        if entry_p <= 0:
            return 0.0
        side = str(pos.get("side", "LONG")).upper()
        if side == "SHORT":
            return 1.0 - (cur_price / entry_p)
        return (cur_price / entry_p) - 1.0

    @staticmethod
    def _position_equity_value(pos: dict[str, Any], cur_price: float) -> float:
        notional = float(pos.get("notional_usdt", float(pos.get("quantity", 0.0)) * float(pos.get("entry_price", 0.0))))
        gross = PaperTradingV5._position_gross_return(pos, cur_price)
        return max(0.0, notional * (1.0 + gross))

    @staticmethod
    def _compute_cta_indicators(df: pd.DataFrame) -> dict[str, float]:
        """Calcula indicadores institucionais CTA (EMA 48/168/720, ATR 72h e Volatilidade Anualizada 168h)."""
        close = df["close"].astype(float)
        high = df["high"].astype(float)
        low = df["low"].astype(float)

        tr = pd.concat(
            [(high - low), (high - close.shift(1)).abs(), (low - close.shift(1)).abs()],
            axis=1,
        ).max(axis=1)
        atr_72 = float(tr.rolling(V6_ATR_WINDOW).mean().iloc[-1])
        cur = float(close.iloc[-1])
        if not np.isfinite(atr_72) or atr_72 <= 0:
            atr_72 = cur * 0.015

        vol_168 = float(close.pct_change().rolling(168).std().iloc[-1])
        if not np.isfinite(vol_168) or vol_168 <= 0:
            vol_168 = 0.008
        ann_vol = vol_168 * math.sqrt(8760.0)

        ema_48 = float(close.ewm(span=V6_EMA_FAST, adjust=False).mean().iloc[-1])
        ema_168 = float(close.ewm(span=V6_EMA_SLOW, adjust=False).mean().iloc[-1])
        ema_720 = float(close.ewm(span=V6_EMA_MACRO, adjust=False).mean().iloc[-1])
        trend_spread = (ema_48 / ema_168 - 1.0) if ema_168 > 0 else 0.0

        return {
            "close": cur,
            "ema_48": ema_48,
            "ema_168": ema_168,
            "ema_720": ema_720,
            "atr_72": atr_72,
            "vol_168": vol_168,
            "ann_vol": ann_vol,
            "trend_spread": trend_spread,
        }

    def execute_cycle(self, live: bool = True) -> list[PaperSignal]:
        """Executa um ciclo completo do motor V6.0 Institutional Regime-Weighted CTA (Long/Short 1x)."""
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
        stopped_sides: dict[str, str] = state.setdefault("stopped_sides", {})
        last_exits: dict[str, str] = state.setdefault("last_exit_times", {})
        trade_history: list[dict[str, Any]] = state.setdefault("trade_history", [])

        btc_features = build_features(asset=Asset.BTCUSDT, market=market, intrahour=None, config=v4_compat)
        btc_latest = btc_features.iloc[-1]
        btc_24h_ret = float(btc_latest.get("return_24h", 0.0))
        btc_cvd_24h = float(btc_latest.get("cvd_ratio_24h", 0.0))

        fee_side = V6_PERP_FEE_RT_BPS / 20_000.0
        order_fills: list[tuple[PaperOrder, PaperFill]] = []

        # Pré-calcular preços atuais para equity mark-to-market precisa
        price_lookup = {
            asset.value: float(market[asset.value].iloc[-1]["close"])
            for asset in (Asset.BTCUSDT, Asset.ETHUSDT, Asset.SOLUSDT)
        }

        for asset in (Asset.BTCUSDT, Asset.ETHUSDT, Asset.SOLUSDT):
            df_asset = market[asset.value]
            cta = self._compute_cta_indicators(df_asset)
            curr_price = cta["close"]
            ema_168 = cta["ema_168"]
            ema_720 = cta["ema_720"]
            atr_72 = cta["atr_72"]
            ann_vol = cta["ann_vol"]
            trend_spread = cta["trend_spread"]

            # Telemetria auxiliar (features V4 + Ensemble 5x XGBoost ONNX para ML Conviction Tilt)
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
            flow_bps = (cvd_24h * 120.0) + (cvd_6h * 80.0) + (btc_cvd_24h * 60.0)

            # 1. Direção de Tendência Institucional TSMOM (EMA 48h vs EMA 168h com histerese de 0.80%)
            macro_bull = ema_168 >= ema_720
            macro_regime = "MACRO_BULL" if macro_bull else "MACRO_BEAR"

            raw_dir: str | None = None
            if trend_spread > V6_TREND_BUFFER and curr_price > ema_168:
                raw_dir = "LONG"
            elif trend_spread < -V6_TREND_BUFFER and curr_price < ema_168:
                raw_dir = "SHORT"
            elif abs(trend_spread) <= V6_FLAT_BUFFER:
                raw_dir = "FLAT"

            # Limpar bloqueio pós-Stop somente quando a tendência realmente neutralizar ou inverter
            if asset.value in stopped_sides and raw_dir is not None and raw_dir != stopped_sides[asset.value]:
                stopped_sides.pop(asset.value, None)

            stop_locked = stopped_sides.get(asset.value) == raw_dir if raw_dir in ("LONG", "SHORT") else False

            pos_info = positions_state.get(asset.value)
            has_pos = pos_info is not None and float(pos_info.get("quantity", 0.0)) > 0.0

            signal_label = "CASH"
            reason = f"Tendência neutra ({trend_spread*100:+.2f}% dentro do buffer ±{V6_TREND_BUFFER*100:.2f}%)"
            atr_stop_price = 0.0
            target_weight_pct = 0.0

            # 2. Gestão de Posição Aberta (Saída por Reversão de Tendência, Chandelier ATR 5.5x ou Hard Stop)
            closed_this_cycle = False
            if has_pos and pos_info is not None:
                pos_side = str(pos_info.get("side", "LONG")).upper()
                entry_p = float(pos_info["entry_price"])
                gross = self._position_gross_return(pos_info, curr_price)

                opened_dt = now_utc
                with contextlib.suppress(Exception):
                    opened_dt = datetime.fromisoformat(str(pos_info.get("opened_at", now_utc.isoformat())))
                held_hours = max(0.0, (now_utc - opened_dt).total_seconds() / 3600.0)

                if pos_side == "LONG":
                    peak_p = max(float(pos_info.get("peak_price", entry_p)), curr_price)
                    pos_info["peak_price"] = round(peak_p, 4)
                    atr_stop_price = peak_p - (V6_ATR_STOP_MULT * atr_72)
                    atr_hit = curr_price <= atr_stop_price
                    best_pct = (peak_p / entry_p - 1.0) * 100.0 if entry_p > 0 else 0.0
                else:
                    trough_p = min(float(pos_info.get("trough_price", entry_p)), curr_price)
                    pos_info["trough_price"] = round(trough_p, 4)
                    atr_stop_price = trough_p + (V6_ATR_STOP_MULT * atr_72)
                    atr_hit = curr_price >= atr_stop_price
                    best_pct = (1.0 - trough_p / entry_p) * 100.0 if entry_p > 0 else 0.0

                pos_info["atr_stop_price"] = round(atr_stop_price, 4)

                exit_reason: str | None = None
                is_stop_exit = False
                if gross <= -V6_HARD_STOP_PCT:
                    exit_reason = f"Hard Stop catastrófico {pos_side} ({gross*100:+.2f}%)"
                    is_stop_exit = True
                elif raw_dir is not None and raw_dir != pos_side:
                    exit_reason = f"Inversão de tendência TSMOM {pos_side} -> {raw_dir} ({gross*100:+.2f}%)"
                elif atr_hit:
                    exit_reason = (
                        f"Chandelier ATR(5.5x) {pos_side} acionado "
                        f"(stop ${atr_stop_price:,.2f} · melhor {best_pct:+.2f}% · realizou {gross*100:+.2f}%)"
                    )
                    is_stop_exit = True

                if exit_reason is not None:
                    qty = float(pos_info["quantity"])
                    entry_notional = float(pos_info.get("notional_usdt", qty * entry_p))
                    entry_fee = float(pos_info.get("entry_fee_usdt", entry_notional * fee_side))
                    gross_pnl_usdt = entry_notional * gross
                    exit_notional = max(0.0, entry_notional * (1.0 + gross))
                    exit_fee = exit_notional * fee_side
                    net_pnl_usdt = gross_pnl_usdt - entry_fee - exit_fee
                    net_pct = (net_pnl_usdt / entry_notional) * 100.0 if entry_notional > 0 else 0.0

                    close_side = "SELL" if pos_side == "LONG" else "BUY"
                    order_id = f"v6-{asset.value}-CLOSE-{pos_side}-{now_utc.strftime('%Y%m%d%H%M%S')}"
                    order = PaperOrder(
                        client_order_id=order_id,
                        ledger=self.ledger_name,
                        asset=asset,
                        as_of=now_utc,
                        side=close_side,
                        quantity=Decimal(f"{qty:.6f}"),
                        reference_price=Decimal(f"{curr_price:.4f}"),
                        reason=exit_reason[:120],
                    )
                    fill = PaperFill(
                        client_order_id=order_id,
                        ledger=self.ledger_name,
                        asset=asset,
                        as_of=now_utc,
                        side=close_side,
                        quantity=Decimal(f"{qty:.6f}"),
                        price=Decimal(f"{curr_price:.4f}"),
                        fee=Decimal(f"{exit_fee:.6f}"),
                        bid=Decimal(f"{curr_price * 0.9998:.4f}"),
                        ask=Decimal(f"{curr_price * 1.0002:.4f}"),
                        visible_depth_quantity=Decimal("10.0"),
                        visible_depth_notional=Decimal("500000.0"),
                        spread_bps=4.0,
                        impact_bps=0.0,
                    )
                    order_fills.append((order, fill))
                    cash += exit_notional - exit_fee

                    state["realized_pnl_usdt"] = round(float(state.get("realized_pnl_usdt", 0.0)) + net_pnl_usdt, 4)
                    state["closed_trades_count"] = int(state.get("closed_trades_count", 0)) + 1
                    if net_pnl_usdt > 0:
                        state["winning_trades_count"] = int(state.get("winning_trades_count", 0)) + 1

                    trade_record = {
                        "asset": asset.value,
                        "side": pos_side,
                        "opened_at": pos_info.get("opened_at", ""),
                        "closed_at": now_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
                        "entry_price": round(entry_p, 4),
                        "exit_price": round(curr_price, 4),
                        "quantity": round(qty, 6),
                        "gross_pnl_pct": round(gross * 100.0, 2),
                        "net_pnl_pct": round(net_pct, 2),
                        "net_pnl_usdt": round(net_pnl_usdt, 2),
                        "exit_reason": exit_reason,
                    }
                    trade_history.insert(0, trade_record)
                    state["trade_history"] = trade_history[:50]
                    last_exits[asset.value] = now_utc.isoformat()
                    if is_stop_exit:
                        stopped_sides[asset.value] = pos_side
                        stop_locked = True
                    positions_state.pop(asset.value, None)
                    has_pos = False
                    closed_this_cycle = True
                    signal_label = "CLOSE"
                    reason = exit_reason
                else:
                    signal_label = f"HOLD_{pos_side}"
                    reason = (
                        f"Posição {pos_side} ativa há {held_hours:.1f}h "
                        f"(PnL: {gross*100:+.2f}% · Stop ATR: ${atr_stop_price:,.2f} · {macro_regime})"
                    )

            # 3. Nova Entrada Institucional (Permite reversão imediata se fechou por Flip para lado oposto)
            if not has_pos and raw_dir in ("LONG", "SHORT") and not stop_locked:
                is_aligned = (raw_dir == "LONG" and macro_bull) or (raw_dir == "SHORT" and not macro_bull)
                regime_scale = 1.0 if is_aligned else V6_COUNTER_TREND_SCALE

                # ML Conviction Tilt (XGBoost 5x ONNX ajusta tamanho em ±15% sem travar a tendência macro)
                ml_tilt = 1.0
                if pred_std_bps <= 20.0:
                    if (raw_dir == "LONG" and pred_mean_bps >= 15.0) or (raw_dir == "SHORT" and pred_mean_bps <= -15.0):
                        ml_tilt = 1.15
                    elif (raw_dir == "LONG" and pred_mean_bps <= -35.0) or (raw_dir == "SHORT" and pred_mean_bps >= 35.0):
                        ml_tilt = 0.80

                # Dimensionamento Inverso à Volatilidade (Volatility Targeting 30% a.a., 1x sem alavancagem)
                vol_weight = ((V6_TARGET_ANN_VOL / 3.0) / max(0.25, ann_vol)) * regime_scale * ml_tilt
                weight = min(V6_MAX_ASSET_WEIGHT * regime_scale, max(0.10 * regime_scale, vol_weight))
                target_weight_pct = weight * 100.0

                open_eq = sum(
                    self._position_equity_value(p, price_lookup.get(k, float(p["entry_price"])))
                    for k, p in positions_state.items()
                    if float(p.get("quantity", 0.0)) > 0
                )
                total_eq = cash + open_eq
                trade_notional = min(cash * 0.95, total_eq * weight)

                if trade_notional >= 50.0:
                    qty = trade_notional / curr_price
                    entry_fee = trade_notional * fee_side
                    order_side = "BUY" if raw_dir == "LONG" else "SELL"
                    order_id = f"v6-{asset.value}-OPEN-{raw_dir}-{now_utc.strftime('%Y%m%d%H%M%S')}"
                    align_tag = "A Favor do Macro" if is_aligned else f"Contra-Macro ({int(regime_scale*100)}%)"
                    atr_stop_price = (
                        curr_price - V6_ATR_STOP_MULT * atr_72
                        if raw_dir == "LONG"
                        else curr_price + V6_ATR_STOP_MULT * atr_72
                    )
                    entry_reason = (
                        f"Entrada CTA {raw_dir} 1x [{align_tag}] · "
                        f"Spread EMA48/168: {trend_spread*100:+.2f}% · Peso: {weight*100:.1f}% · "
                        f"Stop ATR: ${atr_stop_price:,.2f}"
                    )

                    order = PaperOrder(
                        client_order_id=order_id,
                        ledger=self.ledger_name,
                        asset=asset,
                        as_of=now_utc,
                        side=order_side,
                        quantity=Decimal(f"{qty:.6f}"),
                        reference_price=Decimal(f"{curr_price:.4f}"),
                        reason=entry_reason[:120],
                    )
                    fill = PaperFill(
                        client_order_id=order_id,
                        ledger=self.ledger_name,
                        asset=asset,
                        as_of=now_utc,
                        side=order_side,
                        quantity=Decimal(f"{qty:.6f}"),
                        price=Decimal(f"{curr_price:.4f}"),
                        fee=Decimal(f"{entry_fee:.6f}"),
                        bid=Decimal(f"{curr_price * 0.9998:.4f}"),
                        ask=Decimal(f"{curr_price * 1.0002:.4f}"),
                        visible_depth_quantity=Decimal("10.0"),
                        visible_depth_notional=Decimal("500000.0"),
                        spread_bps=4.0,
                        impact_bps=0.0,
                    )
                    order_fills.append((order, fill))
                    cash -= trade_notional + entry_fee
                    positions_state[asset.value] = {
                        "asset": asset.value,
                        "side": raw_dir,
                        "quantity": round(qty, 6),
                        "entry_price": round(curr_price, 4),
                        "peak_price": round(curr_price, 4),
                        "trough_price": round(curr_price, 4),
                        "atr_stop_price": round(atr_stop_price, 4),
                        "notional_usdt": round(trade_notional, 2),
                        "entry_fee_usdt": round(entry_fee, 4),
                        "opened_at": now_utc.isoformat(),
                        "macro_regime": macro_regime,
                        "entry_ml_bps": round(pred_mean_bps, 2),
                        "entry_reason": entry_reason,
                    }
                    signal_label = raw_dir
                    reason = entry_reason
            elif not has_pos and not closed_this_cycle and stop_locked:
                signal_label = "CASH"
                reason = f"Bloqueio anti-whipsaw pós-Stop ({stopped_sides.get(asset.value)}); aguardando reset de tendência"

            signals.append(
                PaperSignal(
                    asset=asset.value,
                    prediction_bps=pred_mean_bps,
                    effective_bps=trend_spread * 10_000.0,
                    threshold_bps=V6_TREND_BUFFER * 10_000.0,
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
                    macro_regime=macro_regime,
                    trend_spread_pct=trend_spread * 100.0,
                    ann_vol_pct=ann_vol * 100.0,
                    atr_stop_price=atr_stop_price,
                    target_weight_pct=target_weight_pct,
                    filters={
                        "stop_locked": bool(stop_locked),
                        "macro_bear": not macro_bull,
                        "neutral_zone": raw_dir is None or raw_dir == "FLAT",
                    },
                )
            )

        state["cash"] = round(cash, 4)
        self._save_portfolio_state(state)

        for o, f in order_fills:
            with contextlib.suppress(Exception):
                self.storage.apply_order_fill(o, f)

        return signals

    def get_status_summary(self, signals: list[PaperSignal]) -> str:
        """Gera o painel de telemetria em formato ASCII para terminal e Telegram."""
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
            self._position_equity_value(p, price_map.get(asset_k, float(p["entry_price"])))
            for asset_k, p in positions_state.items()
            if float(p.get("quantity", 0.0)) > 0
        )
        total_equity = cash + pos_value
        pnl_pct = (total_equity / 1000.0 - 1.0) * 100.0

        lines = [
            "=" * 74,
            "  [BOT] BOTTRADE V6.0 - INSTITUTIONAL CTA LONG/SHORT 1X (ONLINE)",
            f"  Timestamp: {now_str} | Ledger: {self.ledger_name}",
            "=" * 74,
            f"  Patrimonio Liquido Total: ${total_equity:,.2f} USDT ({pnl_pct:+.2f}%)",
            f"  Caixa Disponivel:        ${cash:,.2f} USDT",
            f"  Margem em Posicoes (1x): ${pos_value:,.2f} USDT",
            f"  Trades Fechados:         {closed_count} (Win Rate: {win_rate:.1f}% | PnL Realizado: ${realized_pnl:+.2f})",
            "-" * 74,
            "  SINAIS CTA (TSMOM EMA 48h/168h/720h + Volatility Targeting + ML Tilt):",
        ]

        for s in signals:
            icon_map = {
                "LONG": "[LONG]",
                "SHORT": "[SHORT]",
                "CLOSE": "[CLOSE]",
                "HOLD_LONG": "[H-LONG]",
                "HOLD_SHORT": "[H-SHRT]",
                "CASH": "[CAIXA]",
            }
            icon = icon_map.get(s.signal, "[CAIXA]")
            lines.append(
                f"  {icon:<8} {s.asset:<7} | Preco: ${s.current_price:>10,.2f} | "
                f"EMA48/168: {s.trend_spread_pct:>+5.2f}% | {s.macro_regime:<10} | "
                f"ML12h: {s.prediction_bps:>+5.1f} bps | {s.reason}"
            )

        lines.extend([
            "-" * 74,
            "  POSICOES ATIVAS NA CARTEIRA (1x SEM ALAVANCAGEM):",
        ])

        active_positions = [p for p in positions_state.values() if float(p.get("quantity", 0.0)) > 0]
        if not active_positions:
            lines.append("  (Nenhuma posicao aberta no momento; aguardando rompimento TSMOM ±0.80%)")
        else:
            for p in active_positions:
                asset_name = str(p["asset"])
                side = str(p.get("side", "LONG")).upper()
                cur_p = price_map.get(asset_name, float(p["entry_price"]))
                entry_p = float(p["entry_price"])
                stop_p = float(p.get("atr_stop_price", 0.0))
                gross_pnl = self._position_gross_return(p, cur_p) * 100.0
                notional = float(p.get("notional_usdt", 0.0))
                lines.append(
                    f"  [{side:<5}] {asset_name:<7} | Notional: ${notional:>6,.2f} | "
                    f"Entrada: ${entry_p:,.2f} | Atual: ${cur_p:,.2f} | "
                    f"Stop ATR: ${stop_p:,.2f} | PnL Aberto: {gross_pnl:+.2f}%"
                )

        lines.append("=" * 74)
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
            self._position_equity_value(p, price_map.get(asset_k, float(p["entry_price"])))
            for asset_k, p in positions_state.items()
            if float(p.get("quantity", 0.0)) > 0
        )
        total_equity = cash + pos_value
        pnl_pct = (total_equity / 1000.0 - 1.0) * 100.0

        md_lines = [
            "# 🤖 BOTTRADE V6.0 - Painel Oficial de Paper Trading (Institutional CTA Long/Short 1x)",
            f"**Ultima Atualizacao**: `{now_str}` | **Ledger**: `{self.ledger_name}` | **Status**: 🟢 **ONLINE**",
            "",
            "## 💰 Resumo da Carteira (1x Sem Alavancagem)",
            f"- **Patrimonio Liquido Total**: **${total_equity:,.2f} USDT** (`{pnl_pct:+.2f}%`)",
            f"- **Caixa Disponivel**: **${cash:,.2f} USDT**",
            f"- **Capital em Posicoes (Long + Short 1x)**: **${pos_value:,.2f} USDT**",
            f"- **Trades Realizados**: **{closed_count}** | **Taxa de Acerto (Win Rate)**: **{win_rate:.1f}%** | **PnL Realizado**: **${realized_pnl:+.2f} USDT**",
            "",
            "## 📊 Sinais CTA em Tempo Real (TSMOM EMA 48h/168h/720h + Volatility Targeting + ML Tilt)",
            "",
            "| Ativo | Preco Atual | Sinal | Spread EMA48/168 | Regime Macro (30d) | Vol Anual | ML 12h | Status / Diagnostico |",
            "|:---|---:|:---:|---:|:---:|---:|---:|:---|",
        ]

        badge_map = {
            "LONG": "🟢 **LONG**",
            "SHORT": "🔴 **SHORT**",
            "CLOSE": "🚪 **CLOSE**",
            "HOLD_LONG": "🟡 **HOLD LONG**",
            "HOLD_SHORT": "🟠 **HOLD SHORT**",
            "CASH": "⚪ **CASH**",
        }

        for s in signals:
            badge = badge_map.get(s.signal, "⚪ **CASH**")
            md_lines.append(
                f"| **{s.asset}** | ${s.current_price:,.2f} | {badge} | **{s.trend_spread_pct:+.2f}%** | "
                f"`{s.macro_regime}` | `{s.ann_vol_pct:.0f}%` | `{s.prediction_bps:+.1f} bps` | {s.reason} |"
            )

        md_lines.extend([
            "",
            "## 📈 Posicoes Abertas (Long & Short 1x)",
            "",
        ])

        active_positions = [p for p in positions_state.values() if float(p.get("quantity", 0.0)) > 0]
        if not active_positions:
            md_lines.append(
                "> *Nenhuma posicao aberta no momento. Aguardando confirmacao de tendencia TSMOM (EMA48/168 fora da zona neutra ±0.80%).*"
            )
        else:
            md_lines.append("| Ativo | Lado | Margem (USDT) | Preco Entrada | Preco Atual | Stop ATR (5.5x) | PnL Aberto (%) |")
            md_lines.append("|:---|:---:|---:|---:|---:|---:|---:|")
            for p in active_positions:
                asset_name = str(p["asset"])
                side = str(p.get("side", "LONG")).upper()
                side_badge = "🟢 LONG" if side == "LONG" else "🔴 SHORT"
                cur_p = price_map.get(asset_name, float(p["entry_price"]))
                entry_p = float(p["entry_price"])
                stop_p = float(p.get("atr_stop_price", 0.0))
                notional = float(p.get("notional_usdt", 0.0))
                gross_pnl = self._position_gross_return(p, cur_p) * 100.0
                md_lines.append(
                    f"| **{asset_name}** | {side_badge} | ${notional:,.2f} | ${entry_p:,.2f} | "
                    f"${cur_p:,.2f} | ${stop_p:,.2f} | **`{gross_pnl:+.2f}%`** |"
                )

        if trade_history:
            md_lines.extend([
                "",
                "## 🏆 Historico Recente de Operacoes Fechadas",
                "",
                "| Ativo | Lado | Abertura | Fechamento | Entrada | Saida | PnL Liquido (%) | PnL (USDT) | Motivo da Saida |",
                "|:---|:---:|:---|:---|---:|---:|---:|---:|:---|",
            ])
            for tr in trade_history[:10]:
                tr_side = str(tr.get("side", "LONG")).upper()
                md_lines.append(
                    f"| **{tr['asset']}** | `{tr_side}` | `{str(tr['opened_at'])[:16]}` | `{str(tr['closed_at'])[:16]}` | "
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
            "engine_version": "V6.0-CTA-LS1x",
            "total_equity": round(total_equity, 2),
            "cash": round(cash, 2),
            "signals": [
                {
                    "asset": s.asset,
                    "price": round(s.current_price, 4),
                    "signal": s.signal,
                    "macro_regime": s.macro_regime,
                    "trend_spread_pct": round(s.trend_spread_pct, 3),
                    "ann_vol_pct": round(s.ann_vol_pct, 1),
                    "atr_stop_price": round(s.atr_stop_price, 4),
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

        badge_map = {
            "LONG": "🟢 **LONG**",
            "SHORT": "🔴 **SHORT**",
            "CLOSE": "🚪 **CLOSE**",
            "HOLD_LONG": "🟡 **HOLD LONG**",
            "HOLD_SHORT": "🟠 **HOLD SHORT**",
            "CASH": "⚪ **CASH**",
        }

        new_block_lines = [
            f"### 🕒 Ciclo `{now_str}` | Patrimônio: **${total_equity:,.2f} USDT** (Caixa: `${cash:,.2f}`)",
            "",
            "| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |",
            "|:---|---:|:---:|---:|:---:|---:|---:|:---|",
        ]
        for s in signals:
            badge = badge_map.get(s.signal, "⚪ **CASH**")
            new_block_lines.append(
                f"| **{s.asset}** | ${s.current_price:,.2f} | {badge} | **{s.trend_spread_pct:+.2f}%** | "
                f"`{s.macro_regime}` | `{s.ann_vol_pct:.0f}%` | `{s.prediction_bps:+.1f} bps` | {s.reason} |"
            )

        new_block = "\n".join(new_block_lines)

        header = (
            "# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)\n\n"
            "Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.\n"
            "Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.\n\n"
            f"**Última Atualização**: `{now_str}` | **Ledger**: `{self.ledger_name}`\n\n"
            f"{header_marker}"
        )

        all_blocks = [new_block] + kept_blocks
        full_md = header + "\n\n---\n\n".join(all_blocks) + "\n"
        audit_file.write_text(full_md, encoding="utf-8")
