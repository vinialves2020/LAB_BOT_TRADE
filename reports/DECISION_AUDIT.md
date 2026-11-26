# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-26 19:45:43 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-11-26 16:30:41 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,458.01 | ⚪ **CASH** | **-1.32%** | `MACRO_BEAR` | `79%` | `-31.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,685.75 | ⚪ **CASH** | **-1.52%** | `MACRO_BEAR` | `87%` | `+4.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.72 | ⚪ **CASH** | **-1.10%** | `MACRO_BEAR` | `91%` | `+3.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 16:15:40 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,610.53 | ⚪ **CASH** | **-1.31%** | `MACRO_BEAR` | `79%` | `-31.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,689.44 | ⚪ **CASH** | **-1.51%** | `MACRO_BEAR` | `87%` | `+4.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.98 | ⚪ **CASH** | **-1.09%** | `MACRO_BEAR` | `91%` | `+3.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 16:00:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,699.01 | ⚪ **CASH** | **-1.31%** | `MACRO_BEAR` | `79%` | `-31.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,694.41 | ⚪ **CASH** | **-1.51%** | `MACRO_BEAR` | `87%` | `+4.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.10 | ⚪ **CASH** | **-1.09%** | `MACRO_BEAR` | `91%` | `+3.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 15:45:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,412.12 | ⚪ **CASH** | **-1.35%** | `MACRO_BEAR` | `79%` | `-34.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,687.14 | ⚪ **CASH** | **-1.55%** | `MACRO_BEAR` | `87%` | `-9.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.74 | ⚪ **CASH** | **-1.14%** | `MACRO_BEAR` | `91%` | `-35.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 15:30:59 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,322.52 | ⚪ **CASH** | **-1.36%** | `MACRO_BEAR` | `79%` | `-34.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,684.19 | ⚪ **CASH** | **-1.55%** | `MACRO_BEAR` | `87%` | `-9.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.55 | ⚪ **CASH** | **-1.15%** | `MACRO_BEAR` | `91%` | `-35.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 15:15:50 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,205.99 | ⚪ **CASH** | **-1.36%** | `MACRO_BEAR` | `79%` | `-34.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,679.03 | ⚪ **CASH** | **-1.56%** | `MACRO_BEAR` | `87%` | `-9.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.28 | ⚪ **CASH** | **-1.16%** | `MACRO_BEAR` | `91%` | `-35.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 15:00:58 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,668.01 | ⚪ **CASH** | **-1.34%** | `MACRO_BEAR` | `79%` | `-34.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,696.94 | ⚪ **CASH** | **-1.53%** | `MACRO_BEAR` | `87%` | `-9.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.99 | ⚪ **CASH** | **-1.13%** | `MACRO_BEAR` | `91%` | `-35.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 14:45:47 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,787.67 | ⚪ **CASH** | **-1.37%** | `MACRO_BEAR` | `79%` | `-39.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,700.30 | ⚪ **CASH** | **-1.56%** | `MACRO_BEAR` | `87%` | `-11.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.25 | ⚪ **CASH** | **-1.17%** | `MACRO_BEAR` | `92%` | `-36.5 bps` | Tendência neutra (-1.17% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 14:30:42 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,791.25 | ⚪ **CASH** | **-1.37%** | `MACRO_BEAR` | `79%` | `-39.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,702.70 | ⚪ **CASH** | **-1.55%** | `MACRO_BEAR` | `87%` | `-11.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.39 | ⚪ **CASH** | **-1.16%** | `MACRO_BEAR` | `92%` | `-36.5 bps` | Tendência neutra (-1.16% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 14:16:00 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,807.14 | ⚪ **CASH** | **-1.37%** | `MACRO_BEAR` | `79%` | `-39.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,703.31 | ⚪ **CASH** | **-1.55%** | `MACRO_BEAR` | `87%` | `-11.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.40 | ⚪ **CASH** | **-1.16%** | `MACRO_BEAR` | `92%` | `-36.5 bps` | Tendência neutra (-1.16% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 14:00:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,868.71 | ⚪ **CASH** | **-1.37%** | `MACRO_BEAR` | `79%` | `-39.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,703.65 | ⚪ **CASH** | **-1.55%** | `MACRO_BEAR` | `87%` | `-11.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.21 | ⚪ **CASH** | **-1.17%** | `MACRO_BEAR` | `92%` | `-36.5 bps` | Tendência neutra (-1.17% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-26 13:45:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,930.00 | ⚪ **CASH** | **-1.42%** | `MACRO_BEAR` | `79%` | `-37.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,705.18 | ⚪ **CASH** | **-1.60%** | `MACRO_BEAR` | `87%` | `-23.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.08 | ⚪ **CASH** | **-1.23%** | `MACRO_BEAR` | `92%` | `-48.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 13:30:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,854.98 | ⚪ **CASH** | **-1.42%** | `MACRO_BEAR` | `79%` | `-37.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,705.39 | ⚪ **CASH** | **-1.60%** | `MACRO_BEAR` | `87%` | `-23.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.95 | ⚪ **CASH** | **-1.24%** | `MACRO_BEAR` | `92%` | `-48.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 13:15:37 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,840.17 | ⚪ **CASH** | **-1.42%** | `MACRO_BEAR` | `79%` | `-37.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,706.37 | ⚪ **CASH** | **-1.60%** | `MACRO_BEAR` | `87%` | `-23.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.99 | ⚪ **CASH** | **-1.23%** | `MACRO_BEAR` | `92%` | `-48.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 13:00:45 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,829.05 | ⚪ **CASH** | **-1.42%** | `MACRO_BEAR` | `79%` | `-37.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,705.50 | ⚪ **CASH** | **-1.60%** | `MACRO_BEAR` | `87%` | `-23.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.95 | ⚪ **CASH** | **-1.24%** | `MACRO_BEAR` | `92%` | `-48.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 12:45:40 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,943.71 | ⚪ **CASH** | **-1.46%** | `MACRO_BEAR` | `79%` | `-19.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,708.93 | ⚪ **CASH** | **-1.65%** | `MACRO_BEAR` | `88%` | `-31.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.06 | ⚪ **CASH** | **-1.28%** | `MACRO_BEAR` | `92%` | `-76.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 12:30:56 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,619.28 | ⚪ **CASH** | **-1.48%** | `MACRO_BEAR` | `79%` | `-19.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,701.38 | ⚪ **CASH** | **-1.66%** | `MACRO_BEAR` | `87%` | `-31.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.75 | ⚪ **CASH** | **-1.29%** | `MACRO_BEAR` | `92%` | `-76.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 12:15:46 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,648.01 | ⚪ **CASH** | **-1.48%** | `MACRO_BEAR` | `79%` | `-19.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,700.74 | ⚪ **CASH** | **-1.66%** | `MACRO_BEAR` | `87%` | `-31.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.81 | ⚪ **CASH** | **-1.29%** | `MACRO_BEAR` | `92%` | `-76.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 12:00:57 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,708.80 | ⚪ **CASH** | **-1.48%** | `MACRO_BEAR` | `79%` | `-19.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,700.81 | ⚪ **CASH** | **-1.66%** | `MACRO_BEAR` | `87%` | `-31.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.92 | ⚪ **CASH** | **-1.28%** | `MACRO_BEAR` | `92%` | `-76.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 11:45:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,747.95 | ⚪ **CASH** | **-1.52%** | `MACRO_BEAR` | `79%` | `-22.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,700.98 | ⚪ **CASH** | **-1.70%** | `MACRO_BEAR` | `87%` | `-18.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.83 | ⚪ **CASH** | **-1.33%** | `MACRO_BEAR` | `92%` | `-56.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 11:31:02 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,642.38 | ⚪ **CASH** | **-1.52%** | `MACRO_BEAR` | `79%` | `-22.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,699.07 | ⚪ **CASH** | **-1.71%** | `MACRO_BEAR` | `87%` | `-18.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.75 | ⚪ **CASH** | **-1.33%** | `MACRO_BEAR` | `92%` | `-56.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 11:15:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,622.90 | ⚪ **CASH** | **-1.52%** | `MACRO_BEAR` | `79%` | `-22.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,697.03 | ⚪ **CASH** | **-1.71%** | `MACRO_BEAR` | `87%` | `-18.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.61 | ⚪ **CASH** | **-1.34%** | `MACRO_BEAR` | `92%` | `-56.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-26 11:00:55 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,500.00 | ⚪ **CASH** | **-1.53%** | `MACRO_BEAR` | `79%` | `-22.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,693.87 | ⚪ **CASH** | **-1.72%** | `MACRO_BEAR` | `87%` | `-18.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.48 | ⚪ **CASH** | **-1.35%** | `MACRO_BEAR` | `92%` | `-56.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
