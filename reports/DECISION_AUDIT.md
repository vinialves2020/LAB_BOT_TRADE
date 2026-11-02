# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-02 23:02:32 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-11-02 19:47:13 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,765.04 | ⚪ **CASH** | **+43.6 bps** (±7.1) | `+59.6 bps` | `+0.090 / +0.117` | `0.22%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,240.14 | ⚪ **CASH** | **+49.9 bps** (±8.0) | `+96.6 bps` | `-0.067 / -0.035` | `0.31%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $91.06 | ⚪ **CASH** | **+7.8 bps** (±20.4) | `-2.9 bps` | `+0.104 / +0.095` | `0.43%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 19:32:31 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,950.01 | ⚪ **CASH** | **+43.6 bps** (±7.1) | `+59.6 bps` | `+0.090 / +0.117` | `0.22%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,250.34 | ⚪ **CASH** | **+49.9 bps** (±8.0) | `+96.6 bps` | `-0.067 / -0.035` | `0.31%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $91.60 | ⚪ **CASH** | **+7.8 bps** (±20.4) | `-2.9 bps` | `+0.104 / +0.095` | `0.43%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 19:17:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,988.03 | ⚪ **CASH** | **+43.6 bps** (±7.1) | `+59.6 bps` | `+0.090 / +0.117` | `0.22%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,250.56 | ⚪ **CASH** | **+49.9 bps** (±8.0) | `+96.6 bps` | `-0.067 / -0.035` | `0.31%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $91.82 | ⚪ **CASH** | **+7.8 bps** (±20.4) | `-2.9 bps` | `+0.104 / +0.095` | `0.43%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 19:02:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,962.61 | ⚪ **CASH** | **+43.6 bps** (±7.1) | `+59.6 bps` | `+0.090 / +0.117` | `0.22%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,251.44 | ⚪ **CASH** | **+49.9 bps** (±8.0) | `+96.6 bps` | `-0.067 / -0.035` | `0.31%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $92.20 | ⚪ **CASH** | **+7.8 bps** (±20.4) | `-2.9 bps` | `+0.104 / +0.095` | `0.43%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 18:47:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,005.79 | ⚪ **CASH** | **+31.8 bps** (±7.4) | `+41.2 bps` | `+0.076 / +0.103` | `0.22%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,253.35 | ⚪ **CASH** | **+51.2 bps** (±8.9) | `+96.7 bps` | `-0.065 / +0.011` | `0.32%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $92.08 | ⚪ **CASH** | **+10.6 bps** (±23.9) | `+4.7 bps` | `+0.095 / +0.089` | `0.43%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 18:32:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,948.84 | ⚪ **CASH** | **+31.8 bps** (±7.4) | `+41.2 bps` | `+0.076 / +0.103` | `0.22%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,250.35 | ⚪ **CASH** | **+51.2 bps** (±8.9) | `+96.7 bps` | `-0.065 / +0.011` | `0.32%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $91.83 | ⚪ **CASH** | **+10.6 bps** (±23.9) | `+4.7 bps` | `+0.095 / +0.089` | `0.43%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 18:17:12 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,257.07 | ⚪ **CASH** | **+31.8 bps** (±7.4) | `+41.2 bps` | `+0.076 / +0.103` | `0.22%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,259.68 | ⚪ **CASH** | **+51.2 bps** (±8.9) | `+96.7 bps` | `-0.065 / +0.011` | `0.32%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $92.36 | ⚪ **CASH** | **+10.6 bps** (±23.9) | `+4.7 bps` | `+0.095 / +0.089` | `0.43%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 17:47:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,894.25 | ⚪ **CASH** | **+31.4 bps** (±10.0) | `+37.6 bps` | `+0.088 / +0.127` | `0.21%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,247.66 | ⚪ **CASH** | **+40.1 bps** (±8.2) | `+77.6 bps` | `-0.065 / -0.016` | `0.31%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $91.69 | ⚪ **CASH** | **+18.8 bps** (±16.1) | `+16.4 bps` | `+0.095 / +0.108` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 17:32:25 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,092.00 | ⚪ **CASH** | **+31.4 bps** (±10.0) | `+37.6 bps` | `+0.088 / +0.127` | `0.21%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,255.30 | ⚪ **CASH** | **+40.1 bps** (±8.2) | `+77.6 bps` | `-0.065 / -0.016` | `0.31%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $92.63 | ⚪ **CASH** | **+18.8 bps** (±16.1) | `+16.4 bps` | `+0.095 / +0.108` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 17:17:22 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,446.23 | ⚪ **CASH** | **+31.4 bps** (±10.0) | `+37.6 bps` | `+0.088 / +0.127` | `0.21%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,269.54 | ⚪ **CASH** | **+40.1 bps** (±8.2) | `+77.6 bps` | `-0.065 / -0.016` | `0.31%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $93.19 | ⚪ **CASH** | **+18.8 bps** (±16.1) | `+16.4 bps` | `+0.095 / +0.108` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 17:03:07 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,507.36 | 🔴 **SELL** | **+31.4 bps** (±10.0) | `+37.6 bps` | `+0.088 / +0.127` | `0.21%/h` | `vol_compressed` | Alvo temporal de 12h concluído (-1.18%) |
| **ETHUSDT** | $2,270.16 | 🔴 **SELL** | **+40.1 bps** (±8.2) | `+77.6 bps` | `-0.065 / -0.016` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Alvo temporal de 12h concluído (-1.01%) |
| **SOLUSDT** | $93.48 | ⚪ **CASH** | **+18.8 bps** (±16.1) | `+16.4 bps` | `+0.095 / +0.108` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 16:47:47 UTC` | Patrimônio: **$960.76 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,499.61 | 🟡 **HOLD** | **+26.3 bps** (±10.2) | `+32.7 bps` | `+0.078 / +0.082` | `0.22%/h` | `vol_compressed` | Posição ativa há 11.8h (PnL: -1.19% | Pico: +0.00%) |
| **ETHUSDT** | $2,270.15 | 🟡 **HOLD** | **+45.5 bps** (±9.6) | `+96.8 bps` | `-0.057 / -0.162` | `0.32%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 11.8h (PnL: -1.01% | Pico: +0.31%) |
| **SOLUSDT** | $93.46 | ⚪ **CASH** | **+18.3 bps** (±14.9) | `+17.4 bps` | `+0.089 / +0.091` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 16:32:37 UTC` | Patrimônio: **$960.67 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,446.82 | 🟡 **HOLD** | **+26.3 bps** (±10.2) | `+32.7 bps` | `+0.078 / +0.082` | `0.22%/h` | `vol_compressed` | Posição ativa há 11.5h (PnL: -1.26% | Pico: +0.00%) |
| **ETHUSDT** | $2,271.01 | 🟡 **HOLD** | **+45.5 bps** (±9.6) | `+96.8 bps` | `-0.057 / -0.162` | `0.32%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 11.5h (PnL: -0.98% | Pico: +0.31%) |
| **SOLUSDT** | $93.51 | ⚪ **CASH** | **+18.3 bps** (±14.9) | `+17.4 bps` | `+0.089 / +0.091` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 16:17:34 UTC` | Patrimônio: **$960.41 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,394.38 | 🟡 **HOLD** | **+26.3 bps** (±10.2) | `+32.7 bps` | `+0.078 / +0.082` | `0.22%/h` | `vol_compressed` | Posição ativa há 11.2h (PnL: -1.32% | Pico: +0.00%) |
| **ETHUSDT** | $2,269.13 | 🟡 **HOLD** | **+45.5 bps** (±9.6) | `+96.8 bps` | `-0.057 / -0.162` | `0.32%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 11.2h (PnL: -1.06% | Pico: +0.31%) |
| **SOLUSDT** | $93.29 | ⚪ **CASH** | **+18.3 bps** (±14.9) | `+17.4 bps` | `+0.089 / +0.091` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 16:02:25 UTC` | Patrimônio: **$961.33 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,574.97 | 🟡 **HOLD** | **+26.3 bps** (±10.2) | `+32.7 bps` | `+0.078 / +0.082` | `0.22%/h` | `vol_compressed` | Posição ativa há 11.0h (PnL: -1.09% | Pico: +0.00%) |
| **ETHUSDT** | $2,275.95 | 🟡 **HOLD** | **+45.5 bps** (±9.6) | `+96.8 bps` | `-0.057 / -0.162` | `0.32%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 11.0h (PnL: -0.76% | Pico: +0.31%) |
| **SOLUSDT** | $93.58 | ⚪ **CASH** | **+18.3 bps** (±14.9) | `+17.4 bps` | `+0.089 / +0.091` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 15:47:18 UTC` | Patrimônio: **$963.38 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,983.85 | 🟡 **HOLD** | **+27.0 bps** (±7.0) | `+32.0 bps` | `+0.089 / +0.081` | `0.21%/h` | `vol_compressed` | Posição ativa há 10.7h (PnL: -0.57% | Pico: +0.00%) |
| **ETHUSDT** | $2,290.83 | 🟡 **HOLD** | **+43.9 bps** (±11.7) | `+95.2 bps` | `-0.046 / -0.200` | `0.28%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 10.7h (PnL: -0.11% | Pico: +0.31%) |
| **SOLUSDT** | $94.26 | ⚪ **CASH** | **+24.5 bps** (±20.0) | `+23.9 bps` | `+0.104 / +0.147` | `0.36%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-02 15:32:29 UTC` | Patrimônio: **$962.96 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,855.10 | 🟡 **HOLD** | **+27.0 bps** (±7.0) | `+32.0 bps` | `+0.089 / +0.081` | `0.21%/h` | `vol_compressed` | Posição ativa há 10.5h (PnL: -0.74% | Pico: +0.00%) |
| **ETHUSDT** | $2,289.80 | 🟡 **HOLD** | **+43.9 bps** (±11.7) | `+95.2 bps` | `-0.046 / -0.200` | `0.28%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 10.5h (PnL: -0.16% | Pico: +0.31%) |
| **SOLUSDT** | $94.13 | ⚪ **CASH** | **+24.5 bps** (±20.0) | `+23.9 bps` | `+0.104 / +0.147` | `0.36%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-02 15:17:19 UTC` | Patrimônio: **$963.58 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,978.00 | 🟡 **HOLD** | **+27.0 bps** (±7.0) | `+32.0 bps` | `+0.089 / +0.081` | `0.21%/h` | `vol_compressed` | Posição ativa há 10.2h (PnL: -0.58% | Pico: +0.00%) |
| **ETHUSDT** | $2,294.26 | 🟡 **HOLD** | **+43.9 bps** (±11.7) | `+95.2 bps` | `-0.046 / -0.200` | `0.28%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 10.2h (PnL: +0.04% | Pico: +0.31%) |
| **SOLUSDT** | $94.47 | ⚪ **CASH** | **+24.5 bps** (±20.0) | `+23.9 bps` | `+0.104 / +0.147` | `0.36%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-02 15:02:24 UTC` | Patrimônio: **$962.64 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,805.65 | 🟡 **HOLD** | **+27.0 bps** (±7.0) | `+32.0 bps` | `+0.089 / +0.081` | `0.21%/h` | `vol_compressed` | Posição ativa há 10.0h (PnL: -0.80% | Pico: +0.00%) |
| **ETHUSDT** | $2,286.81 | 🟡 **HOLD** | **+43.9 bps** (±11.7) | `+95.2 bps` | `-0.046 / -0.200` | `0.28%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 10.0h (PnL: -0.29% | Pico: +0.31%) |
| **SOLUSDT** | $94.22 | ⚪ **CASH** | **+24.5 bps** (±20.0) | `+23.9 bps` | `+0.104 / +0.147` | `0.36%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-02 14:47:28 UTC` | Patrimônio: **$963.38 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,934.00 | 🟡 **HOLD** | **+27.5 bps** (±12.0) | `+39.3 bps` | `+0.066 / +0.048` | `0.21%/h` | `vol_compressed` | Posição ativa há 9.7h (PnL: -0.64% | Pico: +0.00%) |
| **ETHUSDT** | $2,292.94 | 🟡 **HOLD** | **+59.4 bps** (±9.1) | `+124.3 bps` | `-0.049 / -0.201` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 9.7h (PnL: -0.02% | Pico: +0.31%) |
| **SOLUSDT** | $94.49 | ⚪ **CASH** | **+18.8 bps** (±18.3) | `+14.8 bps` | `+0.097 / +0.153` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 14:32:34 UTC` | Patrimônio: **$963.60 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,017.13 | 🟡 **HOLD** | **+27.5 bps** (±12.0) | `+39.3 bps` | `+0.066 / +0.048` | `0.21%/h` | `vol_compressed` | Posição ativa há 9.5h (PnL: -0.53% | Pico: +0.00%) |
| **ETHUSDT** | $2,292.97 | 🟡 **HOLD** | **+59.4 bps** (±9.1) | `+124.3 bps` | `-0.049 / -0.201` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 9.5h (PnL: -0.02% | Pico: +0.31%) |
| **SOLUSDT** | $94.43 | ⚪ **CASH** | **+18.8 bps** (±18.3) | `+14.8 bps` | `+0.097 / +0.153` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 14:17:37 UTC` | Patrimônio: **$963.37 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,955.29 | 🟡 **HOLD** | **+27.5 bps** (±12.0) | `+39.3 bps` | `+0.066 / +0.048` | `0.21%/h` | `vol_compressed` | Posição ativa há 9.3h (PnL: -0.61% | Pico: +0.00%) |
| **ETHUSDT** | $2,291.85 | 🟡 **HOLD** | **+59.4 bps** (±9.1) | `+124.3 bps` | `-0.049 / -0.201` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 9.3h (PnL: -0.07% | Pico: +0.31%) |
| **SOLUSDT** | $94.22 | ⚪ **CASH** | **+18.8 bps** (±18.3) | `+14.8 bps` | `+0.097 / +0.153` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 14:02:37 UTC` | Patrimônio: **$963.34 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,988.00 | 🟡 **HOLD** | **+27.5 bps** (±12.0) | `+39.3 bps` | `+0.066 / +0.048` | `0.21%/h` | `vol_compressed` | Posição ativa há 9.0h (PnL: -0.57% | Pico: +0.00%) |
| **ETHUSDT** | $2,290.05 | 🟡 **HOLD** | **+59.4 bps** (±9.1) | `+124.3 bps` | `-0.049 / -0.201` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 9.0h (PnL: -0.15% | Pico: +0.31%) |
| **SOLUSDT** | $94.45 | ⚪ **CASH** | **+18.8 bps** (±18.3) | `+14.8 bps` | `+0.097 / +0.153` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
