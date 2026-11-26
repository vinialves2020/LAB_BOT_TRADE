# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-26 04:00:55 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-26 04:00:55 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,796.40 | ⚪ **CASH** | **-1.89%** | `MACRO_BEAR` | `79%` | `-18.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,699.20 | ⚪ **CASH** | **-2.02%** | `MACRO_BEAR` | `87%` | `-10.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.07 | ⚪ **CASH** | **-1.70%** | `MACRO_BEAR` | `92%` | `-40.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 03:45:57 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,817.56 | ⚪ **CASH** | **-1.95%** | `MACRO_BEAR` | `79%` | `-19.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,698.95 | ⚪ **CASH** | **-2.07%** | `MACRO_BEAR` | `87%` | `-22.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.22 | ⚪ **CASH** | **-1.76%** | `MACRO_BEAR` | `92%` | `-29.1 bps` | Tendência neutra (-1.76% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 03:30:46 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,677.98 | ⚪ **CASH** | **-1.96%** | `MACRO_BEAR` | `79%` | `-19.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,694.44 | ⚪ **CASH** | **-2.08%** | `MACRO_BEAR` | `87%` | `-22.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.01 | ⚪ **CASH** | **-1.77%** | `MACRO_BEAR` | `92%` | `-29.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 03:15:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,762.00 | ⚪ **CASH** | **-1.96%** | `MACRO_BEAR` | `79%` | `-19.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,698.87 | ⚪ **CASH** | **-2.07%** | `MACRO_BEAR` | `87%` | `-22.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.27 | ⚪ **CASH** | **-1.76%** | `MACRO_BEAR` | `92%` | `-29.1 bps` | Tendência neutra (-1.76% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 03:00:58 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,738.37 | ⚪ **CASH** | **-1.96%** | `MACRO_BEAR` | `79%` | `-19.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,698.78 | ⚪ **CASH** | **-2.07%** | `MACRO_BEAR` | `87%` | `-22.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.17 | ⚪ **CASH** | **-1.76%** | `MACRO_BEAR` | `92%` | `-29.1 bps` | Tendência neutra (-1.76% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 02:45:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,984.37 | ⚪ **CASH** | **-2.01%** | `MACRO_BEAR` | `79%` | `-20.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,703.30 | ⚪ **CASH** | **-2.12%** | `MACRO_BEAR` | `88%` | `-20.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.35 | ⚪ **CASH** | **-1.83%** | `MACRO_BEAR` | `93%` | `-36.5 bps` | Tendência neutra (-1.83% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 02:30:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,950.30 | ⚪ **CASH** | **-2.01%** | `MACRO_BEAR` | `79%` | `-20.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,703.04 | ⚪ **CASH** | **-2.12%** | `MACRO_BEAR` | `88%` | `-20.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.30 | ⚪ **CASH** | **-1.83%** | `MACRO_BEAR` | `93%` | `-36.5 bps` | Tendência neutra (-1.83% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 02:15:41 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,887.00 | ⚪ **CASH** | **-2.01%** | `MACRO_BEAR` | `79%` | `-20.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,703.13 | ⚪ **CASH** | **-2.12%** | `MACRO_BEAR` | `88%` | `-20.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.38 | ⚪ **CASH** | **-1.83%** | `MACRO_BEAR` | `93%` | `-36.5 bps` | Tendência neutra (-1.83% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 02:00:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,800.01 | ⚪ **CASH** | **-2.02%** | `MACRO_BEAR` | `79%` | `-20.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,699.93 | ⚪ **CASH** | **-2.13%** | `MACRO_BEAR` | `88%` | `-20.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.04 | ⚪ **CASH** | **-1.84%** | `MACRO_BEAR` | `93%` | `-36.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 01:45:43 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,771.25 | ⚪ **CASH** | **-2.09%** | `MACRO_BEAR` | `79%` | `-18.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,701.13 | ⚪ **CASH** | **-2.19%** | `MACRO_BEAR` | `88%` | `-1.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.93 | ⚪ **CASH** | **-1.93%** | `MACRO_BEAR` | `93%` | `+2.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 01:30:54 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,774.01 | ⚪ **CASH** | **-2.09%** | `MACRO_BEAR` | `79%` | `-18.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,702.40 | ⚪ **CASH** | **-2.19%** | `MACRO_BEAR` | `88%` | `-1.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.95 | ⚪ **CASH** | **-1.92%** | `MACRO_BEAR` | `93%` | `+2.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 01:15:42 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,784.00 | ⚪ **CASH** | **-2.09%** | `MACRO_BEAR` | `79%` | `-18.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,704.36 | ⚪ **CASH** | **-2.18%** | `MACRO_BEAR` | `88%` | `-1.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.06 | ⚪ **CASH** | **-1.92%** | `MACRO_BEAR` | `93%` | `+2.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 01:00:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,481.36 | ⚪ **CASH** | **-2.11%** | `MACRO_BEAR` | `79%` | `-18.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,696.22 | ⚪ **CASH** | **-2.20%** | `MACRO_BEAR` | `88%` | `-1.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.74 | ⚪ **CASH** | **-1.93%** | `MACRO_BEAR` | `93%` | `+2.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 00:45:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,604.01 | ⚪ **CASH** | **-2.16%** | `MACRO_BEAR` | `79%` | `-18.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,697.29 | ⚪ **CASH** | **-2.26%** | `MACRO_BEAR` | `88%` | `+0.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.83 | ⚪ **CASH** | **-2.00%** | `MACRO_BEAR` | `93%` | `-7.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 00:30:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,807.16 | ⚪ **CASH** | **-2.15%** | `MACRO_BEAR` | `79%` | `-18.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,704.44 | ⚪ **CASH** | **-2.24%** | `MACRO_BEAR` | `88%` | `+0.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.09 | ⚪ **CASH** | **-1.99%** | `MACRO_BEAR` | `93%` | `-7.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 00:15:45 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,861.40 | ⚪ **CASH** | **-2.15%** | `MACRO_BEAR` | `79%` | `-18.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,705.02 | ⚪ **CASH** | **-2.24%** | `MACRO_BEAR` | `88%` | `+0.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.02 | ⚪ **CASH** | **-1.99%** | `MACRO_BEAR` | `93%` | `-7.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 00:00:56 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,512.57 | ⚪ **CASH** | **-2.17%** | `MACRO_BEAR` | `79%` | `-18.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,693.63 | ⚪ **CASH** | **-2.26%** | `MACRO_BEAR` | `88%` | `+0.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.56 | ⚪ **CASH** | **-2.01%** | `MACRO_BEAR` | `93%` | `-7.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 23:45:37 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,364.30 | ⚪ **CASH** | **-2.23%** | `MACRO_BEAR` | `79%` | `-6.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,692.97 | ⚪ **CASH** | **-2.32%** | `MACRO_BEAR` | `88%` | `+3.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.43 | ⚪ **CASH** | **-2.07%** | `MACRO_BEAR` | `93%` | `+29.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 23:30:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,183.53 | ⚪ **CASH** | **-2.24%** | `MACRO_BEAR` | `79%` | `-6.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,689.79 | ⚪ **CASH** | **-2.32%** | `MACRO_BEAR` | `88%` | `+3.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.34 | ⚪ **CASH** | **-2.08%** | `MACRO_BEAR` | `93%` | `+29.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 23:15:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,282.46 | ⚪ **CASH** | **-2.23%** | `MACRO_BEAR` | `79%` | `-6.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,689.88 | ⚪ **CASH** | **-2.32%** | `MACRO_BEAR` | `88%` | `+3.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.59 | ⚪ **CASH** | **-2.07%** | `MACRO_BEAR` | `93%` | `+29.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 23:00:54 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,018.00 | ⚪ **CASH** | **-2.25%** | `MACRO_BEAR` | `79%` | `-6.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,682.16 | ⚪ **CASH** | **-2.33%** | `MACRO_BEAR` | `88%` | `+3.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.32 | ⚪ **CASH** | **-2.08%** | `MACRO_BEAR` | `93%` | `+29.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 22:45:47 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,210.82 | ⚪ **CASH** | **-2.28%** | `MACRO_BEAR` | `80%` | `-11.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,688.04 | ⚪ **CASH** | **-2.37%** | `MACRO_BEAR` | `88%` | `-3.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.50 | ⚪ **CASH** | **-2.13%** | `MACRO_BEAR` | `93%` | `+26.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 22:30:46 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,139.83 | ⚪ **CASH** | **-2.29%** | `MACRO_BEAR` | `80%` | `-11.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,685.04 | ⚪ **CASH** | **-2.37%** | `MACRO_BEAR` | `88%` | `-3.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.44 | ⚪ **CASH** | **-2.13%** | `MACRO_BEAR` | `93%` | `+26.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 22:15:45 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,126.47 | ⚪ **CASH** | **-2.29%** | `MACRO_BEAR` | `80%` | `-11.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,684.17 | ⚪ **CASH** | **-2.37%** | `MACRO_BEAR` | `88%` | `-3.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.53 | ⚪ **CASH** | **-2.13%** | `MACRO_BEAR` | `93%` | `+26.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 22:00:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,168.79 | ⚪ **CASH** | **-2.28%** | `MACRO_BEAR` | `80%` | `-11.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,684.13 | ⚪ **CASH** | **-2.37%** | `MACRO_BEAR` | `88%` | `-3.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.57 | ⚪ **CASH** | **-2.13%** | `MACRO_BEAR` | `93%` | `+26.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 21:45:38 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,278.27 | ⚪ **CASH** | **-2.33%** | `MACRO_BEAR` | `80%` | `-5.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,688.76 | ⚪ **CASH** | **-2.41%** | `MACRO_BEAR` | `88%` | `-3.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.82 | ⚪ **CASH** | **-2.19%** | `MACRO_BEAR` | `93%` | `+25.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 21:30:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,360.43 | ⚪ **CASH** | **-2.33%** | `MACRO_BEAR` | `80%` | `-5.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,691.64 | ⚪ **CASH** | **-2.41%** | `MACRO_BEAR` | `88%` | `-3.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.69 | ⚪ **CASH** | **-2.19%** | `MACRO_BEAR` | `93%` | `+25.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 21:15:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,235.25 | ⚪ **CASH** | **-2.33%** | `MACRO_BEAR` | `80%` | `-5.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,687.16 | ⚪ **CASH** | **-2.41%** | `MACRO_BEAR` | `88%` | `-3.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.53 | ⚪ **CASH** | **-2.20%** | `MACRO_BEAR` | `93%` | `+25.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 21:00:57 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,182.47 | ⚪ **CASH** | **-2.34%** | `MACRO_BEAR` | `80%` | `-5.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,688.33 | ⚪ **CASH** | **-2.41%** | `MACRO_BEAR` | `88%` | `-3.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.51 | ⚪ **CASH** | **-2.20%** | `MACRO_BEAR` | `93%` | `+25.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 20:45:38 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,949.18 | ⚪ **CASH** | **-2.40%** | `MACRO_BEAR` | `80%` | `-9.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,682.57 | ⚪ **CASH** | **-2.47%** | `MACRO_BEAR` | `88%` | `+13.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.22 | ⚪ **CASH** | **-2.28%** | `MACRO_BEAR` | `93%` | `+45.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 20:30:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,846.99 | ⚪ **CASH** | **-2.41%** | `MACRO_BEAR` | `80%` | `-9.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,680.93 | ⚪ **CASH** | **-2.48%** | `MACRO_BEAR` | `88%` | `+13.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.26 | ⚪ **CASH** | **-2.28%** | `MACRO_BEAR` | `93%` | `+45.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 20:15:50 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,060.01 | ⚪ **CASH** | **-2.40%** | `MACRO_BEAR` | `80%` | `-9.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,686.27 | ⚪ **CASH** | **-2.47%** | `MACRO_BEAR` | `88%` | `+13.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.50 | ⚪ **CASH** | **-2.27%** | `MACRO_BEAR` | `93%` | `+45.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 20:00:56 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,945.21 | ⚪ **CASH** | **-2.40%** | `MACRO_BEAR` | `80%` | `-9.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,685.89 | ⚪ **CASH** | **-2.47%** | `MACRO_BEAR` | `88%` | `+13.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.36 | ⚪ **CASH** | **-2.28%** | `MACRO_BEAR` | `93%` | `+45.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 19:45:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,942.01 | ⚪ **CASH** | **-2.44%** | `MACRO_BEAR` | `80%` | `-13.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,686.04 | ⚪ **CASH** | **-2.51%** | `MACRO_BEAR` | `88%` | `+10.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.49 | ⚪ **CASH** | **-2.33%** | `MACRO_BEAR` | `93%` | `+38.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 19:30:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,107.72 | ⚪ **CASH** | **-2.43%** | `MACRO_BEAR` | `80%` | `-13.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,689.48 | ⚪ **CASH** | **-2.51%** | `MACRO_BEAR` | `88%` | `+10.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.56 | ⚪ **CASH** | **-2.33%** | `MACRO_BEAR` | `93%` | `+38.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-25 19:15:37 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,036.01 | ⚪ **CASH** | **-2.44%** | `MACRO_BEAR` | `80%` | `-13.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,689.46 | ⚪ **CASH** | **-2.51%** | `MACRO_BEAR` | `88%` | `+10.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.33 | ⚪ **CASH** | **-2.34%** | `MACRO_BEAR` | `93%` | `+38.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
