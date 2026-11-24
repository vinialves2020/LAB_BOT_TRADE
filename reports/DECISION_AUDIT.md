# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-24 10:30:48 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-24 10:30:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,842.60 | ⚪ **CASH** | **-1.85%** | `MACRO_BEAR` | `78%` | `+53.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,684.48 | ⚪ **CASH** | **-1.85%** | `MACRO_BEAR` | `88%` | `+102.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.62 | ⚪ **CASH** | **-0.76%** | `MACRO_BEAR` | `93%` | `+21.2 bps` | Tendência neutra (-0.76% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 10:15:54 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,021.22 | ⚪ **CASH** | **-1.84%** | `MACRO_BEAR` | `78%` | `+53.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,687.55 | ⚪ **CASH** | **-1.85%** | `MACRO_BEAR` | `88%` | `+102.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.79 | ⚪ **CASH** | **-0.76%** | `MACRO_BEAR` | `93%` | `+21.2 bps` | Tendência neutra (-0.76% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 10:00:57 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,008.01 | ⚪ **CASH** | **-1.84%** | `MACRO_BEAR` | `78%` | `+53.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,684.88 | ⚪ **CASH** | **-1.85%** | `MACRO_BEAR` | `88%` | `+102.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.79 | ⚪ **CASH** | **-0.76%** | `MACRO_BEAR` | `93%` | `+21.2 bps` | Tendência neutra (-0.76% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 09:45:40 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,164.01 | ⚪ **CASH** | **-1.81%** | `MACRO_BEAR` | `78%` | `+54.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,690.33 | ⚪ **CASH** | **-1.82%** | `MACRO_BEAR` | `88%` | `+108.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.94 | ⚪ **CASH** | **-0.72%** | `MACRO_BEAR` | `93%` | `+16.4 bps` | Tendência neutra (-0.72% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 09:30:54 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,998.01 | ⚪ **CASH** | **-1.82%** | `MACRO_BEAR` | `78%` | `+54.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,686.24 | ⚪ **CASH** | **-1.82%** | `MACRO_BEAR` | `88%` | `+108.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.92 | ⚪ **CASH** | **-0.72%** | `MACRO_BEAR` | `93%` | `+16.4 bps` | Tendência neutra (-0.72% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 09:15:46 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $59,906.12 | ⚪ **CASH** | **-1.82%** | `MACRO_BEAR` | `78%` | `+54.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,681.78 | ⚪ **CASH** | **-1.83%** | `MACRO_BEAR` | `88%` | `+108.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.73 | ⚪ **CASH** | **-0.73%** | `MACRO_BEAR` | `93%` | `+16.4 bps` | Tendência neutra (-0.73% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 09:01:00 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,026.88 | ⚪ **CASH** | **-1.82%** | `MACRO_BEAR` | `78%` | `+54.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,685.63 | ⚪ **CASH** | **-1.82%** | `MACRO_BEAR` | `88%` | `+108.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.87 | ⚪ **CASH** | **-0.72%** | `MACRO_BEAR` | `93%` | `+16.4 bps` | Tendência neutra (-0.72% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 08:45:45 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,396.01 | ⚪ **CASH** | **-1.79%** | `MACRO_BEAR` | `78%` | `+65.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,699.23 | ⚪ **CASH** | **-1.79%** | `MACRO_BEAR` | `88%` | `+95.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.47 | ⚪ **CASH** | **-0.68%** | `MACRO_BEAR` | `93%` | `+12.2 bps` | Tendência neutra (-0.68% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 08:30:47 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,158.81 | ⚪ **CASH** | **-1.80%** | `MACRO_BEAR` | `78%` | `+65.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,692.47 | ⚪ **CASH** | **-1.80%** | `MACRO_BEAR` | `88%` | `+95.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.20 | ⚪ **CASH** | **-0.69%** | `MACRO_BEAR` | `93%` | `+12.2 bps` | Tendência neutra (-0.69% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 08:15:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,280.27 | ⚪ **CASH** | **-1.79%** | `MACRO_BEAR` | `78%` | `+65.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,696.37 | ⚪ **CASH** | **-1.79%** | `MACRO_BEAR` | `88%` | `+95.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.45 | ⚪ **CASH** | **-0.68%** | `MACRO_BEAR` | `93%` | `+12.2 bps` | Tendência neutra (-0.68% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 08:00:46 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,385.16 | ⚪ **CASH** | **-1.79%** | `MACRO_BEAR` | `78%` | `+65.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,696.36 | ⚪ **CASH** | **-1.79%** | `MACRO_BEAR` | `88%` | `+95.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.42 | ⚪ **CASH** | **-0.68%** | `MACRO_BEAR` | `93%` | `+12.2 bps` | Tendência neutra (-0.68% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 07:45:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,481.32 | ⚪ **CASH** | **-1.78%** | `MACRO_BEAR` | `78%` | `+38.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,701.03 | ⚪ **CASH** | **-1.78%** | `MACRO_BEAR` | `88%` | `+105.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.61 | ⚪ **CASH** | **-0.67%** | `MACRO_BEAR` | `93%` | `+15.2 bps` | Tendência neutra (-0.67% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 07:30:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,435.26 | ⚪ **CASH** | **-1.78%** | `MACRO_BEAR` | `78%` | `+38.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,696.54 | ⚪ **CASH** | **-1.78%** | `MACRO_BEAR` | `88%` | `+105.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.67 | ⚪ **CASH** | **-0.67%** | `MACRO_BEAR` | `93%` | `+15.2 bps` | Tendência neutra (-0.67% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 07:15:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,474.00 | ⚪ **CASH** | **-1.78%** | `MACRO_BEAR` | `78%` | `+38.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,700.34 | ⚪ **CASH** | **-1.78%** | `MACRO_BEAR` | `88%` | `+105.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.80 | ⚪ **CASH** | **-0.66%** | `MACRO_BEAR` | `93%` | `+15.2 bps` | Tendência neutra (-0.66% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 07:00:45 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,459.84 | ⚪ **CASH** | **-1.78%** | `MACRO_BEAR` | `78%` | `+38.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,700.19 | ⚪ **CASH** | **-1.78%** | `MACRO_BEAR` | `88%` | `+105.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.85 | ⚪ **CASH** | **-0.66%** | `MACRO_BEAR` | `93%` | `+15.2 bps` | Tendência neutra (-0.66% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 06:45:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,418.00 | ⚪ **CASH** | **-1.78%** | `MACRO_BEAR` | `78%` | `+23.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,698.91 | ⚪ **CASH** | **-1.77%** | `MACRO_BEAR` | `89%` | `+36.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.72 | ⚪ **CASH** | **-0.67%** | `MACRO_BEAR` | `93%` | `+34.2 bps` | Tendência neutra (-0.67% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-24 06:30:55 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,479.43 | ⚪ **CASH** | **-1.77%** | `MACRO_BEAR` | `78%` | `+23.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,701.30 | ⚪ **CASH** | **-1.77%** | `MACRO_BEAR` | `89%` | `+36.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.65 | ⚪ **CASH** | **-0.68%** | `MACRO_BEAR` | `93%` | `+34.2 bps` | Tendência neutra (-0.68% dentro do buffer ±0.80%) |

---

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
