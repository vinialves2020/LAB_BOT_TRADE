# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-21 20:45:50 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-11-21 15:30:50 UTC` | Patrimônio: **$975.63 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,886.45 | ⚪ **CASH** | **-5.38%** | `MACRO_BEAR` | `78%` | `+43.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,679.04 | ⚪ **CASH** | **-5.66%** | `MACRO_BEAR` | `94%` | `-8.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.17 | 🟠 **HOLD SHORT** | **-4.18%** | `MACRO_BEAR` | `98%` | `+130.3 bps` | Posição SHORT ativa há 44.1h (PnL: +5.00% · Stop ATR: $71.10 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 15:15:47 UTC` | Patrimônio: **$974.73 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,208.35 | ⚪ **CASH** | **-5.36%** | `MACRO_BEAR` | `78%` | `+43.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,689.86 | ⚪ **CASH** | **-5.64%** | `MACRO_BEAR` | `94%` | `-8.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.76 | 🟠 **HOLD SHORT** | **-4.16%** | `MACRO_BEAR` | `98%` | `+130.3 bps` | Posição SHORT ativa há 43.8h (PnL: +4.20% · Stop ATR: $71.06 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 15:00:54 UTC` | Patrimônio: **$974.83 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,356.85 | ⚪ **CASH** | **-5.35%** | `MACRO_BEAR` | `78%` | `+43.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,690.95 | ⚪ **CASH** | **-5.64%** | `MACRO_BEAR` | `94%` | `-8.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.69 | 🟠 **HOLD SHORT** | **-4.16%** | `MACRO_BEAR` | `98%` | `+130.3 bps` | Posição SHORT ativa há 43.6h (PnL: +4.29% · Stop ATR: $71.04 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 14:45:44 UTC` | Patrimônio: **$974.82 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,380.91 | ⚪ **CASH** | **-5.43%** | `MACRO_BEAR` | `78%` | `+39.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,689.82 | ⚪ **CASH** | **-5.72%** | `MACRO_BEAR` | `94%` | `-1.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.70 | 🟠 **HOLD SHORT** | **-4.23%** | `MACRO_BEAR` | `98%` | `+100.1 bps` | Posição SHORT ativa há 43.3h (PnL: +4.28% · Stop ATR: $71.12 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 14:30:53 UTC` | Patrimônio: **$974.97 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,433.74 | ⚪ **CASH** | **-5.43%** | `MACRO_BEAR` | `78%` | `+39.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,694.14 | ⚪ **CASH** | **-5.71%** | `MACRO_BEAR` | `94%` | `-1.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.60 | 🟠 **HOLD SHORT** | **-4.23%** | `MACRO_BEAR` | `98%` | `+100.1 bps` | Posição SHORT ativa há 43.1h (PnL: +4.41% · Stop ATR: $71.12 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 14:15:43 UTC` | Patrimônio: **$975.16 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,295.62 | ⚪ **CASH** | **-5.43%** | `MACRO_BEAR` | `78%` | `+39.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,691.84 | ⚪ **CASH** | **-5.71%** | `MACRO_BEAR` | `94%` | `-1.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.48 | 🟠 **HOLD SHORT** | **-4.24%** | `MACRO_BEAR` | `98%` | `+100.1 bps` | Posição SHORT ativa há 42.8h (PnL: +4.58% · Stop ATR: $71.12 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 14:00:46 UTC` | Patrimônio: **$974.68 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,621.74 | ⚪ **CASH** | **-5.42%** | `MACRO_BEAR` | `78%` | `+39.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,703.92 | ⚪ **CASH** | **-5.69%** | `MACRO_BEAR` | `94%` | `-1.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.79 | 🟠 **HOLD SHORT** | **-4.23%** | `MACRO_BEAR` | `98%` | `+100.1 bps` | Posição SHORT ativa há 42.6h (PnL: +4.16% · Stop ATR: $71.06 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 13:45:44 UTC` | Patrimônio: **$975.09 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,529.27 | 🚪 **CLOSE** | **-5.51%** | `MACRO_BEAR` | `79%` | `+156.8 bps` | Chandelier ATR(5.5x) SHORT acionado (stop $59,794.50 · melhor +11.45% · realizou +3.65%) |
| **ETHUSDT** | $1,702.25 | 🚪 **CLOSE** | **-5.79%** | `MACRO_BEAR` | `95%` | `-47.8 bps` | Chandelier ATR(5.5x) SHORT acionado (stop $1,687.17 · melhor +12.86% · realizou +4.35%) |
| **SOLUSDT** | $70.52 | 🟠 **HOLD SHORT** | **-4.31%** | `MACRO_BEAR` | `99%` | `+84.1 bps` | Posição SHORT ativa há 42.3h (PnL: +4.52% · Stop ATR: $71.18 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 13:30:53 UTC` | Patrimônio: **$980.29 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,560.57 | 🟠 **HOLD SHORT** | **-5.55%** | `MACRO_BEAR` | `77%` | `+156.8 bps` | Posição SHORT ativa há 42.1h (PnL: +5.19% · Stop ATR: $59,708.60 · MACRO_BEAR) |
| **ETHUSDT** | $1,676.64 | 🟠 **HOLD SHORT** | **-5.84%** | `MACRO_BEAR` | `94%` | `-47.8 bps` | Posição SHORT ativa há 42.1h (PnL: +5.79% · Stop ATR: $1,684.53 · MACRO_BEAR) |
| **SOLUSDT** | $69.73 | 🟠 **HOLD SHORT** | **-4.34%** | `MACRO_BEAR` | `98%` | `+84.1 bps` | Posição SHORT ativa há 42.1h (PnL: +5.59% · Stop ATR: $71.10 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 13:15:47 UTC` | Patrimônio: **$981.26 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,302.40 | 🟠 **HOLD SHORT** | **-5.57%** | `MACRO_BEAR` | `76%` | `+156.8 bps` | Posição SHORT ativa há 41.8h (PnL: +5.60% · Stop ATR: $59,686.75 · MACRO_BEAR) |
| **ETHUSDT** | $1,672.69 | 🟠 **HOLD SHORT** | **-5.84%** | `MACRO_BEAR` | `93%` | `-47.8 bps` | Posição SHORT ativa há 41.8h (PnL: +6.01% · Stop ATR: $1,684.34 · MACRO_BEAR) |
| **SOLUSDT** | $69.62 | 🟠 **HOLD SHORT** | **-4.35%** | `MACRO_BEAR` | `98%` | `+84.1 bps` | Posição SHORT ativa há 41.8h (PnL: +5.74% · Stop ATR: $71.10 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 13:00:53 UTC` | Patrimônio: **$983.60 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $58,828.88 | 🟠 **HOLD SHORT** | **-5.59%** | `MACRO_BEAR` | `76%` | `+156.8 bps` | Posição SHORT ativa há 41.6h (PnL: +6.36% · Stop ATR: $59,636.76 · MACRO_BEAR) |
| **ETHUSDT** | $1,663.35 | 🟠 **HOLD SHORT** | **-5.86%** | `MACRO_BEAR` | `93%` | `-47.8 bps` | Posição SHORT ativa há 41.6h (PnL: +6.53% · Stop ATR: $1,683.13 · MACRO_BEAR) |
| **SOLUSDT** | $69.15 | 🟠 **HOLD SHORT** | **-4.37%** | `MACRO_BEAR` | `98%` | `+84.1 bps` | Posição SHORT ativa há 41.6h (PnL: +6.38% · Stop ATR: $71.05 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 12:45:49 UTC` | Patrimônio: **$982.89 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $58,915.67 | 🟠 **HOLD SHORT** | **-5.59%** | `MACRO_BEAR` | `76%` | `+143.7 bps` | Posição SHORT ativa há 41.3h (PnL: +6.22% · Stop ATR: $59,652.86 · MACRO_BEAR) |
| **ETHUSDT** | $1,667.09 | 🟠 **HOLD SHORT** | **-5.89%** | `MACRO_BEAR` | `93%` | `-13.9 bps` | Posição SHORT ativa há 41.3h (PnL: +6.32% · Stop ATR: $1,683.83 · MACRO_BEAR) |
| **SOLUSDT** | $69.33 | 🟠 **HOLD SHORT** | **-4.37%** | `MACRO_BEAR` | `98%` | `+213.7 bps` | Posição SHORT ativa há 41.3h (PnL: +6.13% · Stop ATR: $71.07 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 12:31:12 UTC` | Patrimônio: **$984.63 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $58,499.99 | 🟠 **HOLD SHORT** | **-5.61%** | `MACRO_BEAR` | `76%` | `+143.7 bps` | Posição SHORT ativa há 41.1h (PnL: +6.88% · Stop ATR: $59,608.61 · MACRO_BEAR) |
| **ETHUSDT** | $1,658.69 | 🟠 **HOLD SHORT** | **-5.90%** | `MACRO_BEAR` | `93%` | `-13.9 bps` | Posição SHORT ativa há 41.1h (PnL: +6.80% · Stop ATR: $1,682.58 · MACRO_BEAR) |
| **SOLUSDT** | $69.13 | 🟠 **HOLD SHORT** | **-4.38%** | `MACRO_BEAR` | `98%` | `+213.7 bps` | Posição SHORT ativa há 41.1h (PnL: +6.40% · Stop ATR: $71.03 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 12:15:51 UTC` | Patrimônio: **$985.04 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $58,376.00 | 🟠 **HOLD SHORT** | **-5.62%** | `MACRO_BEAR` | `76%` | `+143.7 bps` | Posição SHORT ativa há 40.8h (PnL: +7.08% · Stop ATR: $59,594.54 · MACRO_BEAR) |
| **ETHUSDT** | $1,656.84 | 🟠 **HOLD SHORT** | **-5.91%** | `MACRO_BEAR` | `93%` | `-13.9 bps` | Posição SHORT ativa há 40.8h (PnL: +6.90% · Stop ATR: $1,682.28 · MACRO_BEAR) |
| **SOLUSDT** | $69.11 | 🟠 **HOLD SHORT** | **-4.38%** | `MACRO_BEAR` | `98%` | `+213.7 bps` | Posição SHORT ativa há 40.8h (PnL: +6.43% · Stop ATR: $71.02 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 12:00:55 UTC` | Patrimônio: **$985.78 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $58,238.01 | 🟠 **HOLD SHORT** | **-5.63%** | `MACRO_BEAR` | `75%` | `+143.7 bps` | Posição SHORT ativa há 40.6h (PnL: +7.30% · Stop ATR: $59,577.30 · MACRO_BEAR) |
| **ETHUSDT** | $1,654.27 | 🟠 **HOLD SHORT** | **-5.91%** | `MACRO_BEAR` | `93%` | `-13.9 bps` | Posição SHORT ativa há 40.6h (PnL: +7.04% · Stop ATR: $1,681.80 · MACRO_BEAR) |
| **SOLUSDT** | $68.93 | 🟠 **HOLD SHORT** | **-4.39%** | `MACRO_BEAR` | `98%` | `+213.7 bps` | Posição SHORT ativa há 40.6h (PnL: +6.67% · Stop ATR: $70.99 · MACRO_BEAR) |
