# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-08 11:30:50 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-08 11:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,992.72 | ⚪ **CASH** | **+4.2 bps** (±5.9) | `+12.2 bps` | `-0.010 / -0.028` | `0.30%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,240.76 | ⚪ **CASH** | **-28.5 bps** (±6.7) | `-41.0 bps` | `-0.069 / -0.035` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.69 | ⚪ **CASH** | **-0.7 bps** (±12.4) | `-5.6 bps` | `-0.009 / +0.121` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 11:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,954.01 | ⚪ **CASH** | **+4.2 bps** (±5.9) | `+12.2 bps` | `-0.010 / -0.028` | `0.30%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,237.95 | ⚪ **CASH** | **-28.5 bps** (±6.7) | `-41.0 bps` | `-0.069 / -0.035` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.33 | ⚪ **CASH** | **-0.7 bps** (±12.4) | `-5.6 bps` | `-0.009 / +0.121` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 11:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,921.30 | ⚪ **CASH** | **+4.2 bps** (±5.9) | `+12.2 bps` | `-0.010 / -0.028` | `0.30%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.96 | ⚪ **CASH** | **-28.5 bps** (±6.7) | `-41.0 bps` | `-0.069 / -0.035` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.25 | ⚪ **CASH** | **-0.7 bps** (±12.4) | `-5.6 bps` | `-0.009 / +0.121` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 10:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,899.28 | ⚪ **CASH** | **+2.5 bps** (±8.6) | `+7.7 bps` | `-0.008 / -0.005` | `0.30%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.09 | ⚪ **CASH** | **-34.3 bps** (±6.1) | `-51.8 bps` | `-0.081 / -0.014` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.22 | ⚪ **CASH** | **-2.6 bps** (±13.5) | `-5.5 bps` | `-0.016 / +0.080` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 10:30:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,877.96 | ⚪ **CASH** | **+2.5 bps** (±8.6) | `+7.7 bps` | `-0.008 / -0.005` | `0.30%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.82 | ⚪ **CASH** | **-34.3 bps** (±6.1) | `-51.8 bps` | `-0.081 / -0.014` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.09 | ⚪ **CASH** | **-2.6 bps** (±13.5) | `-5.5 bps` | `-0.016 / +0.080` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 10:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,889.77 | ⚪ **CASH** | **+2.5 bps** (±8.6) | `+7.7 bps` | `-0.008 / -0.005` | `0.30%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.07 | ⚪ **CASH** | **-34.3 bps** (±6.1) | `-51.8 bps` | `-0.081 / -0.014` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.26 | ⚪ **CASH** | **-2.6 bps** (±13.5) | `-5.5 bps` | `-0.016 / +0.080` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 10:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,933.45 | ⚪ **CASH** | **+2.5 bps** (±8.6) | `+7.7 bps` | `-0.008 / -0.005` | `0.30%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.79 | ⚪ **CASH** | **-34.3 bps** (±6.1) | `-51.8 bps` | `-0.081 / -0.014` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.27 | ⚪ **CASH** | **-2.6 bps** (±13.5) | `-5.5 bps` | `-0.016 / +0.080` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 09:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,957.13 | ⚪ **CASH** | **+8.7 bps** (±10.2) | `+11.8 bps` | `+0.013 / +0.063` | `0.31%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,237.99 | ⚪ **CASH** | **-33.0 bps** (±8.0) | `-50.7 bps` | `-0.084 / -0.004` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.26 | ⚪ **CASH** | **-2.8 bps** (±13.7) | `-6.5 bps` | `-0.019 / +0.079` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 09:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,900.62 | ⚪ **CASH** | **+8.7 bps** (±10.2) | `+11.8 bps` | `+0.013 / +0.063` | `0.31%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.68 | ⚪ **CASH** | **-33.0 bps** (±8.0) | `-50.7 bps` | `-0.084 / -0.004` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.27 | ⚪ **CASH** | **-2.8 bps** (±13.7) | `-6.5 bps` | `-0.019 / +0.079` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 09:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,881.97 | ⚪ **CASH** | **+8.7 bps** (±10.2) | `+11.8 bps` | `+0.013 / +0.063` | `0.31%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.00 | ⚪ **CASH** | **-33.0 bps** (±8.0) | `-50.7 bps` | `-0.084 / -0.004` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.11 | ⚪ **CASH** | **-2.8 bps** (±13.7) | `-6.5 bps` | `-0.019 / +0.079` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 09:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,942.24 | ⚪ **CASH** | **+8.7 bps** (±10.2) | `+11.8 bps` | `+0.013 / +0.063` | `0.31%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,239.30 | ⚪ **CASH** | **-33.0 bps** (±8.0) | `-50.7 bps` | `-0.084 / -0.004` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.30 | ⚪ **CASH** | **-2.8 bps** (±13.7) | `-6.5 bps` | `-0.019 / +0.079` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 08:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,928.36 | ⚪ **CASH** | **+6.0 bps** (±8.2) | `+9.2 bps` | `+0.015 / +0.015` | `0.31%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.55 | ⚪ **CASH** | **-34.0 bps** (±8.1) | `-51.3 bps` | `-0.077 / -0.032` | `0.40%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.26 | ⚪ **CASH** | **-2.1 bps** (±10.6) | `-3.2 bps` | `-0.018 / +0.035` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 08:30:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,889.94 | ⚪ **CASH** | **+6.0 bps** (±8.2) | `+9.2 bps` | `+0.015 / +0.015` | `0.31%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,237.39 | ⚪ **CASH** | **-34.0 bps** (±8.1) | `-51.3 bps` | `-0.077 / -0.032` | `0.40%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.15 | ⚪ **CASH** | **-2.1 bps** (±10.6) | `-3.2 bps` | `-0.018 / +0.035` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 08:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,911.26 | ⚪ **CASH** | **+6.0 bps** (±8.2) | `+9.2 bps` | `+0.015 / +0.015` | `0.31%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,239.58 | ⚪ **CASH** | **-34.0 bps** (±8.1) | `-51.3 bps` | `-0.077 / -0.032` | `0.40%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.16 | ⚪ **CASH** | **-2.1 bps** (±10.6) | `-3.2 bps` | `-0.018 / +0.035` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 08:00:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,962.00 | ⚪ **CASH** | **+6.0 bps** (±8.2) | `+9.2 bps` | `+0.015 / +0.015` | `0.31%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,240.52 | ⚪ **CASH** | **-34.0 bps** (±8.1) | `-51.3 bps` | `-0.077 / -0.032` | `0.40%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.30 | ⚪ **CASH** | **-2.1 bps** (±10.6) | `-3.2 bps` | `-0.018 / +0.035` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 07:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,921.23 | ⚪ **CASH** | **+3.4 bps** (±6.6) | `+9.1 bps` | `-0.007 / -0.009` | `0.31%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.94 | ⚪ **CASH** | **-39.0 bps** (±6.3) | `-50.5 bps` | `-0.101 / -0.138` | `0.40%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.23 | ⚪ **CASH** | **-62.3 bps** (±8.2) | `-105.8 bps` | `-0.035 / -0.035` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 07:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,839.85 | ⚪ **CASH** | **+3.4 bps** (±6.6) | `+9.1 bps` | `-0.007 / -0.009` | `0.31%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.52 | ⚪ **CASH** | **-39.0 bps** (±6.3) | `-50.5 bps` | `-0.101 / -0.138` | `0.40%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.08 | ⚪ **CASH** | **-62.3 bps** (±8.2) | `-105.8 bps` | `-0.035 / -0.035` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 07:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,861.53 | ⚪ **CASH** | **+3.4 bps** (±6.6) | `+9.1 bps` | `-0.007 / -0.009` | `0.31%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.76 | ⚪ **CASH** | **-39.0 bps** (±6.3) | `-50.5 bps` | `-0.101 / -0.138` | `0.40%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.14 | ⚪ **CASH** | **-62.3 bps** (±8.2) | `-105.8 bps` | `-0.035 / -0.035` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 07:00:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,842.28 | ⚪ **CASH** | **+3.4 bps** (±6.6) | `+9.1 bps` | `-0.007 / -0.009` | `0.31%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.83 | ⚪ **CASH** | **-39.0 bps** (±6.3) | `-50.5 bps` | `-0.101 / -0.138` | `0.40%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.08 | ⚪ **CASH** | **-62.3 bps** (±8.2) | `-105.8 bps` | `-0.035 / -0.035` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 06:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,780.00 | ⚪ **CASH** | **+6.4 bps** (±8.2) | `+11.3 bps` | `+0.008 / +0.009` | `0.32%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,232.70 | ⚪ **CASH** | **-43.2 bps** (±15.5) | `-62.4 bps` | `-0.099 / -0.061` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $88.92 | ⚪ **CASH** | **-59.8 bps** (±11.9) | `-102.1 bps` | `-0.029 / -0.031` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 06:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,845.49 | ⚪ **CASH** | **+6.4 bps** (±8.2) | `+11.3 bps` | `+0.008 / +0.009` | `0.32%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.91 | ⚪ **CASH** | **-43.2 bps** (±15.5) | `-62.4 bps` | `-0.099 / -0.061` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.15 | ⚪ **CASH** | **-59.8 bps** (±11.9) | `-102.1 bps` | `-0.029 / -0.031` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 06:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,785.81 | ⚪ **CASH** | **+6.4 bps** (±8.2) | `+11.3 bps` | `+0.008 / +0.009` | `0.32%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.41 | ⚪ **CASH** | **-43.2 bps** (±15.5) | `-62.4 bps` | `-0.099 / -0.061` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.21 | ⚪ **CASH** | **-59.8 bps** (±11.9) | `-102.1 bps` | `-0.029 / -0.031` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 06:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,821.03 | ⚪ **CASH** | **+6.4 bps** (±8.2) | `+11.3 bps` | `+0.008 / +0.009` | `0.32%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.90 | ⚪ **CASH** | **-43.2 bps** (±15.5) | `-62.4 bps` | `-0.099 / -0.061` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.18 | ⚪ **CASH** | **-59.8 bps** (±11.9) | `-102.1 bps` | `-0.029 / -0.031` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 05:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,810.02 | ⚪ **CASH** | **+9.9 bps** (±8.5) | `+10.6 bps` | `+0.027 / +0.077` | `0.32%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.31 | ⚪ **CASH** | **-38.5 bps** (±17.5) | `-61.0 bps` | `-0.079 / +0.010` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.15 | ⚪ **CASH** | **-7.7 bps** (±10.5) | `-5.1 bps` | `-0.037 / -0.073` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 05:30:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,877.93 | ⚪ **CASH** | **+9.9 bps** (±8.5) | `+10.6 bps` | `+0.027 / +0.077` | `0.32%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,237.31 | ⚪ **CASH** | **-38.5 bps** (±17.5) | `-61.0 bps` | `-0.079 / +0.010` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.38 | ⚪ **CASH** | **-7.7 bps** (±10.5) | `-5.1 bps` | `-0.037 / -0.073` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 05:15:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,909.94 | ⚪ **CASH** | **+9.9 bps** (±8.5) | `+10.6 bps` | `+0.027 / +0.077` | `0.32%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.07 | ⚪ **CASH** | **-38.5 bps** (±17.5) | `-61.0 bps` | `-0.079 / +0.010` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.34 | ⚪ **CASH** | **-7.7 bps** (±10.5) | `-5.1 bps` | `-0.037 / -0.073` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 05:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,871.41 | ⚪ **CASH** | **+9.9 bps** (±8.5) | `+10.6 bps` | `+0.027 / +0.077` | `0.32%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.18 | ⚪ **CASH** | **-38.5 bps** (±17.5) | `-61.0 bps` | `-0.079 / +0.010` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.10 | ⚪ **CASH** | **-7.7 bps** (±10.5) | `-5.1 bps` | `-0.037 / -0.073` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 04:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,902.00 | ⚪ **CASH** | **+10.2 bps** (±8.6) | `+10.0 bps` | `+0.036 / +0.073` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.31 | ⚪ **CASH** | **-37.1 bps** (±17.9) | `-59.4 bps` | `-0.075 / +0.014` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.04 | ⚪ **CASH** | **-5.6 bps** (±11.6) | `-5.0 bps` | `-0.039 / -0.016` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 04:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,952.31 | ⚪ **CASH** | **+10.2 bps** (±8.6) | `+10.0 bps` | `+0.036 / +0.073` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.85 | ⚪ **CASH** | **-37.1 bps** (±17.9) | `-59.4 bps` | `-0.075 / +0.014` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.28 | ⚪ **CASH** | **-5.6 bps** (±11.6) | `-5.0 bps` | `-0.039 / -0.016` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 04:15:34 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,929.64 | ⚪ **CASH** | **+10.2 bps** (±8.6) | `+10.0 bps` | `+0.036 / +0.073` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.27 | ⚪ **CASH** | **-37.1 bps** (±17.9) | `-59.4 bps` | `-0.075 / +0.014` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.34 | ⚪ **CASH** | **-5.6 bps** (±11.6) | `-5.0 bps` | `-0.039 / -0.016` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 04:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,928.78 | ⚪ **CASH** | **+10.2 bps** (±8.6) | `+10.0 bps` | `+0.036 / +0.073` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.41 | ⚪ **CASH** | **-37.1 bps** (±17.9) | `-59.4 bps` | `-0.075 / +0.014` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.34 | ⚪ **CASH** | **-5.6 bps** (±11.6) | `-5.0 bps` | `-0.039 / -0.016` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 03:45:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,886.30 | ⚪ **CASH** | **+9.8 bps** (±8.2) | `+13.6 bps` | `+0.013 / +0.058` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,239.55 | ⚪ **CASH** | **-37.4 bps** (±17.1) | `-58.2 bps` | `-0.076 / +0.002` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.35 | ⚪ **CASH** | **-8.6 bps** (±12.3) | `-6.7 bps` | `-0.077 / +0.005` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 03:31:01 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,878.59 | ⚪ **CASH** | **+9.8 bps** (±8.2) | `+13.6 bps` | `+0.013 / +0.058` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,237.24 | ⚪ **CASH** | **-37.4 bps** (±17.1) | `-58.2 bps` | `-0.076 / +0.002` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.26 | ⚪ **CASH** | **-8.6 bps** (±12.3) | `-6.7 bps` | `-0.077 / +0.005` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 03:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,913.82 | ⚪ **CASH** | **+9.8 bps** (±8.2) | `+13.6 bps` | `+0.013 / +0.058` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,239.43 | ⚪ **CASH** | **-37.4 bps** (±17.1) | `-58.2 bps` | `-0.076 / +0.002` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.40 | ⚪ **CASH** | **-8.6 bps** (±12.3) | `-6.7 bps` | `-0.077 / +0.005` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 03:00:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,818.00 | ⚪ **CASH** | **+9.8 bps** (±8.2) | `+13.6 bps` | `+0.013 / +0.058` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.38 | ⚪ **CASH** | **-37.4 bps** (±17.1) | `-58.2 bps` | `-0.076 / +0.002` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.22 | ⚪ **CASH** | **-8.6 bps** (±12.3) | `-6.7 bps` | `-0.077 / +0.005` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 02:45:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,700.00 | ⚪ **CASH** | **+9.9 bps** (±9.5) | `+12.9 bps` | `+0.012 / +0.079` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,230.51 | ⚪ **CASH** | **-37.8 bps** (±16.2) | `-59.9 bps` | `-0.075 / +0.012` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $88.91 | ⚪ **CASH** | **-7.0 bps** (±12.1) | `-3.2 bps` | `-0.071 / -0.015` | `0.47%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
