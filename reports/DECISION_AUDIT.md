# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-30 17:02:32 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-30 17:02:32 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,409.88 | ⚪ **CASH** | **-22.4 bps** (±16.3) | `-23.4 bps` | `-0.086 / -0.026` | `0.58%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,240.58 | ⚪ **CASH** | **+16.6 bps** (±13.4) | `+18.1 bps` | `+0.023 / +0.253` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.04 | ⚪ **CASH** | **-55.9 bps** (±14.7) | `-87.4 bps` | `-0.069 / -0.009` | `0.91%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 16:47:27 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,351.69 | ⚪ **CASH** | **-14.2 bps** (±12.9) | `-8.4 bps` | `-0.085 / -0.038` | `0.58%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,226.69 | ⚪ **CASH** | **+23.7 bps** (±8.9) | `+32.0 bps` | `+0.015 / +0.235` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.86 | ⚪ **CASH** | **-50.2 bps** (±13.3) | `-78.4 bps` | `-0.060 / -0.006` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 16:32:27 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,472.00 | ⚪ **CASH** | **-14.2 bps** (±12.9) | `-8.4 bps` | `-0.085 / -0.038` | `0.58%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,233.05 | ⚪ **CASH** | **+23.7 bps** (±8.9) | `+32.0 bps` | `+0.015 / +0.235` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.13 | ⚪ **CASH** | **-50.2 bps** (±13.3) | `-78.4 bps` | `-0.060 / -0.006` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 16:17:35 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,653.21 | ⚪ **CASH** | **-14.2 bps** (±12.9) | `-8.4 bps` | `-0.085 / -0.038` | `0.58%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,237.21 | ⚪ **CASH** | **+23.7 bps** (±8.9) | `+32.0 bps` | `+0.015 / +0.235` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.39 | ⚪ **CASH** | **-50.2 bps** (±13.3) | `-78.4 bps` | `-0.060 / -0.006` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 16:02:41 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,428.27 | ⚪ **CASH** | **-14.2 bps** (±12.9) | `-8.4 bps` | `-0.085 / -0.038` | `0.58%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,225.58 | ⚪ **CASH** | **+23.7 bps** (±8.9) | `+32.0 bps` | `+0.015 / +0.235` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.62 | ⚪ **CASH** | **-50.2 bps** (±13.3) | `-78.4 bps` | `-0.060 / -0.006` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 15:47:27 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,430.00 | ⚪ **CASH** | **-29.7 bps** (±14.9) | `-31.8 bps` | `-0.081 / -0.113` | `0.58%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,226.88 | ⚪ **CASH** | **+15.7 bps** (±12.1) | `+21.7 bps` | `+0.002 / +0.196` | `0.76%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.39 | ⚪ **CASH** | **-54.6 bps** (±11.0) | `-86.5 bps` | `-0.054 / -0.024` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 15:32:28 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,531.33 | ⚪ **CASH** | **-29.7 bps** (±14.9) | `-31.8 bps` | `-0.081 / -0.113` | `0.58%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,231.56 | ⚪ **CASH** | **+15.7 bps** (±12.1) | `+21.7 bps` | `+0.002 / +0.196` | `0.76%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.70 | ⚪ **CASH** | **-54.6 bps** (±11.0) | `-86.5 bps` | `-0.054 / -0.024` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 15:17:13 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,887.99 | ⚪ **CASH** | **-29.7 bps** (±14.9) | `-31.8 bps` | `-0.081 / -0.113` | `0.58%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,255.00 | ⚪ **CASH** | **+15.7 bps** (±12.1) | `+21.7 bps` | `+0.002 / +0.196` | `0.76%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.44 | ⚪ **CASH** | **-54.6 bps** (±11.0) | `-86.5 bps` | `-0.054 / -0.024` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 15:02:24 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,486.00 | ⚪ **CASH** | **-29.7 bps** (±14.9) | `-31.8 bps` | `-0.081 / -0.113` | `0.58%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,246.25 | ⚪ **CASH** | **+15.7 bps** (±12.1) | `+21.7 bps` | `+0.002 / +0.196` | `0.76%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.02 | ⚪ **CASH** | **-54.6 bps** (±11.0) | `-86.5 bps` | `-0.054 / -0.024` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 14:47:41 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,043.46 | ⚪ **CASH** | **-36.3 bps** (±11.5) | `-39.7 bps` | `-0.081 / -0.187` | `0.59%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,234.15 | ⚪ **CASH** | **-5.9 bps** (±12.8) | `-12.9 bps` | `-0.004 / +0.135` | `0.76%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.94 | ⚪ **CASH** | **-114.2 bps** (±33.7) | `-193.0 bps` | `-0.046 / -0.001` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 14:32:41 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,745.15 | ⚪ **CASH** | **-36.3 bps** (±11.5) | `-39.7 bps` | `-0.081 / -0.187` | `0.59%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,218.23 | ⚪ **CASH** | **-5.9 bps** (±12.8) | `-12.9 bps` | `-0.004 / +0.135` | `0.76%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.19 | ⚪ **CASH** | **-114.2 bps** (±33.7) | `-193.0 bps` | `-0.046 / -0.001` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 14:17:26 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,740.54 | ⚪ **CASH** | **-36.3 bps** (±11.5) | `-39.7 bps` | `-0.081 / -0.187` | `0.59%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,215.50 | ⚪ **CASH** | **-5.9 bps** (±12.8) | `-12.9 bps` | `-0.004 / +0.135` | `0.76%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.39 | ⚪ **CASH** | **-114.2 bps** (±33.7) | `-193.0 bps` | `-0.046 / -0.001` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 14:02:44 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,948.00 | ⚪ **CASH** | **-36.3 bps** (±11.5) | `-39.7 bps` | `-0.081 / -0.187` | `0.59%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,222.14 | ⚪ **CASH** | **-5.9 bps** (±12.8) | `-12.9 bps` | `-0.004 / +0.135` | `0.76%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.04 | ⚪ **CASH** | **-114.2 bps** (±33.7) | `-193.0 bps` | `-0.046 / -0.001` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 13:47:19 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,000.89 | ⚪ **CASH** | **-35.1 bps** (±9.6) | `-41.3 bps` | `-0.072 / -0.156` | `0.60%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,223.19 | ⚪ **CASH** | **+6.0 bps** (±9.8) | `+7.1 bps` | `-0.008 / +0.149` | `0.77%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.15 | ⚪ **CASH** | **-51.8 bps** (±16.1) | `-84.4 bps` | `-0.042 / +0.011` | `0.91%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 13:32:29 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,107.61 | ⚪ **CASH** | **-35.1 bps** (±9.6) | `-41.3 bps` | `-0.072 / -0.156` | `0.60%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,220.16 | ⚪ **CASH** | **+6.0 bps** (±9.8) | `+7.1 bps` | `-0.008 / +0.149` | `0.77%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.67 | ⚪ **CASH** | **-51.8 bps** (±16.1) | `-84.4 bps` | `-0.042 / +0.011` | `0.91%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 13:17:17 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,300.00 | ⚪ **CASH** | **-35.1 bps** (±9.6) | `-41.3 bps` | `-0.072 / -0.156` | `0.60%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,229.04 | ⚪ **CASH** | **+6.0 bps** (±9.8) | `+7.1 bps` | `-0.008 / +0.149` | `0.77%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.34 | ⚪ **CASH** | **-51.8 bps** (±16.1) | `-84.4 bps` | `-0.042 / +0.011` | `0.91%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 13:02:59 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,376.01 | ⚪ **CASH** | **-35.1 bps** (±9.6) | `-41.3 bps` | `-0.072 / -0.156` | `0.60%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,232.57 | ⚪ **CASH** | **+6.0 bps** (±9.8) | `+7.1 bps` | `-0.008 / +0.149` | `0.77%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.84 | ⚪ **CASH** | **-51.8 bps** (±16.1) | `-84.4 bps` | `-0.042 / +0.011` | `0.91%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 12:47:25 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,350.01 | ⚪ **CASH** | **-32.7 bps** (±14.7) | `-36.8 bps` | `-0.071 / -0.144` | `0.60%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,230.53 | ⚪ **CASH** | **+7.5 bps** (±13.6) | `+11.4 bps` | `-0.012 / +0.144` | `0.78%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.59 | ⚪ **CASH** | **-53.8 bps** (±11.5) | `-90.4 bps` | `-0.039 / +0.030` | `0.92%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 12:32:46 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,497.00 | ⚪ **CASH** | **-32.7 bps** (±14.7) | `-36.8 bps` | `-0.071 / -0.144` | `0.60%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,234.66 | ⚪ **CASH** | **+7.5 bps** (±13.6) | `+11.4 bps` | `-0.012 / +0.144` | `0.78%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.60 | ⚪ **CASH** | **-53.8 bps** (±11.5) | `-90.4 bps` | `-0.039 / +0.030` | `0.92%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 12:17:20 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,470.01 | ⚪ **CASH** | **-32.7 bps** (±14.7) | `-36.8 bps` | `-0.071 / -0.144` | `0.60%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,235.86 | ⚪ **CASH** | **+7.5 bps** (±13.6) | `+11.4 bps` | `-0.012 / +0.144` | `0.78%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.60 | ⚪ **CASH** | **-53.8 bps** (±11.5) | `-90.4 bps` | `-0.039 / +0.030` | `0.92%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 12:02:40 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,366.00 | ⚪ **CASH** | **-32.7 bps** (±14.7) | `-36.8 bps` | `-0.071 / -0.144` | `0.60%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,233.08 | ⚪ **CASH** | **+7.5 bps** (±13.6) | `+11.4 bps` | `-0.012 / +0.144` | `0.78%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.51 | ⚪ **CASH** | **-53.8 bps** (±11.5) | `-90.4 bps` | `-0.039 / +0.030` | `0.92%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 11:47:16 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,436.14 | ⚪ **CASH** | **-20.6 bps** (±8.0) | `-19.1 bps` | `-0.064 / -0.114` | `0.61%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,235.86 | ⚪ **CASH** | **+7.7 bps** (±7.1) | `+9.6 bps` | `-0.012 / +0.151` | `0.79%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.56 | ⚪ **CASH** | **-60.2 bps** (±8.3) | `-103.3 bps` | `-0.038 / +0.033` | `0.92%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 11:32:24 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,762.01 | ⚪ **CASH** | **-20.6 bps** (±8.0) | `-19.1 bps` | `-0.064 / -0.114` | `0.61%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,248.76 | ⚪ **CASH** | **+7.7 bps** (±7.1) | `+9.6 bps` | `-0.012 / +0.151` | `0.79%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.08 | ⚪ **CASH** | **-60.2 bps** (±8.3) | `-103.3 bps` | `-0.038 / +0.033` | `0.92%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 11:17:31 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,624.50 | ⚪ **CASH** | **-20.6 bps** (±8.0) | `-19.1 bps` | `-0.064 / -0.114` | `0.61%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,244.55 | ⚪ **CASH** | **+7.7 bps** (±7.1) | `+9.6 bps` | `-0.012 / +0.151` | `0.79%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.94 | ⚪ **CASH** | **-60.2 bps** (±8.3) | `-103.3 bps` | `-0.038 / +0.033` | `0.92%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 11:02:24 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,826.00 | ⚪ **CASH** | **-20.6 bps** (±8.0) | `-19.1 bps` | `-0.064 / -0.114` | `0.61%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,250.06 | ⚪ **CASH** | **+7.7 bps** (±7.1) | `+9.6 bps` | `-0.012 / +0.151` | `0.79%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.23 | ⚪ **CASH** | **-60.2 bps** (±8.3) | `-103.3 bps` | `-0.038 / +0.033` | `0.92%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 10:47:16 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,609.52 | ⚪ **CASH** | **-30.8 bps** (±15.5) | `-38.4 bps` | `-0.058 / -0.094` | `0.61%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,241.83 | ⚪ **CASH** | **-24.0 bps** (±11.4) | `-45.0 bps` | `-0.016 / +0.121` | `0.78%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.95 | ⚪ **CASH** | **-59.8 bps** (±13.3) | `-105.5 bps` | `-0.035 / +0.083` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 10:32:42 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,512.00 | ⚪ **CASH** | **-30.8 bps** (±15.5) | `-38.4 bps` | `-0.058 / -0.094` | `0.61%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,236.56 | ⚪ **CASH** | **-24.0 bps** (±11.4) | `-45.0 bps` | `-0.016 / +0.121` | `0.78%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.90 | ⚪ **CASH** | **-59.8 bps** (±13.3) | `-105.5 bps` | `-0.035 / +0.083` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 10:17:26 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,405.24 | ⚪ **CASH** | **-30.8 bps** (±15.5) | `-38.4 bps` | `-0.058 / -0.094` | `0.61%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,223.42 | ⚪ **CASH** | **-24.0 bps** (±11.4) | `-45.0 bps` | `-0.016 / +0.121` | `0.78%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.40 | ⚪ **CASH** | **-59.8 bps** (±13.3) | `-105.5 bps` | `-0.035 / +0.083` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 10:02:57 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,600.01 | ⚪ **CASH** | **-30.8 bps** (±15.5) | `-38.4 bps` | `-0.058 / -0.094` | `0.61%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,226.05 | ⚪ **CASH** | **-24.0 bps** (±11.4) | `-45.0 bps` | `-0.016 / +0.121` | `0.78%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.64 | ⚪ **CASH** | **-59.8 bps** (±13.3) | `-105.5 bps` | `-0.035 / +0.083` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 09:47:25 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,600.02 | ⚪ **CASH** | **-29.5 bps** (±9.6) | `-44.4 bps` | `-0.047 / -0.009` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,228.19 | ⚪ **CASH** | **-12.7 bps** (±11.3) | `-24.2 bps` | `-0.019 / +0.112` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.85 | ⚪ **CASH** | **-67.5 bps** (±14.7) | `-120.2 bps` | `-0.036 / +0.091` | `0.94%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 09:32:27 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,641.27 | ⚪ **CASH** | **-29.5 bps** (±9.6) | `-44.4 bps` | `-0.047 / -0.009` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,223.54 | ⚪ **CASH** | **-12.7 bps** (±11.3) | `-24.2 bps` | `-0.019 / +0.112` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.87 | ⚪ **CASH** | **-67.5 bps** (±14.7) | `-120.2 bps` | `-0.036 / +0.091` | `0.94%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 09:17:12 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,817.69 | ⚪ **CASH** | **-29.5 bps** (±9.6) | `-44.4 bps` | `-0.047 / -0.009` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,224.80 | ⚪ **CASH** | **-12.7 bps** (±11.3) | `-24.2 bps` | `-0.019 / +0.112` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.10 | ⚪ **CASH** | **-67.5 bps** (±14.7) | `-120.2 bps` | `-0.036 / +0.091` | `0.94%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 09:02:16 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,994.14 | ⚪ **CASH** | **-29.5 bps** (±9.6) | `-44.4 bps` | `-0.047 / -0.009` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,229.17 | ⚪ **CASH** | **-12.7 bps** (±11.3) | `-24.2 bps` | `-0.019 / +0.112` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.35 | ⚪ **CASH** | **-67.5 bps** (±14.7) | `-120.2 bps` | `-0.036 / +0.091` | `0.94%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 08:47:10 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,966.01 | ⚪ **CASH** | **-9.7 bps** (±5.6) | `-11.8 bps` | `-0.034 / +0.002` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,225.15 | ⚪ **CASH** | **-1.1 bps** (±10.5) | `-3.0 bps` | `-0.020 / +0.100` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.11 | ⚪ **CASH** | **-49.3 bps** (±20.7) | `-86.8 bps` | `-0.037 / +0.095` | `0.95%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 08:34:17 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,051.50 | ⚪ **CASH** | **-9.7 bps** (±5.6) | `-11.8 bps` | `-0.034 / +0.002` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,231.05 | ⚪ **CASH** | **-1.1 bps** (±10.5) | `-3.0 bps` | `-0.020 / +0.100` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.37 | ⚪ **CASH** | **-49.3 bps** (±20.7) | `-86.8 bps` | `-0.037 / +0.095` | `0.95%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 08:17:25 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,143.24 | ⚪ **CASH** | **-9.7 bps** (±5.6) | `-11.8 bps` | `-0.034 / +0.002` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,233.86 | ⚪ **CASH** | **-1.1 bps** (±10.5) | `-3.0 bps` | `-0.020 / +0.100` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.41 | ⚪ **CASH** | **-49.3 bps** (±20.7) | `-86.8 bps` | `-0.037 / +0.095` | `0.95%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
