# 📋 BOT_TRADE V5 — Livro de Auditoria de Decisões e Análise de Mercado

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o consenso dos 5 modelos XGBoost, o comportamento do CVD (Cumulative Volume Delta) e o disparo de travas de risco.

**Última Atualização**: `2026-10-15 12:32:04 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-15 12:32:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,621.75 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.1, +0.0, +0.1, +0.1, +0.2]` | `+0.113` | `0.42%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,341.90 | ⚪ **CASH** | **-3.5 bps** (±0.7) | `[-4.4, -2.8, -2.4, -3.1, -3.2]` | `-0.178` | `0.58%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.65 | ⚪ **CASH** | **-1.9 bps** (±0.5) | `[-1.4, -2.6, -1.8, -1.3, -1.4]` | `+0.010` | `0.75%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 12:17:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,018.01 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.1, +0.0, +0.1, +0.1, +0.2]` | `+0.113` | `0.42%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,367.55 | ⚪ **CASH** | **-3.5 bps** (±0.7) | `[-4.4, -2.8, -2.4, -3.1, -3.2]` | `-0.178` | `0.58%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.28 | ⚪ **CASH** | **-1.9 bps** (±0.5) | `[-1.4, -2.6, -1.8, -1.3, -1.4]` | `+0.010` | `0.75%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 12:02:12 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,904.68 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.1, +0.0, +0.1, +0.1, +0.2]` | `+0.113` | `0.42%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,360.20 | ⚪ **CASH** | **-3.5 bps** (±0.7) | `[-4.4, -2.8, -2.4, -3.1, -3.2]` | `-0.178` | `0.58%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.03 | ⚪ **CASH** | **-1.9 bps** (±0.5) | `[-1.4, -2.6, -1.8, -1.3, -1.4]` | `+0.010` | `0.75%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 11:47:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,106.00 | ⚪ **CASH** | **+0.5 bps** (±0.1) | `[+0.4, +0.6, +0.4, +0.5, +0.6]` | `+0.003` | `0.42%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,367.93 | ⚪ **CASH** | **-2.2 bps** (±0.3) | `[-2.3, -1.4, -2.2, -2.1, -2.1]` | `-0.222` | `0.59%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.54 | ⚪ **CASH** | **+0.4 bps** (±0.4) | `[+1.2, +0.3, +0.1, +1.1, +0.6]` | `-0.036` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 11:32:03 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,130.00 | ⚪ **CASH** | **+0.5 bps** (±0.1) | `[+0.4, +0.6, +0.4, +0.5, +0.6]` | `+0.003` | `0.42%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,367.99 | ⚪ **CASH** | **-2.2 bps** (±0.3) | `[-2.3, -1.4, -2.2, -2.1, -2.1]` | `-0.222` | `0.59%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.50 | ⚪ **CASH** | **+0.4 bps** (±0.4) | `[+1.2, +0.3, +0.1, +1.1, +0.6]` | `-0.036` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 11:17:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,040.28 | ⚪ **CASH** | **+0.5 bps** (±0.1) | `[+0.4, +0.6, +0.4, +0.5, +0.6]` | `+0.003` | `0.42%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,366.13 | ⚪ **CASH** | **-2.2 bps** (±0.3) | `[-2.3, -1.4, -2.2, -2.1, -2.1]` | `-0.222` | `0.59%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.43 | ⚪ **CASH** | **+0.4 bps** (±0.4) | `[+1.2, +0.3, +0.1, +1.1, +0.6]` | `-0.036` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 11:02:10 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,962.01 | ⚪ **CASH** | **+0.5 bps** (±0.1) | `[+0.4, +0.6, +0.4, +0.5, +0.6]` | `+0.003` | `0.42%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,364.49 | ⚪ **CASH** | **-2.2 bps** (±0.3) | `[-2.3, -1.4, -2.2, -2.1, -2.1]` | `-0.222` | `0.59%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.20 | ⚪ **CASH** | **+0.4 bps** (±0.4) | `[+1.2, +0.3, +0.1, +1.1, +0.6]` | `-0.036` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 10:47:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,892.88 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.5, +0.5, +0.3]` | `+0.016` | `0.43%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,361.24 | ⚪ **CASH** | **-2.6 bps** (±0.5) | `[-3.2, -1.9, -1.9, -2.3, -2.6]` | `-0.183` | `0.60%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.07 | ⚪ **CASH** | **-1.7 bps** (±0.2) | `[-1.8, -1.8, -1.6, -1.6, -1.3]` | `+0.024` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 10:32:18 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,100.20 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.5, +0.5, +0.3]` | `+0.016` | `0.43%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,367.16 | ⚪ **CASH** | **-2.6 bps** (±0.5) | `[-3.2, -1.9, -1.9, -2.3, -2.6]` | `-0.183` | `0.60%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.27 | ⚪ **CASH** | **-1.7 bps** (±0.2) | `[-1.8, -1.8, -1.6, -1.6, -1.3]` | `+0.024` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 10:17:15 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,144.00 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.5, +0.5, +0.3]` | `+0.016` | `0.43%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,367.78 | ⚪ **CASH** | **-2.6 bps** (±0.5) | `[-3.2, -1.9, -1.9, -2.3, -2.6]` | `-0.183` | `0.60%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.38 | ⚪ **CASH** | **-1.7 bps** (±0.2) | `[-1.8, -1.8, -1.6, -1.6, -1.3]` | `+0.024` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 10:02:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,272.97 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.5, +0.5, +0.3]` | `+0.016` | `0.43%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,375.52 | ⚪ **CASH** | **-2.6 bps** (±0.5) | `[-3.2, -1.9, -1.9, -2.3, -2.6]` | `-0.183` | `0.60%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $103.20 | ⚪ **CASH** | **-1.7 bps** (±0.2) | `[-1.8, -1.8, -1.6, -1.6, -1.3]` | `+0.024` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 09:46:56 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,241.12 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.3, +0.5, +0.3]` | `+0.013` | `0.43%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,370.82 | ⚪ **CASH** | **-2.3 bps** (±0.6) | `[-3.0, -1.8, -2.0, -1.6, -1.4]` | `-0.201` | `0.61%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.86 | ⚪ **CASH** | **-1.6 bps** (±0.1) | `[-1.6, -1.5, -1.6, -1.6, -1.3]` | `+0.032` | `0.77%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 09:32:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,224.63 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.3, +0.5, +0.3]` | `+0.013` | `0.43%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,369.73 | ⚪ **CASH** | **-2.3 bps** (±0.6) | `[-3.0, -1.8, -2.0, -1.6, -1.4]` | `-0.201` | `0.61%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.87 | ⚪ **CASH** | **-1.6 bps** (±0.1) | `[-1.6, -1.5, -1.6, -1.6, -1.3]` | `+0.032` | `0.77%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 09:17:16 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,300.01 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.3, +0.5, +0.3]` | `+0.013` | `0.43%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,372.65 | ⚪ **CASH** | **-2.3 bps** (±0.6) | `[-3.0, -1.8, -2.0, -1.6, -1.4]` | `-0.201` | `0.61%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $103.07 | ⚪ **CASH** | **-1.6 bps** (±0.1) | `[-1.6, -1.5, -1.6, -1.6, -1.3]` | `+0.032` | `0.77%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 09:02:21 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,316.19 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.3, +0.5, +0.3]` | `+0.013` | `0.43%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,373.48 | ⚪ **CASH** | **-2.3 bps** (±0.6) | `[-3.0, -1.8, -2.0, -1.6, -1.4]` | `-0.201` | `0.61%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $103.19 | ⚪ **CASH** | **-1.6 bps** (±0.1) | `[-1.6, -1.5, -1.6, -1.6, -1.3]` | `+0.032` | `0.77%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 08:47:09 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,278.43 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.2, +0.0, +0.2, +0.1, +0.2]` | `-0.016` | `0.44%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,375.77 | ⚪ **CASH** | **-3.1 bps** (±0.4) | `[-3.6, -2.9, -2.4, -2.9, -2.7]` | `-0.169` | `0.62%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $103.26 | ⚪ **CASH** | **-1.5 bps** (±0.2) | `[-1.3, -1.1, -1.6, -1.6, -1.3]` | `-0.082` | `0.78%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 08:32:03 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,334.06 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.2, +0.0, +0.2, +0.1, +0.2]` | `-0.016` | `0.44%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,375.59 | ⚪ **CASH** | **-3.1 bps** (±0.4) | `[-3.6, -2.9, -2.4, -2.9, -2.7]` | `-0.169` | `0.62%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $103.20 | ⚪ **CASH** | **-1.5 bps** (±0.2) | `[-1.3, -1.1, -1.6, -1.6, -1.3]` | `-0.082` | `0.78%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 08:16:56 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,281.05 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.2, +0.0, +0.2, +0.1, +0.2]` | `-0.016` | `0.44%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,369.33 | ⚪ **CASH** | **-3.1 bps** (±0.4) | `[-3.6, -2.9, -2.4, -2.9, -2.7]` | `-0.169` | `0.62%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.91 | ⚪ **CASH** | **-1.5 bps** (±0.2) | `[-1.3, -1.1, -1.6, -1.6, -1.3]` | `-0.082` | `0.78%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 08:02:07 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,498.01 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.2, +0.0, +0.2, +0.1, +0.2]` | `-0.016` | `0.44%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,377.55 | ⚪ **CASH** | **-3.1 bps** (±0.4) | `[-3.6, -2.9, -2.4, -2.9, -2.7]` | `-0.169` | `0.62%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $103.21 | ⚪ **CASH** | **-1.5 bps** (±0.2) | `[-1.3, -1.1, -1.6, -1.6, -1.3]` | `-0.082` | `0.78%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 07:46:57 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,350.01 | ⚪ **CASH** | **-0.4 bps** (±0.2) | `[-0.2, -0.2, -0.1, -0.5, -0.6]` | `-0.046` | `0.42%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,373.41 | ⚪ **CASH** | **-3.5 bps** (±0.6) | `[-4.1, -2.9, -2.5, -2.8, -3.8]` | `-0.161` | `0.59%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.60 | ⚪ **CASH** | **-1.8 bps** (±0.4) | `[-0.9, -2.0, -1.8, -1.3, -1.8]` | `-0.103` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 07:32:31 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,148.01 | ⚪ **CASH** | **-0.4 bps** (±0.2) | `[-0.2, -0.2, -0.1, -0.5, -0.6]` | `-0.046` | `0.42%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,369.27 | ⚪ **CASH** | **-3.5 bps** (±0.6) | `[-4.1, -2.9, -2.5, -2.8, -3.8]` | `-0.161` | `0.59%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.24 | ⚪ **CASH** | **-1.8 bps** (±0.4) | `[-0.9, -2.0, -1.8, -1.3, -1.8]` | `-0.103` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 07:17:15 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,022.01 | ⚪ **CASH** | **-0.4 bps** (±0.2) | `[-0.2, -0.2, -0.1, -0.5, -0.6]` | `-0.046` | `0.42%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,366.05 | ⚪ **CASH** | **-3.5 bps** (±0.6) | `[-4.1, -2.9, -2.5, -2.8, -3.8]` | `-0.161` | `0.59%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.36 | ⚪ **CASH** | **-1.8 bps** (±0.4) | `[-0.9, -2.0, -1.8, -1.3, -1.8]` | `-0.103` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 07:02:23 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,882.82 | ⚪ **CASH** | **-0.4 bps** (±0.2) | `[-0.2, -0.2, -0.1, -0.5, -0.6]` | `-0.046` | `0.42%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,357.77 | ⚪ **CASH** | **-3.5 bps** (±0.6) | `[-4.1, -2.9, -2.5, -2.8, -3.8]` | `-0.161` | `0.59%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.15 | ⚪ **CASH** | **-1.8 bps** (±0.4) | `[-0.9, -2.0, -1.8, -1.3, -1.8]` | `-0.103` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 06:47:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,837.96 | ⚪ **CASH** | **+1.5 bps** (±0.6) | `[+1.2, +2.6, +1.1, +1.8, +2.1]` | `-0.057` | `0.42%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,355.63 | ⚪ **CASH** | **-3.4 bps** (±0.7) | `[-4.1, -2.9, -2.2, -2.6, -3.4]` | `-0.166` | `0.60%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.01 | ⚪ **CASH** | **+1.5 bps** (±0.7) | `[+3.2, +1.6, +1.5, +1.2, +2.1]` | `-0.087` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 06:32:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,950.00 | ⚪ **CASH** | **+1.5 bps** (±0.6) | `[+1.2, +2.6, +1.1, +1.8, +2.1]` | `-0.057` | `0.42%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,362.11 | ⚪ **CASH** | **-3.4 bps** (±0.7) | `[-4.1, -2.9, -2.2, -2.6, -3.4]` | `-0.166` | `0.60%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.10 | ⚪ **CASH** | **+1.5 bps** (±0.7) | `[+3.2, +1.6, +1.5, +1.2, +2.1]` | `-0.087` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 06:17:02 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,838.97 | ⚪ **CASH** | **+1.5 bps** (±0.6) | `[+1.2, +2.6, +1.1, +1.8, +2.1]` | `-0.057` | `0.42%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,355.85 | ⚪ **CASH** | **-3.4 bps** (±0.7) | `[-4.1, -2.9, -2.2, -2.6, -3.4]` | `-0.166` | `0.60%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.09 | ⚪ **CASH** | **+1.5 bps** (±0.7) | `[+3.2, +1.6, +1.5, +1.2, +2.1]` | `-0.087` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 06:02:29 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,623.26 | ⚪ **CASH** | **+1.5 bps** (±0.6) | `[+1.2, +2.6, +1.1, +1.8, +2.1]` | `-0.057` | `0.42%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,350.71 | ⚪ **CASH** | **-3.4 bps** (±0.7) | `[-4.1, -2.9, -2.2, -2.6, -3.4]` | `-0.166` | `0.60%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.62 | ⚪ **CASH** | **+1.5 bps** (±0.7) | `[+3.2, +1.6, +1.5, +1.2, +2.1]` | `-0.087` | `0.76%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 05:47:12 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,922.96 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.2, +0.0, +0.2, +0.1, +0.2]` | `-0.011` | `0.36%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,358.18 | ⚪ **CASH** | **-2.8 bps** (±0.4) | `[-3.0, -2.9, -2.5, -2.4, -1.8]` | `-0.134` | `0.56%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.85 | ⚪ **CASH** | **-1.9 bps** (±0.3) | `[-2.2, -1.6, -1.9, -1.4, -1.7]` | `-0.065` | `0.66%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 05:32:18 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,032.99 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.2, +0.0, +0.2, +0.1, +0.2]` | `-0.011` | `0.36%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,357.50 | ⚪ **CASH** | **-2.8 bps** (±0.4) | `[-3.0, -2.9, -2.5, -2.4, -1.8]` | `-0.134` | `0.56%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.15 | ⚪ **CASH** | **-1.9 bps** (±0.3) | `[-2.2, -1.6, -1.9, -1.4, -1.7]` | `-0.065` | `0.66%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 05:17:16 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,178.01 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.2, +0.0, +0.2, +0.1, +0.2]` | `-0.011` | `0.36%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,365.06 | ⚪ **CASH** | **-2.8 bps** (±0.4) | `[-3.0, -2.9, -2.5, -2.4, -1.8]` | `-0.134` | `0.56%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.57 | ⚪ **CASH** | **-1.9 bps** (±0.3) | `[-2.2, -1.6, -1.9, -1.4, -1.7]` | `-0.065` | `0.66%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 05:02:21 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,582.90 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.2, +0.0, +0.2, +0.1, +0.2]` | `-0.011` | `0.36%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,381.22 | ⚪ **CASH** | **-2.8 bps** (±0.4) | `[-3.0, -2.9, -2.5, -2.4, -1.8]` | `-0.134` | `0.56%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $103.74 | ⚪ **CASH** | **-1.9 bps** (±0.3) | `[-2.2, -1.6, -1.9, -1.4, -1.7]` | `-0.065` | `0.66%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 04:47:07 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,586.64 | ⚪ **CASH** | **+1.7 bps** (±0.3) | `[+1.7, +2.4, +1.4, +1.8, +2.1]` | `-0.027` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,381.58 | ⚪ **CASH** | **-0.6 bps** (±0.8) | `[-1.0, +0.9, -0.5, +0.8, -0.9]` | `-0.184` | `0.53%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.05 | ⚪ **CASH** | **+1.1 bps** (±0.8) | `[+2.3, +1.1, +0.3, +1.3, +2.3]` | `-0.113` | `0.61%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 04:32:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,493.99 | ⚪ **CASH** | **+1.7 bps** (±0.3) | `[+1.7, +2.4, +1.4, +1.8, +2.1]` | `-0.027` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,381.47 | ⚪ **CASH** | **-0.6 bps** (±0.8) | `[-1.0, +0.9, -0.5, +0.8, -0.9]` | `-0.184` | `0.53%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.01 | ⚪ **CASH** | **+1.1 bps** (±0.8) | `[+2.3, +1.1, +0.3, +1.3, +2.3]` | `-0.113` | `0.61%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 04:17:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,980.32 | ⚪ **CASH** | **+1.7 bps** (±0.3) | `[+1.7, +2.4, +1.4, +1.8, +2.1]` | `-0.027` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,364.79 | ⚪ **CASH** | **-0.6 bps** (±0.8) | `[-1.0, +0.9, -0.5, +0.8, -0.9]` | `-0.184` | `0.53%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.71 | ⚪ **CASH** | **+1.1 bps** (±0.8) | `[+2.3, +1.1, +0.3, +1.3, +2.3]` | `-0.113` | `0.61%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 04:02:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,975.88 | ⚪ **CASH** | **+1.7 bps** (±0.3) | `[+1.7, +2.4, +1.4, +1.8, +2.1]` | `-0.027` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,365.35 | ⚪ **CASH** | **-0.6 bps** (±0.8) | `[-1.0, +0.9, -0.5, +0.8, -0.9]` | `-0.184` | `0.53%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.75 | ⚪ **CASH** | **+1.1 bps** (±0.8) | `[+2.3, +1.1, +0.3, +1.3, +2.3]` | `-0.113` | `0.61%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 03:46:53 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,850.01 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.3, +0.3, +0.1, +0.1, -0.1]` | `-0.025` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,355.13 | ⚪ **CASH** | **-4.1 bps** (±0.9) | `[-4.2, -3.6, -2.6, -5.0, -2.8]` | `-0.107` | `0.52%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.19 | ⚪ **CASH** | **-5.0 bps** (±1.8) | `[-5.0, -6.1, -5.6, -1.6, -2.2]` | `-0.130` | `0.61%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
