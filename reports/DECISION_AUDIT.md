# 📋 BOT_TRADE V5 — Livro de Auditoria de Decisões e Análise de Mercado

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o consenso dos 5 modelos XGBoost, o comportamento do CVD (Cumulative Volume Delta) e o disparo de travas de risco.

**Última Atualização**: `2026-10-09 01:02:10 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-09 01:02:10 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,825.98 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.157` | `0.45%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,476.80 | ⚪ **CASH** | **-3.1 bps** (±0.4) | `[-3.4, -2.7, -2.4, -3.0, -3.0]` | `-0.070` | `0.74%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $109.39 | ⚪ **CASH** | **-1.7 bps** (±0.3) | `[-1.4, -2.2, -1.3, -1.3, -1.5]` | `-0.036` | `0.80%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-09 00:47:16 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,862.67 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.3, +0.5, +0.3]` | `+0.193` | `0.46%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,481.54 | ⚪ **CASH** | **-2.2 bps** (±0.4) | `[-2.7, -1.8, -1.5, -2.1, -2.1]` | `+0.013` | `0.75%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $109.35 | ⚪ **CASH** | **-1.8 bps** (±0.3) | `[-1.4, -2.2, -1.7, -1.3, -1.5]` | `+0.009` | `0.81%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-09 00:32:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,830.01 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.3, +0.5, +0.3]` | `+0.193` | `0.46%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,480.29 | ⚪ **CASH** | **-2.2 bps** (±0.4) | `[-2.7, -1.8, -1.5, -2.1, -2.1]` | `+0.013` | `0.75%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $109.05 | ⚪ **CASH** | **-1.8 bps** (±0.3) | `[-1.4, -2.2, -1.7, -1.3, -1.5]` | `+0.009` | `0.81%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-09 00:16:48 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,812.00 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.3, +0.5, +0.3]` | `+0.193` | `0.46%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,479.28 | ⚪ **CASH** | **-2.2 bps** (±0.4) | `[-2.7, -1.8, -1.5, -2.1, -2.1]` | `+0.013` | `0.75%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $109.51 | ⚪ **CASH** | **-1.8 bps** (±0.3) | `[-1.4, -2.2, -1.7, -1.3, -1.5]` | `+0.009` | `0.81%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-09 00:02:15 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,775.19 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.3, +0.5, +0.3]` | `+0.193` | `0.46%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,476.81 | ⚪ **CASH** | **-2.2 bps** (±0.4) | `[-2.7, -1.8, -1.5, -2.1, -2.1]` | `+0.013` | `0.75%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $109.43 | ⚪ **CASH** | **-1.8 bps** (±0.3) | `[-1.4, -2.2, -1.7, -1.3, -1.5]` | `+0.009` | `0.81%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 23:47:00 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,751.35 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.092` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,474.11 | ⚪ **CASH** | **-3.0 bps** (±0.3) | `[-3.4, -2.7, -2.4, -3.0, -2.9]` | `+0.019` | `0.76%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $109.93 | ⚪ **CASH** | **-1.7 bps** (±0.4) | `[-1.4, -2.2, -1.1, -1.5, -1.7]` | `-0.027` | `0.82%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 23:32:03 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,874.00 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.092` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,479.22 | ⚪ **CASH** | **-3.0 bps** (±0.3) | `[-3.4, -2.7, -2.4, -3.0, -2.9]` | `+0.019` | `0.76%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $110.40 | ⚪ **CASH** | **-1.7 bps** (±0.4) | `[-1.4, -2.2, -1.1, -1.5, -1.7]` | `-0.027` | `0.82%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 23:16:55 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,842.90 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.092` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,476.10 | ⚪ **CASH** | **-3.0 bps** (±0.3) | `[-3.4, -2.7, -2.4, -3.0, -2.9]` | `+0.019` | `0.76%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $110.30 | ⚪ **CASH** | **-1.7 bps** (±0.4) | `[-1.4, -2.2, -1.1, -1.5, -1.7]` | `-0.027` | `0.82%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 23:02:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,927.74 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.092` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,477.89 | ⚪ **CASH** | **-3.0 bps** (±0.3) | `[-3.4, -2.7, -2.4, -3.0, -2.9]` | `+0.019` | `0.76%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $110.40 | ⚪ **CASH** | **-1.7 bps** (±0.4) | `[-1.4, -2.2, -1.1, -1.5, -1.7]` | `-0.027` | `0.82%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 22:46:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,940.00 | ⚪ **CASH** | **+0.4 bps** (±0.1) | `[+0.3, +0.5, +0.3, +0.5, +0.3]` | `+0.013` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,476.50 | ⚪ **CASH** | **-2.3 bps** (±0.1) | `[-2.4, -2.3, -2.1, -2.4, -2.3]` | `+0.020` | `0.77%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $110.52 | ⚪ **CASH** | **-1.7 bps** (±0.4) | `[-1.4, -2.2, -1.1, -1.5, -1.7]` | `-0.013` | `0.83%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 22:32:00 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,770.00 | ⚪ **CASH** | **+0.4 bps** (±0.1) | `[+0.3, +0.5, +0.3, +0.5, +0.3]` | `+0.013` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,473.16 | ⚪ **CASH** | **-2.3 bps** (±0.1) | `[-2.4, -2.3, -2.1, -2.4, -2.3]` | `+0.020` | `0.77%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $110.14 | ⚪ **CASH** | **-1.7 bps** (±0.4) | `[-1.4, -2.2, -1.1, -1.5, -1.7]` | `-0.013` | `0.83%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 22:17:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,844.01 | ⚪ **CASH** | **+0.4 bps** (±0.1) | `[+0.3, +0.5, +0.3, +0.5, +0.3]` | `+0.013` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,478.83 | ⚪ **CASH** | **-2.3 bps** (±0.1) | `[-2.4, -2.3, -2.1, -2.4, -2.3]` | `+0.020` | `0.77%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $110.56 | ⚪ **CASH** | **-1.7 bps** (±0.4) | `[-1.4, -2.2, -1.1, -1.5, -1.7]` | `-0.013` | `0.83%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 22:02:18 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,735.11 | ⚪ **CASH** | **+0.4 bps** (±0.1) | `[+0.3, +0.5, +0.3, +0.5, +0.3]` | `+0.013` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,480.21 | ⚪ **CASH** | **-2.3 bps** (±0.1) | `[-2.4, -2.3, -2.1, -2.4, -2.3]` | `+0.020` | `0.77%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $110.70 | ⚪ **CASH** | **-1.7 bps** (±0.4) | `[-1.4, -2.2, -1.1, -1.5, -1.7]` | `-0.013` | `0.83%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 21:47:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,634.65 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.1, +0.0, +0.2, +0.1, +0.2]` | `-0.071` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,471.99 | ⚪ **CASH** | **-2.9 bps** (±0.8) | `[-4.0, -1.7, -2.2, -2.0, -2.7]` | `+0.003` | `0.78%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $110.03 | ⚪ **CASH** | **-1.5 bps** (±1.2) | `[-1.6, -1.1, +1.5, -1.5, -1.7]` | `-0.035` | `0.83%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 21:31:53 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,686.01 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.1, +0.0, +0.2, +0.1, +0.2]` | `-0.071` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,474.75 | ⚪ **CASH** | **-2.9 bps** (±0.8) | `[-4.0, -1.7, -2.2, -2.0, -2.7]` | `+0.003` | `0.78%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $110.00 | ⚪ **CASH** | **-1.5 bps** (±1.2) | `[-1.6, -1.1, +1.5, -1.5, -1.7]` | `-0.035` | `0.83%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 21:17:03 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,736.01 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.1, +0.0, +0.2, +0.1, +0.2]` | `-0.071` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,473.35 | ⚪ **CASH** | **-2.9 bps** (±0.8) | `[-4.0, -1.7, -2.2, -2.0, -2.7]` | `+0.003` | `0.78%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $109.99 | ⚪ **CASH** | **-1.5 bps** (±1.2) | `[-1.6, -1.1, +1.5, -1.5, -1.7]` | `-0.035` | `0.83%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 21:02:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,782.09 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.1, +0.0, +0.2, +0.1, +0.2]` | `-0.071` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,474.61 | ⚪ **CASH** | **-2.9 bps** (±0.8) | `[-4.0, -1.7, -2.2, -2.0, -2.7]` | `+0.003` | `0.78%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $109.88 | ⚪ **CASH** | **-1.5 bps** (±1.2) | `[-1.6, -1.1, +1.5, -1.5, -1.7]` | `-0.035` | `0.83%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 20:47:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,822.67 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.2, +0.0, +0.2, +0.1, +0.2]` | `-0.047` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,472.08 | ⚪ **CASH** | **-2.5 bps** (±0.4) | `[-2.5, -1.7, -2.3, -2.0, -2.9]` | `+0.028` | `0.79%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $109.70 | ⚪ **CASH** | **-1.7 bps** (±0.9) | `[-2.1, -1.3, +0.3, -1.6, -1.7]` | `-0.009` | `0.83%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 20:32:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,741.66 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.2, +0.0, +0.2, +0.1, +0.2]` | `-0.047` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,468.37 | ⚪ **CASH** | **-2.5 bps** (±0.4) | `[-2.5, -1.7, -2.3, -2.0, -2.9]` | `+0.028` | `0.79%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $109.35 | ⚪ **CASH** | **-1.7 bps** (±0.9) | `[-2.1, -1.3, +0.3, -1.6, -1.7]` | `-0.009` | `0.83%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 20:16:54 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,862.67 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.2, +0.0, +0.2, +0.1, +0.2]` | `-0.047` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,471.52 | ⚪ **CASH** | **-2.5 bps** (±0.4) | `[-2.5, -1.7, -2.3, -2.0, -2.9]` | `+0.028` | `0.79%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $109.60 | ⚪ **CASH** | **-1.7 bps** (±0.9) | `[-2.1, -1.3, +0.3, -1.6, -1.7]` | `-0.009` | `0.83%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 20:02:51 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,870.01 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.2, +0.0, +0.2, +0.1, +0.2]` | `-0.047` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,468.31 | ⚪ **CASH** | **-2.5 bps** (±0.4) | `[-2.5, -1.7, -2.3, -2.0, -2.9]` | `+0.028` | `0.79%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $109.26 | ⚪ **CASH** | **-1.7 bps** (±0.9) | `[-2.1, -1.3, +0.3, -1.6, -1.7]` | `-0.009` | `0.83%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 19:47:00 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,730.00 | ⚪ **CASH** | **-0.6 bps** (±0.0) | `[-0.5, -0.6, -0.6, -0.6, -0.6]` | `-0.064` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,461.34 | ⚪ **CASH** | **-2.5 bps** (±0.3) | `[-2.7, -2.5, -1.9, -2.1, -2.7]` | `+0.030` | `0.78%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $109.07 | ⚪ **CASH** | **-1.0 bps** (±0.8) | `[+0.4, -0.8, -0.2, -0.4, -2.0]` | `-0.002` | `0.81%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 19:32:00 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,772.01 | ⚪ **CASH** | **-0.6 bps** (±0.0) | `[-0.5, -0.6, -0.6, -0.6, -0.6]` | `-0.064` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,459.87 | ⚪ **CASH** | **-2.5 bps** (±0.3) | `[-2.7, -2.5, -1.9, -2.1, -2.7]` | `+0.030` | `0.78%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $109.07 | ⚪ **CASH** | **-1.0 bps** (±0.8) | `[+0.4, -0.8, -0.2, -0.4, -2.0]` | `-0.002` | `0.81%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 19:17:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,574.01 | ⚪ **CASH** | **-0.6 bps** (±0.0) | `[-0.5, -0.6, -0.6, -0.6, -0.6]` | `-0.064` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,453.57 | ⚪ **CASH** | **-2.5 bps** (±0.3) | `[-2.7, -2.5, -1.9, -2.1, -2.7]` | `+0.030` | `0.78%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $108.82 | ⚪ **CASH** | **-1.0 bps** (±0.8) | `[+0.4, -0.8, -0.2, -0.4, -2.0]` | `-0.002` | `0.81%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 19:02:40 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,581.98 | ⚪ **CASH** | **-0.6 bps** (±0.0) | `[-0.5, -0.6, -0.6, -0.6, -0.6]` | `-0.064` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,452.00 | ⚪ **CASH** | **-2.5 bps** (±0.3) | `[-2.7, -2.5, -1.9, -2.1, -2.7]` | `+0.030` | `0.78%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $108.40 | ⚪ **CASH** | **-1.0 bps** (±0.8) | `[+0.4, -0.8, -0.2, -0.4, -2.0]` | `-0.002` | `0.81%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 18:47:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,496.00 | ⚪ **CASH** | **-2.2 bps** (±1.0) | `[-2.5, -1.9, -1.1, -0.2, -2.9]` | `-0.098` | `0.45%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,445.19 | ⚪ **CASH** | **-6.8 bps** (±2.0) | `[-8.0, -7.0, -4.6, -6.9, -2.6]` | `-0.006` | `0.75%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $107.87 | ⚪ **CASH** | **+3.4 bps** (±3.1) | `[+8.0, -0.7, +7.3, +4.9, +5.2]` | `-0.004` | `0.75%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 18:32:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,374.46 | ⚪ **CASH** | **-2.2 bps** (±1.0) | `[-2.5, -1.9, -1.1, -0.2, -2.9]` | `-0.098` | `0.45%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,438.13 | ⚪ **CASH** | **-6.8 bps** (±2.0) | `[-8.0, -7.0, -4.6, -6.9, -2.6]` | `-0.006` | `0.75%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $107.63 | ⚪ **CASH** | **+3.4 bps** (±3.1) | `[+8.0, -0.7, +7.3, +4.9, +5.2]` | `-0.004` | `0.75%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 18:17:21 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,006.93 | ⚪ **CASH** | **-2.2 bps** (±1.0) | `[-2.5, -1.9, -1.1, -0.2, -2.9]` | `-0.098` | `0.45%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,425.99 | ⚪ **CASH** | **-6.8 bps** (±2.0) | `[-8.0, -7.0, -4.6, -6.9, -2.6]` | `-0.006` | `0.75%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.93 | ⚪ **CASH** | **+3.4 bps** (±3.1) | `[+8.0, -0.7, +7.3, +4.9, +5.2]` | `-0.004` | `0.75%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 18:02:47 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,766.07 | ⚪ **CASH** | **-2.2 bps** (±1.0) | `[-2.5, -1.9, -1.1, -0.2, -2.9]` | `-0.098` | `0.45%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,419.44 | ⚪ **CASH** | **-6.8 bps** (±2.0) | `[-8.0, -7.0, -4.6, -6.9, -2.6]` | `-0.006` | `0.75%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.78 | ⚪ **CASH** | **+3.4 bps** (±3.1) | `[+8.0, -0.7, +7.3, +4.9, +5.2]` | `-0.004` | `0.75%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 17:47:03 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,790.07 | ⚪ **CASH** | **-2.2 bps** (±1.2) | `[-2.2, -1.8, -2.6, +0.6, -2.3]` | `-0.077` | `0.46%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,420.18 | ⚪ **CASH** | **-8.5 bps** (±2.4) | `[-5.8, -11.6, -6.8, -7.6, -4.5]` | `-0.034` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.39 | ⚪ **CASH** | **+0.3 bps** (±2.4) | `[+5.5, +2.2, -1.0, -1.1, +2.0]` | `+0.027` | `0.74%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 17:32:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,868.68 | ⚪ **CASH** | **-2.2 bps** (±1.2) | `[-2.2, -1.8, -2.6, +0.6, -2.3]` | `-0.077` | `0.46%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,422.06 | ⚪ **CASH** | **-8.5 bps** (±2.4) | `[-5.8, -11.6, -6.8, -7.6, -4.5]` | `-0.034` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.86 | ⚪ **CASH** | **+0.3 bps** (±2.4) | `[+5.5, +2.2, -1.0, -1.1, +2.0]` | `+0.027` | `0.74%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 17:17:02 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,800.00 | ⚪ **CASH** | **-2.2 bps** (±1.2) | `[-2.2, -1.8, -2.6, +0.6, -2.3]` | `-0.077` | `0.46%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,421.39 | ⚪ **CASH** | **-8.5 bps** (±2.4) | `[-5.8, -11.6, -6.8, -7.6, -4.5]` | `-0.034` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $107.38 | ⚪ **CASH** | **+0.3 bps** (±2.4) | `[+5.5, +2.2, -1.0, -1.1, +2.0]` | `+0.027` | `0.74%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 17:02:34 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,808.92 | ⚪ **CASH** | **-2.2 bps** (±1.2) | `[-2.2, -1.8, -2.6, +0.6, -2.3]` | `-0.077` | `0.46%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,415.59 | ⚪ **CASH** | **-8.5 bps** (±2.4) | `[-5.8, -11.6, -6.8, -7.6, -4.5]` | `-0.034` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $107.61 | ⚪ **CASH** | **+0.3 bps** (±2.4) | `[+5.5, +2.2, -1.0, -1.1, +2.0]` | `+0.027` | `0.74%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 16:46:58 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,339.22 | ⚪ **CASH** | **-5.2 bps** (±1.9) | `[-2.0, -5.4, -6.3, -1.9, -5.8]` | `-0.070` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,430.40 | ⚪ **CASH** | **-15.4 bps** (±6.2) | `[-20.7, -17.7, -4.3, -6.9, -12.0]` | `-0.055` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $108.67 | ⚪ **CASH** | **+4.1 bps** (±3.4) | `[+2.8, +0.9, +9.7, +8.4, +7.2]` | `-0.008` | `0.74%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 16:32:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,166.62 | ⚪ **CASH** | **-5.2 bps** (±1.9) | `[-2.0, -5.4, -6.3, -1.9, -5.8]` | `-0.070` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,424.38 | ⚪ **CASH** | **-15.4 bps** (±6.2) | `[-20.7, -17.7, -4.3, -6.9, -12.0]` | `-0.055` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $108.46 | ⚪ **CASH** | **+4.1 bps** (±3.4) | `[+2.8, +0.9, +9.7, +8.4, +7.2]` | `-0.008` | `0.74%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-08 16:17:03 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,961.31 | ⚪ **CASH** | **-5.2 bps** (±1.9) | `[-2.0, -5.4, -6.3, -1.9, -5.8]` | `-0.070` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,421.04 | ⚪ **CASH** | **-15.4 bps** (±6.2) | `[-20.7, -17.7, -4.3, -6.9, -12.0]` | `-0.055` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $108.11 | ⚪ **CASH** | **+4.1 bps** (±3.4) | `[+2.8, +0.9, +9.7, +8.4, +7.2]` | `-0.008` | `0.74%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
