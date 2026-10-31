# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-31 07:02:40 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-31 07:02:40 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,359.25 | ⚪ **CASH** | **+4.4 bps** (±1.0) | `+3.9 bps` | `-0.032 / +0.136` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,245.00 | ⚪ **CASH** | **+4.3 bps** (±5.3) | `+9.1 bps` | `+0.213 / -0.302` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.92 | ⚪ **CASH** | **-5.3 bps** (±12.4) | `-26.0 bps` | `+0.099 / +0.160` | `0.79%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 06:47:33 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,515.47 | ⚪ **CASH** | **+2.0 bps** (±3.3) | `+4.4 bps` | `-0.041 / +0.091` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,248.82 | ⚪ **CASH** | **+5.3 bps** (±5.1) | `+9.6 bps` | `+0.210 / -0.271` | `0.64%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.25 | ⚪ **CASH** | **-8.9 bps** (±11.4) | `-32.3 bps` | `+0.099 / +0.161` | `0.80%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 06:32:22 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,277.25 | ⚪ **CASH** | **+2.0 bps** (±3.3) | `+4.4 bps` | `-0.041 / +0.091` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,243.54 | ⚪ **CASH** | **+5.3 bps** (±5.1) | `+9.6 bps` | `+0.210 / -0.271` | `0.64%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.91 | ⚪ **CASH** | **-8.9 bps** (±11.4) | `-32.3 bps` | `+0.099 / +0.161` | `0.80%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 06:17:37 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,299.75 | ⚪ **CASH** | **+2.0 bps** (±3.3) | `+4.4 bps` | `-0.041 / +0.091` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,243.55 | ⚪ **CASH** | **+5.3 bps** (±5.1) | `+9.6 bps` | `+0.210 / -0.271` | `0.64%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.04 | ⚪ **CASH** | **-8.9 bps** (±11.4) | `-32.3 bps` | `+0.099 / +0.161` | `0.80%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 06:02:48 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,366.00 | ⚪ **CASH** | **+2.0 bps** (±3.3) | `+4.4 bps` | `-0.041 / +0.091` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,244.92 | ⚪ **CASH** | **+5.3 bps** (±5.1) | `+9.6 bps` | `+0.210 / -0.271` | `0.64%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.15 | ⚪ **CASH** | **-8.9 bps** (±11.4) | `-32.3 bps` | `+0.099 / +0.161` | `0.80%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 05:32:35 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,222.00 | ⚪ **CASH** | **+0.3 bps** (±3.0) | `+2.4 bps` | `-0.043 / +0.077` | `0.52%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,240.34 | ⚪ **CASH** | **+7.3 bps** (±5.2) | `+9.9 bps` | `+0.210 / -0.216` | `0.65%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.07 | ⚪ **CASH** | **-5.4 bps** (±8.1) | `-27.4 bps` | `+0.094 / +0.183` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 05:17:24 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,252.01 | ⚪ **CASH** | **+0.3 bps** (±3.0) | `+2.4 bps` | `-0.043 / +0.077` | `0.52%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,241.46 | ⚪ **CASH** | **+7.3 bps** (±5.2) | `+9.9 bps` | `+0.210 / -0.216` | `0.65%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.14 | ⚪ **CASH** | **-5.4 bps** (±8.1) | `-27.4 bps` | `+0.094 / +0.183` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 05:02:22 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,230.33 | ⚪ **CASH** | **+0.3 bps** (±3.0) | `+2.4 bps` | `-0.043 / +0.077` | `0.52%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,240.19 | ⚪ **CASH** | **+7.3 bps** (±5.2) | `+9.9 bps` | `+0.210 / -0.216` | `0.65%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.81 | ⚪ **CASH** | **-5.4 bps** (±8.1) | `-27.4 bps` | `+0.094 / +0.183` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 04:47:26 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,184.12 | ⚪ **CASH** | **+0.8 bps** (±3.1) | `+2.7 bps` | `-0.042 / +0.084` | `0.53%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,238.67 | ⚪ **CASH** | **+10.3 bps** (±4.7) | `+11.0 bps` | `+0.202 / -0.141` | `0.66%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.77 | ⚪ **CASH** | **+5.4 bps** (±14.4) | `-9.7 bps` | `+0.102 / +0.218` | `0.82%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 04:32:24 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,268.01 | ⚪ **CASH** | **+0.8 bps** (±3.1) | `+2.7 bps` | `-0.042 / +0.084` | `0.53%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,240.40 | ⚪ **CASH** | **+10.3 bps** (±4.7) | `+11.0 bps` | `+0.202 / -0.141` | `0.66%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.28 | ⚪ **CASH** | **+5.4 bps** (±14.4) | `-9.7 bps` | `+0.102 / +0.218` | `0.82%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 04:17:22 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,220.01 | ⚪ **CASH** | **+0.8 bps** (±3.1) | `+2.7 bps` | `-0.042 / +0.084` | `0.53%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,239.51 | ⚪ **CASH** | **+10.3 bps** (±4.7) | `+11.0 bps` | `+0.202 / -0.141` | `0.66%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.19 | ⚪ **CASH** | **+5.4 bps** (±14.4) | `-9.7 bps` | `+0.102 / +0.218` | `0.82%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 04:02:25 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,252.99 | ⚪ **CASH** | **+0.8 bps** (±3.1) | `+2.7 bps` | `-0.042 / +0.084` | `0.53%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,241.36 | ⚪ **CASH** | **+10.3 bps** (±4.7) | `+11.0 bps` | `+0.202 / -0.141` | `0.66%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.43 | ⚪ **CASH** | **+5.4 bps** (±14.4) | `-9.7 bps` | `+0.102 / +0.218` | `0.82%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 03:47:48 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,216.01 | ⚪ **CASH** | **+6.7 bps** (±2.5) | `+10.3 bps` | `-0.031 / +0.104` | `0.53%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,242.84 | ⚪ **CASH** | **+13.9 bps** (±4.9) | `+6.4 bps` | `+0.202 / +0.021` | `0.66%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.46 | ⚪ **CASH** | **+22.0 bps** (±20.9) | `+19.5 bps` | `+0.102 / +0.242` | `0.82%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 03:32:19 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,329.35 | ⚪ **CASH** | **+6.7 bps** (±2.5) | `+10.3 bps` | `-0.031 / +0.104` | `0.53%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,244.44 | ⚪ **CASH** | **+13.9 bps** (±4.9) | `+6.4 bps` | `+0.202 / +0.021` | `0.66%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.76 | ⚪ **CASH** | **+22.0 bps** (±20.9) | `+19.5 bps` | `+0.102 / +0.242` | `0.82%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 03:17:21 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,350.00 | ⚪ **CASH** | **+6.7 bps** (±2.5) | `+10.3 bps` | `-0.031 / +0.104` | `0.53%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,244.04 | ⚪ **CASH** | **+13.9 bps** (±4.9) | `+6.4 bps` | `+0.202 / +0.021` | `0.66%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.92 | ⚪ **CASH** | **+22.0 bps** (±20.9) | `+19.5 bps` | `+0.102 / +0.242` | `0.82%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 03:02:19 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,425.02 | ⚪ **CASH** | **+6.7 bps** (±2.5) | `+10.3 bps` | `-0.031 / +0.104` | `0.53%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,246.39 | ⚪ **CASH** | **+13.9 bps** (±4.9) | `+6.4 bps` | `+0.202 / +0.021` | `0.66%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.85 | ⚪ **CASH** | **+22.0 bps** (±20.9) | `+19.5 bps` | `+0.102 / +0.242` | `0.82%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 02:47:31 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,454.01 | ⚪ **CASH** | **+6.1 bps** (±2.0) | `+10.5 bps` | `-0.036 / +0.096` | `0.54%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,247.10 | ⚪ **CASH** | **+20.3 bps** (±6.3) | `+13.0 bps` | `+0.196 / +0.116` | `0.67%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.98 | ⚪ **CASH** | **+20.1 bps** (±18.4) | `+16.3 bps` | `+0.100 / +0.237` | `0.83%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 02:32:17 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,392.01 | ⚪ **CASH** | **+6.1 bps** (±2.0) | `+10.5 bps` | `-0.036 / +0.096` | `0.54%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,245.49 | ⚪ **CASH** | **+20.3 bps** (±6.3) | `+13.0 bps` | `+0.196 / +0.116` | `0.67%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.79 | ⚪ **CASH** | **+20.1 bps** (±18.4) | `+16.3 bps` | `+0.100 / +0.237` | `0.83%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 02:17:51 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,450.00 | ⚪ **CASH** | **+6.1 bps** (±2.0) | `+10.5 bps` | `-0.036 / +0.096` | `0.54%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,247.33 | ⚪ **CASH** | **+20.3 bps** (±6.3) | `+13.0 bps` | `+0.196 / +0.116` | `0.67%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.77 | ⚪ **CASH** | **+20.1 bps** (±18.4) | `+16.3 bps` | `+0.100 / +0.237` | `0.83%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 02:02:24 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,384.00 | ⚪ **CASH** | **+6.1 bps** (±2.0) | `+10.5 bps` | `-0.036 / +0.096` | `0.54%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,243.90 | ⚪ **CASH** | **+20.3 bps** (±6.3) | `+13.0 bps` | `+0.196 / +0.116` | `0.67%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.68 | ⚪ **CASH** | **+20.1 bps** (±18.4) | `+16.3 bps` | `+0.100 / +0.237` | `0.83%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 01:47:36 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,488.01 | ⚪ **CASH** | **+6.3 bps** (±2.9) | `+10.1 bps` | `-0.038 / +0.113` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,247.19 | ⚪ **CASH** | **+22.1 bps** (±9.5) | `+14.1 bps` | `+0.161 / +0.214` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.00 | ⚪ **CASH** | **+24.1 bps** (±15.0) | `+24.2 bps` | `+0.078 / +0.252` | `0.85%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-10-31 01:32:26 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,434.02 | ⚪ **CASH** | **+6.3 bps** (±2.9) | `+10.1 bps` | `-0.038 / +0.113` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,244.94 | ⚪ **CASH** | **+22.1 bps** (±9.5) | `+14.1 bps` | `+0.161 / +0.214` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.68 | ⚪ **CASH** | **+24.1 bps** (±15.0) | `+24.2 bps` | `+0.078 / +0.252` | `0.85%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-10-31 01:17:27 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,560.01 | ⚪ **CASH** | **+6.3 bps** (±2.9) | `+10.1 bps` | `-0.038 / +0.113` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,248.56 | ⚪ **CASH** | **+22.1 bps** (±9.5) | `+14.1 bps` | `+0.161 / +0.214` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.78 | ⚪ **CASH** | **+24.1 bps** (±15.0) | `+24.2 bps` | `+0.078 / +0.252` | `0.85%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-10-31 01:02:25 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,643.04 | ⚪ **CASH** | **+6.3 bps** (±2.9) | `+10.1 bps` | `-0.038 / +0.113` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,252.03 | ⚪ **CASH** | **+22.1 bps** (±9.5) | `+14.1 bps` | `+0.161 / +0.214` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.99 | ⚪ **CASH** | **+24.1 bps** (±15.0) | `+24.2 bps` | `+0.078 / +0.252` | `0.85%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-10-31 00:47:18 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,435.43 | ⚪ **CASH** | **-2.4 bps** (±2.6) | `+5.0 bps` | `-0.060 / -0.002` | `0.55%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,249.60 | ⚪ **CASH** | **+22.4 bps** (±10.2) | `+15.6 bps` | `+0.124 / +0.271` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.72 | ⚪ **CASH** | **+20.5 bps** (±13.8) | `+22.2 bps` | `+0.048 / +0.242` | `0.85%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 00:32:29 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,277.76 | ⚪ **CASH** | **-2.4 bps** (±2.6) | `+5.0 bps` | `-0.060 / -0.002` | `0.55%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,246.02 | ⚪ **CASH** | **+22.4 bps** (±10.2) | `+15.6 bps` | `+0.124 / +0.271` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.34 | ⚪ **CASH** | **+20.5 bps** (±13.8) | `+22.2 bps` | `+0.048 / +0.242` | `0.85%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 00:17:25 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,418.70 | ⚪ **CASH** | **-2.4 bps** (±2.6) | `+5.0 bps` | `-0.060 / -0.002` | `0.55%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,248.00 | ⚪ **CASH** | **+22.4 bps** (±10.2) | `+15.6 bps` | `+0.124 / +0.271` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.49 | ⚪ **CASH** | **+20.5 bps** (±13.8) | `+22.2 bps` | `+0.048 / +0.242` | `0.85%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 00:03:00 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,380.00 | ⚪ **CASH** | **-2.4 bps** (±2.6) | `+5.0 bps` | `-0.060 / -0.002` | `0.55%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,246.11 | ⚪ **CASH** | **+22.4 bps** (±10.2) | `+15.6 bps` | `+0.124 / +0.271` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.46 | ⚪ **CASH** | **+20.5 bps** (±13.8) | `+22.2 bps` | `+0.048 / +0.242` | `0.85%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 23:47:24 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,322.01 | ⚪ **CASH** | **-3.7 bps** (±5.3) | `+5.5 bps` | `-0.070 / -0.016` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,245.22 | ⚪ **CASH** | **+22.1 bps** (±9.6) | `+14.0 bps` | `+0.116 / +0.306` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.36 | ⚪ **CASH** | **+3.0 bps** (±13.6) | `-5.8 bps` | `+0.016 / +0.238` | `0.86%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 23:32:28 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,185.66 | ⚪ **CASH** | **-3.7 bps** (±5.3) | `+5.5 bps` | `-0.070 / -0.016` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,243.75 | ⚪ **CASH** | **+22.1 bps** (±9.6) | `+14.0 bps` | `+0.116 / +0.306` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.16 | ⚪ **CASH** | **+3.0 bps** (±13.6) | `-5.8 bps` | `+0.016 / +0.238` | `0.86%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 23:17:35 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,047.99 | ⚪ **CASH** | **-3.7 bps** (±5.3) | `+5.5 bps` | `-0.070 / -0.016` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,238.79 | ⚪ **CASH** | **+22.1 bps** (±9.6) | `+14.0 bps` | `+0.116 / +0.306` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.93 | ⚪ **CASH** | **+3.0 bps** (±13.6) | `-5.8 bps` | `+0.016 / +0.238` | `0.86%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 23:02:23 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,990.01 | ⚪ **CASH** | **-3.7 bps** (±5.3) | `+5.5 bps` | `-0.070 / -0.016` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,237.56 | ⚪ **CASH** | **+22.1 bps** (±9.6) | `+14.0 bps` | `+0.116 / +0.306` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.92 | ⚪ **CASH** | **+3.0 bps** (±13.6) | `-5.8 bps` | `+0.016 / +0.238` | `0.86%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 22:47:22 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,986.00 | ⚪ **CASH** | **-6.8 bps** (±7.5) | `+1.5 bps` | `-0.072 / -0.029` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,237.77 | ⚪ **CASH** | **+21.4 bps** (±8.4) | `+15.1 bps` | `+0.088 / +0.311` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.84 | ⚪ **CASH** | **-20.6 bps** (±9.1) | `-41.2 bps` | `-0.024 / +0.173` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 22:32:49 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,908.00 | ⚪ **CASH** | **-6.8 bps** (±7.5) | `+1.5 bps` | `-0.072 / -0.029` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,237.58 | ⚪ **CASH** | **+21.4 bps** (±8.4) | `+15.1 bps` | `+0.088 / +0.311` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.77 | ⚪ **CASH** | **-20.6 bps** (±9.1) | `-41.2 bps` | `-0.024 / +0.173` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 22:17:33 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,903.59 | ⚪ **CASH** | **-6.8 bps** (±7.5) | `+1.5 bps` | `-0.072 / -0.029` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,241.24 | ⚪ **CASH** | **+21.4 bps** (±8.4) | `+15.1 bps` | `+0.088 / +0.311` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.68 | ⚪ **CASH** | **-20.6 bps** (±9.1) | `-41.2 bps` | `-0.024 / +0.173` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 22:02:31 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,832.00 | ⚪ **CASH** | **-6.8 bps** (±7.5) | `+1.5 bps` | `-0.072 / -0.029` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,242.78 | ⚪ **CASH** | **+21.4 bps** (±8.4) | `+15.1 bps` | `+0.088 / +0.311` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.56 | ⚪ **CASH** | **-20.6 bps** (±9.1) | `-41.2 bps` | `-0.024 / +0.173` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
