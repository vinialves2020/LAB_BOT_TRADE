# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-22 06:30:49 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-22 06:30:49 UTC` | Patrimônio: **$977.28 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,036.92 | ⚪ **CASH** | **-4.65%** | `MACRO_BEAR` | `71%` | `-2.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,660.28 | ⚪ **CASH** | **-4.90%** | `MACRO_BEAR` | `82%` | `-47.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.10 | 🟠 **HOLD SHORT** | **-3.59%** | `MACRO_BEAR` | `85%` | `-7.4 bps` | Posição SHORT ativa há 59.1h (PnL: +6.44% · Stop ATR: $70.69 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 06:15:49 UTC` | Patrimônio: **$977.39 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,103.92 | ⚪ **CASH** | **-4.65%** | `MACRO_BEAR` | `71%` | `-2.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,660.49 | ⚪ **CASH** | **-4.90%** | `MACRO_BEAR` | `82%` | `-47.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.03 | 🟠 **HOLD SHORT** | **-3.59%** | `MACRO_BEAR` | `85%` | `-7.4 bps` | Posição SHORT ativa há 58.8h (PnL: +6.54% · Stop ATR: $70.68 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 06:00:49 UTC` | Patrimônio: **$977.26 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,037.84 | ⚪ **CASH** | **-4.65%** | `MACRO_BEAR` | `71%` | `-2.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,660.31 | ⚪ **CASH** | **-4.90%** | `MACRO_BEAR` | `82%` | `-47.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.11 | 🟠 **HOLD SHORT** | **-3.59%** | `MACRO_BEAR` | `85%` | `-7.4 bps` | Posição SHORT ativa há 58.6h (PnL: +6.43% · Stop ATR: $70.67 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 05:45:44 UTC` | Patrimônio: **$977.68 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $58,799.22 | ⚪ **CASH** | **-4.66%** | `MACRO_BEAR` | `71%` | `-11.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,649.67 | ⚪ **CASH** | **-4.93%** | `MACRO_BEAR` | `82%` | `-63.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $68.84 | 🟠 **HOLD SHORT** | **-3.60%** | `MACRO_BEAR` | `85%` | `-14.1 bps` | Posição SHORT ativa há 58.3h (PnL: +6.80% · Stop ATR: $70.70 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 05:30:52 UTC` | Patrimônio: **$977.55 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $58,995.94 | ⚪ **CASH** | **-4.65%** | `MACRO_BEAR` | `71%` | `-11.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,653.75 | ⚪ **CASH** | **-4.92%** | `MACRO_BEAR` | `82%` | `-63.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $68.92 | 🟠 **HOLD SHORT** | **-3.59%** | `MACRO_BEAR` | `85%` | `-14.1 bps` | Posição SHORT ativa há 58.1h (PnL: +6.69% · Stop ATR: $70.70 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 05:15:44 UTC` | Patrimônio: **$977.22 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $58,993.61 | ⚪ **CASH** | **-4.65%** | `MACRO_BEAR` | `71%` | `-11.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,659.00 | ⚪ **CASH** | **-4.91%** | `MACRO_BEAR` | `82%` | `-63.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.14 | 🟠 **HOLD SHORT** | **-3.58%** | `MACRO_BEAR` | `85%` | `-14.1 bps` | Posição SHORT ativa há 57.8h (PnL: +6.39% · Stop ATR: $70.67 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 05:00:54 UTC` | Patrimônio: **$976.77 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,310.89 | ⚪ **CASH** | **-4.64%** | `MACRO_BEAR` | `71%` | `-11.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,664.52 | ⚪ **CASH** | **-4.90%** | `MACRO_BEAR` | `82%` | `-63.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.43 | 🟠 **HOLD SHORT** | **-3.57%** | `MACRO_BEAR` | `85%` | `-14.1 bps` | Posição SHORT ativa há 57.6h (PnL: +6.00% · Stop ATR: $70.65 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 04:45:44 UTC` | Patrimônio: **$976.60 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,331.80 | ⚪ **CASH** | **-4.66%** | `MACRO_BEAR` | `71%` | `-1.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,664.04 | ⚪ **CASH** | **-4.93%** | `MACRO_BEAR` | `82%` | `-55.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.54 | 🟠 **HOLD SHORT** | **-3.58%** | `MACRO_BEAR` | `85%` | `+11.9 bps` | Posição SHORT ativa há 57.3h (PnL: +5.85% · Stop ATR: $70.67 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 04:30:54 UTC` | Patrimônio: **$976.71 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,276.96 | ⚪ **CASH** | **-4.66%** | `MACRO_BEAR` | `71%` | `-1.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,662.27 | ⚪ **CASH** | **-4.94%** | `MACRO_BEAR` | `82%` | `-55.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.47 | 🟠 **HOLD SHORT** | **-3.58%** | `MACRO_BEAR` | `85%` | `+11.9 bps` | Posição SHORT ativa há 57.1h (PnL: +5.94% · Stop ATR: $70.67 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 04:15:46 UTC` | Patrimônio: **$976.51 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,486.13 | ⚪ **CASH** | **-4.65%** | `MACRO_BEAR` | `71%` | `-1.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,665.87 | ⚪ **CASH** | **-4.93%** | `MACRO_BEAR` | `82%` | `-55.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.60 | 🟠 **HOLD SHORT** | **-3.58%** | `MACRO_BEAR` | `85%` | `+11.9 bps` | Posição SHORT ativa há 56.8h (PnL: +5.77% · Stop ATR: $70.66 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 04:00:57 UTC` | Patrimônio: **$976.56 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,448.01 | ⚪ **CASH** | **-4.65%** | `MACRO_BEAR` | `71%` | `-1.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,664.08 | ⚪ **CASH** | **-4.93%** | `MACRO_BEAR` | `82%` | `-55.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.57 | 🟠 **HOLD SHORT** | **-3.58%** | `MACRO_BEAR` | `85%` | `+11.9 bps` | Posição SHORT ativa há 56.6h (PnL: +5.81% · Stop ATR: $70.64 · MACRO_BEAR) |

---

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
