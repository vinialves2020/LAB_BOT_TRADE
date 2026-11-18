# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-18 02:15:51 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-18 02:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,302.64 | ⚪ **CASH** | **+17.0 bps** (±15.5) | `+13.4 bps` | `+0.094 / +0.098` | `0.61%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,801.58 | ⚪ **CASH** | **-0.8 bps** (±16.3) | `+7.7 bps` | `-0.082 / -0.041` | `0.77%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.38 | ⚪ **CASH** | **+16.6 bps** (±11.7) | `+38.9 bps` | `-0.074 / -0.061` | `0.84%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 02:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,347.72 | ⚪ **CASH** | **+17.0 bps** (±15.5) | `+13.4 bps` | `+0.094 / +0.098` | `0.61%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,803.59 | ⚪ **CASH** | **-0.8 bps** (±16.3) | `+7.7 bps` | `-0.082 / -0.041` | `0.77%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.26 | ⚪ **CASH** | **+16.6 bps** (±11.7) | `+38.9 bps` | `-0.074 / -0.061` | `0.84%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 01:45:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,476.49 | ⚪ **CASH** | **+6.3 bps** (±12.1) | `-8.7 bps` | `+0.100 / +0.116` | `0.60%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,809.17 | ⚪ **CASH** | **-16.6 bps** (±26.5) | `-21.1 bps` | `-0.079 / -0.020` | `0.77%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.5 bps > 19.5) |
| **SOLUSDT** | $74.48 | ⚪ **CASH** | **+14.7 bps** (±7.4) | `+34.5 bps` | `-0.081 / -0.051` | `0.84%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 01:30:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,538.77 | ⚪ **CASH** | **+6.3 bps** (±12.1) | `-8.7 bps` | `+0.100 / +0.116` | `0.60%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,809.46 | ⚪ **CASH** | **-16.6 bps** (±26.5) | `-21.1 bps` | `-0.079 / -0.020` | `0.77%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.5 bps > 19.5) |
| **SOLUSDT** | $74.37 | ⚪ **CASH** | **+14.7 bps** (±7.4) | `+34.5 bps` | `-0.081 / -0.051` | `0.84%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 01:15:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,655.51 | ⚪ **CASH** | **+6.3 bps** (±12.1) | `-8.7 bps` | `+0.100 / +0.116` | `0.60%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,815.43 | ⚪ **CASH** | **-16.6 bps** (±26.5) | `-21.1 bps` | `-0.079 / -0.020` | `0.77%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.5 bps > 19.5) |
| **SOLUSDT** | $74.79 | ⚪ **CASH** | **+14.7 bps** (±7.4) | `+34.5 bps` | `-0.081 / -0.051` | `0.84%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 01:01:02 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,684.13 | ⚪ **CASH** | **+6.3 bps** (±12.1) | `-8.7 bps` | `+0.100 / +0.116` | `0.60%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,817.10 | ⚪ **CASH** | **-16.6 bps** (±26.5) | `-21.1 bps` | `-0.079 / -0.020` | `0.77%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.5 bps > 19.5) |
| **SOLUSDT** | $74.81 | ⚪ **CASH** | **+14.7 bps** (±7.4) | `+34.5 bps` | `-0.081 / -0.051` | `0.84%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 00:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,698.70 | ⚪ **CASH** | **+0.6 bps** (±18.7) | `-18.3 bps` | `+0.102 / +0.120` | `0.62%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,817.39 | ⚪ **CASH** | **-15.9 bps** (±26.6) | `-20.2 bps` | `-0.083 / -0.011` | `0.78%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (26.6 bps > 19.5) |
| **SOLUSDT** | $75.08 | ⚪ **CASH** | **+25.1 bps** (±16.8) | `+54.9 bps` | `-0.084 / -0.046` | `0.85%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 00:30:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,839.32 | ⚪ **CASH** | **+0.6 bps** (±18.7) | `-18.3 bps` | `+0.102 / +0.120` | `0.62%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,821.68 | ⚪ **CASH** | **-15.9 bps** (±26.6) | `-20.2 bps` | `-0.083 / -0.011` | `0.78%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (26.6 bps > 19.5) |
| **SOLUSDT** | $75.35 | ⚪ **CASH** | **+25.1 bps** (±16.8) | `+54.9 bps` | `-0.084 / -0.046` | `0.85%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 00:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,884.42 | ⚪ **CASH** | **+0.6 bps** (±18.7) | `-18.3 bps` | `+0.102 / +0.120` | `0.62%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,821.89 | ⚪ **CASH** | **-15.9 bps** (±26.6) | `-20.2 bps` | `-0.083 / -0.011` | `0.78%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (26.6 bps > 19.5) |
| **SOLUSDT** | $74.94 | ⚪ **CASH** | **+25.1 bps** (±16.8) | `+54.9 bps` | `-0.084 / -0.046` | `0.85%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 00:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,926.75 | ⚪ **CASH** | **+0.6 bps** (±18.7) | `-18.3 bps` | `+0.102 / +0.120` | `0.62%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,825.31 | ⚪ **CASH** | **-15.9 bps** (±26.6) | `-20.2 bps` | `-0.083 / -0.011` | `0.78%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (26.6 bps > 19.5) |
| **SOLUSDT** | $75.20 | ⚪ **CASH** | **+25.1 bps** (±16.8) | `+54.9 bps` | `-0.084 / -0.046` | `0.85%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 23:45:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,940.97 | ⚪ **CASH** | **+2.2 bps** (±15.6) | `-13.6 bps` | `+0.093 / +0.102` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,823.71 | ⚪ **CASH** | **-43.6 bps** (±3.9) | `-73.1 bps` | `-0.092 / -0.015` | `0.79%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.97 | ⚪ **CASH** | **+12.1 bps** (±11.3) | `+30.9 bps` | `-0.095 / -0.033` | `0.83%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 23:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,006.77 | ⚪ **CASH** | **+2.2 bps** (±15.6) | `-13.6 bps` | `+0.093 / +0.102` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,824.04 | ⚪ **CASH** | **-43.6 bps** (±3.9) | `-73.1 bps` | `-0.092 / -0.015` | `0.79%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.09 | ⚪ **CASH** | **+12.1 bps** (±11.3) | `+30.9 bps` | `-0.095 / -0.033` | `0.83%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 23:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,085.87 | ⚪ **CASH** | **+2.2 bps** (±15.6) | `-13.6 bps` | `+0.093 / +0.102` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,827.20 | ⚪ **CASH** | **-43.6 bps** (±3.9) | `-73.1 bps` | `-0.092 / -0.015` | `0.79%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.20 | ⚪ **CASH** | **+12.1 bps** (±11.3) | `+30.9 bps` | `-0.095 / -0.033` | `0.83%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 23:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,749.77 | ⚪ **CASH** | **+2.2 bps** (±15.6) | `-13.6 bps` | `+0.093 / +0.102` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,815.71 | ⚪ **CASH** | **-43.6 bps** (±3.9) | `-73.1 bps` | `-0.092 / -0.015` | `0.79%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.01 | ⚪ **CASH** | **+12.1 bps** (±11.3) | `+30.9 bps` | `-0.095 / -0.033` | `0.83%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 22:45:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,833.54 | ⚪ **CASH** | **+12.5 bps** (±11.2) | `+7.8 bps` | `+0.082 / +0.075` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,815.88 | ⚪ **CASH** | **-36.4 bps** (±5.8) | `-57.6 bps` | `-0.095 / -0.036` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.02 | ⚪ **CASH** | **+7.7 bps** (±14.8) | `+25.0 bps` | `-0.102 / -0.036` | `0.84%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 22:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,674.96 | ⚪ **CASH** | **+12.5 bps** (±11.2) | `+7.8 bps` | `+0.082 / +0.075` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,811.73 | ⚪ **CASH** | **-36.4 bps** (±5.8) | `-57.6 bps` | `-0.095 / -0.036` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.92 | ⚪ **CASH** | **+7.7 bps** (±14.8) | `+25.0 bps` | `-0.102 / -0.036` | `0.84%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 22:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,448.61 | ⚪ **CASH** | **+12.5 bps** (±11.2) | `+7.8 bps` | `+0.082 / +0.075` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,805.64 | ⚪ **CASH** | **-36.4 bps** (±5.8) | `-57.6 bps` | `-0.095 / -0.036` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.67 | ⚪ **CASH** | **+7.7 bps** (±14.8) | `+25.0 bps` | `-0.102 / -0.036` | `0.84%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 22:01:05 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,299.40 | ⚪ **CASH** | **+12.5 bps** (±11.2) | `+7.8 bps` | `+0.082 / +0.075` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,803.38 | ⚪ **CASH** | **-36.4 bps** (±5.8) | `-57.6 bps` | `-0.095 / -0.036` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.40 | ⚪ **CASH** | **+7.7 bps** (±14.8) | `+25.0 bps` | `-0.102 / -0.036` | `0.84%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 21:45:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,373.39 | ⚪ **CASH** | **+9.6 bps** (±9.6) | `+3.7 bps` | `+0.087 / +0.040` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.2 bps) |
| **ETHUSDT** | $1,808.01 | ⚪ **CASH** | **-26.3 bps** (±15.4) | `-34.0 bps` | `-0.102 / -0.081` | `0.82%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.3 bps) |
| **SOLUSDT** | $73.54 | ⚪ **CASH** | **+15.0 bps** (±6.0) | `+42.0 bps` | `-0.104 / -0.117` | `0.85%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 21:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,598.48 | ⚪ **CASH** | **+9.6 bps** (±9.6) | `+3.7 bps` | `+0.087 / +0.040` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.2 bps) |
| **ETHUSDT** | $1,816.77 | ⚪ **CASH** | **-26.3 bps** (±15.4) | `-34.0 bps` | `-0.102 / -0.081` | `0.82%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.3 bps) |
| **SOLUSDT** | $73.97 | ⚪ **CASH** | **+15.0 bps** (±6.0) | `+42.0 bps` | `-0.104 / -0.117` | `0.85%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 21:15:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,051.13 | ⚪ **CASH** | **+9.6 bps** (±9.6) | `+3.7 bps` | `+0.087 / +0.040` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.2 bps) |
| **ETHUSDT** | $1,797.58 | ⚪ **CASH** | **-26.3 bps** (±15.4) | `-34.0 bps` | `-0.102 / -0.081` | `0.82%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.3 bps) |
| **SOLUSDT** | $73.12 | ⚪ **CASH** | **+15.0 bps** (±6.0) | `+42.0 bps` | `-0.104 / -0.117` | `0.85%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 21:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,043.17 | ⚪ **CASH** | **+9.6 bps** (±9.6) | `+3.7 bps` | `+0.087 / +0.040` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.2 bps) |
| **ETHUSDT** | $1,804.77 | ⚪ **CASH** | **-26.3 bps** (±15.4) | `-34.0 bps` | `-0.102 / -0.081` | `0.82%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.3 bps) |
| **SOLUSDT** | $73.25 | ⚪ **CASH** | **+15.0 bps** (±6.0) | `+42.0 bps` | `-0.104 / -0.117` | `0.85%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 20:45:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,985.09 | ⚪ **CASH** | **+16.2 bps** (±3.1) | `+12.2 bps` | `+0.091 / +0.067` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |
| **ETHUSDT** | $1,798.71 | ⚪ **CASH** | **-19.4 bps** (±11.6) | `-24.9 bps` | `-0.092 / -0.055` | `0.84%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |
| **SOLUSDT** | $73.01 | ⚪ **CASH** | **+12.3 bps** (±11.9) | `+33.0 bps` | `-0.092 / -0.060` | `0.87%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |

---

### 🕒 Ciclo `2026-11-17 20:30:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,991.00 | ⚪ **CASH** | **+16.2 bps** (±3.1) | `+12.2 bps` | `+0.091 / +0.067` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |
| **ETHUSDT** | $1,798.07 | ⚪ **CASH** | **-19.4 bps** (±11.6) | `-24.9 bps` | `-0.092 / -0.055` | `0.84%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |
| **SOLUSDT** | $73.03 | ⚪ **CASH** | **+12.3 bps** (±11.9) | `+33.0 bps` | `-0.092 / -0.060` | `0.87%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |

---

### 🕒 Ciclo `2026-11-17 20:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,815.43 | ⚪ **CASH** | **+16.2 bps** (±3.1) | `+12.2 bps` | `+0.091 / +0.067` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |
| **ETHUSDT** | $1,793.91 | ⚪ **CASH** | **-19.4 bps** (±11.6) | `-24.9 bps` | `-0.092 / -0.055` | `0.84%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |
| **SOLUSDT** | $72.82 | ⚪ **CASH** | **+12.3 bps** (±11.9) | `+33.0 bps` | `-0.092 / -0.060` | `0.87%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |

---

### 🕒 Ciclo `2026-11-17 20:00:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,750.01 | ⚪ **CASH** | **+16.2 bps** (±3.1) | `+12.2 bps` | `+0.091 / +0.067` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |
| **ETHUSDT** | $1,791.06 | ⚪ **CASH** | **-19.4 bps** (±11.6) | `-24.9 bps` | `-0.092 / -0.055` | `0.84%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |
| **SOLUSDT** | $72.82 | ⚪ **CASH** | **+12.3 bps** (±11.9) | `+33.0 bps` | `-0.092 / -0.060` | `0.87%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |

---

### 🕒 Ciclo `2026-11-17 19:45:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,864.91 | ⚪ **CASH** | **+10.4 bps** (±5.7) | `+5.3 bps` | `+0.084 / +0.034` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.2 bps) |
| **ETHUSDT** | $1,793.77 | ⚪ **CASH** | **-23.0 bps** (±13.5) | `-30.4 bps` | `-0.091 / -0.064` | `0.86%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.4 bps) |
| **SOLUSDT** | $73.00 | ⚪ **CASH** | **+12.8 bps** (±13.2) | `+35.4 bps` | `-0.095 / -0.070` | `0.88%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-17 19:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,732.23 | ⚪ **CASH** | **+10.4 bps** (±5.7) | `+5.3 bps` | `+0.084 / +0.034` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.2 bps) |
| **ETHUSDT** | $1,788.96 | ⚪ **CASH** | **-23.0 bps** (±13.5) | `-30.4 bps` | `-0.091 / -0.064` | `0.86%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.4 bps) |
| **SOLUSDT** | $72.50 | ⚪ **CASH** | **+12.8 bps** (±13.2) | `+35.4 bps` | `-0.095 / -0.070` | `0.88%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-17 19:15:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,852.23 | ⚪ **CASH** | **+10.4 bps** (±5.7) | `+5.3 bps` | `+0.084 / +0.034` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.2 bps) |
| **ETHUSDT** | $1,793.34 | ⚪ **CASH** | **-23.0 bps** (±13.5) | `-30.4 bps` | `-0.091 / -0.064` | `0.86%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.4 bps) |
| **SOLUSDT** | $72.73 | ⚪ **CASH** | **+12.8 bps** (±13.2) | `+35.4 bps` | `-0.095 / -0.070` | `0.88%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-17 19:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,731.36 | ⚪ **CASH** | **+10.4 bps** (±5.7) | `+5.3 bps` | `+0.084 / +0.034` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.2 bps) |
| **ETHUSDT** | $1,788.00 | ⚪ **CASH** | **-23.0 bps** (±13.5) | `-30.4 bps` | `-0.091 / -0.064` | `0.86%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.4 bps) |
| **SOLUSDT** | $72.37 | ⚪ **CASH** | **+12.8 bps** (±13.2) | `+35.4 bps` | `-0.095 / -0.070` | `0.88%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-17 18:45:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,744.62 | ⚪ **CASH** | **+11.2 bps** (±9.4) | `+6.2 bps` | `+0.092 / +0.037` | `0.66%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |
| **ETHUSDT** | $1,788.49 | ⚪ **CASH** | **-19.6 bps** (±8.8) | `-24.3 bps` | `-0.093 / -0.077` | `0.87%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |
| **SOLUSDT** | $72.37 | ⚪ **CASH** | **+13.6 bps** (±12.8) | `+35.9 bps` | `-0.097 / -0.059` | `0.90%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |

---

### 🕒 Ciclo `2026-11-17 18:31:03 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,895.78 | ⚪ **CASH** | **+11.2 bps** (±9.4) | `+6.2 bps` | `+0.092 / +0.037` | `0.66%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |
| **ETHUSDT** | $1,798.18 | ⚪ **CASH** | **-19.6 bps** (±8.8) | `-24.3 bps` | `-0.093 / -0.077` | `0.87%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |
| **SOLUSDT** | $72.72 | ⚪ **CASH** | **+13.6 bps** (±12.8) | `+35.9 bps` | `-0.097 / -0.059` | `0.90%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |

---

### 🕒 Ciclo `2026-11-17 18:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,660.71 | ⚪ **CASH** | **+11.2 bps** (±9.4) | `+6.2 bps` | `+0.092 / +0.037` | `0.66%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |
| **ETHUSDT** | $1,784.48 | ⚪ **CASH** | **-19.6 bps** (±8.8) | `-24.3 bps` | `-0.093 / -0.077` | `0.87%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |
| **SOLUSDT** | $72.06 | ⚪ **CASH** | **+13.6 bps** (±12.8) | `+35.9 bps` | `-0.097 / -0.059` | `0.90%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |

---

### 🕒 Ciclo `2026-11-17 18:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,825.65 | ⚪ **CASH** | **+11.2 bps** (±9.4) | `+6.2 bps` | `+0.092 / +0.037` | `0.66%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |
| **ETHUSDT** | $1,787.88 | ⚪ **CASH** | **-19.6 bps** (±8.8) | `-24.3 bps` | `-0.093 / -0.077` | `0.87%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |
| **SOLUSDT** | $72.39 | ⚪ **CASH** | **+13.6 bps** (±12.8) | `+35.9 bps` | `-0.097 / -0.059` | `0.90%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |

---

### 🕒 Ciclo `2026-11-17 17:45:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,781.34 | ⚪ **CASH** | **-2.6 bps** (±5.6) | `-21.6 bps` | `+0.095 / +0.058` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.4 bps) |
| **ETHUSDT** | $1,784.12 | ⚪ **CASH** | **-35.5 bps** (±7.7) | `-52.7 bps` | `-0.101 / -0.079` | `0.88%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.4 bps) |
| **SOLUSDT** | $72.36 | ⚪ **CASH** | **+27.1 bps** (±14.5) | `+61.8 bps` | `-0.108 / -0.060` | `0.91%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.3 bps) |

---

### 🕒 Ciclo `2026-11-17 17:30:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,741.65 | ⚪ **CASH** | **-2.6 bps** (±5.6) | `-21.6 bps` | `+0.095 / +0.058` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.4 bps) |
| **ETHUSDT** | $1,784.03 | ⚪ **CASH** | **-35.5 bps** (±7.7) | `-52.7 bps` | `-0.101 / -0.079` | `0.88%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.4 bps) |
| **SOLUSDT** | $72.26 | ⚪ **CASH** | **+27.1 bps** (±14.5) | `+61.8 bps` | `-0.108 / -0.060` | `0.91%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.3 bps) |
