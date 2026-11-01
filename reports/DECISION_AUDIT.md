# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-01 15:17:24 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-01 15:17:24 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,064.00 | ⚪ **CASH** | **+8.5 bps** (±7.7) | `-5.3 bps` | `+0.154 / -0.008` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,270.32 | ⚪ **CASH** | **+1.3 bps** (±4.3) | `-4.6 bps` | `+0.032 / -0.045` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.99 | ⚪ **CASH** | **-78.3 bps** (±18.9) | `-130.9 bps` | `-0.066 / -0.138` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 15:02:37 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,058.52 | ⚪ **CASH** | **+8.5 bps** (±7.7) | `-5.3 bps` | `+0.154 / -0.008` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,272.48 | ⚪ **CASH** | **+1.3 bps** (±4.3) | `-4.6 bps` | `+0.032 / -0.045` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.08 | ⚪ **CASH** | **-78.3 bps** (±18.9) | `-130.9 bps` | `-0.066 / -0.138` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 14:47:24 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,058.51 | ⚪ **CASH** | **+10.3 bps** (±6.6) | `-0.6 bps` | `+0.154 / -0.033` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,272.08 | ⚪ **CASH** | **+2.7 bps** (±4.9) | `-5.2 bps` | `+0.025 / +0.015` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.09 | ⚪ **CASH** | **-81.1 bps** (±22.7) | `-137.7 bps` | `-0.068 / -0.099` | `0.53%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 14:32:21 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,028.01 | ⚪ **CASH** | **+10.3 bps** (±6.6) | `-0.6 bps` | `+0.154 / -0.033` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,269.68 | ⚪ **CASH** | **+2.7 bps** (±4.9) | `-5.2 bps` | `+0.025 / +0.015` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.12 | ⚪ **CASH** | **-81.1 bps** (±22.7) | `-137.7 bps` | `-0.068 / -0.099` | `0.53%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 14:17:21 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,000.00 | ⚪ **CASH** | **+10.3 bps** (±6.6) | `-0.6 bps` | `+0.154 / -0.033` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,267.98 | ⚪ **CASH** | **+2.7 bps** (±4.9) | `-5.2 bps` | `+0.025 / +0.015` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.10 | ⚪ **CASH** | **-81.1 bps** (±22.7) | `-137.7 bps` | `-0.068 / -0.099` | `0.53%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 13:47:16 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,955.04 | ⚪ **CASH** | **+12.0 bps** (±6.9) | `-1.5 bps` | `+0.170 / -0.007` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,267.36 | ⚪ **CASH** | **-4.7 bps** (±5.7) | `-16.7 bps` | `+0.022 / -0.021` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.93 | ⚪ **CASH** | **-83.5 bps** (±20.5) | `-143.4 bps` | `-0.068 / -0.096` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 13:32:31 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,990.98 | ⚪ **CASH** | **+12.0 bps** (±6.9) | `-1.5 bps` | `+0.170 / -0.007` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,267.48 | ⚪ **CASH** | **-4.7 bps** (±5.7) | `-16.7 bps` | `+0.022 / -0.021` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.09 | ⚪ **CASH** | **-83.5 bps** (±20.5) | `-143.4 bps` | `-0.068 / -0.096` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 13:17:30 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,008.25 | ⚪ **CASH** | **+12.0 bps** (±6.9) | `-1.5 bps` | `+0.170 / -0.007` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,266.71 | ⚪ **CASH** | **-4.7 bps** (±5.7) | `-16.7 bps` | `+0.022 / -0.021` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.06 | ⚪ **CASH** | **-83.5 bps** (±20.5) | `-143.4 bps` | `-0.068 / -0.096` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 13:02:31 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,948.24 | ⚪ **CASH** | **+12.0 bps** (±6.9) | `-1.5 bps` | `+0.170 / -0.007` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,263.61 | ⚪ **CASH** | **-4.7 bps** (±5.7) | `-16.7 bps` | `+0.022 / -0.021` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.96 | ⚪ **CASH** | **-83.5 bps** (±20.5) | `-143.4 bps` | `-0.068 / -0.096` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 12:47:23 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,883.02 | ⚪ **CASH** | **+16.8 bps** (±7.5) | `-0.3 bps` | `+0.187 / +0.071` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,261.81 | ⚪ **CASH** | **+9.9 bps** (±7.8) | `+1.8 bps` | `+0.052 / +0.053` | `0.42%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.87 | ⚪ **CASH** | **-74.4 bps** (±16.4) | `-132.8 bps` | `-0.051 / -0.057` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 12:32:19 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,823.54 | ⚪ **CASH** | **+16.8 bps** (±7.5) | `-0.3 bps` | `+0.187 / +0.071` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,259.77 | ⚪ **CASH** | **+9.9 bps** (±7.8) | `+1.8 bps` | `+0.052 / +0.053` | `0.42%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.51 | ⚪ **CASH** | **-74.4 bps** (±16.4) | `-132.8 bps` | `-0.051 / -0.057` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 12:17:19 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,801.29 | ⚪ **CASH** | **+16.8 bps** (±7.5) | `-0.3 bps` | `+0.187 / +0.071` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,260.34 | ⚪ **CASH** | **+9.9 bps** (±7.8) | `+1.8 bps` | `+0.052 / +0.053` | `0.42%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.78 | ⚪ **CASH** | **-74.4 bps** (±16.4) | `-132.8 bps` | `-0.051 / -0.057` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 12:02:45 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,012.05 | ⚪ **CASH** | **+16.8 bps** (±7.5) | `-0.3 bps` | `+0.187 / +0.071` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,270.79 | ⚪ **CASH** | **+9.9 bps** (±7.8) | `+1.8 bps` | `+0.052 / +0.053` | `0.42%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.37 | ⚪ **CASH** | **-74.4 bps** (±16.4) | `-132.8 bps` | `-0.051 / -0.057` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 11:47:12 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,953.79 | ⚪ **CASH** | **+20.4 bps** (±6.3) | `+4.6 bps` | `+0.193 / +0.080` | `0.35%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,269.10 | ⚪ **CASH** | **+8.1 bps** (±9.8) | `+2.4 bps` | `+0.040 / +0.012` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.26 | ⚪ **CASH** | **-71.3 bps** (±24.6) | `-127.6 bps` | `-0.045 / -0.041` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 11:32:29 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,972.00 | ⚪ **CASH** | **+20.4 bps** (±6.3) | `+4.6 bps` | `+0.193 / +0.080` | `0.35%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,268.28 | ⚪ **CASH** | **+8.1 bps** (±9.8) | `+2.4 bps` | `+0.040 / +0.012` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.28 | ⚪ **CASH** | **-71.3 bps** (±24.6) | `-127.6 bps` | `-0.045 / -0.041` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 11:17:27 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,008.01 | ⚪ **CASH** | **+20.4 bps** (±6.3) | `+4.6 bps` | `+0.193 / +0.080` | `0.35%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,270.75 | ⚪ **CASH** | **+8.1 bps** (±9.8) | `+2.4 bps` | `+0.040 / +0.012` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.40 | ⚪ **CASH** | **-71.3 bps** (±24.6) | `-127.6 bps` | `-0.045 / -0.041` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 11:02:44 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,037.89 | ⚪ **CASH** | **+20.4 bps** (±6.3) | `+4.6 bps` | `+0.193 / +0.080` | `0.35%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,269.51 | ⚪ **CASH** | **+8.1 bps** (±9.8) | `+2.4 bps` | `+0.040 / +0.012` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.45 | ⚪ **CASH** | **-71.3 bps** (±24.6) | `-127.6 bps` | `-0.045 / -0.041` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 10:47:16 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,052.01 | ⚪ **CASH** | **+19.8 bps** (±5.0) | `+0.9 bps` | `+0.199 / +0.102` | `0.35%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,271.02 | ⚪ **CASH** | **+7.6 bps** (±9.5) | `+2.6 bps` | `+0.038 / -0.007` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.42 | ⚪ **CASH** | **-59.8 bps** (±28.7) | `-108.9 bps` | `-0.030 / -0.024` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 10:32:42 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,100.01 | ⚪ **CASH** | **+19.8 bps** (±5.0) | `+0.9 bps` | `+0.199 / +0.102` | `0.35%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,271.55 | ⚪ **CASH** | **+7.6 bps** (±9.5) | `+2.6 bps` | `+0.038 / -0.007` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.53 | ⚪ **CASH** | **-59.8 bps** (±28.7) | `-108.9 bps` | `-0.030 / -0.024` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 10:17:16 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,156.66 | ⚪ **CASH** | **+19.8 bps** (±5.0) | `+0.9 bps` | `+0.199 / +0.102` | `0.35%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,272.59 | ⚪ **CASH** | **+7.6 bps** (±9.5) | `+2.6 bps` | `+0.038 / -0.007` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.58 | ⚪ **CASH** | **-59.8 bps** (±28.7) | `-108.9 bps` | `-0.030 / -0.024` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 10:02:46 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,090.33 | ⚪ **CASH** | **+19.8 bps** (±5.0) | `+0.9 bps` | `+0.199 / +0.102` | `0.35%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,269.58 | ⚪ **CASH** | **+7.6 bps** (±9.5) | `+2.6 bps` | `+0.038 / -0.007` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.45 | ⚪ **CASH** | **-59.8 bps** (±28.7) | `-108.9 bps` | `-0.030 / -0.024` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 09:47:19 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,091.00 | ⚪ **CASH** | **+22.0 bps** (±8.3) | `+1.7 bps` | `+0.214 / +0.127` | `0.36%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,272.10 | ⚪ **CASH** | **+16.7 bps** (±14.0) | `+12.9 bps` | `+0.056 / +0.060` | `0.44%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.62 | ⚪ **CASH** | **-59.0 bps** (±28.7) | `-117.3 bps` | `+0.024 / +0.037` | `0.56%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 09:32:45 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,006.39 | ⚪ **CASH** | **+22.0 bps** (±8.3) | `+1.7 bps` | `+0.214 / +0.127` | `0.36%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,268.86 | ⚪ **CASH** | **+16.7 bps** (±14.0) | `+12.9 bps` | `+0.056 / +0.060` | `0.44%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.35 | ⚪ **CASH** | **-59.0 bps** (±28.7) | `-117.3 bps` | `+0.024 / +0.037` | `0.56%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 09:17:14 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,227.49 | ⚪ **CASH** | **+22.0 bps** (±8.3) | `+1.7 bps` | `+0.214 / +0.127` | `0.36%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,274.46 | ⚪ **CASH** | **+16.7 bps** (±14.0) | `+12.9 bps` | `+0.056 / +0.060` | `0.44%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.79 | ⚪ **CASH** | **-59.0 bps** (±28.7) | `-117.3 bps` | `+0.024 / +0.037` | `0.56%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 09:02:19 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,251.45 | ⚪ **CASH** | **+22.0 bps** (±8.3) | `+1.7 bps` | `+0.214 / +0.127` | `0.36%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,275.29 | ⚪ **CASH** | **+16.7 bps** (±14.0) | `+12.9 bps` | `+0.056 / +0.060` | `0.44%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.90 | ⚪ **CASH** | **-59.0 bps** (±28.7) | `-117.3 bps` | `+0.024 / +0.037` | `0.56%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 08:47:16 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,216.75 | ⚪ **CASH** | **+14.7 bps** (±8.3) | `-14.9 bps` | `+0.224 / +0.153` | `0.35%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,273.78 | ⚪ **CASH** | **+4.7 bps** (±7.8) | `+0.2 bps` | `+0.027 / -0.057` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.76 | ⚪ **CASH** | **-72.2 bps** (±21.3) | `-137.3 bps` | `+0.010 / -0.033` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 08:32:37 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,050.50 | ⚪ **CASH** | **+14.7 bps** (±8.3) | `-14.9 bps` | `+0.224 / +0.153` | `0.35%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,272.39 | ⚪ **CASH** | **+4.7 bps** (±7.8) | `+0.2 bps` | `+0.027 / -0.057` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.50 | ⚪ **CASH** | **-72.2 bps** (±21.3) | `-137.3 bps` | `+0.010 / -0.033` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 08:17:12 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,943.01 | ⚪ **CASH** | **+14.7 bps** (±8.3) | `-14.9 bps` | `+0.224 / +0.153` | `0.35%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,268.53 | ⚪ **CASH** | **+4.7 bps** (±7.8) | `+0.2 bps` | `+0.027 / -0.057` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.39 | ⚪ **CASH** | **-72.2 bps** (±21.3) | `-137.3 bps` | `+0.010 / -0.033` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 08:02:33 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,004.01 | ⚪ **CASH** | **+14.7 bps** (±8.3) | `-14.9 bps` | `+0.224 / +0.153` | `0.35%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,270.71 | ⚪ **CASH** | **+4.7 bps** (±7.8) | `+0.2 bps` | `+0.027 / -0.057` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.58 | ⚪ **CASH** | **-72.2 bps** (±21.3) | `-137.3 bps` | `+0.010 / -0.033` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 07:47:34 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,914.00 | ⚪ **CASH** | **+11.1 bps** (±9.8) | `-17.7 bps` | `+0.224 / +0.102` | `0.36%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,268.23 | ⚪ **CASH** | **+12.1 bps** (±18.1) | `+8.1 bps` | `+0.031 / +0.047` | `0.45%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.51 | ⚪ **CASH** | **-66.4 bps** (±17.1) | `-127.6 bps` | `+0.008 / -0.027` | `0.57%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 07:32:33 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,916.85 | ⚪ **CASH** | **+11.1 bps** (±9.8) | `-17.7 bps` | `+0.224 / +0.102` | `0.36%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,267.95 | ⚪ **CASH** | **+12.1 bps** (±18.1) | `+8.1 bps` | `+0.031 / +0.047` | `0.45%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.49 | ⚪ **CASH** | **-66.4 bps** (±17.1) | `-127.6 bps` | `+0.008 / -0.027` | `0.57%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 07:17:14 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,870.84 | ⚪ **CASH** | **+11.1 bps** (±9.8) | `-17.7 bps` | `+0.224 / +0.102` | `0.36%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,266.25 | ⚪ **CASH** | **+12.1 bps** (±18.1) | `+8.1 bps` | `+0.031 / +0.047` | `0.45%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.44 | ⚪ **CASH** | **-66.4 bps** (±17.1) | `-127.6 bps` | `+0.008 / -0.027` | `0.57%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 07:02:21 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,005.90 | ⚪ **CASH** | **+11.1 bps** (±9.8) | `-17.7 bps` | `+0.224 / +0.102` | `0.36%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,269.54 | ⚪ **CASH** | **+12.1 bps** (±18.1) | `+8.1 bps` | `+0.031 / +0.047` | `0.45%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.65 | ⚪ **CASH** | **-66.4 bps** (±17.1) | `-127.6 bps` | `+0.008 / -0.027` | `0.57%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 06:47:25 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,947.75 | ⚪ **CASH** | **+5.6 bps** (±13.8) | `-27.3 bps` | `+0.243 / +0.062` | `0.36%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,268.68 | ⚪ **CASH** | **+11.3 bps** (±4.8) | `-0.3 bps` | `+0.029 / +0.108` | `0.45%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.59 | ⚪ **CASH** | **-53.9 bps** (±24.1) | `-106.6 bps` | `+0.007 / +0.004` | `0.58%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 06:32:21 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,978.90 | ⚪ **CASH** | **+5.6 bps** (±13.8) | `-27.3 bps` | `+0.243 / +0.062` | `0.36%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,269.50 | ⚪ **CASH** | **+11.3 bps** (±4.8) | `-0.3 bps` | `+0.029 / +0.108` | `0.45%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.68 | ⚪ **CASH** | **-53.9 bps** (±24.1) | `-106.6 bps` | `+0.007 / +0.004` | `0.58%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 06:17:14 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,962.52 | ⚪ **CASH** | **+5.6 bps** (±13.8) | `-27.3 bps` | `+0.243 / +0.062` | `0.36%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,271.04 | ⚪ **CASH** | **+11.3 bps** (±4.8) | `-0.3 bps` | `+0.029 / +0.108` | `0.45%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.90 | ⚪ **CASH** | **-53.9 bps** (±24.1) | `-106.6 bps` | `+0.007 / +0.004` | `0.58%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
