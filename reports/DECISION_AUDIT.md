# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-23 23:45:50 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-11-23 17:30:57 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,722.14 | ⚪ **CASH** | **-1.91%** | `MACRO_BEAR` | `77%` | `-57.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,756.47 | ⚪ **CASH** | **-1.83%** | `MACRO_BEAR` | `88%` | `+8.8 bps` | Tendência neutra (-1.83% dentro do buffer ±0.80%) |
| **SOLUSDT** | $73.89 | ⚪ **CASH** | **-0.89%** | `MACRO_BEAR` | `92%` | `+91.7 bps` | Tendência neutra (-0.89% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 17:15:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $62,041.62 | ⚪ **CASH** | **-1.89%** | `MACRO_BEAR` | `77%` | `-57.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,767.37 | ⚪ **CASH** | **-1.81%** | `MACRO_BEAR` | `88%` | `+8.8 bps` | Tendência neutra (-1.81% dentro do buffer ±0.80%) |
| **SOLUSDT** | $74.64 | ⚪ **CASH** | **-0.86%** | `MACRO_BEAR` | `92%` | `+91.7 bps` | Tendência neutra (-0.86% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 17:01:04 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $62,159.55 | ⚪ **CASH** | **-1.89%** | `MACRO_BEAR` | `77%` | `-57.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,766.65 | ⚪ **CASH** | **-1.82%** | `MACRO_BEAR` | `88%` | `+8.8 bps` | Tendência neutra (-1.82% dentro do buffer ±0.80%) |
| **SOLUSDT** | $74.50 | ⚪ **CASH** | **-0.86%** | `MACRO_BEAR` | `92%` | `+91.7 bps` | Tendência neutra (-0.86% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 16:45:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $62,122.10 | ⚪ **CASH** | **-1.97%** | `MACRO_BEAR` | `77%` | `-71.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,761.24 | ⚪ **CASH** | **-1.93%** | `MACRO_BEAR` | `88%` | `-11.3 bps` | Tendência neutra (-1.93% dentro do buffer ±0.80%) |
| **SOLUSDT** | $74.20 | ⚪ **CASH** | **-1.01%** | `MACRO_BEAR` | `93%` | `+100.7 bps` | Tendência neutra (-1.01% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 16:30:55 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $62,760.43 | ⚪ **CASH** | **-1.94%** | `MACRO_BEAR` | `77%` | `-71.3 bps` | Tendência neutra (-1.94% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,776.38 | ⚪ **CASH** | **-1.91%** | `MACRO_BEAR` | `88%` | `-11.3 bps` | Tendência neutra (-1.91% dentro do buffer ±0.80%) |
| **SOLUSDT** | $75.31 | ⚪ **CASH** | **-0.96%** | `MACRO_BEAR` | `92%` | `+100.7 bps` | Tendência neutra (-0.96% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 16:15:46 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $62,724.28 | ⚪ **CASH** | **-1.94%** | `MACRO_BEAR` | `77%` | `-71.3 bps` | Tendência neutra (-1.94% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,769.17 | ⚪ **CASH** | **-1.92%** | `MACRO_BEAR` | `88%` | `-11.3 bps` | Tendência neutra (-1.92% dentro do buffer ±0.80%) |
| **SOLUSDT** | $75.12 | ⚪ **CASH** | **-0.97%** | `MACRO_BEAR` | `92%` | `+100.7 bps` | Tendência neutra (-0.97% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 16:01:00 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $62,906.88 | ⚪ **CASH** | **-1.93%** | `MACRO_BEAR` | `77%` | `-71.3 bps` | Tendência neutra (-1.93% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,774.39 | ⚪ **CASH** | **-1.91%** | `MACRO_BEAR` | `88%` | `-11.3 bps` | Tendência neutra (-1.91% dentro do buffer ±0.80%) |
| **SOLUSDT** | $75.80 | ⚪ **CASH** | **-0.94%** | `MACRO_BEAR` | `92%` | `+100.7 bps` | Tendência neutra (-0.94% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 15:45:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $62,854.06 | ⚪ **CASH** | **-2.04%** | `MACRO_BEAR` | `77%` | `-52.2 bps` | Tendência neutra (-2.04% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,773.19 | ⚪ **CASH** | **-2.03%** | `MACRO_BEAR` | `88%` | `+2.9 bps` | Tendência neutra (-2.03% dentro do buffer ±0.80%) |
| **SOLUSDT** | $75.48 | ⚪ **CASH** | **-1.13%** | `MACRO_BEAR` | `92%` | `+83.0 bps` | Tendência neutra (-1.13% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 15:30:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $63,434.76 | ⚪ **CASH** | **-2.01%** | `MACRO_BEAR` | `77%` | `-52.2 bps` | Tendência neutra (-2.01% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,790.23 | ⚪ **CASH** | **-2.00%** | `MACRO_BEAR` | `88%` | `+2.9 bps` | Tendência neutra (-2.00% dentro do buffer ±0.80%) |
| **SOLUSDT** | $76.49 | ⚪ **CASH** | **-1.09%** | `MACRO_BEAR` | `91%` | `+83.0 bps` | Tendência neutra (-1.09% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 15:15:41 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $63,057.70 | ⚪ **CASH** | **-2.03%** | `MACRO_BEAR` | `77%` | `-52.2 bps` | Tendência neutra (-2.03% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,781.07 | ⚪ **CASH** | **-2.02%** | `MACRO_BEAR` | `88%` | `+2.9 bps` | Tendência neutra (-2.02% dentro do buffer ±0.80%) |
| **SOLUSDT** | $75.98 | ⚪ **CASH** | **-1.11%** | `MACRO_BEAR` | `92%` | `+83.0 bps` | Tendência neutra (-1.11% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 15:00:58 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $62,987.03 | ⚪ **CASH** | **-2.04%** | `MACRO_BEAR` | `77%` | `-52.2 bps` | Tendência neutra (-2.04% dentro do buffer ±0.80%) |
| **ETHUSDT** | $1,780.23 | ⚪ **CASH** | **-2.02%** | `MACRO_BEAR` | `88%` | `+2.9 bps` | Tendência neutra (-2.02% dentro do buffer ±0.80%) |
| **SOLUSDT** | $76.61 | ⚪ **CASH** | **-1.09%** | `MACRO_BEAR` | `91%` | `+83.0 bps` | Tendência neutra (-1.09% dentro do buffer ±0.80%) |
