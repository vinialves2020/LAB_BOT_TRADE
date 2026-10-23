# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-23 15:32:21 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-23 15:32:21 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,584.00 | ⚪ **CASH** | **+1.4 bps** (±7.9) | `-7.0 bps` | `+0.059 / +0.036` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,404.10 | ⚪ **CASH** | **+4.7 bps** (±2.8) | `-0.5 bps` | `+0.051 / +0.026` | `0.39%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.54 | ⚪ **CASH** | **+5.0 bps** (±11.5) | `+9.9 bps` | `-0.044 / +0.042` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 15:17:12 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,446.01 | ⚪ **CASH** | **+1.4 bps** (±7.9) | `-7.0 bps` | `+0.059 / +0.036` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,399.81 | ⚪ **CASH** | **+4.7 bps** (±2.8) | `-0.5 bps` | `+0.051 / +0.026` | `0.39%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.36 | ⚪ **CASH** | **+5.0 bps** (±11.5) | `+9.9 bps` | `-0.044 / +0.042` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 15:02:16 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,724.01 | ⚪ **CASH** | **+1.4 bps** (±7.9) | `-7.0 bps` | `+0.059 / +0.036` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,405.28 | ⚪ **CASH** | **+4.7 bps** (±2.8) | `-0.5 bps` | `+0.051 / +0.026` | `0.39%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.67 | ⚪ **CASH** | **+5.0 bps** (±11.5) | `+9.9 bps` | `-0.044 / +0.042` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 14:47:01 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,780.00 | ⚪ **CASH** | **+10.2 bps** (±9.6) | `+7.7 bps` | `+0.072 / +0.029` | `0.31%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,408.95 | ⚪ **CASH** | **+13.8 bps** (±4.8) | `+4.9 bps` | `+0.046 / +0.198` | `0.43%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.65 | ⚪ **CASH** | **-2.8 bps** (±21.0) | `-1.8 bps` | `-0.050 / +0.028` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 14:32:06 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,522.01 | ⚪ **CASH** | **+10.2 bps** (±9.6) | `+7.7 bps` | `+0.072 / +0.029` | `0.31%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,398.01 | ⚪ **CASH** | **+13.8 bps** (±4.8) | `+4.9 bps` | `+0.046 / +0.198` | `0.43%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.23 | ⚪ **CASH** | **-2.8 bps** (±21.0) | `-1.8 bps` | `-0.050 / +0.028` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 14:17:10 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,180.01 | ⚪ **CASH** | **+10.2 bps** (±9.6) | `+7.7 bps` | `+0.072 / +0.029` | `0.31%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,383.65 | ⚪ **CASH** | **+13.8 bps** (±4.8) | `+4.9 bps` | `+0.046 / +0.198` | `0.43%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.66 | ⚪ **CASH** | **-2.8 bps** (±21.0) | `-1.8 bps` | `-0.050 / +0.028` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 14:02:20 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,018.88 | ⚪ **CASH** | **+10.2 bps** (±9.6) | `+7.7 bps` | `+0.072 / +0.029` | `0.31%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,415.56 | ⚪ **CASH** | **+13.8 bps** (±4.8) | `+4.9 bps` | `+0.046 / +0.198` | `0.43%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.17 | ⚪ **CASH** | **-2.8 bps** (±21.0) | `-1.8 bps` | `-0.050 / +0.028` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 13:47:11 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,922.01 | ⚪ **CASH** | **+8.0 bps** (±7.1) | `+6.5 bps` | `+0.057 / +0.013` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,411.72 | ⚪ **CASH** | **+19.5 bps** (±6.9) | `+16.7 bps` | `+0.044 / +0.198` | `0.43%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.85 | ⚪ **CASH** | **-6.4 bps** (±10.5) | `-5.1 bps` | `-0.055 / -0.031` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 13:32:15 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,734.02 | ⚪ **CASH** | **+8.0 bps** (±7.1) | `+6.5 bps` | `+0.057 / +0.013` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,402.25 | ⚪ **CASH** | **+19.5 bps** (±6.9) | `+16.7 bps` | `+0.044 / +0.198` | `0.43%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.39 | ⚪ **CASH** | **-6.4 bps** (±10.5) | `-5.1 bps` | `-0.055 / -0.031` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 13:16:59 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,651.96 | ⚪ **CASH** | **+8.0 bps** (±7.1) | `+6.5 bps` | `+0.057 / +0.013` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,398.48 | ⚪ **CASH** | **+19.5 bps** (±6.9) | `+16.7 bps` | `+0.044 / +0.198` | `0.43%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.33 | ⚪ **CASH** | **-6.4 bps** (±10.5) | `-5.1 bps` | `-0.055 / -0.031` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 13:02:08 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,739.92 | ⚪ **CASH** | **+8.0 bps** (±7.1) | `+6.5 bps` | `+0.057 / +0.013` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,403.58 | ⚪ **CASH** | **+19.5 bps** (±6.9) | `+16.7 bps` | `+0.044 / +0.198` | `0.43%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.52 | ⚪ **CASH** | **-6.4 bps** (±10.5) | `-5.1 bps` | `-0.055 / -0.031` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 12:47:23 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,809.73 | ⚪ **CASH** | **+6.5 bps** (±7.2) | `+6.8 bps` | `+0.047 / -0.009` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,402.66 | ⚪ **CASH** | **+18.3 bps** (±6.8) | `+14.2 bps` | `+0.042 / +0.211` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.46 | ⚪ **CASH** | **-10.1 bps** (±9.6) | `-10.8 bps` | `-0.053 / -0.045` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 12:32:12 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,752.00 | ⚪ **CASH** | **+6.5 bps** (±7.2) | `+6.8 bps` | `+0.047 / -0.009` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,402.49 | ⚪ **CASH** | **+18.3 bps** (±6.8) | `+14.2 bps` | `+0.042 / +0.211` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.65 | ⚪ **CASH** | **-10.1 bps** (±9.6) | `-10.8 bps` | `-0.053 / -0.045` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 12:17:03 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,482.01 | ⚪ **CASH** | **+6.5 bps** (±7.2) | `+6.8 bps` | `+0.047 / -0.009` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,395.76 | ⚪ **CASH** | **+18.3 bps** (±6.8) | `+14.2 bps` | `+0.042 / +0.211` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.37 | ⚪ **CASH** | **-10.1 bps** (±9.6) | `-10.8 bps` | `-0.053 / -0.045` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 12:02:08 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,649.99 | ⚪ **CASH** | **+6.5 bps** (±7.2) | `+6.8 bps` | `+0.047 / -0.009` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,399.75 | ⚪ **CASH** | **+18.3 bps** (±6.8) | `+14.2 bps` | `+0.042 / +0.211` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.39 | ⚪ **CASH** | **-10.1 bps** (±9.6) | `-10.8 bps` | `-0.053 / -0.045` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 11:47:19 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,730.70 | ⚪ **CASH** | **+8.5 bps** (±4.7) | `+12.1 bps` | `+0.029 / -0.001` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,404.27 | ⚪ **CASH** | **+19.3 bps** (±5.5) | `+17.3 bps` | `+0.039 / +0.208` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.54 | ⚪ **CASH** | **-14.0 bps** (±11.1) | `-15.5 bps` | `-0.056 / -0.058` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 11:32:06 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,659.11 | ⚪ **CASH** | **+8.5 bps** (±4.7) | `+12.1 bps` | `+0.029 / -0.001` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,396.92 | ⚪ **CASH** | **+19.3 bps** (±5.5) | `+17.3 bps` | `+0.039 / +0.208` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.26 | ⚪ **CASH** | **-14.0 bps** (±11.1) | `-15.5 bps` | `-0.056 / -0.058` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 11:17:10 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,622.01 | ⚪ **CASH** | **+8.5 bps** (±4.7) | `+12.1 bps` | `+0.029 / -0.001` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,396.69 | ⚪ **CASH** | **+19.3 bps** (±5.5) | `+17.3 bps` | `+0.039 / +0.208` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.00 | ⚪ **CASH** | **-14.0 bps** (±11.1) | `-15.5 bps` | `-0.056 / -0.058` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 11:02:06 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,606.00 | ⚪ **CASH** | **+8.5 bps** (±4.7) | `+12.1 bps` | `+0.029 / -0.001` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,392.80 | ⚪ **CASH** | **+19.3 bps** (±5.5) | `+17.3 bps` | `+0.039 / +0.208` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.91 | ⚪ **CASH** | **-14.0 bps** (±11.1) | `-15.5 bps` | `-0.056 / -0.058` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 10:47:14 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,704.00 | ⚪ **CASH** | **+3.4 bps** (±6.7) | `+6.4 bps` | `+0.022 / -0.033` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,399.48 | ⚪ **CASH** | **+11.7 bps** (±9.2) | `+7.2 bps` | `+0.035 / +0.173` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.15 | ⚪ **CASH** | **-6.5 bps** (±11.9) | `+1.5 bps` | `-0.054 / -0.107` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 10:32:18 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,704.91 | ⚪ **CASH** | **+3.4 bps** (±6.7) | `+6.4 bps` | `+0.022 / -0.033` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,400.26 | ⚪ **CASH** | **+11.7 bps** (±9.2) | `+7.2 bps` | `+0.035 / +0.173` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.19 | ⚪ **CASH** | **-6.5 bps** (±11.9) | `+1.5 bps` | `-0.054 / -0.107` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 10:17:12 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,809.25 | ⚪ **CASH** | **+3.4 bps** (±6.7) | `+6.4 bps` | `+0.022 / -0.033` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,403.16 | ⚪ **CASH** | **+11.7 bps** (±9.2) | `+7.2 bps` | `+0.035 / +0.173` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.46 | ⚪ **CASH** | **-6.5 bps** (±11.9) | `+1.5 bps` | `-0.054 / -0.107` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 10:02:16 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,618.70 | ⚪ **CASH** | **+3.4 bps** (±6.7) | `+6.4 bps` | `+0.022 / -0.033` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,395.54 | ⚪ **CASH** | **+11.7 bps** (±9.2) | `+7.2 bps` | `+0.035 / +0.173` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.13 | ⚪ **CASH** | **-6.5 bps** (±11.9) | `+1.5 bps` | `-0.054 / -0.107` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 09:47:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,630.01 | ⚪ **CASH** | **+8.6 bps** (±7.5) | `+16.3 bps` | `+0.026 / -0.048` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,398.58 | ⚪ **CASH** | **+14.7 bps** (±7.5) | `+12.3 bps` | `+0.028 / +0.181` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.22 | ⚪ **CASH** | **-1.8 bps** (±7.7) | `+5.9 bps` | `-0.035 / -0.088` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 09:32:25 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,648.00 | ⚪ **CASH** | **+8.6 bps** (±7.5) | `+16.3 bps` | `+0.026 / -0.048` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,395.31 | ⚪ **CASH** | **+14.7 bps** (±7.5) | `+12.3 bps` | `+0.028 / +0.181` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.11 | ⚪ **CASH** | **-1.8 bps** (±7.7) | `+5.9 bps` | `-0.035 / -0.088` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 09:17:09 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,807.78 | ⚪ **CASH** | **+8.6 bps** (±7.5) | `+16.3 bps` | `+0.026 / -0.048` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,406.37 | ⚪ **CASH** | **+14.7 bps** (±7.5) | `+12.3 bps` | `+0.028 / +0.181` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.60 | ⚪ **CASH** | **-1.8 bps** (±7.7) | `+5.9 bps` | `-0.035 / -0.088` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 09:02:09 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,808.32 | ⚪ **CASH** | **+8.6 bps** (±7.5) | `+16.3 bps` | `+0.026 / -0.048` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,407.75 | ⚪ **CASH** | **+14.7 bps** (±7.5) | `+12.3 bps` | `+0.028 / +0.181` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.60 | ⚪ **CASH** | **-1.8 bps** (±7.7) | `+5.9 bps` | `-0.035 / -0.088` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 08:47:22 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,855.95 | ⚪ **CASH** | **+2.6 bps** (±3.5) | `-0.8 bps` | `+0.025 / +0.037` | `0.33%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,411.02 | ⚪ **CASH** | **-0.5 bps** (±9.0) | `+3.7 bps` | `-0.027 / -0.025` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.83 | ⚪ **CASH** | **+4.0 bps** (±7.0) | `+16.2 bps` | `-0.042 / -0.071` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 08:32:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,829.43 | ⚪ **CASH** | **+2.6 bps** (±3.5) | `-0.8 bps` | `+0.025 / +0.037` | `0.33%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,410.49 | ⚪ **CASH** | **-0.5 bps** (±9.0) | `+3.7 bps` | `-0.027 / -0.025` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.69 | ⚪ **CASH** | **+4.0 bps** (±7.0) | `+16.2 bps` | `-0.042 / -0.071` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 08:17:02 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,879.75 | ⚪ **CASH** | **+2.6 bps** (±3.5) | `-0.8 bps` | `+0.025 / +0.037` | `0.33%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,412.45 | ⚪ **CASH** | **-0.5 bps** (±9.0) | `+3.7 bps` | `-0.027 / -0.025` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.83 | ⚪ **CASH** | **+4.0 bps** (±7.0) | `+16.2 bps` | `-0.042 / -0.071` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 08:02:07 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,612.26 | ⚪ **CASH** | **+2.6 bps** (±3.5) | `-0.8 bps` | `+0.025 / +0.037` | `0.33%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,403.02 | ⚪ **CASH** | **-0.5 bps** (±9.0) | `+3.7 bps` | `-0.027 / -0.025` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.38 | ⚪ **CASH** | **+4.0 bps** (±7.0) | `+16.2 bps` | `-0.042 / -0.071` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 07:46:59 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,702.01 | ⚪ **CASH** | **+13.3 bps** (±4.0) | `+17.2 bps` | `+0.011 / +0.094` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,405.59 | ⚪ **CASH** | **+18.0 bps** (±6.9) | `+30.4 bps` | `-0.026 / +0.087` | `0.46%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.54 | ⚪ **CASH** | **+2.3 bps** (±7.8) | `+15.9 bps` | `-0.057 / -0.079` | `0.45%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 07:32:11 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,816.36 | ⚪ **CASH** | **+13.3 bps** (±4.0) | `+17.2 bps` | `+0.011 / +0.094` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,407.93 | ⚪ **CASH** | **+18.0 bps** (±6.9) | `+30.4 bps` | `-0.026 / +0.087` | `0.46%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.69 | ⚪ **CASH** | **+2.3 bps** (±7.8) | `+15.9 bps` | `-0.057 / -0.079` | `0.45%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 07:17:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,790.78 | ⚪ **CASH** | **+13.3 bps** (±4.0) | `+17.2 bps` | `+0.011 / +0.094` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,405.73 | ⚪ **CASH** | **+18.0 bps** (±6.9) | `+30.4 bps` | `-0.026 / +0.087` | `0.46%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.61 | ⚪ **CASH** | **+2.3 bps** (±7.8) | `+15.9 bps` | `-0.057 / -0.079` | `0.45%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 07:02:15 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,842.29 | ⚪ **CASH** | **+13.3 bps** (±4.0) | `+17.2 bps` | `+0.011 / +0.094` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,407.69 | ⚪ **CASH** | **+18.0 bps** (±6.9) | `+30.4 bps` | `-0.026 / +0.087` | `0.46%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.68 | ⚪ **CASH** | **+2.3 bps** (±7.8) | `+15.9 bps` | `-0.057 / -0.079` | `0.45%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-23 06:47:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,894.01 | ⚪ **CASH** | **+6.8 bps** (±4.8) | `+7.6 bps` | `+0.007 / +0.072` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,407.49 | ⚪ **CASH** | **+17.9 bps** (±6.9) | `+30.5 bps` | `-0.030 / +0.089` | `0.46%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.60 | ⚪ **CASH** | **+4.0 bps** (±1.2) | `+16.8 bps` | `-0.065 / -0.048` | `0.45%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
