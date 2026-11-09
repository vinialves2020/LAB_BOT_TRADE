# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-09 02:30:46 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-11-09 00:00:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,820.18 | ⚪ **CASH** | **-22.5 bps** (±11.2) | `-33.5 bps` | `-0.020 / -0.039` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,126.59 | ⚪ **CASH** | **-36.7 bps** (±26.2) | `-44.4 bps` | `-0.094 / -0.112` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.55 | ⚪ **CASH** | **-11.7 bps** (±14.9) | `-22.4 bps` | `+0.034 / +0.022` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 23:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,992.64 | ⚪ **CASH** | **-29.2 bps** (±5.4) | `-42.3 bps` | `-0.030 / -0.081` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,134.19 | ⚪ **CASH** | **-42.5 bps** (±27.1) | `-53.5 bps` | `-0.094 / -0.124` | `0.82%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.77 | ⚪ **CASH** | **-24.3 bps** (±8.8) | `-40.9 bps` | `+0.007 / -0.014` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 23:30:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,434.45 | ⚪ **CASH** | **-29.2 bps** (±5.4) | `-42.3 bps` | `-0.030 / -0.081` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,152.44 | ⚪ **CASH** | **-42.5 bps** (±27.1) | `-53.5 bps` | `-0.094 / -0.124` | `0.82%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.47 | ⚪ **CASH** | **-24.3 bps** (±8.8) | `-40.9 bps` | `+0.007 / -0.014` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 23:15:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,384.05 | ⚪ **CASH** | **-29.2 bps** (±5.4) | `-42.3 bps` | `-0.030 / -0.081` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,157.97 | ⚪ **CASH** | **-42.5 bps** (±27.1) | `-53.5 bps` | `-0.094 / -0.124` | `0.82%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.88 | ⚪ **CASH** | **-24.3 bps** (±8.8) | `-40.9 bps` | `+0.007 / -0.014` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 23:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,787.56 | ⚪ **CASH** | **-29.2 bps** (±5.4) | `-42.3 bps` | `-0.030 / -0.081` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,135.32 | ⚪ **CASH** | **-42.5 bps** (±27.1) | `-53.5 bps` | `-0.094 / -0.124` | `0.82%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.76 | ⚪ **CASH** | **-24.3 bps** (±8.8) | `-40.9 bps` | `+0.007 / -0.014` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 22:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,290.00 | ⚪ **CASH** | **-53.3 bps** (±14.4) | `-75.6 bps` | `-0.050 / -0.174` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,123.03 | ⚪ **CASH** | **-60.8 bps** (±19.6) | `-77.3 bps` | `-0.140 / -0.205` | `0.83%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.87 | ⚪ **CASH** | **-15.1 bps** (±11.4) | `-20.2 bps` | `+0.000 / -0.044` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 22:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,344.84 | ⚪ **CASH** | **-53.3 bps** (±14.4) | `-75.6 bps` | `-0.050 / -0.174` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,121.98 | ⚪ **CASH** | **-60.8 bps** (±19.6) | `-77.3 bps` | `-0.140 / -0.205` | `0.83%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.95 | ⚪ **CASH** | **-15.1 bps** (±11.4) | `-20.2 bps` | `+0.000 / -0.044` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 22:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,602.43 | ⚪ **CASH** | **-53.3 bps** (±14.4) | `-75.6 bps` | `-0.050 / -0.174` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,134.98 | ⚪ **CASH** | **-60.8 bps** (±19.6) | `-77.3 bps` | `-0.140 / -0.205` | `0.83%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.86 | ⚪ **CASH** | **-15.1 bps** (±11.4) | `-20.2 bps` | `+0.000 / -0.044` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 22:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,261.37 | ⚪ **CASH** | **-53.3 bps** (±14.4) | `-75.6 bps` | `-0.050 / -0.174` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,130.95 | ⚪ **CASH** | **-60.8 bps** (±19.6) | `-77.3 bps` | `-0.140 / -0.205` | `0.83%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.31 | ⚪ **CASH** | **-15.1 bps** (±11.4) | `-20.2 bps` | `+0.000 / -0.044` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 21:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,424.07 | ⚪ **CASH** | **+21.6 bps** (±8.3) | `+51.4 bps` | `+0.006 / -0.175` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,218.28 | ⚪ **CASH** | **+9.8 bps** (±7.8) | `+31.8 bps` | `-0.032 / -0.148` | `0.21%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $88.60 | ⚪ **CASH** | **+26.4 bps** (±13.9) | `+35.5 bps` | `+0.071 / +0.118` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 21:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,701.54 | ⚪ **CASH** | **+21.6 bps** (±8.3) | `+51.4 bps` | `+0.006 / -0.175` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,224.79 | ⚪ **CASH** | **+9.8 bps** (±7.8) | `+31.8 bps` | `-0.032 / -0.148` | `0.21%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.04 | ⚪ **CASH** | **+26.4 bps** (±13.9) | `+35.5 bps` | `+0.071 / +0.118` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 21:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,765.55 | ⚪ **CASH** | **+21.6 bps** (±8.3) | `+51.4 bps` | `+0.006 / -0.175` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,226.79 | ⚪ **CASH** | **+9.8 bps** (±7.8) | `+31.8 bps` | `-0.032 / -0.148` | `0.21%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.13 | ⚪ **CASH** | **+26.4 bps** (±13.9) | `+35.5 bps` | `+0.071 / +0.118` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 21:00:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,769.69 | ⚪ **CASH** | **+21.6 bps** (±8.3) | `+51.4 bps` | `+0.006 / -0.175` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,227.71 | ⚪ **CASH** | **+9.8 bps** (±7.8) | `+31.8 bps` | `-0.032 / -0.148` | `0.21%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.17 | ⚪ **CASH** | **+26.4 bps** (±13.9) | `+35.5 bps` | `+0.071 / +0.118` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 20:45:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,838.42 | ⚪ **CASH** | **+19.5 bps** (±9.4) | `+41.1 bps` | `+0.017 / -0.097` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,228.35 | ⚪ **CASH** | **+14.9 bps** (±9.7) | `+33.7 bps` | `-0.014 / -0.066` | `0.21%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.35 | ⚪ **CASH** | **+24.8 bps** (±10.2) | `+32.0 bps` | `+0.058 / +0.129` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 20:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,900.12 | ⚪ **CASH** | **+19.5 bps** (±9.4) | `+41.1 bps` | `+0.017 / -0.097` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,230.59 | ⚪ **CASH** | **+14.9 bps** (±9.7) | `+33.7 bps` | `-0.014 / -0.066` | `0.21%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.55 | ⚪ **CASH** | **+24.8 bps** (±10.2) | `+32.0 bps` | `+0.058 / +0.129` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 20:15:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,892.26 | ⚪ **CASH** | **+19.5 bps** (±9.4) | `+41.1 bps` | `+0.017 / -0.097` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,228.90 | ⚪ **CASH** | **+14.9 bps** (±9.7) | `+33.7 bps` | `-0.014 / -0.066` | `0.21%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.49 | ⚪ **CASH** | **+24.8 bps** (±10.2) | `+32.0 bps` | `+0.058 / +0.129` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 20:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,929.04 | ⚪ **CASH** | **+19.5 bps** (±9.4) | `+41.1 bps` | `+0.017 / -0.097` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,231.57 | ⚪ **CASH** | **+14.9 bps** (±9.7) | `+33.7 bps` | `-0.014 / -0.066` | `0.21%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.53 | ⚪ **CASH** | **+24.8 bps** (±10.2) | `+32.0 bps` | `+0.058 / +0.129` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 19:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,913.61 | ⚪ **CASH** | **+32.1 bps** (±16.9) | `+57.0 bps` | `+0.028 / +0.004` | `0.17%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,233.52 | ⚪ **CASH** | **+16.2 bps** (±10.2) | `+33.0 bps` | `-0.018 / -0.021` | `0.22%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.66 | ⚪ **CASH** | **+25.7 bps** (±7.7) | `+31.9 bps` | `+0.058 / +0.142` | `0.33%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 19:30:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,904.04 | ⚪ **CASH** | **+32.1 bps** (±16.9) | `+57.0 bps` | `+0.028 / +0.004` | `0.17%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,233.36 | ⚪ **CASH** | **+16.2 bps** (±10.2) | `+33.0 bps` | `-0.018 / -0.021` | `0.22%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.61 | ⚪ **CASH** | **+25.7 bps** (±7.7) | `+31.9 bps` | `+0.058 / +0.142` | `0.33%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 19:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,857.43 | ⚪ **CASH** | **+32.1 bps** (±16.9) | `+57.0 bps` | `+0.028 / +0.004` | `0.17%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,233.01 | ⚪ **CASH** | **+16.2 bps** (±10.2) | `+33.0 bps` | `-0.018 / -0.021` | `0.22%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.34 | ⚪ **CASH** | **+25.7 bps** (±7.7) | `+31.9 bps` | `+0.058 / +0.142` | `0.33%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 19:00:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,914.43 | ⚪ **CASH** | **+32.1 bps** (±16.9) | `+57.0 bps` | `+0.028 / +0.004` | `0.17%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.17 | ⚪ **CASH** | **+16.2 bps** (±10.2) | `+33.0 bps` | `-0.018 / -0.021` | `0.22%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.46 | ⚪ **CASH** | **+25.7 bps** (±7.7) | `+31.9 bps` | `+0.058 / +0.142` | `0.33%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 18:45:34 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,934.81 | ⚪ **CASH** | **+32.4 bps** (±6.4) | `+57.4 bps` | `+0.021 / -0.008` | `0.16%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.49 | ⚪ **CASH** | **+11.7 bps** (±6.6) | `+25.0 bps` | `-0.011 / -0.038` | `0.21%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.59 | ⚪ **CASH** | **+25.1 bps** (±14.0) | `+38.6 bps` | `+0.043 / +0.066` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 18:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,942.01 | ⚪ **CASH** | **+32.4 bps** (±6.4) | `+57.4 bps` | `+0.021 / -0.008` | `0.16%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.26 | ⚪ **CASH** | **+11.7 bps** (±6.6) | `+25.0 bps` | `-0.011 / -0.038` | `0.21%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.67 | ⚪ **CASH** | **+25.1 bps** (±14.0) | `+38.6 bps` | `+0.043 / +0.066` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 18:15:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,920.01 | ⚪ **CASH** | **+32.4 bps** (±6.4) | `+57.4 bps` | `+0.021 / -0.008` | `0.16%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.74 | ⚪ **CASH** | **+11.7 bps** (±6.6) | `+25.0 bps` | `-0.011 / -0.038` | `0.21%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.54 | ⚪ **CASH** | **+25.1 bps** (±14.0) | `+38.6 bps` | `+0.043 / +0.066` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 18:00:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,754.01 | ⚪ **CASH** | **+32.4 bps** (±6.4) | `+57.4 bps` | `+0.021 / -0.008` | `0.16%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,230.82 | ⚪ **CASH** | **+11.7 bps** (±6.6) | `+25.0 bps` | `-0.011 / -0.038` | `0.21%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.19 | ⚪ **CASH** | **+25.1 bps** (±14.0) | `+38.6 bps` | `+0.043 / +0.066` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 17:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,763.98 | ⚪ **CASH** | **+34.9 bps** (±6.3) | `+58.6 bps` | `+0.026 / +0.033` | `0.17%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,230.13 | ⚪ **CASH** | **+11.3 bps** (±8.2) | `+20.5 bps` | `-0.010 / +0.018` | `0.22%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.09 | ⚪ **CASH** | **+23.5 bps** (±19.0) | `+36.4 bps` | `+0.045 / +0.063` | `0.34%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
