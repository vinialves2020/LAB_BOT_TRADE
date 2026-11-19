# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-19 05:30:46 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-19 05:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,450.93 | ⚪ **CASH** | **+36.3 bps** (±16.9) | `+66.6 bps` | `+0.010 / +0.014` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,799.63 | ⚪ **CASH** | **+5.2 bps** (±4.6) | `+10.0 bps` | `-0.024 / +0.034` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 35.7 bps) |
| **SOLUSDT** | $74.58 | ⚪ **CASH** | **+23.3 bps** (±11.7) | `+30.5 bps` | `+0.044 / +0.140` | `0.72%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 05:15:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,442.26 | ⚪ **CASH** | **+36.3 bps** (±16.9) | `+66.6 bps` | `+0.010 / +0.014` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,797.29 | ⚪ **CASH** | **+5.2 bps** (±4.6) | `+10.0 bps` | `-0.024 / +0.034` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 35.7 bps) |
| **SOLUSDT** | $74.50 | ⚪ **CASH** | **+23.3 bps** (±11.7) | `+30.5 bps` | `+0.044 / +0.140` | `0.72%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 05:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,531.03 | ⚪ **CASH** | **+36.3 bps** (±16.9) | `+66.6 bps` | `+0.010 / +0.014` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,798.55 | ⚪ **CASH** | **+5.2 bps** (±4.6) | `+10.0 bps` | `-0.024 / +0.034` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 35.7 bps) |
| **SOLUSDT** | $74.53 | ⚪ **CASH** | **+23.3 bps** (±11.7) | `+30.5 bps` | `+0.044 / +0.140` | `0.72%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 04:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,563.69 | ⚪ **CASH** | **+35.0 bps** (±15.8) | `+64.3 bps` | `+0.014 / +0.002` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,802.05 | ⚪ **CASH** | **+11.8 bps** (±6.7) | `+22.9 bps` | `-0.029 / +0.031` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.7 bps) |
| **SOLUSDT** | $74.70 | ⚪ **CASH** | **+12.9 bps** (±5.1) | `+15.2 bps` | `+0.025 / +0.091` | `0.73%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 04:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,370.74 | ⚪ **CASH** | **+35.0 bps** (±15.8) | `+64.3 bps` | `+0.014 / +0.002` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,796.99 | ⚪ **CASH** | **+11.8 bps** (±6.7) | `+22.9 bps` | `-0.029 / +0.031` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.7 bps) |
| **SOLUSDT** | $74.54 | ⚪ **CASH** | **+12.9 bps** (±5.1) | `+15.2 bps` | `+0.025 / +0.091` | `0.73%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 04:15:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,292.03 | ⚪ **CASH** | **+35.0 bps** (±15.8) | `+64.3 bps` | `+0.014 / +0.002` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,796.78 | ⚪ **CASH** | **+11.8 bps** (±6.7) | `+22.9 bps` | `-0.029 / +0.031` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.7 bps) |
| **SOLUSDT** | $74.27 | ⚪ **CASH** | **+12.9 bps** (±5.1) | `+15.2 bps` | `+0.025 / +0.091` | `0.73%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 04:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,274.51 | ⚪ **CASH** | **+35.0 bps** (±15.8) | `+64.3 bps` | `+0.014 / +0.002` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,797.52 | ⚪ **CASH** | **+11.8 bps** (±6.7) | `+22.9 bps` | `-0.029 / +0.031` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.7 bps) |
| **SOLUSDT** | $74.33 | ⚪ **CASH** | **+12.9 bps** (±5.1) | `+15.2 bps` | `+0.025 / +0.091` | `0.73%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 03:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,044.01 | ⚪ **CASH** | **+38.3 bps** (±12.1) | `+72.4 bps` | `+0.006 / -0.024` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,782.59 | ⚪ **CASH** | **+46.1 bps** (±11.1) | `+88.5 bps` | `-0.036 / +0.010` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $73.90 | ⚪ **CASH** | **+13.2 bps** (±6.5) | `+19.2 bps` | `+0.012 / +0.069` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-19 03:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,964.01 | ⚪ **CASH** | **+38.3 bps** (±12.1) | `+72.4 bps` | `+0.006 / -0.024` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,779.99 | ⚪ **CASH** | **+46.1 bps** (±11.1) | `+88.5 bps` | `-0.036 / +0.010` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $73.62 | ⚪ **CASH** | **+13.2 bps** (±6.5) | `+19.2 bps` | `+0.012 / +0.069` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-19 03:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,456.66 | ⚪ **CASH** | **+38.3 bps** (±12.1) | `+72.4 bps` | `+0.006 / -0.024` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,766.26 | ⚪ **CASH** | **+46.1 bps** (±11.1) | `+88.5 bps` | `-0.036 / +0.010` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $72.99 | ⚪ **CASH** | **+13.2 bps** (±6.5) | `+19.2 bps` | `+0.012 / +0.069` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-19 03:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,572.00 | ⚪ **CASH** | **+38.3 bps** (±12.1) | `+72.4 bps` | `+0.006 / -0.024` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,768.85 | ⚪ **CASH** | **+46.1 bps** (±11.1) | `+88.5 bps` | `-0.036 / +0.010` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $73.09 | ⚪ **CASH** | **+13.2 bps** (±6.5) | `+19.2 bps` | `+0.012 / +0.069` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-19 02:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,659.94 | ⚪ **CASH** | **+38.3 bps** (±9.8) | `+71.6 bps` | `+0.005 / -0.014` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,770.66 | ⚪ **CASH** | **+19.9 bps** (±11.5) | `+42.5 bps` | `-0.031 / -0.024` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.25 | ⚪ **CASH** | **+15.0 bps** (±6.6) | `+25.4 bps` | `+0.005 / +0.035` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-19 02:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,654.01 | ⚪ **CASH** | **+38.3 bps** (±9.8) | `+71.6 bps` | `+0.005 / -0.014` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,771.95 | ⚪ **CASH** | **+19.9 bps** (±11.5) | `+42.5 bps` | `-0.031 / -0.024` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.24 | ⚪ **CASH** | **+15.0 bps** (±6.6) | `+25.4 bps` | `+0.005 / +0.035` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-19 02:15:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,844.00 | ⚪ **CASH** | **+38.3 bps** (±9.8) | `+71.6 bps` | `+0.005 / -0.014` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,776.93 | ⚪ **CASH** | **+19.9 bps** (±11.5) | `+42.5 bps` | `-0.031 / -0.024` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.53 | ⚪ **CASH** | **+15.0 bps** (±6.6) | `+25.4 bps` | `+0.005 / +0.035` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-19 02:01:03 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,770.01 | ⚪ **CASH** | **+38.3 bps** (±9.8) | `+71.6 bps` | `+0.005 / -0.014` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,776.00 | ⚪ **CASH** | **+19.9 bps** (±11.5) | `+42.5 bps` | `-0.031 / -0.024` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.43 | ⚪ **CASH** | **+15.0 bps** (±6.6) | `+25.4 bps` | `+0.005 / +0.035` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-19 01:45:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,706.01 | ⚪ **CASH** | **+34.1 bps** (±11.8) | `+62.4 bps` | `+0.012 / +0.001` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,776.49 | ⚪ **CASH** | **+31.3 bps** (±14.6) | `+65.0 bps` | `-0.036 / -0.037` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.39 | ⚪ **CASH** | **+11.8 bps** (±8.5) | `+21.1 bps` | `+0.002 / +0.017` | `0.71%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 01:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,649.91 | ⚪ **CASH** | **+34.1 bps** (±11.8) | `+62.4 bps` | `+0.012 / +0.001` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,775.08 | ⚪ **CASH** | **+31.3 bps** (±14.6) | `+65.0 bps` | `-0.036 / -0.037` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.18 | ⚪ **CASH** | **+11.8 bps** (±8.5) | `+21.1 bps` | `+0.002 / +0.017` | `0.71%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 01:15:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,986.79 | ⚪ **CASH** | **+34.1 bps** (±11.8) | `+62.4 bps` | `+0.012 / +0.001` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,782.29 | ⚪ **CASH** | **+31.3 bps** (±14.6) | `+65.0 bps` | `-0.036 / -0.037` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.48 | ⚪ **CASH** | **+11.8 bps** (±8.5) | `+21.1 bps` | `+0.002 / +0.017` | `0.71%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 01:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,219.12 | ⚪ **CASH** | **+34.1 bps** (±11.8) | `+62.4 bps` | `+0.012 / +0.001` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,786.59 | ⚪ **CASH** | **+31.3 bps** (±14.6) | `+65.0 bps` | `-0.036 / -0.037` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.77 | ⚪ **CASH** | **+11.8 bps** (±8.5) | `+21.1 bps` | `+0.002 / +0.017` | `0.71%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 00:45:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,240.57 | ⚪ **CASH** | **+35.1 bps** (±20.0) | `+65.3 bps` | `+0.007 / +0.018` | `0.53%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.0 bps > 19.5) |
| **ETHUSDT** | $1,785.72 | ⚪ **CASH** | **+33.9 bps** (±13.7) | `+68.2 bps` | `-0.034 / -0.017` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.81 | ⚪ **CASH** | **+12.5 bps** (±9.4) | `+24.8 bps` | `-0.006 / -0.001` | `0.73%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 00:30:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,866.01 | ⚪ **CASH** | **+35.1 bps** (±20.0) | `+65.3 bps` | `+0.007 / +0.018` | `0.53%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.0 bps > 19.5) |
| **ETHUSDT** | $1,778.54 | ⚪ **CASH** | **+33.9 bps** (±13.7) | `+68.2 bps` | `-0.034 / -0.017` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.47 | ⚪ **CASH** | **+12.5 bps** (±9.4) | `+24.8 bps` | `-0.006 / -0.001` | `0.73%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 00:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,840.01 | ⚪ **CASH** | **+35.1 bps** (±20.0) | `+65.3 bps` | `+0.007 / +0.018` | `0.53%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.0 bps > 19.5) |
| **ETHUSDT** | $1,772.64 | ⚪ **CASH** | **+33.9 bps** (±13.7) | `+68.2 bps` | `-0.034 / -0.017` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.50 | ⚪ **CASH** | **+12.5 bps** (±9.4) | `+24.8 bps` | `-0.006 / -0.001` | `0.73%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 00:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,954.42 | ⚪ **CASH** | **+35.1 bps** (±20.0) | `+65.3 bps` | `+0.007 / +0.018` | `0.53%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.0 bps > 19.5) |
| **ETHUSDT** | $1,775.32 | ⚪ **CASH** | **+33.9 bps** (±13.7) | `+68.2 bps` | `-0.034 / -0.017` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.54 | ⚪ **CASH** | **+12.5 bps** (±9.4) | `+24.8 bps` | `-0.006 / -0.001` | `0.73%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 23:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,070.43 | ⚪ **CASH** | **+39.0 bps** (±14.3) | `+65.8 bps` | `+0.016 / +0.084` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,780.75 | ⚪ **CASH** | **+62.5 bps** (±9.0) | `+118.8 bps` | `-0.041 / -0.005` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $73.74 | ⚪ **CASH** | **+21.4 bps** (±10.7) | `+40.9 bps` | `-0.017 / +0.012` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 23:30:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,795.26 | ⚪ **CASH** | **+39.0 bps** (±14.3) | `+65.8 bps` | `+0.016 / +0.084` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,772.69 | ⚪ **CASH** | **+62.5 bps** (±9.0) | `+118.8 bps` | `-0.041 / -0.005` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $73.42 | ⚪ **CASH** | **+21.4 bps** (±10.7) | `+40.9 bps` | `-0.017 / +0.012` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 23:15:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,598.65 | ⚪ **CASH** | **+39.0 bps** (±14.3) | `+65.8 bps` | `+0.016 / +0.084` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,768.35 | ⚪ **CASH** | **+62.5 bps** (±9.0) | `+118.8 bps` | `-0.041 / -0.005` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $73.19 | ⚪ **CASH** | **+21.4 bps** (±10.7) | `+40.9 bps` | `-0.017 / +0.012` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 23:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,319.38 | ⚪ **CASH** | **+39.0 bps** (±14.3) | `+65.8 bps` | `+0.016 / +0.084` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,759.51 | ⚪ **CASH** | **+62.5 bps** (±9.0) | `+118.8 bps` | `-0.041 / -0.005` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.68 | ⚪ **CASH** | **+21.4 bps** (±10.7) | `+40.9 bps` | `-0.017 / +0.012` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 22:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,510.01 | ⚪ **CASH** | **+37.2 bps** (±17.2) | `+64.3 bps` | `+0.033 / +0.024` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,765.47 | ⚪ **CASH** | **+57.1 bps** (±8.2) | `+108.0 bps` | `-0.039 / -0.009` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.90 | ⚪ **CASH** | **+25.8 bps** (±9.3) | `+45.5 bps` | `-0.009 / +0.038` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.8 bps) |

---

### 🕒 Ciclo `2026-11-18 22:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,568.35 | ⚪ **CASH** | **+37.2 bps** (±17.2) | `+64.3 bps` | `+0.033 / +0.024` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,765.02 | ⚪ **CASH** | **+57.1 bps** (±8.2) | `+108.0 bps` | `-0.039 / -0.009` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.96 | ⚪ **CASH** | **+25.8 bps** (±9.3) | `+45.5 bps` | `-0.009 / +0.038` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.8 bps) |

---

### 🕒 Ciclo `2026-11-18 22:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,421.87 | ⚪ **CASH** | **+37.2 bps** (±17.2) | `+64.3 bps` | `+0.033 / +0.024` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,765.35 | ⚪ **CASH** | **+57.1 bps** (±8.2) | `+108.0 bps` | `-0.039 / -0.009` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.88 | ⚪ **CASH** | **+25.8 bps** (±9.3) | `+45.5 bps` | `-0.009 / +0.038` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.8 bps) |

---

### 🕒 Ciclo `2026-11-18 22:00:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,377.00 | ⚪ **CASH** | **+37.2 bps** (±17.2) | `+64.3 bps` | `+0.033 / +0.024` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,764.94 | ⚪ **CASH** | **+57.1 bps** (±8.2) | `+108.0 bps` | `-0.039 / -0.009` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $73.02 | ⚪ **CASH** | **+25.8 bps** (±9.3) | `+45.5 bps` | `-0.009 / +0.038` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.8 bps) |

---

### 🕒 Ciclo `2026-11-18 21:45:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,365.16 | ⚪ **CASH** | **+33.3 bps** (±13.8) | `+59.9 bps` | `+0.029 / -0.018` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,764.68 | ⚪ **CASH** | **+39.6 bps** (±8.1) | `+75.8 bps` | `-0.033 / -0.006` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $73.00 | ⚪ **CASH** | **+23.8 bps** (±10.2) | `+42.7 bps` | `-0.004 / +0.023` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-18 21:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,432.53 | ⚪ **CASH** | **+33.3 bps** (±13.8) | `+59.9 bps` | `+0.029 / -0.018` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,761.94 | ⚪ **CASH** | **+39.6 bps** (±8.1) | `+75.8 bps` | `-0.033 / -0.006` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $73.08 | ⚪ **CASH** | **+23.8 bps** (±10.2) | `+42.7 bps` | `-0.004 / +0.023` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-18 21:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,477.10 | ⚪ **CASH** | **+33.3 bps** (±13.8) | `+59.9 bps` | `+0.029 / -0.018` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,755.61 | ⚪ **CASH** | **+39.6 bps** (±8.1) | `+75.8 bps` | `-0.033 / -0.006` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $73.06 | ⚪ **CASH** | **+23.8 bps** (±10.2) | `+42.7 bps` | `-0.004 / +0.023` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-18 21:00:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,648.00 | ⚪ **CASH** | **+33.3 bps** (±13.8) | `+59.9 bps` | `+0.029 / -0.018` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,755.24 | ⚪ **CASH** | **+39.6 bps** (±8.1) | `+75.8 bps` | `-0.033 / -0.006` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $73.13 | ⚪ **CASH** | **+23.8 bps** (±10.2) | `+42.7 bps` | `-0.004 / +0.023` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-18 20:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,504.00 | ⚪ **CASH** | **+34.5 bps** (±8.0) | `+59.1 bps` | `+0.034 / +0.002` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,748.71 | ⚪ **CASH** | **+38.7 bps** (±7.4) | `+73.7 bps` | `-0.035 / -0.003` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.92 | ⚪ **CASH** | **+19.0 bps** (±11.2) | `+36.2 bps` | `-0.018 / +0.007` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |
