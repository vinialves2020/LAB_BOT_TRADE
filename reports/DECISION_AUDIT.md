# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-22 12:15:49 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-22 12:15:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,528.70 | ⚪ **CASH** | **-4.16%** | `MACRO_BEAR` | `72%` | `-16.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,719.27 | ⚪ **CASH** | **-4.37%** | `MACRO_BEAR` | `82%` | `-0.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.88 | ⚪ **CASH** | **-3.29%** | `MACRO_BEAR` | `84%` | `+15.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 12:00:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,065.04 | ⚪ **CASH** | **-4.18%** | `MACRO_BEAR` | `72%` | `-16.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,708.80 | ⚪ **CASH** | **-4.38%** | `MACRO_BEAR` | `82%` | `-0.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.63 | ⚪ **CASH** | **-3.30%** | `MACRO_BEAR` | `84%` | `+15.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 11:45:47 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,028.93 | ⚪ **CASH** | **-4.28%** | `MACRO_BEAR` | `72%` | `-17.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,708.81 | ⚪ **CASH** | **-4.48%** | `MACRO_BEAR` | `82%` | `-2.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.75 | ⚪ **CASH** | **-3.35%** | `MACRO_BEAR` | `84%` | `+9.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 11:30:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,984.61 | ⚪ **CASH** | **-4.28%** | `MACRO_BEAR` | `72%` | `-17.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,708.76 | ⚪ **CASH** | **-4.48%** | `MACRO_BEAR` | `82%` | `-2.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.75 | ⚪ **CASH** | **-3.35%** | `MACRO_BEAR` | `84%` | `+9.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 11:15:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,972.45 | ⚪ **CASH** | **-4.28%** | `MACRO_BEAR` | `72%` | `-17.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,711.12 | ⚪ **CASH** | **-4.47%** | `MACRO_BEAR` | `82%` | `-2.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.82 | 🚪 **CLOSE** | **-3.35%** | `MACRO_BEAR` | `84%` | `+9.8 bps` | Chandelier ATR(5.5x) SHORT acionado (stop $70.74 · melhor +11.51% · realizou +4.12%) |

---

### 🕒 Ciclo `2026-11-22 11:00:56 UTC` | Patrimônio: **$974.83 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,878.72 | ⚪ **CASH** | **-4.28%** | `MACRO_BEAR` | `72%` | `-17.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,710.44 | ⚪ **CASH** | **-4.47%** | `MACRO_BEAR` | `82%` | `-2.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.69 | 🟠 **HOLD SHORT** | **-3.35%** | `MACRO_BEAR` | `84%` | `+9.8 bps` | Posição SHORT ativa há 63.6h (PnL: +4.29% · Stop ATR: $70.73 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 10:45:40 UTC` | Patrimônio: **$975.09 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,774.10 | ⚪ **CASH** | **-4.38%** | `MACRO_BEAR` | `72%` | `-26.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,709.89 | ⚪ **CASH** | **-4.57%** | `MACRO_BEAR` | `82%` | `-45.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.52 | 🟠 **HOLD SHORT** | **-3.42%** | `MACRO_BEAR` | `84%` | `+12.5 bps` | Posição SHORT ativa há 63.3h (PnL: +4.52% · Stop ATR: $70.77 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 10:30:54 UTC` | Patrimônio: **$975.02 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,874.55 | ⚪ **CASH** | **-4.38%** | `MACRO_BEAR` | `72%` | `-26.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,710.02 | ⚪ **CASH** | **-4.57%** | `MACRO_BEAR` | `82%` | `-45.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.57 | 🟠 **HOLD SHORT** | **-3.42%** | `MACRO_BEAR` | `84%` | `+12.5 bps` | Posição SHORT ativa há 63.1h (PnL: +4.45% · Stop ATR: $70.77 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 10:15:46 UTC` | Patrimônio: **$974.94 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,958.53 | ⚪ **CASH** | **-4.37%** | `MACRO_BEAR` | `72%` | `-26.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,713.22 | ⚪ **CASH** | **-4.57%** | `MACRO_BEAR` | `82%` | `-45.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.62 | 🟠 **HOLD SHORT** | **-3.42%** | `MACRO_BEAR` | `84%` | `+12.5 bps` | Posição SHORT ativa há 62.8h (PnL: +4.39% · Stop ATR: $70.77 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 10:00:48 UTC` | Patrimônio: **$975.09 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,932.98 | ⚪ **CASH** | **-4.37%** | `MACRO_BEAR` | `72%` | `-26.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,712.39 | ⚪ **CASH** | **-4.57%** | `MACRO_BEAR` | `82%` | `-45.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.52 | 🟠 **HOLD SHORT** | **-3.42%** | `MACRO_BEAR` | `84%` | `+12.5 bps` | Posição SHORT ativa há 62.6h (PnL: +4.52% · Stop ATR: $70.77 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 09:45:46 UTC` | Patrimônio: **$975.92 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,226.70 | ⚪ **CASH** | **-4.51%** | `MACRO_BEAR` | `70%` | `-23.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,694.90 | ⚪ **CASH** | **-4.71%** | `MACRO_BEAR` | `81%` | `-21.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.98 | 🟠 **HOLD SHORT** | **-3.51%** | `MACRO_BEAR` | `84%` | `+15.5 bps` | Posição SHORT ativa há 62.3h (PnL: +5.25% · Stop ATR: $70.71 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 09:30:47 UTC` | Patrimônio: **$976.12 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,952.53 | ⚪ **CASH** | **-4.53%** | `MACRO_BEAR` | `70%` | `-23.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,687.86 | ⚪ **CASH** | **-4.72%** | `MACRO_BEAR` | `81%` | `-21.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.85 | 🟠 **HOLD SHORT** | **-3.51%** | `MACRO_BEAR` | `84%` | `+15.5 bps` | Posição SHORT ativa há 62.1h (PnL: +5.43% · Stop ATR: $70.71 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 09:15:51 UTC` | Patrimônio: **$976.40 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,715.56 | ⚪ **CASH** | **-4.54%** | `MACRO_BEAR` | `70%` | `-23.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,683.75 | ⚪ **CASH** | **-4.73%** | `MACRO_BEAR` | `81%` | `-21.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.67 | 🟠 **HOLD SHORT** | **-3.52%** | `MACRO_BEAR` | `84%` | `+15.5 bps` | Posição SHORT ativa há 61.8h (PnL: +5.67% · Stop ATR: $70.70 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 09:00:57 UTC` | Patrimônio: **$976.00 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,818.56 | ⚪ **CASH** | **-4.53%** | `MACRO_BEAR` | `70%` | `-23.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,688.77 | ⚪ **CASH** | **-4.72%** | `MACRO_BEAR` | `81%` | `-21.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.93 | 🟠 **HOLD SHORT** | **-3.51%** | `MACRO_BEAR` | `84%` | `+15.5 bps` | Posição SHORT ativa há 61.6h (PnL: +5.32% · Stop ATR: $70.68 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 08:45:49 UTC` | Patrimônio: **$976.29 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,654.78 | ⚪ **CASH** | **-4.59%** | `MACRO_BEAR` | `70%` | `-17.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,682.89 | ⚪ **CASH** | **-4.80%** | `MACRO_BEAR` | `81%` | `-22.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.74 | 🟠 **HOLD SHORT** | **-3.55%** | `MACRO_BEAR` | `84%` | `-0.4 bps` | Posição SHORT ativa há 61.3h (PnL: +5.58% · Stop ATR: $70.71 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 08:30:54 UTC` | Patrimônio: **$976.25 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,704.59 | ⚪ **CASH** | **-4.58%** | `MACRO_BEAR` | `70%` | `-17.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,682.13 | ⚪ **CASH** | **-4.80%** | `MACRO_BEAR` | `81%` | `-22.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.77 | 🟠 **HOLD SHORT** | **-3.55%** | `MACRO_BEAR` | `84%` | `-0.4 bps` | Posição SHORT ativa há 61.1h (PnL: +5.54% · Stop ATR: $70.70 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 08:15:49 UTC` | Patrimônio: **$976.66 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,262.71 | ⚪ **CASH** | **-4.60%** | `MACRO_BEAR` | `70%` | `-17.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,673.49 | ⚪ **CASH** | **-4.81%** | `MACRO_BEAR` | `81%` | `-22.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.50 | 🟠 **HOLD SHORT** | **-3.56%** | `MACRO_BEAR` | `84%` | `-0.4 bps` | Posição SHORT ativa há 60.8h (PnL: +5.90% · Stop ATR: $70.67 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 08:00:54 UTC` | Patrimônio: **$977.17 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,136.00 | ⚪ **CASH** | **-4.61%** | `MACRO_BEAR` | `70%` | `-17.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,666.37 | ⚪ **CASH** | **-4.82%** | `MACRO_BEAR` | `81%` | `-22.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.17 | 🟠 **HOLD SHORT** | **-3.58%** | `MACRO_BEAR` | `84%` | `-0.4 bps` | Posição SHORT ativa há 60.6h (PnL: +6.35% · Stop ATR: $70.63 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 07:45:45 UTC` | Patrimônio: **$977.12 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,055.58 | ⚪ **CASH** | **-4.63%** | `MACRO_BEAR` | `71%` | `-16.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,664.63 | ⚪ **CASH** | **-4.86%** | `MACRO_BEAR` | `82%` | `-17.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.20 | 🟠 **HOLD SHORT** | **-3.58%** | `MACRO_BEAR` | `84%` | `+1.6 bps` | Posição SHORT ativa há 60.3h (PnL: +6.31% · Stop ATR: $70.67 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 07:30:50 UTC` | Patrimônio: **$977.08 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,082.60 | ⚪ **CASH** | **-4.63%** | `MACRO_BEAR` | `71%` | `-16.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,663.32 | ⚪ **CASH** | **-4.86%** | `MACRO_BEAR` | `81%` | `-17.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.23 | 🟠 **HOLD SHORT** | **-3.58%** | `MACRO_BEAR` | `84%` | `+1.6 bps` | Posição SHORT ativa há 60.1h (PnL: +6.27% · Stop ATR: $70.67 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 07:15:46 UTC` | Patrimônio: **$977.26 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,148.49 | ⚪ **CASH** | **-4.63%** | `MACRO_BEAR` | `71%` | `-16.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,663.54 | ⚪ **CASH** | **-4.86%** | `MACRO_BEAR` | `81%` | `-17.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.11 | 🟠 **HOLD SHORT** | **-3.59%** | `MACRO_BEAR` | `84%` | `+1.6 bps` | Posição SHORT ativa há 59.8h (PnL: +6.43% · Stop ATR: $70.66 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 07:00:55 UTC` | Patrimônio: **$977.25 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,092.46 | ⚪ **CASH** | **-4.63%** | `MACRO_BEAR` | `71%` | `-16.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,660.66 | ⚪ **CASH** | **-4.87%** | `MACRO_BEAR` | `82%` | `-17.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.12 | 🟠 **HOLD SHORT** | **-3.59%** | `MACRO_BEAR` | `84%` | `+1.6 bps` | Posição SHORT ativa há 59.6h (PnL: +6.42% · Stop ATR: $70.65 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-22 06:45:51 UTC` | Patrimônio: **$977.25 USDT** (Caixa: `$856.37`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,152.61 | ⚪ **CASH** | **-4.64%** | `MACRO_BEAR` | `71%` | `-2.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,663.01 | ⚪ **CASH** | **-4.89%** | `MACRO_BEAR` | `82%` | `-47.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.12 | 🟠 **HOLD SHORT** | **-3.59%** | `MACRO_BEAR` | `85%` | `-7.4 bps` | Posição SHORT ativa há 59.3h (PnL: +6.42% · Stop ATR: $70.69 · MACRO_BEAR) |

---

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
