# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-04 11:31:28 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-04 11:31:28 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,695.63 | ⚪ **CASH** | **+20.2 bps** (±10.8) | `+20.3 bps` | `+0.086 / +0.087` | `0.38%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,336.55 | ⚪ **CASH** | **+13.4 bps** (±17.3) | `+22.1 bps` | `+0.013 / -0.001` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $94.01 | ⚪ **CASH** | **+16.7 bps** (±16.1) | `+11.4 bps` | `+0.052 / +0.192` | `0.50%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 11:15:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,609.79 | ⚪ **CASH** | **+20.2 bps** (±10.8) | `+20.3 bps` | `+0.086 / +0.087` | `0.38%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,331.73 | ⚪ **CASH** | **+13.4 bps** (±17.3) | `+22.1 bps` | `+0.013 / -0.001` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.76 | ⚪ **CASH** | **+16.7 bps** (±16.1) | `+11.4 bps` | `+0.052 / +0.192` | `0.50%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 11:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,602.58 | ⚪ **CASH** | **+20.2 bps** (±10.8) | `+20.3 bps` | `+0.086 / +0.087` | `0.38%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,328.71 | ⚪ **CASH** | **+13.4 bps** (±17.3) | `+22.1 bps` | `+0.013 / -0.001` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.57 | ⚪ **CASH** | **+16.7 bps** (±16.1) | `+11.4 bps` | `+0.052 / +0.192` | `0.50%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 10:46:18 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,526.42 | ⚪ **CASH** | **+20.1 bps** (±14.4) | `+18.2 bps` | `+0.091 / +0.114` | `0.38%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,327.27 | ⚪ **CASH** | **+19.4 bps** (±17.4) | `+33.8 bps` | `+0.008 / -0.008` | `0.44%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.46 | ⚪ **CASH** | **+17.4 bps** (±16.0) | `+14.9 bps` | `+0.042 / +0.170` | `0.49%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 10:31:15 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,548.46 | ⚪ **CASH** | **+20.1 bps** (±14.4) | `+18.2 bps` | `+0.091 / +0.114` | `0.38%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,327.70 | ⚪ **CASH** | **+19.4 bps** (±17.4) | `+33.8 bps` | `+0.008 / -0.008` | `0.44%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.54 | ⚪ **CASH** | **+17.4 bps** (±16.0) | `+14.9 bps` | `+0.042 / +0.170` | `0.49%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 10:16:26 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,524.54 | ⚪ **CASH** | **+20.1 bps** (±14.4) | `+18.2 bps` | `+0.091 / +0.114` | `0.38%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,327.30 | ⚪ **CASH** | **+19.4 bps** (±17.4) | `+33.8 bps` | `+0.008 / -0.008` | `0.44%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.45 | ⚪ **CASH** | **+17.4 bps** (±16.0) | `+14.9 bps` | `+0.042 / +0.170` | `0.49%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 10:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,378.77 | ⚪ **CASH** | **+20.1 bps** (±14.4) | `+18.2 bps` | `+0.091 / +0.114` | `0.38%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,321.31 | ⚪ **CASH** | **+19.4 bps** (±17.4) | `+33.8 bps` | `+0.008 / -0.008` | `0.44%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.09 | ⚪ **CASH** | **+17.4 bps** (±16.0) | `+14.9 bps` | `+0.042 / +0.170` | `0.49%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 09:46:10 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,463.51 | ⚪ **CASH** | **+15.2 bps** (±16.1) | `+9.9 bps` | `+0.099 / +0.091` | `0.39%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,320.73 | ⚪ **CASH** | **+20.0 bps** (±17.5) | `+33.5 bps` | `+0.025 / -0.020` | `0.44%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.01 | ⚪ **CASH** | **+10.8 bps** (±6.6) | `+6.6 bps` | `+0.030 / +0.098` | `0.50%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 09:31:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,392.01 | ⚪ **CASH** | **+15.2 bps** (±16.1) | `+9.9 bps` | `+0.099 / +0.091` | `0.39%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,320.49 | ⚪ **CASH** | **+20.0 bps** (±17.5) | `+33.5 bps` | `+0.025 / -0.020` | `0.44%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.98 | ⚪ **CASH** | **+10.8 bps** (±6.6) | `+6.6 bps` | `+0.030 / +0.098` | `0.50%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 09:16:21 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,429.57 | ⚪ **CASH** | **+15.2 bps** (±16.1) | `+9.9 bps` | `+0.099 / +0.091` | `0.39%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,321.44 | ⚪ **CASH** | **+20.0 bps** (±17.5) | `+33.5 bps` | `+0.025 / -0.020` | `0.44%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.12 | ⚪ **CASH** | **+10.8 bps** (±6.6) | `+6.6 bps` | `+0.030 / +0.098` | `0.50%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 09:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,500.00 | ⚪ **CASH** | **+15.2 bps** (±16.1) | `+9.9 bps` | `+0.099 / +0.091` | `0.39%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,322.76 | ⚪ **CASH** | **+20.0 bps** (±17.5) | `+33.5 bps` | `+0.025 / -0.020` | `0.44%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.29 | ⚪ **CASH** | **+10.8 bps** (±6.6) | `+6.6 bps` | `+0.030 / +0.098` | `0.50%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 08:46:17 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,458.39 | ⚪ **CASH** | **+14.5 bps** (±14.3) | `+11.1 bps` | `+0.099 / +0.049` | `0.38%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,326.80 | ⚪ **CASH** | **+28.4 bps** (±17.4) | `+52.4 bps` | `+0.025 / -0.075` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.38 | ⚪ **CASH** | **+11.3 bps** (±8.1) | `+12.5 bps` | `+0.014 / +0.051` | `0.50%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 08:31:29 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,366.91 | ⚪ **CASH** | **+14.5 bps** (±14.3) | `+11.1 bps` | `+0.099 / +0.049` | `0.38%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,318.71 | ⚪ **CASH** | **+28.4 bps** (±17.4) | `+52.4 bps` | `+0.025 / -0.075` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.30 | ⚪ **CASH** | **+11.3 bps** (±8.1) | `+12.5 bps` | `+0.014 / +0.051` | `0.50%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 08:16:10 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,437.94 | ⚪ **CASH** | **+14.5 bps** (±14.3) | `+11.1 bps` | `+0.099 / +0.049` | `0.38%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,323.83 | ⚪ **CASH** | **+28.4 bps** (±17.4) | `+52.4 bps` | `+0.025 / -0.075` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.47 | ⚪ **CASH** | **+11.3 bps** (±8.1) | `+12.5 bps` | `+0.014 / +0.051` | `0.50%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 08:01:21 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,194.01 | ⚪ **CASH** | **+14.5 bps** (±14.3) | `+11.1 bps` | `+0.099 / +0.049` | `0.38%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,304.94 | ⚪ **CASH** | **+28.4 bps** (±17.4) | `+52.4 bps` | `+0.025 / -0.075` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.13 | ⚪ **CASH** | **+11.3 bps** (±8.1) | `+12.5 bps` | `+0.014 / +0.051` | `0.50%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 07:46:13 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,182.00 | ⚪ **CASH** | **+12.4 bps** (±8.2) | `+8.2 bps` | `+0.090 / +0.038` | `0.39%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,305.25 | ⚪ **CASH** | **+34.6 bps** (±15.7) | `+57.8 bps` | `+0.086 / -0.074` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.19 | ⚪ **CASH** | **+11.0 bps** (±5.1) | `+12.6 bps` | `+0.012 / +0.042` | `0.51%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 07:31:22 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,240.01 | ⚪ **CASH** | **+12.4 bps** (±8.2) | `+8.2 bps` | `+0.090 / +0.038` | `0.39%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,303.38 | ⚪ **CASH** | **+34.6 bps** (±15.7) | `+57.8 bps` | `+0.086 / -0.074` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.20 | ⚪ **CASH** | **+11.0 bps** (±5.1) | `+12.6 bps` | `+0.012 / +0.042` | `0.51%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 07:16:09 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,084.01 | ⚪ **CASH** | **+12.4 bps** (±8.2) | `+8.2 bps` | `+0.090 / +0.038` | `0.39%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,299.43 | ⚪ **CASH** | **+34.6 bps** (±15.7) | `+57.8 bps` | `+0.086 / -0.074` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.97 | ⚪ **CASH** | **+11.0 bps** (±5.1) | `+12.6 bps` | `+0.012 / +0.042` | `0.51%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 07:01:28 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,992.00 | ⚪ **CASH** | **+12.4 bps** (±8.2) | `+8.2 bps` | `+0.090 / +0.038` | `0.39%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,297.67 | ⚪ **CASH** | **+34.6 bps** (±15.7) | `+57.8 bps` | `+0.086 / -0.074` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.95 | ⚪ **CASH** | **+11.0 bps** (±5.1) | `+12.6 bps` | `+0.012 / +0.042` | `0.51%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 06:46:12 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,942.01 | ⚪ **CASH** | **+9.7 bps** (±9.8) | `+5.2 bps` | `+0.078 / +0.041` | `0.39%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,294.84 | ⚪ **CASH** | **+39.1 bps** (±18.9) | `+64.9 bps` | `+0.102 / -0.064` | `0.44%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $92.90 | ⚪ **CASH** | **+3.1 bps** (±12.1) | `+1.3 bps` | `+0.009 / +0.027` | `0.52%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 06:31:19 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,957.07 | ⚪ **CASH** | **+9.7 bps** (±9.8) | `+5.2 bps` | `+0.078 / +0.041` | `0.39%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,295.23 | ⚪ **CASH** | **+39.1 bps** (±18.9) | `+64.9 bps` | `+0.102 / -0.064` | `0.44%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $93.07 | ⚪ **CASH** | **+3.1 bps** (±12.1) | `+1.3 bps` | `+0.009 / +0.027` | `0.52%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 06:16:12 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,782.01 | ⚪ **CASH** | **+9.7 bps** (±9.8) | `+5.2 bps` | `+0.078 / +0.041` | `0.39%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,290.20 | ⚪ **CASH** | **+39.1 bps** (±18.9) | `+64.9 bps` | `+0.102 / -0.064` | `0.44%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $92.71 | ⚪ **CASH** | **+3.1 bps** (±12.1) | `+1.3 bps` | `+0.009 / +0.027` | `0.52%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 06:01:23 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,818.46 | ⚪ **CASH** | **+9.7 bps** (±9.8) | `+5.2 bps` | `+0.078 / +0.041` | `0.39%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,295.59 | ⚪ **CASH** | **+39.1 bps** (±18.9) | `+64.9 bps` | `+0.102 / -0.064` | `0.44%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $92.85 | ⚪ **CASH** | **+3.1 bps** (±12.1) | `+1.3 bps` | `+0.009 / +0.027` | `0.52%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 05:46:24 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,818.01 | ⚪ **CASH** | **+7.6 bps** (±10.8) | `+4.5 bps` | `+0.066 / +0.023` | `0.39%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,296.24 | ⚪ **CASH** | **+34.4 bps** (±14.4) | `+60.4 bps` | `+0.098 / -0.124` | `0.43%/h` | `weak_order_flow` `macro_downtrend` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.00 | ⚪ **CASH** | **+6.0 bps** (±7.8) | `+7.8 bps` | `-0.001 / +0.020` | `0.52%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 05:31:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,446.00 | ⚪ **CASH** | **+7.6 bps** (±10.8) | `+4.5 bps` | `+0.066 / +0.023` | `0.39%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,279.97 | ⚪ **CASH** | **+34.4 bps** (±14.4) | `+60.4 bps` | `+0.098 / -0.124` | `0.43%/h` | `weak_order_flow` `macro_downtrend` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.30 | ⚪ **CASH** | **+6.0 bps** (±7.8) | `+7.8 bps` | `-0.001 / +0.020` | `0.52%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 05:15:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,324.08 | ⚪ **CASH** | **+7.6 bps** (±10.8) | `+4.5 bps` | `+0.066 / +0.023` | `0.39%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,278.96 | ⚪ **CASH** | **+34.4 bps** (±14.4) | `+60.4 bps` | `+0.098 / -0.124` | `0.43%/h` | `weak_order_flow` `macro_downtrend` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.09 | ⚪ **CASH** | **+6.0 bps** (±7.8) | `+7.8 bps` | `-0.001 / +0.020` | `0.52%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 05:01:19 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,330.01 | ⚪ **CASH** | **+7.6 bps** (±10.8) | `+4.5 bps` | `+0.066 / +0.023` | `0.39%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,279.24 | ⚪ **CASH** | **+34.4 bps** (±14.4) | `+60.4 bps` | `+0.098 / -0.124` | `0.43%/h` | `weak_order_flow` `macro_downtrend` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.29 | ⚪ **CASH** | **+6.0 bps** (±7.8) | `+7.8 bps` | `-0.001 / +0.020` | `0.52%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 04:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,012.79 | ⚪ **CASH** | **+6.4 bps** (±7.1) | `+6.4 bps` | `+0.051 / -0.013` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,268.56 | ⚪ **CASH** | **+21.4 bps** (±18.1) | `+41.1 bps` | `+0.097 / -0.169` | `0.36%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.79 | ⚪ **CASH** | **+1.8 bps** (±7.6) | `+4.9 bps` | `-0.013 / -0.021` | `0.45%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 04:31:22 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,753.61 | ⚪ **CASH** | **+6.4 bps** (±7.1) | `+6.4 bps` | `+0.051 / -0.013` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,259.30 | ⚪ **CASH** | **+21.4 bps** (±18.1) | `+41.1 bps` | `+0.097 / -0.169` | `0.36%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.52 | ⚪ **CASH** | **+1.8 bps** (±7.6) | `+4.9 bps` | `-0.013 / -0.021` | `0.45%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

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
