# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-23 12:15:47 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-23 12:15:47 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,322.01 | ⚪ **CASH** | **-2.44%** | `MACRO_BEAR` | `72%` | `-39.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,721.82 | ⚪ **CASH** | **-2.49%** | `MACRO_BEAR` | `81%` | `-12.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.41 | ⚪ **CASH** | **-1.79%** | `MACRO_BEAR` | `82%` | `+25.8 bps` | Tendência neutra (-1.79% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 12:00:55 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,376.58 | ⚪ **CASH** | **-2.44%** | `MACRO_BEAR` | `71%` | `-39.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,723.95 | ⚪ **CASH** | **-2.49%** | `MACRO_BEAR` | `81%` | `-12.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.46 | ⚪ **CASH** | **-1.79%** | `MACRO_BEAR` | `82%` | `+25.8 bps` | Tendência neutra (-1.79% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 11:45:38 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,516.99 | ⚪ **CASH** | **-2.50%** | `MACRO_BEAR` | `72%` | `-36.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,727.58 | ⚪ **CASH** | **-2.54%** | `MACRO_BEAR` | `81%` | `-6.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.79 | ⚪ **CASH** | **-1.87%** | `MACRO_BEAR` | `82%` | `+21.9 bps` | Tendência neutra (-1.87% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 11:30:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,450.87 | ⚪ **CASH** | **-2.50%** | `MACRO_BEAR` | `72%` | `-36.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,727.59 | ⚪ **CASH** | **-2.54%** | `MACRO_BEAR` | `81%` | `-6.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.63 | ⚪ **CASH** | **-1.88%** | `MACRO_BEAR` | `82%` | `+21.9 bps` | Tendência neutra (-1.88% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 11:15:54 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,349.38 | ⚪ **CASH** | **-2.50%** | `MACRO_BEAR` | `72%` | `-36.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,723.14 | ⚪ **CASH** | **-2.55%** | `MACRO_BEAR` | `81%` | `-6.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.34 | ⚪ **CASH** | **-1.89%** | `MACRO_BEAR` | `82%` | `+21.9 bps` | Tendência neutra (-1.89% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 11:01:01 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,445.01 | ⚪ **CASH** | **-2.50%** | `MACRO_BEAR` | `72%` | `-36.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,725.72 | ⚪ **CASH** | **-2.55%** | `MACRO_BEAR` | `81%` | `-6.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.33 | ⚪ **CASH** | **-1.89%** | `MACRO_BEAR` | `82%` | `+21.9 bps` | Tendência neutra (-1.89% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 10:45:40 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,335.04 | ⚪ **CASH** | **-2.57%** | `MACRO_BEAR` | `72%` | `-43.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,722.23 | ⚪ **CASH** | **-2.61%** | `MACRO_BEAR` | `81%` | `-6.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.32 | ⚪ **CASH** | **-1.97%** | `MACRO_BEAR` | `82%` | `+25.5 bps` | Tendência neutra (-1.97% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 10:30:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,408.00 | ⚪ **CASH** | **-2.56%** | `MACRO_BEAR` | `72%` | `-43.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,723.86 | ⚪ **CASH** | **-2.61%** | `MACRO_BEAR` | `81%` | `-6.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.30 | ⚪ **CASH** | **-1.97%** | `MACRO_BEAR` | `82%` | `+25.5 bps` | Tendência neutra (-1.97% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 10:15:47 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,398.01 | ⚪ **CASH** | **-2.56%** | `MACRO_BEAR` | `72%` | `-43.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,723.21 | ⚪ **CASH** | **-2.61%** | `MACRO_BEAR` | `81%` | `-6.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.27 | ⚪ **CASH** | **-1.98%** | `MACRO_BEAR` | `82%` | `+25.5 bps` | Tendência neutra (-1.98% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 10:00:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,472.00 | ⚪ **CASH** | **-2.56%** | `MACRO_BEAR` | `72%` | `-43.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,724.12 | ⚪ **CASH** | **-2.61%** | `MACRO_BEAR` | `81%` | `-6.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.50 | ⚪ **CASH** | **-1.97%** | `MACRO_BEAR` | `82%` | `+25.5 bps` | Tendência neutra (-1.97% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 09:45:41 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,469.06 | ⚪ **CASH** | **-2.62%** | `MACRO_BEAR` | `72%` | `-53.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,723.29 | ⚪ **CASH** | **-2.67%** | `MACRO_BEAR` | `81%` | `-15.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.26 | ⚪ **CASH** | **-2.07%** | `MACRO_BEAR` | `82%` | `+28.9 bps` | Tendência neutra (-2.07% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 09:30:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,694.70 | ⚪ **CASH** | **-2.61%** | `MACRO_BEAR` | `72%` | `-53.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,730.29 | ⚪ **CASH** | **-2.66%** | `MACRO_BEAR` | `81%` | `-15.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.69 | ⚪ **CASH** | **-2.06%** | `MACRO_BEAR` | `82%` | `+28.9 bps` | Tendência neutra (-2.06% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 09:15:43 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,706.46 | ⚪ **CASH** | **-2.61%** | `MACRO_BEAR` | `72%` | `-53.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,731.12 | ⚪ **CASH** | **-2.66%** | `MACRO_BEAR` | `81%` | `-15.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.54 | ⚪ **CASH** | **-2.06%** | `MACRO_BEAR` | `82%` | `+28.9 bps` | Tendência neutra (-2.06% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 09:00:56 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,452.97 | ⚪ **CASH** | **-2.63%** | `MACRO_BEAR` | `72%` | `-53.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,723.47 | ⚪ **CASH** | **-2.67%** | `MACRO_BEAR` | `81%` | `-15.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.35 | ⚪ **CASH** | **-2.07%** | `MACRO_BEAR` | `82%` | `+28.9 bps` | Tendência neutra (-2.07% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 08:45:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,563.08 | ⚪ **CASH** | **-2.69%** | `MACRO_BEAR` | `72%` | `-52.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,725.75 | ⚪ **CASH** | **-2.73%** | `MACRO_BEAR` | `81%` | `-39.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.55 | ⚪ **CASH** | **-2.16%** | `MACRO_BEAR` | `82%` | `+17.6 bps` | Tendência neutra (-2.16% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 08:30:58 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,328.78 | ⚪ **CASH** | **-2.70%** | `MACRO_BEAR` | `72%` | `-52.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,721.96 | ⚪ **CASH** | **-2.74%** | `MACRO_BEAR` | `81%` | `-39.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.28 | ⚪ **CASH** | **-2.17%** | `MACRO_BEAR` | `82%` | `+17.6 bps` | Tendência neutra (-2.17% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 08:15:39 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,164.00 | ⚪ **CASH** | **-2.71%** | `MACRO_BEAR` | `72%` | `-52.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,716.61 | ⚪ **CASH** | **-2.75%** | `MACRO_BEAR` | `81%` | `-39.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.98 | ⚪ **CASH** | **-2.18%** | `MACRO_BEAR` | `82%` | `+17.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-23 08:00:58 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,474.13 | ⚪ **CASH** | **-2.70%** | `MACRO_BEAR` | `72%` | `-52.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,723.90 | ⚪ **CASH** | **-2.74%** | `MACRO_BEAR` | `81%` | `-39.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.10 | ⚪ **CASH** | **-2.18%** | `MACRO_BEAR` | `82%` | `+17.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-23 07:45:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,485.59 | ⚪ **CASH** | **-2.76%** | `MACRO_BEAR` | `72%` | `-51.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,722.17 | ⚪ **CASH** | **-2.80%** | `MACRO_BEAR` | `81%` | `-39.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.09 | ⚪ **CASH** | **-2.27%** | `MACRO_BEAR` | `82%` | `+27.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-23 07:30:46 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,499.27 | ⚪ **CASH** | **-2.76%** | `MACRO_BEAR` | `72%` | `-51.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,726.01 | ⚪ **CASH** | **-2.80%** | `MACRO_BEAR` | `81%` | `-39.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.09 | ⚪ **CASH** | **-2.27%** | `MACRO_BEAR` | `82%` | `+27.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-23 07:15:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,502.31 | ⚪ **CASH** | **-2.76%** | `MACRO_BEAR` | `72%` | `-51.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,726.37 | ⚪ **CASH** | **-2.80%** | `MACRO_BEAR` | `81%` | `-39.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.20 | ⚪ **CASH** | **-2.26%** | `MACRO_BEAR` | `82%` | `+27.9 bps` | Tendência neutra (-2.26% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 07:01:01 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,485.37 | ⚪ **CASH** | **-2.77%** | `MACRO_BEAR` | `72%` | `-51.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,724.44 | ⚪ **CASH** | **-2.80%** | `MACRO_BEAR` | `81%` | `-39.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.04 | ⚪ **CASH** | **-2.27%** | `MACRO_BEAR` | `82%` | `+27.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-23 06:45:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,556.84 | ⚪ **CASH** | **-2.84%** | `MACRO_BEAR` | `72%` | `-56.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,725.45 | ⚪ **CASH** | **-2.87%** | `MACRO_BEAR` | `81%` | `-46.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.92 | ⚪ **CASH** | **-2.36%** | `MACRO_BEAR` | `82%` | `+48.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-23 06:30:45 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,570.96 | ⚪ **CASH** | **-2.83%** | `MACRO_BEAR` | `72%` | `-56.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,724.21 | ⚪ **CASH** | **-2.87%** | `MACRO_BEAR` | `81%` | `-46.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.77 | ⚪ **CASH** | **-2.37%** | `MACRO_BEAR` | `82%` | `+48.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-23 06:15:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,785.99 | ⚪ **CASH** | **-2.82%** | `MACRO_BEAR` | `72%` | `-56.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,730.38 | ⚪ **CASH** | **-2.86%** | `MACRO_BEAR` | `81%` | `-46.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.01 | ⚪ **CASH** | **-2.36%** | `MACRO_BEAR` | `82%` | `+48.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-23 06:00:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,773.00 | ⚪ **CASH** | **-2.82%** | `MACRO_BEAR` | `72%` | `-56.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,735.02 | ⚪ **CASH** | **-2.85%** | `MACRO_BEAR` | `81%` | `-46.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.00 | ⚪ **CASH** | **-2.36%** | `MACRO_BEAR` | `82%` | `+48.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-23 05:45:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,787.59 | ⚪ **CASH** | **-2.91%** | `MACRO_BEAR` | `72%` | `-52.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,737.42 | ⚪ **CASH** | **-2.93%** | `MACRO_BEAR` | `81%` | `-37.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $72.20 | ⚪ **CASH** | **-2.44%** | `MACRO_BEAR` | `83%` | `+24.9 bps` | Tendência neutra (-2.44% dentro do buffer ±0.80%) |

---

### 🕒 Ciclo `2026-11-23 05:30:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,500.55 | ⚪ **CASH** | **-2.92%** | `MACRO_BEAR` | `72%` | `-52.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,732.09 | ⚪ **CASH** | **-2.94%** | `MACRO_BEAR` | `81%` | `-37.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.66 | ⚪ **CASH** | **-2.46%** | `MACRO_BEAR` | `82%` | `+24.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-23 05:15:41 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,248.00 | ⚪ **CASH** | **-2.94%** | `MACRO_BEAR` | `72%` | `-52.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,726.92 | ⚪ **CASH** | **-2.95%** | `MACRO_BEAR` | `81%` | `-37.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.45 | ⚪ **CASH** | **-2.47%** | `MACRO_BEAR` | `82%` | `+24.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-23 05:00:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,252.01 | ⚪ **CASH** | **-2.94%** | `MACRO_BEAR` | `72%` | `-52.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,727.53 | ⚪ **CASH** | **-2.95%** | `MACRO_BEAR` | `81%` | `-37.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.34 | ⚪ **CASH** | **-2.47%** | `MACRO_BEAR` | `82%` | `+24.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-23 04:45:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,173.50 | ⚪ **CASH** | **-3.01%** | `MACRO_BEAR` | `72%` | `-58.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,727.36 | ⚪ **CASH** | **-3.02%** | `MACRO_BEAR` | `81%` | `-46.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.37 | ⚪ **CASH** | **-2.54%** | `MACRO_BEAR` | `82%` | `+22.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-23 04:30:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,128.05 | ⚪ **CASH** | **-3.01%** | `MACRO_BEAR` | `72%` | `-58.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,726.38 | ⚪ **CASH** | **-3.03%** | `MACRO_BEAR` | `81%` | `-46.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.30 | ⚪ **CASH** | **-2.55%** | `MACRO_BEAR` | `82%` | `+22.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-23 04:15:50 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,358.25 | ⚪ **CASH** | **-3.00%** | `MACRO_BEAR` | `72%` | `-58.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,732.98 | ⚪ **CASH** | **-3.02%** | `MACRO_BEAR` | `81%` | `-46.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.32 | ⚪ **CASH** | **-2.55%** | `MACRO_BEAR` | `82%` | `+22.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-23 04:00:58 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,212.01 | ⚪ **CASH** | **-3.01%** | `MACRO_BEAR` | `72%` | `-58.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,730.29 | ⚪ **CASH** | **-3.02%** | `MACRO_BEAR` | `81%` | `-46.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.31 | ⚪ **CASH** | **-2.55%** | `MACRO_BEAR` | `82%` | `+22.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-23 03:45:50 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,235.34 | ⚪ **CASH** | **-3.08%** | `MACRO_BEAR` | `72%` | `-30.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,731.12 | ⚪ **CASH** | **-3.11%** | `MACRO_BEAR` | `81%` | `-2.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.25 | ⚪ **CASH** | **-2.62%** | `MACRO_BEAR` | `82%` | `-0.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-23 03:30:54 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,400.24 | ⚪ **CASH** | **-3.07%** | `MACRO_BEAR` | `72%` | `-30.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,729.62 | ⚪ **CASH** | **-3.11%** | `MACRO_BEAR` | `81%` | `-2.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $71.30 | ⚪ **CASH** | **-2.62%** | `MACRO_BEAR` | `82%` | `-0.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
