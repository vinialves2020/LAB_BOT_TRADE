# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-09 09:00:50 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-09 09:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,536.58 | ⚪ **CASH** | **+0.8 bps** (±5.4) | `+2.2 bps` | `-0.009 / +0.024` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,121.89 | ⚪ **CASH** | **-55.1 bps** (±11.2) | `-63.2 bps` | `-0.172 / -0.270` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.94 | ⚪ **CASH** | **-13.5 bps** (±12.5) | `-25.6 bps` | `+0.035 / +0.004` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 08:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,285.91 | ⚪ **CASH** | **-16.8 bps** (±4.2) | `-20.7 bps` | `-0.039 / -0.052` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,113.37 | ⚪ **CASH** | **-48.9 bps** (±15.5) | `-46.0 bps` | `-0.182 / -0.311` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.51 | ⚪ **CASH** | **-19.4 bps** (±18.3) | `-30.5 bps` | `+0.025 / -0.032` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 08:30:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,203.14 | ⚪ **CASH** | **-16.8 bps** (±4.2) | `-20.7 bps` | `-0.039 / -0.052` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,109.12 | ⚪ **CASH** | **-48.9 bps** (±15.5) | `-46.0 bps` | `-0.182 / -0.311` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.36 | ⚪ **CASH** | **-19.4 bps** (±18.3) | `-30.5 bps` | `+0.025 / -0.032` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 08:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,912.00 | ⚪ **CASH** | **-16.8 bps** (±4.2) | `-20.7 bps` | `-0.039 / -0.052` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,096.00 | ⚪ **CASH** | **-48.9 bps** (±15.5) | `-46.0 bps` | `-0.182 / -0.311` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.97 | ⚪ **CASH** | **-19.4 bps** (±18.3) | `-30.5 bps` | `+0.025 / -0.032` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 08:00:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,920.01 | ⚪ **CASH** | **-16.8 bps** (±4.2) | `-20.7 bps` | `-0.039 / -0.052` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,094.97 | ⚪ **CASH** | **-48.9 bps** (±15.5) | `-46.0 bps` | `-0.182 / -0.311` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.65 | ⚪ **CASH** | **-19.4 bps** (±18.3) | `-30.5 bps` | `+0.025 / -0.032` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 07:45:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,885.44 | ⚪ **CASH** | **-16.2 bps** (±5.3) | `-20.8 bps` | `-0.028 / -0.053` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,087.78 | ⚪ **CASH** | **-75.6 bps** (±19.7) | `-94.7 bps` | `-0.164 / -0.330` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.40 | ⚪ **CASH** | **-22.3 bps** (±19.9) | `-38.6 bps` | `+0.033 / -0.005` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 07:30:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,958.00 | ⚪ **CASH** | **-16.2 bps** (±5.3) | `-20.8 bps` | `-0.028 / -0.053` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,088.26 | ⚪ **CASH** | **-75.6 bps** (±19.7) | `-94.7 bps` | `-0.164 / -0.330` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.46 | ⚪ **CASH** | **-22.3 bps** (±19.9) | `-38.6 bps` | `+0.033 / -0.005` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 07:15:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,025.15 | ⚪ **CASH** | **-16.2 bps** (±5.3) | `-20.8 bps` | `-0.028 / -0.053` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,092.11 | ⚪ **CASH** | **-75.6 bps** (±19.7) | `-94.7 bps` | `-0.164 / -0.330` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.52 | ⚪ **CASH** | **-22.3 bps** (±19.9) | `-38.6 bps` | `+0.033 / -0.005` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 07:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,386.00 | ⚪ **CASH** | **-16.2 bps** (±5.3) | `-20.8 bps` | `-0.028 / -0.053` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,115.05 | ⚪ **CASH** | **-75.6 bps** (±19.7) | `-94.7 bps` | `-0.164 / -0.330` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.12 | ⚪ **CASH** | **-22.3 bps** (±19.9) | `-38.6 bps` | `+0.033 / -0.005` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 06:45:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,138.02 | ⚪ **CASH** | **-10.5 bps** (±6.0) | `-16.7 bps` | `-0.013 / +0.010` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,108.97 | ⚪ **CASH** | **-63.8 bps** (±18.9) | `-79.8 bps` | `-0.148 / -0.268` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.01 | ⚪ **CASH** | **-15.7 bps** (±19.4) | `-32.8 bps` | `+0.046 / +0.059` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 06:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,318.01 | ⚪ **CASH** | **-10.5 bps** (±6.0) | `-16.7 bps` | `-0.013 / +0.010` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,120.24 | ⚪ **CASH** | **-63.8 bps** (±18.9) | `-79.8 bps` | `-0.148 / -0.268` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.38 | ⚪ **CASH** | **-15.7 bps** (±19.4) | `-32.8 bps` | `+0.046 / +0.059` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 06:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,481.07 | ⚪ **CASH** | **-10.5 bps** (±6.0) | `-16.7 bps` | `-0.013 / +0.010` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,128.33 | ⚪ **CASH** | **-63.8 bps** (±18.9) | `-79.8 bps` | `-0.148 / -0.268` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.41 | ⚪ **CASH** | **-15.7 bps** (±19.4) | `-32.8 bps` | `+0.046 / +0.059` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 06:00:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,516.08 | ⚪ **CASH** | **-10.5 bps** (±6.0) | `-16.7 bps` | `-0.013 / +0.010` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,130.54 | ⚪ **CASH** | **-63.8 bps** (±18.9) | `-79.8 bps` | `-0.148 / -0.268` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.72 | ⚪ **CASH** | **-15.7 bps** (±19.4) | `-32.8 bps` | `+0.046 / +0.059` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 05:45:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,422.90 | ⚪ **CASH** | **-11.7 bps** (±13.1) | `-18.4 bps` | `-0.019 / +0.035` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,130.04 | ⚪ **CASH** | **-61.9 bps** (±17.4) | `-84.1 bps` | `-0.131 / -0.175` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.87 | ⚪ **CASH** | **-7.7 bps** (±11.3) | `-25.4 bps` | `+0.059 / +0.130` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 05:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,558.64 | ⚪ **CASH** | **-11.7 bps** (±13.1) | `-18.4 bps` | `-0.019 / +0.035` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,133.94 | ⚪ **CASH** | **-61.9 bps** (±17.4) | `-84.1 bps` | `-0.131 / -0.175` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.12 | ⚪ **CASH** | **-7.7 bps** (±11.3) | `-25.4 bps` | `+0.059 / +0.130` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 05:15:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,597.92 | ⚪ **CASH** | **-11.7 bps** (±13.1) | `-18.4 bps` | `-0.019 / +0.035` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,138.01 | ⚪ **CASH** | **-61.9 bps** (±17.4) | `-84.1 bps` | `-0.131 / -0.175` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.16 | ⚪ **CASH** | **-7.7 bps** (±11.3) | `-25.4 bps` | `+0.059 / +0.130` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 05:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,780.32 | ⚪ **CASH** | **-11.7 bps** (±13.1) | `-18.4 bps` | `-0.019 / +0.035` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,137.97 | ⚪ **CASH** | **-61.9 bps** (±17.4) | `-84.1 bps` | `-0.131 / -0.175` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.34 | ⚪ **CASH** | **-7.7 bps** (±11.3) | `-25.4 bps` | `+0.059 / +0.130` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 04:45:35 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,974.00 | ⚪ **CASH** | **-10.3 bps** (±8.9) | `-17.2 bps` | `-0.021 / +0.051` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,141.08 | ⚪ **CASH** | **-55.6 bps** (±12.9) | `-81.3 bps` | `-0.117 / -0.076` | `0.78%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.55 | ⚪ **CASH** | **-1.5 bps** (±10.9) | `-12.0 bps` | `+0.053 / +0.107` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 04:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,964.00 | ⚪ **CASH** | **-10.3 bps** (±8.9) | `-17.2 bps` | `-0.021 / +0.051` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,141.53 | ⚪ **CASH** | **-55.6 bps** (±12.9) | `-81.3 bps` | `-0.117 / -0.076` | `0.78%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.46 | ⚪ **CASH** | **-1.5 bps** (±10.9) | `-12.0 bps` | `+0.053 / +0.107` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 04:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,003.53 | ⚪ **CASH** | **-10.3 bps** (±8.9) | `-17.2 bps` | `-0.021 / +0.051` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,145.01 | ⚪ **CASH** | **-55.6 bps** (±12.9) | `-81.3 bps` | `-0.117 / -0.076` | `0.78%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.68 | ⚪ **CASH** | **-1.5 bps** (±10.9) | `-12.0 bps` | `+0.053 / +0.107` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 04:00:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,876.81 | ⚪ **CASH** | **-10.3 bps** (±8.9) | `-17.2 bps` | `-0.021 / +0.051` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,142.27 | ⚪ **CASH** | **-55.6 bps** (±12.9) | `-81.3 bps` | `-0.117 / -0.076` | `0.78%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.58 | ⚪ **CASH** | **-1.5 bps** (±10.9) | `-12.0 bps` | `+0.053 / +0.107` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 03:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,043.45 | ⚪ **CASH** | **-18.1 bps** (±6.6) | `-28.4 bps` | `-0.016 / -0.015` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,145.00 | ⚪ **CASH** | **-41.8 bps** (±23.7) | `-51.7 bps` | `-0.112 / -0.126` | `0.79%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.77 | ⚪ **CASH** | **-3.4 bps** (±7.3) | `-10.7 bps` | `+0.049 / +0.029` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 03:30:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,046.01 | ⚪ **CASH** | **-18.1 bps** (±6.6) | `-28.4 bps` | `-0.016 / -0.015` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,143.73 | ⚪ **CASH** | **-41.8 bps** (±23.7) | `-51.7 bps` | `-0.112 / -0.126` | `0.79%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.78 | ⚪ **CASH** | **-3.4 bps** (±7.3) | `-10.7 bps` | `+0.049 / +0.029` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 03:15:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,918.72 | ⚪ **CASH** | **-18.1 bps** (±6.6) | `-28.4 bps` | `-0.016 / -0.015` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,136.80 | ⚪ **CASH** | **-41.8 bps** (±23.7) | `-51.7 bps` | `-0.112 / -0.126` | `0.79%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.24 | ⚪ **CASH** | **-3.4 bps** (±7.3) | `-10.7 bps` | `+0.049 / +0.029` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 03:00:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,282.01 | ⚪ **CASH** | **-18.1 bps** (±6.6) | `-28.4 bps` | `-0.016 / -0.015` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,147.72 | ⚪ **CASH** | **-41.8 bps** (±23.7) | `-51.7 bps` | `-0.112 / -0.126` | `0.79%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $88.08 | ⚪ **CASH** | **-3.4 bps** (±7.3) | `-10.7 bps` | `+0.049 / +0.029` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 02:45:34 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,449.53 | ⚪ **CASH** | **-19.5 bps** (±6.5) | `-28.3 bps` | `-0.025 / -0.033` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,155.77 | ⚪ **CASH** | **-46.4 bps** (±18.1) | `-59.2 bps` | `-0.118 / -0.138` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $88.33 | ⚪ **CASH** | **-5.8 bps** (±8.0) | `-14.0 bps` | `+0.045 / +0.028` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 02:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,512.01 | ⚪ **CASH** | **-19.5 bps** (±6.5) | `-28.3 bps` | `-0.025 / -0.033` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,155.20 | ⚪ **CASH** | **-46.4 bps** (±18.1) | `-59.2 bps` | `-0.118 / -0.138` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $88.24 | ⚪ **CASH** | **-5.8 bps** (±8.0) | `-14.0 bps` | `+0.045 / +0.028` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 02:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,216.01 | ⚪ **CASH** | **-19.5 bps** (±6.5) | `-28.3 bps` | `-0.025 / -0.033` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,144.81 | ⚪ **CASH** | **-46.4 bps** (±18.1) | `-59.2 bps` | `-0.118 / -0.138` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.88 | ⚪ **CASH** | **-5.8 bps** (±8.0) | `-14.0 bps` | `+0.045 / +0.028` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 02:00:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,137.43 | ⚪ **CASH** | **-19.5 bps** (±6.5) | `-28.3 bps` | `-0.025 / -0.033` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,141.12 | ⚪ **CASH** | **-46.4 bps** (±18.1) | `-59.2 bps` | `-0.118 / -0.138` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.73 | ⚪ **CASH** | **-5.8 bps** (±8.0) | `-14.0 bps` | `+0.045 / +0.028` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 01:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,196.01 | ⚪ **CASH** | **-20.6 bps** (±7.1) | `-31.1 bps` | `-0.016 / -0.042` | `0.43%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,143.39 | ⚪ **CASH** | **-32.1 bps** (±22.1) | `-35.4 bps` | `-0.104 / -0.121` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.97 | ⚪ **CASH** | **-5.5 bps** (±6.8) | `-13.0 bps` | `+0.040 / +0.018` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 01:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,797.51 | ⚪ **CASH** | **-20.6 bps** (±7.1) | `-31.1 bps` | `-0.016 / -0.042` | `0.43%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,127.41 | ⚪ **CASH** | **-32.1 bps** (±22.1) | `-35.4 bps` | `-0.104 / -0.121` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.07 | ⚪ **CASH** | **-5.5 bps** (±6.8) | `-13.0 bps` | `+0.040 / +0.018` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 01:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,089.39 | ⚪ **CASH** | **-20.6 bps** (±7.1) | `-31.1 bps` | `-0.016 / -0.042` | `0.43%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,134.50 | ⚪ **CASH** | **-32.1 bps** (±22.1) | `-35.4 bps` | `-0.104 / -0.121` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.34 | ⚪ **CASH** | **-5.5 bps** (±6.8) | `-13.0 bps` | `+0.040 / +0.018` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 01:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,275.37 | ⚪ **CASH** | **-20.6 bps** (±7.1) | `-31.1 bps` | `-0.016 / -0.042` | `0.43%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,145.14 | ⚪ **CASH** | **-32.1 bps** (±22.1) | `-35.4 bps` | `-0.104 / -0.121` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.66 | ⚪ **CASH** | **-5.5 bps** (±6.8) | `-13.0 bps` | `+0.040 / +0.018` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 00:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,039.42 | ⚪ **CASH** | **-22.5 bps** (±11.2) | `-33.5 bps` | `-0.020 / -0.039` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,138.22 | ⚪ **CASH** | **-36.7 bps** (±26.2) | `-44.4 bps` | `-0.094 / -0.112` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.08 | ⚪ **CASH** | **-11.7 bps** (±14.9) | `-22.4 bps` | `+0.034 / +0.022` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 00:30:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,008.01 | ⚪ **CASH** | **-22.5 bps** (±11.2) | `-33.5 bps` | `-0.020 / -0.039` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,141.09 | ⚪ **CASH** | **-36.7 bps** (±26.2) | `-44.4 bps` | `-0.094 / -0.112` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.05 | ⚪ **CASH** | **-11.7 bps** (±14.9) | `-22.4 bps` | `+0.034 / +0.022` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 00:15:35 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,020.00 | ⚪ **CASH** | **-22.5 bps** (±11.2) | `-33.5 bps` | `-0.020 / -0.039` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,140.22 | ⚪ **CASH** | **-36.7 bps** (±26.2) | `-44.4 bps` | `-0.094 / -0.112` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.29 | ⚪ **CASH** | **-11.7 bps** (±14.9) | `-22.4 bps` | `+0.034 / +0.022` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
