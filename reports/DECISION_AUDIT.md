# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-22 08:02:14 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-22 08:02:14 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,223.84 | ⚪ **CASH** | **-13.5 bps** (±3.2) | `+6.4 bps` | `-0.109 / -0.217` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,428.47 | ⚪ **CASH** | **+2.2 bps** (±10.1) | `+20.2 bps` | `-0.018 / -0.110` | `0.47%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.37 | ⚪ **CASH** | **-1.6 bps** (±7.5) | `+23.0 bps` | `-0.026 / -0.255` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 07:47:02 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,302.78 | ⚪ **CASH** | **-11.3 bps** (±3.9) | `+12.3 bps` | `-0.102 / -0.262` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,431.43 | ⚪ **CASH** | **-1.4 bps** (±5.8) | `+17.6 bps` | `-0.013 / -0.195` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.39 | ⚪ **CASH** | **-11.3 bps** (±11.0) | `+2.7 bps` | `-0.007 / -0.236` | `0.52%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 07:32:31 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,270.34 | ⚪ **CASH** | **-11.3 bps** (±3.9) | `+12.3 bps` | `-0.102 / -0.262` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,427.45 | ⚪ **CASH** | **-1.4 bps** (±5.8) | `+17.6 bps` | `-0.013 / -0.195` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.37 | ⚪ **CASH** | **-11.3 bps** (±11.0) | `+2.7 bps` | `-0.007 / -0.236` | `0.52%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 07:17:12 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,340.99 | ⚪ **CASH** | **-11.3 bps** (±3.9) | `+12.3 bps` | `-0.102 / -0.262` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,429.37 | ⚪ **CASH** | **-1.4 bps** (±5.8) | `+17.6 bps` | `-0.013 / -0.195` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.42 | ⚪ **CASH** | **-11.3 bps** (±11.0) | `+2.7 bps` | `-0.007 / -0.236` | `0.52%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 07:02:13 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,516.87 | ⚪ **CASH** | **-11.3 bps** (±3.9) | `+12.3 bps` | `-0.102 / -0.262` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,434.45 | ⚪ **CASH** | **-1.4 bps** (±5.8) | `+17.6 bps` | `-0.013 / -0.195` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.63 | ⚪ **CASH** | **-11.3 bps** (±11.0) | `+2.7 bps` | `-0.007 / -0.236` | `0.52%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 06:47:29 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,508.31 | ⚪ **CASH** | **-15.9 bps** (±5.1) | `+5.7 bps` | `-0.099 / -0.293` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,429.99 | ⚪ **CASH** | **+0.8 bps** (±5.8) | `+20.3 bps` | `-0.015 / -0.177` | `0.48%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.49 | ⚪ **CASH** | **-2.2 bps** (±9.6) | `+13.9 bps` | `+0.007 / -0.183` | `0.52%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 06:32:00 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,590.00 | ⚪ **CASH** | **-15.9 bps** (±5.1) | `+5.7 bps` | `-0.099 / -0.293` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,433.46 | ⚪ **CASH** | **+0.8 bps** (±5.8) | `+20.3 bps` | `-0.015 / -0.177` | `0.48%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.64 | ⚪ **CASH** | **-2.2 bps** (±9.6) | `+13.9 bps` | `+0.007 / -0.183` | `0.52%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 06:17:10 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,808.40 | ⚪ **CASH** | **-15.9 bps** (±5.1) | `+5.7 bps` | `-0.099 / -0.293` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,440.10 | ⚪ **CASH** | **+0.8 bps** (±5.8) | `+20.3 bps` | `-0.015 / -0.177` | `0.48%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.99 | ⚪ **CASH** | **-2.2 bps** (±9.6) | `+13.9 bps` | `+0.007 / -0.183` | `0.52%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 06:02:04 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,825.53 | ⚪ **CASH** | **-15.9 bps** (±5.1) | `+5.7 bps` | `-0.099 / -0.293` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,439.54 | ⚪ **CASH** | **+0.8 bps** (±5.8) | `+20.3 bps` | `-0.015 / -0.177` | `0.48%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.02 | ⚪ **CASH** | **-2.2 bps** (±9.6) | `+13.9 bps` | `+0.007 / -0.183` | `0.52%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 05:46:56 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,809.34 | ⚪ **CASH** | **-14.6 bps** (±4.3) | `+6.7 bps` | `-0.089 / -0.296` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,438.70 | ⚪ **CASH** | **+3.9 bps** (±3.5) | `+23.3 bps` | `-0.010 / -0.156` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.02 | ⚪ **CASH** | **-3.4 bps** (±10.1) | `+3.6 bps` | `+0.034 / -0.104` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 05:32:15 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,814.01 | ⚪ **CASH** | **-14.6 bps** (±4.3) | `+6.7 bps` | `-0.089 / -0.296` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,440.61 | ⚪ **CASH** | **+3.9 bps** (±3.5) | `+23.3 bps` | `-0.010 / -0.156` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.14 | ⚪ **CASH** | **-3.4 bps** (±10.1) | `+3.6 bps` | `+0.034 / -0.104` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 05:17:01 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,804.17 | ⚪ **CASH** | **-14.6 bps** (±4.3) | `+6.7 bps` | `-0.089 / -0.296` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,441.41 | ⚪ **CASH** | **+3.9 bps** (±3.5) | `+23.3 bps` | `-0.010 / -0.156` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.17 | ⚪ **CASH** | **-3.4 bps** (±10.1) | `+3.6 bps` | `+0.034 / -0.104` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 05:02:14 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,902.73 | ⚪ **CASH** | **-14.6 bps** (±4.3) | `+6.7 bps` | `-0.089 / -0.296` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,446.66 | ⚪ **CASH** | **+3.9 bps** (±3.5) | `+23.3 bps` | `-0.010 / -0.156` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.60 | ⚪ **CASH** | **-3.4 bps** (±10.1) | `+3.6 bps` | `+0.034 / -0.104` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 04:47:08 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,857.20 | ⚪ **CASH** | **-10.9 bps** (±6.0) | `+13.4 bps` | `-0.079 / -0.314` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,443.43 | ⚪ **CASH** | **+6.6 bps** (±2.4) | `+28.5 bps` | `-0.006 / -0.177` | `0.49%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.41 | ⚪ **CASH** | **-5.4 bps** (±9.7) | `-0.4 bps` | `+0.037 / -0.113` | `0.53%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 04:32:09 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,900.57 | ⚪ **CASH** | **-10.9 bps** (±6.0) | `+13.4 bps` | `-0.079 / -0.314` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,446.04 | ⚪ **CASH** | **+6.6 bps** (±2.4) | `+28.5 bps` | `-0.006 / -0.177` | `0.49%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.51 | ⚪ **CASH** | **-5.4 bps** (±9.7) | `-0.4 bps` | `+0.037 / -0.113` | `0.53%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 04:17:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,915.45 | ⚪ **CASH** | **-10.9 bps** (±6.0) | `+13.4 bps` | `-0.079 / -0.314` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,445.06 | ⚪ **CASH** | **+6.6 bps** (±2.4) | `+28.5 bps` | `-0.006 / -0.177` | `0.49%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.52 | ⚪ **CASH** | **-5.4 bps** (±9.7) | `-0.4 bps` | `+0.037 / -0.113` | `0.53%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 04:02:03 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,937.90 | ⚪ **CASH** | **-10.9 bps** (±6.0) | `+13.4 bps` | `-0.079 / -0.314` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,446.08 | ⚪ **CASH** | **+6.6 bps** (±2.4) | `+28.5 bps` | `-0.006 / -0.177` | `0.49%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.66 | ⚪ **CASH** | **-5.4 bps** (±9.7) | `-0.4 bps` | `+0.037 / -0.113` | `0.53%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 03:47:15 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,916.31 | ⚪ **CASH** | **-6.2 bps** (±3.9) | `+18.3 bps` | `-0.068 / -0.290` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,443.84 | ⚪ **CASH** | **+10.0 bps** (±3.7) | `+35.0 bps` | `-0.007 / -0.185` | `0.50%/h` | `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.45 | ⚪ **CASH** | **+4.0 bps** (±10.1) | `+8.0 bps` | `+0.062 / -0.026` | `0.54%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 03:32:10 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,762.11 | ⚪ **CASH** | **-6.2 bps** (±3.9) | `+18.3 bps` | `-0.068 / -0.290` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,437.20 | ⚪ **CASH** | **+10.0 bps** (±3.7) | `+35.0 bps` | `-0.007 / -0.185` | `0.50%/h` | `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.29 | ⚪ **CASH** | **+4.0 bps** (±10.1) | `+8.0 bps` | `+0.062 / -0.026` | `0.54%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 03:17:02 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,853.13 | ⚪ **CASH** | **-6.2 bps** (±3.9) | `+18.3 bps` | `-0.068 / -0.290` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,441.17 | ⚪ **CASH** | **+10.0 bps** (±3.7) | `+35.0 bps` | `-0.007 / -0.185` | `0.50%/h` | `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.56 | ⚪ **CASH** | **+4.0 bps** (±10.1) | `+8.0 bps` | `+0.062 / -0.026` | `0.54%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 03:02:16 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,960.07 | ⚪ **CASH** | **-6.2 bps** (±3.9) | `+18.3 bps` | `-0.068 / -0.290` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,444.51 | ⚪ **CASH** | **+10.0 bps** (±3.7) | `+35.0 bps` | `-0.007 / -0.185` | `0.50%/h` | `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.70 | ⚪ **CASH** | **+4.0 bps** (±10.1) | `+8.0 bps` | `+0.062 / -0.026` | `0.54%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 02:47:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,959.60 | ⚪ **CASH** | **-11.4 bps** (±5.0) | `+4.2 bps` | `-0.042 / -0.273` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,440.85 | ⚪ **CASH** | **+8.1 bps** (±5.5) | `+25.2 bps` | `-0.003 / -0.109` | `0.50%/h` | `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.64 | ⚪ **CASH** | **+5.9 bps** (±12.2) | `+8.2 bps` | `+0.058 / +0.016` | `0.53%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 02:32:30 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,922.89 | ⚪ **CASH** | **-11.4 bps** (±5.0) | `+4.2 bps` | `-0.042 / -0.273` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,441.39 | ⚪ **CASH** | **+8.1 bps** (±5.5) | `+25.2 bps` | `-0.003 / -0.109` | `0.50%/h` | `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.45 | ⚪ **CASH** | **+5.9 bps** (±12.2) | `+8.2 bps` | `+0.058 / +0.016` | `0.53%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 02:17:17 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,266.40 | ⚪ **CASH** | **-11.4 bps** (±5.0) | `+4.2 bps` | `-0.042 / -0.273` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,448.66 | ⚪ **CASH** | **+8.1 bps** (±5.5) | `+25.2 bps` | `-0.003 / -0.109` | `0.50%/h` | `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.95 | ⚪ **CASH** | **+5.9 bps** (±12.2) | `+8.2 bps` | `+0.058 / +0.016` | `0.53%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 02:02:11 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,478.70 | ⚪ **CASH** | **-11.4 bps** (±5.0) | `+4.2 bps` | `-0.042 / -0.273` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,453.89 | 🔴 **SELL** | **+8.1 bps** (±5.5) | `+25.2 bps` | `-0.003 / -0.109` | `0.50%/h` | `weak_order_flow` | Stop Loss técnico acionado (-1.45%) |
| **SOLUSDT** | $106.24 | ⚪ **CASH** | **+5.9 bps** (±12.2) | `+8.2 bps` | `+0.058 / +0.016` | `0.53%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 01:47:09 UTC` | Patrimônio: **$995.27 USDT** (Caixa: `$669.53`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,731.34 | ⚪ **CASH** | **-19.4 bps** (±5.3) | `-17.0 bps` | `-0.024 / -0.210` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,458.11 | 🟡 **HOLD** | **-1.6 bps** (±5.6) | `+2.8 bps` | `+0.014 / -0.075` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 6.7h (PnL: -1.28% | Pico: +0.40%) |
| **SOLUSDT** | $106.48 | ⚪ **CASH** | **+17.2 bps** (±9.6) | `+19.7 bps` | `+0.064 / +0.126` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 01:32:12 UTC` | Patrimônio: **$997.55 USDT** (Caixa: `$669.53`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,244.10 | ⚪ **CASH** | **-19.4 bps** (±5.3) | `-17.0 bps` | `-0.024 / -0.210` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,475.34 | 🟡 **HOLD** | **-1.6 bps** (±5.6) | `+2.8 bps` | `+0.014 / -0.075` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 6.5h (PnL: -0.59% | Pico: +0.40%) |
| **SOLUSDT** | $107.20 | ⚪ **CASH** | **+17.2 bps** (±9.6) | `+19.7 bps` | `+0.064 / +0.126` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 01:17:09 UTC` | Patrimônio: **$997.89 USDT** (Caixa: `$669.53`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,341.96 | ⚪ **CASH** | **-19.4 bps** (±5.3) | `-17.0 bps` | `-0.024 / -0.210` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,477.90 | 🟡 **HOLD** | **-1.6 bps** (±5.6) | `+2.8 bps` | `+0.014 / -0.075` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 6.2h (PnL: -0.49% | Pico: +0.40%) |
| **SOLUSDT** | $107.44 | ⚪ **CASH** | **+17.2 bps** (±9.6) | `+19.7 bps` | `+0.064 / +0.126` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 01:02:16 UTC` | Patrimônio: **$996.89 USDT** (Caixa: `$669.53`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,115.83 | ⚪ **CASH** | **-19.4 bps** (±5.3) | `-17.0 bps` | `-0.024 / -0.210` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,470.32 | 🟡 **HOLD** | **-1.6 bps** (±5.6) | `+2.8 bps` | `+0.014 / -0.075` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 6.0h (PnL: -0.79% | Pico: +0.40%) |
| **SOLUSDT** | $107.10 | ⚪ **CASH** | **+17.2 bps** (±9.6) | `+19.7 bps` | `+0.064 / +0.126` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 00:47:10 UTC` | Patrimônio: **$997.88 USDT** (Caixa: `$669.53`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,318.04 | ⚪ **CASH** | **-17.7 bps** (±5.5) | `-16.0 bps` | `-0.016 / -0.195` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,477.83 | 🟡 **HOLD** | **-3.9 bps** (±10.0) | `-1.2 bps` | `+0.014 / -0.071` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 5.7h (PnL: -0.49% | Pico: +0.40%) |
| **SOLUSDT** | $107.41 | ⚪ **CASH** | **+17.8 bps** (±10.7) | `+24.1 bps` | `+0.056 / +0.084` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 00:32:08 UTC` | Patrimônio: **$997.48 USDT** (Caixa: `$669.53`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,219.73 | ⚪ **CASH** | **-17.7 bps** (±5.5) | `-16.0 bps` | `-0.016 / -0.195` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,474.84 | 🟡 **HOLD** | **-3.9 bps** (±10.0) | `-1.2 bps` | `+0.014 / -0.071` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 5.5h (PnL: -0.61% | Pico: +0.40%) |
| **SOLUSDT** | $107.25 | ⚪ **CASH** | **+17.8 bps** (±10.7) | `+24.1 bps` | `+0.056 / +0.084` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 00:16:55 UTC` | Patrimônio: **$998.00 USDT** (Caixa: `$669.53`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,234.20 | ⚪ **CASH** | **-17.7 bps** (±5.5) | `-16.0 bps` | `-0.016 / -0.195` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,478.70 | 🟡 **HOLD** | **-3.9 bps** (±10.0) | `-1.2 bps` | `+0.014 / -0.071` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 5.2h (PnL: -0.45% | Pico: +0.40%) |
| **SOLUSDT** | $107.26 | ⚪ **CASH** | **+17.8 bps** (±10.7) | `+24.1 bps` | `+0.056 / +0.084` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 00:02:04 UTC` | Patrimônio: **$997.45 USDT** (Caixa: `$669.53`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,138.00 | ⚪ **CASH** | **-17.7 bps** (±5.5) | `-16.0 bps` | `-0.016 / -0.195` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,474.59 | 🟡 **HOLD** | **-3.9 bps** (±10.0) | `-1.2 bps` | `+0.014 / -0.071` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 5.0h (PnL: -0.62% | Pico: +0.40%) |
| **SOLUSDT** | $107.06 | ⚪ **CASH** | **+17.8 bps** (±10.7) | `+24.1 bps` | `+0.056 / +0.084` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 23:47:14 UTC` | Patrimônio: **$997.39 USDT** (Caixa: `$669.53`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,251.13 | ⚪ **CASH** | **-6.7 bps** (±3.8) | `+0.4 bps` | `-0.004 / -0.174` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,474.10 | 🟡 **HOLD** | **+14.4 bps** (±8.1) | `+27.9 bps` | `+0.017 / -0.027` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 4.8h (PnL: -0.64% | Pico: +0.40%) |
| **SOLUSDT** | $106.84 | ⚪ **CASH** | **+21.0 bps** (±10.4) | `+27.1 bps` | `+0.056 / +0.115` | `0.52%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 23:32:07 UTC` | Patrimônio: **$997.73 USDT** (Caixa: `$669.53`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,310.81 | ⚪ **CASH** | **-6.7 bps** (±3.8) | `+0.4 bps` | `-0.004 / -0.174` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,476.72 | 🟡 **HOLD** | **+14.4 bps** (±8.1) | `+27.9 bps` | `+0.017 / -0.027` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 4.5h (PnL: -0.53% | Pico: +0.40%) |
| **SOLUSDT** | $107.00 | ⚪ **CASH** | **+21.0 bps** (±10.4) | `+27.1 bps` | `+0.056 / +0.115` | `0.52%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 23:17:15 UTC` | Patrimônio: **$998.17 USDT** (Caixa: `$669.53`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,340.31 | ⚪ **CASH** | **-6.7 bps** (±3.8) | `+0.4 bps` | `-0.004 / -0.174` | `0.32%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,480.01 | 🟡 **HOLD** | **+14.4 bps** (±8.1) | `+27.9 bps` | `+0.017 / -0.027` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 4.3h (PnL: -0.40% | Pico: +0.40%) |
| **SOLUSDT** | $107.17 | ⚪ **CASH** | **+21.0 bps** (±10.4) | `+27.1 bps` | `+0.056 / +0.115` | `0.52%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
