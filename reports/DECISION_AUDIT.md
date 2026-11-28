# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-28 02:45:42 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-28 02:45:42 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,981.79 | ⚪ **CASH** | **-0.76%** | `MACRO_BEAR` | `76%` | `+25.4 bps` | Tendência neutra (-0.76% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,664.03 | ⚪ **CASH** | **-1.07%** | `MACRO_BEAR` | `82%` | `+31.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.68 | ⚪ **CASH** | **+0.36%** | `MACRO_BEAR` | `85%` | `+23.8 bps` | Tendência neutra (+0.36% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 02:30:55 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,082.82 | ⚪ **CASH** | **-0.76%** | `MACRO_BEAR` | `76%` | `+25.4 bps` | Tendência neutra (-0.76% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,667.33 | ⚪ **CASH** | **-1.06%** | `MACRO_BEAR` | `82%` | `+31.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.89 | ⚪ **CASH** | **+0.36%** | `MACRO_BEAR` | `85%` | `+23.8 bps` | Tendência neutra (+0.36% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 02:15:50 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,199.29 | ⚪ **CASH** | **-0.75%** | `MACRO_BEAR` | `76%` | `+25.4 bps` | Tendência neutra (-0.75% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,670.10 | ⚪ **CASH** | **-1.06%** | `MACRO_BEAR` | `82%` | `+31.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.19 | ⚪ **CASH** | **+0.38%** | `MACRO_BEAR` | `85%` | `+23.8 bps` | Tendência neutra (+0.38% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 02:00:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,199.16 | ⚪ **CASH** | **-0.75%** | `MACRO_BEAR` | `76%` | `+25.4 bps` | Tendência neutra (-0.75% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,670.19 | ⚪ **CASH** | **-1.05%** | `MACRO_BEAR` | `82%` | `+31.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.20 | ⚪ **CASH** | **+0.38%** | `MACRO_BEAR` | `85%` | `+23.8 bps` | Tendência neutra (+0.38% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 01:45:37 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,181.20 | ⚪ **CASH** | **-0.75%** | `MACRO_BEAR` | `76%` | `+35.0 bps` | Tendência neutra (-0.75% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,669.05 | ⚪ **CASH** | **-1.03%** | `MACRO_BEAR` | `82%` | `+26.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.06 | ⚪ **CASH** | **+0.36%** | `MACRO_BEAR` | `85%` | `+20.4 bps` | Tendência neutra (+0.36% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 01:30:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,140.88 | ⚪ **CASH** | **-0.75%** | `MACRO_BEAR` | `76%` | `+35.0 bps` | Tendência neutra (-0.75% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,668.80 | ⚪ **CASH** | **-1.03%** | `MACRO_BEAR` | `82%` | `+26.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.02 | ⚪ **CASH** | **+0.36%** | `MACRO_BEAR` | `85%` | `+20.4 bps` | Tendência neutra (+0.36% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 01:15:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,112.01 | ⚪ **CASH** | **-0.75%** | `MACRO_BEAR` | `76%` | `+35.0 bps` | Tendência neutra (-0.75% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,668.16 | ⚪ **CASH** | **-1.03%** | `MACRO_BEAR` | `82%` | `+26.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.06 | ⚪ **CASH** | **+0.36%** | `MACRO_BEAR` | `85%` | `+20.4 bps` | Tendência neutra (+0.36% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 01:00:56 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,856.02 | ⚪ **CASH** | **-0.76%** | `MACRO_BEAR` | `76%` | `+35.0 bps` | Tendência neutra (-0.76% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,660.67 | ⚪ **CASH** | **-1.05%** | `MACRO_BEAR` | `82%` | `+26.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.64 | ⚪ **CASH** | **+0.34%** | `MACRO_BEAR` | `85%` | `+20.4 bps` | Tendência neutra (+0.34% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 00:45:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,977.08 | ⚪ **CASH** | **-0.74%** | `MACRO_BEAR` | `76%` | `+27.1 bps` | Tendência neutra (-0.74% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,664.53 | ⚪ **CASH** | **-1.00%** | `MACRO_BEAR` | `82%` | `+26.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.76 | ⚪ **CASH** | **+0.35%** | `MACRO_BEAR` | `85%` | `+23.8 bps` | Tendência neutra (+0.35% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 00:30:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,987.38 | ⚪ **CASH** | **-0.74%** | `MACRO_BEAR` | `76%` | `+27.1 bps` | Tendência neutra (-0.74% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,665.19 | ⚪ **CASH** | **-1.00%** | `MACRO_BEAR` | `82%` | `+26.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.74 | ⚪ **CASH** | **+0.35%** | `MACRO_BEAR` | `85%` | `+23.8 bps` | Tendência neutra (+0.35% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 00:15:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,975.11 | ⚪ **CASH** | **-0.74%** | `MACRO_BEAR` | `76%` | `+27.1 bps` | Tendência neutra (-0.74% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,665.41 | ⚪ **CASH** | **-1.00%** | `MACRO_BEAR` | `82%` | `+26.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.81 | ⚪ **CASH** | **+0.35%** | `MACRO_BEAR` | `85%` | `+23.8 bps` | Tendência neutra (+0.35% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 00:00:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,943.62 | ⚪ **CASH** | **-0.74%** | `MACRO_BEAR` | `76%` | `+27.1 bps` | Tendência neutra (-0.74% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,663.36 | ⚪ **CASH** | **-1.00%** | `MACRO_BEAR` | `82%` | `+26.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.69 | ⚪ **CASH** | **+0.35%** | `MACRO_BEAR` | `85%` | `+23.8 bps` | Tendência neutra (+0.35% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 23:45:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,846.64 | ⚪ **CASH** | **-0.73%** | `MACRO_BEAR` | `76%` | `+32.8 bps` | Tendência neutra (-0.73% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,660.35 | ⚪ **CASH** | **-0.97%** | `MACRO_BEAR` | `82%` | `+26.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.48 | ⚪ **CASH** | **+0.34%** | `MACRO_BEAR` | `85%` | `+15.5 bps` | Tendência neutra (+0.34% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 23:30:54 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,854.01 | ⚪ **CASH** | **-0.73%** | `MACRO_BEAR` | `76%` | `+32.8 bps` | Tendência neutra (-0.73% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,659.73 | ⚪ **CASH** | **-0.97%** | `MACRO_BEAR` | `82%` | `+26.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.51 | ⚪ **CASH** | **+0.34%** | `MACRO_BEAR` | `85%` | `+15.5 bps` | Tendência neutra (+0.34% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 23:15:45 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,772.31 | ⚪ **CASH** | **-0.73%** | `MACRO_BEAR` | `76%` | `+32.8 bps` | Tendência neutra (-0.73% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,656.73 | ⚪ **CASH** | **-0.98%** | `MACRO_BEAR` | `82%` | `+26.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.27 | ⚪ **CASH** | **+0.33%** | `MACRO_BEAR` | `85%` | `+15.5 bps` | Tendência neutra (+0.33% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 23:00:56 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,842.96 | ⚪ **CASH** | **-0.73%** | `MACRO_BEAR` | `76%` | `+32.8 bps` | Tendência neutra (-0.73% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,659.87 | ⚪ **CASH** | **-0.97%** | `MACRO_BEAR` | `82%` | `+26.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.68 | ⚪ **CASH** | **+0.35%** | `MACRO_BEAR` | `85%` | `+15.5 bps` | Tendência neutra (+0.35% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 22:45:50 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,749.89 | ⚪ **CASH** | **-0.70%** | `MACRO_BEAR` | `76%` | `+32.2 bps` | Tendência neutra (-0.70% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,656.92 | ⚪ **CASH** | **-0.92%** | `MACRO_BEAR` | `82%` | `+27.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.55 | ⚪ **CASH** | **+0.36%** | `MACRO_BEAR` | `85%` | `+21.4 bps` | Tendência neutra (+0.36% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 22:30:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,754.11 | ⚪ **CASH** | **-0.70%** | `MACRO_BEAR` | `76%` | `+32.2 bps` | Tendência neutra (-0.70% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,659.03 | ⚪ **CASH** | **-0.92%** | `MACRO_BEAR` | `82%` | `+27.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.58 | ⚪ **CASH** | **+0.36%** | `MACRO_BEAR` | `85%` | `+21.4 bps` | Tendência neutra (+0.36% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 22:15:42 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,671.55 | ⚪ **CASH** | **-0.70%** | `MACRO_BEAR` | `76%` | `+32.2 bps` | Tendência neutra (-0.70% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,656.62 | ⚪ **CASH** | **-0.92%** | `MACRO_BEAR` | `82%` | `+27.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.51 | ⚪ **CASH** | **+0.35%** | `MACRO_BEAR` | `85%` | `+21.4 bps` | Tendência neutra (+0.35% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 22:00:46 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,754.07 | ⚪ **CASH** | **-0.70%** | `MACRO_BEAR` | `76%` | `+32.2 bps` | Tendência neutra (-0.70% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,662.61 | ⚪ **CASH** | **-0.91%** | `MACRO_BEAR` | `82%` | `+27.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.86 | ⚪ **CASH** | **+0.37%** | `MACRO_BEAR` | `85%` | `+21.4 bps` | Tendência neutra (+0.37% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 21:45:36 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,824.82 | ⚪ **CASH** | **-0.67%** | `MACRO_BEAR` | `76%` | `+46.4 bps` | Tendência neutra (-0.67% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,666.20 | ⚪ **CASH** | **-0.86%** | `MACRO_BEAR` | `82%` | `+31.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.00 | ⚪ **CASH** | **+0.37%** | `MACRO_BEAR` | `85%` | `+32.1 bps` | Tendência neutra (+0.37% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 21:30:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,803.18 | ⚪ **CASH** | **-0.67%** | `MACRO_BEAR` | `76%` | `+46.4 bps` | Tendência neutra (-0.67% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,665.20 | ⚪ **CASH** | **-0.86%** | `MACRO_BEAR` | `82%` | `+31.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.87 | ⚪ **CASH** | **+0.36%** | `MACRO_BEAR` | `85%` | `+32.1 bps` | Tendência neutra (+0.36% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 21:15:47 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,855.65 | ⚪ **CASH** | **-0.67%** | `MACRO_BEAR` | `76%` | `+46.4 bps` | Tendência neutra (-0.67% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,667.36 | ⚪ **CASH** | **-0.86%** | `MACRO_BEAR` | `82%` | `+31.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.95 | ⚪ **CASH** | **+0.37%** | `MACRO_BEAR` | `85%` | `+32.1 bps` | Tendência neutra (+0.37% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 21:00:54 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,864.01 | ⚪ **CASH** | **-0.67%** | `MACRO_BEAR` | `76%` | `+46.4 bps` | Tendência neutra (-0.67% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,669.09 | ⚪ **CASH** | **-0.86%** | `MACRO_BEAR` | `82%` | `+31.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.08 | ⚪ **CASH** | **+0.37%** | `MACRO_BEAR` | `85%` | `+32.1 bps` | Tendência neutra (+0.37% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 20:45:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,840.97 | ⚪ **CASH** | **-0.64%** | `MACRO_BEAR` | `77%` | `+36.6 bps` | Tendência neutra (-0.64% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,667.33 | ⚪ **CASH** | **-0.82%** | `MACRO_BEAR` | `82%` | `+45.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.08 | ⚪ **CASH** | **+0.37%** | `MACRO_BEAR` | `87%` | `+43.0 bps` | Tendência neutra (+0.37% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 20:31:00 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,818.83 | ⚪ **CASH** | **-0.64%** | `MACRO_BEAR` | `77%` | `+36.6 bps` | Tendência neutra (-0.64% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,667.52 | ⚪ **CASH** | **-0.82%** | `MACRO_BEAR` | `82%` | `+45.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.13 | ⚪ **CASH** | **+0.37%** | `MACRO_BEAR` | `87%` | `+43.0 bps` | Tendência neutra (+0.37% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 20:15:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,743.75 | ⚪ **CASH** | **-0.64%** | `MACRO_BEAR` | `77%` | `+36.6 bps` | Tendência neutra (-0.64% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,667.91 | ⚪ **CASH** | **-0.82%** | `MACRO_BEAR` | `82%` | `+45.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.99 | ⚪ **CASH** | **+0.36%** | `MACRO_BEAR` | `87%` | `+43.0 bps` | Tendência neutra (+0.36% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 20:00:59 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,865.75 | ⚪ **CASH** | **-0.64%** | `MACRO_BEAR` | `77%` | `+36.6 bps` | Tendência neutra (-0.64% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,669.72 | ⚪ **CASH** | **-0.82%** | `MACRO_BEAR` | `82%` | `+45.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.92 | ⚪ **CASH** | **+0.36%** | `MACRO_BEAR` | `87%` | `+43.0 bps` | Tendência neutra (+0.36% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 19:45:39 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,014.01 | ⚪ **CASH** | **-0.60%** | `MACRO_BEAR` | `77%` | `+32.3 bps` | Tendência neutra (-0.60% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,674.06 | ⚪ **CASH** | **-0.77%** | `MACRO_BEAR` | `82%` | `+35.9 bps` | Tendência neutra (-0.77% dentro do buffer ±0.80%) |
| **SOLUSDT** | $72.38 | ⚪ **CASH** | **+0.37%** | `MACRO_BEAR` | `87%` | `+44.1 bps` | Tendência neutra (+0.37% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 19:30:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,960.17 | ⚪ **CASH** | **-0.60%** | `MACRO_BEAR` | `77%` | `+32.3 bps` | Tendência neutra (-0.60% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,672.79 | ⚪ **CASH** | **-0.77%** | `MACRO_BEAR` | `82%` | `+35.9 bps` | Tendência neutra (-0.77% dentro do buffer ±0.80%) |
| **SOLUSDT** | $72.28 | ⚪ **CASH** | **+0.36%** | `MACRO_BEAR` | `87%` | `+44.1 bps` | Tendência neutra (+0.36% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 19:15:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,865.16 | ⚪ **CASH** | **-0.61%** | `MACRO_BEAR` | `77%` | `+32.3 bps` | Tendência neutra (-0.61% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,670.89 | ⚪ **CASH** | **-0.78%** | `MACRO_BEAR` | `82%` | `+35.9 bps` | Tendência neutra (-0.78% dentro do buffer ±0.80%) |
| **SOLUSDT** | $72.10 | ⚪ **CASH** | **+0.36%** | `MACRO_BEAR` | `87%` | `+44.1 bps` | Tendência neutra (+0.36% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 19:00:57 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,894.31 | ⚪ **CASH** | **-0.61%** | `MACRO_BEAR` | `77%` | `+32.3 bps` | Tendência neutra (-0.61% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,670.61 | ⚪ **CASH** | **-0.78%** | `MACRO_BEAR` | `82%` | `+35.9 bps` | Tendência neutra (-0.78% dentro do buffer ±0.80%) |
| **SOLUSDT** | $71.95 | ⚪ **CASH** | **+0.35%** | `MACRO_BEAR` | `87%` | `+44.1 bps` | Tendência neutra (+0.35% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 18:45:50 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,806.29 | ⚪ **CASH** | **-0.58%** | `MACRO_BEAR` | `77%` | `+33.8 bps` | Tendência neutra (-0.58% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,667.98 | ⚪ **CASH** | **-0.74%** | `MACRO_BEAR` | `82%` | `+31.0 bps` | Tendência neutra (-0.74% dentro do buffer ±0.80%) |
| **SOLUSDT** | $71.85 | ⚪ **CASH** | **+0.34%** | `MACRO_BEAR` | `87%` | `+42.8 bps` | Tendência neutra (+0.34% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 18:30:45 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,866.01 | ⚪ **CASH** | **-0.58%** | `MACRO_BEAR` | `77%` | `+33.8 bps` | Tendência neutra (-0.58% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,667.96 | ⚪ **CASH** | **-0.74%** | `MACRO_BEAR` | `82%` | `+31.0 bps` | Tendência neutra (-0.74% dentro do buffer ±0.80%) |
| **SOLUSDT** | $71.73 | ⚪ **CASH** | **+0.33%** | `MACRO_BEAR` | `87%` | `+42.8 bps` | Tendência neutra (+0.33% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 18:15:54 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,901.42 | ⚪ **CASH** | **-0.58%** | `MACRO_BEAR` | `77%` | `+33.8 bps` | Tendência neutra (-0.58% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,671.30 | ⚪ **CASH** | **-0.74%** | `MACRO_BEAR` | `82%` | `+31.0 bps` | Tendência neutra (-0.74% dentro do buffer ±0.80%) |
| **SOLUSDT** | $71.92 | ⚪ **CASH** | **+0.34%** | `MACRO_BEAR` | `87%` | `+42.8 bps` | Tendência neutra (+0.34% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-27 18:00:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,827.41 | ⚪ **CASH** | **-0.58%** | `MACRO_BEAR` | `77%` | `+33.8 bps` | Tendência neutra (-0.58% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,670.40 | ⚪ **CASH** | **-0.74%** | `MACRO_BEAR` | `82%` | `+31.0 bps` | Tendência neutra (-0.74% dentro do buffer ±0.80%) |
| **SOLUSDT** | $72.00 | ⚪ **CASH** | **+0.34%** | `MACRO_BEAR` | `87%` | `+42.8 bps` | Tendência neutra (+0.34% dentro do buffer ±0.80%) |
