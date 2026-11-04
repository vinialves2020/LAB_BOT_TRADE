# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-04 00:01:17 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-04 00:01:17 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,456.01 | ⚪ **CASH** | **+13.9 bps** (±6.2) | `+30.0 bps` | `-0.018 / -0.016` | `0.26%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,275.01 | ⚪ **CASH** | **+28.2 bps** (±18.7) | `+37.5 bps` | `+0.145 / +0.059` | `0.33%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.89 | ⚪ **CASH** | **+37.4 bps** (±9.4) | `+77.2 bps` | `-0.020 / -0.071` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-03 23:46:11 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,748.92 | ⚪ **CASH** | **+18.6 bps** (±9.5) | `+34.0 bps` | `-0.007 / +0.039` | `0.24%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,284.29 | ⚪ **CASH** | **+23.1 bps** (±7.3) | `+21.4 bps` | `+0.156 / +0.107` | `0.30%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.25 | ⚪ **CASH** | **+29.7 bps** (±21.3) | `+64.7 bps` | `-0.015 / -0.075` | `0.39%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 23:31:20 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,914.21 | ⚪ **CASH** | **+18.6 bps** (±9.5) | `+34.0 bps` | `-0.007 / +0.039` | `0.24%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,289.68 | ⚪ **CASH** | **+23.1 bps** (±7.3) | `+21.4 bps` | `+0.156 / +0.107` | `0.30%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.51 | ⚪ **CASH** | **+29.7 bps** (±21.3) | `+64.7 bps` | `-0.015 / -0.075` | `0.39%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 23:16:20 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,878.00 | ⚪ **CASH** | **+18.6 bps** (±9.5) | `+34.0 bps` | `-0.007 / +0.039` | `0.24%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,292.75 | ⚪ **CASH** | **+23.1 bps** (±7.3) | `+21.4 bps` | `+0.156 / +0.107` | `0.30%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.49 | ⚪ **CASH** | **+29.7 bps** (±21.3) | `+64.7 bps` | `-0.015 / -0.075` | `0.39%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 23:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,902.52 | ⚪ **CASH** | **+18.6 bps** (±9.5) | `+34.0 bps` | `-0.007 / +0.039` | `0.24%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,294.00 | ⚪ **CASH** | **+23.1 bps** (±7.3) | `+21.4 bps` | `+0.156 / +0.107` | `0.30%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.52 | ⚪ **CASH** | **+29.7 bps** (±21.3) | `+64.7 bps` | `-0.015 / -0.075` | `0.39%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 22:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,802.01 | ⚪ **CASH** | **+24.3 bps** (±6.2) | `+40.2 bps` | `+0.007 / +0.060` | `0.24%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,292.18 | ⚪ **CASH** | **+24.2 bps** (±4.4) | `+23.0 bps` | `+0.155 / +0.097` | `0.31%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.44 | ⚪ **CASH** | **+30.9 bps** (±18.9) | `+62.4 bps` | `-0.010 / -0.035` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 22:31:17 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,787.06 | ⚪ **CASH** | **+24.3 bps** (±6.2) | `+40.2 bps` | `+0.007 / +0.060` | `0.24%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,288.39 | ⚪ **CASH** | **+24.2 bps** (±4.4) | `+23.0 bps` | `+0.155 / +0.097` | `0.31%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.38 | ⚪ **CASH** | **+30.9 bps** (±18.9) | `+62.4 bps` | `-0.010 / -0.035` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 22:16:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,823.13 | ⚪ **CASH** | **+24.3 bps** (±6.2) | `+40.2 bps` | `+0.007 / +0.060` | `0.24%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,293.81 | ⚪ **CASH** | **+24.2 bps** (±4.4) | `+23.0 bps` | `+0.155 / +0.097` | `0.31%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.60 | ⚪ **CASH** | **+30.9 bps** (±18.9) | `+62.4 bps` | `-0.010 / -0.035` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 22:02:00 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,893.14 | ⚪ **CASH** | **+24.3 bps** (±6.2) | `+40.2 bps` | `+0.007 / +0.060` | `0.24%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,295.03 | ⚪ **CASH** | **+24.2 bps** (±4.4) | `+23.0 bps` | `+0.155 / +0.097` | `0.31%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.69 | ⚪ **CASH** | **+30.9 bps** (±18.9) | `+62.4 bps` | `-0.010 / -0.035` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 21:46:24 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,022.60 | ⚪ **CASH** | **+26.2 bps** (±8.6) | `+42.2 bps` | `+0.015 / +0.071` | `0.25%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,298.45 | ⚪ **CASH** | **+26.2 bps** (±4.6) | `+26.4 bps` | `+0.156 / +0.093` | `0.31%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.85 | ⚪ **CASH** | **+37.3 bps** (±12.7) | `+68.8 bps` | `+0.001 / +0.008` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-03 21:31:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,924.25 | ⚪ **CASH** | **+26.2 bps** (±8.6) | `+42.2 bps` | `+0.015 / +0.071` | `0.25%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,296.36 | ⚪ **CASH** | **+26.2 bps** (±4.6) | `+26.4 bps` | `+0.156 / +0.093` | `0.31%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.79 | ⚪ **CASH** | **+37.3 bps** (±12.7) | `+68.8 bps` | `+0.001 / +0.008` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-03 21:17:07 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,914.02 | ⚪ **CASH** | **+26.2 bps** (±8.6) | `+42.2 bps` | `+0.015 / +0.071` | `0.25%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,296.98 | ⚪ **CASH** | **+26.2 bps** (±4.6) | `+26.4 bps` | `+0.156 / +0.093` | `0.31%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.81 | ⚪ **CASH** | **+37.3 bps** (±12.7) | `+68.8 bps` | `+0.001 / +0.008` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-03 21:02:06 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,843.22 | ⚪ **CASH** | **+26.2 bps** (±8.6) | `+42.2 bps` | `+0.015 / +0.071` | `0.25%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,290.60 | ⚪ **CASH** | **+26.2 bps** (±4.6) | `+26.4 bps` | `+0.156 / +0.093` | `0.31%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.53 | ⚪ **CASH** | **+37.3 bps** (±12.7) | `+68.8 bps` | `+0.001 / +0.008` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-03 20:46:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,842.88 | ⚪ **CASH** | **+24.6 bps** (±10.0) | `+40.6 bps` | `+0.017 / +0.051` | `0.24%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,290.42 | ⚪ **CASH** | **+17.6 bps** (±6.3) | `+14.6 bps` | `+0.144 / +0.055` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.53 | ⚪ **CASH** | **+33.9 bps** (±11.1) | `+64.0 bps` | `-0.004 / -0.011` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 20:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,770.00 | ⚪ **CASH** | **+24.6 bps** (±10.0) | `+40.6 bps` | `+0.017 / +0.051` | `0.24%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,285.80 | ⚪ **CASH** | **+17.6 bps** (±6.3) | `+14.6 bps` | `+0.144 / +0.055` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.44 | ⚪ **CASH** | **+33.9 bps** (±11.1) | `+64.0 bps` | `-0.004 / -0.011` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 20:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,640.01 | ⚪ **CASH** | **+24.6 bps** (±10.0) | `+40.6 bps` | `+0.017 / +0.051` | `0.24%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,281.16 | ⚪ **CASH** | **+17.6 bps** (±6.3) | `+14.6 bps` | `+0.144 / +0.055` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.15 | ⚪ **CASH** | **+33.9 bps** (±11.1) | `+64.0 bps` | `-0.004 / -0.011` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 20:01:30 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,627.46 | ⚪ **CASH** | **+24.6 bps** (±10.0) | `+40.6 bps` | `+0.017 / +0.051` | `0.24%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,287.17 | ⚪ **CASH** | **+17.6 bps** (±6.3) | `+14.6 bps` | `+0.144 / +0.055` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.25 | ⚪ **CASH** | **+33.9 bps** (±11.1) | `+64.0 bps` | `-0.004 / -0.011` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 19:45:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,611.91 | ⚪ **CASH** | **+27.8 bps** (±9.4) | `+40.1 bps` | `+0.021 / +0.138` | `0.25%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,289.49 | ⚪ **CASH** | **+18.9 bps** (±10.4) | `+13.6 bps` | `+0.137 / +0.125` | `0.31%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.24 | ⚪ **CASH** | **+34.5 bps** (±12.6) | `+64.1 bps` | `-0.002 / +0.002` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 19:31:30 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,581.52 | ⚪ **CASH** | **+27.8 bps** (±9.4) | `+40.1 bps` | `+0.021 / +0.138` | `0.25%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,289.51 | ⚪ **CASH** | **+18.9 bps** (±10.4) | `+13.6 bps` | `+0.137 / +0.125` | `0.31%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.25 | ⚪ **CASH** | **+34.5 bps** (±12.6) | `+64.1 bps` | `-0.002 / +0.002` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 19:16:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,541.98 | ⚪ **CASH** | **+27.8 bps** (±9.4) | `+40.1 bps` | `+0.021 / +0.138` | `0.25%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,289.24 | ⚪ **CASH** | **+18.9 bps** (±10.4) | `+13.6 bps` | `+0.137 / +0.125` | `0.31%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.27 | ⚪ **CASH** | **+34.5 bps** (±12.6) | `+64.1 bps` | `-0.002 / +0.002` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 19:01:29 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,557.86 | ⚪ **CASH** | **+27.8 bps** (±9.4) | `+40.1 bps` | `+0.021 / +0.138` | `0.25%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,290.58 | ⚪ **CASH** | **+18.9 bps** (±10.4) | `+13.6 bps` | `+0.137 / +0.125` | `0.31%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.42 | ⚪ **CASH** | **+34.5 bps** (±12.6) | `+64.1 bps` | `-0.002 / +0.002` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 18:46:33 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,738.00 | ⚪ **CASH** | **+32.6 bps** (±9.6) | `+44.9 bps` | `+0.034 / +0.169` | `0.25%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,297.98 | ⚪ **CASH** | **+20.3 bps** (±8.7) | `+15.5 bps` | `+0.131 / +0.129` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.64 | ⚪ **CASH** | **+35.2 bps** (±10.3) | `+62.7 bps` | `+0.008 / +0.010` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 18:31:32 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,720.41 | ⚪ **CASH** | **+32.6 bps** (±9.6) | `+44.9 bps` | `+0.034 / +0.169` | `0.25%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,297.51 | ⚪ **CASH** | **+20.3 bps** (±8.7) | `+15.5 bps` | `+0.131 / +0.129` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.55 | ⚪ **CASH** | **+35.2 bps** (±10.3) | `+62.7 bps` | `+0.008 / +0.010` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 18:16:32 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,679.58 | ⚪ **CASH** | **+32.6 bps** (±9.6) | `+44.9 bps` | `+0.034 / +0.169` | `0.25%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,297.60 | ⚪ **CASH** | **+20.3 bps** (±8.7) | `+15.5 bps` | `+0.131 / +0.129` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.61 | ⚪ **CASH** | **+35.2 bps** (±10.3) | `+62.7 bps` | `+0.008 / +0.010` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 18:01:32 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,642.48 | ⚪ **CASH** | **+32.6 bps** (±9.6) | `+44.9 bps` | `+0.034 / +0.169` | `0.25%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,296.54 | ⚪ **CASH** | **+20.3 bps** (±8.7) | `+15.5 bps` | `+0.131 / +0.129` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.37 | ⚪ **CASH** | **+35.2 bps** (±10.3) | `+62.7 bps` | `+0.008 / +0.010` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 17:45:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,673.17 | ⚪ **CASH** | **+36.2 bps** (±10.5) | `+52.2 bps` | `+0.022 / +0.187` | `0.25%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,295.38 | ⚪ **CASH** | **+16.8 bps** (±9.6) | `+11.5 bps` | `+0.121 / +0.119` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.29 | ⚪ **CASH** | **+31.8 bps** (±10.5) | `+57.0 bps` | `+0.013 / +0.007` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 17:31:24 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,672.16 | ⚪ **CASH** | **+36.2 bps** (±10.5) | `+52.2 bps` | `+0.022 / +0.187` | `0.25%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,297.01 | ⚪ **CASH** | **+16.8 bps** (±9.6) | `+11.5 bps` | `+0.121 / +0.119` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.38 | ⚪ **CASH** | **+31.8 bps** (±10.5) | `+57.0 bps` | `+0.013 / +0.007` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 17:16:21 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,691.05 | ⚪ **CASH** | **+36.2 bps** (±10.5) | `+52.2 bps` | `+0.022 / +0.187` | `0.25%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,298.01 | ⚪ **CASH** | **+16.8 bps** (±9.6) | `+11.5 bps` | `+0.121 / +0.119` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.45 | ⚪ **CASH** | **+31.8 bps** (±10.5) | `+57.0 bps` | `+0.013 / +0.007` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 17:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,738.56 | ⚪ **CASH** | **+36.2 bps** (±10.5) | `+52.2 bps` | `+0.022 / +0.187` | `0.25%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,297.82 | ⚪ **CASH** | **+16.8 bps** (±9.6) | `+11.5 bps` | `+0.121 / +0.119` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.56 | ⚪ **CASH** | **+31.8 bps** (±10.5) | `+57.0 bps` | `+0.013 / +0.007` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 16:46:11 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,465.23 | ⚪ **CASH** | **+38.6 bps** (±6.3) | `+54.2 bps` | `+0.028 / +0.200` | `0.26%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,289.75 | ⚪ **CASH** | **+18.6 bps** (±8.9) | `+14.7 bps` | `+0.112 / +0.129` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.14 | ⚪ **CASH** | **+31.1 bps** (±7.9) | `+53.2 bps` | `+0.024 / +0.014` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 16:31:28 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,554.01 | ⚪ **CASH** | **+38.6 bps** (±6.3) | `+54.2 bps` | `+0.028 / +0.200` | `0.26%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,292.19 | ⚪ **CASH** | **+18.6 bps** (±8.9) | `+14.7 bps` | `+0.112 / +0.129` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.38 | ⚪ **CASH** | **+31.1 bps** (±7.9) | `+53.2 bps` | `+0.024 / +0.014` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 16:16:13 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,592.43 | ⚪ **CASH** | **+38.6 bps** (±6.3) | `+54.2 bps` | `+0.028 / +0.200` | `0.26%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,292.90 | ⚪ **CASH** | **+18.6 bps** (±8.9) | `+14.7 bps` | `+0.112 / +0.129` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.37 | ⚪ **CASH** | **+31.1 bps** (±7.9) | `+53.2 bps` | `+0.024 / +0.014` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 16:01:23 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,678.01 | ⚪ **CASH** | **+38.6 bps** (±6.3) | `+54.2 bps` | `+0.028 / +0.200` | `0.26%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,299.17 | ⚪ **CASH** | **+18.6 bps** (±8.9) | `+14.7 bps` | `+0.112 / +0.129` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.70 | ⚪ **CASH** | **+31.1 bps** (±7.9) | `+53.2 bps` | `+0.024 / +0.014` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 15:46:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,724.00 | ⚪ **CASH** | **+34.8 bps** (±10.2) | `+48.4 bps` | `+0.019 / +0.211` | `0.25%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,299.77 | ⚪ **CASH** | **+25.0 bps** (±9.7) | `+29.1 bps` | `+0.079 / +0.143` | `0.32%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.82 | ⚪ **CASH** | **+28.0 bps** (±13.0) | `+50.2 bps` | `+0.015 / +0.011` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 15:38:05 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,376.01 | ⚪ **CASH** | **+34.8 bps** (±10.2) | `+48.4 bps` | `+0.019 / +0.211` | `0.25%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,290.50 | ⚪ **CASH** | **+25.0 bps** (±9.7) | `+29.1 bps` | `+0.079 / +0.143` | `0.32%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.27 | ⚪ **CASH** | **+28.0 bps** (±13.0) | `+50.2 bps` | `+0.015 / +0.011` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-03 01:49:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,202.00 | ⚪ **CASH** | **+25.1 bps** (±7.7) | `+16.2 bps` | `+0.121 / +0.199` | `0.22%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,259.21 | ⚪ **CASH** | **+49.2 bps** (±7.4) | `+89.6 bps` | `-0.083 / +0.053` | `0.30%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $92.44 | ⚪ **CASH** | **+19.1 bps** (±10.0) | `+20.7 bps` | `+0.088 / +0.019` | `0.43%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
