# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-28 09:15:47 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-28 09:15:47 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,608.00 | ⚪ **CASH** | **-0.90%** | `MACRO_BEAR` | `66%` | `+22.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,651.36 | ⚪ **CASH** | **-1.31%** | `MACRO_BEAR` | `70%` | `-18.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.06 | ⚪ **CASH** | **+0.23%** | `MACRO_BEAR` | `74%` | `-0.2 bps` | Tendência neutra (+0.23% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 09:00:50 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,567.91 | ⚪ **CASH** | **-0.90%** | `MACRO_BEAR` | `66%` | `+22.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,653.00 | ⚪ **CASH** | **-1.30%** | `MACRO_BEAR` | `70%` | `-18.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.02 | ⚪ **CASH** | **+0.23%** | `MACRO_BEAR` | `74%` | `-0.2 bps` | Tendência neutra (+0.23% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 08:45:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,610.50 | ⚪ **CASH** | **-0.87%** | `MACRO_BEAR` | `66%` | `+19.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,652.58 | ⚪ **CASH** | **-1.27%** | `MACRO_BEAR` | `70%` | `-17.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.00 | ⚪ **CASH** | **+0.26%** | `MACRO_BEAR` | `75%` | `+3.6 bps` | Tendência neutra (+0.26% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 08:30:56 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,690.85 | ⚪ **CASH** | **-0.87%** | `MACRO_BEAR` | `66%` | `+19.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,655.93 | ⚪ **CASH** | **-1.26%** | `MACRO_BEAR` | `70%` | `-17.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.24 | ⚪ **CASH** | **+0.27%** | `MACRO_BEAR` | `75%` | `+3.6 bps` | Tendência neutra (+0.27% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 08:15:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,674.00 | ⚪ **CASH** | **-0.87%** | `MACRO_BEAR` | `66%` | `+19.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,654.43 | ⚪ **CASH** | **-1.27%** | `MACRO_BEAR` | `70%` | `-17.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.05 | ⚪ **CASH** | **+0.26%** | `MACRO_BEAR` | `75%` | `+3.6 bps` | Tendência neutra (+0.26% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 08:00:56 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,861.76 | ⚪ **CASH** | **-0.86%** | `MACRO_BEAR` | `66%` | `+19.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,659.13 | ⚪ **CASH** | **-1.26%** | `MACRO_BEAR` | `70%` | `-17.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.29 | ⚪ **CASH** | **+0.27%** | `MACRO_BEAR` | `75%` | `+3.6 bps` | Tendência neutra (+0.27% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 07:45:40 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,780.84 | ⚪ **CASH** | **-0.85%** | `MACRO_BEAR` | `66%` | `+24.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,657.25 | ⚪ **CASH** | **-1.23%** | `MACRO_BEAR` | `70%` | `-7.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.20 | ⚪ **CASH** | **+0.28%** | `MACRO_BEAR` | `75%` | `+7.1 bps` | Tendência neutra (+0.28% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 07:30:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,727.14 | ⚪ **CASH** | **-0.85%** | `MACRO_BEAR` | `66%` | `+24.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,656.07 | ⚪ **CASH** | **-1.23%** | `MACRO_BEAR` | `70%` | `-7.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.20 | ⚪ **CASH** | **+0.28%** | `MACRO_BEAR` | `75%` | `+7.1 bps` | Tendência neutra (+0.28% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 07:15:46 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,694.49 | ⚪ **CASH** | **-0.85%** | `MACRO_BEAR` | `66%` | `+24.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,654.39 | ⚪ **CASH** | **-1.24%** | `MACRO_BEAR` | `70%` | `-7.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.23 | ⚪ **CASH** | **+0.29%** | `MACRO_BEAR` | `75%` | `+7.1 bps` | Tendência neutra (+0.29% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 07:00:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,770.15 | ⚪ **CASH** | **-0.85%** | `MACRO_BEAR` | `66%` | `+24.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,658.14 | ⚪ **CASH** | **-1.23%** | `MACRO_BEAR` | `70%` | `-7.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.45 | ⚪ **CASH** | **+0.29%** | `MACRO_BEAR` | `75%` | `+7.1 bps` | Tendência neutra (+0.29% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 06:45:50 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,860.59 | ⚪ **CASH** | **-0.83%** | `MACRO_BEAR` | `66%` | `+23.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,661.11 | ⚪ **CASH** | **-1.19%** | `MACRO_BEAR` | `70%` | `+0.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.47 | ⚪ **CASH** | **+0.31%** | `MACRO_BEAR` | `75%` | `+12.7 bps` | Tendência neutra (+0.31% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 06:30:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,860.00 | ⚪ **CASH** | **-0.83%** | `MACRO_BEAR` | `66%` | `+23.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,659.96 | ⚪ **CASH** | **-1.19%** | `MACRO_BEAR` | `70%` | `+0.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.50 | ⚪ **CASH** | **+0.31%** | `MACRO_BEAR` | `75%` | `+12.7 bps` | Tendência neutra (+0.31% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 06:15:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,756.44 | ⚪ **CASH** | **-0.83%** | `MACRO_BEAR` | `66%` | `+23.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,657.54 | ⚪ **CASH** | **-1.20%** | `MACRO_BEAR` | `70%` | `+0.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.35 | ⚪ **CASH** | **+0.30%** | `MACRO_BEAR` | `75%` | `+12.7 bps` | Tendência neutra (+0.30% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 06:01:01 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,773.51 | ⚪ **CASH** | **-0.83%** | `MACRO_BEAR` | `66%` | `+23.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,656.72 | ⚪ **CASH** | **-1.20%** | `MACRO_BEAR` | `70%` | `+0.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.25 | ⚪ **CASH** | **+0.30%** | `MACRO_BEAR` | `75%` | `+12.7 bps` | Tendência neutra (+0.30% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 05:45:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,740.59 | ⚪ **CASH** | **-0.81%** | `MACRO_BEAR` | `72%` | `+24.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,655.09 | ⚪ **CASH** | **-1.16%** | `MACRO_BEAR` | `79%` | `+7.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.22 | ⚪ **CASH** | **+0.32%** | `MACRO_BEAR` | `81%` | `+10.9 bps` | Tendência neutra (+0.32% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 05:30:50 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,802.01 | ⚪ **CASH** | **-0.81%** | `MACRO_BEAR` | `72%` | `+24.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,657.85 | ⚪ **CASH** | **-1.16%** | `MACRO_BEAR` | `79%` | `+7.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.42 | ⚪ **CASH** | **+0.33%** | `MACRO_BEAR` | `81%` | `+10.9 bps` | Tendência neutra (+0.33% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 05:15:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,808.37 | ⚪ **CASH** | **-0.81%** | `MACRO_BEAR` | `72%` | `+24.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,658.02 | ⚪ **CASH** | **-1.16%** | `MACRO_BEAR` | `79%` | `+7.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.32 | ⚪ **CASH** | **+0.33%** | `MACRO_BEAR` | `81%` | `+10.9 bps` | Tendência neutra (+0.33% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 05:00:57 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,949.96 | ⚪ **CASH** | **-0.80%** | `MACRO_BEAR` | `72%` | `+24.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,661.13 | ⚪ **CASH** | **-1.15%** | `MACRO_BEAR` | `79%` | `+7.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.50 | ⚪ **CASH** | **+0.33%** | `MACRO_BEAR` | `81%` | `+10.9 bps` | Tendência neutra (+0.33% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 04:45:50 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,024.01 | ⚪ **CASH** | **-0.79%** | `MACRO_BEAR` | `72%` | `+20.6 bps` | Tendência neutra (-0.79% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,663.81 | ⚪ **CASH** | **-1.12%** | `MACRO_BEAR` | `79%` | `+8.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.61 | ⚪ **CASH** | **+0.35%** | `MACRO_BEAR` | `82%` | `+17.5 bps` | Tendência neutra (+0.35% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 04:30:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,007.44 | ⚪ **CASH** | **-0.79%** | `MACRO_BEAR` | `72%` | `+20.6 bps` | Tendência neutra (-0.79% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,664.35 | ⚪ **CASH** | **-1.12%** | `MACRO_BEAR` | `79%` | `+8.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.61 | ⚪ **CASH** | **+0.35%** | `MACRO_BEAR` | `82%` | `+17.5 bps` | Tendência neutra (+0.35% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 04:15:50 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,063.03 | ⚪ **CASH** | **-0.78%** | `MACRO_BEAR` | `72%` | `+20.6 bps` | Tendência neutra (-0.78% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,666.11 | ⚪ **CASH** | **-1.12%** | `MACRO_BEAR` | `79%` | `+8.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.72 | ⚪ **CASH** | **+0.35%** | `MACRO_BEAR` | `82%` | `+17.5 bps` | Tendência neutra (+0.35% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 04:00:56 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,063.62 | ⚪ **CASH** | **-0.78%** | `MACRO_BEAR` | `72%` | `+20.6 bps` | Tendência neutra (-0.78% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,666.93 | ⚪ **CASH** | **-1.12%** | `MACRO_BEAR` | `79%` | `+8.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.76 | ⚪ **CASH** | **+0.35%** | `MACRO_BEAR` | `82%` | `+17.5 bps` | Tendência neutra (+0.35% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 03:45:46 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,969.50 | ⚪ **CASH** | **-0.78%** | `MACRO_BEAR` | `73%` | `+41.4 bps` | Tendência neutra (-0.78% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,664.25 | ⚪ **CASH** | **-1.10%** | `MACRO_BEAR` | `79%` | `+16.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.71 | ⚪ **CASH** | **+0.35%** | `MACRO_BEAR` | `82%` | `+15.9 bps` | Tendência neutra (+0.35% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 03:30:50 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,931.68 | ⚪ **CASH** | **-0.78%** | `MACRO_BEAR` | `73%` | `+41.4 bps` | Tendência neutra (-0.78% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,662.83 | ⚪ **CASH** | **-1.10%** | `MACRO_BEAR` | `79%` | `+16.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.57 | ⚪ **CASH** | **+0.35%** | `MACRO_BEAR` | `82%` | `+15.9 bps` | Tendência neutra (+0.35% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 03:15:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,976.00 | ⚪ **CASH** | **-0.78%** | `MACRO_BEAR` | `73%` | `+41.4 bps` | Tendência neutra (-0.78% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,664.61 | ⚪ **CASH** | **-1.09%** | `MACRO_BEAR` | `79%` | `+16.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.78 | ⚪ **CASH** | **+0.36%** | `MACRO_BEAR` | `82%` | `+15.9 bps` | Tendência neutra (+0.36% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 03:00:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,968.19 | ⚪ **CASH** | **-0.78%** | `MACRO_BEAR` | `73%` | `+41.4 bps` | Tendência neutra (-0.78% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,664.42 | ⚪ **CASH** | **-1.09%** | `MACRO_BEAR` | `79%` | `+16.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.71 | ⚪ **CASH** | **+0.35%** | `MACRO_BEAR` | `82%` | `+15.9 bps` | Tendência neutra (+0.35% dentro do buffer ±0.80%) |

---

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
