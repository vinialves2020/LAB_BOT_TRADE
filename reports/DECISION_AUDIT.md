# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-09 06:15:36 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-09 06:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,481.07 | ⚪ **CASH** | **-10.5 bps** (±6.0) | `-16.7 bps` | `-0.013 / +0.010` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,128.33 | ⚪ **CASH** | **-63.8 bps** (±18.9) | `-79.8 bps` | `-0.148 / -0.268` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.41 | ⚪ **CASH** | **-15.7 bps** (±19.4) | `-32.8 bps` | `+0.046 / +0.059` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 06:00:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,516.08 | ⚪ **CASH** | **-10.5 bps** (±6.0) | `-16.7 bps` | `-0.013 / +0.010` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,130.54 | ⚪ **CASH** | **-63.8 bps** (±18.9) | `-79.8 bps` | `-0.148 / -0.268` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.72 | ⚪ **CASH** | **-15.7 bps** (±19.4) | `-32.8 bps` | `+0.046 / +0.059` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 05:45:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,422.90 | ⚪ **CASH** | **-11.7 bps** (±13.1) | `-18.4 bps` | `-0.019 / +0.035` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,130.04 | ⚪ **CASH** | **-61.9 bps** (±17.4) | `-84.1 bps` | `-0.131 / -0.175` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.87 | ⚪ **CASH** | **-7.7 bps** (±11.3) | `-25.4 bps` | `+0.059 / +0.130` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 05:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,558.64 | ⚪ **CASH** | **-11.7 bps** (±13.1) | `-18.4 bps` | `-0.019 / +0.035` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,133.94 | ⚪ **CASH** | **-61.9 bps** (±17.4) | `-84.1 bps` | `-0.131 / -0.175` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.12 | ⚪ **CASH** | **-7.7 bps** (±11.3) | `-25.4 bps` | `+0.059 / +0.130` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 05:15:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,597.92 | ⚪ **CASH** | **-11.7 bps** (±13.1) | `-18.4 bps` | `-0.019 / +0.035` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,138.01 | ⚪ **CASH** | **-61.9 bps** (±17.4) | `-84.1 bps` | `-0.131 / -0.175` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.16 | ⚪ **CASH** | **-7.7 bps** (±11.3) | `-25.4 bps` | `+0.059 / +0.130` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 05:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,780.32 | ⚪ **CASH** | **-11.7 bps** (±13.1) | `-18.4 bps` | `-0.019 / +0.035` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,137.97 | ⚪ **CASH** | **-61.9 bps** (±17.4) | `-84.1 bps` | `-0.131 / -0.175` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.34 | ⚪ **CASH** | **-7.7 bps** (±11.3) | `-25.4 bps` | `+0.059 / +0.130` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 04:45:35 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,974.00 | ⚪ **CASH** | **-10.3 bps** (±8.9) | `-17.2 bps` | `-0.021 / +0.051` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,141.08 | ⚪ **CASH** | **-55.6 bps** (±12.9) | `-81.3 bps` | `-0.117 / -0.076` | `0.78%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.55 | ⚪ **CASH** | **-1.5 bps** (±10.9) | `-12.0 bps` | `+0.053 / +0.107` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 04:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,964.00 | ⚪ **CASH** | **-10.3 bps** (±8.9) | `-17.2 bps` | `-0.021 / +0.051` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,141.53 | ⚪ **CASH** | **-55.6 bps** (±12.9) | `-81.3 bps` | `-0.117 / -0.076` | `0.78%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.46 | ⚪ **CASH** | **-1.5 bps** (±10.9) | `-12.0 bps` | `+0.053 / +0.107` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 04:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,003.53 | ⚪ **CASH** | **-10.3 bps** (±8.9) | `-17.2 bps` | `-0.021 / +0.051` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,145.01 | ⚪ **CASH** | **-55.6 bps** (±12.9) | `-81.3 bps` | `-0.117 / -0.076` | `0.78%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.68 | ⚪ **CASH** | **-1.5 bps** (±10.9) | `-12.0 bps` | `+0.053 / +0.107` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 04:00:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,876.81 | ⚪ **CASH** | **-10.3 bps** (±8.9) | `-17.2 bps` | `-0.021 / +0.051` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,142.27 | ⚪ **CASH** | **-55.6 bps** (±12.9) | `-81.3 bps` | `-0.117 / -0.076` | `0.78%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.58 | ⚪ **CASH** | **-1.5 bps** (±10.9) | `-12.0 bps` | `+0.053 / +0.107` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 03:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,043.45 | ⚪ **CASH** | **-18.1 bps** (±6.6) | `-28.4 bps` | `-0.016 / -0.015` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,145.00 | ⚪ **CASH** | **-41.8 bps** (±23.7) | `-51.7 bps` | `-0.112 / -0.126` | `0.79%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.77 | ⚪ **CASH** | **-3.4 bps** (±7.3) | `-10.7 bps` | `+0.049 / +0.029` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 03:30:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,046.01 | ⚪ **CASH** | **-18.1 bps** (±6.6) | `-28.4 bps` | `-0.016 / -0.015` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,143.73 | ⚪ **CASH** | **-41.8 bps** (±23.7) | `-51.7 bps` | `-0.112 / -0.126` | `0.79%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.78 | ⚪ **CASH** | **-3.4 bps** (±7.3) | `-10.7 bps` | `+0.049 / +0.029` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 03:15:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,918.72 | ⚪ **CASH** | **-18.1 bps** (±6.6) | `-28.4 bps` | `-0.016 / -0.015` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,136.80 | ⚪ **CASH** | **-41.8 bps** (±23.7) | `-51.7 bps` | `-0.112 / -0.126` | `0.79%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.24 | ⚪ **CASH** | **-3.4 bps** (±7.3) | `-10.7 bps` | `+0.049 / +0.029` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 03:00:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,282.01 | ⚪ **CASH** | **-18.1 bps** (±6.6) | `-28.4 bps` | `-0.016 / -0.015` | `0.41%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,147.72 | ⚪ **CASH** | **-41.8 bps** (±23.7) | `-51.7 bps` | `-0.112 / -0.126` | `0.79%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $88.08 | ⚪ **CASH** | **-3.4 bps** (±7.3) | `-10.7 bps` | `+0.049 / +0.029` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 02:45:34 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,449.53 | ⚪ **CASH** | **-19.5 bps** (±6.5) | `-28.3 bps` | `-0.025 / -0.033` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,155.77 | ⚪ **CASH** | **-46.4 bps** (±18.1) | `-59.2 bps` | `-0.118 / -0.138` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $88.33 | ⚪ **CASH** | **-5.8 bps** (±8.0) | `-14.0 bps` | `+0.045 / +0.028` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 02:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,512.01 | ⚪ **CASH** | **-19.5 bps** (±6.5) | `-28.3 bps` | `-0.025 / -0.033` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,155.20 | ⚪ **CASH** | **-46.4 bps** (±18.1) | `-59.2 bps` | `-0.118 / -0.138` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $88.24 | ⚪ **CASH** | **-5.8 bps** (±8.0) | `-14.0 bps` | `+0.045 / +0.028` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 02:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,216.01 | ⚪ **CASH** | **-19.5 bps** (±6.5) | `-28.3 bps` | `-0.025 / -0.033` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,144.81 | ⚪ **CASH** | **-46.4 bps** (±18.1) | `-59.2 bps` | `-0.118 / -0.138` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.88 | ⚪ **CASH** | **-5.8 bps** (±8.0) | `-14.0 bps` | `+0.045 / +0.028` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 02:00:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,137.43 | ⚪ **CASH** | **-19.5 bps** (±6.5) | `-28.3 bps` | `-0.025 / -0.033` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,141.12 | ⚪ **CASH** | **-46.4 bps** (±18.1) | `-59.2 bps` | `-0.118 / -0.138` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.73 | ⚪ **CASH** | **-5.8 bps** (±8.0) | `-14.0 bps` | `+0.045 / +0.028` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 01:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,196.01 | ⚪ **CASH** | **-20.6 bps** (±7.1) | `-31.1 bps` | `-0.016 / -0.042` | `0.43%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,143.39 | ⚪ **CASH** | **-32.1 bps** (±22.1) | `-35.4 bps` | `-0.104 / -0.121` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.97 | ⚪ **CASH** | **-5.5 bps** (±6.8) | `-13.0 bps` | `+0.040 / +0.018` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 01:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,797.51 | ⚪ **CASH** | **-20.6 bps** (±7.1) | `-31.1 bps` | `-0.016 / -0.042` | `0.43%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,127.41 | ⚪ **CASH** | **-32.1 bps** (±22.1) | `-35.4 bps` | `-0.104 / -0.121` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.07 | ⚪ **CASH** | **-5.5 bps** (±6.8) | `-13.0 bps` | `+0.040 / +0.018` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 01:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,089.39 | ⚪ **CASH** | **-20.6 bps** (±7.1) | `-31.1 bps` | `-0.016 / -0.042` | `0.43%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,134.50 | ⚪ **CASH** | **-32.1 bps** (±22.1) | `-35.4 bps` | `-0.104 / -0.121` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.34 | ⚪ **CASH** | **-5.5 bps** (±6.8) | `-13.0 bps` | `+0.040 / +0.018` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 01:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,275.37 | ⚪ **CASH** | **-20.6 bps** (±7.1) | `-31.1 bps` | `-0.016 / -0.042` | `0.43%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,145.14 | ⚪ **CASH** | **-32.1 bps** (±22.1) | `-35.4 bps` | `-0.104 / -0.121` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.66 | ⚪ **CASH** | **-5.5 bps** (±6.8) | `-13.0 bps` | `+0.040 / +0.018` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 00:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,039.42 | ⚪ **CASH** | **-22.5 bps** (±11.2) | `-33.5 bps` | `-0.020 / -0.039` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,138.22 | ⚪ **CASH** | **-36.7 bps** (±26.2) | `-44.4 bps` | `-0.094 / -0.112` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.08 | ⚪ **CASH** | **-11.7 bps** (±14.9) | `-22.4 bps` | `+0.034 / +0.022` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 00:30:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,008.01 | ⚪ **CASH** | **-22.5 bps** (±11.2) | `-33.5 bps` | `-0.020 / -0.039` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,141.09 | ⚪ **CASH** | **-36.7 bps** (±26.2) | `-44.4 bps` | `-0.094 / -0.112` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.05 | ⚪ **CASH** | **-11.7 bps** (±14.9) | `-22.4 bps` | `+0.034 / +0.022` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 00:15:35 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,020.00 | ⚪ **CASH** | **-22.5 bps** (±11.2) | `-33.5 bps` | `-0.020 / -0.039` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,140.22 | ⚪ **CASH** | **-36.7 bps** (±26.2) | `-44.4 bps` | `-0.094 / -0.112` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.29 | ⚪ **CASH** | **-11.7 bps** (±14.9) | `-22.4 bps` | `+0.034 / +0.022` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 00:00:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,820.18 | ⚪ **CASH** | **-22.5 bps** (±11.2) | `-33.5 bps` | `-0.020 / -0.039` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,126.59 | ⚪ **CASH** | **-36.7 bps** (±26.2) | `-44.4 bps` | `-0.094 / -0.112` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.55 | ⚪ **CASH** | **-11.7 bps** (±14.9) | `-22.4 bps` | `+0.034 / +0.022` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 23:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,992.64 | ⚪ **CASH** | **-29.2 bps** (±5.4) | `-42.3 bps` | `-0.030 / -0.081` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,134.19 | ⚪ **CASH** | **-42.5 bps** (±27.1) | `-53.5 bps` | `-0.094 / -0.124` | `0.82%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.77 | ⚪ **CASH** | **-24.3 bps** (±8.8) | `-40.9 bps` | `+0.007 / -0.014` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 23:30:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,434.45 | ⚪ **CASH** | **-29.2 bps** (±5.4) | `-42.3 bps` | `-0.030 / -0.081` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,152.44 | ⚪ **CASH** | **-42.5 bps** (±27.1) | `-53.5 bps` | `-0.094 / -0.124` | `0.82%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.47 | ⚪ **CASH** | **-24.3 bps** (±8.8) | `-40.9 bps` | `+0.007 / -0.014` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 23:15:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,384.05 | ⚪ **CASH** | **-29.2 bps** (±5.4) | `-42.3 bps` | `-0.030 / -0.081` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,157.97 | ⚪ **CASH** | **-42.5 bps** (±27.1) | `-53.5 bps` | `-0.094 / -0.124` | `0.82%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.88 | ⚪ **CASH** | **-24.3 bps** (±8.8) | `-40.9 bps` | `+0.007 / -0.014` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 23:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,787.56 | ⚪ **CASH** | **-29.2 bps** (±5.4) | `-42.3 bps` | `-0.030 / -0.081` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,135.32 | ⚪ **CASH** | **-42.5 bps** (±27.1) | `-53.5 bps` | `-0.094 / -0.124` | `0.82%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.76 | ⚪ **CASH** | **-24.3 bps** (±8.8) | `-40.9 bps` | `+0.007 / -0.014` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 22:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,290.00 | ⚪ **CASH** | **-53.3 bps** (±14.4) | `-75.6 bps` | `-0.050 / -0.174` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,123.03 | ⚪ **CASH** | **-60.8 bps** (±19.6) | `-77.3 bps` | `-0.140 / -0.205` | `0.83%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.87 | ⚪ **CASH** | **-15.1 bps** (±11.4) | `-20.2 bps` | `+0.000 / -0.044` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 22:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,344.84 | ⚪ **CASH** | **-53.3 bps** (±14.4) | `-75.6 bps` | `-0.050 / -0.174` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,121.98 | ⚪ **CASH** | **-60.8 bps** (±19.6) | `-77.3 bps` | `-0.140 / -0.205` | `0.83%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.95 | ⚪ **CASH** | **-15.1 bps** (±11.4) | `-20.2 bps` | `+0.000 / -0.044` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 22:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,602.43 | ⚪ **CASH** | **-53.3 bps** (±14.4) | `-75.6 bps` | `-0.050 / -0.174` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,134.98 | ⚪ **CASH** | **-60.8 bps** (±19.6) | `-77.3 bps` | `-0.140 / -0.205` | `0.83%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.86 | ⚪ **CASH** | **-15.1 bps** (±11.4) | `-20.2 bps` | `+0.000 / -0.044` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 22:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,261.37 | ⚪ **CASH** | **-53.3 bps** (±14.4) | `-75.6 bps` | `-0.050 / -0.174` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,130.95 | ⚪ **CASH** | **-60.8 bps** (±19.6) | `-77.3 bps` | `-0.140 / -0.205` | `0.83%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.31 | ⚪ **CASH** | **-15.1 bps** (±11.4) | `-20.2 bps` | `+0.000 / -0.044` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 21:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,424.07 | ⚪ **CASH** | **+21.6 bps** (±8.3) | `+51.4 bps` | `+0.006 / -0.175` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,218.28 | ⚪ **CASH** | **+9.8 bps** (±7.8) | `+31.8 bps` | `-0.032 / -0.148` | `0.21%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $88.60 | ⚪ **CASH** | **+26.4 bps** (±13.9) | `+35.5 bps` | `+0.071 / +0.118` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 21:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,701.54 | ⚪ **CASH** | **+21.6 bps** (±8.3) | `+51.4 bps` | `+0.006 / -0.175` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,224.79 | ⚪ **CASH** | **+9.8 bps** (±7.8) | `+31.8 bps` | `-0.032 / -0.148` | `0.21%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.04 | ⚪ **CASH** | **+26.4 bps** (±13.9) | `+35.5 bps` | `+0.071 / +0.118` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
