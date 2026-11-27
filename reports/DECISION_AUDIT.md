# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-27 01:30:46 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-27 01:30:46 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,770.12 | ⚪ **CASH** | **-1.04%** | `MACRO_BEAR` | `78%` | `+21.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,702.22 | ⚪ **CASH** | **-1.21%** | `MACRO_BEAR` | `86%` | `+2.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.48 | ⚪ **CASH** | **-0.70%** | `MACRO_BEAR` | `89%` | `-7.2 bps` | Tendência neutra (-0.70% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 01:15:43 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,826.36 | ⚪ **CASH** | **-1.04%** | `MACRO_BEAR` | `78%` | `+21.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,702.70 | ⚪ **CASH** | **-1.21%** | `MACRO_BEAR` | `86%` | `+2.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.46 | ⚪ **CASH** | **-0.70%** | `MACRO_BEAR` | `89%` | `-7.2 bps` | Tendência neutra (-0.70% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 01:00:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,744.92 | ⚪ **CASH** | **-1.04%** | `MACRO_BEAR` | `78%` | `+21.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,703.70 | ⚪ **CASH** | **-1.21%** | `MACRO_BEAR` | `86%` | `+2.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.34 | ⚪ **CASH** | **-0.71%** | `MACRO_BEAR` | `89%` | `-7.2 bps` | Tendência neutra (-0.71% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 00:45:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,739.69 | ⚪ **CASH** | **-1.07%** | `MACRO_BEAR` | `78%` | `+13.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,699.57 | ⚪ **CASH** | **-1.25%** | `MACRO_BEAR` | `86%` | `-4.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.38 | ⚪ **CASH** | **-0.74%** | `MACRO_BEAR` | `90%` | `-0.0 bps` | Tendência neutra (-0.74% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 00:30:45 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,598.00 | ⚪ **CASH** | **-1.08%** | `MACRO_BEAR` | `78%` | `+13.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,692.02 | ⚪ **CASH** | **-1.26%** | `MACRO_BEAR` | `86%` | `-4.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.22 | ⚪ **CASH** | **-0.75%** | `MACRO_BEAR` | `90%` | `-0.0 bps` | Tendência neutra (-0.75% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 00:15:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,606.73 | ⚪ **CASH** | **-1.08%** | `MACRO_BEAR` | `78%` | `+13.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,691.01 | ⚪ **CASH** | **-1.27%** | `MACRO_BEAR` | `86%` | `-4.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.13 | ⚪ **CASH** | **-0.75%** | `MACRO_BEAR` | `90%` | `-0.0 bps` | Tendência neutra (-0.75% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 00:00:54 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,597.50 | ⚪ **CASH** | **-1.08%** | `MACRO_BEAR` | `78%` | `+13.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,690.54 | ⚪ **CASH** | **-1.27%** | `MACRO_BEAR` | `86%` | `-4.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.09 | ⚪ **CASH** | **-0.75%** | `MACRO_BEAR` | `90%` | `-0.0 bps` | Tendência neutra (-0.75% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 23:45:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,486.73 | ⚪ **CASH** | **-1.10%** | `MACRO_BEAR` | `78%` | `-4.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,687.01 | ⚪ **CASH** | **-1.29%** | `MACRO_BEAR` | `86%` | `-10.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.02 | ⚪ **CASH** | **-0.78%** | `MACRO_BEAR` | `90%` | `-0.4 bps` | Tendência neutra (-0.78% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 23:30:41 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,486.72 | ⚪ **CASH** | **-1.10%** | `MACRO_BEAR` | `78%` | `-4.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,687.79 | ⚪ **CASH** | **-1.28%** | `MACRO_BEAR` | `86%` | `-10.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.95 | ⚪ **CASH** | **-0.79%** | `MACRO_BEAR` | `90%` | `-0.4 bps` | Tendência neutra (-0.79% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 23:15:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,472.09 | ⚪ **CASH** | **-1.11%** | `MACRO_BEAR` | `78%` | `-4.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,687.96 | ⚪ **CASH** | **-1.28%** | `MACRO_BEAR` | `86%` | `-10.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.94 | ⚪ **CASH** | **-0.79%** | `MACRO_BEAR` | `90%` | `-0.4 bps` | Tendência neutra (-0.79% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 23:00:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,460.01 | ⚪ **CASH** | **-1.11%** | `MACRO_BEAR` | `78%` | `-4.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,689.94 | ⚪ **CASH** | **-1.28%** | `MACRO_BEAR` | `86%` | `-10.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.96 | ⚪ **CASH** | **-0.78%** | `MACRO_BEAR` | `90%` | `-0.4 bps` | Tendência neutra (-0.78% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 22:45:43 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,640.54 | ⚪ **CASH** | **-1.12%** | `MACRO_BEAR` | `78%` | `-10.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,697.78 | ⚪ **CASH** | **-1.29%** | `MACRO_BEAR` | `86%` | `+3.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.29 | ⚪ **CASH** | **-0.80%** | `MACRO_BEAR` | `90%` | `-70.3 bps` | Tendência neutra (-0.80% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 22:30:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,590.01 | ⚪ **CASH** | **-1.12%** | `MACRO_BEAR` | `78%` | `-10.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,697.11 | ⚪ **CASH** | **-1.29%** | `MACRO_BEAR` | `86%` | `+3.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.23 | ⚪ **CASH** | **-0.80%** | `MACRO_BEAR` | `90%` | `-70.3 bps` | Tendência neutra (-0.80% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 22:15:46 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,566.00 | ⚪ **CASH** | **-1.12%** | `MACRO_BEAR` | `78%` | `-10.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,696.95 | ⚪ **CASH** | **-1.29%** | `MACRO_BEAR` | `86%` | `+3.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.17 | ⚪ **CASH** | **-0.81%** | `MACRO_BEAR` | `90%` | `-70.3 bps` | Tendência neutra (-0.81% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 22:00:57 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,758.08 | ⚪ **CASH** | **-1.11%** | `MACRO_BEAR` | `78%` | `-10.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,703.26 | ⚪ **CASH** | **-1.28%** | `MACRO_BEAR` | `86%` | `+3.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.54 | ⚪ **CASH** | **-0.79%** | `MACRO_BEAR` | `90%` | `-70.3 bps` | Tendência neutra (-0.79% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 21:45:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,896.76 | ⚪ **CASH** | **-1.14%** | `MACRO_BEAR` | `78%` | `-12.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,707.98 | ⚪ **CASH** | **-1.31%** | `MACRO_BEAR` | `86%` | `-9.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.71 | ⚪ **CASH** | **-0.84%** | `MACRO_BEAR` | `90%` | `-81.7 bps` | Tendência neutra (-0.84% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 21:30:45 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,937.79 | ⚪ **CASH** | **-1.14%** | `MACRO_BEAR` | `78%` | `-12.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,706.66 | ⚪ **CASH** | **-1.31%** | `MACRO_BEAR` | `86%` | `-9.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.60 | ⚪ **CASH** | **-0.84%** | `MACRO_BEAR` | `90%` | `-81.7 bps` | Tendência neutra (-0.84% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 21:15:40 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,800.01 | ⚪ **CASH** | **-1.15%** | `MACRO_BEAR` | `78%` | `-12.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,704.43 | ⚪ **CASH** | **-1.32%** | `MACRO_BEAR` | `86%` | `-9.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.51 | ⚪ **CASH** | **-0.85%** | `MACRO_BEAR` | `90%` | `-81.7 bps` | Tendência neutra (-0.85% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 21:00:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,789.32 | ⚪ **CASH** | **-1.15%** | `MACRO_BEAR` | `78%` | `-12.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,705.22 | ⚪ **CASH** | **-1.32%** | `MACRO_BEAR` | `86%` | `-9.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.35 | ⚪ **CASH** | **-0.86%** | `MACRO_BEAR` | `90%` | `-81.7 bps` | Tendência neutra (-0.86% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 20:45:47 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,802.98 | ⚪ **CASH** | **-1.19%** | `MACRO_BEAR` | `78%` | `-7.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,705.81 | ⚪ **CASH** | **-1.36%** | `MACRO_BEAR` | `87%` | `-8.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.37 | ⚪ **CASH** | **-0.90%** | `MACRO_BEAR` | `91%` | `-83.0 bps` | Tendência neutra (-0.90% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 20:30:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,702.01 | ⚪ **CASH** | **-1.19%** | `MACRO_BEAR` | `78%` | `-7.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,703.21 | ⚪ **CASH** | **-1.36%** | `MACRO_BEAR` | `87%` | `-8.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.40 | ⚪ **CASH** | **-0.90%** | `MACRO_BEAR` | `91%` | `-83.0 bps` | Tendência neutra (-0.90% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 20:15:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,724.01 | ⚪ **CASH** | **-1.19%** | `MACRO_BEAR` | `78%` | `-7.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,703.38 | ⚪ **CASH** | **-1.36%** | `MACRO_BEAR` | `87%` | `-8.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.28 | ⚪ **CASH** | **-0.90%** | `MACRO_BEAR` | `91%` | `-83.0 bps` | Tendência neutra (-0.90% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 20:00:55 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,684.71 | ⚪ **CASH** | **-1.19%** | `MACRO_BEAR` | `78%` | `-7.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,703.23 | ⚪ **CASH** | **-1.36%** | `MACRO_BEAR` | `87%` | `-8.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.23 | ⚪ **CASH** | **-0.90%** | `MACRO_BEAR` | `91%` | `-83.0 bps` | Tendência neutra (-0.90% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 19:45:43 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,672.00 | ⚪ **CASH** | **-1.23%** | `MACRO_BEAR` | `78%` | `-18.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,706.22 | ⚪ **CASH** | **-1.40%** | `MACRO_BEAR` | `87%` | `-25.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.37 | ⚪ **CASH** | **-0.94%** | `MACRO_BEAR` | `91%` | `-33.9 bps` | Tendência neutra (-0.94% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 19:30:46 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,647.69 | ⚪ **CASH** | **-1.23%** | `MACRO_BEAR` | `78%` | `-18.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,704.51 | ⚪ **CASH** | **-1.40%** | `MACRO_BEAR` | `87%` | `-25.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.47 | ⚪ **CASH** | **-0.94%** | `MACRO_BEAR` | `91%` | `-33.9 bps` | Tendência neutra (-0.94% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 19:15:46 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,523.63 | ⚪ **CASH** | **-1.23%** | `MACRO_BEAR` | `78%` | `-18.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,700.82 | ⚪ **CASH** | **-1.41%** | `MACRO_BEAR` | `87%` | `-25.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.30 | ⚪ **CASH** | **-0.95%** | `MACRO_BEAR` | `91%` | `-33.9 bps` | Tendência neutra (-0.95% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 19:00:57 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,485.67 | ⚪ **CASH** | **-1.23%** | `MACRO_BEAR` | `78%` | `-18.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,699.92 | ⚪ **CASH** | **-1.41%** | `MACRO_BEAR` | `87%` | `-25.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.31 | ⚪ **CASH** | **-0.95%** | `MACRO_BEAR` | `91%` | `-33.9 bps` | Tendência neutra (-0.95% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 18:45:41 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,640.23 | ⚪ **CASH** | **-1.25%** | `MACRO_BEAR` | `79%` | `-29.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,701.17 | ⚪ **CASH** | **-1.44%** | `MACRO_BEAR` | `87%` | `-37.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.31 | ⚪ **CASH** | **-0.99%** | `MACRO_BEAR` | `91%` | `-30.7 bps` | Tendência neutra (-0.99% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 18:30:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,664.01 | ⚪ **CASH** | **-1.25%** | `MACRO_BEAR` | `79%` | `-29.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,698.44 | ⚪ **CASH** | **-1.45%** | `MACRO_BEAR` | `87%` | `-37.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.30 | ⚪ **CASH** | **-1.00%** | `MACRO_BEAR` | `91%` | `-30.7 bps` | Tendência neutra (-1.00% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 18:15:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,486.73 | ⚪ **CASH** | **-1.26%** | `MACRO_BEAR` | `79%` | `-29.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,691.85 | ⚪ **CASH** | **-1.46%** | `MACRO_BEAR` | `87%` | `-37.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.05 | ⚪ **CASH** | **-1.01%** | `MACRO_BEAR` | `91%` | `-30.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 18:01:00 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,564.01 | ⚪ **CASH** | **-1.26%** | `MACRO_BEAR` | `79%` | `-29.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,695.80 | ⚪ **CASH** | **-1.45%** | `MACRO_BEAR` | `87%` | `-37.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.17 | ⚪ **CASH** | **-1.00%** | `MACRO_BEAR` | `91%` | `-30.7 bps` | Tendência neutra (-1.00% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 17:45:39 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,432.65 | ⚪ **CASH** | **-1.29%** | `MACRO_BEAR` | `79%` | `-37.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,690.79 | ⚪ **CASH** | **-1.49%** | `MACRO_BEAR` | `87%` | `-1.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.88 | ⚪ **CASH** | **-1.05%** | `MACRO_BEAR` | `91%` | `-13.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 17:30:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,429.02 | ⚪ **CASH** | **-1.29%** | `MACRO_BEAR` | `79%` | `-37.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,690.67 | ⚪ **CASH** | **-1.49%** | `MACRO_BEAR` | `87%` | `-1.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.84 | ⚪ **CASH** | **-1.06%** | `MACRO_BEAR` | `91%` | `-13.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 17:15:37 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,553.10 | ⚪ **CASH** | **-1.28%** | `MACRO_BEAR` | `79%` | `-37.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,694.51 | ⚪ **CASH** | **-1.48%** | `MACRO_BEAR` | `87%` | `-1.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.08 | ⚪ **CASH** | **-1.05%** | `MACRO_BEAR` | `91%` | `-13.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 17:00:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,591.74 | ⚪ **CASH** | **-1.28%** | `MACRO_BEAR` | `79%` | `-37.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,694.55 | ⚪ **CASH** | **-1.48%** | `MACRO_BEAR` | `87%` | `-1.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.08 | ⚪ **CASH** | **-1.05%** | `MACRO_BEAR` | `91%` | `-13.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 16:45:39 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,540.97 | ⚪ **CASH** | **-1.31%** | `MACRO_BEAR` | `79%` | `-31.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,691.75 | ⚪ **CASH** | **-1.51%** | `MACRO_BEAR` | `87%` | `+4.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.04 | ⚪ **CASH** | **-1.09%** | `MACRO_BEAR` | `91%` | `+3.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
