# 📋 BOT_TRADE V5 — Livro de Auditoria de Decisões e Análise de Mercado

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o consenso dos 5 modelos XGBoost, o comportamento do CVD (Cumulative Volume Delta) e o disparo de travas de risco.

**Última Atualização**: `2026-10-13 01:31:59 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-13 01:31:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,135.40 | ⚪ **CASH** | **+0.8 bps** (±0.9) | `[+0.3, +1.7, +0.1, +1.6, +2.5]` | `-0.009` | `0.32%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,456.41 | ⚪ **CASH** | **-3.8 bps** (±0.5) | `[-4.2, -4.1, -3.3, -3.4, -3.0]` | `-0.142` | `0.46%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.70 | ⚪ **CASH** | **+5.6 bps** (±2.7) | `[+8.5, +2.3, +8.9, +5.6, +9.3]` | `-0.000` | `0.71%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-13 01:16:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,010.54 | ⚪ **CASH** | **+0.8 bps** (±0.9) | `[+0.3, +1.7, +0.1, +1.6, +2.5]` | `-0.009` | `0.32%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,441.52 | ⚪ **CASH** | **-3.8 bps** (±0.5) | `[-4.2, -4.1, -3.3, -3.4, -3.0]` | `-0.142` | `0.46%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.24 | ⚪ **CASH** | **+5.6 bps** (±2.7) | `[+8.5, +2.3, +8.9, +5.6, +9.3]` | `-0.000` | `0.71%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-13 01:02:02 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,553.62 | ⚪ **CASH** | **+0.8 bps** (±0.9) | `[+0.3, +1.7, +0.1, +1.6, +2.5]` | `-0.009` | `0.32%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,427.46 | ⚪ **CASH** | **-3.8 bps** (±0.5) | `[-4.2, -4.1, -3.3, -3.4, -3.0]` | `-0.142` | `0.46%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $103.46 | ⚪ **CASH** | **+5.6 bps** (±2.7) | `[+8.5, +2.3, +8.9, +5.6, +9.3]` | `-0.000` | `0.71%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-13 00:47:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,286.53 | ⚪ **CASH** | **+1.1 bps** (±0.5) | `[+0.8, +1.3, +0.9, +1.5, +2.3]` | `+0.003` | `0.31%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,421.11 | ⚪ **CASH** | **-0.7 bps** (±0.6) | `[-0.9, -0.0, -0.5, -1.0, +0.5]` | `-0.133` | `0.43%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $103.58 | ⚪ **CASH** | **-1.2 bps** (±0.6) | `[-1.4, -0.1, -0.4, -1.5, -1.3]` | `+0.061` | `0.56%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-13 00:32:10 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,310.82 | ⚪ **CASH** | **+1.1 bps** (±0.5) | `[+0.8, +1.3, +0.9, +1.5, +2.3]` | `+0.003` | `0.31%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,419.74 | ⚪ **CASH** | **-0.7 bps** (±0.6) | `[-0.9, -0.0, -0.5, -1.0, +0.5]` | `-0.133` | `0.43%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $103.65 | ⚪ **CASH** | **-1.2 bps** (±0.6) | `[-1.4, -0.1, -0.4, -1.5, -1.3]` | `+0.061` | `0.56%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-13 00:17:02 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,550.58 | ⚪ **CASH** | **+1.1 bps** (±0.5) | `[+0.8, +1.3, +0.9, +1.5, +2.3]` | `+0.003` | `0.31%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,429.53 | ⚪ **CASH** | **-0.7 bps** (±0.6) | `[-0.9, -0.0, -0.5, -1.0, +0.5]` | `-0.133` | `0.43%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.45 | ⚪ **CASH** | **-1.2 bps** (±0.6) | `[-1.4, -0.1, -0.4, -1.5, -1.3]` | `+0.061` | `0.56%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-13 00:02:03 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,948.05 | ⚪ **CASH** | **+1.1 bps** (±0.5) | `[+0.8, +1.3, +0.9, +1.5, +2.3]` | `+0.003` | `0.31%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,450.00 | ⚪ **CASH** | **-0.7 bps** (±0.6) | `[-0.9, -0.0, -0.5, -1.0, +0.5]` | `-0.133` | `0.43%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.84 | ⚪ **CASH** | **-1.2 bps** (±0.6) | `[-1.4, -0.1, -0.4, -1.5, -1.3]` | `+0.061` | `0.56%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 23:46:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,847.57 | ⚪ **CASH** | **+1.5 bps** (±0.7) | `[+0.9, +2.2, +1.3, +1.9, +2.9]` | `+0.020` | `0.31%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,449.35 | ⚪ **CASH** | **+0.4 bps** (±0.5) | `[+0.5, +1.1, +0.2, -0.0, +1.1]` | `-0.118` | `0.42%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.71 | ⚪ **CASH** | **-0.4 bps** (±0.7) | `[-1.0, +0.5, +0.9, -0.4, -0.3]` | `+0.124` | `0.57%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 23:32:16 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,991.89 | ⚪ **CASH** | **+1.5 bps** (±0.7) | `[+0.9, +2.2, +1.3, +1.9, +2.9]` | `+0.020` | `0.31%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,459.01 | ⚪ **CASH** | **+0.4 bps** (±0.5) | `[+0.5, +1.1, +0.2, -0.0, +1.1]` | `-0.118` | `0.42%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.99 | ⚪ **CASH** | **-0.4 bps** (±0.7) | `[-1.0, +0.5, +0.9, -0.4, -0.3]` | `+0.124` | `0.57%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 23:17:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,063.32 | ⚪ **CASH** | **+1.5 bps** (±0.7) | `[+0.9, +2.2, +1.3, +1.9, +2.9]` | `+0.020` | `0.31%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,462.49 | ⚪ **CASH** | **+0.4 bps** (±0.5) | `[+0.5, +1.1, +0.2, -0.0, +1.1]` | `-0.118` | `0.42%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.21 | ⚪ **CASH** | **-0.4 bps** (±0.7) | `[-1.0, +0.5, +0.9, -0.4, -0.3]` | `+0.124` | `0.57%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 23:02:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,105.30 | ⚪ **CASH** | **+1.5 bps** (±0.7) | `[+0.9, +2.2, +1.3, +1.9, +2.9]` | `+0.020` | `0.31%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,464.39 | ⚪ **CASH** | **+0.4 bps** (±0.5) | `[+0.5, +1.1, +0.2, -0.0, +1.1]` | `-0.118` | `0.42%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.25 | ⚪ **CASH** | **-0.4 bps** (±0.7) | `[-1.0, +0.5, +0.9, -0.4, -0.3]` | `+0.124` | `0.57%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 22:46:58 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,533.70 | ⚪ **CASH** | **+1.9 bps** (±0.5) | `[+2.1, +2.6, +1.4, +2.1, +2.6]` | `+0.036` | `0.30%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,483.29 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.4, +0.5, -0.0, +0.3, +0.2]` | `-0.101` | `0.39%/h` | `alt_downtrend` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.83 | ⚪ **CASH** | **-0.4 bps** (±0.7) | `[-1.0, +0.5, +0.9, -0.7, +0.4]` | `+0.126` | `0.56%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 22:31:57 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,666.05 | ⚪ **CASH** | **+1.9 bps** (±0.5) | `[+2.1, +2.6, +1.4, +2.1, +2.6]` | `+0.036` | `0.30%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,491.01 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.4, +0.5, -0.0, +0.3, +0.2]` | `-0.101` | `0.39%/h` | `alt_downtrend` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $107.14 | ⚪ **CASH** | **-0.4 bps** (±0.7) | `[-1.0, +0.5, +0.9, -0.7, +0.4]` | `+0.126` | `0.56%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 22:16:58 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,674.01 | ⚪ **CASH** | **+1.9 bps** (±0.5) | `[+2.1, +2.6, +1.4, +2.1, +2.6]` | `+0.036` | `0.30%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,493.35 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.4, +0.5, -0.0, +0.3, +0.2]` | `-0.101` | `0.39%/h` | `alt_downtrend` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $107.24 | ⚪ **CASH** | **-0.4 bps** (±0.7) | `[-1.0, +0.5, +0.9, -0.7, +0.4]` | `+0.126` | `0.56%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 22:02:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,625.60 | ⚪ **CASH** | **+1.9 bps** (±0.5) | `[+2.1, +2.6, +1.4, +2.1, +2.6]` | `+0.036` | `0.30%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,492.84 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.4, +0.5, -0.0, +0.3, +0.2]` | `-0.101` | `0.39%/h` | `alt_downtrend` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $107.30 | ⚪ **CASH** | **-0.4 bps** (±0.7) | `[-1.0, +0.5, +0.9, -0.7, +0.4]` | `+0.126` | `0.56%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 21:47:00 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,510.34 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.2, +0.0, +0.2, +0.1, +0.2]` | `+0.019` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,489.43 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.5, -0.4, -0.1, -0.1, -0.1]` | `-0.076` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.85 | ⚪ **CASH** | **-2.6 bps** (±0.2) | `[-2.7, -2.7, -2.4, -2.5, -2.0]` | `+0.137` | `0.53%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 21:31:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,950.20 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.2, +0.0, +0.2, +0.1, +0.2]` | `+0.019` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,514.87 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.5, -0.4, -0.1, -0.1, -0.1]` | `-0.076` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $108.25 | ⚪ **CASH** | **-2.6 bps** (±0.2) | `[-2.7, -2.7, -2.4, -2.5, -2.0]` | `+0.137` | `0.53%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 21:17:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,909.21 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.2, +0.0, +0.2, +0.1, +0.2]` | `+0.019` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,512.64 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.5, -0.4, -0.1, -0.1, -0.1]` | `-0.076` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $108.19 | ⚪ **CASH** | **-2.6 bps** (±0.2) | `[-2.7, -2.7, -2.4, -2.5, -2.0]` | `+0.137` | `0.53%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 21:02:17 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,062.01 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.2, +0.0, +0.2, +0.1, +0.2]` | `+0.019` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,518.26 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.5, -0.4, -0.1, -0.1, -0.1]` | `-0.076` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $108.34 | ⚪ **CASH** | **-2.6 bps** (±0.2) | `[-2.7, -2.7, -2.4, -2.5, -2.0]` | `+0.137` | `0.53%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 20:46:53 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,096.00 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.2, +0.0, +0.0, +0.1, +0.2]` | `+0.048` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,523.91 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.2, -0.4, -0.1, -0.2, -0.4]` | `-0.103` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $108.71 | ⚪ **CASH** | **-2.5 bps** (±0.2) | `[-2.5, -2.4, -2.4, -2.5, -2.0]` | `+0.083` | `0.54%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 20:32:03 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,103.19 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.2, +0.0, +0.0, +0.1, +0.2]` | `+0.048` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,525.05 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.2, -0.4, -0.1, -0.2, -0.4]` | `-0.103` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $108.59 | ⚪ **CASH** | **-2.5 bps** (±0.2) | `[-2.5, -2.4, -2.4, -2.5, -2.0]` | `+0.083` | `0.54%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 20:16:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,077.32 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.2, +0.0, +0.0, +0.1, +0.2]` | `+0.048` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,525.80 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.2, -0.4, -0.1, -0.2, -0.4]` | `-0.103` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $108.80 | ⚪ **CASH** | **-2.5 bps** (±0.2) | `[-2.5, -2.4, -2.4, -2.5, -2.0]` | `+0.083` | `0.54%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 20:02:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,862.11 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.2, +0.0, +0.0, +0.1, +0.2]` | `+0.048` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,522.49 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.2, -0.4, -0.1, -0.2, -0.4]` | `-0.103` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $108.38 | ⚪ **CASH** | **-2.5 bps** (±0.2) | `[-2.5, -2.4, -2.4, -2.5, -2.0]` | `+0.083` | `0.54%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 19:46:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,748.01 | ⚪ **CASH** | **+0.4 bps** (±0.3) | `[+0.1, +0.9, +0.5, +0.5, +1.1]` | `+0.042` | `0.27%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,517.05 | ⚪ **CASH** | **-0.6 bps** (±0.2) | `[-0.7, -0.5, -0.2, -0.7, -0.7]` | `-0.089` | `0.35%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $108.16 | ⚪ **CASH** | **-3.5 bps** (±0.6) | `[-4.1, -3.1, -2.6, -3.6, -2.8]` | `+0.058` | `0.53%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 19:32:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,713.72 | ⚪ **CASH** | **+0.4 bps** (±0.3) | `[+0.1, +0.9, +0.5, +0.5, +1.1]` | `+0.042` | `0.27%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,519.10 | ⚪ **CASH** | **-0.6 bps** (±0.2) | `[-0.7, -0.5, -0.2, -0.7, -0.7]` | `-0.089` | `0.35%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $108.23 | ⚪ **CASH** | **-3.5 bps** (±0.6) | `[-4.1, -3.1, -2.6, -3.6, -2.8]` | `+0.058` | `0.53%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 19:17:12 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,350.01 | ⚪ **CASH** | **+0.4 bps** (±0.3) | `[+0.1, +0.9, +0.5, +0.5, +1.1]` | `+0.042` | `0.27%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,508.29 | ⚪ **CASH** | **-0.6 bps** (±0.2) | `[-0.7, -0.5, -0.2, -0.7, -0.7]` | `-0.089` | `0.35%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $107.47 | ⚪ **CASH** | **-3.5 bps** (±0.6) | `[-4.1, -3.1, -2.6, -3.6, -2.8]` | `+0.058` | `0.53%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 19:02:10 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,524.30 | ⚪ **CASH** | **+0.4 bps** (±0.3) | `[+0.1, +0.9, +0.5, +0.5, +1.1]` | `+0.042` | `0.27%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,517.11 | ⚪ **CASH** | **-0.6 bps** (±0.2) | `[-0.7, -0.5, -0.2, -0.7, -0.7]` | `-0.089` | `0.35%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $107.71 | ⚪ **CASH** | **-3.5 bps** (±0.6) | `[-4.1, -3.1, -2.6, -3.6, -2.8]` | `+0.058` | `0.53%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 18:47:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,460.01 | ⚪ **CASH** | **+0.4 bps** (±0.2) | `[+0.1, +0.6, +0.5, +0.5, +0.6]` | `+0.057` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,512.93 | ⚪ **CASH** | **-0.6 bps** (±0.2) | `[-0.7, -0.5, -0.2, -0.7, -0.7]` | `-0.114` | `0.35%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $107.65 | ⚪ **CASH** | **-3.5 bps** (±0.4) | `[-3.9, -3.1, -3.4, -3.6, -2.8]` | `+0.016` | `0.54%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 18:32:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,508.01 | ⚪ **CASH** | **+0.4 bps** (±0.2) | `[+0.1, +0.6, +0.5, +0.5, +0.6]` | `+0.057` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,513.69 | ⚪ **CASH** | **-0.6 bps** (±0.2) | `[-0.7, -0.5, -0.2, -0.7, -0.7]` | `-0.114` | `0.35%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $107.73 | ⚪ **CASH** | **-3.5 bps** (±0.4) | `[-3.9, -3.1, -3.4, -3.6, -2.8]` | `+0.016` | `0.54%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 18:16:58 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,466.45 | ⚪ **CASH** | **+0.4 bps** (±0.2) | `[+0.1, +0.6, +0.5, +0.5, +0.6]` | `+0.057` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,512.47 | ⚪ **CASH** | **-0.6 bps** (±0.2) | `[-0.7, -0.5, -0.2, -0.7, -0.7]` | `-0.114` | `0.35%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $107.68 | ⚪ **CASH** | **-3.5 bps** (±0.4) | `[-3.9, -3.1, -3.4, -3.6, -2.8]` | `+0.016` | `0.54%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 18:02:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,548.00 | ⚪ **CASH** | **+0.4 bps** (±0.2) | `[+0.1, +0.6, +0.5, +0.5, +0.6]` | `+0.057` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,513.31 | ⚪ **CASH** | **-0.6 bps** (±0.2) | `[-0.7, -0.5, -0.2, -0.7, -0.7]` | `-0.114` | `0.35%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $107.86 | ⚪ **CASH** | **-3.5 bps** (±0.4) | `[-3.9, -3.1, -3.4, -3.6, -2.8]` | `+0.016` | `0.54%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 17:47:02 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,490.37 | ⚪ **CASH** | **+0.5 bps** (±0.1) | `[+0.6, +0.6, +0.5, +0.5, +0.6]` | `+0.074` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,508.18 | ⚪ **CASH** | **+0.4 bps** (±0.2) | `[+0.7, +0.7, +0.2, +0.3, +0.4]` | `-0.044` | `0.35%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $107.55 | ⚪ **CASH** | **-1.5 bps** (±0.4) | `[-1.7, -1.3, -1.5, -1.5, -0.6]` | `-0.035` | `0.55%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 17:32:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,474.01 | ⚪ **CASH** | **+0.5 bps** (±0.1) | `[+0.6, +0.6, +0.5, +0.5, +0.6]` | `+0.074` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,508.67 | ⚪ **CASH** | **+0.4 bps** (±0.2) | `[+0.7, +0.7, +0.2, +0.3, +0.4]` | `-0.044` | `0.35%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $107.49 | ⚪ **CASH** | **-1.5 bps** (±0.4) | `[-1.7, -1.3, -1.5, -1.5, -0.6]` | `-0.035` | `0.55%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 17:17:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,622.00 | ⚪ **CASH** | **+0.5 bps** (±0.1) | `[+0.6, +0.6, +0.5, +0.5, +0.6]` | `+0.074` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,518.49 | ⚪ **CASH** | **+0.4 bps** (±0.2) | `[+0.7, +0.7, +0.2, +0.3, +0.4]` | `-0.044` | `0.35%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $108.05 | ⚪ **CASH** | **-1.5 bps** (±0.4) | `[-1.7, -1.3, -1.5, -1.5, -0.6]` | `-0.035` | `0.55%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 17:02:10 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,545.81 | ⚪ **CASH** | **+0.5 bps** (±0.1) | `[+0.6, +0.6, +0.5, +0.5, +0.6]` | `+0.074` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,515.46 | ⚪ **CASH** | **+0.4 bps** (±0.2) | `[+0.7, +0.7, +0.2, +0.3, +0.4]` | `-0.044` | `0.35%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $108.02 | ⚪ **CASH** | **-1.5 bps** (±0.4) | `[-1.7, -1.3, -1.5, -1.5, -0.6]` | `-0.035` | `0.55%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-12 16:47:10 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,774.96 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.092` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,526.18 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.3, -0.4, -0.1, -0.1, +0.0]` | `+0.004` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $108.66 | ⚪ **CASH** | **-3.3 bps** (±0.5) | `[-3.9, -3.1, -2.6, -3.3, -2.5]` | `-0.024` | `0.53%/h` | `alt_downtrend` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |
