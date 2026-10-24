# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-24 10:02:10 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-24 10:02:10 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,647.46 | ⚪ **CASH** | **+5.7 bps** (±6.4) | `+5.0 bps` | `+0.020 / +0.056` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,368.34 | ⚪ **CASH** | **-0.8 bps** (±4.0) | `+1.4 bps` | `+0.027 / -0.087` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.43 | ⚪ **CASH** | **+11.8 bps** (±8.5) | `+24.3 bps` | `-0.022 / -0.001` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 09:47:08 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,540.41 | ⚪ **CASH** | **+8.9 bps** (±5.3) | `+6.9 bps` | `+0.020 / +0.111` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,361.21 | ⚪ **CASH** | **+2.0 bps** (±3.6) | `+0.9 bps` | `+0.026 / -0.002` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.23 | ⚪ **CASH** | **+9.9 bps** (±9.1) | `+20.7 bps` | `-0.025 / +0.007` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 09:32:25 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,620.61 | ⚪ **CASH** | **+8.9 bps** (±5.3) | `+6.9 bps` | `+0.020 / +0.111` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,363.27 | ⚪ **CASH** | **+2.0 bps** (±3.6) | `+0.9 bps` | `+0.026 / -0.002` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.47 | ⚪ **CASH** | **+9.9 bps** (±9.1) | `+20.7 bps` | `-0.025 / +0.007` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 09:17:09 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,620.72 | ⚪ **CASH** | **+8.9 bps** (±5.3) | `+6.9 bps` | `+0.020 / +0.111` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,364.15 | ⚪ **CASH** | **+2.0 bps** (±3.6) | `+0.9 bps` | `+0.026 / -0.002` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.60 | ⚪ **CASH** | **+9.9 bps** (±9.1) | `+20.7 bps` | `-0.025 / +0.007` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 09:02:15 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,666.99 | ⚪ **CASH** | **+8.9 bps** (±5.3) | `+6.9 bps` | `+0.020 / +0.111` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,367.91 | ⚪ **CASH** | **+2.0 bps** (±3.6) | `+0.9 bps` | `+0.026 / -0.002` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.85 | ⚪ **CASH** | **+9.9 bps** (±9.1) | `+20.7 bps` | `-0.025 / +0.007` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 08:47:06 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,664.50 | ⚪ **CASH** | **+6.8 bps** (±4.9) | `+6.9 bps` | `+0.004 / +0.088` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,368.38 | ⚪ **CASH** | **+7.2 bps** (±5.2) | `+7.1 bps` | `+0.094 / -0.040` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.92 | ⚪ **CASH** | **+7.8 bps** (±7.6) | `+16.6 bps` | `-0.027 / +0.023` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 08:32:02 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,811.99 | ⚪ **CASH** | **+6.8 bps** (±4.9) | `+6.9 bps` | `+0.004 / +0.088` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,372.71 | ⚪ **CASH** | **+7.2 bps** (±5.2) | `+7.1 bps` | `+0.094 / -0.040` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.11 | ⚪ **CASH** | **+7.8 bps** (±7.6) | `+16.6 bps` | `-0.027 / +0.023` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 08:16:59 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,780.49 | ⚪ **CASH** | **+6.8 bps** (±4.9) | `+6.9 bps` | `+0.004 / +0.088` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,374.13 | ⚪ **CASH** | **+7.2 bps** (±5.2) | `+7.1 bps` | `+0.094 / -0.040` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.07 | ⚪ **CASH** | **+7.8 bps** (±7.6) | `+16.6 bps` | `-0.027 / +0.023` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 08:02:08 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,775.05 | ⚪ **CASH** | **+6.8 bps** (±4.9) | `+6.9 bps` | `+0.004 / +0.088` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,375.44 | ⚪ **CASH** | **+7.2 bps** (±5.2) | `+7.1 bps` | `+0.094 / -0.040` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.00 | ⚪ **CASH** | **+7.8 bps** (±7.6) | `+16.6 bps` | `-0.027 / +0.023` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 07:47:03 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,810.83 | ⚪ **CASH** | **+9.2 bps** (±3.6) | `+9.6 bps` | `+0.005 / +0.106` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,378.45 | ⚪ **CASH** | **+10.3 bps** (±3.3) | `+10.4 bps` | `+0.096 / -0.011` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.09 | ⚪ **CASH** | **+3.7 bps** (±5.0) | `+8.9 bps` | `-0.029 / +0.018` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 07:32:10 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,759.25 | ⚪ **CASH** | **+9.2 bps** (±3.6) | `+9.6 bps` | `+0.005 / +0.106` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,376.83 | ⚪ **CASH** | **+10.3 bps** (±3.3) | `+10.4 bps` | `+0.096 / -0.011` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.94 | ⚪ **CASH** | **+3.7 bps** (±5.0) | `+8.9 bps` | `-0.029 / +0.018` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 07:16:54 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,833.54 | ⚪ **CASH** | **+9.2 bps** (±3.6) | `+9.6 bps` | `+0.005 / +0.106` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,380.21 | ⚪ **CASH** | **+10.3 bps** (±3.3) | `+10.4 bps` | `+0.096 / -0.011` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.29 | ⚪ **CASH** | **+3.7 bps** (±5.0) | `+8.9 bps` | `-0.029 / +0.018` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 07:02:04 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,821.42 | ⚪ **CASH** | **+9.2 bps** (±3.6) | `+9.6 bps` | `+0.005 / +0.106` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,379.67 | ⚪ **CASH** | **+10.3 bps** (±3.3) | `+10.4 bps` | `+0.096 / -0.011` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.26 | ⚪ **CASH** | **+3.7 bps** (±5.0) | `+8.9 bps` | `-0.029 / +0.018` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 06:47:17 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,776.00 | ⚪ **CASH** | **+1.8 bps** (±5.5) | `+2.1 bps` | `-0.001 / +0.036` | `0.30%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,378.05 | ⚪ **CASH** | **+9.1 bps** (±2.4) | `+9.3 bps` | `+0.097 / -0.027` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.13 | ⚪ **CASH** | **+3.2 bps** (±6.9) | `+15.4 bps` | `-0.048 / -0.055` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 06:32:02 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,799.35 | ⚪ **CASH** | **+1.8 bps** (±5.5) | `+2.1 bps` | `-0.001 / +0.036` | `0.30%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,379.55 | ⚪ **CASH** | **+9.1 bps** (±2.4) | `+9.3 bps` | `+0.097 / -0.027` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.20 | ⚪ **CASH** | **+3.2 bps** (±6.9) | `+15.4 bps` | `-0.048 / -0.055` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 06:17:03 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,816.18 | ⚪ **CASH** | **+1.8 bps** (±5.5) | `+2.1 bps` | `-0.001 / +0.036` | `0.30%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,380.00 | ⚪ **CASH** | **+9.1 bps** (±2.4) | `+9.3 bps` | `+0.097 / -0.027` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.37 | ⚪ **CASH** | **+3.2 bps** (±6.9) | `+15.4 bps` | `-0.048 / -0.055` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 06:02:12 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,726.01 | ⚪ **CASH** | **+1.8 bps** (±5.5) | `+2.1 bps` | `-0.001 / +0.036` | `0.30%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,376.76 | ⚪ **CASH** | **+9.1 bps** (±2.4) | `+9.3 bps` | `+0.097 / -0.027` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.25 | ⚪ **CASH** | **+3.2 bps** (±6.9) | `+15.4 bps` | `-0.048 / -0.055` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 05:46:58 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,785.16 | ⚪ **CASH** | **-0.9 bps** (±3.9) | `-0.5 bps` | `-0.006 / +0.009` | `0.31%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,378.20 | ⚪ **CASH** | **+17.4 bps** (±1.0) | `+19.8 bps` | `+0.096 / +0.044` | `0.43%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.36 | ⚪ **CASH** | **+3.4 bps** (±8.2) | `+11.1 bps` | `-0.037 / +0.009` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 05:32:21 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,734.56 | ⚪ **CASH** | **-0.9 bps** (±3.9) | `-0.5 bps` | `-0.006 / +0.009` | `0.31%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,375.76 | ⚪ **CASH** | **+17.4 bps** (±1.0) | `+19.8 bps` | `+0.096 / +0.044` | `0.43%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.24 | ⚪ **CASH** | **+3.4 bps** (±8.2) | `+11.1 bps` | `-0.037 / +0.009` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 05:17:02 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,861.00 | ⚪ **CASH** | **-0.9 bps** (±3.9) | `-0.5 bps` | `-0.006 / +0.009` | `0.31%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,380.26 | ⚪ **CASH** | **+17.4 bps** (±1.0) | `+19.8 bps` | `+0.096 / +0.044` | `0.43%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.56 | ⚪ **CASH** | **+3.4 bps** (±8.2) | `+11.1 bps` | `-0.037 / +0.009` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 05:02:08 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,880.01 | ⚪ **CASH** | **-0.9 bps** (±3.9) | `-0.5 bps` | `-0.006 / +0.009` | `0.31%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,381.06 | ⚪ **CASH** | **+17.4 bps** (±1.0) | `+19.8 bps` | `+0.096 / +0.044` | `0.43%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.59 | ⚪ **CASH** | **+3.4 bps** (±8.2) | `+11.1 bps` | `-0.037 / +0.009` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 04:47:02 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,880.06 | ⚪ **CASH** | **-1.0 bps** (±5.4) | `+2.3 bps` | `-0.001 / -0.045` | `0.31%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,382.83 | ⚪ **CASH** | **+12.7 bps** (±12.9) | `+20.8 bps` | `+0.087 / -0.059` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.71 | ⚪ **CASH** | **+2.1 bps** (±7.2) | `+12.3 bps` | `-0.042 / -0.046` | `0.42%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 04:31:56 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,889.37 | ⚪ **CASH** | **-1.0 bps** (±5.4) | `+2.3 bps` | `-0.001 / -0.045` | `0.31%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,381.06 | ⚪ **CASH** | **+12.7 bps** (±12.9) | `+20.8 bps` | `+0.087 / -0.059` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.70 | ⚪ **CASH** | **+2.1 bps** (±7.2) | `+12.3 bps` | `-0.042 / -0.046` | `0.42%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 04:17:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,895.41 | ⚪ **CASH** | **-1.0 bps** (±5.4) | `+2.3 bps` | `-0.001 / -0.045` | `0.31%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,380.20 | ⚪ **CASH** | **+12.7 bps** (±12.9) | `+20.8 bps` | `+0.087 / -0.059` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.56 | ⚪ **CASH** | **+2.1 bps** (±7.2) | `+12.3 bps` | `-0.042 / -0.046` | `0.42%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 04:02:07 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,071.00 | ⚪ **CASH** | **-1.0 bps** (±5.4) | `+2.3 bps` | `-0.001 / -0.045` | `0.31%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,385.97 | ⚪ **CASH** | **+12.7 bps** (±12.9) | `+20.8 bps` | `+0.087 / -0.059` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.83 | ⚪ **CASH** | **+2.1 bps** (±7.2) | `+12.3 bps` | `-0.042 / -0.046` | `0.42%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 03:47:30 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,953.86 | ⚪ **CASH** | **-7.4 bps** (±2.5) | `-2.5 bps` | `-0.018 / -0.120` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,383.54 | ⚪ **CASH** | **+12.0 bps** (±10.2) | `+21.9 bps` | `+0.077 / -0.074` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.70 | ⚪ **CASH** | **+1.3 bps** (±8.9) | `+11.8 bps` | `-0.043 / -0.042` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 03:32:04 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,009.05 | ⚪ **CASH** | **-7.4 bps** (±2.5) | `-2.5 bps` | `-0.018 / -0.120` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,386.38 | ⚪ **CASH** | **+12.0 bps** (±10.2) | `+21.9 bps` | `+0.077 / -0.074` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.81 | ⚪ **CASH** | **+1.3 bps** (±8.9) | `+11.8 bps` | `-0.043 / -0.042` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 03:17:12 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,979.98 | ⚪ **CASH** | **-7.4 bps** (±2.5) | `-2.5 bps` | `-0.018 / -0.120` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,385.16 | ⚪ **CASH** | **+12.0 bps** (±10.2) | `+21.9 bps` | `+0.077 / -0.074` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.76 | ⚪ **CASH** | **+1.3 bps** (±8.9) | `+11.8 bps` | `-0.043 / -0.042` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 03:02:33 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,043.38 | ⚪ **CASH** | **-7.4 bps** (±2.5) | `-2.5 bps` | `-0.018 / -0.120` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,387.42 | ⚪ **CASH** | **+12.0 bps** (±10.2) | `+21.9 bps` | `+0.077 / -0.074` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.89 | ⚪ **CASH** | **+1.3 bps** (±8.9) | `+11.8 bps` | `-0.043 / -0.042` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 02:47:06 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,974.01 | ⚪ **CASH** | **-6.1 bps** (±6.8) | `-0.1 bps` | `-0.008 / -0.130` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,383.83 | ⚪ **CASH** | **+14.8 bps** (±12.8) | `+21.4 bps` | `+0.086 / -0.003` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.64 | ⚪ **CASH** | **-2.8 bps** (±9.8) | `+7.1 bps` | `-0.046 / -0.083` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 02:32:09 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,943.68 | ⚪ **CASH** | **-6.1 bps** (±6.8) | `-0.1 bps` | `-0.008 / -0.130` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,383.39 | ⚪ **CASH** | **+14.8 bps** (±12.8) | `+21.4 bps` | `+0.086 / -0.003` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.56 | ⚪ **CASH** | **-2.8 bps** (±9.8) | `+7.1 bps` | `-0.046 / -0.083` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 02:17:18 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,900.01 | ⚪ **CASH** | **-6.1 bps** (±6.8) | `-0.1 bps` | `-0.008 / -0.130` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,381.28 | ⚪ **CASH** | **+14.8 bps** (±12.8) | `+21.4 bps` | `+0.086 / -0.003` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.54 | ⚪ **CASH** | **-2.8 bps** (±9.8) | `+7.1 bps` | `-0.046 / -0.083` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 02:02:09 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,923.00 | ⚪ **CASH** | **-6.1 bps** (±6.8) | `-0.1 bps` | `-0.008 / -0.130` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,382.16 | ⚪ **CASH** | **+14.8 bps** (±12.8) | `+21.4 bps` | `+0.086 / -0.003` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.56 | ⚪ **CASH** | **-2.8 bps** (±9.8) | `+7.1 bps` | `-0.046 / -0.083` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 01:46:57 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,880.62 | ⚪ **CASH** | **-3.5 bps** (±4.3) | `+4.3 bps` | `+0.007 / -0.167` | `0.31%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,380.29 | ⚪ **CASH** | **+20.6 bps** (±7.2) | `+26.5 bps` | `+0.103 / +0.028` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.51 | ⚪ **CASH** | **+0.6 bps** (±8.8) | `+14.0 bps` | `-0.048 / -0.106` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 01:32:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,783.18 | ⚪ **CASH** | **-3.5 bps** (±4.3) | `+4.3 bps` | `+0.007 / -0.167` | `0.31%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,374.37 | ⚪ **CASH** | **+20.6 bps** (±7.2) | `+26.5 bps` | `+0.103 / +0.028` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.38 | ⚪ **CASH** | **+0.6 bps** (±8.8) | `+14.0 bps` | `-0.048 / -0.106` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 01:17:00 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,832.01 | ⚪ **CASH** | **-3.5 bps** (±4.3) | `+4.3 bps` | `+0.007 / -0.167` | `0.31%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,380.61 | ⚪ **CASH** | **+20.6 bps** (±7.2) | `+26.5 bps` | `+0.103 / +0.028` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.63 | ⚪ **CASH** | **+0.6 bps** (±8.8) | `+14.0 bps` | `-0.048 / -0.106` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
