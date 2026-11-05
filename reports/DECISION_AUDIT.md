# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-05 09:00:57 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-05 09:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,494.16 | ⚪ **CASH** | **-2.3 bps** (±2.2) | `+11.5 bps` | `+0.012 / -0.262` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,419.70 | ⚪ **CASH** | **-22.9 bps** (±4.6) | `-22.7 bps` | `-0.020 / -0.255` | `0.60%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.80 | ⚪ **CASH** | **-20.3 bps** (±5.8) | `-44.7 bps` | `+0.074 / +0.014` | `0.66%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 08:46:15 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,503.35 | ⚪ **CASH** | **-2.0 bps** (±4.3) | `+10.1 bps` | `+0.028 / -0.263` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,420.34 | ⚪ **CASH** | **-23.5 bps** (±4.7) | `-27.6 bps` | `-0.008 / -0.229` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.59 | ⚪ **CASH** | **-17.5 bps** (±7.1) | `-38.9 bps` | `+0.081 / -0.013` | `0.65%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 08:31:26 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,566.50 | ⚪ **CASH** | **-2.0 bps** (±4.3) | `+10.1 bps` | `+0.028 / -0.263` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,424.31 | ⚪ **CASH** | **-23.5 bps** (±4.7) | `-27.6 bps` | `-0.008 / -0.229` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.76 | ⚪ **CASH** | **-17.5 bps** (±7.1) | `-38.9 bps` | `+0.081 / -0.013` | `0.65%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 08:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,522.01 | ⚪ **CASH** | **-2.0 bps** (±4.3) | `+10.1 bps` | `+0.028 / -0.263` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,421.86 | ⚪ **CASH** | **-23.5 bps** (±4.7) | `-27.6 bps` | `-0.008 / -0.229` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.11 | ⚪ **CASH** | **-17.5 bps** (±7.1) | `-38.9 bps` | `+0.081 / -0.013` | `0.65%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 08:00:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,387.79 | ⚪ **CASH** | **-2.0 bps** (±4.3) | `+10.1 bps` | `+0.028 / -0.263` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,418.53 | ⚪ **CASH** | **-23.5 bps** (±4.7) | `-27.6 bps` | `-0.008 / -0.229` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.98 | ⚪ **CASH** | **-17.5 bps** (±7.1) | `-38.9 bps` | `+0.081 / -0.013` | `0.65%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 07:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,396.56 | ⚪ **CASH** | **+5.7 bps** (±4.3) | `+12.8 bps` | `+0.054 / -0.147` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,415.49 | ⚪ **CASH** | **-16.5 bps** (±3.9) | `-23.3 bps` | `+0.010 / -0.145` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.95 | ⚪ **CASH** | **-17.8 bps** (±4.3) | `-39.9 bps` | `+0.080 / -0.035` | `0.65%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 07:31:22 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,462.85 | ⚪ **CASH** | **+5.7 bps** (±4.3) | `+12.8 bps` | `+0.054 / -0.147` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,419.93 | ⚪ **CASH** | **-16.5 bps** (±3.9) | `-23.3 bps` | `+0.010 / -0.145` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.89 | ⚪ **CASH** | **-17.8 bps** (±4.3) | `-39.9 bps` | `+0.080 / -0.035` | `0.65%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 07:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,655.99 | ⚪ **CASH** | **+5.7 bps** (±4.3) | `+12.8 bps` | `+0.054 / -0.147` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,428.74 | ⚪ **CASH** | **-16.5 bps** (±3.9) | `-23.3 bps` | `+0.010 / -0.145` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.21 | ⚪ **CASH** | **-17.8 bps** (±4.3) | `-39.9 bps` | `+0.080 / -0.035` | `0.65%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 07:01:28 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,645.99 | ⚪ **CASH** | **+5.7 bps** (±4.3) | `+12.8 bps` | `+0.054 / -0.147` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,429.68 | ⚪ **CASH** | **-16.5 bps** (±3.9) | `-23.3 bps` | `+0.010 / -0.145` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.22 | ⚪ **CASH** | **-17.8 bps** (±4.3) | `-39.9 bps` | `+0.080 / -0.035` | `0.65%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 06:45:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,527.68 | ⚪ **CASH** | **+2.7 bps** (±3.8) | `+7.3 bps` | `+0.056 / -0.154` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,426.16 | ⚪ **CASH** | **-16.6 bps** (±3.3) | `-22.2 bps` | `+0.004 / -0.160` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.04 | ⚪ **CASH** | **-16.4 bps** (±6.3) | `-38.6 bps` | `+0.080 / -0.010` | `0.66%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 06:31:22 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,544.00 | ⚪ **CASH** | **+2.7 bps** (±3.8) | `+7.3 bps` | `+0.056 / -0.154` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,426.89 | ⚪ **CASH** | **-16.6 bps** (±3.3) | `-22.2 bps` | `+0.004 / -0.160` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.02 | ⚪ **CASH** | **-16.4 bps** (±6.3) | `-38.6 bps` | `+0.080 / -0.010` | `0.66%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 06:16:13 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,543.36 | ⚪ **CASH** | **+2.7 bps** (±3.8) | `+7.3 bps` | `+0.056 / -0.154` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,426.64 | ⚪ **CASH** | **-16.6 bps** (±3.3) | `-22.2 bps` | `+0.004 / -0.160` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.13 | ⚪ **CASH** | **-16.4 bps** (±6.3) | `-38.6 bps` | `+0.080 / -0.010` | `0.66%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 06:01:21 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,436.01 | ⚪ **CASH** | **+2.7 bps** (±3.8) | `+7.3 bps` | `+0.056 / -0.154` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,420.29 | ⚪ **CASH** | **-16.6 bps** (±3.3) | `-22.2 bps` | `+0.004 / -0.160` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.82 | ⚪ **CASH** | **-16.4 bps** (±6.3) | `-38.6 bps` | `+0.080 / -0.010` | `0.66%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 05:46:33 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,398.07 | ⚪ **CASH** | **+4.6 bps** (±3.7) | `+9.0 bps` | `+0.064 / -0.145` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,419.61 | ⚪ **CASH** | **-21.2 bps** (±5.7) | `-30.5 bps` | `+0.009 / -0.170` | `0.62%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.82 | ⚪ **CASH** | **-12.6 bps** (±5.0) | `-37.2 bps` | `+0.088 / +0.053` | `0.66%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 05:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,442.00 | ⚪ **CASH** | **+4.6 bps** (±3.7) | `+9.0 bps` | `+0.064 / -0.145` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,423.49 | ⚪ **CASH** | **-21.2 bps** (±5.7) | `-30.5 bps` | `+0.009 / -0.170` | `0.62%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.98 | ⚪ **CASH** | **-12.6 bps** (±5.0) | `-37.2 bps` | `+0.088 / +0.053` | `0.66%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 05:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,463.88 | ⚪ **CASH** | **+4.6 bps** (±3.7) | `+9.0 bps` | `+0.064 / -0.145` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,425.54 | ⚪ **CASH** | **-21.2 bps** (±5.7) | `-30.5 bps` | `+0.009 / -0.170` | `0.62%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.92 | ⚪ **CASH** | **-12.6 bps** (±5.0) | `-37.2 bps` | `+0.088 / +0.053` | `0.66%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 05:01:31 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,464.23 | ⚪ **CASH** | **+4.6 bps** (±3.7) | `+9.0 bps` | `+0.064 / -0.145` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,422.55 | ⚪ **CASH** | **-21.2 bps** (±5.7) | `-30.5 bps` | `+0.009 / -0.170` | `0.62%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.93 | ⚪ **CASH** | **-12.6 bps** (±5.0) | `-37.2 bps` | `+0.088 / +0.053` | `0.66%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 04:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,718.01 | ⚪ **CASH** | **-9.2 bps** (±5.6) | `-20.0 bps` | `+0.073 / -0.099` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,431.59 | ⚪ **CASH** | **-25.6 bps** (±10.0) | `-41.8 bps` | `+0.015 / -0.121` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.50 | ⚪ **CASH** | **-9.1 bps** (±5.4) | `-34.8 bps` | `+0.091 / +0.102` | `0.67%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 04:31:17 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,474.01 | ⚪ **CASH** | **-9.2 bps** (±5.6) | `-20.0 bps` | `+0.073 / -0.099` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,424.72 | ⚪ **CASH** | **-25.6 bps** (±10.0) | `-41.8 bps` | `+0.015 / -0.121` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.16 | ⚪ **CASH** | **-9.1 bps** (±5.4) | `-34.8 bps` | `+0.091 / +0.102` | `0.67%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 04:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,450.01 | ⚪ **CASH** | **-9.2 bps** (±5.6) | `-20.0 bps` | `+0.073 / -0.099` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,421.00 | ⚪ **CASH** | **-25.6 bps** (±10.0) | `-41.8 bps` | `+0.015 / -0.121` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.03 | ⚪ **CASH** | **-9.1 bps** (±5.4) | `-34.8 bps` | `+0.091 / +0.102` | `0.67%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 04:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,519.76 | ⚪ **CASH** | **-9.2 bps** (±5.6) | `-20.0 bps` | `+0.073 / -0.099` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,422.87 | ⚪ **CASH** | **-25.6 bps** (±10.0) | `-41.8 bps` | `+0.015 / -0.121` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.19 | ⚪ **CASH** | **-9.1 bps** (±5.4) | `-34.8 bps` | `+0.091 / +0.102` | `0.67%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 03:45:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,686.53 | ⚪ **CASH** | **-7.3 bps** (±8.0) | `-17.8 bps` | `+0.071 / -0.070` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,429.80 | ⚪ **CASH** | **-20.1 bps** (±7.5) | `-32.2 bps` | `+0.008 / -0.109` | `0.64%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.78 | ⚪ **CASH** | **-4.9 bps** (±3.3) | `-27.2 bps` | `+0.086 / +0.106` | `0.68%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 03:30:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,696.85 | ⚪ **CASH** | **-7.3 bps** (±8.0) | `-17.8 bps` | `+0.071 / -0.070` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,431.27 | ⚪ **CASH** | **-20.1 bps** (±7.5) | `-32.2 bps` | `+0.008 / -0.109` | `0.64%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.69 | ⚪ **CASH** | **-4.9 bps** (±3.3) | `-27.2 bps` | `+0.086 / +0.106` | `0.68%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 03:16:07 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,662.01 | ⚪ **CASH** | **-7.3 bps** (±8.0) | `-17.8 bps` | `+0.071 / -0.070` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,432.94 | ⚪ **CASH** | **-20.1 bps** (±7.5) | `-32.2 bps` | `+0.008 / -0.109` | `0.64%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.67 | ⚪ **CASH** | **-4.9 bps** (±3.3) | `-27.2 bps` | `+0.086 / +0.106` | `0.68%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 03:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,559.32 | ⚪ **CASH** | **-7.3 bps** (±8.0) | `-17.8 bps` | `+0.071 / -0.070` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,427.93 | ⚪ **CASH** | **-20.1 bps** (±7.5) | `-32.2 bps` | `+0.008 / -0.109` | `0.64%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.32 | ⚪ **CASH** | **-4.9 bps** (±3.3) | `-27.2 bps` | `+0.086 / +0.106` | `0.68%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 02:46:22 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,630.01 | ⚪ **CASH** | **-0.6 bps** (±8.1) | `-7.1 bps` | `+0.071 / -0.046` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,431.57 | ⚪ **CASH** | **-15.3 bps** (±10.4) | `-22.2 bps` | `+0.001 / -0.110` | `0.64%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.43 | ⚪ **CASH** | **-6.6 bps** (±9.7) | `-28.4 bps` | `+0.083 / +0.098` | `0.69%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 02:31:18 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,660.01 | ⚪ **CASH** | **-0.6 bps** (±8.1) | `-7.1 bps` | `+0.071 / -0.046` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,429.61 | ⚪ **CASH** | **-15.3 bps** (±10.4) | `-22.2 bps` | `+0.001 / -0.110` | `0.64%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.21 | ⚪ **CASH** | **-6.6 bps** (±9.7) | `-28.4 bps` | `+0.083 / +0.098` | `0.69%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 02:15:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,762.00 | ⚪ **CASH** | **-0.6 bps** (±8.1) | `-7.1 bps` | `+0.071 / -0.046` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,431.82 | ⚪ **CASH** | **-15.3 bps** (±10.4) | `-22.2 bps` | `+0.001 / -0.110` | `0.64%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.30 | ⚪ **CASH** | **-6.6 bps** (±9.7) | `-28.4 bps` | `+0.083 / +0.098` | `0.69%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 02:01:25 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,690.01 | ⚪ **CASH** | **-0.6 bps** (±8.1) | `-7.1 bps` | `+0.071 / -0.046` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,429.16 | ⚪ **CASH** | **-15.3 bps** (±10.4) | `-22.2 bps` | `+0.001 / -0.110` | `0.64%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.01 | ⚪ **CASH** | **-6.6 bps** (±9.7) | `-28.4 bps` | `+0.083 / +0.098` | `0.69%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 01:45:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,816.68 | ⚪ **CASH** | **-13.5 bps** (±9.2) | `-25.5 bps` | `+0.073 / -0.122` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,430.88 | ⚪ **CASH** | **-18.4 bps** (±12.0) | `-28.4 bps` | `+0.008 / -0.109` | `0.65%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.12 | ⚪ **CASH** | **-3.9 bps** (±7.1) | `-22.1 bps` | `+0.083 / +0.069` | `0.70%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 01:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,435.47 | ⚪ **CASH** | **-13.5 bps** (±9.2) | `-25.5 bps` | `+0.073 / -0.122` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,416.65 | ⚪ **CASH** | **-18.4 bps** (±12.0) | `-28.4 bps` | `+0.008 / -0.109` | `0.65%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.61 | ⚪ **CASH** | **-3.9 bps** (±7.1) | `-22.1 bps` | `+0.083 / +0.069` | `0.70%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 01:15:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,442.60 | ⚪ **CASH** | **-13.5 bps** (±9.2) | `-25.5 bps` | `+0.073 / -0.122` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,416.74 | ⚪ **CASH** | **-18.4 bps** (±12.0) | `-28.4 bps` | `+0.008 / -0.109` | `0.65%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.52 | ⚪ **CASH** | **-3.9 bps** (±7.1) | `-22.1 bps` | `+0.083 / +0.069` | `0.70%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 01:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,524.64 | ⚪ **CASH** | **-13.5 bps** (±9.2) | `-25.5 bps` | `+0.073 / -0.122` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,420.43 | ⚪ **CASH** | **-18.4 bps** (±12.0) | `-28.4 bps` | `+0.008 / -0.109` | `0.65%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.72 | ⚪ **CASH** | **-3.9 bps** (±7.1) | `-22.1 bps` | `+0.083 / +0.069` | `0.70%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 00:46:20 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,812.00 | ⚪ **CASH** | **-28.4 bps** (±7.0) | `-58.2 bps` | `+0.080 / -0.060` | `0.44%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,429.13 | ⚪ **CASH** | **-12.4 bps** (±9.6) | `-20.8 bps` | `+0.007 / -0.069` | `0.66%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.03 | ⚪ **CASH** | **+4.6 bps** (±8.6) | `-6.0 bps` | `+0.078 / +0.069` | `0.71%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 00:30:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,730.80 | ⚪ **CASH** | **-28.4 bps** (±7.0) | `-58.2 bps` | `+0.080 / -0.060` | `0.44%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,429.19 | ⚪ **CASH** | **-12.4 bps** (±9.6) | `-20.8 bps` | `+0.007 / -0.069` | `0.66%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.88 | ⚪ **CASH** | **+4.6 bps** (±8.6) | `-6.0 bps` | `+0.078 / +0.069` | `0.71%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 00:16:20 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,712.00 | ⚪ **CASH** | **-28.4 bps** (±7.0) | `-58.2 bps` | `+0.080 / -0.060` | `0.44%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,428.66 | ⚪ **CASH** | **-12.4 bps** (±9.6) | `-20.8 bps` | `+0.007 / -0.069` | `0.66%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.64 | ⚪ **CASH** | **+4.6 bps** (±8.6) | `-6.0 bps` | `+0.078 / +0.069` | `0.71%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
