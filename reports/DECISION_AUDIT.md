# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-31 22:02:26 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-31 22:02:26 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,742.01 | ⚪ **CASH** | **+7.6 bps** (±9.0) | `-41.0 bps` | `+0.218 / +0.372` | `0.42%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,264.33 | ⚪ **CASH** | **-1.4 bps** (±5.1) | `-7.9 bps` | `-0.070 / +0.038` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.11 | ⚪ **CASH** | **+3.6 bps** (±13.2) | `-9.5 bps` | `+0.120 / -0.062` | `0.65%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 21:47:21 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,564.62 | ⚪ **CASH** | **+11.1 bps** (±6.4) | `-37.7 bps` | `+0.220 / +0.406` | `0.42%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,254.40 | ⚪ **CASH** | **+0.3 bps** (±2.8) | `-4.4 bps` | `-0.044 / -0.016` | `0.52%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.87 | ⚪ **CASH** | **+3.4 bps** (±9.8) | `-13.3 bps` | `+0.139 / -0.050` | `0.65%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 21:32:16 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,523.85 | ⚪ **CASH** | **+11.1 bps** (±6.4) | `-37.7 bps` | `+0.220 / +0.406` | `0.42%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,253.68 | ⚪ **CASH** | **+0.3 bps** (±2.8) | `-4.4 bps` | `-0.044 / -0.016` | `0.52%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.81 | ⚪ **CASH** | **+3.4 bps** (±9.8) | `-13.3 bps` | `+0.139 / -0.050` | `0.65%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 21:17:13 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,488.74 | ⚪ **CASH** | **+11.1 bps** (±6.4) | `-37.7 bps` | `+0.220 / +0.406` | `0.42%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,253.32 | ⚪ **CASH** | **+0.3 bps** (±2.8) | `-4.4 bps` | `-0.044 / -0.016` | `0.52%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.73 | ⚪ **CASH** | **+3.4 bps** (±9.8) | `-13.3 bps` | `+0.139 / -0.050` | `0.65%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 21:02:30 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,478.01 | ⚪ **CASH** | **+11.1 bps** (±6.4) | `-37.7 bps` | `+0.220 / +0.406` | `0.42%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,252.55 | ⚪ **CASH** | **+0.3 bps** (±2.8) | `-4.4 bps` | `-0.044 / -0.016` | `0.52%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.56 | ⚪ **CASH** | **+3.4 bps** (±9.8) | `-13.3 bps` | `+0.139 / -0.050` | `0.65%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 20:47:15 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,586.02 | ⚪ **CASH** | **+9.7 bps** (±7.5) | `-39.2 bps` | `+0.214 / +0.408` | `0.43%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,254.35 | ⚪ **CASH** | **+3.7 bps** (±5.1) | `-1.6 bps` | `+0.002 / -0.021` | `0.53%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.64 | ⚪ **CASH** | **-0.4 bps** (±10.1) | `-20.1 bps` | `+0.151 / -0.064` | `0.66%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 20:32:37 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,589.44 | ⚪ **CASH** | **+9.7 bps** (±7.5) | `-39.2 bps` | `+0.214 / +0.408` | `0.43%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,253.82 | ⚪ **CASH** | **+3.7 bps** (±5.1) | `-1.6 bps` | `+0.002 / -0.021` | `0.53%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.74 | ⚪ **CASH** | **-0.4 bps** (±10.1) | `-20.1 bps` | `+0.151 / -0.064` | `0.66%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 20:17:10 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,619.18 | ⚪ **CASH** | **+9.7 bps** (±7.5) | `-39.2 bps` | `+0.214 / +0.408` | `0.43%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,254.93 | ⚪ **CASH** | **+3.7 bps** (±5.1) | `-1.6 bps` | `+0.002 / -0.021` | `0.53%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.89 | ⚪ **CASH** | **-0.4 bps** (±10.1) | `-20.1 bps` | `+0.151 / -0.064` | `0.66%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 20:02:41 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,624.75 | ⚪ **CASH** | **+9.7 bps** (±7.5) | `-39.2 bps` | `+0.214 / +0.408` | `0.43%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,255.82 | ⚪ **CASH** | **+3.7 bps** (±5.1) | `-1.6 bps` | `+0.002 / -0.021` | `0.53%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.90 | ⚪ **CASH** | **-0.4 bps** (±10.1) | `-20.1 bps` | `+0.151 / -0.064` | `0.66%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 19:47:18 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,583.62 | ⚪ **CASH** | **+9.9 bps** (±7.4) | `-37.9 bps` | `+0.207 / +0.410` | `0.44%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,253.14 | ⚪ **CASH** | **+13.2 bps** (±5.1) | `+10.4 bps` | `+0.057 / -0.020` | `0.54%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.83 | ⚪ **CASH** | **-4.9 bps** (±9.7) | `-29.8 bps` | `+0.173 / -0.070` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 19:32:31 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,594.00 | ⚪ **CASH** | **+9.9 bps** (±7.4) | `-37.9 bps` | `+0.207 / +0.410` | `0.44%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,254.36 | ⚪ **CASH** | **+13.2 bps** (±5.1) | `+10.4 bps` | `+0.057 / -0.020` | `0.54%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.96 | ⚪ **CASH** | **-4.9 bps** (±9.7) | `-29.8 bps` | `+0.173 / -0.070` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 19:17:42 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,642.01 | ⚪ **CASH** | **+9.9 bps** (±7.4) | `-37.9 bps` | `+0.207 / +0.410` | `0.44%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,256.01 | ⚪ **CASH** | **+13.2 bps** (±5.1) | `+10.4 bps` | `+0.057 / -0.020` | `0.54%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.00 | ⚪ **CASH** | **-4.9 bps** (±9.7) | `-29.8 bps` | `+0.173 / -0.070` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 19:02:19 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,648.99 | ⚪ **CASH** | **+9.9 bps** (±7.4) | `-37.9 bps` | `+0.207 / +0.410` | `0.44%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,255.74 | ⚪ **CASH** | **+13.2 bps** (±5.1) | `+10.4 bps` | `+0.057 / -0.020` | `0.54%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.02 | ⚪ **CASH** | **-4.9 bps** (±9.7) | `-29.8 bps` | `+0.173 / -0.070` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 18:47:40 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,694.94 | ⚪ **CASH** | **+3.1 bps** (±8.8) | `-39.9 bps` | `+0.153 / +0.374` | `0.44%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,258.29 | ⚪ **CASH** | **+10.2 bps** (±6.7) | `+1.7 bps` | `+0.094 / +0.021` | `0.54%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.22 | ⚪ **CASH** | **-8.0 bps** (±11.7) | `-33.8 bps` | `+0.171 / -0.044` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 18:32:18 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,723.99 | ⚪ **CASH** | **+3.1 bps** (±8.8) | `-39.9 bps` | `+0.153 / +0.374` | `0.44%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,257.92 | ⚪ **CASH** | **+10.2 bps** (±6.7) | `+1.7 bps` | `+0.094 / +0.021` | `0.54%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.21 | ⚪ **CASH** | **-8.0 bps** (±11.7) | `-33.8 bps` | `+0.171 / -0.044` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 18:17:33 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,753.25 | ⚪ **CASH** | **+3.1 bps** (±8.8) | `-39.9 bps` | `+0.153 / +0.374` | `0.44%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,257.26 | ⚪ **CASH** | **+10.2 bps** (±6.7) | `+1.7 bps` | `+0.094 / +0.021` | `0.54%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.24 | ⚪ **CASH** | **-8.0 bps** (±11.7) | `-33.8 bps` | `+0.171 / -0.044` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 18:02:39 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,711.88 | ⚪ **CASH** | **+3.1 bps** (±8.8) | `-39.9 bps` | `+0.153 / +0.374` | `0.44%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,255.54 | ⚪ **CASH** | **+10.2 bps** (±6.7) | `+1.7 bps` | `+0.094 / +0.021` | `0.54%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.08 | ⚪ **CASH** | **-8.0 bps** (±11.7) | `-33.8 bps` | `+0.171 / -0.044` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 17:47:45 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,704.00 | ⚪ **CASH** | **-0.5 bps** (±9.0) | `-38.6 bps` | `+0.126 / +0.318` | `0.45%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,256.79 | ⚪ **CASH** | **+18.0 bps** (±3.0) | `+10.5 bps` | `+0.143 / +0.041` | `0.55%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.19 | ⚪ **CASH** | **-6.2 bps** (±7.4) | `-31.1 bps` | `+0.173 / -0.031` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 17:32:32 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,601.38 | ⚪ **CASH** | **-0.5 bps** (±9.0) | `-38.6 bps` | `+0.126 / +0.318` | `0.45%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,251.29 | ⚪ **CASH** | **+18.0 bps** (±3.0) | `+10.5 bps` | `+0.143 / +0.041` | `0.55%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.00 | ⚪ **CASH** | **-6.2 bps** (±7.4) | `-31.1 bps` | `+0.173 / -0.031` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 17:17:37 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,657.49 | ⚪ **CASH** | **-0.5 bps** (±9.0) | `-38.6 bps` | `+0.126 / +0.318` | `0.45%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,252.00 | ⚪ **CASH** | **+18.0 bps** (±3.0) | `+10.5 bps` | `+0.143 / +0.041` | `0.55%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.02 | ⚪ **CASH** | **-6.2 bps** (±7.4) | `-31.1 bps` | `+0.173 / -0.031` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 17:02:34 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,622.00 | ⚪ **CASH** | **-0.5 bps** (±9.0) | `-38.6 bps` | `+0.126 / +0.318` | `0.45%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,251.04 | ⚪ **CASH** | **+18.0 bps** (±3.0) | `+10.5 bps` | `+0.143 / +0.041` | `0.55%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.98 | ⚪ **CASH** | **-6.2 bps** (±7.4) | `-31.1 bps` | `+0.173 / -0.031` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 16:47:20 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,614.01 | ⚪ **CASH** | **-3.0 bps** (±11.3) | `-33.2 bps` | `+0.095 / +0.243` | `0.45%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,253.07 | ⚪ **CASH** | **+17.2 bps** (±5.2) | `+10.8 bps` | `+0.174 / -0.005` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.03 | ⚪ **CASH** | **-10.1 bps** (±9.4) | `-35.5 bps` | `+0.154 / -0.015` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 16:32:21 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,592.75 | ⚪ **CASH** | **-3.0 bps** (±11.3) | `-33.2 bps` | `+0.095 / +0.243` | `0.45%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,252.38 | ⚪ **CASH** | **+17.2 bps** (±5.2) | `+10.8 bps` | `+0.174 / -0.005` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.04 | ⚪ **CASH** | **-10.1 bps** (±9.4) | `-35.5 bps` | `+0.154 / -0.015` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 16:17:45 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,627.03 | ⚪ **CASH** | **-3.0 bps** (±11.3) | `-33.2 bps` | `+0.095 / +0.243` | `0.45%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,251.63 | ⚪ **CASH** | **+17.2 bps** (±5.2) | `+10.8 bps` | `+0.174 / -0.005` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.01 | ⚪ **CASH** | **-10.1 bps** (±9.4) | `-35.5 bps` | `+0.154 / -0.015` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 16:02:53 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,625.64 | ⚪ **CASH** | **-3.0 bps** (±11.3) | `-33.2 bps` | `+0.095 / +0.243` | `0.45%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,252.19 | ⚪ **CASH** | **+17.2 bps** (±5.2) | `+10.8 bps` | `+0.174 / -0.005` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.04 | ⚪ **CASH** | **-10.1 bps** (±9.4) | `-35.5 bps` | `+0.154 / -0.015` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 15:47:46 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,606.01 | ⚪ **CASH** | **+1.9 bps** (±8.1) | `-18.6 bps` | `+0.077 / +0.186` | `0.46%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,251.30 | ⚪ **CASH** | **+20.4 bps** (±3.5) | `+13.3 bps` | `+0.210 / -0.001` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.99 | ⚪ **CASH** | **-7.4 bps** (±12.0) | `-38.5 bps` | `+0.153 / +0.129` | `0.71%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 15:32:28 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,514.01 | ⚪ **CASH** | **+1.9 bps** (±8.1) | `-18.6 bps` | `+0.077 / +0.186` | `0.46%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,250.14 | ⚪ **CASH** | **+20.4 bps** (±3.5) | `+13.3 bps` | `+0.210 / -0.001` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.01 | ⚪ **CASH** | **-7.4 bps** (±12.0) | `-38.5 bps` | `+0.153 / +0.129` | `0.71%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 15:17:37 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,496.73 | ⚪ **CASH** | **+1.9 bps** (±8.1) | `-18.6 bps` | `+0.077 / +0.186` | `0.46%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,248.68 | ⚪ **CASH** | **+20.4 bps** (±3.5) | `+13.3 bps` | `+0.210 / -0.001` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.90 | ⚪ **CASH** | **-7.4 bps** (±12.0) | `-38.5 bps` | `+0.153 / +0.129` | `0.71%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 15:02:22 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,474.12 | ⚪ **CASH** | **+1.9 bps** (±8.1) | `-18.6 bps` | `+0.077 / +0.186` | `0.46%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,247.59 | ⚪ **CASH** | **+20.4 bps** (±3.5) | `+13.3 bps` | `+0.210 / -0.001` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.80 | ⚪ **CASH** | **-7.4 bps** (±12.0) | `-38.5 bps` | `+0.153 / +0.129` | `0.71%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 14:47:20 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,576.97 | ⚪ **CASH** | **+1.3 bps** (±8.0) | `-21.0 bps` | `+0.089 / +0.177` | `0.46%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,253.58 | ⚪ **CASH** | **+22.6 bps** (±3.8) | `+13.8 bps` | `+0.232 / +0.012` | `0.57%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.86 | ⚪ **CASH** | **-5.6 bps** (±8.3) | `-35.6 bps` | `+0.142 / +0.132` | `0.72%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 14:32:20 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,519.79 | ⚪ **CASH** | **+1.3 bps** (±8.0) | `-21.0 bps` | `+0.089 / +0.177` | `0.46%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,252.33 | ⚪ **CASH** | **+22.6 bps** (±3.8) | `+13.8 bps` | `+0.232 / +0.012` | `0.57%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.75 | ⚪ **CASH** | **-5.6 bps** (±8.3) | `-35.6 bps` | `+0.142 / +0.132` | `0.72%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 14:17:33 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,484.00 | ⚪ **CASH** | **+1.3 bps** (±8.0) | `-21.0 bps` | `+0.089 / +0.177` | `0.46%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,249.90 | ⚪ **CASH** | **+22.6 bps** (±3.8) | `+13.8 bps` | `+0.232 / +0.012` | `0.57%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.76 | ⚪ **CASH** | **-5.6 bps** (±8.3) | `-35.6 bps` | `+0.142 / +0.132` | `0.72%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 14:02:26 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,500.00 | ⚪ **CASH** | **+1.3 bps** (±8.0) | `-21.0 bps` | `+0.089 / +0.177` | `0.46%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,250.60 | ⚪ **CASH** | **+22.6 bps** (±3.8) | `+13.8 bps` | `+0.232 / +0.012` | `0.57%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.70 | ⚪ **CASH** | **-5.6 bps** (±8.3) | `-35.6 bps` | `+0.142 / +0.132` | `0.72%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 13:47:45 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,598.00 | ⚪ **CASH** | **+10.7 bps** (±2.7) | `+4.7 bps` | `+0.053 / +0.113` | `0.47%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,253.53 | ⚪ **CASH** | **+19.7 bps** (±3.7) | `+13.7 bps` | `+0.223 / -0.027` | `0.58%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.20 | ⚪ **CASH** | **-11.0 bps** (±10.6) | `-41.9 bps` | `+0.127 / +0.132` | `0.73%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 13:17:17 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,503.34 | ⚪ **CASH** | **+10.7 bps** (±2.7) | `+4.7 bps` | `+0.053 / +0.113` | `0.47%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,248.25 | ⚪ **CASH** | **+19.7 bps** (±3.7) | `+13.7 bps` | `+0.223 / -0.027` | `0.58%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.85 | ⚪ **CASH** | **-11.0 bps** (±10.6) | `-41.9 bps` | `+0.127 / +0.132` | `0.73%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 13:02:24 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,527.78 | ⚪ **CASH** | **+10.7 bps** (±2.7) | `+4.7 bps` | `+0.053 / +0.113` | `0.47%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,250.76 | ⚪ **CASH** | **+19.7 bps** (±3.7) | `+13.7 bps` | `+0.223 / -0.027` | `0.58%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.00 | ⚪ **CASH** | **-11.0 bps** (±10.6) | `-41.9 bps` | `+0.127 / +0.132` | `0.73%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
