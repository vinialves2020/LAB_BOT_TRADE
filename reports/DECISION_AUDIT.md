# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-06 04:00:59 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-06 04:00:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,887.58 | ⚪ **CASH** | **+0.8 bps** (±23.9) | `+21.3 bps` | `-0.094 / -0.026` | `0.64%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.79 | ⚪ **CASH** | **-45.1 bps** (±31.2) | `-54.8 bps` | `-0.123 / -0.074` | `0.86%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.73 | ⚪ **CASH** | **-48.2 bps** (±30.2) | `-75.0 bps` | `-0.030 / +0.004` | `0.86%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 03:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,952.96 | ⚪ **CASH** | **-1.4 bps** (±26.9) | `+20.5 bps` | `-0.099 / -0.054` | `0.65%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.39 | ⚪ **CASH** | **-38.5 bps** (±17.7) | `-42.0 bps` | `-0.123 / -0.119` | `0.87%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.91 | ⚪ **CASH** | **-33.1 bps** (±15.0) | `-50.2 bps` | `-0.027 / +0.004` | `0.87%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 03:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,970.01 | ⚪ **CASH** | **-1.4 bps** (±26.9) | `+20.5 bps` | `-0.099 / -0.054` | `0.65%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.19 | ⚪ **CASH** | **-38.5 bps** (±17.7) | `-42.0 bps` | `-0.123 / -0.119` | `0.87%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.02 | ⚪ **CASH** | **-33.1 bps** (±15.0) | `-50.2 bps` | `-0.027 / +0.004` | `0.87%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 03:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,123.01 | ⚪ **CASH** | **-1.4 bps** (±26.9) | `+20.5 bps` | `-0.099 / -0.054` | `0.65%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,240.44 | ⚪ **CASH** | **-38.5 bps** (±17.7) | `-42.0 bps` | `-0.123 / -0.119` | `0.87%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.19 | ⚪ **CASH** | **-33.1 bps** (±15.0) | `-50.2 bps` | `-0.027 / +0.004` | `0.87%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 03:00:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,168.01 | ⚪ **CASH** | **-1.4 bps** (±26.9) | `+20.5 bps` | `-0.099 / -0.054` | `0.65%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,242.15 | ⚪ **CASH** | **-38.5 bps** (±17.7) | `-42.0 bps` | `-0.123 / -0.119` | `0.87%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.32 | ⚪ **CASH** | **-33.1 bps** (±15.0) | `-50.2 bps` | `-0.027 / +0.004` | `0.87%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 02:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,158.77 | ⚪ **CASH** | **+8.3 bps** (±17.6) | `+36.0 bps` | `-0.104 / -0.037` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,242.42 | ⚪ **CASH** | **-19.7 bps** (±21.2) | `-7.2 bps` | `-0.124 / -0.116` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.33 | ⚪ **CASH** | **-28.0 bps** (±21.0) | `-41.3 bps` | `-0.023 / +0.024` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 02:30:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,180.01 | ⚪ **CASH** | **+8.3 bps** (±17.6) | `+36.0 bps` | `-0.104 / -0.037` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,242.15 | ⚪ **CASH** | **-19.7 bps** (±21.2) | `-7.2 bps` | `-0.124 / -0.116` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.22 | ⚪ **CASH** | **-28.0 bps** (±21.0) | `-41.3 bps` | `-0.023 / +0.024` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 02:15:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,108.34 | ⚪ **CASH** | **+8.3 bps** (±17.6) | `+36.0 bps` | `-0.104 / -0.037` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,239.30 | ⚪ **CASH** | **-19.7 bps** (±21.2) | `-7.2 bps` | `-0.124 / -0.116` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.03 | ⚪ **CASH** | **-28.0 bps** (±21.0) | `-41.3 bps` | `-0.023 / +0.024` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 02:00:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,162.01 | ⚪ **CASH** | **+8.3 bps** (±17.6) | `+36.0 bps` | `-0.104 / -0.037` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,242.08 | ⚪ **CASH** | **-19.7 bps** (±21.2) | `-7.2 bps` | `-0.124 / -0.116` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.25 | ⚪ **CASH** | **-28.0 bps** (±21.0) | `-41.3 bps` | `-0.023 / +0.024` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 01:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,152.00 | ⚪ **CASH** | **-8.6 bps** (±19.2) | `+3.1 bps` | `-0.102 / -0.003` | `0.67%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,240.03 | ⚪ **CASH** | **-28.0 bps** (±12.6) | `-24.6 bps` | `-0.126 / -0.101` | `0.89%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.13 | ⚪ **CASH** | **-35.1 bps** (±21.9) | `-52.6 bps` | `-0.031 / +0.012` | `0.89%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 01:30:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,086.00 | ⚪ **CASH** | **-8.6 bps** (±19.2) | `+3.1 bps` | `-0.102 / -0.003` | `0.67%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.54 | ⚪ **CASH** | **-28.0 bps** (±12.6) | `-24.6 bps` | `-0.126 / -0.101` | `0.89%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.88 | ⚪ **CASH** | **-35.1 bps** (±21.9) | `-52.6 bps` | `-0.031 / +0.012` | `0.89%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 01:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,252.65 | ⚪ **CASH** | **-8.6 bps** (±19.2) | `+3.1 bps` | `-0.102 / -0.003` | `0.67%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,243.71 | ⚪ **CASH** | **-28.0 bps** (±12.6) | `-24.6 bps` | `-0.126 / -0.101` | `0.89%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.39 | ⚪ **CASH** | **-35.1 bps** (±21.9) | `-52.6 bps` | `-0.031 / +0.012` | `0.89%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 01:00:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,285.54 | ⚪ **CASH** | **-8.6 bps** (±19.2) | `+3.1 bps` | `-0.102 / -0.003` | `0.67%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,244.51 | ⚪ **CASH** | **-28.0 bps** (±12.6) | `-24.6 bps` | `-0.126 / -0.101` | `0.89%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.23 | ⚪ **CASH** | **-35.1 bps** (±21.9) | `-52.6 bps` | `-0.031 / +0.012` | `0.89%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 00:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,362.53 | ⚪ **CASH** | **+12.1 bps** (±19.6) | `+40.7 bps` | `-0.106 / +0.006` | `0.67%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,248.10 | ⚪ **CASH** | **-12.3 bps** (±21.5) | `+8.3 bps` | `-0.136 / -0.126` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.45 | ⚪ **CASH** | **-33.2 bps** (±31.4) | `-49.6 bps` | `-0.028 / +0.044` | `0.87%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 00:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,225.01 | ⚪ **CASH** | **+12.1 bps** (±19.6) | `+40.7 bps` | `-0.106 / +0.006` | `0.67%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,242.87 | ⚪ **CASH** | **-12.3 bps** (±21.5) | `+8.3 bps` | `-0.136 / -0.126` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.02 | ⚪ **CASH** | **-33.2 bps** (±31.4) | `-49.6 bps` | `-0.028 / +0.044` | `0.87%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 00:15:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,188.00 | ⚪ **CASH** | **+12.1 bps** (±19.6) | `+40.7 bps` | `-0.106 / +0.006` | `0.67%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,239.51 | ⚪ **CASH** | **-12.3 bps** (±21.5) | `+8.3 bps` | `-0.136 / -0.126` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.84 | ⚪ **CASH** | **-33.2 bps** (±31.4) | `-49.6 bps` | `-0.028 / +0.044` | `0.87%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 00:00:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,072.85 | ⚪ **CASH** | **+12.1 bps** (±19.6) | `+40.7 bps` | `-0.106 / +0.006` | `0.67%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.43 | ⚪ **CASH** | **-12.3 bps** (±21.5) | `+8.3 bps` | `-0.136 / -0.126` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.38 | ⚪ **CASH** | **-33.2 bps** (±31.4) | `-49.6 bps` | `-0.028 / +0.044` | `0.87%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 23:45:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,074.22 | ⚪ **CASH** | **+25.7 bps** (±24.9) | `+63.6 bps` | `-0.105 / +0.047` | `0.67%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,239.25 | ⚪ **CASH** | **-24.1 bps** (±29.9) | `-14.4 bps` | `-0.136 / -0.084` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.36 | ⚪ **CASH** | **-26.9 bps** (±24.9) | `-37.4 bps` | `-0.026 / +0.010` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 23:30:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,852.00 | ⚪ **CASH** | **+25.7 bps** (±24.9) | `+63.6 bps` | `-0.105 / +0.047` | `0.67%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,230.87 | ⚪ **CASH** | **-24.1 bps** (±29.9) | `-14.4 bps` | `-0.136 / -0.084` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.06 | ⚪ **CASH** | **-26.9 bps** (±24.9) | `-37.4 bps` | `-0.026 / +0.010` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 23:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,423.06 | ⚪ **CASH** | **+25.7 bps** (±24.9) | `+63.6 bps` | `-0.105 / +0.047` | `0.67%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,216.79 | ⚪ **CASH** | **-24.1 bps** (±29.9) | `-14.4 bps` | `-0.136 / -0.084` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $88.76 | ⚪ **CASH** | **-26.9 bps** (±24.9) | `-37.4 bps` | `-0.026 / +0.010` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 23:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,650.01 | ⚪ **CASH** | **+25.7 bps** (±24.9) | `+63.6 bps` | `-0.105 / +0.047` | `0.67%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,228.67 | ⚪ **CASH** | **-24.1 bps** (±29.9) | `-14.4 bps` | `-0.136 / -0.084` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.61 | ⚪ **CASH** | **-26.9 bps** (±24.9) | `-37.4 bps` | `-0.026 / +0.010` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 22:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,822.38 | ⚪ **CASH** | **+14.4 bps** (±22.0) | `+41.9 bps` | `-0.107 / +0.062` | `0.68%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,233.38 | ⚪ **CASH** | **-20.1 bps** (±19.6) | `-12.4 bps` | `-0.130 / -0.039` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.74 | ⚪ **CASH** | **-26.0 bps** (±32.3) | `-36.1 bps` | `-0.016 / +0.024` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 22:30:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,017.19 | ⚪ **CASH** | **+14.4 bps** (±22.0) | `+41.9 bps` | `-0.107 / +0.062` | `0.68%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,237.95 | ⚪ **CASH** | **-20.1 bps** (±19.6) | `-12.4 bps` | `-0.130 / -0.039` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.02 | ⚪ **CASH** | **-26.0 bps** (±32.3) | `-36.1 bps` | `-0.016 / +0.024` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 22:15:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,100.01 | ⚪ **CASH** | **+14.4 bps** (±22.0) | `+41.9 bps` | `-0.107 / +0.062` | `0.68%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,242.13 | ⚪ **CASH** | **-20.1 bps** (±19.6) | `-12.4 bps` | `-0.130 / -0.039` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.20 | ⚪ **CASH** | **-26.0 bps** (±32.3) | `-36.1 bps` | `-0.016 / +0.024` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 22:00:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,794.55 | ⚪ **CASH** | **+14.4 bps** (±22.0) | `+41.9 bps` | `-0.107 / +0.062` | `0.68%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,226.88 | ⚪ **CASH** | **-20.1 bps** (±19.6) | `-12.4 bps` | `-0.130 / -0.039` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.85 | ⚪ **CASH** | **-26.0 bps** (±32.3) | `-36.1 bps` | `-0.016 / +0.024` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 21:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,965.21 | ⚪ **CASH** | **-9.5 bps** (±18.0) | `+5.7 bps` | `-0.105 / -0.066` | `0.69%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.04 | ⚪ **CASH** | **-38.5 bps** (±16.4) | `-44.4 bps` | `-0.122 / -0.084` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.11 | ⚪ **CASH** | **-17.1 bps** (±22.6) | `-20.6 bps` | `-0.014 / +0.003` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 21:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,016.01 | ⚪ **CASH** | **-9.5 bps** (±18.0) | `+5.7 bps` | `-0.105 / -0.066` | `0.69%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.13 | ⚪ **CASH** | **-38.5 bps** (±16.4) | `-44.4 bps` | `-0.122 / -0.084` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.99 | ⚪ **CASH** | **-17.1 bps** (±22.6) | `-20.6 bps` | `-0.014 / +0.003` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 21:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,005.92 | ⚪ **CASH** | **-9.5 bps** (±18.0) | `+5.7 bps` | `-0.105 / -0.066` | `0.69%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.70 | ⚪ **CASH** | **-38.5 bps** (±16.4) | `-44.4 bps` | `-0.122 / -0.084` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.68 | ⚪ **CASH** | **-17.1 bps** (±22.6) | `-20.6 bps` | `-0.014 / +0.003` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 21:01:04 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,130.74 | ⚪ **CASH** | **-9.5 bps** (±18.0) | `+5.7 bps` | `-0.105 / -0.066` | `0.69%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,246.70 | ⚪ **CASH** | **-38.5 bps** (±16.4) | `-44.4 bps` | `-0.122 / -0.084` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.80 | ⚪ **CASH** | **-17.1 bps** (±22.6) | `-20.6 bps` | `-0.014 / +0.003` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 20:46:02 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,182.77 | ⚪ **CASH** | **-18.0 bps** (±7.7) | `-9.9 bps` | `-0.111 / -0.078` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,250.32 | ⚪ **CASH** | **-52.1 bps** (±9.2) | `-70.4 bps` | `-0.124 / -0.078` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.17 | ⚪ **CASH** | **-8.6 bps** (±16.7) | `-4.3 bps` | `-0.015 / -0.021` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 20:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,004.16 | ⚪ **CASH** | **-18.0 bps** (±7.7) | `-9.9 bps` | `-0.111 / -0.078` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,246.10 | ⚪ **CASH** | **-52.1 bps** (±9.2) | `-70.4 bps` | `-0.124 / -0.078` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.86 | ⚪ **CASH** | **-8.6 bps** (±16.7) | `-4.3 bps` | `-0.015 / -0.021` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 20:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,054.21 | ⚪ **CASH** | **-18.0 bps** (±7.7) | `-9.9 bps` | `-0.111 / -0.078` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,250.04 | ⚪ **CASH** | **-52.1 bps** (±9.2) | `-70.4 bps` | `-0.124 / -0.078` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.87 | ⚪ **CASH** | **-8.6 bps** (±16.7) | `-4.3 bps` | `-0.015 / -0.021` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 20:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,320.01 | ⚪ **CASH** | **-18.0 bps** (±7.7) | `-9.9 bps` | `-0.111 / -0.078` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,260.39 | ⚪ **CASH** | **-52.1 bps** (±9.2) | `-70.4 bps` | `-0.124 / -0.078` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.06 | ⚪ **CASH** | **-8.6 bps** (±16.7) | `-4.3 bps` | `-0.015 / -0.021` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 19:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,428.01 | ⚪ **CASH** | **-11.5 bps** (±11.2) | `+5.5 bps` | `-0.127 / -0.087` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,265.30 | ⚪ **CASH** | **-43.6 bps** (±16.0) | `-51.8 bps` | `-0.130 / -0.086` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.00 | ⚪ **CASH** | **-28.4 bps** (±26.8) | `-36.4 bps` | `-0.022 / -0.029` | `0.93%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 19:30:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,038.01 | ⚪ **CASH** | **-11.5 bps** (±11.2) | `+5.5 bps` | `-0.127 / -0.087` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,251.14 | ⚪ **CASH** | **-43.6 bps** (±16.0) | `-51.8 bps` | `-0.130 / -0.086` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.34 | ⚪ **CASH** | **-28.4 bps** (±26.8) | `-36.4 bps` | `-0.022 / -0.029` | `0.93%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 19:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,262.01 | ⚪ **CASH** | **-11.5 bps** (±11.2) | `+5.5 bps` | `-0.127 / -0.087` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,258.60 | ⚪ **CASH** | **-43.6 bps** (±16.0) | `-51.8 bps` | `-0.130 / -0.086` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.74 | ⚪ **CASH** | **-28.4 bps** (±26.8) | `-36.4 bps` | `-0.022 / -0.029` | `0.93%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
