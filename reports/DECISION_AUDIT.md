# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-03 18:16:32 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-11-03 01:48:05 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,206.00 | ⚪ **CASH** | **+25.1 bps** (±7.7) | `+16.2 bps` | `+0.121 / +0.199` | `0.22%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,259.88 | ⚪ **CASH** | **+49.2 bps** (±7.4) | `+89.6 bps` | `-0.083 / +0.053` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $92.44 | ⚪ **CASH** | **+19.1 bps** (±10.0) | `+20.7 bps` | `+0.088 / +0.019` | `0.43%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-03 01:32:34 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,226.01 | ⚪ **CASH** | **+25.1 bps** (±7.7) | `+16.2 bps` | `+0.121 / +0.199` | `0.22%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,261.04 | ⚪ **CASH** | **+49.2 bps** (±7.4) | `+89.6 bps` | `-0.083 / +0.053` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $92.39 | ⚪ **CASH** | **+19.1 bps** (±10.0) | `+20.7 bps` | `+0.088 / +0.019` | `0.43%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-03 01:17:21 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,225.98 | ⚪ **CASH** | **+25.1 bps** (±7.7) | `+16.2 bps` | `+0.121 / +0.199` | `0.22%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,260.97 | ⚪ **CASH** | **+49.2 bps** (±7.4) | `+89.6 bps` | `-0.083 / +0.053` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $92.58 | ⚪ **CASH** | **+19.1 bps** (±10.0) | `+20.7 bps` | `+0.088 / +0.019` | `0.43%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-03 01:02:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,169.45 | ⚪ **CASH** | **+25.1 bps** (±7.7) | `+16.2 bps` | `+0.121 / +0.199` | `0.22%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,259.70 | ⚪ **CASH** | **+49.2 bps** (±7.4) | `+89.6 bps` | `-0.083 / +0.053` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $92.54 | ⚪ **CASH** | **+19.1 bps** (±10.0) | `+20.7 bps` | `+0.088 / +0.019` | `0.43%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-03 00:32:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,110.19 | ⚪ **CASH** | **+23.9 bps** (±5.8) | `+10.7 bps` | `+0.120 / +0.245` | `0.21%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,258.86 | ⚪ **CASH** | **+49.8 bps** (±12.2) | `+92.6 bps` | `-0.066 / +0.013` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $92.52 | ⚪ **CASH** | **+19.6 bps** (±10.3) | `+20.8 bps` | `+0.083 / +0.041` | `0.43%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-03 00:17:31 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,922.01 | ⚪ **CASH** | **+23.9 bps** (±5.8) | `+10.7 bps` | `+0.120 / +0.245` | `0.21%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,257.15 | ⚪ **CASH** | **+49.8 bps** (±12.2) | `+92.6 bps` | `-0.066 / +0.013` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $92.32 | ⚪ **CASH** | **+19.6 bps** (±10.3) | `+20.8 bps` | `+0.083 / +0.041` | `0.43%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-03 00:02:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,802.33 | ⚪ **CASH** | **+23.9 bps** (±5.8) | `+10.7 bps` | `+0.120 / +0.245` | `0.21%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,252.03 | ⚪ **CASH** | **+49.8 bps** (±12.2) | `+92.6 bps` | `-0.066 / +0.013` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $92.00 | ⚪ **CASH** | **+19.6 bps** (±10.3) | `+20.8 bps` | `+0.083 / +0.041` | `0.43%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 23:47:27 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,822.83 | ⚪ **CASH** | **+35.8 bps** (±6.7) | `+38.9 bps` | `+0.120 / +0.148` | `0.22%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,252.68 | ⚪ **CASH** | **+50.5 bps** (±8.5) | `+94.0 bps` | `-0.060 / -0.010` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $91.95 | ⚪ **CASH** | **+7.2 bps** (±19.2) | `-0.3 bps` | `+0.087 / +0.037` | `0.44%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 23:32:30 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,758.89 | ⚪ **CASH** | **+35.8 bps** (±6.7) | `+38.9 bps` | `+0.120 / +0.148` | `0.22%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,249.88 | ⚪ **CASH** | **+50.5 bps** (±8.5) | `+94.0 bps` | `-0.060 / -0.010` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $91.75 | ⚪ **CASH** | **+7.2 bps** (±19.2) | `-0.3 bps` | `+0.087 / +0.037` | `0.44%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 23:17:28 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,846.00 | ⚪ **CASH** | **+35.8 bps** (±6.7) | `+38.9 bps` | `+0.120 / +0.148` | `0.22%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,253.97 | ⚪ **CASH** | **+50.5 bps** (±8.5) | `+94.0 bps` | `-0.060 / -0.010` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $91.88 | ⚪ **CASH** | **+7.2 bps** (±19.2) | `-0.3 bps` | `+0.087 / +0.037` | `0.44%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 23:02:32 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,735.01 | ⚪ **CASH** | **+35.8 bps** (±6.7) | `+38.9 bps` | `+0.120 / +0.148` | `0.22%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,249.80 | ⚪ **CASH** | **+50.5 bps** (±8.5) | `+94.0 bps` | `-0.060 / -0.010` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $91.71 | ⚪ **CASH** | **+7.2 bps** (±19.2) | `-0.3 bps` | `+0.087 / +0.037` | `0.44%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 22:47:29 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,908.48 | ⚪ **CASH** | **+32.9 bps** (±6.8) | `+37.0 bps` | `+0.107 / +0.127` | `0.22%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,254.61 | ⚪ **CASH** | **+48.9 bps** (±8.1) | `+93.4 bps` | `-0.062 / -0.033` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $92.14 | ⚪ **CASH** | **+5.7 bps** (±20.0) | `-4.3 bps` | `+0.089 / +0.065` | `0.44%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 22:32:34 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,848.01 | ⚪ **CASH** | **+32.9 bps** (±6.8) | `+37.0 bps` | `+0.107 / +0.127` | `0.22%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,251.54 | ⚪ **CASH** | **+48.9 bps** (±8.1) | `+93.4 bps` | `-0.062 / -0.033` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $91.74 | ⚪ **CASH** | **+5.7 bps** (±20.0) | `-4.3 bps` | `+0.089 / +0.065` | `0.44%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 22:19:34 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,011.00 | ⚪ **CASH** | **+32.9 bps** (±6.8) | `+37.0 bps` | `+0.107 / +0.127` | `0.22%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,260.13 | ⚪ **CASH** | **+48.9 bps** (±8.1) | `+93.4 bps` | `-0.062 / -0.033` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $92.25 | ⚪ **CASH** | **+5.7 bps** (±20.0) | `-4.3 bps` | `+0.089 / +0.065` | `0.44%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 22:03:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,870.12 | ⚪ **CASH** | **+32.9 bps** (±6.8) | `+37.0 bps` | `+0.107 / +0.127` | `0.22%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,258.38 | ⚪ **CASH** | **+48.9 bps** (±8.1) | `+93.4 bps` | `-0.062 / -0.033` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $92.22 | ⚪ **CASH** | **+5.7 bps** (±20.0) | `-4.3 bps` | `+0.089 / +0.065` | `0.44%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 21:47:27 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,930.00 | ⚪ **CASH** | **+33.0 bps** (±7.2) | `+42.7 bps` | `+0.098 / +0.064` | `0.22%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,258.12 | ⚪ **CASH** | **+51.0 bps** (±8.4) | `+103.2 bps` | `-0.065 / -0.112` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $92.14 | ⚪ **CASH** | **+0.1 bps** (±15.5) | `-12.8 bps` | `+0.089 / +0.036` | `0.42%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 21:32:24 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,824.34 | ⚪ **CASH** | **+33.0 bps** (±7.2) | `+42.7 bps` | `+0.098 / +0.064` | `0.22%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,253.39 | ⚪ **CASH** | **+51.0 bps** (±8.4) | `+103.2 bps` | `-0.065 / -0.112` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $91.72 | ⚪ **CASH** | **+0.1 bps** (±15.5) | `-12.8 bps` | `+0.089 / +0.036` | `0.42%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 21:17:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,869.31 | ⚪ **CASH** | **+33.0 bps** (±7.2) | `+42.7 bps` | `+0.098 / +0.064` | `0.22%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,253.47 | ⚪ **CASH** | **+51.0 bps** (±8.4) | `+103.2 bps` | `-0.065 / -0.112` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $91.81 | ⚪ **CASH** | **+0.1 bps** (±15.5) | `-12.8 bps` | `+0.089 / +0.036` | `0.42%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 21:02:34 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,856.01 | ⚪ **CASH** | **+33.0 bps** (±7.2) | `+42.7 bps` | `+0.098 / +0.064` | `0.22%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,252.13 | ⚪ **CASH** | **+51.0 bps** (±8.4) | `+103.2 bps` | `-0.065 / -0.112` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $91.69 | ⚪ **CASH** | **+0.1 bps** (±15.5) | `-12.8 bps` | `+0.089 / +0.036` | `0.42%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 20:47:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,984.01 | ⚪ **CASH** | **+40.5 bps** (±6.1) | `+52.7 bps` | `+0.097 / +0.118` | `0.21%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,251.83 | ⚪ **CASH** | **+45.0 bps** (±11.1) | `+92.1 bps` | `-0.068 / -0.098` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $91.66 | ⚪ **CASH** | **+7.0 bps** (±19.3) | `-2.4 bps` | `+0.099 / +0.063` | `0.42%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 20:32:18 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,893.70 | ⚪ **CASH** | **+40.5 bps** (±6.1) | `+52.7 bps` | `+0.097 / +0.118` | `0.21%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,247.37 | ⚪ **CASH** | **+45.0 bps** (±11.1) | `+92.1 bps` | `-0.068 / -0.098` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $91.51 | ⚪ **CASH** | **+7.0 bps** (±19.3) | `-2.4 bps` | `+0.099 / +0.063` | `0.42%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 20:17:35 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,025.50 | ⚪ **CASH** | **+40.5 bps** (±6.1) | `+52.7 bps` | `+0.097 / +0.118` | `0.21%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,253.98 | ⚪ **CASH** | **+45.0 bps** (±11.1) | `+92.1 bps` | `-0.068 / -0.098` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $91.67 | ⚪ **CASH** | **+7.0 bps** (±19.3) | `-2.4 bps` | `+0.099 / +0.063` | `0.42%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 20:02:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,969.70 | ⚪ **CASH** | **+40.5 bps** (±6.1) | `+52.7 bps` | `+0.097 / +0.118` | `0.21%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,251.69 | ⚪ **CASH** | **+45.0 bps** (±11.1) | `+92.1 bps` | `-0.068 / -0.098` | `0.31%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $91.68 | ⚪ **CASH** | **+7.0 bps** (±19.3) | `-2.4 bps` | `+0.099 / +0.063` | `0.42%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
