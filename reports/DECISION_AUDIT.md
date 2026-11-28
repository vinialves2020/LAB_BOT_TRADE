# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-28 16:00:56 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-28 16:00:56 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,495.85 | ⚪ **CASH** | **-1.10%** | `MACRO_BEAR` | `62%` | `+11.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,650.67 | ⚪ **CASH** | **-1.55%** | `MACRO_BEAR` | `67%` | `-14.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.68 | ⚪ **CASH** | **-0.01%** | `MACRO_BEAR` | `73%` | `+31.2 bps` | Tendência neutra (-0.01% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 15:45:46 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,378.55 | ⚪ **CASH** | **-1.10%** | `MACRO_BEAR` | `62%` | `+5.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,648.46 | ⚪ **CASH** | **-1.53%** | `MACRO_BEAR` | `67%` | `-3.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.58 | ⚪ **CASH** | **+0.01%** | `MACRO_BEAR` | `73%` | `+31.6 bps` | Tendência neutra (+0.01% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 15:30:56 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,282.93 | ⚪ **CASH** | **-1.10%** | `MACRO_BEAR` | `62%` | `+5.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,646.34 | ⚪ **CASH** | **-1.53%** | `MACRO_BEAR` | `67%` | `-3.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.55 | ⚪ **CASH** | **+0.01%** | `MACRO_BEAR` | `73%` | `+31.6 bps` | Tendência neutra (+0.01% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 15:15:43 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,397.46 | ⚪ **CASH** | **-1.09%** | `MACRO_BEAR` | `62%` | `+5.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,650.61 | ⚪ **CASH** | **-1.53%** | `MACRO_BEAR` | `67%` | `-3.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.73 | ⚪ **CASH** | **+0.02%** | `MACRO_BEAR` | `73%` | `+31.6 bps` | Tendência neutra (+0.02% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 15:00:56 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,324.03 | ⚪ **CASH** | **-1.10%** | `MACRO_BEAR` | `62%` | `+5.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,647.91 | ⚪ **CASH** | **-1.53%** | `MACRO_BEAR` | `67%` | `-3.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.56 | ⚪ **CASH** | **+0.01%** | `MACRO_BEAR` | `73%` | `+31.6 bps` | Tendência neutra (+0.01% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 14:45:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,250.58 | ⚪ **CASH** | **-1.08%** | `MACRO_BEAR` | `62%` | `+16.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,645.30 | ⚪ **CASH** | **-1.51%** | `MACRO_BEAR` | `67%` | `-22.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.54 | ⚪ **CASH** | **+0.04%** | `MACRO_BEAR` | `73%` | `+38.8 bps` | Tendência neutra (+0.04% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 14:30:47 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,302.66 | ⚪ **CASH** | **-1.08%** | `MACRO_BEAR` | `62%` | `+16.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,647.31 | ⚪ **CASH** | **-1.50%** | `MACRO_BEAR` | `67%` | `-22.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.60 | ⚪ **CASH** | **+0.05%** | `MACRO_BEAR` | `73%` | `+38.8 bps` | Tendência neutra (+0.05% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 14:15:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,184.31 | ⚪ **CASH** | **-1.08%** | `MACRO_BEAR` | `62%` | `+16.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,644.40 | ⚪ **CASH** | **-1.51%** | `MACRO_BEAR` | `67%` | `-22.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.43 | ⚪ **CASH** | **+0.04%** | `MACRO_BEAR` | `73%` | `+38.8 bps` | Tendência neutra (+0.04% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 14:00:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,146.32 | ⚪ **CASH** | **-1.08%** | `MACRO_BEAR` | `62%` | `+16.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,642.91 | ⚪ **CASH** | **-1.51%** | `MACRO_BEAR` | `67%` | `-22.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.30 | ⚪ **CASH** | **+0.04%** | `MACRO_BEAR` | `73%` | `+38.8 bps` | Tendência neutra (+0.04% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 13:45:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,041.80 | ⚪ **CASH** | **-1.05%** | `MACRO_BEAR` | `62%` | `+23.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,639.31 | ⚪ **CASH** | **-1.47%** | `MACRO_BEAR` | `67%` | `-10.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.27 | ⚪ **CASH** | **+0.08%** | `MACRO_BEAR` | `73%` | `+13.6 bps` | Tendência neutra (+0.08% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 13:30:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,275.14 | ⚪ **CASH** | **-1.04%** | `MACRO_BEAR` | `62%` | `+23.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,647.11 | ⚪ **CASH** | **-1.46%** | `MACRO_BEAR` | `67%` | `-10.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.75 | ⚪ **CASH** | **+0.10%** | `MACRO_BEAR` | `72%` | `+13.6 bps` | Tendência neutra (+0.10% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 13:15:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,209.59 | ⚪ **CASH** | **-1.04%** | `MACRO_BEAR` | `62%` | `+23.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,647.60 | ⚪ **CASH** | **-1.46%** | `MACRO_BEAR` | `67%` | `-10.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.73 | ⚪ **CASH** | **+0.10%** | `MACRO_BEAR` | `72%` | `+13.6 bps` | Tendência neutra (+0.10% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 13:00:54 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,209.91 | ⚪ **CASH** | **-1.04%** | `MACRO_BEAR` | `62%` | `+23.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,647.32 | ⚪ **CASH** | **-1.46%** | `MACRO_BEAR` | `67%` | `-10.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.85 | ⚪ **CASH** | **+0.11%** | `MACRO_BEAR` | `72%` | `+13.6 bps` | Tendência neutra (+0.11% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 12:45:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,218.72 | ⚪ **CASH** | **-1.01%** | `MACRO_BEAR` | `65%` | `+20.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,648.42 | ⚪ **CASH** | **-1.42%** | `MACRO_BEAR` | `69%` | `-17.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.81 | ⚪ **CASH** | **+0.13%** | `MACRO_BEAR` | `74%` | `+1.6 bps` | Tendência neutra (+0.13% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 12:30:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,314.90 | ⚪ **CASH** | **-1.00%** | `MACRO_BEAR` | `65%` | `+20.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,651.52 | ⚪ **CASH** | **-1.42%** | `MACRO_BEAR` | `69%` | `-17.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.94 | ⚪ **CASH** | **+0.14%** | `MACRO_BEAR` | `74%` | `+1.6 bps` | Tendência neutra (+0.14% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 12:15:47 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,298.27 | ⚪ **CASH** | **-1.01%** | `MACRO_BEAR` | `65%` | `+20.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,650.30 | ⚪ **CASH** | **-1.42%** | `MACRO_BEAR` | `69%` | `-17.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.98 | ⚪ **CASH** | **+0.14%** | `MACRO_BEAR` | `74%` | `+1.6 bps` | Tendência neutra (+0.14% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 12:01:02 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,365.87 | ⚪ **CASH** | **-1.00%** | `MACRO_BEAR` | `65%` | `+20.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,652.64 | ⚪ **CASH** | **-1.41%** | `MACRO_BEAR` | `69%` | `-17.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.14 | ⚪ **CASH** | **+0.15%** | `MACRO_BEAR` | `74%` | `+1.6 bps` | Tendência neutra (+0.15% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 11:45:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,204.73 | ⚪ **CASH** | **-0.98%** | `MACRO_BEAR` | `66%` | `+24.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,647.48 | ⚪ **CASH** | **-1.39%** | `MACRO_BEAR` | `69%` | `-28.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.92 | ⚪ **CASH** | **+0.16%** | `MACRO_BEAR` | `74%` | `+9.2 bps` | Tendência neutra (+0.16% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 11:30:42 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,245.55 | ⚪ **CASH** | **-0.97%** | `MACRO_BEAR` | `66%` | `+24.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,646.89 | ⚪ **CASH** | **-1.39%** | `MACRO_BEAR` | `69%` | `-28.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.80 | ⚪ **CASH** | **+0.16%** | `MACRO_BEAR` | `74%` | `+9.2 bps` | Tendência neutra (+0.16% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 11:15:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,256.56 | ⚪ **CASH** | **-0.97%** | `MACRO_BEAR` | `66%` | `+24.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,647.66 | ⚪ **CASH** | **-1.39%** | `MACRO_BEAR` | `69%` | `-28.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.78 | ⚪ **CASH** | **+0.16%** | `MACRO_BEAR` | `74%` | `+9.2 bps` | Tendência neutra (+0.16% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 11:00:45 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,239.88 | ⚪ **CASH** | **-0.97%** | `MACRO_BEAR` | `66%` | `+24.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,645.43 | ⚪ **CASH** | **-1.39%** | `MACRO_BEAR` | `69%` | `-28.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.73 | ⚪ **CASH** | **+0.16%** | `MACRO_BEAR` | `74%` | `+9.2 bps` | Tendência neutra (+0.16% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 10:45:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,215.69 | ⚪ **CASH** | **-0.94%** | `MACRO_BEAR` | `66%` | `+15.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,649.09 | ⚪ **CASH** | **-1.34%** | `MACRO_BEAR` | `70%` | `-18.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.77 | ⚪ **CASH** | **+0.19%** | `MACRO_BEAR` | `75%` | `-4.6 bps` | Tendência neutra (+0.19% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 10:30:57 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,351.15 | ⚪ **CASH** | **-0.93%** | `MACRO_BEAR` | `66%` | `+15.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,653.40 | ⚪ **CASH** | **-1.34%** | `MACRO_BEAR` | `70%` | `-18.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.03 | ⚪ **CASH** | **+0.20%** | `MACRO_BEAR` | `74%` | `-4.6 bps` | Tendência neutra (+0.20% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 10:15:43 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,448.37 | ⚪ **CASH** | **-0.93%** | `MACRO_BEAR` | `66%` | `+15.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,652.51 | ⚪ **CASH** | **-1.34%** | `MACRO_BEAR` | `70%` | `-18.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.06 | ⚪ **CASH** | **+0.21%** | `MACRO_BEAR` | `74%` | `-4.6 bps` | Tendência neutra (+0.21% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 10:00:54 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,540.03 | ⚪ **CASH** | **-0.92%** | `MACRO_BEAR` | `66%` | `+15.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,652.19 | ⚪ **CASH** | **-1.34%** | `MACRO_BEAR` | `70%` | `-18.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.04 | ⚪ **CASH** | **+0.20%** | `MACRO_BEAR` | `74%` | `-4.6 bps` | Tendência neutra (+0.20% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 09:45:45 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,537.73 | ⚪ **CASH** | **-0.90%** | `MACRO_BEAR` | `66%` | `+22.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,649.53 | ⚪ **CASH** | **-1.31%** | `MACRO_BEAR` | `70%` | `-18.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.87 | ⚪ **CASH** | **+0.22%** | `MACRO_BEAR` | `74%` | `-0.2 bps` | Tendência neutra (+0.22% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-28 09:30:56 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,664.32 | ⚪ **CASH** | **-0.89%** | `MACRO_BEAR` | `66%` | `+22.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,652.76 | ⚪ **CASH** | **-1.31%** | `MACRO_BEAR` | `70%` | `-18.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.07 | ⚪ **CASH** | **+0.23%** | `MACRO_BEAR` | `74%` | `-0.2 bps` | Tendência neutra (+0.23% dentro do buffer ±0.80%) |

---

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
