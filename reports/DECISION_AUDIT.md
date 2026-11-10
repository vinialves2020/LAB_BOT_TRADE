# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-10 14:15:36 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-10 14:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,917.61 | ⚪ **CASH** | **-38.5 bps** (±7.5) | `-87.8 bps` | `+0.116 / +0.031` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,068.13 | ⚪ **CASH** | **-11.0 bps** (±7.4) | `-18.2 bps` | `-0.024 / -0.057` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.11 | ⚪ **CASH** | **-5.6 bps** (±11.8) | `-10.7 bps` | `+0.040 / -0.106` | `0.63%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 14:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,871.55 | ⚪ **CASH** | **-38.5 bps** (±7.5) | `-87.8 bps` | `+0.116 / +0.031` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,069.87 | ⚪ **CASH** | **-11.0 bps** (±7.4) | `-18.2 bps` | `-0.024 / -0.057` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.30 | ⚪ **CASH** | **-5.6 bps** (±11.8) | `-10.7 bps` | `+0.040 / -0.106` | `0.63%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 13:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,930.26 | ⚪ **CASH** | **-32.1 bps** (±8.0) | `-86.5 bps` | `+0.141 / +0.134` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,070.62 | ⚪ **CASH** | **-4.6 bps** (±3.2) | `-8.9 bps` | `-0.017 / -0.063` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.32 | ⚪ **CASH** | **+6.8 bps** (±6.1) | `+8.2 bps` | `+0.060 / -0.116` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 13:30:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,042.27 | ⚪ **CASH** | **-32.1 bps** (±8.0) | `-86.5 bps` | `+0.141 / +0.134` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,060.84 | ⚪ **CASH** | **-4.6 bps** (±3.2) | `-8.9 bps` | `-0.017 / -0.063` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.77 | ⚪ **CASH** | **+6.8 bps** (±6.1) | `+8.2 bps` | `+0.060 / -0.116` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 13:15:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,308.70 | ⚪ **CASH** | **-32.1 bps** (±8.0) | `-86.5 bps` | `+0.141 / +0.134` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,094.73 | ⚪ **CASH** | **-4.6 bps** (±3.2) | `-8.9 bps` | `-0.017 / -0.063` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.75 | ⚪ **CASH** | **+6.8 bps** (±6.1) | `+8.2 bps` | `+0.060 / -0.116` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 13:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,343.35 | ⚪ **CASH** | **-32.1 bps** (±8.0) | `-86.5 bps` | `+0.141 / +0.134` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,098.30 | ⚪ **CASH** | **-4.6 bps** (±3.2) | `-8.9 bps` | `-0.017 / -0.063` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.95 | ⚪ **CASH** | **+6.8 bps** (±6.1) | `+8.2 bps` | `+0.060 / -0.116` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 12:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,251.20 | ⚪ **CASH** | **-34.0 bps** (±9.4) | `-89.1 bps` | `+0.153 / +0.100` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,090.32 | ⚪ **CASH** | **-21.2 bps** (±5.3) | `-40.1 bps` | `-0.010 / -0.060` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.83 | ⚪ **CASH** | **+3.8 bps** (±6.2) | `+1.3 bps` | `+0.065 / -0.109` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 12:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,219.78 | ⚪ **CASH** | **-34.0 bps** (±9.4) | `-89.1 bps` | `+0.153 / +0.100` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,089.54 | ⚪ **CASH** | **-21.2 bps** (±5.3) | `-40.1 bps` | `-0.010 / -0.060` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.67 | ⚪ **CASH** | **+3.8 bps** (±6.2) | `+1.3 bps` | `+0.065 / -0.109` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 12:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,387.30 | ⚪ **CASH** | **-34.0 bps** (±9.4) | `-89.1 bps` | `+0.153 / +0.100` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,093.89 | ⚪ **CASH** | **-21.2 bps** (±5.3) | `-40.1 bps` | `-0.010 / -0.060` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.84 | ⚪ **CASH** | **+3.8 bps** (±6.2) | `+1.3 bps` | `+0.065 / -0.109` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 12:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,414.78 | ⚪ **CASH** | **-34.0 bps** (±9.4) | `-89.1 bps` | `+0.153 / +0.100` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,094.06 | ⚪ **CASH** | **-21.2 bps** (±5.3) | `-40.1 bps` | `-0.010 / -0.060` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.68 | ⚪ **CASH** | **+3.8 bps** (±6.2) | `+1.3 bps` | `+0.065 / -0.109` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 11:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,391.77 | ⚪ **CASH** | **-39.7 bps** (±9.2) | `-96.0 bps` | `+0.151 / +0.049` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,093.72 | ⚪ **CASH** | **-23.0 bps** (±8.8) | `-42.2 bps` | `-0.009 / -0.071` | `0.62%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.68 | ⚪ **CASH** | **+6.9 bps** (±5.9) | `+7.5 bps` | `+0.069 / -0.124` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 11:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,238.58 | ⚪ **CASH** | **-39.7 bps** (±9.2) | `-96.0 bps` | `+0.151 / +0.049` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,093.86 | ⚪ **CASH** | **-23.0 bps** (±8.8) | `-42.2 bps` | `-0.009 / -0.071` | `0.62%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.47 | ⚪ **CASH** | **+6.9 bps** (±5.9) | `+7.5 bps` | `+0.069 / -0.124` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 11:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,397.66 | ⚪ **CASH** | **-39.7 bps** (±9.2) | `-96.0 bps` | `+0.151 / +0.049` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,100.28 | ⚪ **CASH** | **-23.0 bps** (±8.8) | `-42.2 bps` | `-0.009 / -0.071` | `0.62%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.87 | ⚪ **CASH** | **+6.9 bps** (±5.9) | `+7.5 bps` | `+0.069 / -0.124` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 11:00:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,203.25 | ⚪ **CASH** | **-39.7 bps** (±9.2) | `-96.0 bps` | `+0.151 / +0.049` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,089.45 | ⚪ **CASH** | **-23.0 bps** (±8.8) | `-42.2 bps` | `-0.009 / -0.071` | `0.62%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.42 | ⚪ **CASH** | **+6.9 bps** (±5.9) | `+7.5 bps` | `+0.069 / -0.124` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 10:45:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,158.89 | ⚪ **CASH** | **-38.2 bps** (±4.9) | `-97.7 bps` | `+0.160 / +0.084` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,087.09 | ⚪ **CASH** | **-7.6 bps** (±5.1) | `-14.4 bps` | `-0.011 / -0.081` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.44 | ⚪ **CASH** | **+2.5 bps** (±7.6) | `-4.2 bps` | `+0.087 / -0.095` | `0.60%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 10:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,322.94 | ⚪ **CASH** | **-38.2 bps** (±4.9) | `-97.7 bps` | `+0.160 / +0.084` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,093.37 | ⚪ **CASH** | **-7.6 bps** (±5.1) | `-14.4 bps` | `-0.011 / -0.081` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.27 | ⚪ **CASH** | **+2.5 bps** (±7.6) | `-4.2 bps` | `+0.087 / -0.095` | `0.60%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 10:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,347.01 | ⚪ **CASH** | **-38.2 bps** (±4.9) | `-97.7 bps` | `+0.160 / +0.084` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,096.75 | ⚪ **CASH** | **-7.6 bps** (±5.1) | `-14.4 bps` | `-0.011 / -0.081` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.26 | ⚪ **CASH** | **+2.5 bps** (±7.6) | `-4.2 bps` | `+0.087 / -0.095` | `0.60%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 10:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,548.18 | ⚪ **CASH** | **-38.2 bps** (±4.9) | `-97.7 bps` | `+0.160 / +0.084` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,105.34 | ⚪ **CASH** | **-7.6 bps** (±5.1) | `-14.4 bps` | `-0.011 / -0.081` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.64 | ⚪ **CASH** | **+2.5 bps** (±7.6) | `-4.2 bps` | `+0.087 / -0.095` | `0.60%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 09:45:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,478.01 | ⚪ **CASH** | **-42.6 bps** (±9.1) | `-103.3 bps` | `+0.153 / +0.076` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,104.41 | ⚪ **CASH** | **-1.0 bps** (±3.3) | `-1.8 bps` | `-0.013 / -0.086` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.59 | ⚪ **CASH** | **+13.1 bps** (±5.6) | `+1.3 bps` | `+0.112 / +0.077` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 09:30:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,417.31 | ⚪ **CASH** | **-42.6 bps** (±9.1) | `-103.3 bps` | `+0.153 / +0.076` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,104.00 | ⚪ **CASH** | **-1.0 bps** (±3.3) | `-1.8 bps` | `-0.013 / -0.086` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.41 | ⚪ **CASH** | **+13.1 bps** (±5.6) | `+1.3 bps` | `+0.112 / +0.077` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 09:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,337.97 | ⚪ **CASH** | **-42.6 bps** (±9.1) | `-103.3 bps` | `+0.153 / +0.076` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,101.30 | ⚪ **CASH** | **-1.0 bps** (±3.3) | `-1.8 bps` | `-0.013 / -0.086` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.31 | ⚪ **CASH** | **+13.1 bps** (±5.6) | `+1.3 bps` | `+0.112 / +0.077` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 09:00:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,474.01 | ⚪ **CASH** | **-42.6 bps** (±9.1) | `-103.3 bps` | `+0.153 / +0.076` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,109.73 | ⚪ **CASH** | **-1.0 bps** (±3.3) | `-1.8 bps` | `-0.013 / -0.086` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.60 | ⚪ **CASH** | **+13.1 bps** (±5.6) | `+1.3 bps` | `+0.112 / +0.077` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 08:45:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,564.55 | ⚪ **CASH** | **-40.8 bps** (±7.7) | `-101.0 bps` | `+0.167 / +0.054` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,113.41 | ⚪ **CASH** | **-5.1 bps** (±5.1) | `-8.7 bps` | `-0.025 / -0.083` | `0.63%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.70 | ⚪ **CASH** | **+11.4 bps** (±5.2) | `-4.9 bps` | `+0.127 / +0.090` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 08:30:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,642.86 | ⚪ **CASH** | **-40.8 bps** (±7.7) | `-101.0 bps` | `+0.167 / +0.054` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,112.29 | ⚪ **CASH** | **-5.1 bps** (±5.1) | `-8.7 bps` | `-0.025 / -0.083` | `0.63%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.72 | ⚪ **CASH** | **+11.4 bps** (±5.2) | `-4.9 bps` | `+0.127 / +0.090` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 08:15:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,786.01 | ⚪ **CASH** | **-40.8 bps** (±7.7) | `-101.0 bps` | `+0.167 / +0.054` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,115.42 | ⚪ **CASH** | **-5.1 bps** (±5.1) | `-8.7 bps` | `-0.025 / -0.083` | `0.63%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.97 | ⚪ **CASH** | **+11.4 bps** (±5.2) | `-4.9 bps` | `+0.127 / +0.090` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 08:00:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,803.11 | ⚪ **CASH** | **-40.8 bps** (±7.7) | `-101.0 bps` | `+0.167 / +0.054` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,113.98 | ⚪ **CASH** | **-5.1 bps** (±5.1) | `-8.7 bps` | `-0.025 / -0.083` | `0.63%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.05 | ⚪ **CASH** | **+11.4 bps** (±5.2) | `-4.9 bps` | `+0.127 / +0.090` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 07:45:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,938.41 | ⚪ **CASH** | **-40.6 bps** (±6.6) | `-92.5 bps` | `+0.143 / -0.019` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,123.87 | ⚪ **CASH** | **-13.2 bps** (±6.9) | `-17.5 bps` | `-0.066 / -0.089` | `0.64%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.29 | ⚪ **CASH** | **+12.1 bps** (±6.9) | `+1.3 bps` | `+0.116 / +0.053` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 07:30:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,839.88 | ⚪ **CASH** | **-40.6 bps** (±6.6) | `-92.5 bps` | `+0.143 / -0.019` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,123.23 | ⚪ **CASH** | **-13.2 bps** (±6.9) | `-17.5 bps` | `-0.066 / -0.089` | `0.64%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.40 | ⚪ **CASH** | **+12.1 bps** (±6.9) | `+1.3 bps` | `+0.116 / +0.053` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 07:15:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,697.04 | ⚪ **CASH** | **-40.6 bps** (±6.6) | `-92.5 bps` | `+0.143 / -0.019` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,116.72 | ⚪ **CASH** | **-13.2 bps** (±6.9) | `-17.5 bps` | `-0.066 / -0.089` | `0.64%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.12 | ⚪ **CASH** | **+12.1 bps** (±6.9) | `+1.3 bps` | `+0.116 / +0.053` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 07:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,692.01 | ⚪ **CASH** | **-40.6 bps** (±6.6) | `-92.5 bps` | `+0.143 / -0.019` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,118.55 | ⚪ **CASH** | **-13.2 bps** (±6.9) | `-17.5 bps` | `-0.066 / -0.089` | `0.64%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.17 | ⚪ **CASH** | **+12.1 bps** (±6.9) | `+1.3 bps` | `+0.116 / +0.053` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 06:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,703.41 | ⚪ **CASH** | **-41.5 bps** (±6.7) | `-96.2 bps` | `+0.123 / +0.059` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,118.13 | ⚪ **CASH** | **-18.8 bps** (±9.1) | `-24.7 bps` | `-0.088 / -0.079` | `0.65%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.06 | ⚪ **CASH** | **+8.8 bps** (±6.8) | `-1.0 bps` | `+0.096 / +0.044` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 06:30:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,672.72 | ⚪ **CASH** | **-41.5 bps** (±6.7) | `-96.2 bps` | `+0.123 / +0.059` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,118.29 | ⚪ **CASH** | **-18.8 bps** (±9.1) | `-24.7 bps` | `-0.088 / -0.079` | `0.65%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.01 | ⚪ **CASH** | **+8.8 bps** (±6.8) | `-1.0 bps` | `+0.096 / +0.044` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 06:15:34 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,584.00 | ⚪ **CASH** | **-41.5 bps** (±6.7) | `-96.2 bps` | `+0.123 / +0.059` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,115.83 | ⚪ **CASH** | **-18.8 bps** (±9.1) | `-24.7 bps` | `-0.088 / -0.079` | `0.65%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.86 | ⚪ **CASH** | **+8.8 bps** (±6.8) | `-1.0 bps` | `+0.096 / +0.044` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 06:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,788.00 | ⚪ **CASH** | **-41.5 bps** (±6.7) | `-96.2 bps` | `+0.123 / +0.059` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,124.23 | ⚪ **CASH** | **-18.8 bps** (±9.1) | `-24.7 bps` | `-0.088 / -0.079` | `0.65%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.22 | ⚪ **CASH** | **+8.8 bps** (±6.8) | `-1.0 bps` | `+0.096 / +0.044` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 05:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,892.01 | ⚪ **CASH** | **-38.7 bps** (±6.8) | `-94.0 bps` | `+0.120 / +0.108` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,127.08 | ⚪ **CASH** | **-18.6 bps** (±7.7) | `-20.2 bps` | `-0.112 / -0.110` | `0.65%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.30 | ⚪ **CASH** | **+2.4 bps** (±8.7) | `-9.9 bps` | `+0.081 / +0.031` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 05:30:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,804.01 | ⚪ **CASH** | **-38.7 bps** (±6.8) | `-94.0 bps` | `+0.120 / +0.108` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,123.65 | ⚪ **CASH** | **-18.6 bps** (±7.7) | `-20.2 bps` | `-0.112 / -0.110` | `0.65%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.15 | ⚪ **CASH** | **+2.4 bps** (±8.7) | `-9.9 bps` | `+0.081 / +0.031` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
