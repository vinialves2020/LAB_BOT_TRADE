# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-23 01:02:09 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-23 01:02:09 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,548.82 | ⚪ **CASH** | **-7.2 bps** (±3.1) | `-2.7 bps` | `-0.088 / +0.048` | `0.31%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,396.61 | ⚪ **CASH** | **-13.3 bps** (±7.2) | `-11.3 bps` | `-0.067 / -0.012` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.16 | ⚪ **CASH** | **-7.4 bps** (±13.4) | `+13.3 bps` | `-0.109 / -0.144` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 00:47:07 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,531.51 | ⚪ **CASH** | **-5.2 bps** (±7.5) | `-1.7 bps` | `-0.094 / +0.112` | `0.32%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,395.56 | ⚪ **CASH** | **-16.1 bps** (±8.5) | `-15.9 bps` | `-0.068 / -0.007` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.03 | ⚪ **CASH** | **-16.6 bps** (±19.8) | `-1.1 bps` | `-0.100 / -0.169` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 00:32:11 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,328.16 | ⚪ **CASH** | **-5.2 bps** (±7.5) | `-1.7 bps` | `-0.094 / +0.112` | `0.32%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,389.53 | ⚪ **CASH** | **-16.1 bps** (±8.5) | `-15.9 bps` | `-0.068 / -0.007` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.90 | ⚪ **CASH** | **-16.6 bps** (±19.8) | `-1.1 bps` | `-0.100 / -0.169` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 00:17:02 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,158.13 | ⚪ **CASH** | **-5.2 bps** (±7.5) | `-1.7 bps` | `-0.094 / +0.112` | `0.32%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,386.50 | ⚪ **CASH** | **-16.1 bps** (±8.5) | `-15.9 bps` | `-0.068 / -0.007` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.58 | ⚪ **CASH** | **-16.6 bps** (±19.8) | `-1.1 bps` | `-0.100 / -0.169` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 00:02:11 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,364.64 | ⚪ **CASH** | **-5.2 bps** (±7.5) | `-1.7 bps` | `-0.094 / +0.112` | `0.32%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,388.12 | ⚪ **CASH** | **-16.1 bps** (±8.5) | `-15.9 bps` | `-0.068 / -0.007` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.69 | ⚪ **CASH** | **-16.6 bps** (±19.8) | `-1.1 bps` | `-0.100 / -0.169` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 23:47:04 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,385.59 | ⚪ **CASH** | **-13.4 bps** (±8.2) | `-18.4 bps` | `-0.104 / +0.166` | `0.32%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,386.16 | ⚪ **CASH** | **-16.2 bps** (±9.8) | `-15.7 bps` | `-0.070 / -0.001` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.59 | ⚪ **CASH** | **-16.9 bps** (±16.9) | `-4.7 bps` | `-0.096 / -0.128` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 23:32:11 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,323.90 | ⚪ **CASH** | **-13.4 bps** (±8.2) | `-18.4 bps` | `-0.104 / +0.166` | `0.32%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,382.92 | ⚪ **CASH** | **-16.2 bps** (±9.8) | `-15.7 bps` | `-0.070 / -0.001` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.28 | ⚪ **CASH** | **-16.9 bps** (±16.9) | `-4.7 bps` | `-0.096 / -0.128` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 23:17:17 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,338.58 | ⚪ **CASH** | **-13.4 bps** (±8.2) | `-18.4 bps` | `-0.104 / +0.166` | `0.32%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,384.30 | ⚪ **CASH** | **-16.2 bps** (±9.8) | `-15.7 bps` | `-0.070 / -0.001` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.41 | ⚪ **CASH** | **-16.9 bps** (±16.9) | `-4.7 bps` | `-0.096 / -0.128` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 23:02:04 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,344.75 | ⚪ **CASH** | **-13.4 bps** (±8.2) | `-18.4 bps` | `-0.104 / +0.166` | `0.32%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,384.12 | ⚪ **CASH** | **-16.2 bps** (±9.8) | `-15.7 bps` | `-0.070 / -0.001` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.32 | ⚪ **CASH** | **-16.9 bps** (±16.9) | `-4.7 bps` | `-0.096 / -0.128` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 22:46:56 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,338.01 | ⚪ **CASH** | **-19.3 bps** (±7.4) | `-22.5 bps` | `-0.114 / +0.085` | `0.32%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,385.13 | ⚪ **CASH** | **-26.7 bps** (±12.2) | `-32.5 bps` | `-0.074 / -0.014` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.37 | ⚪ **CASH** | **-20.1 bps** (±11.8) | `-12.6 bps` | `-0.092 / -0.109` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 22:32:26 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,372.01 | ⚪ **CASH** | **-19.3 bps** (±7.4) | `-22.5 bps` | `-0.114 / +0.085` | `0.32%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,384.87 | ⚪ **CASH** | **-26.7 bps** (±12.2) | `-32.5 bps` | `-0.074 / -0.014` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.47 | ⚪ **CASH** | **-20.1 bps** (±11.8) | `-12.6 bps` | `-0.092 / -0.109` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 22:17:06 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,451.78 | ⚪ **CASH** | **-19.3 bps** (±7.4) | `-22.5 bps` | `-0.114 / +0.085` | `0.32%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,389.84 | ⚪ **CASH** | **-26.7 bps** (±12.2) | `-32.5 bps` | `-0.074 / -0.014` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.64 | ⚪ **CASH** | **-20.1 bps** (±11.8) | `-12.6 bps` | `-0.092 / -0.109` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 22:02:14 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,531.92 | ⚪ **CASH** | **-19.3 bps** (±7.4) | `-22.5 bps` | `-0.114 / +0.085` | `0.32%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,395.59 | ⚪ **CASH** | **-26.7 bps** (±12.2) | `-32.5 bps` | `-0.074 / -0.014` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.84 | ⚪ **CASH** | **-20.1 bps** (±11.8) | `-12.6 bps` | `-0.092 / -0.109` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 21:47:03 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,475.27 | ⚪ **CASH** | **-22.9 bps** (±9.9) | `-27.1 bps` | `-0.117 / +0.070` | `0.32%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,393.49 | ⚪ **CASH** | **-27.2 bps** (±15.0) | `-30.4 bps` | `-0.090 / -0.028` | `0.44%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.55 | ⚪ **CASH** | **-17.6 bps** (±14.1) | `-7.0 bps` | `-0.096 / -0.110` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 21:32:13 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,532.01 | ⚪ **CASH** | **-22.9 bps** (±9.9) | `-27.1 bps` | `-0.117 / +0.070` | `0.32%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,396.00 | ⚪ **CASH** | **-27.2 bps** (±15.0) | `-30.4 bps` | `-0.090 / -0.028` | `0.44%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.86 | ⚪ **CASH** | **-17.6 bps** (±14.1) | `-7.0 bps` | `-0.096 / -0.110` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 21:17:06 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,512.74 | ⚪ **CASH** | **-22.9 bps** (±9.9) | `-27.1 bps` | `-0.117 / +0.070` | `0.32%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,397.40 | ⚪ **CASH** | **-27.2 bps** (±15.0) | `-30.4 bps` | `-0.090 / -0.028` | `0.44%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.99 | ⚪ **CASH** | **-17.6 bps** (±14.1) | `-7.0 bps` | `-0.096 / -0.110` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 21:02:17 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,250.01 | ⚪ **CASH** | **-22.9 bps** (±9.9) | `-27.1 bps` | `-0.117 / +0.070` | `0.32%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,381.02 | ⚪ **CASH** | **-27.2 bps** (±15.0) | `-30.4 bps` | `-0.090 / -0.028` | `0.44%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.30 | ⚪ **CASH** | **-17.6 bps** (±14.1) | `-7.0 bps` | `-0.096 / -0.110` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 20:47:27 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,252.01 | ⚪ **CASH** | **-20.8 bps** (±11.1) | `-24.2 bps` | `-0.120 / +0.093` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,381.76 | ⚪ **CASH** | **-26.9 bps** (±14.3) | `-31.5 bps` | `-0.081 / -0.015` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.16 | ⚪ **CASH** | **-21.5 bps** (±18.4) | `-16.9 bps` | `-0.085 / -0.070` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 20:32:22 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,350.02 | ⚪ **CASH** | **-20.8 bps** (±11.1) | `-24.2 bps` | `-0.120 / +0.093` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,384.39 | ⚪ **CASH** | **-26.9 bps** (±14.3) | `-31.5 bps` | `-0.081 / -0.015` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.46 | ⚪ **CASH** | **-21.5 bps** (±18.4) | `-16.9 bps` | `-0.085 / -0.070` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 20:17:02 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,386.63 | ⚪ **CASH** | **-20.8 bps** (±11.1) | `-24.2 bps` | `-0.120 / +0.093` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,384.68 | ⚪ **CASH** | **-26.9 bps** (±14.3) | `-31.5 bps` | `-0.081 / -0.015` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.45 | ⚪ **CASH** | **-21.5 bps** (±18.4) | `-16.9 bps` | `-0.085 / -0.070` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 20:02:29 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,484.00 | ⚪ **CASH** | **-20.8 bps** (±11.1) | `-24.2 bps` | `-0.120 / +0.093` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,387.63 | ⚪ **CASH** | **-26.9 bps** (±14.3) | `-31.5 bps` | `-0.081 / -0.015` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.73 | ⚪ **CASH** | **-21.5 bps** (±18.4) | `-16.9 bps` | `-0.085 / -0.070` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 19:47:04 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,339.06 | ⚪ **CASH** | **-27.5 bps** (±12.2) | `-33.1 bps` | `-0.127 / +0.062` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,379.62 | ⚪ **CASH** | **-28.6 bps** (±13.3) | `-33.0 bps` | `-0.096 / -0.015` | `0.45%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.24 | ⚪ **CASH** | **-21.9 bps** (±15.0) | `-24.2 bps` | `-0.057 / -0.017` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 19:32:01 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,530.16 | ⚪ **CASH** | **-27.5 bps** (±12.2) | `-33.1 bps` | `-0.127 / +0.062` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,391.87 | ⚪ **CASH** | **-28.6 bps** (±13.3) | `-33.0 bps` | `-0.096 / -0.015` | `0.45%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.88 | ⚪ **CASH** | **-21.9 bps** (±15.0) | `-24.2 bps` | `-0.057 / -0.017` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 19:17:10 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,356.00 | ⚪ **CASH** | **-27.5 bps** (±12.2) | `-33.1 bps` | `-0.127 / +0.062` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,382.78 | ⚪ **CASH** | **-28.6 bps** (±13.3) | `-33.0 bps` | `-0.096 / -0.015` | `0.45%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.45 | ⚪ **CASH** | **-21.9 bps** (±15.0) | `-24.2 bps` | `-0.057 / -0.017` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 19:02:10 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,360.01 | ⚪ **CASH** | **-27.5 bps** (±12.2) | `-33.1 bps` | `-0.127 / +0.062` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,382.35 | ⚪ **CASH** | **-28.6 bps** (±13.3) | `-33.0 bps` | `-0.096 / -0.015` | `0.45%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.49 | ⚪ **CASH** | **-21.9 bps** (±15.0) | `-24.2 bps` | `-0.057 / -0.017` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 18:47:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,383.11 | ⚪ **CASH** | **-40.0 bps** (±13.0) | `-52.6 bps` | `-0.134 / +0.030` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,384.10 | ⚪ **CASH** | **-31.1 bps** (±17.4) | `-34.5 bps` | `-0.099 / -0.040` | `0.46%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.82 | ⚪ **CASH** | **-19.0 bps** (±15.2) | `-20.4 bps` | `-0.048 / -0.001` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 18:32:06 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,166.06 | ⚪ **CASH** | **-40.0 bps** (±13.0) | `-52.6 bps` | `-0.134 / +0.030` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,377.91 | ⚪ **CASH** | **-31.1 bps** (±17.4) | `-34.5 bps` | `-0.099 / -0.040` | `0.46%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.54 | ⚪ **CASH** | **-19.0 bps** (±15.2) | `-20.4 bps` | `-0.048 / -0.001` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 18:17:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,136.63 | ⚪ **CASH** | **-40.0 bps** (±13.0) | `-52.6 bps` | `-0.134 / +0.030` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,377.18 | ⚪ **CASH** | **-31.1 bps** (±17.4) | `-34.5 bps` | `-0.099 / -0.040` | `0.46%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.22 | ⚪ **CASH** | **-19.0 bps** (±15.2) | `-20.4 bps` | `-0.048 / -0.001` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 18:02:16 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,135.04 | ⚪ **CASH** | **-40.0 bps** (±13.0) | `-52.6 bps` | `-0.134 / +0.030` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,377.55 | ⚪ **CASH** | **-31.1 bps** (±17.4) | `-34.5 bps` | `-0.099 / -0.040` | `0.46%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.50 | ⚪ **CASH** | **-19.0 bps** (±15.2) | `-20.4 bps` | `-0.048 / -0.001` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 17:47:10 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,356.00 | ⚪ **CASH** | **-41.3 bps** (±12.3) | `-48.1 bps` | `-0.149 / -0.044` | `0.34%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,383.60 | ⚪ **CASH** | **-36.3 bps** (±14.8) | `-42.5 bps` | `-0.094 / -0.066` | `0.47%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.90 | ⚪ **CASH** | **-10.1 bps** (±20.8) | `-3.9 bps` | `-0.041 / +0.010` | `0.50%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 17:32:17 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,358.00 | ⚪ **CASH** | **-41.3 bps** (±12.3) | `-48.1 bps` | `-0.149 / -0.044` | `0.34%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,382.22 | ⚪ **CASH** | **-36.3 bps** (±14.8) | `-42.5 bps` | `-0.094 / -0.066` | `0.47%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.94 | ⚪ **CASH** | **-10.1 bps** (±20.8) | `-3.9 bps` | `-0.041 / +0.010` | `0.50%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 17:17:23 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,302.00 | ⚪ **CASH** | **-41.3 bps** (±12.3) | `-48.1 bps` | `-0.149 / -0.044` | `0.34%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,382.41 | ⚪ **CASH** | **-36.3 bps** (±14.8) | `-42.5 bps` | `-0.094 / -0.066` | `0.47%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.66 | ⚪ **CASH** | **-10.1 bps** (±20.8) | `-3.9 bps` | `-0.041 / +0.010` | `0.50%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 17:02:19 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,306.46 | ⚪ **CASH** | **-41.3 bps** (±12.3) | `-48.1 bps` | `-0.149 / -0.044` | `0.34%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,381.16 | ⚪ **CASH** | **-36.3 bps** (±14.8) | `-42.5 bps` | `-0.094 / -0.066` | `0.47%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.78 | ⚪ **CASH** | **-10.1 bps** (±20.8) | `-3.9 bps` | `-0.041 / +0.010` | `0.50%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 16:47:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,353.21 | ⚪ **CASH** | **-40.6 bps** (±9.3) | `-46.6 bps` | `-0.152 / -0.047` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,378.82 | ⚪ **CASH** | **-36.4 bps** (±11.9) | `-45.7 bps` | `-0.080 / -0.046` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.89 | ⚪ **CASH** | **-2.7 bps** (±14.7) | `+5.8 bps` | `-0.037 / +0.048` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 16:32:08 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,477.35 | ⚪ **CASH** | **-40.6 bps** (±9.3) | `-46.6 bps` | `-0.152 / -0.047` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,388.93 | ⚪ **CASH** | **-36.4 bps** (±11.9) | `-45.7 bps` | `-0.080 / -0.046` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.08 | ⚪ **CASH** | **-2.7 bps** (±14.7) | `+5.8 bps` | `-0.037 / +0.048` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 16:17:18 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,652.01 | ⚪ **CASH** | **-40.6 bps** (±9.3) | `-46.6 bps` | `-0.152 / -0.047` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,397.87 | ⚪ **CASH** | **-36.4 bps** (±11.9) | `-45.7 bps` | `-0.080 / -0.046` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.50 | ⚪ **CASH** | **-2.7 bps** (±14.7) | `+5.8 bps` | `-0.037 / +0.048` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
