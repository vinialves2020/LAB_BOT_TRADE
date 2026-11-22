# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-22 00:30:44 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-11-21 18:45:48 UTC` | Patrimônio: **$974.60 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,170.72 | ⚪ **CASH** | **-5.18%** | `MACRO_BEAR` | `78%` | `-4.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,684.44 | ⚪ **CASH** | **-5.46%** | `MACRO_BEAR` | `93%` | `+17.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.84 | 🟠 **HOLD SHORT** | **-3.97%** | `MACRO_BEAR` | `97%` | `+40.5 bps` | Posição SHORT ativa há 47.3h (PnL: +4.09% · Stop ATR: $70.93 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 18:30:53 UTC` | Patrimônio: **$974.71 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,201.31 | ⚪ **CASH** | **-5.18%** | `MACRO_BEAR` | `78%` | `-4.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,684.73 | ⚪ **CASH** | **-5.46%** | `MACRO_BEAR` | `93%` | `+17.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.77 | 🟠 **HOLD SHORT** | **-3.97%** | `MACRO_BEAR` | `97%` | `+40.5 bps` | Posição SHORT ativa há 47.1h (PnL: +4.18% · Stop ATR: $70.92 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 18:15:47 UTC` | Patrimônio: **$974.77 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,123.05 | ⚪ **CASH** | **-5.19%** | `MACRO_BEAR` | `78%` | `-4.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,681.64 | ⚪ **CASH** | **-5.46%** | `MACRO_BEAR` | `93%` | `+17.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.73 | 🟠 **HOLD SHORT** | **-3.97%** | `MACRO_BEAR` | `97%` | `+40.5 bps` | Posição SHORT ativa há 46.8h (PnL: +4.24% · Stop ATR: $70.92 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 18:00:58 UTC` | Patrimônio: **$974.85 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,084.77 | ⚪ **CASH** | **-5.19%** | `MACRO_BEAR` | `78%` | `-4.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,682.92 | ⚪ **CASH** | **-5.46%** | `MACRO_BEAR` | `93%` | `+17.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.68 | 🟠 **HOLD SHORT** | **-3.97%** | `MACRO_BEAR` | `97%` | `+40.5 bps` | Posição SHORT ativa há 46.6h (PnL: +4.31% · Stop ATR: $70.91 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 17:45:41 UTC` | Patrimônio: **$974.83 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,090.80 | ⚪ **CASH** | **-5.25%** | `MACRO_BEAR` | `78%` | `+9.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,680.84 | ⚪ **CASH** | **-5.52%** | `MACRO_BEAR` | `93%` | `+32.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.69 | 🟠 **HOLD SHORT** | **-4.04%** | `MACRO_BEAR` | `97%` | `+51.9 bps` | Posição SHORT ativa há 46.3h (PnL: +4.29% · Stop ATR: $70.96 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 17:30:41 UTC` | Patrimônio: **$974.82 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,139.99 | ⚪ **CASH** | **-5.25%** | `MACRO_BEAR` | `78%` | `+9.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,682.93 | ⚪ **CASH** | **-5.52%** | `MACRO_BEAR` | `93%` | `+32.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.70 | 🟠 **HOLD SHORT** | **-4.04%** | `MACRO_BEAR` | `97%` | `+51.9 bps` | Posição SHORT ativa há 46.1h (PnL: +4.28% · Stop ATR: $70.95 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 17:15:50 UTC` | Patrimônio: **$974.71 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,214.00 | ⚪ **CASH** | **-5.24%** | `MACRO_BEAR` | `78%` | `+9.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,685.77 | ⚪ **CASH** | **-5.52%** | `MACRO_BEAR` | `93%` | `+32.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.77 | 🟠 **HOLD SHORT** | **-4.03%** | `MACRO_BEAR` | `97%` | `+51.9 bps` | Posição SHORT ativa há 45.8h (PnL: +4.18% · Stop ATR: $70.95 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 17:00:58 UTC` | Patrimônio: **$974.77 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,098.92 | ⚪ **CASH** | **-5.25%** | `MACRO_BEAR` | `78%` | `+9.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,685.59 | ⚪ **CASH** | **-5.52%** | `MACRO_BEAR` | `93%` | `+32.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.73 | 🟠 **HOLD SHORT** | **-4.04%** | `MACRO_BEAR` | `97%` | `+51.9 bps` | Posição SHORT ativa há 45.6h (PnL: +4.24% · Stop ATR: $70.94 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 16:45:45 UTC` | Patrimônio: **$974.93 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,066.20 | ⚪ **CASH** | **-5.31%** | `MACRO_BEAR` | `78%` | `+8.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,685.20 | ⚪ **CASH** | **-5.58%** | `MACRO_BEAR` | `94%` | `+33.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.63 | 🟠 **HOLD SHORT** | **-4.11%** | `MACRO_BEAR` | `97%` | `+62.3 bps` | Posição SHORT ativa há 45.3h (PnL: +4.37% · Stop ATR: $71.03 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 16:30:54 UTC` | Patrimônio: **$975.34 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,008.00 | ⚪ **CASH** | **-5.31%** | `MACRO_BEAR` | `78%` | `+8.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,682.14 | ⚪ **CASH** | **-5.59%** | `MACRO_BEAR` | `94%` | `+33.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.36 | 🟠 **HOLD SHORT** | **-4.12%** | `MACRO_BEAR` | `97%` | `+62.3 bps` | Posição SHORT ativa há 45.1h (PnL: +4.74% · Stop ATR: $71.02 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 16:15:45 UTC` | Patrimônio: **$975.39 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,920.00 | ⚪ **CASH** | **-5.32%** | `MACRO_BEAR` | `78%` | `+8.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,681.15 | ⚪ **CASH** | **-5.59%** | `MACRO_BEAR` | `94%` | `+33.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.33 | 🟠 **HOLD SHORT** | **-4.12%** | `MACRO_BEAR` | `97%` | `+62.3 bps` | Posição SHORT ativa há 44.8h (PnL: +4.78% · Stop ATR: $71.02 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 16:00:56 UTC` | Patrimônio: **$975.28 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,956.28 | ⚪ **CASH** | **-5.32%** | `MACRO_BEAR` | `78%` | `+8.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,684.46 | ⚪ **CASH** | **-5.58%** | `MACRO_BEAR` | `94%` | `+33.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.40 | 🟠 **HOLD SHORT** | **-4.12%** | `MACRO_BEAR` | `97%` | `+62.3 bps` | Posição SHORT ativa há 44.6h (PnL: +4.68% · Stop ATR: $71.00 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 15:45:49 UTC` | Patrimônio: **$975.02 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,116.45 | ⚪ **CASH** | **-5.37%** | `MACRO_BEAR` | `78%` | `+43.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,687.38 | ⚪ **CASH** | **-5.64%** | `MACRO_BEAR` | `94%` | `-8.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.57 | 🟠 **HOLD SHORT** | **-4.17%** | `MACRO_BEAR` | `98%` | `+130.3 bps` | Posição SHORT ativa há 44.3h (PnL: +4.45% · Stop ATR: $71.10 · MACRO_BEAR) |
