# 📋 BOT_TRADE V5 — Livro de Auditoria de Decisões e Análise de Mercado

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o consenso dos 5 modelos XGBoost, o comportamento do CVD (Cumulative Volume Delta) e o disparo de travas de risco.

**Última Atualização**: `2026-09-15 21:17:15 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-09-15 21:17:15 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,874.75 | ⚪ **CASH** | **+0.6 bps** (±0.1) | `[+0.6, +0.8, +0.8, +0.6, +0.6]` | `+0.030` | `0.41%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,403.11 | ⚪ **CASH** | **+0.6 bps** (±0.6) | `[+0.4, +1.0, -0.0, +1.4, +1.5]` | `-0.070` | `0.61%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.18 | ⚪ **CASH** | **-0.2 bps** (±0.6) | `[-0.2, -0.4, -0.1, +1.3, +0.0]` | `-0.042` | `0.61%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 21:02:22 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,781.69 | ⚪ **CASH** | **+0.6 bps** (±0.1) | `[+0.6, +0.8, +0.8, +0.6, +0.6]` | `+0.030` | `0.41%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,401.04 | ⚪ **CASH** | **+0.6 bps** (±0.6) | `[+0.4, +1.0, -0.0, +1.4, +1.5]` | `-0.070` | `0.61%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.10 | ⚪ **CASH** | **-0.2 bps** (±0.6) | `[-0.2, -0.4, -0.1, +1.3, +0.0]` | `-0.042` | `0.61%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 20:47:23 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,948.91 | ⚪ **CASH** | **-0.0 bps** (±0.1) | `[-0.2, +0.0, +0.0, +0.1, +0.2]` | `-0.002` | `0.41%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,408.80 | ⚪ **CASH** | **-0.4 bps** (±0.2) | `[-0.2, -0.3, -0.4, -0.5, -0.0]` | `-0.104` | `0.61%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.42 | ⚪ **CASH** | **-2.3 bps** (±0.3) | `[-2.3, -1.7, -2.4, -2.0, -2.4]` | `-0.074` | `0.62%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 20:32:03 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,807.66 | ⚪ **CASH** | **-0.0 bps** (±0.1) | `[-0.2, +0.0, +0.0, +0.1, +0.2]` | `-0.002` | `0.41%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,403.49 | ⚪ **CASH** | **-0.4 bps** (±0.2) | `[-0.2, -0.3, -0.4, -0.5, -0.0]` | `-0.104` | `0.61%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $96.93 | ⚪ **CASH** | **-2.3 bps** (±0.3) | `[-2.3, -1.7, -2.4, -2.0, -2.4]` | `-0.074` | `0.62%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 20:17:16 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,997.13 | ⚪ **CASH** | **-0.0 bps** (±0.1) | `[-0.2, +0.0, +0.0, +0.1, +0.2]` | `-0.002` | `0.41%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,406.90 | ⚪ **CASH** | **-0.4 bps** (±0.2) | `[-0.2, -0.3, -0.4, -0.5, -0.0]` | `-0.104` | `0.61%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.52 | ⚪ **CASH** | **-2.3 bps** (±0.3) | `[-2.3, -1.7, -2.4, -2.0, -2.4]` | `-0.074` | `0.62%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 20:02:17 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,217.11 | ⚪ **CASH** | **-0.0 bps** (±0.1) | `[-0.2, +0.0, +0.0, +0.1, +0.2]` | `-0.002` | `0.41%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,415.92 | ⚪ **CASH** | **-0.4 bps** (±0.2) | `[-0.2, -0.3, -0.4, -0.5, -0.0]` | `-0.104` | `0.61%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.94 | ⚪ **CASH** | **-2.3 bps** (±0.3) | `[-2.3, -1.7, -2.4, -2.0, -2.4]` | `-0.074` | `0.62%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 19:47:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,886.96 | ⚪ **CASH** | **+0.9 bps** (±0.8) | `[+2.1, -0.0, +1.2, +2.0, +1.3]` | `-0.042` | `0.42%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,404.37 | ⚪ **CASH** | **+0.3 bps** (±0.6) | `[+0.2, +1.5, -0.2, +0.7, +0.5]` | `-0.138` | `0.61%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.62 | ⚪ **CASH** | **+0.6 bps** (±0.9) | `[+1.3, +1.2, +2.7, +0.1, +0.3]` | `-0.096` | `0.62%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 19:32:18 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,000.00 | ⚪ **CASH** | **+0.9 bps** (±0.8) | `[+2.1, -0.0, +1.2, +2.0, +1.3]` | `-0.042` | `0.42%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,404.10 | ⚪ **CASH** | **+0.3 bps** (±0.6) | `[+0.2, +1.5, -0.2, +0.7, +0.5]` | `-0.138` | `0.61%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.78 | ⚪ **CASH** | **+0.6 bps** (±0.9) | `[+1.3, +1.2, +2.7, +0.1, +0.3]` | `-0.096` | `0.62%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 19:17:19 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,171.80 | ⚪ **CASH** | **+0.9 bps** (±0.8) | `[+2.1, -0.0, +1.2, +2.0, +1.3]` | `-0.042` | `0.42%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,413.11 | ⚪ **CASH** | **+0.3 bps** (±0.6) | `[+0.2, +1.5, -0.2, +0.7, +0.5]` | `-0.138` | `0.61%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $98.46 | ⚪ **CASH** | **+0.6 bps** (±0.9) | `[+1.3, +1.2, +2.7, +0.1, +0.3]` | `-0.096` | `0.62%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 19:02:21 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,895.05 | ⚪ **CASH** | **+0.9 bps** (±0.8) | `[+2.1, -0.0, +1.2, +2.0, +1.3]` | `-0.042` | `0.42%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,401.40 | ⚪ **CASH** | **+0.3 bps** (±0.6) | `[+0.2, +1.5, -0.2, +0.7, +0.5]` | `-0.138` | `0.61%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.90 | ⚪ **CASH** | **+0.6 bps** (±0.9) | `[+1.3, +1.2, +2.7, +0.1, +0.3]` | `-0.096` | `0.62%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 18:47:07 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,309.78 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.012` | `0.36%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,372.82 | ⚪ **CASH** | **-0.5 bps** (±0.2) | `[-0.4, -0.7, -0.5, -0.3, -0.1]` | `-0.175` | `0.56%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $96.66 | ⚪ **CASH** | **-1.5 bps** (±0.4) | `[-1.9, -1.0, -1.4, -0.6, -1.5]` | `-0.053` | `0.52%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 18:32:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,867.73 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.012` | `0.36%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,432.86 | ⚪ **CASH** | **-0.5 bps** (±0.2) | `[-0.4, -0.7, -0.5, -0.3, -0.1]` | `-0.175` | `0.56%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $99.80 | ⚪ **CASH** | **-1.5 bps** (±0.4) | `[-1.9, -1.0, -1.4, -0.6, -1.5]` | `-0.053` | `0.52%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 18:17:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,690.36 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.012` | `0.36%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,427.86 | ⚪ **CASH** | **-0.5 bps** (±0.2) | `[-0.4, -0.7, -0.5, -0.3, -0.1]` | `-0.175` | `0.56%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $99.62 | ⚪ **CASH** | **-1.5 bps** (±0.4) | `[-1.9, -1.0, -1.4, -0.6, -1.5]` | `-0.053` | `0.52%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 18:02:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,924.00 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.012` | `0.36%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,440.75 | ⚪ **CASH** | **-0.5 bps** (±0.2) | `[-0.4, -0.7, -0.5, -0.3, -0.1]` | `-0.175` | `0.56%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $100.21 | ⚪ **CASH** | **-1.5 bps** (±0.4) | `[-1.9, -1.0, -1.4, -0.6, -1.5]` | `-0.053` | `0.52%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 17:47:17 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,914.02 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.4, +0.5, +0.3]` | `-0.007` | `0.34%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,436.13 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.2, +0.1, -0.1, +0.3, -0.3]` | `-0.220` | `0.54%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $100.07 | ⚪ **CASH** | **-2.1 bps** (±0.1) | `[-1.9, -2.2, -2.1, -2.1, -1.9]` | `-0.099` | `0.49%/h` | `btc_dumping` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 17:32:26 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,772.01 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.4, +0.5, +0.3]` | `-0.007` | `0.34%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,431.99 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.2, +0.1, -0.1, +0.3, -0.3]` | `-0.220` | `0.54%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $99.73 | ⚪ **CASH** | **-2.1 bps** (±0.1) | `[-1.9, -2.2, -2.1, -2.1, -1.9]` | `-0.099` | `0.49%/h` | `btc_dumping` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 17:17:10 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,287.17 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.4, +0.5, +0.3]` | `-0.007` | `0.34%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,417.25 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.2, +0.1, -0.1, +0.3, -0.3]` | `-0.220` | `0.54%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $98.96 | ⚪ **CASH** | **-2.1 bps** (±0.1) | `[-1.9, -2.2, -2.1, -2.1, -1.9]` | `-0.099` | `0.49%/h` | `btc_dumping` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 17:02:19 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,389.21 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.4, +0.5, +0.3]` | `-0.007` | `0.34%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,422.01 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.2, +0.1, -0.1, +0.3, -0.3]` | `-0.220` | `0.54%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $99.09 | ⚪ **CASH** | **-2.1 bps** (±0.1) | `[-1.9, -2.2, -2.1, -2.1, -1.9]` | `-0.099` | `0.49%/h` | `btc_dumping` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 16:47:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,414.00 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.0, +0.0, +0.2, +0.1, +0.2]` | `-0.011` | `0.34%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,422.73 | ⚪ **CASH** | **-0.1 bps** (±0.4) | `[-0.5, +0.5, -0.0, +0.1, +0.3]` | `-0.203` | `0.55%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $99.22 | ⚪ **CASH** | **-2.2 bps** (±0.2) | `[-1.9, -1.9, -2.4, -2.0, -2.0]` | `-0.081` | `0.49%/h` | `btc_dumping` `alt_downtrend` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 16:32:21 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,412.02 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.0, +0.0, +0.2, +0.1, +0.2]` | `-0.011` | `0.34%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,421.88 | ⚪ **CASH** | **-0.1 bps** (±0.4) | `[-0.5, +0.5, -0.0, +0.1, +0.3]` | `-0.203` | `0.55%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $99.20 | ⚪ **CASH** | **-2.2 bps** (±0.2) | `[-1.9, -1.9, -2.4, -2.0, -2.0]` | `-0.081` | `0.49%/h` | `btc_dumping` `alt_downtrend` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 16:17:15 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,372.13 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.0, +0.0, +0.2, +0.1, +0.2]` | `-0.011` | `0.34%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,417.78 | ⚪ **CASH** | **-0.1 bps** (±0.4) | `[-0.5, +0.5, -0.0, +0.1, +0.3]` | `-0.203` | `0.55%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $99.06 | ⚪ **CASH** | **-2.2 bps** (±0.2) | `[-1.9, -1.9, -2.4, -2.0, -2.0]` | `-0.081` | `0.49%/h` | `btc_dumping` `alt_downtrend` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 16:02:24 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,548.13 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.0, +0.0, +0.2, +0.1, +0.2]` | `-0.011` | `0.34%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,424.70 | ⚪ **CASH** | **-0.1 bps** (±0.4) | `[-0.5, +0.5, -0.0, +0.1, +0.3]` | `-0.203` | `0.55%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $99.41 | ⚪ **CASH** | **-2.2 bps** (±0.2) | `[-1.9, -1.9, -2.4, -2.0, -2.0]` | `-0.081` | `0.49%/h` | `btc_dumping` `alt_downtrend` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 15:47:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,462.00 | ⚪ **CASH** | **+2.3 bps** (±0.7) | `[+2.1, +2.3, +1.9, +3.2, +3.8]` | `-0.045` | `0.31%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,428.21 | ⚪ **CASH** | **+0.5 bps** (±0.7) | `[-0.1, +1.2, +0.0, +1.7, +1.4]` | `-0.226` | `0.54%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $99.48 | ⚪ **CASH** | **-0.0 bps** (±1.0) | `[+0.2, +0.7, +1.1, -1.3, +1.6]` | `-0.088` | `0.49%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 15:32:29 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,326.01 | ⚪ **CASH** | **+2.3 bps** (±0.7) | `[+2.1, +2.3, +1.9, +3.2, +3.8]` | `-0.045` | `0.31%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,426.34 | ⚪ **CASH** | **+0.5 bps** (±0.7) | `[-0.1, +1.2, +0.0, +1.7, +1.4]` | `-0.226` | `0.54%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $99.39 | ⚪ **CASH** | **-0.0 bps** (±1.0) | `[+0.2, +0.7, +1.1, -1.3, +1.6]` | `-0.088` | `0.49%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 15:17:09 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,009.95 | ⚪ **CASH** | **+2.3 bps** (±0.7) | `[+2.1, +2.3, +1.9, +3.2, +3.8]` | `-0.045` | `0.31%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,414.41 | ⚪ **CASH** | **+0.5 bps** (±0.7) | `[-0.1, +1.2, +0.0, +1.7, +1.4]` | `-0.226` | `0.54%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $99.11 | ⚪ **CASH** | **-0.0 bps** (±1.0) | `[+0.2, +0.7, +1.1, -1.3, +1.6]` | `-0.088` | `0.49%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 15:02:37 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,915.64 | ⚪ **CASH** | **+2.3 bps** (±0.7) | `[+2.1, +2.3, +1.9, +3.2, +3.8]` | `-0.045` | `0.31%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,404.49 | ⚪ **CASH** | **+0.5 bps** (±0.7) | `[-0.1, +1.2, +0.0, +1.7, +1.4]` | `-0.226` | `0.54%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $98.77 | ⚪ **CASH** | **-0.0 bps** (±1.0) | `[+0.2, +0.7, +1.1, -1.3, +1.6]` | `-0.088` | `0.49%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 14:47:36 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,790.57 | ⚪ **CASH** | **+0.8 bps** (±0.3) | `[+0.8, +1.0, +0.9, +0.6, +1.5]` | `+0.014` | `0.28%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,410.45 | ⚪ **CASH** | **-0.9 bps** (±0.2) | `[-1.1, -0.6, -1.0, -0.8, -0.5]` | `-0.210` | `0.44%/h` | `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $98.66 | ⚪ **CASH** | **+0.9 bps** (±0.3) | `[+1.0, +1.6, +0.6, +1.1, +0.9]` | `+0.035` | `0.39%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 14:32:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,245.49 | ⚪ **CASH** | **+0.8 bps** (±0.3) | `[+0.8, +1.0, +0.9, +0.6, +1.5]` | `+0.014` | `0.28%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,435.91 | ⚪ **CASH** | **-0.9 bps** (±0.2) | `[-1.1, -0.6, -1.0, -0.8, -0.5]` | `-0.210` | `0.44%/h` | `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $99.91 | ⚪ **CASH** | **+0.9 bps** (±0.3) | `[+1.0, +1.6, +0.6, +1.1, +0.9]` | `+0.035` | `0.39%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 14:17:10 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,334.00 | ⚪ **CASH** | **+0.8 bps** (±0.3) | `[+0.8, +1.0, +0.9, +0.6, +1.5]` | `+0.014` | `0.28%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,444.17 | ⚪ **CASH** | **-0.9 bps** (±0.2) | `[-1.1, -0.6, -1.0, -0.8, -0.5]` | `-0.210` | `0.44%/h` | `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $100.15 | ⚪ **CASH** | **+0.9 bps** (±0.3) | `[+1.0, +1.6, +0.6, +1.1, +0.9]` | `+0.035` | `0.39%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 14:02:29 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,541.47 | ⚪ **CASH** | **+0.8 bps** (±0.3) | `[+0.8, +1.0, +0.9, +0.6, +1.5]` | `+0.014` | `0.28%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,452.64 | ⚪ **CASH** | **-0.9 bps** (±0.2) | `[-1.1, -0.6, -1.0, -0.8, -0.5]` | `-0.210` | `0.44%/h` | `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $100.55 | ⚪ **CASH** | **+0.9 bps** (±0.3) | `[+1.0, +1.6, +0.6, +1.1, +0.9]` | `+0.035` | `0.39%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 13:47:12 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,246.79 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.126` | `0.27%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,447.70 | ⚪ **CASH** | **-1.7 bps** (±0.2) | `[-1.8, -1.3, -1.4, -1.9, -1.4]` | `-0.123` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $100.02 | ⚪ **CASH** | **-1.7 bps** (±0.1) | `[-1.8, -1.7, -1.6, -1.6, -1.5]` | `+0.034` | `0.39%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 13:32:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,773.79 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.126` | `0.27%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,470.99 | ⚪ **CASH** | **-1.7 bps** (±0.2) | `[-1.8, -1.3, -1.4, -1.9, -1.4]` | `-0.123` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $100.61 | ⚪ **CASH** | **-1.7 bps** (±0.1) | `[-1.8, -1.7, -1.6, -1.6, -1.5]` | `+0.034` | `0.39%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 13:16:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,002.00 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.126` | `0.27%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,479.16 | ⚪ **CASH** | **-1.7 bps** (±0.2) | `[-1.8, -1.3, -1.4, -1.9, -1.4]` | `-0.123` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.10 | ⚪ **CASH** | **-1.7 bps** (±0.1) | `[-1.8, -1.7, -1.6, -1.6, -1.5]` | `+0.034` | `0.39%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 13:02:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,000.00 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.126` | `0.27%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,482.02 | ⚪ **CASH** | **-1.7 bps** (±0.2) | `[-1.8, -1.3, -1.4, -1.9, -1.4]` | `-0.123` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.05 | ⚪ **CASH** | **-1.7 bps** (±0.1) | `[-1.8, -1.7, -1.6, -1.6, -1.5]` | `+0.034` | `0.39%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 12:47:22 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,945.99 | ⚪ **CASH** | **+0.4 bps** (±0.1) | `[+0.3, +0.5, +0.3, +0.5, +0.3]` | `+0.102` | `0.27%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,477.98 | ⚪ **CASH** | **-1.5 bps** (±0.2) | `[-1.3, -1.3, -1.1, -1.4, -1.7]` | `-0.079` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $100.96 | ⚪ **CASH** | **-1.5 bps** (±0.2) | `[-1.2, -1.5, -1.6, -1.4, -1.3]` | `+0.024` | `0.40%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-15 12:32:20 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,895.96 | ⚪ **CASH** | **+0.4 bps** (±0.1) | `[+0.3, +0.5, +0.3, +0.5, +0.3]` | `+0.102` | `0.27%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,476.92 | ⚪ **CASH** | **-1.5 bps** (±0.2) | `[-1.3, -1.3, -1.1, -1.4, -1.7]` | `-0.079` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $100.94 | ⚪ **CASH** | **-1.5 bps** (±0.2) | `[-1.2, -1.5, -1.6, -1.4, -1.3]` | `+0.024` | `0.40%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |
