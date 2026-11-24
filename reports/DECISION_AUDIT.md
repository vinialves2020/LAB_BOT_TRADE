# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-24 06:15:49 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-24 06:15:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,440.00 | ⚪ **CASH** | **-1.77%** | `MACRO_BEAR` | `78%` | `+23.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,699.35 | ⚪ **CASH** | **-1.77%** | `MACRO_BEAR` | `89%` | `+36.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.60 | ⚪ **CASH** | **-0.68%** | `MACRO_BEAR` | `93%` | `+34.2 bps` | Tendência neutra (-0.68% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 06:00:41 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,638.30 | ⚪ **CASH** | **-1.76%** | `MACRO_BEAR` | `78%` | `+23.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,706.20 | ⚪ **CASH** | **-1.76%** | `MACRO_BEAR` | `89%` | `+36.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.81 | ⚪ **CASH** | **-0.67%** | `MACRO_BEAR` | `93%` | `+34.2 bps` | Tendência neutra (-0.67% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 05:45:36 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,707.35 | ⚪ **CASH** | **-1.76%** | `MACRO_BEAR` | `78%` | `+51.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,708.52 | ⚪ **CASH** | **-1.76%** | `MACRO_BEAR` | `89%` | `+42.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.86 | ⚪ **CASH** | **-0.68%** | `MACRO_BEAR` | `93%` | `+33.9 bps` | Tendência neutra (-0.68% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 05:30:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,761.21 | ⚪ **CASH** | **-1.76%** | `MACRO_BEAR` | `78%` | `+51.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,709.72 | ⚪ **CASH** | **-1.76%** | `MACRO_BEAR` | `89%` | `+42.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.80 | ⚪ **CASH** | **-0.68%** | `MACRO_BEAR` | `93%` | `+33.9 bps` | Tendência neutra (-0.68% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 05:15:47 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,617.08 | ⚪ **CASH** | **-1.77%** | `MACRO_BEAR` | `78%` | `+51.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,705.40 | ⚪ **CASH** | **-1.77%** | `MACRO_BEAR` | `89%` | `+42.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.88 | ⚪ **CASH** | **-0.67%** | `MACRO_BEAR` | `93%` | `+33.9 bps` | Tendência neutra (-0.67% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 05:00:57 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,380.14 | ⚪ **CASH** | **-1.78%** | `MACRO_BEAR` | `78%` | `+51.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,699.61 | ⚪ **CASH** | **-1.78%** | `MACRO_BEAR` | `89%` | `+42.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.52 | ⚪ **CASH** | **-0.69%** | `MACRO_BEAR` | `93%` | `+33.9 bps` | Tendência neutra (-0.69% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 04:45:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,542.81 | ⚪ **CASH** | **-1.76%** | `MACRO_BEAR` | `78%` | `+53.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,704.83 | ⚪ **CASH** | **-1.76%** | `MACRO_BEAR` | `89%` | `+59.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.87 | ⚪ **CASH** | **-0.67%** | `MACRO_BEAR` | `93%` | `+39.1 bps` | Tendência neutra (-0.67% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 04:30:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,511.63 | ⚪ **CASH** | **-1.76%** | `MACRO_BEAR` | `78%` | `+53.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,700.02 | ⚪ **CASH** | **-1.77%** | `MACRO_BEAR` | `89%` | `+59.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.84 | ⚪ **CASH** | **-0.67%** | `MACRO_BEAR` | `93%` | `+39.1 bps` | Tendência neutra (-0.67% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 04:15:36 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,406.00 | ⚪ **CASH** | **-1.76%** | `MACRO_BEAR` | `78%` | `+53.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,697.53 | ⚪ **CASH** | **-1.77%** | `MACRO_BEAR` | `88%` | `+59.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.69 | ⚪ **CASH** | **-0.68%** | `MACRO_BEAR` | `93%` | `+39.1 bps` | Tendência neutra (-0.68% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 04:00:55 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,316.30 | ⚪ **CASH** | **-1.77%** | `MACRO_BEAR` | `78%` | `+53.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,696.34 | ⚪ **CASH** | **-1.77%** | `MACRO_BEAR` | `88%` | `+59.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.38 | ⚪ **CASH** | **-0.69%** | `MACRO_BEAR` | `93%` | `+39.1 bps` | Tendência neutra (-0.69% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 03:45:41 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,314.41 | ⚪ **CASH** | **-1.75%** | `MACRO_BEAR` | `78%` | `+38.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,693.35 | ⚪ **CASH** | **-1.76%** | `MACRO_BEAR` | `88%` | `+71.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.09 | ⚪ **CASH** | **-0.69%** | `MACRO_BEAR` | `93%` | `+70.6 bps` | Tendência neutra (-0.69% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 03:30:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,234.19 | ⚪ **CASH** | **-1.76%** | `MACRO_BEAR` | `78%` | `+38.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,691.66 | ⚪ **CASH** | **-1.77%** | `MACRO_BEAR` | `88%` | `+71.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.05 | ⚪ **CASH** | **-0.69%** | `MACRO_BEAR` | `93%` | `+70.6 bps` | Tendência neutra (-0.69% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 03:15:43 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,552.01 | ⚪ **CASH** | **-1.79%** | `MACRO_BEAR` | `78%` | `+38.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,675.09 | ⚪ **CASH** | **-1.79%** | `MACRO_BEAR` | `88%` | `+71.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.38 | ⚪ **CASH** | **-0.72%** | `MACRO_BEAR` | `93%` | `+70.6 bps` | Tendência neutra (-0.72% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 03:00:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,197.23 | ⚪ **CASH** | **-1.76%** | `MACRO_BEAR` | `78%` | `+38.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,689.33 | ⚪ **CASH** | **-1.77%** | `MACRO_BEAR` | `88%` | `+71.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.00 | ⚪ **CASH** | **-0.70%** | `MACRO_BEAR` | `93%` | `+70.6 bps` | Tendência neutra (-0.70% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 02:45:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,337.97 | ⚪ **CASH** | **-1.72%** | `MACRO_BEAR` | `78%` | `-4.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,689.20 | ⚪ **CASH** | **-1.74%** | `MACRO_BEAR` | `89%` | `+41.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.15 | ⚪ **CASH** | **-0.66%** | `MACRO_BEAR` | `93%` | `+31.5 bps` | Tendência neutra (-0.66% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 02:30:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,682.50 | ⚪ **CASH** | **-1.71%** | `MACRO_BEAR` | `77%` | `-4.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,697.68 | ⚪ **CASH** | **-1.72%** | `MACRO_BEAR` | `88%` | `+41.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.29 | ⚪ **CASH** | **-0.65%** | `MACRO_BEAR` | `93%` | `+31.5 bps` | Tendência neutra (-0.65% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 02:15:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,851.70 | ⚪ **CASH** | **-1.70%** | `MACRO_BEAR` | `77%` | `-4.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,703.42 | ⚪ **CASH** | **-1.71%** | `MACRO_BEAR` | `88%` | `+41.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.71 | ⚪ **CASH** | **-0.64%** | `MACRO_BEAR` | `93%` | `+31.5 bps` | Tendência neutra (-0.64% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 02:00:56 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,060.01 | ⚪ **CASH** | **-1.69%** | `MACRO_BEAR` | `77%` | `-4.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,703.95 | ⚪ **CASH** | **-1.71%** | `MACRO_BEAR` | `88%` | `+41.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.78 | ⚪ **CASH** | **-0.63%** | `MACRO_BEAR` | `93%` | `+31.5 bps` | Tendência neutra (-0.63% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 01:45:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,516.93 | ⚪ **CASH** | **-1.68%** | `MACRO_BEAR` | `77%` | `+13.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,718.39 | ⚪ **CASH** | **-1.68%** | `MACRO_BEAR` | `88%` | `+49.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.49 | ⚪ **CASH** | **-0.61%** | `MACRO_BEAR` | `93%` | `+47.8 bps` | Tendência neutra (-0.61% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 01:30:39 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,505.05 | ⚪ **CASH** | **-1.68%** | `MACRO_BEAR` | `77%` | `+13.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,718.01 | ⚪ **CASH** | **-1.68%** | `MACRO_BEAR` | `88%` | `+49.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.53 | ⚪ **CASH** | **-0.61%** | `MACRO_BEAR` | `93%` | `+47.8 bps` | Tendência neutra (-0.61% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 01:15:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,528.30 | ⚪ **CASH** | **-1.68%** | `MACRO_BEAR` | `77%` | `+13.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,718.67 | ⚪ **CASH** | **-1.68%** | `MACRO_BEAR` | `88%` | `+49.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.46 | ⚪ **CASH** | **-0.61%** | `MACRO_BEAR` | `93%` | `+47.8 bps` | Tendência neutra (-0.61% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 01:00:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,346.26 | ⚪ **CASH** | **-1.69%** | `MACRO_BEAR` | `77%` | `+13.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,712.43 | ⚪ **CASH** | **-1.69%** | `MACRO_BEAR` | `88%` | `+49.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.24 | ⚪ **CASH** | **-0.62%** | `MACRO_BEAR` | `93%` | `+47.8 bps` | Tendência neutra (-0.62% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 00:45:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,290.64 | ⚪ **CASH** | **-1.72%** | `MACRO_BEAR` | `77%` | `+16.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,711.23 | ⚪ **CASH** | **-1.70%** | `MACRO_BEAR` | `88%` | `+44.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.16 | ⚪ **CASH** | **-0.64%** | `MACRO_BEAR` | `93%` | `+52.0 bps` | Tendência neutra (-0.64% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 00:30:47 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,247.77 | ⚪ **CASH** | **-1.72%** | `MACRO_BEAR` | `77%` | `+16.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,710.88 | ⚪ **CASH** | **-1.70%** | `MACRO_BEAR` | `88%` | `+44.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.14 | ⚪ **CASH** | **-0.64%** | `MACRO_BEAR` | `93%` | `+52.0 bps` | Tendência neutra (-0.64% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 00:15:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,264.47 | ⚪ **CASH** | **-1.72%** | `MACRO_BEAR` | `77%` | `+16.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,709.74 | ⚪ **CASH** | **-1.70%** | `MACRO_BEAR` | `88%` | `+44.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.00 | ⚪ **CASH** | **-0.65%** | `MACRO_BEAR` | `93%` | `+52.0 bps` | Tendência neutra (-0.65% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 00:00:58 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,238.12 | ⚪ **CASH** | **-1.72%** | `MACRO_BEAR` | `77%` | `+16.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,710.06 | ⚪ **CASH** | **-1.70%** | `MACRO_BEAR` | `88%` | `+44.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.98 | ⚪ **CASH** | **-0.65%** | `MACRO_BEAR` | `93%` | `+52.0 bps` | Tendência neutra (-0.65% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 23:45:50 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,191.82 | ⚪ **CASH** | **-1.75%** | `MACRO_BEAR` | `77%` | `-32.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,707.13 | ⚪ **CASH** | **-1.71%** | `MACRO_BEAR` | `88%` | `+53.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.74 | ⚪ **CASH** | **-0.67%** | `MACRO_BEAR` | `93%` | `+73.5 bps` | Tendência neutra (-0.67% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 23:31:11 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,545.89 | ⚪ **CASH** | **-1.73%** | `MACRO_BEAR` | `77%` | `-32.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,718.72 | ⚪ **CASH** | **-1.69%** | `MACRO_BEAR` | `88%` | `+53.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.21 | ⚪ **CASH** | **-0.65%** | `MACRO_BEAR` | `93%` | `+73.5 bps` | Tendência neutra (-0.65% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 23:15:42 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,463.03 | ⚪ **CASH** | **-1.74%** | `MACRO_BEAR` | `77%` | `-32.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,718.47 | ⚪ **CASH** | **-1.69%** | `MACRO_BEAR` | `88%` | `+53.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.98 | ⚪ **CASH** | **-0.66%** | `MACRO_BEAR` | `93%` | `+73.5 bps` | Tendência neutra (-0.66% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 23:00:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,322.81 | ⚪ **CASH** | **-1.74%** | `MACRO_BEAR` | `77%` | `-32.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,714.29 | ⚪ **CASH** | **-1.70%** | `MACRO_BEAR` | `88%` | `+53.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.05 | ⚪ **CASH** | **-0.66%** | `MACRO_BEAR` | `93%` | `+73.5 bps` | Tendência neutra (-0.66% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 22:45:43 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,180.00 | ⚪ **CASH** | **-1.78%** | `MACRO_BEAR` | `77%` | `-42.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,711.19 | ⚪ **CASH** | **-1.71%** | `MACRO_BEAR` | `88%` | `+46.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.03 | ⚪ **CASH** | **-0.67%** | `MACRO_BEAR` | `93%` | `+59.1 bps` | Tendência neutra (-0.67% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 22:30:43 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,219.53 | ⚪ **CASH** | **-1.77%** | `MACRO_BEAR` | `77%` | `-42.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,715.26 | ⚪ **CASH** | **-1.70%** | `MACRO_BEAR` | `88%` | `+46.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.21 | ⚪ **CASH** | **-0.66%** | `MACRO_BEAR` | `93%` | `+59.1 bps` | Tendência neutra (-0.66% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 22:15:57 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,222.10 | ⚪ **CASH** | **-1.77%** | `MACRO_BEAR` | `77%` | `-42.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,718.61 | ⚪ **CASH** | **-1.69%** | `MACRO_BEAR` | `88%` | `+46.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.19 | ⚪ **CASH** | **-0.66%** | `MACRO_BEAR` | `93%` | `+59.1 bps` | Tendência neutra (-0.66% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 22:00:50 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,315.27 | ⚪ **CASH** | **-1.77%** | `MACRO_BEAR` | `77%` | `-42.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,723.67 | ⚪ **CASH** | **-1.69%** | `MACRO_BEAR` | `88%` | `+46.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.39 | ⚪ **CASH** | **-0.65%** | `MACRO_BEAR` | `93%` | `+59.1 bps` | Tendência neutra (-0.65% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 21:45:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,152.68 | ⚪ **CASH** | **-1.81%** | `MACRO_BEAR` | `77%` | `-34.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,715.97 | ⚪ **CASH** | **-1.72%** | `MACRO_BEAR` | `88%` | `+35.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.21 | ⚪ **CASH** | **-0.69%** | `MACRO_BEAR` | `93%` | `+67.9 bps` | Tendência neutra (-0.69% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 21:30:54 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,420.76 | ⚪ **CASH** | **-1.79%** | `MACRO_BEAR` | `77%` | `-34.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,724.12 | ⚪ **CASH** | **-1.71%** | `MACRO_BEAR` | `88%` | `+35.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.56 | ⚪ **CASH** | **-0.68%** | `MACRO_BEAR` | `93%` | `+67.9 bps` | Tendência neutra (-0.68% dentro do buffer ±0.80%) |
