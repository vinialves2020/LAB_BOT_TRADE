# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-16 03:45:41 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-16 03:45:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,987.78 | ⚪ **CASH** | **+7.2 bps** (±16.0) | `+37.8 bps` | `-0.101 / -0.106` | `0.80%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.6 bps) |
| **ETHUSDT** | $1,823.31 | ⚪ **CASH** | **-6.2 bps** (±24.4) | `+8.6 bps` | `-0.067 / -0.060` | `1.03%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.4 bps > 19.5) |
| **SOLUSDT** | $71.94 | ⚪ **CASH** | **+12.5 bps** (±17.4) | `+39.4 bps` | `-0.091 / +0.008` | `1.14%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.7 bps) |

---

### 🕒 Ciclo `2026-11-16 03:30:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,088.00 | ⚪ **CASH** | **+7.2 bps** (±16.0) | `+37.8 bps` | `-0.101 / -0.106` | `0.80%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.6 bps) |
| **ETHUSDT** | $1,821.76 | ⚪ **CASH** | **-6.2 bps** (±24.4) | `+8.6 bps` | `-0.067 / -0.060` | `1.03%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.4 bps > 19.5) |
| **SOLUSDT** | $72.11 | ⚪ **CASH** | **+12.5 bps** (±17.4) | `+39.4 bps` | `-0.091 / +0.008` | `1.14%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.7 bps) |

---

### 🕒 Ciclo `2026-11-16 03:15:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,120.01 | ⚪ **CASH** | **+7.2 bps** (±16.0) | `+37.8 bps` | `-0.101 / -0.106` | `0.80%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.6 bps) |
| **ETHUSDT** | $1,823.01 | ⚪ **CASH** | **-6.2 bps** (±24.4) | `+8.6 bps` | `-0.067 / -0.060` | `1.03%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.4 bps > 19.5) |
| **SOLUSDT** | $72.20 | ⚪ **CASH** | **+12.5 bps** (±17.4) | `+39.4 bps` | `-0.091 / +0.008` | `1.14%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.7 bps) |

---

### 🕒 Ciclo `2026-11-16 03:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,238.01 | ⚪ **CASH** | **+7.2 bps** (±16.0) | `+37.8 bps` | `-0.101 / -0.106` | `0.80%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.6 bps) |
| **ETHUSDT** | $1,827.83 | ⚪ **CASH** | **-6.2 bps** (±24.4) | `+8.6 bps` | `-0.067 / -0.060` | `1.03%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.4 bps > 19.5) |
| **SOLUSDT** | $72.38 | ⚪ **CASH** | **+12.5 bps** (±17.4) | `+39.4 bps` | `-0.091 / +0.008` | `1.14%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.7 bps) |

---

### 🕒 Ciclo `2026-11-16 02:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,174.01 | ⚪ **CASH** | **+17.0 bps** (±26.7) | `+57.9 bps` | `-0.088 / -0.141` | `0.79%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.7 bps > 19.5) |
| **ETHUSDT** | $1,824.78 | ⚪ **CASH** | **+4.8 bps** (±24.4) | `+26.2 bps` | `-0.043 / -0.069` | `1.03%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.4 bps > 19.5) |
| **SOLUSDT** | $72.27 | ⚪ **CASH** | **-16.4 bps** (±19.6) | `-17.2 bps` | `-0.066 / +0.026` | `1.13%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (19.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 02:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,215.42 | ⚪ **CASH** | **+17.0 bps** (±26.7) | `+57.9 bps` | `-0.088 / -0.141` | `0.79%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.7 bps > 19.5) |
| **ETHUSDT** | $1,828.79 | ⚪ **CASH** | **+4.8 bps** (±24.4) | `+26.2 bps` | `-0.043 / -0.069` | `1.03%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.4 bps > 19.5) |
| **SOLUSDT** | $72.46 | ⚪ **CASH** | **-16.4 bps** (±19.6) | `-17.2 bps` | `-0.066 / +0.026` | `1.13%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (19.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 02:15:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,993.40 | ⚪ **CASH** | **+17.0 bps** (±26.7) | `+57.9 bps` | `-0.088 / -0.141` | `0.79%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.7 bps > 19.5) |
| **ETHUSDT** | $1,820.79 | ⚪ **CASH** | **+4.8 bps** (±24.4) | `+26.2 bps` | `-0.043 / -0.069` | `1.03%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.4 bps > 19.5) |
| **SOLUSDT** | $72.01 | ⚪ **CASH** | **-16.4 bps** (±19.6) | `-17.2 bps` | `-0.066 / +0.026` | `1.13%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (19.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 02:00:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,625.79 | ⚪ **CASH** | **+17.0 bps** (±26.7) | `+57.9 bps` | `-0.088 / -0.141` | `0.79%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.7 bps > 19.5) |
| **ETHUSDT** | $1,805.97 | ⚪ **CASH** | **+4.8 bps** (±24.4) | `+26.2 bps` | `-0.043 / -0.069` | `1.03%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.4 bps > 19.5) |
| **SOLUSDT** | $71.37 | ⚪ **CASH** | **-16.4 bps** (±19.6) | `-17.2 bps` | `-0.066 / +0.026` | `1.13%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (19.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 01:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,811.05 | ⚪ **CASH** | **+10.0 bps** (±25.1) | `+47.2 bps` | `-0.099 / -0.149` | `0.80%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.1 bps > 19.5) |
| **ETHUSDT** | $1,809.37 | ⚪ **CASH** | **+6.9 bps** (±19.4) | `+28.8 bps` | `-0.047 / -0.049` | `1.04%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.27 | ⚪ **CASH** | **-16.9 bps** (±11.5) | `-22.5 bps` | `-0.067 / +0.080` | `1.14%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 01:30:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,971.99 | ⚪ **CASH** | **+10.0 bps** (±25.1) | `+47.2 bps` | `-0.099 / -0.149` | `0.80%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.1 bps > 19.5) |
| **ETHUSDT** | $1,815.75 | ⚪ **CASH** | **+6.9 bps** (±19.4) | `+28.8 bps` | `-0.047 / -0.049` | `1.04%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.53 | ⚪ **CASH** | **-16.9 bps** (±11.5) | `-22.5 bps` | `-0.067 / +0.080` | `1.14%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 01:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,864.00 | ⚪ **CASH** | **+10.0 bps** (±25.1) | `+47.2 bps` | `-0.099 / -0.149` | `0.80%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.1 bps > 19.5) |
| **ETHUSDT** | $1,812.80 | ⚪ **CASH** | **+6.9 bps** (±19.4) | `+28.8 bps` | `-0.047 / -0.049` | `1.04%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.54 | ⚪ **CASH** | **-16.9 bps** (±11.5) | `-22.5 bps` | `-0.067 / +0.080` | `1.14%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 01:01:01 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,878.01 | ⚪ **CASH** | **+10.0 bps** (±25.1) | `+47.2 bps` | `-0.099 / -0.149` | `0.80%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.1 bps > 19.5) |
| **ETHUSDT** | $1,811.98 | ⚪ **CASH** | **+6.9 bps** (±19.4) | `+28.8 bps` | `-0.047 / -0.049` | `1.04%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.79 | ⚪ **CASH** | **-16.9 bps** (±11.5) | `-22.5 bps` | `-0.067 / +0.080` | `1.14%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 00:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,805.88 | ⚪ **CASH** | **+7.4 bps** (±18.0) | `+42.0 bps` | `-0.095 / -0.174` | `0.80%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,811.32 | ⚪ **CASH** | **-8.0 bps** (±31.8) | `+6.0 bps` | `-0.061 / -0.064` | `1.04%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (31.8 bps > 19.5) |
| **SOLUSDT** | $71.64 | ⚪ **CASH** | **-17.9 bps** (±23.7) | `-19.2 bps` | `-0.075 / +0.044` | `1.14%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (23.7 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 00:30:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,993.50 | ⚪ **CASH** | **+7.4 bps** (±18.0) | `+42.0 bps` | `-0.095 / -0.174` | `0.80%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,822.97 | ⚪ **CASH** | **-8.0 bps** (±31.8) | `+6.0 bps` | `-0.061 / -0.064` | `1.04%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (31.8 bps > 19.5) |
| **SOLUSDT** | $72.05 | ⚪ **CASH** | **-17.9 bps** (±23.7) | `-19.2 bps` | `-0.075 / +0.044` | `1.14%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (23.7 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 00:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,024.23 | ⚪ **CASH** | **+7.4 bps** (±18.0) | `+42.0 bps` | `-0.095 / -0.174` | `0.80%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,824.74 | ⚪ **CASH** | **-8.0 bps** (±31.8) | `+6.0 bps` | `-0.061 / -0.064` | `1.04%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (31.8 bps > 19.5) |
| **SOLUSDT** | $72.24 | ⚪ **CASH** | **-17.9 bps** (±23.7) | `-19.2 bps` | `-0.075 / +0.044` | `1.14%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (23.7 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 00:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,326.00 | ⚪ **CASH** | **+7.4 bps** (±18.0) | `+42.0 bps` | `-0.095 / -0.174` | `0.80%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,835.56 | ⚪ **CASH** | **-8.0 bps** (±31.8) | `+6.0 bps` | `-0.061 / -0.064` | `1.04%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (31.8 bps > 19.5) |
| **SOLUSDT** | $72.73 | ⚪ **CASH** | **-17.9 bps** (±23.7) | `-19.2 bps` | `-0.075 / +0.044` | `1.14%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (23.7 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 23:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,317.47 | ⚪ **CASH** | **-4.1 bps** (±17.1) | `+25.8 bps` | `-0.073 / -0.296` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,835.51 | ⚪ **CASH** | **+5.1 bps** (±21.9) | `+32.8 bps` | `-0.056 / -0.161` | `1.05%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.9 bps > 19.5) |
| **SOLUSDT** | $72.67 | ⚪ **CASH** | **-19.4 bps** (±21.9) | `-22.4 bps` | `-0.070 / +0.025` | `1.15%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (21.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 23:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,113.46 | ⚪ **CASH** | **-4.1 bps** (±17.1) | `+25.8 bps` | `-0.073 / -0.296` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,829.87 | ⚪ **CASH** | **+5.1 bps** (±21.9) | `+32.8 bps` | `-0.056 / -0.161` | `1.05%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.9 bps > 19.5) |
| **SOLUSDT** | $72.38 | ⚪ **CASH** | **-19.4 bps** (±21.9) | `-22.4 bps` | `-0.070 / +0.025` | `1.15%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (21.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 23:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,080.01 | ⚪ **CASH** | **-4.1 bps** (±17.1) | `+25.8 bps` | `-0.073 / -0.296` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,826.79 | ⚪ **CASH** | **+5.1 bps** (±21.9) | `+32.8 bps` | `-0.056 / -0.161` | `1.05%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.9 bps > 19.5) |
| **SOLUSDT** | $72.29 | ⚪ **CASH** | **-19.4 bps** (±21.9) | `-22.4 bps` | `-0.070 / +0.025` | `1.15%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (21.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 23:01:01 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,408.95 | ⚪ **CASH** | **-4.1 bps** (±17.1) | `+25.8 bps` | `-0.073 / -0.296` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,836.41 | ⚪ **CASH** | **+5.1 bps** (±21.9) | `+32.8 bps` | `-0.056 / -0.161` | `1.05%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.9 bps > 19.5) |
| **SOLUSDT** | $72.78 | ⚪ **CASH** | **-19.4 bps** (±21.9) | `-22.4 bps` | `-0.070 / +0.025` | `1.15%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (21.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 22:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,161.38 | ⚪ **CASH** | **+1.8 bps** (±8.2) | `+34.3 bps` | `-0.068 / -0.299` | `0.82%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,827.39 | ⚪ **CASH** | **-4.9 bps** (±14.2) | `+14.2 bps` | `-0.062 / -0.168` | `1.06%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.31 | ⚪ **CASH** | **-20.6 bps** (±20.2) | `-23.9 bps` | `-0.070 / +0.005` | `1.16%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 22:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,186.01 | ⚪ **CASH** | **+1.8 bps** (±8.2) | `+34.3 bps` | `-0.068 / -0.299` | `0.82%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,827.49 | ⚪ **CASH** | **-4.9 bps** (±14.2) | `+14.2 bps` | `-0.062 / -0.168` | `1.06%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.28 | ⚪ **CASH** | **-20.6 bps** (±20.2) | `-23.9 bps` | `-0.070 / +0.005` | `1.16%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 22:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,206.89 | ⚪ **CASH** | **+1.8 bps** (±8.2) | `+34.3 bps` | `-0.068 / -0.299` | `0.82%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,824.67 | ⚪ **CASH** | **-4.9 bps** (±14.2) | `+14.2 bps` | `-0.062 / -0.168` | `1.06%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.18 | ⚪ **CASH** | **-20.6 bps** (±20.2) | `-23.9 bps` | `-0.070 / +0.005` | `1.16%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 22:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,940.01 | ⚪ **CASH** | **+1.8 bps** (±8.2) | `+34.3 bps` | `-0.068 / -0.299` | `0.82%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,818.05 | ⚪ **CASH** | **-4.9 bps** (±14.2) | `+14.2 bps` | `-0.062 / -0.168` | `1.06%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.87 | ⚪ **CASH** | **-20.6 bps** (±20.2) | `-23.9 bps` | `-0.070 / +0.005` | `1.16%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 21:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,086.49 | ⚪ **CASH** | **+1.6 bps** (±14.7) | `+30.9 bps` | `-0.061 / -0.248` | `0.83%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,822.48 | ⚪ **CASH** | **+44.7 bps** (±15.8) | `+105.4 bps` | `-0.063 / -0.183` | `1.07%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $72.05 | ⚪ **CASH** | **-25.7 bps** (±17.7) | `-31.7 bps` | `-0.076 / -0.019` | `1.17%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-15 21:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,966.01 | ⚪ **CASH** | **+1.6 bps** (±14.7) | `+30.9 bps` | `-0.061 / -0.248` | `0.83%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,816.79 | ⚪ **CASH** | **+44.7 bps** (±15.8) | `+105.4 bps` | `-0.063 / -0.183` | `1.07%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $71.78 | ⚪ **CASH** | **-25.7 bps** (±17.7) | `-31.7 bps` | `-0.076 / -0.019` | `1.17%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-15 21:15:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,008.01 | ⚪ **CASH** | **+1.6 bps** (±14.7) | `+30.9 bps` | `-0.061 / -0.248` | `0.83%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,821.11 | ⚪ **CASH** | **+44.7 bps** (±15.8) | `+105.4 bps` | `-0.063 / -0.183` | `1.07%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $71.80 | ⚪ **CASH** | **-25.7 bps** (±17.7) | `-31.7 bps` | `-0.076 / -0.019` | `1.17%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-15 21:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,068.29 | ⚪ **CASH** | **+1.6 bps** (±14.7) | `+30.9 bps` | `-0.061 / -0.248` | `0.83%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,823.57 | ⚪ **CASH** | **+44.7 bps** (±15.8) | `+105.4 bps` | `-0.063 / -0.183` | `1.07%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $71.80 | ⚪ **CASH** | **-25.7 bps** (±17.7) | `-31.7 bps` | `-0.076 / -0.019` | `1.17%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-15 20:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,988.01 | ⚪ **CASH** | **+0.9 bps** (±22.1) | `+31.2 bps` | `-0.068 / -0.238` | `0.84%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,826.92 | ⚪ **CASH** | **+22.0 bps** (±33.6) | `+70.9 bps` | `-0.077 / -0.212` | `1.09%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.6 bps > 19.5) |
| **SOLUSDT** | $71.88 | ⚪ **CASH** | **-17.3 bps** (±49.9) | `-7.1 bps` | `-0.080 / -0.063` | `1.19%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (49.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 20:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,918.01 | ⚪ **CASH** | **+0.9 bps** (±22.1) | `+31.2 bps` | `-0.068 / -0.238` | `0.84%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,825.57 | ⚪ **CASH** | **+22.0 bps** (±33.6) | `+70.9 bps` | `-0.077 / -0.212` | `1.09%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.6 bps > 19.5) |
| **SOLUSDT** | $71.67 | ⚪ **CASH** | **-17.3 bps** (±49.9) | `-7.1 bps` | `-0.080 / -0.063` | `1.19%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (49.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 20:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,720.01 | ⚪ **CASH** | **+0.9 bps** (±22.1) | `+31.2 bps` | `-0.068 / -0.238` | `0.84%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,817.68 | ⚪ **CASH** | **+22.0 bps** (±33.6) | `+70.9 bps` | `-0.077 / -0.212` | `1.09%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.6 bps > 19.5) |
| **SOLUSDT** | $71.25 | ⚪ **CASH** | **-17.3 bps** (±49.9) | `-7.1 bps` | `-0.080 / -0.063` | `1.19%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (49.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 20:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,896.01 | ⚪ **CASH** | **+0.9 bps** (±22.1) | `+31.2 bps` | `-0.068 / -0.238` | `0.84%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,822.11 | ⚪ **CASH** | **+22.0 bps** (±33.6) | `+70.9 bps` | `-0.077 / -0.212` | `1.09%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.6 bps > 19.5) |
| **SOLUSDT** | $71.59 | ⚪ **CASH** | **-17.3 bps** (±49.9) | `-7.1 bps` | `-0.080 / -0.063` | `1.19%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (49.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 19:45:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,980.86 | ⚪ **CASH** | **+9.0 bps** (±23.3) | `+43.3 bps` | `-0.064 / -0.203` | `0.85%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.3 bps > 19.5) |
| **ETHUSDT** | $1,825.76 | ⚪ **CASH** | **+12.9 bps** (±35.2) | `+55.2 bps` | `-0.077 / -0.223` | `1.10%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (35.2 bps > 19.5) |
| **SOLUSDT** | $71.82 | ⚪ **CASH** | **-37.3 bps** (±28.9) | `-44.7 bps` | `-0.087 / -0.095` | `1.19%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 19:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,980.00 | ⚪ **CASH** | **+9.0 bps** (±23.3) | `+43.3 bps` | `-0.064 / -0.203` | `0.85%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.3 bps > 19.5) |
| **ETHUSDT** | $1,826.51 | ⚪ **CASH** | **+12.9 bps** (±35.2) | `+55.2 bps` | `-0.077 / -0.223` | `1.10%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (35.2 bps > 19.5) |
| **SOLUSDT** | $71.68 | ⚪ **CASH** | **-37.3 bps** (±28.9) | `-44.7 bps` | `-0.087 / -0.095` | `1.19%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 19:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,019.16 | ⚪ **CASH** | **+9.0 bps** (±23.3) | `+43.3 bps` | `-0.064 / -0.203` | `0.85%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.3 bps > 19.5) |
| **ETHUSDT** | $1,823.92 | ⚪ **CASH** | **+12.9 bps** (±35.2) | `+55.2 bps` | `-0.077 / -0.223` | `1.10%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (35.2 bps > 19.5) |
| **SOLUSDT** | $71.59 | ⚪ **CASH** | **-37.3 bps** (±28.9) | `-44.7 bps` | `-0.087 / -0.095` | `1.19%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 19:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,756.03 | ⚪ **CASH** | **+9.0 bps** (±23.3) | `+43.3 bps` | `-0.064 / -0.203` | `0.85%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.3 bps > 19.5) |
| **ETHUSDT** | $1,817.13 | ⚪ **CASH** | **+12.9 bps** (±35.2) | `+55.2 bps` | `-0.077 / -0.223` | `1.10%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (35.2 bps > 19.5) |
| **SOLUSDT** | $71.21 | ⚪ **CASH** | **-37.3 bps** (±28.9) | `-44.7 bps` | `-0.087 / -0.095` | `1.19%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.9 bps > 19.5) |
