# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-22 03:45:43 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-22 03:45:43 UTC` | Patrimônio: **$976.86 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,234.57 | ⚪ **CASH** | **-4.68%** | `MACRO_BEAR` | `71%` | `-6.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,659.75 | ⚪ **CASH** | **-4.96%** | `MACRO_BEAR` | `82%` | `-22.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.37 | 🟠 **HOLD SHORT** | **-3.60%** | `MACRO_BEAR` | `85%` | `+23.0 bps` | Posição SHORT ativa há 56.3h (PnL: +6.08% · Stop ATR: $70.67 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 03:30:54 UTC` | Patrimônio: **$976.62 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,327.41 | ⚪ **CASH** | **-4.68%** | `MACRO_BEAR` | `71%` | `-6.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,662.51 | ⚪ **CASH** | **-4.96%** | `MACRO_BEAR` | `82%` | `-22.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.53 | 🟠 **HOLD SHORT** | **-3.59%** | `MACRO_BEAR` | `85%` | `+23.0 bps` | Posição SHORT ativa há 56.1h (PnL: +5.86% · Stop ATR: $70.67 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 03:15:54 UTC` | Patrimônio: **$976.83 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,329.40 | ⚪ **CASH** | **-4.68%** | `MACRO_BEAR` | `71%` | `-6.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,663.17 | ⚪ **CASH** | **-4.96%** | `MACRO_BEAR` | `82%` | `-22.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.39 | 🟠 **HOLD SHORT** | **-3.60%** | `MACRO_BEAR` | `85%` | `+23.0 bps` | Posição SHORT ativa há 55.8h (PnL: +6.05% · Stop ATR: $70.67 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 03:00:48 UTC` | Patrimônio: **$976.49 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,501.75 | ⚪ **CASH** | **-4.67%** | `MACRO_BEAR` | `71%` | `-6.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,672.01 | ⚪ **CASH** | **-4.94%** | `MACRO_BEAR` | `82%` | `-22.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.61 | 🟠 **HOLD SHORT** | **-3.59%** | `MACRO_BEAR` | `85%` | `+23.0 bps` | Posição SHORT ativa há 55.6h (PnL: +5.75% · Stop ATR: $70.64 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 02:45:47 UTC` | Patrimônio: **$976.63 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,549.35 | ⚪ **CASH** | **-4.70%** | `MACRO_BEAR` | `71%` | `-36.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,668.51 | ⚪ **CASH** | **-4.98%** | `MACRO_BEAR` | `82%` | `-42.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.52 | 🟠 **HOLD SHORT** | **-3.61%** | `MACRO_BEAR` | `85%` | `+24.2 bps` | Posição SHORT ativa há 55.3h (PnL: +5.88% · Stop ATR: $70.74 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 02:30:53 UTC` | Patrimônio: **$976.00 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,784.15 | ⚪ **CASH** | **-4.68%** | `MACRO_BEAR` | `71%` | `-36.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,678.11 | ⚪ **CASH** | **-4.97%** | `MACRO_BEAR` | `81%` | `-42.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.93 | 🟠 **HOLD SHORT** | **-3.59%** | `MACRO_BEAR` | `84%` | `+24.2 bps` | Posição SHORT ativa há 55.1h (PnL: +5.32% · Stop ATR: $70.71 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 02:15:43 UTC` | Patrimônio: **$975.45 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,036.11 | ⚪ **CASH** | **-4.67%** | `MACRO_BEAR` | `71%` | `-36.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,685.64 | ⚪ **CASH** | **-4.96%** | `MACRO_BEAR` | `81%` | `-42.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.29 | 🟠 **HOLD SHORT** | **-3.57%** | `MACRO_BEAR` | `84%` | `+24.2 bps` | Posição SHORT ativa há 54.8h (PnL: +4.83% · Stop ATR: $70.68 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 02:00:57 UTC` | Patrimônio: **$975.29 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,159.00 | ⚪ **CASH** | **-4.67%** | `MACRO_BEAR` | `71%` | `-36.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,687.75 | ⚪ **CASH** | **-4.95%** | `MACRO_BEAR` | `81%` | `-42.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.39 | 🟠 **HOLD SHORT** | **-3.57%** | `MACRO_BEAR` | `84%` | `+24.2 bps` | Posição SHORT ativa há 54.6h (PnL: +4.70% · Stop ATR: $70.67 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 01:45:51 UTC` | Patrimônio: **$975.39 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,119.99 | ⚪ **CASH** | **-4.72%** | `MACRO_BEAR` | `76%` | `-35.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,686.93 | ⚪ **CASH** | **-5.02%** | `MACRO_BEAR` | `89%` | `-38.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.33 | 🟠 **HOLD SHORT** | **-3.62%** | `MACRO_BEAR` | `92%` | `+25.9 bps` | Posição SHORT ativa há 54.3h (PnL: +4.78% · Stop ATR: $70.70 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 01:30:54 UTC` | Patrimônio: **$975.46 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,094.28 | ⚪ **CASH** | **-4.72%** | `MACRO_BEAR` | `76%` | `-35.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,684.25 | ⚪ **CASH** | **-5.02%** | `MACRO_BEAR` | `89%` | `-38.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.28 | 🟠 **HOLD SHORT** | **-3.62%** | `MACRO_BEAR` | `92%` | `+25.9 bps` | Posição SHORT ativa há 54.1h (PnL: +4.85% · Stop ATR: $70.70 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 01:15:48 UTC` | Patrimônio: **$975.23 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,189.91 | ⚪ **CASH** | **-4.72%** | `MACRO_BEAR` | `75%` | `-35.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,686.14 | ⚪ **CASH** | **-5.02%** | `MACRO_BEAR` | `89%` | `-38.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.43 | 🟠 **HOLD SHORT** | **-3.61%** | `MACRO_BEAR` | `92%` | `+25.9 bps` | Posição SHORT ativa há 53.8h (PnL: +4.64% · Stop ATR: $70.70 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 01:00:54 UTC` | Patrimônio: **$975.42 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,194.85 | ⚪ **CASH** | **-4.72%** | `MACRO_BEAR` | `75%` | `-35.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,683.68 | ⚪ **CASH** | **-5.02%** | `MACRO_BEAR` | `89%` | `-38.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.31 | 🟠 **HOLD SHORT** | **-3.62%** | `MACRO_BEAR` | `92%` | `+25.9 bps` | Posição SHORT ativa há 53.6h (PnL: +4.81% · Stop ATR: $70.69 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 00:45:34 UTC` | Patrimônio: **$975.32 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,252.14 | ⚪ **CASH** | **-4.78%** | `MACRO_BEAR` | `76%` | `-35.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,683.65 | ⚪ **CASH** | **-5.08%** | `MACRO_BEAR` | `89%` | `-21.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.37 | 🟠 **HOLD SHORT** | **-3.66%** | `MACRO_BEAR` | `94%` | `+50.0 bps` | Posição SHORT ativa há 53.3h (PnL: +4.73% · Stop ATR: $70.76 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 00:30:44 UTC` | Patrimônio: **$975.32 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,256.35 | ⚪ **CASH** | **-4.78%** | `MACRO_BEAR` | `76%` | `-35.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,684.02 | ⚪ **CASH** | **-5.08%** | `MACRO_BEAR` | `89%` | `-21.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.37 | 🟠 **HOLD SHORT** | **-3.66%** | `MACRO_BEAR` | `94%` | `+50.0 bps` | Posição SHORT ativa há 53.1h (PnL: +4.73% · Stop ATR: $70.75 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 00:15:40 UTC` | Patrimônio: **$975.37 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,284.22 | ⚪ **CASH** | **-4.77%** | `MACRO_BEAR` | `76%` | `-35.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,684.15 | ⚪ **CASH** | **-5.08%** | `MACRO_BEAR` | `89%` | `-21.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.34 | 🟠 **HOLD SHORT** | **-3.66%** | `MACRO_BEAR` | `94%` | `+50.0 bps` | Posição SHORT ativa há 52.8h (PnL: +4.77% · Stop ATR: $70.75 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 00:00:57 UTC` | Patrimônio: **$975.52 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,190.00 | ⚪ **CASH** | **-4.78%** | `MACRO_BEAR` | `76%` | `-35.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,684.28 | ⚪ **CASH** | **-5.08%** | `MACRO_BEAR` | `89%` | `-21.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.24 | 🟠 **HOLD SHORT** | **-3.67%** | `MACRO_BEAR` | `94%` | `+50.0 bps` | Posição SHORT ativa há 52.6h (PnL: +4.90% · Stop ATR: $70.74 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 23:45:47 UTC` | Patrimônio: **$975.36 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,231.79 | ⚪ **CASH** | **-4.84%** | `MACRO_BEAR` | `76%` | `-31.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,683.99 | ⚪ **CASH** | **-5.14%** | `MACRO_BEAR` | `90%` | `-21.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.35 | 🟠 **HOLD SHORT** | **-3.71%** | `MACRO_BEAR` | `94%` | `+55.5 bps` | Posição SHORT ativa há 52.3h (PnL: +4.75% · Stop ATR: $70.78 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 23:30:52 UTC` | Patrimônio: **$975.43 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,250.01 | ⚪ **CASH** | **-4.84%** | `MACRO_BEAR` | `76%` | `-31.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,683.74 | ⚪ **CASH** | **-5.14%** | `MACRO_BEAR` | `90%` | `-21.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.30 | 🟠 **HOLD SHORT** | **-3.71%** | `MACRO_BEAR` | `94%` | `+55.5 bps` | Posição SHORT ativa há 52.1h (PnL: +4.82% · Stop ATR: $70.78 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 23:15:49 UTC` | Patrimônio: **$975.40 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,275.49 | ⚪ **CASH** | **-4.83%** | `MACRO_BEAR` | `76%` | `-31.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,684.15 | ⚪ **CASH** | **-5.14%** | `MACRO_BEAR` | `90%` | `-21.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.32 | 🟠 **HOLD SHORT** | **-3.71%** | `MACRO_BEAR` | `94%` | `+55.5 bps` | Posição SHORT ativa há 51.8h (PnL: +4.79% · Stop ATR: $70.78 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 23:00:57 UTC` | Patrimônio: **$975.56 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,136.06 | ⚪ **CASH** | **-4.84%** | `MACRO_BEAR` | `76%` | `-31.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,680.26 | ⚪ **CASH** | **-5.15%** | `MACRO_BEAR` | `90%` | `-21.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.22 | 🟠 **HOLD SHORT** | **-3.71%** | `MACRO_BEAR` | `94%` | `+55.5 bps` | Posição SHORT ativa há 51.6h (PnL: +4.93% · Stop ATR: $70.76 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 22:45:45 UTC` | Patrimônio: **$975.71 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,205.35 | ⚪ **CASH** | **-4.90%** | `MACRO_BEAR` | `77%` | `-52.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,680.56 | ⚪ **CASH** | **-5.20%** | `MACRO_BEAR` | `90%` | `-20.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.12 | 🟠 **HOLD SHORT** | **-3.76%** | `MACRO_BEAR` | `95%` | `+49.8 bps` | Posição SHORT ativa há 51.3h (PnL: +5.06% · Stop ATR: $70.86 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 22:30:47 UTC` | Patrimônio: **$975.51 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,321.80 | ⚪ **CASH** | **-4.89%** | `MACRO_BEAR` | `77%` | `-52.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,683.91 | ⚪ **CASH** | **-5.20%** | `MACRO_BEAR` | `90%` | `-20.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.25 | 🟠 **HOLD SHORT** | **-3.75%** | `MACRO_BEAR` | `95%` | `+49.8 bps` | Posição SHORT ativa há 51.1h (PnL: +4.89% · Stop ATR: $70.86 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 22:15:40 UTC` | Patrimônio: **$975.52 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,301.73 | ⚪ **CASH** | **-4.89%** | `MACRO_BEAR` | `77%` | `-52.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,683.50 | ⚪ **CASH** | **-5.20%** | `MACRO_BEAR` | `90%` | `-20.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.24 | 🟠 **HOLD SHORT** | **-3.75%** | `MACRO_BEAR` | `95%` | `+49.8 bps` | Posição SHORT ativa há 50.8h (PnL: +4.90% · Stop ATR: $70.86 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 22:00:54 UTC` | Patrimônio: **$975.25 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,471.52 | ⚪ **CASH** | **-4.88%** | `MACRO_BEAR` | `77%` | `-52.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,688.11 | ⚪ **CASH** | **-5.19%** | `MACRO_BEAR` | `90%` | `-20.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.42 | 🟠 **HOLD SHORT** | **-3.75%** | `MACRO_BEAR` | `95%` | `+49.8 bps` | Posição SHORT ativa há 50.6h (PnL: +4.66% · Stop ATR: $70.83 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 21:45:41 UTC` | Patrimônio: **$975.20 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,419.30 | ⚪ **CASH** | **-4.96%** | `MACRO_BEAR` | `77%` | `-51.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,686.94 | ⚪ **CASH** | **-5.26%** | `MACRO_BEAR` | `91%` | `-25.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.45 | 🟠 **HOLD SHORT** | **-3.79%** | `MACRO_BEAR` | `95%` | `+50.7 bps` | Posição SHORT ativa há 50.3h (PnL: +4.62% · Stop ATR: $70.89 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 21:30:54 UTC` | Patrimônio: **$975.08 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,418.01 | ⚪ **CASH** | **-4.96%** | `MACRO_BEAR` | `77%` | `-51.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,686.45 | ⚪ **CASH** | **-5.26%** | `MACRO_BEAR` | `91%` | `-25.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.53 | 🟠 **HOLD SHORT** | **-3.79%** | `MACRO_BEAR` | `95%` | `+50.7 bps` | Posição SHORT ativa há 50.1h (PnL: +4.51% · Stop ATR: $70.88 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 21:15:44 UTC` | Patrimônio: **$975.02 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,474.59 | ⚪ **CASH** | **-4.96%** | `MACRO_BEAR` | `77%` | `-51.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,687.56 | ⚪ **CASH** | **-5.26%** | `MACRO_BEAR` | `91%` | `-25.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.57 | 🟠 **HOLD SHORT** | **-3.79%** | `MACRO_BEAR` | `95%` | `+50.7 bps` | Posição SHORT ativa há 49.8h (PnL: +4.45% · Stop ATR: $70.87 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 21:00:52 UTC` | Patrimônio: **$974.96 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,489.73 | ⚪ **CASH** | **-4.96%** | `MACRO_BEAR` | `77%` | `-51.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,687.27 | ⚪ **CASH** | **-5.26%** | `MACRO_BEAR` | `91%` | `-25.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.61 | 🟠 **HOLD SHORT** | **-3.79%** | `MACRO_BEAR` | `95%` | `+50.7 bps` | Posição SHORT ativa há 49.6h (PnL: +4.40% · Stop ATR: $70.87 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 20:45:50 UTC` | Patrimônio: **$975.11 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,430.40 | ⚪ **CASH** | **-5.04%** | `MACRO_BEAR` | `77%` | `-42.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,686.08 | ⚪ **CASH** | **-5.33%** | `MACRO_BEAR` | `91%` | `-34.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.51 | 🟠 **HOLD SHORT** | **-3.85%** | `MACRO_BEAR` | `95%` | `+41.7 bps` | Posição SHORT ativa há 49.3h (PnL: +4.54% · Stop ATR: $70.89 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 20:30:46 UTC` | Patrimônio: **$974.93 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,460.25 | ⚪ **CASH** | **-5.03%** | `MACRO_BEAR` | `77%` | `-42.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,687.08 | ⚪ **CASH** | **-5.32%** | `MACRO_BEAR` | `91%` | `-34.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.63 | 🟠 **HOLD SHORT** | **-3.85%** | `MACRO_BEAR` | `95%` | `+41.7 bps` | Posição SHORT ativa há 49.1h (PnL: +4.37% · Stop ATR: $70.89 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 20:15:42 UTC` | Patrimônio: **$975.19 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,322.37 | ⚪ **CASH** | **-5.04%** | `MACRO_BEAR` | `77%` | `-42.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,685.67 | ⚪ **CASH** | **-5.33%** | `MACRO_BEAR` | `91%` | `-34.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.46 | 🟠 **HOLD SHORT** | **-3.85%** | `MACRO_BEAR` | `95%` | `+41.7 bps` | Posição SHORT ativa há 48.8h (PnL: +4.60% · Stop ATR: $70.88 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 20:00:59 UTC` | Patrimônio: **$975.14 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,317.62 | ⚪ **CASH** | **-5.04%** | `MACRO_BEAR` | `77%` | `-42.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,685.54 | ⚪ **CASH** | **-5.33%** | `MACRO_BEAR` | `91%` | `-34.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.49 | 🟠 **HOLD SHORT** | **-3.85%** | `MACRO_BEAR` | `95%` | `+41.7 bps` | Posição SHORT ativa há 48.6h (PnL: +4.56% · Stop ATR: $70.88 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 19:45:49 UTC` | Patrimônio: **$974.76 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,409.55 | ⚪ **CASH** | **-5.11%** | `MACRO_BEAR` | `78%` | `-32.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,688.62 | ⚪ **CASH** | **-5.39%** | `MACRO_BEAR` | `93%` | `-58.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.74 | 🟠 **HOLD SHORT** | **-3.90%** | `MACRO_BEAR` | `97%` | `+42.7 bps` | Posição SHORT ativa há 48.3h (PnL: +4.22% · Stop ATR: $70.89 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 19:30:56 UTC` | Patrimônio: **$974.83 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,331.57 | ⚪ **CASH** | **-5.11%** | `MACRO_BEAR` | `78%` | `-32.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,685.47 | ⚪ **CASH** | **-5.39%** | `MACRO_BEAR` | `93%` | `-58.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.69 | 🟠 **HOLD SHORT** | **-3.90%** | `MACRO_BEAR` | `97%` | `+42.7 bps` | Posição SHORT ativa há 48.1h (PnL: +4.29% · Stop ATR: $70.89 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 19:15:40 UTC` | Patrimônio: **$974.79 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,291.08 | ⚪ **CASH** | **-5.11%** | `MACRO_BEAR` | `78%` | `-32.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,684.75 | ⚪ **CASH** | **-5.40%** | `MACRO_BEAR` | `93%` | `-58.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.72 | 🟠 **HOLD SHORT** | **-3.90%** | `MACRO_BEAR` | `97%` | `+42.7 bps` | Posição SHORT ativa há 47.8h (PnL: +4.25% · Stop ATR: $70.89 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 19:01:01 UTC` | Patrimônio: **$974.79 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,115.89 | ⚪ **CASH** | **-5.12%** | `MACRO_BEAR` | `78%` | `-32.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,681.47 | ⚪ **CASH** | **-5.40%** | `MACRO_BEAR` | `93%` | `-58.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.72 | 🟠 **HOLD SHORT** | **-3.90%** | `MACRO_BEAR` | `97%` | `+42.7 bps` | Posição SHORT ativa há 47.6h (PnL: +4.25% · Stop ATR: $70.87 · MACRO_BEAR) |
