# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-03 20:30:52 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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
