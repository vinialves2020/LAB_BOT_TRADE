# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-04 04:16:09 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-04 04:16:09 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,822.62 | ⚪ **CASH** | **+6.4 bps** (±7.1) | `+6.4 bps` | `+0.051 / -0.013` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,264.87 | ⚪ **CASH** | **+21.4 bps** (±18.1) | `+41.1 bps` | `+0.097 / -0.169` | `0.36%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.90 | ⚪ **CASH** | **+1.8 bps** (±7.6) | `+4.9 bps` | `-0.013 / -0.021` | `0.45%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 04:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,456.07 | ⚪ **CASH** | **+6.4 bps** (±7.1) | `+6.4 bps` | `+0.051 / -0.013` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,248.18 | ⚪ **CASH** | **+21.4 bps** (±18.1) | `+41.1 bps` | `+0.097 / -0.169` | `0.36%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.00 | ⚪ **CASH** | **+1.8 bps** (±7.6) | `+4.9 bps` | `-0.013 / -0.021` | `0.45%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 03:46:10 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,314.35 | ⚪ **CASH** | **+2.0 bps** (±4.5) | `+1.7 bps` | `+0.022 / -0.006` | `0.32%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,244.58 | ⚪ **CASH** | **+14.3 bps** (±15.7) | `+23.2 bps` | `+0.115 / -0.101` | `0.36%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.78 | ⚪ **CASH** | **+10.1 bps** (±12.5) | `+24.2 bps` | `-0.019 / -0.041` | `0.46%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 03:31:12 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,251.47 | ⚪ **CASH** | **+2.0 bps** (±4.5) | `+1.7 bps` | `+0.022 / -0.006` | `0.32%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,245.76 | ⚪ **CASH** | **+14.3 bps** (±15.7) | `+23.2 bps` | `+0.115 / -0.101` | `0.36%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.04 | ⚪ **CASH** | **+10.1 bps** (±12.5) | `+24.2 bps` | `-0.019 / -0.041` | `0.46%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 03:16:17 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,000.00 | ⚪ **CASH** | **+2.0 bps** (±4.5) | `+1.7 bps` | `+0.022 / -0.006` | `0.32%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,237.45 | ⚪ **CASH** | **+14.3 bps** (±15.7) | `+23.2 bps` | `+0.115 / -0.101` | `0.36%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.66 | ⚪ **CASH** | **+10.1 bps** (±12.5) | `+24.2 bps` | `-0.019 / -0.041` | `0.46%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 03:01:21 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,073.64 | ⚪ **CASH** | **+2.0 bps** (±4.5) | `+1.7 bps` | `+0.022 / -0.006` | `0.32%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.07 | ⚪ **CASH** | **+14.3 bps** (±15.7) | `+23.2 bps` | `+0.115 / -0.101` | `0.36%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.53 | ⚪ **CASH** | **+10.1 bps** (±12.5) | `+24.2 bps` | `-0.019 / -0.041` | `0.46%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 02:46:09 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,623.00 | ⚪ **CASH** | **+20.6 bps** (±12.6) | `+38.1 bps` | `-0.007 / +0.041` | `0.26%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,255.16 | ⚪ **CASH** | **+25.7 bps** (±15.3) | `+34.9 bps` | `+0.128 / +0.036` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.41 | ⚪ **CASH** | **+29.2 bps** (±10.0) | `+60.1 bps` | `-0.024 / -0.038` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 02:30:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,777.62 | ⚪ **CASH** | **+20.6 bps** (±12.6) | `+38.1 bps` | `-0.007 / +0.041` | `0.26%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,258.30 | ⚪ **CASH** | **+25.7 bps** (±15.3) | `+34.9 bps` | `+0.128 / +0.036` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.58 | ⚪ **CASH** | **+29.2 bps** (±10.0) | `+60.1 bps` | `-0.024 / -0.038` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 02:16:12 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,881.84 | ⚪ **CASH** | **+20.6 bps** (±12.6) | `+38.1 bps` | `-0.007 / +0.041` | `0.26%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,260.15 | ⚪ **CASH** | **+25.7 bps** (±15.3) | `+34.9 bps` | `+0.128 / +0.036` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.76 | ⚪ **CASH** | **+29.2 bps** (±10.0) | `+60.1 bps` | `-0.024 / -0.038` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 02:01:20 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,084.02 | ⚪ **CASH** | **+20.6 bps** (±12.6) | `+38.1 bps` | `-0.007 / +0.041` | `0.26%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,265.99 | ⚪ **CASH** | **+25.7 bps** (±15.3) | `+34.9 bps` | `+0.128 / +0.036` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.09 | ⚪ **CASH** | **+29.2 bps** (±10.0) | `+60.1 bps` | `-0.024 / -0.038` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 01:46:08 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,870.12 | ⚪ **CASH** | **+18.7 bps** (±12.9) | `+35.7 bps` | `-0.012 / +0.036` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,260.78 | ⚪ **CASH** | **+25.9 bps** (±15.8) | `+36.7 bps` | `+0.129 / +0.020` | `0.33%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.72 | ⚪ **CASH** | **+29.6 bps** (±10.4) | `+63.4 bps` | `-0.025 / -0.070` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 01:31:22 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,965.63 | ⚪ **CASH** | **+18.7 bps** (±12.9) | `+35.7 bps` | `-0.012 / +0.036` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,263.03 | ⚪ **CASH** | **+25.9 bps** (±15.8) | `+36.7 bps` | `+0.129 / +0.020` | `0.33%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.88 | ⚪ **CASH** | **+29.6 bps** (±10.4) | `+63.4 bps` | `-0.025 / -0.070` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 01:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,926.50 | ⚪ **CASH** | **+18.7 bps** (±12.9) | `+35.7 bps` | `-0.012 / +0.036` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,264.89 | ⚪ **CASH** | **+25.9 bps** (±15.8) | `+36.7 bps` | `+0.129 / +0.020` | `0.33%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.89 | ⚪ **CASH** | **+29.6 bps** (±10.4) | `+63.4 bps` | `-0.025 / -0.070` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 01:01:27 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,214.74 | ⚪ **CASH** | **+18.7 bps** (±12.9) | `+35.7 bps` | `-0.012 / +0.036` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,273.30 | ⚪ **CASH** | **+25.9 bps** (±15.8) | `+36.7 bps` | `+0.129 / +0.020` | `0.33%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.45 | ⚪ **CASH** | **+29.6 bps** (±10.4) | `+63.4 bps` | `-0.025 / -0.070` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 00:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,003.98 | ⚪ **CASH** | **+13.9 bps** (±6.2) | `+30.0 bps` | `-0.018 / -0.016` | `0.26%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,267.04 | ⚪ **CASH** | **+28.2 bps** (±18.7) | `+37.5 bps` | `+0.145 / +0.059` | `0.33%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.12 | ⚪ **CASH** | **+37.4 bps** (±9.4) | `+77.2 bps` | `-0.020 / -0.071` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-04 00:31:11 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,263.70 | ⚪ **CASH** | **+13.9 bps** (±6.2) | `+30.0 bps` | `-0.018 / -0.016` | `0.26%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,271.08 | ⚪ **CASH** | **+28.2 bps** (±18.7) | `+37.5 bps` | `+0.145 / +0.059` | `0.33%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.24 | ⚪ **CASH** | **+37.4 bps** (±9.4) | `+77.2 bps` | `-0.020 / -0.071` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-04 00:16:20 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,413.74 | ⚪ **CASH** | **+13.9 bps** (±6.2) | `+30.0 bps` | `-0.018 / -0.016` | `0.26%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,276.37 | ⚪ **CASH** | **+28.2 bps** (±18.7) | `+37.5 bps` | `+0.145 / +0.059` | `0.33%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.69 | ⚪ **CASH** | **+37.4 bps** (±9.4) | `+77.2 bps` | `-0.020 / -0.071` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |

---

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
