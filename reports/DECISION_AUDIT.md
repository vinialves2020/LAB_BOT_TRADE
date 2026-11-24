# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-24 02:30:48 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-11-23 21:15:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,411.41 | ⚪ **CASH** | **-1.79%** | `MACRO_BEAR` | `77%` | `-34.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,726.92 | ⚪ **CASH** | **-1.70%** | `MACRO_BEAR` | `88%` | `+35.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.80 | ⚪ **CASH** | **-0.67%** | `MACRO_BEAR` | `93%` | `+67.9 bps` | Tendência neutra (-0.67% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 21:00:56 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,357.92 | ⚪ **CASH** | **-1.80%** | `MACRO_BEAR` | `77%` | `-34.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,728.60 | ⚪ **CASH** | **-1.70%** | `MACRO_BEAR` | `88%` | `+35.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.96 | ⚪ **CASH** | **-0.66%** | `MACRO_BEAR` | `93%` | `+67.9 bps` | Tendência neutra (-0.66% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 20:45:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,268.60 | ⚪ **CASH** | **-1.83%** | `MACRO_BEAR` | `78%` | `-42.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,725.93 | ⚪ **CASH** | **-1.73%** | `MACRO_BEAR` | `88%` | `+31.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.90 | ⚪ **CASH** | **-0.71%** | `MACRO_BEAR` | `93%` | `+66.9 bps` | Tendência neutra (-0.71% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 20:30:55 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,276.94 | ⚪ **CASH** | **-1.82%** | `MACRO_BEAR` | `78%` | `-42.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,730.75 | ⚪ **CASH** | **-1.73%** | `MACRO_BEAR` | `88%` | `+31.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $73.16 | ⚪ **CASH** | **-0.70%** | `MACRO_BEAR` | `93%` | `+66.9 bps` | Tendência neutra (-0.70% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 20:15:39 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,389.75 | ⚪ **CASH** | **-1.82%** | `MACRO_BEAR` | `78%` | `-42.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,733.10 | ⚪ **CASH** | **-1.72%** | `MACRO_BEAR` | `88%` | `+31.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $73.23 | ⚪ **CASH** | **-0.70%** | `MACRO_BEAR` | `93%` | `+66.9 bps` | Tendência neutra (-0.70% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 20:00:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,331.52 | ⚪ **CASH** | **-1.82%** | `MACRO_BEAR` | `78%` | `-42.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,733.09 | ⚪ **CASH** | **-1.72%** | `MACRO_BEAR` | `88%` | `+31.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $73.21 | ⚪ **CASH** | **-0.70%** | `MACRO_BEAR` | `93%` | `+66.9 bps` | Tendência neutra (-0.70% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 19:45:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,031.27 | ⚪ **CASH** | **-1.86%** | `MACRO_BEAR` | `78%` | `-54.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,722.22 | ⚪ **CASH** | **-1.78%** | `MACRO_BEAR` | `89%` | `+30.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.59 | ⚪ **CASH** | **-0.78%** | `MACRO_BEAR` | `93%` | `+71.8 bps` | Tendência neutra (-0.78% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 19:30:50 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,424.74 | ⚪ **CASH** | **-1.84%** | `MACRO_BEAR` | `77%` | `-54.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,736.55 | ⚪ **CASH** | **-1.75%** | `MACRO_BEAR` | `88%` | `+30.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $73.00 | ⚪ **CASH** | **-0.77%** | `MACRO_BEAR` | `93%` | `+71.8 bps` | Tendência neutra (-0.77% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 19:15:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,620.60 | ⚪ **CASH** | **-1.83%** | `MACRO_BEAR` | `78%` | `-54.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,743.04 | ⚪ **CASH** | **-1.74%** | `MACRO_BEAR` | `88%` | `+30.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $73.40 | ⚪ **CASH** | **-0.75%** | `MACRO_BEAR` | `93%` | `+71.8 bps` | Tendência neutra (-0.75% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 19:00:54 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,365.37 | ⚪ **CASH** | **-1.85%** | `MACRO_BEAR` | `77%` | `-54.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,739.20 | ⚪ **CASH** | **-1.75%** | `MACRO_BEAR` | `88%` | `+30.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $73.19 | ⚪ **CASH** | **-0.76%** | `MACRO_BEAR` | `93%` | `+71.8 bps` | Tendência neutra (-0.76% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 18:45:45 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,366.09 | ⚪ **CASH** | **-1.88%** | `MACRO_BEAR` | `77%` | `-57.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,738.61 | ⚪ **CASH** | **-1.80%** | `MACRO_BEAR` | `88%` | `+16.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $73.28 | ⚪ **CASH** | **-0.82%** | `MACRO_BEAR` | `93%` | `+77.6 bps` | Tendência neutra (-0.82% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 18:30:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,527.16 | ⚪ **CASH** | **-1.87%** | `MACRO_BEAR` | `77%` | `-57.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,745.52 | ⚪ **CASH** | **-1.79%** | `MACRO_BEAR` | `88%` | `+16.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $73.61 | ⚪ **CASH** | **-0.81%** | `MACRO_BEAR` | `93%` | `+77.6 bps` | Tendência neutra (-0.81% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 18:15:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,503.37 | ⚪ **CASH** | **-1.87%** | `MACRO_BEAR` | `77%` | `-57.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,742.23 | ⚪ **CASH** | **-1.80%** | `MACRO_BEAR` | `88%` | `+16.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $73.47 | ⚪ **CASH** | **-0.81%** | `MACRO_BEAR` | `93%` | `+77.6 bps` | Tendência neutra (-0.81% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 18:00:58 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,633.16 | ⚪ **CASH** | **-1.87%** | `MACRO_BEAR` | `77%` | `-57.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,742.49 | ⚪ **CASH** | **-1.80%** | `MACRO_BEAR` | `88%` | `+16.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $73.58 | ⚪ **CASH** | **-0.81%** | `MACRO_BEAR` | `93%` | `+77.6 bps` | Tendência neutra (-0.81% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 17:45:46 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,402.43 | ⚪ **CASH** | **-1.92%** | `MACRO_BEAR` | `78%` | `-57.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,734.81 | ⚪ **CASH** | **-1.87%** | `MACRO_BEAR` | `89%` | `+8.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $73.44 | ⚪ **CASH** | **-0.90%** | `MACRO_BEAR` | `93%` | `+91.7 bps` | Tendência neutra (-0.90% dentro do buffer ±0.80%) |
