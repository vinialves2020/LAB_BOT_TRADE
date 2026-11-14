# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-14 01:30:41 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-14 01:30:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,347.93 | ⚪ **CASH** | **-12.4 bps** (±12.3) | `-12.6 bps` | `-0.023 / -0.068` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,931.56 | ⚪ **CASH** | **+4.5 bps** (±14.0) | `+19.7 bps` | `-0.067 / -0.018` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $77.40 | ⚪ **CASH** | **-1.5 bps** (±11.9) | `+2.9 bps` | `-0.017 / -0.012` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.3 bps) |

---

### 🕒 Ciclo `2026-11-14 01:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,231.72 | ⚪ **CASH** | **-12.4 bps** (±12.3) | `-12.6 bps` | `-0.023 / -0.068` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,928.85 | ⚪ **CASH** | **+4.5 bps** (±14.0) | `+19.7 bps` | `-0.067 / -0.018` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $77.38 | ⚪ **CASH** | **-1.5 bps** (±11.9) | `+2.9 bps` | `-0.017 / -0.012` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.3 bps) |

---

### 🕒 Ciclo `2026-11-14 01:00:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,306.01 | ⚪ **CASH** | **-12.4 bps** (±12.3) | `-12.6 bps` | `-0.023 / -0.068` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,931.44 | ⚪ **CASH** | **+4.5 bps** (±14.0) | `+19.7 bps` | `-0.067 / -0.018` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $77.64 | ⚪ **CASH** | **-1.5 bps** (±11.9) | `+2.9 bps` | `-0.017 / -0.012` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.3 bps) |

---

### 🕒 Ciclo `2026-11-14 00:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,311.26 | ⚪ **CASH** | **-12.0 bps** (±10.9) | `-11.4 bps` | `-0.030 / -0.062` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,930.75 | ⚪ **CASH** | **+1.8 bps** (±16.5) | `+17.2 bps` | `-0.071 / -0.038` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |
| **SOLUSDT** | $77.94 | ⚪ **CASH** | **+5.3 bps** (±11.0) | `+15.4 bps` | `-0.018 / -0.010` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.6 bps) |

---

### 🕒 Ciclo `2026-11-14 00:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,330.01 | ⚪ **CASH** | **-12.0 bps** (±10.9) | `-11.4 bps` | `-0.030 / -0.062` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,933.98 | ⚪ **CASH** | **+1.8 bps** (±16.5) | `+17.2 bps` | `-0.071 / -0.038` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |
| **SOLUSDT** | $78.35 | ⚪ **CASH** | **+5.3 bps** (±11.0) | `+15.4 bps` | `-0.018 / -0.010` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.6 bps) |

---

### 🕒 Ciclo `2026-11-14 00:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,377.22 | ⚪ **CASH** | **-12.0 bps** (±10.9) | `-11.4 bps` | `-0.030 / -0.062` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,933.96 | ⚪ **CASH** | **+1.8 bps** (±16.5) | `+17.2 bps` | `-0.071 / -0.038` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |
| **SOLUSDT** | $78.40 | ⚪ **CASH** | **+5.3 bps** (±11.0) | `+15.4 bps` | `-0.018 / -0.010` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.6 bps) |

---

### 🕒 Ciclo `2026-11-14 00:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,374.47 | ⚪ **CASH** | **-12.0 bps** (±10.9) | `-11.4 bps` | `-0.030 / -0.062` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,934.53 | ⚪ **CASH** | **+1.8 bps** (±16.5) | `+17.2 bps` | `-0.071 / -0.038` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |
| **SOLUSDT** | $78.31 | ⚪ **CASH** | **+5.3 bps** (±11.0) | `+15.4 bps` | `-0.018 / -0.010` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.6 bps) |

---

### 🕒 Ciclo `2026-11-13 23:45:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,156.01 | ⚪ **CASH** | **-14.7 bps** (±9.6) | `-16.9 bps` | `-0.030 / -0.058` | `0.50%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.8 bps) |
| **ETHUSDT** | $1,924.21 | ⚪ **CASH** | **+4.9 bps** (±13.6) | `+21.5 bps` | `-0.070 / -0.026` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |
| **SOLUSDT** | $77.96 | ⚪ **CASH** | **-2.7 bps** (±7.5) | `+3.4 bps` | `-0.022 / -0.052` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.3 bps) |

---

### 🕒 Ciclo `2026-11-13 23:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,178.15 | ⚪ **CASH** | **-14.7 bps** (±9.6) | `-16.9 bps` | `-0.030 / -0.058` | `0.50%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.8 bps) |
| **ETHUSDT** | $1,925.65 | ⚪ **CASH** | **+4.9 bps** (±13.6) | `+21.5 bps` | `-0.070 / -0.026` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |
| **SOLUSDT** | $77.85 | ⚪ **CASH** | **-2.7 bps** (±7.5) | `+3.4 bps` | `-0.022 / -0.052` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.3 bps) |

---

### 🕒 Ciclo `2026-11-13 23:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,992.00 | ⚪ **CASH** | **-14.7 bps** (±9.6) | `-16.9 bps` | `-0.030 / -0.058` | `0.50%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.8 bps) |
| **ETHUSDT** | $1,919.55 | ⚪ **CASH** | **+4.9 bps** (±13.6) | `+21.5 bps` | `-0.070 / -0.026` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |
| **SOLUSDT** | $77.45 | ⚪ **CASH** | **-2.7 bps** (±7.5) | `+3.4 bps` | `-0.022 / -0.052` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.3 bps) |

---

### 🕒 Ciclo `2026-11-13 23:00:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,211.03 | ⚪ **CASH** | **-14.7 bps** (±9.6) | `-16.9 bps` | `-0.030 / -0.058` | `0.50%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.8 bps) |
| **ETHUSDT** | $1,923.03 | ⚪ **CASH** | **+4.9 bps** (±13.6) | `+21.5 bps` | `-0.070 / -0.026` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |
| **SOLUSDT** | $77.66 | ⚪ **CASH** | **-2.7 bps** (±7.5) | `+3.4 bps` | `-0.022 / -0.052` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.3 bps) |

---

### 🕒 Ciclo `2026-11-13 22:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,436.00 | ⚪ **CASH** | **-15.6 bps** (±12.0) | `-18.8 bps` | `-0.028 / -0.049` | `0.50%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |
| **ETHUSDT** | $1,932.42 | ⚪ **CASH** | **+7.7 bps** (±14.6) | `+25.7 bps` | `-0.067 / -0.018` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |
| **SOLUSDT** | $78.41 | ⚪ **CASH** | **+2.5 bps** (±3.8) | `+12.7 bps` | `-0.018 / -0.065` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |

---

### 🕒 Ciclo `2026-11-13 22:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,302.01 | ⚪ **CASH** | **-15.6 bps** (±12.0) | `-18.8 bps` | `-0.028 / -0.049` | `0.50%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |
| **ETHUSDT** | $1,927.49 | ⚪ **CASH** | **+7.7 bps** (±14.6) | `+25.7 bps` | `-0.067 / -0.018` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |
| **SOLUSDT** | $78.59 | ⚪ **CASH** | **+2.5 bps** (±3.8) | `+12.7 bps` | `-0.018 / -0.065` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |

---

### 🕒 Ciclo `2026-11-13 22:15:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,157.64 | ⚪ **CASH** | **-15.6 bps** (±12.0) | `-18.8 bps` | `-0.028 / -0.049` | `0.50%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |
| **ETHUSDT** | $1,921.36 | ⚪ **CASH** | **+7.7 bps** (±14.6) | `+25.7 bps` | `-0.067 / -0.018` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |
| **SOLUSDT** | $78.17 | ⚪ **CASH** | **+2.5 bps** (±3.8) | `+12.7 bps` | `-0.018 / -0.065` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |

---

### 🕒 Ciclo `2026-11-13 22:01:04 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,454.01 | ⚪ **CASH** | **-15.6 bps** (±12.0) | `-18.8 bps` | `-0.028 / -0.049` | `0.50%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |
| **ETHUSDT** | $1,930.57 | ⚪ **CASH** | **+7.7 bps** (±14.6) | `+25.7 bps` | `-0.067 / -0.018` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |
| **SOLUSDT** | $78.77 | ⚪ **CASH** | **+2.5 bps** (±3.8) | `+12.7 bps` | `-0.018 / -0.065` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |

---

### 🕒 Ciclo `2026-11-13 21:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,211.85 | ⚪ **CASH** | **-7.1 bps** (±10.8) | `-11.0 bps` | `-0.028 / +0.065` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,923.72 | ⚪ **CASH** | **-22.3 bps** (±4.0) | `-27.4 bps` | `-0.060 / -0.079` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |
| **SOLUSDT** | $78.74 | ⚪ **CASH** | **-11.4 bps** (±12.7) | `-19.9 bps` | `-0.005 / +0.051` | `0.66%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-13 21:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,385.17 | ⚪ **CASH** | **-7.1 bps** (±10.8) | `-11.0 bps` | `-0.028 / +0.065` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,932.39 | ⚪ **CASH** | **-22.3 bps** (±4.0) | `-27.4 bps` | `-0.060 / -0.079` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |
| **SOLUSDT** | $79.38 | ⚪ **CASH** | **-11.4 bps** (±12.7) | `-19.9 bps` | `-0.005 / +0.051` | `0.66%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-13 21:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,558.30 | ⚪ **CASH** | **-7.1 bps** (±10.8) | `-11.0 bps` | `-0.028 / +0.065` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,937.45 | ⚪ **CASH** | **-22.3 bps** (±4.0) | `-27.4 bps` | `-0.060 / -0.079` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |
| **SOLUSDT** | $79.53 | ⚪ **CASH** | **-11.4 bps** (±12.7) | `-19.9 bps` | `-0.005 / +0.051` | `0.66%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-13 21:00:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,870.01 | ⚪ **CASH** | **-7.1 bps** (±10.8) | `-11.0 bps` | `-0.028 / +0.065` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,947.21 | ⚪ **CASH** | **-22.3 bps** (±4.0) | `-27.4 bps` | `-0.060 / -0.079` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |
| **SOLUSDT** | $79.90 | ⚪ **CASH** | **-11.4 bps** (±12.7) | `-19.9 bps` | `-0.005 / +0.051` | `0.66%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-13 20:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,952.01 | ⚪ **CASH** | **-7.0 bps** (±7.5) | `-9.8 bps` | `-0.026 / +0.037` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.3 bps) |
| **ETHUSDT** | $1,948.25 | ⚪ **CASH** | **-7.3 bps** (±8.3) | `-0.3 bps` | `-0.052 / -0.076` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.2 bps) |
| **SOLUSDT** | $80.15 | ⚪ **CASH** | **-11.6 bps** (±9.1) | `-19.6 bps` | `-0.004 / +0.027` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.7 bps) |

---

### 🕒 Ciclo `2026-11-13 20:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,967.65 | ⚪ **CASH** | **-7.0 bps** (±7.5) | `-9.8 bps` | `-0.026 / +0.037` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.3 bps) |
| **ETHUSDT** | $1,950.73 | ⚪ **CASH** | **-7.3 bps** (±8.3) | `-0.3 bps` | `-0.052 / -0.076` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.2 bps) |
| **SOLUSDT** | $80.32 | ⚪ **CASH** | **-11.6 bps** (±9.1) | `-19.6 bps` | `-0.004 / +0.027` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.7 bps) |

---

### 🕒 Ciclo `2026-11-13 20:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,089.76 | ⚪ **CASH** | **-7.0 bps** (±7.5) | `-9.8 bps` | `-0.026 / +0.037` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.3 bps) |
| **ETHUSDT** | $1,954.21 | ⚪ **CASH** | **-7.3 bps** (±8.3) | `-0.3 bps` | `-0.052 / -0.076` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.2 bps) |
| **SOLUSDT** | $80.38 | ⚪ **CASH** | **-11.6 bps** (±9.1) | `-19.6 bps` | `-0.004 / +0.027` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.7 bps) |

---

### 🕒 Ciclo `2026-11-13 20:00:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,016.96 | ⚪ **CASH** | **-7.0 bps** (±7.5) | `-9.8 bps` | `-0.026 / +0.037` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.3 bps) |
| **ETHUSDT** | $1,952.12 | ⚪ **CASH** | **-7.3 bps** (±8.3) | `-0.3 bps` | `-0.052 / -0.076` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.2 bps) |
| **SOLUSDT** | $80.22 | ⚪ **CASH** | **-11.6 bps** (±9.1) | `-19.6 bps` | `-0.004 / +0.027` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.7 bps) |

---

### 🕒 Ciclo `2026-11-13 19:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,983.93 | ⚪ **CASH** | **-10.1 bps** (±9.5) | `-15.8 bps` | `-0.028 / +0.051` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.4 bps) |
| **ETHUSDT** | $1,948.78 | ⚪ **CASH** | **-12.8 bps** (±12.8) | `-12.2 bps` | `-0.052 / -0.035` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |
| **SOLUSDT** | $80.01 | ⚪ **CASH** | **-11.7 bps** (±9.8) | `-21.2 bps` | `+0.004 / +0.043` | `0.68%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.8 bps) |

---

### 🕒 Ciclo `2026-11-13 19:30:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,025.71 | ⚪ **CASH** | **-10.1 bps** (±9.5) | `-15.8 bps` | `-0.028 / +0.051` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.4 bps) |
| **ETHUSDT** | $1,948.85 | ⚪ **CASH** | **-12.8 bps** (±12.8) | `-12.2 bps` | `-0.052 / -0.035` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |
| **SOLUSDT** | $79.98 | ⚪ **CASH** | **-11.7 bps** (±9.8) | `-21.2 bps` | `+0.004 / +0.043` | `0.68%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.8 bps) |

---

### 🕒 Ciclo `2026-11-13 19:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,074.01 | ⚪ **CASH** | **-10.1 bps** (±9.5) | `-15.8 bps` | `-0.028 / +0.051` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.4 bps) |
| **ETHUSDT** | $1,951.37 | ⚪ **CASH** | **-12.8 bps** (±12.8) | `-12.2 bps` | `-0.052 / -0.035` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |
| **SOLUSDT** | $80.29 | ⚪ **CASH** | **-11.7 bps** (±9.8) | `-21.2 bps` | `+0.004 / +0.043` | `0.68%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.8 bps) |

---

### 🕒 Ciclo `2026-11-13 19:01:00 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,889.67 | ⚪ **CASH** | **-10.1 bps** (±9.5) | `-15.8 bps` | `-0.028 / +0.051` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.4 bps) |
| **ETHUSDT** | $1,941.24 | ⚪ **CASH** | **-12.8 bps** (±12.8) | `-12.2 bps` | `-0.052 / -0.035` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |
| **SOLUSDT** | $79.96 | ⚪ **CASH** | **-11.7 bps** (±9.8) | `-21.2 bps` | `+0.004 / +0.043` | `0.68%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.8 bps) |

---

### 🕒 Ciclo `2026-11-13 18:45:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,845.39 | ⚪ **CASH** | **-9.7 bps** (±6.1) | `-15.0 bps` | `-0.031 / +0.047` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.5 bps) |
| **ETHUSDT** | $1,939.89 | ⚪ **CASH** | **-5.6 bps** (±15.4) | `+1.6 bps` | `-0.050 / -0.040` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.1 bps) |
| **SOLUSDT** | $79.97 | ⚪ **CASH** | **-4.5 bps** (±11.2) | `-8.0 bps` | `+0.006 / +0.042` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.9 bps) |

---

### 🕒 Ciclo `2026-11-13 18:30:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,909.53 | ⚪ **CASH** | **-9.7 bps** (±6.1) | `-15.0 bps` | `-0.031 / +0.047` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.5 bps) |
| **ETHUSDT** | $1,940.43 | ⚪ **CASH** | **-5.6 bps** (±15.4) | `+1.6 bps` | `-0.050 / -0.040` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.1 bps) |
| **SOLUSDT** | $80.03 | ⚪ **CASH** | **-4.5 bps** (±11.2) | `-8.0 bps` | `+0.006 / +0.042` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.9 bps) |

---

### 🕒 Ciclo `2026-11-13 18:15:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,882.21 | ⚪ **CASH** | **-9.7 bps** (±6.1) | `-15.0 bps` | `-0.031 / +0.047` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.5 bps) |
| **ETHUSDT** | $1,939.50 | ⚪ **CASH** | **-5.6 bps** (±15.4) | `+1.6 bps` | `-0.050 / -0.040` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.1 bps) |
| **SOLUSDT** | $80.11 | ⚪ **CASH** | **-4.5 bps** (±11.2) | `-8.0 bps` | `+0.006 / +0.042` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.9 bps) |

---

### 🕒 Ciclo `2026-11-13 18:01:09 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,876.56 | ⚪ **CASH** | **-9.7 bps** (±6.1) | `-15.0 bps` | `-0.031 / +0.047` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.5 bps) |
| **ETHUSDT** | $1,936.36 | ⚪ **CASH** | **-5.6 bps** (±15.4) | `+1.6 bps` | `-0.050 / -0.040` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.1 bps) |
| **SOLUSDT** | $79.89 | ⚪ **CASH** | **-4.5 bps** (±11.2) | `-8.0 bps` | `+0.006 / +0.042` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.9 bps) |

---

### 🕒 Ciclo `2026-11-13 17:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,977.94 | ⚪ **CASH** | **-11.8 bps** (±4.8) | `-19.3 bps` | `-0.029 / +0.044` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.8 bps) |
| **ETHUSDT** | $1,941.60 | ⚪ **CASH** | **+16.4 bps** (±18.6) | `+41.7 bps` | `-0.049 / -0.033` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |
| **SOLUSDT** | $80.30 | ⚪ **CASH** | **-10.0 bps** (±9.3) | `-18.2 bps` | `+0.003 / +0.044` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.5 bps) |

---

### 🕒 Ciclo `2026-11-13 17:30:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,702.03 | ⚪ **CASH** | **-11.8 bps** (±4.8) | `-19.3 bps` | `-0.029 / +0.044` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.8 bps) |
| **ETHUSDT** | $1,932.71 | ⚪ **CASH** | **+16.4 bps** (±18.6) | `+41.7 bps` | `-0.049 / -0.033` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |
| **SOLUSDT** | $79.96 | ⚪ **CASH** | **-10.0 bps** (±9.3) | `-18.2 bps` | `+0.003 / +0.044` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.5 bps) |

---

### 🕒 Ciclo `2026-11-13 17:15:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,670.48 | ⚪ **CASH** | **-11.8 bps** (±4.8) | `-19.3 bps` | `-0.029 / +0.044` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.8 bps) |
| **ETHUSDT** | $1,928.38 | ⚪ **CASH** | **+16.4 bps** (±18.6) | `+41.7 bps` | `-0.049 / -0.033` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |
| **SOLUSDT** | $79.62 | ⚪ **CASH** | **-10.0 bps** (±9.3) | `-18.2 bps` | `+0.003 / +0.044` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.5 bps) |

---

### 🕒 Ciclo `2026-11-13 17:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,617.54 | ⚪ **CASH** | **-11.8 bps** (±4.8) | `-19.3 bps` | `-0.029 / +0.044` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.8 bps) |
| **ETHUSDT** | $1,924.77 | ⚪ **CASH** | **+16.4 bps** (±18.6) | `+41.7 bps` | `-0.049 / -0.033` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |
| **SOLUSDT** | $79.48 | ⚪ **CASH** | **-10.0 bps** (±9.3) | `-18.2 bps` | `+0.003 / +0.044` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.5 bps) |

---

### 🕒 Ciclo `2026-11-13 16:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,609.00 | ⚪ **CASH** | **-9.2 bps** (±4.8) | `-14.8 bps` | `-0.026 / +0.042` | `0.53%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.9 bps) |
| **ETHUSDT** | $1,925.86 | ⚪ **CASH** | **+9.6 bps** (±22.1) | `+28.4 bps` | `-0.046 / -0.017` | `0.65%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **SOLUSDT** | $79.39 | ⚪ **CASH** | **+10.3 bps** (±11.0) | `+17.1 bps` | `+0.012 / +0.058` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.0 bps) |
