# 📋 BOT_TRADE V5 — Livro de Auditoria de Decisões e Análise de Mercado

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o consenso dos 5 modelos XGBoost, o comportamento do CVD (Cumulative Volume Delta) e o disparo de travas de risco.

**Última Atualização**: `2026-09-10 13:17:51 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-09-10 13:17:51 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,858.31 | ⚪ **CASH** | **+0.7 bps** (±0.7) | `[+0.9, +0.3, +0.8, +0.9, +2.3]` | `-0.337` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,415.42 | ⚪ **CASH** | **+0.7 bps** (±0.4) | `[+0.5, +1.4, +0.6, +0.7, +1.4]` | `-0.168` | `0.50%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $99.21 | ⚪ **CASH** | **-0.0 bps** (±0.9) | `[+0.2, +0.2, +1.5, -1.1, +1.3]` | `-0.118` | `0.59%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 13:02:28 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,025.93 | ⚪ **CASH** | **+0.7 bps** (±0.7) | `[+0.9, +0.3, +0.8, +0.9, +2.3]` | `-0.337` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,422.53 | ⚪ **CASH** | **+0.7 bps** (±0.4) | `[+0.5, +1.4, +0.6, +0.7, +1.4]` | `-0.168` | `0.50%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $99.28 | ⚪ **CASH** | **-0.0 bps** (±0.9) | `[+0.2, +0.2, +1.5, -1.1, +1.3]` | `-0.118` | `0.59%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 12:48:26 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,956.00 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.259` | `0.31%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,424.70 | ⚪ **CASH** | **-1.7 bps** (±0.5) | `[-1.5, -1.0, -0.8, -2.2, -1.6]` | `-0.125` | `0.38%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $99.29 | ⚪ **CASH** | **-2.9 bps** (±0.4) | `[-3.2, -2.9, -2.0, -2.7, -2.3]` | `-0.180` | `0.49%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 12:32:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,580.00 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.259` | `0.31%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,451.00 | ⚪ **CASH** | **-1.7 bps** (±0.5) | `[-1.5, -1.0, -0.8, -2.2, -1.6]` | `-0.125` | `0.38%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $100.97 | ⚪ **CASH** | **-2.9 bps** (±0.4) | `[-3.2, -2.9, -2.0, -2.7, -2.3]` | `-0.180` | `0.49%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 12:17:45 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,763.05 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.259` | `0.31%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,458.94 | ⚪ **CASH** | **-1.7 bps** (±0.5) | `[-1.5, -1.0, -0.8, -2.2, -1.6]` | `-0.125` | `0.38%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.07 | ⚪ **CASH** | **-2.9 bps** (±0.4) | `[-3.2, -2.9, -2.0, -2.7, -2.3]` | `-0.180` | `0.49%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 12:02:18 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,862.01 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.259` | `0.31%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,462.44 | ⚪ **CASH** | **-1.7 bps** (±0.5) | `[-1.5, -1.0, -0.8, -2.2, -1.6]` | `-0.125` | `0.38%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.21 | ⚪ **CASH** | **-2.9 bps** (±0.4) | `[-3.2, -2.9, -2.0, -2.7, -2.3]` | `-0.180` | `0.49%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 11:47:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,967.27 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.3, +0.1, +0.0, +0.0, -0.1]` | `-0.191` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,466.24 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-0.4, -0.9, -0.4, -1.0, -1.4]` | `-0.105` | `0.38%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.28 | ⚪ **CASH** | **-2.9 bps** (±0.4) | `[-3.2, -2.9, -2.0, -2.7, -2.3]` | `-0.185` | `0.49%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 11:32:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,012.82 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.3, +0.1, +0.0, +0.0, -0.1]` | `-0.191` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,468.42 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-0.4, -0.9, -0.4, -1.0, -1.4]` | `-0.105` | `0.38%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.44 | ⚪ **CASH** | **-2.9 bps** (±0.4) | `[-3.2, -2.9, -2.0, -2.7, -2.3]` | `-0.185` | `0.49%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 11:17:15 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,977.51 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.3, +0.1, +0.0, +0.0, -0.1]` | `-0.191` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,465.28 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-0.4, -0.9, -0.4, -1.0, -1.4]` | `-0.105` | `0.38%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.20 | ⚪ **CASH** | **-2.9 bps** (±0.4) | `[-3.2, -2.9, -2.0, -2.7, -2.3]` | `-0.185` | `0.49%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 11:02:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,823.43 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.3, +0.1, +0.0, +0.0, -0.1]` | `-0.191` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,461.81 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-0.4, -0.9, -0.4, -1.0, -1.4]` | `-0.105` | `0.38%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $100.98 | ⚪ **CASH** | **-2.9 bps** (±0.4) | `[-3.2, -2.9, -2.0, -2.7, -2.3]` | `-0.185` | `0.49%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 10:47:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,966.00 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.2, +0.1, +0.0, +0.0, -0.1]` | `-0.112` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,467.69 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-0.4, -0.9, -0.4, -1.0, -1.4]` | `-0.089` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.26 | ⚪ **CASH** | **-2.9 bps** (±0.5) | `[-3.5, -2.9, -2.0, -2.7, -2.3]` | `-0.183` | `0.50%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 10:32:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,922.01 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.2, +0.1, +0.0, +0.0, -0.1]` | `-0.112` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,465.90 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-0.4, -0.9, -0.4, -1.0, -1.4]` | `-0.089` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.01 | ⚪ **CASH** | **-2.9 bps** (±0.5) | `[-3.5, -2.9, -2.0, -2.7, -2.3]` | `-0.183` | `0.50%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 10:17:03 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,990.01 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.2, +0.1, +0.0, +0.0, -0.1]` | `-0.112` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,470.10 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-0.4, -0.9, -0.4, -1.0, -1.4]` | `-0.089` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.18 | ⚪ **CASH** | **-2.9 bps** (±0.5) | `[-3.5, -2.9, -2.0, -2.7, -2.3]` | `-0.183` | `0.50%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 10:02:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,962.02 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.2, +0.1, +0.0, +0.0, -0.1]` | `-0.112` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,467.93 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-0.4, -0.9, -0.4, -1.0, -1.4]` | `-0.089` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.08 | ⚪ **CASH** | **-2.9 bps** (±0.5) | `[-3.5, -2.9, -2.0, -2.7, -2.3]` | `-0.183` | `0.50%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 09:47:31 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,964.00 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `+0.011` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,468.28 | ⚪ **CASH** | **-1.3 bps** (±0.4) | `[-1.0, -0.7, -0.5, -1.7, -1.4]` | `-0.026` | `0.39%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.08 | ⚪ **CASH** | **-2.9 bps** (±0.5) | `[-3.5, -2.9, -2.0, -2.7, -2.3]` | `-0.166` | `0.51%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 09:32:07 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,092.20 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `+0.011` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,473.45 | ⚪ **CASH** | **-1.3 bps** (±0.4) | `[-1.0, -0.7, -0.5, -1.7, -1.4]` | `-0.026` | `0.39%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.14 | ⚪ **CASH** | **-2.9 bps** (±0.5) | `[-3.5, -2.9, -2.0, -2.7, -2.3]` | `-0.166` | `0.51%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 09:17:31 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,158.00 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `+0.011` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,474.89 | ⚪ **CASH** | **-1.3 bps** (±0.4) | `[-1.0, -0.7, -0.5, -1.7, -1.4]` | `-0.026` | `0.39%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.21 | ⚪ **CASH** | **-2.9 bps** (±0.5) | `[-3.5, -2.9, -2.0, -2.7, -2.3]` | `-0.166` | `0.51%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 09:02:17 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,132.41 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `+0.011` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,471.84 | ⚪ **CASH** | **-1.3 bps** (±0.4) | `[-1.0, -0.7, -0.5, -1.7, -1.4]` | `-0.026` | `0.39%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.18 | ⚪ **CASH** | **-2.9 bps** (±0.5) | `[-3.5, -2.9, -2.0, -2.7, -2.3]` | `-0.166` | `0.51%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 08:47:00 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,099.77 | ⚪ **CASH** | **+0.4 bps** (±0.1) | `[+0.2, +0.4, +0.5, +0.4, +0.5]` | `+0.001` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,471.38 | ⚪ **CASH** | **+0.2 bps** (±0.3) | `[+0.6, +0.1, +0.8, +0.2, +0.2]` | `+0.008` | `0.40%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.20 | ⚪ **CASH** | **-0.2 bps** (±0.5) | `[+0.6, +0.1, -0.9, +0.3, +0.3]` | `-0.131` | `0.51%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 08:32:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,114.01 | ⚪ **CASH** | **+0.4 bps** (±0.1) | `[+0.2, +0.4, +0.5, +0.4, +0.5]` | `+0.001` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,472.62 | ⚪ **CASH** | **+0.2 bps** (±0.3) | `[+0.6, +0.1, +0.8, +0.2, +0.2]` | `+0.008` | `0.40%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.23 | ⚪ **CASH** | **-0.2 bps** (±0.5) | `[+0.6, +0.1, -0.9, +0.3, +0.3]` | `-0.131` | `0.51%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 08:17:40 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,094.01 | ⚪ **CASH** | **+0.4 bps** (±0.1) | `[+0.2, +0.4, +0.5, +0.4, +0.5]` | `+0.001` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,470.99 | ⚪ **CASH** | **+0.2 bps** (±0.3) | `[+0.6, +0.1, +0.8, +0.2, +0.2]` | `+0.008` | `0.40%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.17 | ⚪ **CASH** | **-0.2 bps** (±0.5) | `[+0.6, +0.1, -0.9, +0.3, +0.3]` | `-0.131` | `0.51%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 08:02:31 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,114.63 | ⚪ **CASH** | **+0.4 bps** (±0.1) | `[+0.2, +0.4, +0.5, +0.4, +0.5]` | `+0.001` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,471.90 | ⚪ **CASH** | **+0.2 bps** (±0.3) | `[+0.6, +0.1, +0.8, +0.2, +0.2]` | `+0.008` | `0.40%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.21 | ⚪ **CASH** | **-0.2 bps** (±0.5) | `[+0.6, +0.1, -0.9, +0.3, +0.3]` | `-0.131` | `0.51%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 07:47:15 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,039.24 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.2, +0.1, +0.0, +0.0, -0.1]` | `-0.041` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,469.57 | ⚪ **CASH** | **+0.2 bps** (±0.3) | `[+0.3, +0.4, +0.8, +0.6, -0.2]` | `+0.033` | `0.40%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.17 | ⚪ **CASH** | **-2.1 bps** (±0.2) | `[-2.1, -2.3, -1.9, -1.6, -1.9]` | `-0.057` | `0.51%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 07:32:03 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,032.33 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.2, +0.1, +0.0, +0.0, -0.1]` | `-0.041` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,468.11 | ⚪ **CASH** | **+0.2 bps** (±0.3) | `[+0.3, +0.4, +0.8, +0.6, -0.2]` | `+0.033` | `0.40%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.09 | ⚪ **CASH** | **-2.1 bps** (±0.2) | `[-2.1, -2.3, -1.9, -1.6, -1.9]` | `-0.057` | `0.51%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 07:17:30 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,187.70 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.2, +0.1, +0.0, +0.0, -0.1]` | `-0.041` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,475.07 | ⚪ **CASH** | **+0.2 bps** (±0.3) | `[+0.3, +0.4, +0.8, +0.6, -0.2]` | `+0.033` | `0.40%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.60 | ⚪ **CASH** | **-2.1 bps** (±0.2) | `[-2.1, -2.3, -1.9, -1.6, -1.9]` | `-0.057` | `0.51%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 07:02:31 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,304.98 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.2, +0.1, +0.0, +0.0, -0.1]` | `-0.041` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,476.57 | ⚪ **CASH** | **+0.2 bps** (±0.3) | `[+0.3, +0.4, +0.8, +0.6, -0.2]` | `+0.033` | `0.40%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.70 | ⚪ **CASH** | **-2.1 bps** (±0.2) | `[-2.1, -2.3, -1.9, -1.6, -1.9]` | `-0.057` | `0.51%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 06:47:19 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,334.00 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.3, -0.4, -0.3]` | `-0.043` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,478.40 | ⚪ **CASH** | **-0.2 bps** (±0.3) | `[-0.4, -0.2, +0.3, +0.1, -0.1]` | `+0.018` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.86 | ⚪ **CASH** | **-2.0 bps** (±0.3) | `[-2.1, -2.3, -1.9, -1.6, -1.3]` | `-0.030` | `0.52%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 06:32:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,184.01 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.3, -0.4, -0.3]` | `-0.043` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,472.92 | ⚪ **CASH** | **-0.2 bps** (±0.3) | `[-0.4, -0.2, +0.3, +0.1, -0.1]` | `+0.018` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.68 | ⚪ **CASH** | **-2.0 bps** (±0.3) | `[-2.1, -2.3, -1.9, -1.6, -1.3]` | `-0.030` | `0.52%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 06:17:25 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,235.37 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.3, -0.4, -0.3]` | `-0.043` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,473.67 | ⚪ **CASH** | **-0.2 bps** (±0.3) | `[-0.4, -0.2, +0.3, +0.1, -0.1]` | `+0.018` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.54 | ⚪ **CASH** | **-2.0 bps** (±0.3) | `[-2.1, -2.3, -1.9, -1.6, -1.3]` | `-0.030` | `0.52%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 06:02:26 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,508.65 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.3, -0.4, -0.3]` | `-0.043` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,481.53 | ⚪ **CASH** | **-0.2 bps** (±0.3) | `[-0.4, -0.2, +0.3, +0.1, -0.1]` | `+0.018` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.01 | ⚪ **CASH** | **-2.0 bps** (±0.3) | `[-2.1, -2.3, -1.9, -1.6, -1.3]` | `-0.030` | `0.52%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 05:46:54 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,436.00 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.3, -0.4, -0.3]` | `-0.029` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,480.99 | ⚪ **CASH** | **-0.2 bps** (±0.3) | `[-0.4, -0.2, +0.3, +0.1, -0.1]` | `+0.015` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.07 | ⚪ **CASH** | **-2.4 bps** (±0.2) | `[-2.4, -2.6, -2.2, -2.0, -2.0]` | `-0.011` | `0.53%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 05:32:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,516.65 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.3, -0.4, -0.3]` | `-0.029` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,481.31 | ⚪ **CASH** | **-0.2 bps** (±0.3) | `[-0.4, -0.2, +0.3, +0.1, -0.1]` | `+0.015` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.07 | ⚪ **CASH** | **-2.4 bps** (±0.2) | `[-2.4, -2.6, -2.2, -2.0, -2.0]` | `-0.011` | `0.53%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 05:17:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,393.62 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.3, -0.4, -0.3]` | `-0.029` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,478.69 | ⚪ **CASH** | **-0.2 bps** (±0.3) | `[-0.4, -0.2, +0.3, +0.1, -0.1]` | `+0.015` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.99 | ⚪ **CASH** | **-2.4 bps** (±0.2) | `[-2.4, -2.6, -2.2, -2.0, -2.0]` | `-0.011` | `0.53%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 05:03:44 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,333.43 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.3, -0.4, -0.3]` | `-0.029` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,476.56 | ⚪ **CASH** | **-0.2 bps** (±0.3) | `[-0.4, -0.2, +0.3, +0.1, -0.1]` | `+0.015` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.83 | ⚪ **CASH** | **-2.4 bps** (±0.2) | `[-2.4, -2.6, -2.2, -2.0, -2.0]` | `-0.011` | `0.53%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 04:46:58 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,362.55 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.059` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,478.88 | ⚪ **CASH** | **-0.4 bps** (±0.3) | `[-0.4, -0.2, +0.4, -0.2, -0.6]` | `-0.116` | `0.42%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.03 | ⚪ **CASH** | **-2.1 bps** (±0.2) | `[-2.1, -2.3, -1.9, -1.6, -1.9]` | `-0.085` | `0.53%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-10 04:34:21 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,403.51 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.059` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,480.06 | ⚪ **CASH** | **-0.4 bps** (±0.3) | `[-0.4, -0.2, +0.4, -0.2, -0.6]` | `-0.116` | `0.42%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.14 | ⚪ **CASH** | **-2.1 bps** (±0.2) | `[-2.1, -2.3, -1.9, -1.6, -1.9]` | `-0.085` | `0.53%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |
