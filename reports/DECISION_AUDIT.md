# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-06 15:30:50 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-06 15:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,452.90 | ⚪ **CASH** | **+3.8 bps** (±5.0) | `+9.0 bps` | `-0.013 / +0.011` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,216.95 | ⚪ **CASH** | **-12.5 bps** (±5.9) | `-12.9 bps` | `-0.048 / -0.053` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.37 | ⚪ **CASH** | **-33.9 bps** (±4.8) | `-55.2 bps` | `-0.017 / -0.052` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 15:15:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,802.00 | ⚪ **CASH** | **+3.8 bps** (±5.0) | `+9.0 bps` | `-0.013 / +0.011` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,232.67 | ⚪ **CASH** | **-12.5 bps** (±5.9) | `-12.9 bps` | `-0.048 / -0.053` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.09 | ⚪ **CASH** | **-33.9 bps** (±4.8) | `-55.2 bps` | `-0.017 / -0.052` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 15:00:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,538.24 | ⚪ **CASH** | **+3.8 bps** (±5.0) | `+9.0 bps` | `-0.013 / +0.011` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,228.10 | ⚪ **CASH** | **-12.5 bps** (±5.9) | `-12.9 bps` | `-0.048 / -0.053` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.96 | ⚪ **CASH** | **-33.9 bps** (±4.8) | `-55.2 bps` | `-0.017 / -0.052` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 14:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,946.01 | ⚪ **CASH** | **-0.2 bps** (±16.6) | `-3.6 bps` | `-0.016 / +0.132` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,243.17 | ⚪ **CASH** | **-8.3 bps** (±6.2) | `-13.6 bps` | `-0.044 / +0.071` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.28 | ⚪ **CASH** | **-54.7 bps** (±20.1) | `-90.4 bps` | `-0.027 / -0.029` | `0.76%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 14:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,774.58 | ⚪ **CASH** | **-0.2 bps** (±16.6) | `-3.6 bps` | `-0.016 / +0.132` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.65 | ⚪ **CASH** | **-8.3 bps** (±6.2) | `-13.6 bps` | `-0.044 / +0.071` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.48 | ⚪ **CASH** | **-54.7 bps** (±20.1) | `-90.4 bps` | `-0.027 / -0.029` | `0.76%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 14:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,583.30 | ⚪ **CASH** | **-0.2 bps** (±16.6) | `-3.6 bps` | `-0.016 / +0.132` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,228.18 | ⚪ **CASH** | **-8.3 bps** (±6.2) | `-13.6 bps` | `-0.044 / +0.071` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.96 | ⚪ **CASH** | **-54.7 bps** (±20.1) | `-90.4 bps` | `-0.027 / -0.029` | `0.76%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 14:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,878.34 | ⚪ **CASH** | **-0.2 bps** (±16.6) | `-3.6 bps` | `-0.016 / +0.132` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.76 | ⚪ **CASH** | **-8.3 bps** (±6.2) | `-13.6 bps` | `-0.044 / +0.071` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.37 | ⚪ **CASH** | **-54.7 bps** (±20.1) | `-90.4 bps` | `-0.027 / -0.029` | `0.76%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 13:45:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,882.00 | ⚪ **CASH** | **-2.4 bps** (±20.0) | `-14.4 bps` | `-0.014 / +0.240` | `0.58%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,237.46 | ⚪ **CASH** | **-5.0 bps** (±8.3) | `-8.7 bps` | `-0.047 / +0.100` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.34 | ⚪ **CASH** | **-69.9 bps** (±19.4) | `-120.1 bps` | `-0.018 / -0.017` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 13:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,888.00 | ⚪ **CASH** | **-2.4 bps** (±20.0) | `-14.4 bps` | `-0.014 / +0.240` | `0.58%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.51 | ⚪ **CASH** | **-5.0 bps** (±8.3) | `-8.7 bps` | `-0.047 / +0.100` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.19 | ⚪ **CASH** | **-69.9 bps** (±19.4) | `-120.1 bps` | `-0.018 / -0.017` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 13:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,897.42 | ⚪ **CASH** | **-2.4 bps** (±20.0) | `-14.4 bps` | `-0.014 / +0.240` | `0.58%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.10 | ⚪ **CASH** | **-5.0 bps** (±8.3) | `-8.7 bps` | `-0.047 / +0.100` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.05 | ⚪ **CASH** | **-69.9 bps** (±19.4) | `-120.1 bps` | `-0.018 / -0.017` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 13:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,992.01 | ⚪ **CASH** | **-2.4 bps** (±20.0) | `-14.4 bps` | `-0.014 / +0.240` | `0.58%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,237.37 | ⚪ **CASH** | **-5.0 bps** (±8.3) | `-8.7 bps` | `-0.047 / +0.100` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.13 | ⚪ **CASH** | **-69.9 bps** (±19.4) | `-120.1 bps` | `-0.018 / -0.017` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 12:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,231.99 | ⚪ **CASH** | **+19.7 bps** (±28.1) | `+26.4 bps` | `-0.019 / +0.265` | `0.59%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,244.50 | ⚪ **CASH** | **+1.3 bps** (±5.4) | `+0.2 bps` | `-0.047 / +0.134` | `0.78%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.68 | ⚪ **CASH** | **-64.4 bps** (±20.8) | `-109.1 bps` | `-0.028 / -0.008` | `0.78%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 12:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,310.00 | ⚪ **CASH** | **+19.7 bps** (±28.1) | `+26.4 bps` | `-0.019 / +0.265` | `0.59%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,248.95 | ⚪ **CASH** | **+1.3 bps** (±5.4) | `+0.2 bps` | `-0.047 / +0.134` | `0.78%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.86 | ⚪ **CASH** | **-64.4 bps** (±20.8) | `-109.1 bps` | `-0.028 / -0.008` | `0.78%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 12:15:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,164.00 | ⚪ **CASH** | **+19.7 bps** (±28.1) | `+26.4 bps` | `-0.019 / +0.265` | `0.59%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,243.42 | ⚪ **CASH** | **+1.3 bps** (±5.4) | `+0.2 bps` | `-0.047 / +0.134` | `0.78%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.51 | ⚪ **CASH** | **-64.4 bps** (±20.8) | `-109.1 bps` | `-0.028 / -0.008` | `0.78%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 12:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,104.01 | ⚪ **CASH** | **+19.7 bps** (±28.1) | `+26.4 bps` | `-0.019 / +0.265` | `0.59%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,241.84 | ⚪ **CASH** | **+1.3 bps** (±5.4) | `+0.2 bps` | `-0.047 / +0.134` | `0.78%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.37 | ⚪ **CASH** | **-64.4 bps** (±20.8) | `-109.1 bps` | `-0.028 / -0.008` | `0.78%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 11:45:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,174.50 | ⚪ **CASH** | **+11.7 bps** (±30.7) | `+13.5 bps` | `-0.018 / +0.246` | `0.60%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,246.01 | ⚪ **CASH** | **+14.2 bps** (±6.2) | `+22.1 bps` | `-0.044 / +0.154` | `0.79%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.51 | ⚪ **CASH** | **-68.3 bps** (±24.4) | `-114.9 bps` | `-0.031 / -0.015` | `0.79%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 11:30:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,102.01 | ⚪ **CASH** | **+11.7 bps** (±30.7) | `+13.5 bps` | `-0.018 / +0.246` | `0.60%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,240.14 | ⚪ **CASH** | **+14.2 bps** (±6.2) | `+22.1 bps` | `-0.044 / +0.154` | `0.79%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.31 | ⚪ **CASH** | **-68.3 bps** (±24.4) | `-114.9 bps` | `-0.031 / -0.015` | `0.79%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 11:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,026.79 | ⚪ **CASH** | **+11.7 bps** (±30.7) | `+13.5 bps` | `-0.018 / +0.246` | `0.60%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.61 | ⚪ **CASH** | **+14.2 bps** (±6.2) | `+22.1 bps` | `-0.044 / +0.154` | `0.79%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.07 | ⚪ **CASH** | **-68.3 bps** (±24.4) | `-114.9 bps` | `-0.031 / -0.015` | `0.79%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 11:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,023.66 | ⚪ **CASH** | **+11.7 bps** (±30.7) | `+13.5 bps` | `-0.018 / +0.246` | `0.60%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.21 | ⚪ **CASH** | **+14.2 bps** (±6.2) | `+22.1 bps` | `-0.044 / +0.154` | `0.79%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.98 | ⚪ **CASH** | **-68.3 bps** (±24.4) | `-114.9 bps` | `-0.031 / -0.015` | `0.79%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 10:45:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,239.99 | ⚪ **CASH** | **+8.8 bps** (±21.8) | `+10.8 bps` | `-0.023 / +0.191` | `0.60%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,241.34 | ⚪ **CASH** | **+0.9 bps** (±7.0) | `+0.1 bps` | `-0.047 / +0.130` | `0.80%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.19 | ⚪ **CASH** | **-70.7 bps** (±26.7) | `-117.6 bps` | `-0.032 / -0.029` | `0.80%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 10:31:00 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,164.01 | ⚪ **CASH** | **+8.8 bps** (±21.8) | `+10.8 bps` | `-0.023 / +0.191` | `0.60%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,239.08 | ⚪ **CASH** | **+0.9 bps** (±7.0) | `+0.1 bps` | `-0.047 / +0.130` | `0.80%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.14 | ⚪ **CASH** | **-70.7 bps** (±26.7) | `-117.6 bps` | `-0.032 / -0.029` | `0.80%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 10:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,177.16 | ⚪ **CASH** | **+8.8 bps** (±21.8) | `+10.8 bps` | `-0.023 / +0.191` | `0.60%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.87 | ⚪ **CASH** | **+0.9 bps** (±7.0) | `+0.1 bps` | `-0.047 / +0.130` | `0.80%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.16 | ⚪ **CASH** | **-70.7 bps** (±26.7) | `-117.6 bps` | `-0.032 / -0.029` | `0.80%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 10:00:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,187.84 | ⚪ **CASH** | **+8.8 bps** (±21.8) | `+10.8 bps` | `-0.023 / +0.191` | `0.60%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,239.10 | ⚪ **CASH** | **+0.9 bps** (±7.0) | `+0.1 bps` | `-0.047 / +0.130` | `0.80%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.09 | ⚪ **CASH** | **-70.7 bps** (±26.7) | `-117.6 bps` | `-0.032 / -0.029` | `0.80%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 09:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,100.00 | ⚪ **CASH** | **+10.5 bps** (±22.2) | `+17.6 bps` | `-0.037 / +0.168` | `0.60%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,239.47 | ⚪ **CASH** | **-2.4 bps** (±19.9) | `+0.4 bps` | `-0.067 / +0.112` | `0.80%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.18 | ⚪ **CASH** | **-54.9 bps** (±34.1) | `-84.3 bps` | `-0.037 / -0.061` | `0.80%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 09:30:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,199.59 | ⚪ **CASH** | **+10.5 bps** (±22.2) | `+17.6 bps` | `-0.037 / +0.168` | `0.60%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,244.65 | ⚪ **CASH** | **-2.4 bps** (±19.9) | `+0.4 bps` | `-0.067 / +0.112` | `0.80%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.31 | ⚪ **CASH** | **-54.9 bps** (±34.1) | `-84.3 bps` | `-0.037 / -0.061` | `0.80%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 09:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,178.00 | ⚪ **CASH** | **+10.5 bps** (±22.2) | `+17.6 bps` | `-0.037 / +0.168` | `0.60%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,243.94 | ⚪ **CASH** | **-2.4 bps** (±19.9) | `+0.4 bps` | `-0.067 / +0.112` | `0.80%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.22 | ⚪ **CASH** | **-54.9 bps** (±34.1) | `-84.3 bps` | `-0.037 / -0.061` | `0.80%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 09:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,736.01 | ⚪ **CASH** | **+10.5 bps** (±22.2) | `+17.6 bps` | `-0.037 / +0.168` | `0.60%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,228.95 | ⚪ **CASH** | **-2.4 bps** (±19.9) | `+0.4 bps` | `-0.067 / +0.112` | `0.80%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.66 | ⚪ **CASH** | **-54.9 bps** (±34.1) | `-84.3 bps` | `-0.037 / -0.061` | `0.80%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 08:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,711.52 | ⚪ **CASH** | **+2.7 bps** (±26.1) | `+12.2 bps` | `-0.059 / +0.093` | `0.61%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,229.90 | ⚪ **CASH** | **-50.3 bps** (±27.4) | `-77.2 bps` | `-0.093 / +0.042` | `0.81%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.82 | ⚪ **CASH** | **-57.1 bps** (±39.2) | `-82.5 bps` | `-0.038 / -0.116` | `0.81%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 08:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,628.14 | ⚪ **CASH** | **+2.7 bps** (±26.1) | `+12.2 bps` | `-0.059 / +0.093` | `0.61%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,226.47 | ⚪ **CASH** | **-50.3 bps** (±27.4) | `-77.2 bps` | `-0.093 / +0.042` | `0.81%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.67 | ⚪ **CASH** | **-57.1 bps** (±39.2) | `-82.5 bps` | `-0.038 / -0.116` | `0.81%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 08:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,729.60 | ⚪ **CASH** | **+2.7 bps** (±26.1) | `+12.2 bps` | `-0.059 / +0.093` | `0.61%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,231.89 | ⚪ **CASH** | **-50.3 bps** (±27.4) | `-77.2 bps` | `-0.093 / +0.042` | `0.81%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.83 | ⚪ **CASH** | **-57.1 bps** (±39.2) | `-82.5 bps` | `-0.038 / -0.116` | `0.81%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 08:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,561.17 | ⚪ **CASH** | **+2.7 bps** (±26.1) | `+12.2 bps` | `-0.059 / +0.093` | `0.61%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,224.62 | ⚪ **CASH** | **-50.3 bps** (±27.4) | `-77.2 bps` | `-0.093 / +0.042` | `0.81%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.59 | ⚪ **CASH** | **-57.1 bps** (±39.2) | `-82.5 bps` | `-0.038 / -0.116` | `0.81%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 07:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,783.21 | ⚪ **CASH** | **-1.3 bps** (±29.0) | `+17.2 bps` | `-0.088 / -0.019` | `0.62%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,232.78 | ⚪ **CASH** | **-49.6 bps** (±31.9) | `-67.3 bps` | `-0.115 / -0.023` | `0.83%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.73 | ⚪ **CASH** | **-58.7 bps** (±37.3) | `-91.2 bps` | `-0.030 / -0.024` | `0.83%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 07:30:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,345.89 | ⚪ **CASH** | **-1.3 bps** (±29.0) | `+17.2 bps` | `-0.088 / -0.019` | `0.62%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,215.16 | ⚪ **CASH** | **-49.6 bps** (±31.9) | `-67.3 bps` | `-0.115 / -0.023` | `0.83%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.32 | ⚪ **CASH** | **-58.7 bps** (±37.3) | `-91.2 bps` | `-0.030 / -0.024` | `0.83%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 07:15:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,446.48 | ⚪ **CASH** | **-1.3 bps** (±29.0) | `+17.2 bps` | `-0.088 / -0.019` | `0.62%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,223.31 | ⚪ **CASH** | **-49.6 bps** (±31.9) | `-67.3 bps` | `-0.115 / -0.023` | `0.83%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.54 | ⚪ **CASH** | **-58.7 bps** (±37.3) | `-91.2 bps` | `-0.030 / -0.024` | `0.83%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 07:00:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,705.03 | ⚪ **CASH** | **-1.3 bps** (±29.0) | `+17.2 bps` | `-0.088 / -0.019` | `0.62%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,227.81 | ⚪ **CASH** | **-49.6 bps** (±31.9) | `-67.3 bps` | `-0.115 / -0.023` | `0.83%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.62 | ⚪ **CASH** | **-58.7 bps** (±37.3) | `-91.2 bps` | `-0.030 / -0.024` | `0.83%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 06:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,721.00 | ⚪ **CASH** | **+9.4 bps** (±16.7) | `+36.2 bps` | `-0.092 / -0.040` | `0.62%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,231.06 | ⚪ **CASH** | **-46.3 bps** (±31.8) | `-62.7 bps` | `-0.119 / +0.007` | `0.84%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.83 | ⚪ **CASH** | **-53.7 bps** (±34.5) | `-83.6 bps` | `-0.028 / -0.008` | `0.84%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
