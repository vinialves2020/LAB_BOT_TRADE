# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-21 15:00:54 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-11-21 11:45:48 UTC` | Patrimônio: **$986.15 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $58,163.29 | 🟠 **HOLD SHORT** | **-5.61%** | `MACRO_BEAR` | `75%` | `+154.6 bps` | Posição SHORT ativa há 40.3h (PnL: +7.42% · Stop ATR: $59,606.11 · MACRO_BEAR) |
| **ETHUSDT** | $1,653.87 | 🟠 **HOLD SHORT** | **-5.93%** | `MACRO_BEAR` | `93%` | `+0.3 bps` | Posição SHORT ativa há 40.3h (PnL: +7.07% · Stop ATR: $1,682.94 · MACRO_BEAR) |
| **SOLUSDT** | $68.81 | 🟠 **HOLD SHORT** | **-4.39%** | `MACRO_BEAR` | `98%` | `+185.3 bps` | Posição SHORT ativa há 40.3h (PnL: +6.84% · Stop ATR: $71.04 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 11:30:53 UTC` | Patrimônio: **$988.04 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $57,983.19 | 🟠 **HOLD SHORT** | **-5.61%** | `MACRO_BEAR` | `75%` | `+154.6 bps` | Posição SHORT ativa há 40.1h (PnL: +7.70% · Stop ATR: $59,559.47 · MACRO_BEAR) |
| **ETHUSDT** | $1,641.52 | 🟠 **HOLD SHORT** | **-5.95%** | `MACRO_BEAR` | `93%` | `+0.3 bps` | Posição SHORT ativa há 40.1h (PnL: +7.76% · Stop ATR: $1,680.82 · MACRO_BEAR) |
| **SOLUSDT** | $68.38 | 🟠 **HOLD SHORT** | **-4.41%** | `MACRO_BEAR` | `97%` | `+185.3 bps` | Posição SHORT ativa há 40.1h (PnL: +7.42% · Stop ATR: $70.97 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 11:15:55 UTC` | Patrimônio: **$988.55 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $57,892.79 | 🟠 **HOLD SHORT** | **-5.62%** | `MACRO_BEAR` | `75%` | `+154.6 bps` | Posição SHORT ativa há 39.8h (PnL: +7.85% · Stop ATR: $59,557.80 · MACRO_BEAR) |
| **ETHUSDT** | $1,641.40 | 🟠 **HOLD SHORT** | **-5.95%** | `MACRO_BEAR` | `93%` | `+0.3 bps` | Posição SHORT ativa há 39.8h (PnL: +7.77% · Stop ATR: $1,680.80 · MACRO_BEAR) |
| **SOLUSDT** | $68.17 | 🟠 **HOLD SHORT** | **-4.42%** | `MACRO_BEAR` | `97%` | `+185.3 bps` | Posição SHORT ativa há 39.8h (PnL: +7.70% · Stop ATR: $70.95 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 11:00:50 UTC` | Patrimônio: **$988.83 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $57,886.02 | 🟠 **HOLD SHORT** | **-5.62%** | `MACRO_BEAR` | `75%` | `+154.6 bps` | Posição SHORT ativa há 39.6h (PnL: +7.86% · Stop ATR: $59,551.97 · MACRO_BEAR) |
| **ETHUSDT** | $1,639.64 | 🟠 **HOLD SHORT** | **-5.95%** | `MACRO_BEAR` | `93%` | `+0.3 bps` | Posição SHORT ativa há 39.6h (PnL: +7.87% · Stop ATR: $1,680.56 · MACRO_BEAR) |
| **SOLUSDT** | $68.08 | 🟠 **HOLD SHORT** | **-4.42%** | `MACRO_BEAR` | `97%` | `+185.3 bps` | Posição SHORT ativa há 39.6h (PnL: +7.83% · Stop ATR: $70.93 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 10:45:50 UTC` | Patrimônio: **$988.80 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $57,854.01 | 🟠 **HOLD SHORT** | **-5.58%** | `MACRO_BEAR` | `75%` | `+171.2 bps` | Posição SHORT ativa há 39.3h (PnL: +7.91% · Stop ATR: $59,566.13 · MACRO_BEAR) |
| **ETHUSDT** | $1,639.75 | 🟠 **HOLD SHORT** | **-5.95%** | `MACRO_BEAR` | `93%` | `+14.8 bps` | Posição SHORT ativa há 39.3h (PnL: +7.86% · Stop ATR: $1,681.29 · MACRO_BEAR) |
| **SOLUSDT** | $68.14 | 🟠 **HOLD SHORT** | **-4.39%** | `MACRO_BEAR` | `97%` | `+186.3 bps` | Posição SHORT ativa há 39.3h (PnL: +7.74% · Stop ATR: $70.96 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 10:30:49 UTC` | Patrimônio: **$987.93 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $58,074.74 | 🟠 **HOLD SHORT** | **-5.57%** | `MACRO_BEAR` | `75%` | `+171.2 bps` | Posição SHORT ativa há 39.1h (PnL: +7.56% · Stop ATR: $59,561.11 · MACRO_BEAR) |
| **ETHUSDT** | $1,643.51 | 🟠 **HOLD SHORT** | **-5.94%** | `MACRO_BEAR` | `93%` | `+14.8 bps` | Posição SHORT ativa há 39.1h (PnL: +7.65% · Stop ATR: $1,681.29 · MACRO_BEAR) |
| **SOLUSDT** | $68.24 | 🟠 **HOLD SHORT** | **-4.38%** | `MACRO_BEAR` | `97%` | `+186.3 bps` | Posição SHORT ativa há 39.1h (PnL: +7.61% · Stop ATR: $70.96 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 10:15:50 UTC` | Patrimônio: **$989.00 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $57,941.39 | 🟠 **HOLD SHORT** | **-5.58%** | `MACRO_BEAR` | `75%` | `+171.2 bps` | Posição SHORT ativa há 38.8h (PnL: +7.77% · Stop ATR: $59,550.20 · MACRO_BEAR) |
| **ETHUSDT** | $1,636.11 | 🟠 **HOLD SHORT** | **-5.95%** | `MACRO_BEAR` | `93%` | `+14.8 bps` | Posição SHORT ativa há 38.8h (PnL: +8.06% · Stop ATR: $1,680.63 · MACRO_BEAR) |
| **SOLUSDT** | $68.06 | 🟠 **HOLD SHORT** | **-4.39%** | `MACRO_BEAR` | `97%` | `+186.3 bps` | Posição SHORT ativa há 38.8h (PnL: +7.85% · Stop ATR: $70.94 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 10:00:50 UTC` | Patrimônio: **$988.60 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $58,010.96 | 🟠 **HOLD SHORT** | **-5.57%** | `MACRO_BEAR` | `75%` | `+171.2 bps` | Posição SHORT ativa há 38.6h (PnL: +7.66% · Stop ATR: $59,542.47 · MACRO_BEAR) |
| **ETHUSDT** | $1,638.67 | 🟠 **HOLD SHORT** | **-5.95%** | `MACRO_BEAR` | `93%` | `+14.8 bps` | Posição SHORT ativa há 38.6h (PnL: +7.92% · Stop ATR: $1,680.45 · MACRO_BEAR) |
| **SOLUSDT** | $68.11 | 🟠 **HOLD SHORT** | **-4.39%** | `MACRO_BEAR` | `97%` | `+186.3 bps` | Posição SHORT ativa há 38.6h (PnL: +7.78% · Stop ATR: $70.93 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 09:45:43 UTC` | Patrimônio: **$988.26 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $58,026.08 | 🟠 **HOLD SHORT** | **-5.53%** | `MACRO_BEAR` | `75%` | `+186.8 bps` | Posição SHORT ativa há 38.3h (PnL: +7.64% · Stop ATR: $59,574.05 · MACRO_BEAR) |
| **ETHUSDT** | $1,641.31 | 🟠 **HOLD SHORT** | **-5.93%** | `MACRO_BEAR` | `93%` | `+58.2 bps` | Posição SHORT ativa há 38.3h (PnL: +7.77% · Stop ATR: $1,681.48 · MACRO_BEAR) |
| **SOLUSDT** | $68.19 | 🟠 **HOLD SHORT** | **-4.35%** | `MACRO_BEAR` | `97%` | `+186.8 bps` | Posição SHORT ativa há 38.3h (PnL: +7.68% · Stop ATR: $70.98 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 09:30:48 UTC` | Patrimônio: **$988.74 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $57,996.55 | 🟠 **HOLD SHORT** | **-5.53%** | `MACRO_BEAR` | `75%` | `+186.8 bps` | Posição SHORT ativa há 38.1h (PnL: +7.68% · Stop ATR: $59,574.05 · MACRO_BEAR) |
| **ETHUSDT** | $1,638.76 | 🟠 **HOLD SHORT** | **-5.94%** | `MACRO_BEAR` | `93%` | `+58.2 bps` | Posição SHORT ativa há 38.1h (PnL: +7.92% · Stop ATR: $1,681.38 · MACRO_BEAR) |
| **SOLUSDT** | $68.03 | 🟠 **HOLD SHORT** | **-4.35%** | `MACRO_BEAR` | `97%` | `+186.8 bps` | Posição SHORT ativa há 38.1h (PnL: +7.89% · Stop ATR: $70.97 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 09:15:47 UTC` | Patrimônio: **$989.44 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $57,918.00 | 🟠 **HOLD SHORT** | **-5.54%** | `MACRO_BEAR` | `75%` | `+186.8 bps` | Posição SHORT ativa há 37.8h (PnL: +7.81% · Stop ATR: $59,568.82 · MACRO_BEAR) |
| **ETHUSDT** | $1,636.40 | 🟠 **HOLD SHORT** | **-5.94%** | `MACRO_BEAR` | `93%` | `+58.2 bps` | Posição SHORT ativa há 37.8h (PnL: +8.05% · Stop ATR: $1,681.23 · MACRO_BEAR) |
| **SOLUSDT** | $67.79 | 🟠 **HOLD SHORT** | **-4.36%** | `MACRO_BEAR` | `97%` | `+186.8 bps` | Posição SHORT ativa há 37.8h (PnL: +8.22% · Stop ATR: $70.95 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 09:00:50 UTC` | Patrimônio: **$991.20 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $57,783.61 | 🟠 **HOLD SHORT** | **-5.54%** | `MACRO_BEAR` | `75%` | `+186.8 bps` | Posição SHORT ativa há 37.6h (PnL: +8.02% · Stop ATR: $59,552.62 · MACRO_BEAR) |
| **ETHUSDT** | $1,627.07 | 🟠 **HOLD SHORT** | **-5.96%** | `MACRO_BEAR` | `93%` | `+58.2 bps` | Posição SHORT ativa há 37.6h (PnL: +8.57% · Stop ATR: $1,680.44 · MACRO_BEAR) |
| **SOLUSDT** | $67.25 | 🟠 **HOLD SHORT** | **-4.39%** | `MACRO_BEAR` | `97%` | `+186.8 bps` | Posição SHORT ativa há 37.6h (PnL: +8.95% · Stop ATR: $70.91 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 08:45:50 UTC` | Patrimônio: **$990.90 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $57,867.88 | 🟠 **HOLD SHORT** | **-5.49%** | `MACRO_BEAR` | `75%` | `+181.5 bps` | Posição SHORT ativa há 37.3h (PnL: +7.89% · Stop ATR: $59,554.92 · MACRO_BEAR) |
| **ETHUSDT** | $1,627.91 | 🟠 **HOLD SHORT** | **-5.93%** | `MACRO_BEAR` | `93%` | `+30.5 bps` | Posição SHORT ativa há 37.3h (PnL: +8.52% · Stop ATR: $1,680.30 · MACRO_BEAR) |
| **SOLUSDT** | $67.29 | 🟠 **HOLD SHORT** | **-4.31%** | `MACRO_BEAR` | `97%` | `+179.6 bps` | Posição SHORT ativa há 37.3h (PnL: +8.90% · Stop ATR: $70.93 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 08:30:49 UTC` | Patrimônio: **$991.92 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $57,691.73 | 🟠 **HOLD SHORT** | **-5.49%** | `MACRO_BEAR` | `76%` | `+181.5 bps` | Posição SHORT ativa há 37.1h (PnL: +8.17% · Stop ATR: $59,540.94 · MACRO_BEAR) |
| **ETHUSDT** | $1,624.63 | 🟠 **HOLD SHORT** | **-5.93%** | `MACRO_BEAR` | `93%` | `+30.5 bps` | Posição SHORT ativa há 37.1h (PnL: +8.71% · Stop ATR: $1,680.15 · MACRO_BEAR) |
| **SOLUSDT** | $67.01 | 🟠 **HOLD SHORT** | **-4.32%** | `MACRO_BEAR` | `97%` | `+179.6 bps` | Posição SHORT ativa há 37.1h (PnL: +9.27% · Stop ATR: $70.91 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 08:15:53 UTC` | Patrimônio: **$991.44 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $57,747.34 | 🟠 **HOLD SHORT** | **-5.49%** | `MACRO_BEAR` | `76%` | `+181.5 bps` | Posição SHORT ativa há 36.8h (PnL: +8.08% · Stop ATR: $59,530.59 · MACRO_BEAR) |
| **ETHUSDT** | $1,625.28 | 🟠 **HOLD SHORT** | **-5.93%** | `MACRO_BEAR` | `93%` | `+30.5 bps` | Posição SHORT ativa há 36.8h (PnL: +8.67% · Stop ATR: $1,679.94 · MACRO_BEAR) |
| **SOLUSDT** | $67.22 | 🟠 **HOLD SHORT** | **-4.31%** | `MACRO_BEAR` | `97%` | `+179.6 bps` | Posição SHORT ativa há 36.8h (PnL: +8.99% · Stop ATR: $70.90 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 08:00:58 UTC` | Patrimônio: **$990.64 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $57,910.68 | 🟠 **HOLD SHORT** | **-5.48%** | `MACRO_BEAR` | `75%` | `+181.5 bps` | Posição SHORT ativa há 36.6h (PnL: +7.82% · Stop ATR: $59,518.69 · MACRO_BEAR) |
| **ETHUSDT** | $1,629.36 | 🟠 **HOLD SHORT** | **-5.92%** | `MACRO_BEAR` | `93%` | `+30.5 bps` | Posição SHORT ativa há 36.6h (PnL: +8.44% · Stop ATR: $1,679.62 · MACRO_BEAR) |
| **SOLUSDT** | $67.34 | 🟠 **HOLD SHORT** | **-4.31%** | `MACRO_BEAR` | `97%` | `+179.6 bps` | Posição SHORT ativa há 36.6h (PnL: +8.83% · Stop ATR: $70.88 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 07:45:34 UTC` | Patrimônio: **$989.39 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $58,062.80 | 🟠 **HOLD SHORT** | **-5.43%** | `MACRO_BEAR` | `75%` | `+193.5 bps` | Posição SHORT ativa há 36.3h (PnL: +7.58% · Stop ATR: $59,532.45 · MACRO_BEAR) |
| **ETHUSDT** | $1,632.89 | 🟠 **HOLD SHORT** | **-5.89%** | `MACRO_BEAR` | `93%` | `+22.0 bps` | Posição SHORT ativa há 36.3h (PnL: +8.25% · Stop ATR: $1,679.83 · MACRO_BEAR) |
| **SOLUSDT** | $67.79 | 🟠 **HOLD SHORT** | **-4.22%** | `MACRO_BEAR` | `97%` | `+186.3 bps` | Posição SHORT ativa há 36.3h (PnL: +8.22% · Stop ATR: $70.88 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 07:30:51 UTC` | Patrimônio: **$988.67 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $58,211.16 | 🟠 **HOLD SHORT** | **-5.42%** | `MACRO_BEAR` | `76%` | `+193.5 bps` | Posição SHORT ativa há 36.1h (PnL: +7.34% · Stop ATR: $59,532.45 · MACRO_BEAR) |
| **ETHUSDT** | $1,635.56 | 🟠 **HOLD SHORT** | **-5.88%** | `MACRO_BEAR` | `93%` | `+22.0 bps` | Posição SHORT ativa há 36.1h (PnL: +8.09% · Stop ATR: $1,679.83 · MACRO_BEAR) |
| **SOLUSDT** | $67.94 | 🟠 **HOLD SHORT** | **-4.21%** | `MACRO_BEAR` | `97%` | `+186.3 bps` | Posição SHORT ativa há 36.1h (PnL: +8.02% · Stop ATR: $70.88 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 07:15:41 UTC` | Patrimônio: **$988.87 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $58,200.01 | 🟠 **HOLD SHORT** | **-5.42%** | `MACRO_BEAR` | `76%` | `+193.5 bps` | Posição SHORT ativa há 35.8h (PnL: +7.36% · Stop ATR: $59,532.45 · MACRO_BEAR) |
| **ETHUSDT** | $1,635.17 | 🟠 **HOLD SHORT** | **-5.88%** | `MACRO_BEAR` | `93%` | `+22.0 bps` | Posição SHORT ativa há 35.8h (PnL: +8.12% · Stop ATR: $1,679.83 · MACRO_BEAR) |
| **SOLUSDT** | $67.84 | 🟠 **HOLD SHORT** | **-4.21%** | `MACRO_BEAR` | `97%` | `+186.3 bps` | Posição SHORT ativa há 35.8h (PnL: +8.15% · Stop ATR: $70.88 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 07:00:42 UTC` | Patrimônio: **$988.90 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $57,941.19 | 🟠 **HOLD SHORT** | **-5.43%** | `MACRO_BEAR` | `75%` | `+193.5 bps` | Posição SHORT ativa há 35.6h (PnL: +7.77% · Stop ATR: $59,471.64 · MACRO_BEAR) |
| **ETHUSDT** | $1,636.59 | 🟠 **HOLD SHORT** | **-5.88%** | `MACRO_BEAR` | `93%` | `+22.0 bps` | Posição SHORT ativa há 35.6h (PnL: +8.04% · Stop ATR: $1,678.81 · MACRO_BEAR) |
| **SOLUSDT** | $68.10 | 🟠 **HOLD SHORT** | **-4.20%** | `MACRO_BEAR` | `97%` | `+186.3 bps` | Posição SHORT ativa há 35.6h (PnL: +7.80% · Stop ATR: $70.84 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 06:45:43 UTC` | Patrimônio: **$993.12 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $57,108.45 | 🟠 **HOLD SHORT** | **-5.42%** | `MACRO_BEAR` | `71%` | `+209.2 bps` | Posição SHORT ativa há 35.3h (PnL: +9.10% · Stop ATR: $59,435.19 · MACRO_BEAR) |
| **ETHUSDT** | $1,614.69 | 🟠 **HOLD SHORT** | **-5.90%** | `MACRO_BEAR` | `89%` | `+158.0 bps` | Posição SHORT ativa há 35.3h (PnL: +9.27% · Stop ATR: $1,677.00 · MACRO_BEAR) |
| **SOLUSDT** | $67.46 | 🟠 **HOLD SHORT** | **-4.18%** | `MACRO_BEAR` | `94%` | `+182.2 bps` | Posição SHORT ativa há 35.3h (PnL: +8.67% · Stop ATR: $70.81 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 06:30:52 UTC` | Patrimônio: **$1,000.58 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $56,119.16 | 🟠 **HOLD SHORT** | **-5.46%** | `MACRO_BEAR` | `69%` | `+209.2 bps` | Posição SHORT ativa há 35.1h (PnL: +10.67% · Stop ATR: $59,352.36 · MACRO_BEAR) |
| **ETHUSDT** | $1,570.52 | 🟠 **HOLD SHORT** | **-5.97%** | `MACRO_BEAR` | `86%` | `+158.0 bps` | Posição SHORT ativa há 35.1h (PnL: +11.75% · Stop ATR: $1,673.25 · MACRO_BEAR) |
| **SOLUSDT** | $65.93 | 🟠 **HOLD SHORT** | **-4.24%** | `MACRO_BEAR` | `92%` | `+182.2 bps` | Posição SHORT ativa há 35.1h (PnL: +10.74% · Stop ATR: $70.70 · MACRO_BEAR) |

---

### 🕒 Ciclo `2026-11-21 06:15:52 UTC` | Patrimônio: **$1,003.41 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $55,628.65 | 🟠 **HOLD SHORT** | **-5.49%** | `MACRO_BEAR` | `69%` | `+209.2 bps` | Posição SHORT ativa há 34.8h (PnL: +11.45% · Stop ATR: $59,291.97 · MACRO_BEAR) |
| **ETHUSDT** | $1,556.95 | 🟠 **HOLD SHORT** | **-5.99%** | `MACRO_BEAR` | `86%` | `+158.0 bps` | Posição SHORT ativa há 34.8h (PnL: +12.51% · Stop ATR: $1,671.61 · MACRO_BEAR) |
| **SOLUSDT** | $65.36 | 🟠 **HOLD SHORT** | **-4.27%** | `MACRO_BEAR` | `92%` | `+182.2 bps` | Posição SHORT ativa há 34.8h (PnL: +11.51% · Stop ATR: $70.63 · MACRO_BEAR) |
