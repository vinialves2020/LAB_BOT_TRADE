# 📋 BOT_TRADE V5 — Livro de Auditoria de Decisões e Análise de Mercado

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o consenso dos 5 modelos XGBoost, o comportamento do CVD (Cumulative Volume Delta) e o disparo de travas de risco.

**Última Atualização**: `2026-10-03 12:32:22 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-03 12:32:22 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,852.02 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.3, -0.3, +0.0, -0.4, -0.3]` | `-0.052` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,682.33 | ⚪ **CASH** | **-0.9 bps** (±0.3) | `[-0.2, -0.9, -0.4, -1.1, -0.9]` | `+0.097` | `0.38%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.40 | ⚪ **CASH** | **-1.3 bps** (±0.1) | `[-1.3, -1.3, -1.4, -1.2, -1.3]` | `-0.059` | `0.54%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 12:17:33 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,722.73 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.3, -0.3, +0.0, -0.4, -0.3]` | `-0.052` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,683.70 | ⚪ **CASH** | **-0.9 bps** (±0.3) | `[-0.2, -0.9, -0.4, -1.1, -0.9]` | `+0.097` | `0.38%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.43 | ⚪ **CASH** | **-1.3 bps** (±0.1) | `[-1.3, -1.3, -1.4, -1.2, -1.3]` | `-0.059` | `0.54%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 12:02:26 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,688.83 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.3, -0.3, +0.0, -0.4, -0.3]` | `-0.052` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,684.64 | ⚪ **CASH** | **-0.9 bps** (±0.3) | `[-0.2, -0.9, -0.4, -1.1, -0.9]` | `+0.097` | `0.38%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.42 | ⚪ **CASH** | **-1.3 bps** (±0.1) | `[-1.3, -1.3, -1.4, -1.2, -1.3]` | `-0.059` | `0.54%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 11:47:32 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,671.85 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.3, -0.3, +0.0, -0.4, -0.3]` | `-0.025` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,685.93 | ⚪ **CASH** | **-1.0 bps** (±0.2) | `[-0.8, -0.9, -1.0, -1.2, -0.8]` | `+0.139` | `0.38%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.41 | ⚪ **CASH** | **-1.1 bps** (±0.3) | `[-1.0, -0.6, -0.7, -0.9, -1.5]` | `-0.047` | `0.55%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 11:32:10 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,651.21 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.3, -0.3, +0.0, -0.4, -0.3]` | `-0.025` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,684.26 | ⚪ **CASH** | **-1.0 bps** (±0.2) | `[-0.8, -0.9, -1.0, -1.2, -0.8]` | `+0.139` | `0.38%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.34 | ⚪ **CASH** | **-1.1 bps** (±0.3) | `[-1.0, -0.6, -0.7, -0.9, -1.5]` | `-0.047` | `0.55%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 11:17:15 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,636.13 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.3, -0.3, +0.0, -0.4, -0.3]` | `-0.025` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,682.29 | ⚪ **CASH** | **-1.0 bps** (±0.2) | `[-0.8, -0.9, -1.0, -1.2, -0.8]` | `+0.139` | `0.38%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.30 | ⚪ **CASH** | **-1.1 bps** (±0.3) | `[-1.0, -0.6, -0.7, -0.9, -1.5]` | `-0.047` | `0.55%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 11:02:17 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,633.28 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.3, -0.3, +0.0, -0.4, -0.3]` | `-0.025` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,683.81 | ⚪ **CASH** | **-1.0 bps** (±0.2) | `[-0.8, -0.9, -1.0, -1.2, -0.8]` | `+0.139` | `0.38%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.42 | ⚪ **CASH** | **-1.1 bps** (±0.3) | `[-1.0, -0.6, -0.7, -0.9, -1.5]` | `-0.047` | `0.55%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 10:47:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,620.00 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.3, -0.3, +0.0, -0.4, -0.1]` | `-0.039` | `0.36%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,683.41 | ⚪ **CASH** | **-1.3 bps** (±0.2) | `[-1.1, -1.1, -1.1, -1.6, -1.1]` | `+0.064` | `0.39%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.50 | ⚪ **CASH** | **-1.2 bps** (±0.2) | `[-0.9, -0.9, -1.2, -1.2, -1.3]` | `-0.068` | `0.56%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 10:32:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,615.44 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.3, -0.3, +0.0, -0.4, -0.1]` | `-0.039` | `0.36%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,684.02 | ⚪ **CASH** | **-1.3 bps** (±0.2) | `[-1.1, -1.1, -1.1, -1.6, -1.1]` | `+0.064` | `0.39%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.51 | ⚪ **CASH** | **-1.2 bps** (±0.2) | `[-0.9, -0.9, -1.2, -1.2, -1.3]` | `-0.068` | `0.56%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 10:17:02 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,580.75 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.3, -0.3, +0.0, -0.4, -0.1]` | `-0.039` | `0.36%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,681.38 | ⚪ **CASH** | **-1.3 bps** (±0.2) | `[-1.1, -1.1, -1.1, -1.6, -1.1]` | `+0.064` | `0.39%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.39 | ⚪ **CASH** | **-1.2 bps** (±0.2) | `[-0.9, -0.9, -1.2, -1.2, -1.3]` | `-0.068` | `0.56%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 10:02:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,592.57 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.3, -0.3, +0.0, -0.4, -0.1]` | `-0.039` | `0.36%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,680.39 | ⚪ **CASH** | **-1.3 bps** (±0.2) | `[-1.1, -1.1, -1.1, -1.6, -1.1]` | `+0.064` | `0.39%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.31 | ⚪ **CASH** | **-1.2 bps** (±0.2) | `[-0.9, -0.9, -1.2, -1.2, -1.3]` | `-0.068` | `0.56%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 09:47:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,590.06 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.3, -0.3, +0.0, -0.4, -0.1]` | `+0.008` | `0.37%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,682.14 | ⚪ **CASH** | **-1.2 bps** (±0.3) | `[-0.8, -0.9, -1.0, -1.7, -1.0]` | `+0.077` | `0.40%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.34 | ⚪ **CASH** | **-1.6 bps** (±0.2) | `[-1.3, -1.9, -1.6, -1.2, -1.3]` | `-0.031` | `0.57%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 09:32:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,591.42 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.3, -0.3, +0.0, -0.4, -0.1]` | `+0.008` | `0.37%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,685.02 | ⚪ **CASH** | **-1.2 bps** (±0.3) | `[-0.8, -0.9, -1.0, -1.7, -1.0]` | `+0.077` | `0.40%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.21 | ⚪ **CASH** | **-1.6 bps** (±0.2) | `[-1.3, -1.9, -1.6, -1.2, -1.3]` | `-0.031` | `0.57%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 09:17:17 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,615.58 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.3, -0.3, +0.0, -0.4, -0.1]` | `+0.008` | `0.37%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,685.32 | ⚪ **CASH** | **-1.2 bps** (±0.3) | `[-0.8, -0.9, -1.0, -1.7, -1.0]` | `+0.077` | `0.40%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.39 | ⚪ **CASH** | **-1.6 bps** (±0.2) | `[-1.3, -1.9, -1.6, -1.2, -1.3]` | `-0.031` | `0.57%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 09:02:07 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,624.68 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.3, -0.3, +0.0, -0.4, -0.1]` | `+0.008` | `0.37%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,683.68 | ⚪ **CASH** | **-1.2 bps** (±0.3) | `[-0.8, -0.9, -1.0, -1.7, -1.0]` | `+0.077` | `0.40%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.28 | ⚪ **CASH** | **-1.6 bps** (±0.2) | `[-1.3, -1.9, -1.6, -1.2, -1.3]` | `-0.031` | `0.57%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 08:46:56 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,641.89 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.4, -0.3, +0.0, -0.4, -0.1]` | `+0.026` | `0.37%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,682.89 | ⚪ **CASH** | **-1.4 bps** (±0.2) | `[-1.0, -1.0, -1.1, -1.7, -1.3]` | `+0.018` | `0.40%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.27 | ⚪ **CASH** | **-1.5 bps** (±0.2) | `[-1.6, -1.1, -1.4, -1.6, -1.5]` | `-0.035` | `0.57%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 08:32:10 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,579.19 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.4, -0.3, +0.0, -0.4, -0.1]` | `+0.026` | `0.37%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,679.96 | ⚪ **CASH** | **-1.4 bps** (±0.2) | `[-1.0, -1.0, -1.1, -1.7, -1.3]` | `+0.018` | `0.40%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.18 | ⚪ **CASH** | **-1.5 bps** (±0.2) | `[-1.6, -1.1, -1.4, -1.6, -1.5]` | `-0.035` | `0.57%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 08:17:19 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,624.00 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.4, -0.3, +0.0, -0.4, -0.1]` | `+0.026` | `0.37%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,681.12 | ⚪ **CASH** | **-1.4 bps** (±0.2) | `[-1.0, -1.0, -1.1, -1.7, -1.3]` | `+0.018` | `0.40%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.39 | ⚪ **CASH** | **-1.5 bps** (±0.2) | `[-1.6, -1.1, -1.4, -1.6, -1.5]` | `-0.035` | `0.57%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 08:02:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,594.00 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.4, -0.3, +0.0, -0.4, -0.1]` | `+0.026` | `0.37%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,681.30 | ⚪ **CASH** | **-1.4 bps** (±0.2) | `[-1.0, -1.0, -1.1, -1.7, -1.3]` | `+0.018` | `0.40%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.28 | ⚪ **CASH** | **-1.5 bps** (±0.2) | `[-1.6, -1.1, -1.4, -1.6, -1.5]` | `-0.035` | `0.57%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 07:47:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,585.99 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.4, -0.3, +0.0, -0.4, -0.1]` | `+0.081` | `0.38%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,681.86 | ⚪ **CASH** | **-1.5 bps** (±0.3) | `[-1.1, -1.1, -1.1, -1.9, -1.3]` | `+0.057` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.27 | ⚪ **CASH** | **-1.1 bps** (±0.2) | `[-0.9, -0.9, -0.9, -1.2, -1.3]` | `+0.023` | `0.58%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 07:32:02 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,639.99 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.4, -0.3, +0.0, -0.4, -0.1]` | `+0.081` | `0.38%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,682.12 | ⚪ **CASH** | **-1.5 bps** (±0.3) | `[-1.1, -1.1, -1.1, -1.9, -1.3]` | `+0.057` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.31 | ⚪ **CASH** | **-1.1 bps** (±0.2) | `[-0.9, -0.9, -0.9, -1.2, -1.3]` | `+0.023` | `0.58%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 07:17:15 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,602.01 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.4, -0.3, +0.0, -0.4, -0.1]` | `+0.081` | `0.38%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,682.05 | ⚪ **CASH** | **-1.5 bps** (±0.3) | `[-1.1, -1.1, -1.1, -1.9, -1.3]` | `+0.057` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.54 | ⚪ **CASH** | **-1.1 bps** (±0.2) | `[-0.9, -0.9, -0.9, -1.2, -1.3]` | `+0.023` | `0.58%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 07:02:28 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,586.01 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.4, -0.3, +0.0, -0.4, -0.1]` | `+0.081` | `0.38%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,680.00 | ⚪ **CASH** | **-1.5 bps** (±0.3) | `[-1.1, -1.1, -1.1, -1.9, -1.3]` | `+0.057` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.36 | ⚪ **CASH** | **-1.1 bps** (±0.2) | `[-0.9, -0.9, -0.9, -1.2, -1.3]` | `+0.023` | `0.58%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 06:47:20 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,632.01 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.4, -0.3, -0.1, -0.4, -0.1]` | `+0.094` | `0.38%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,678.28 | ⚪ **CASH** | **-1.4 bps** (±0.2) | `[-1.4, -1.1, -1.2, -1.6, -1.1]` | `+0.088` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.53 | ⚪ **CASH** | **-0.9 bps** (±0.3) | `[-0.7, -0.4, -0.7, -0.5, -1.3]` | `+0.052` | `0.59%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 06:32:31 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,652.02 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.4, -0.3, -0.1, -0.4, -0.1]` | `+0.094` | `0.38%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,679.04 | ⚪ **CASH** | **-1.4 bps** (±0.2) | `[-1.4, -1.1, -1.2, -1.6, -1.1]` | `+0.088` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.79 | ⚪ **CASH** | **-0.9 bps** (±0.3) | `[-0.7, -0.4, -0.7, -0.5, -1.3]` | `+0.052` | `0.59%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 06:16:55 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,634.77 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.4, -0.3, -0.1, -0.4, -0.1]` | `+0.094` | `0.38%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,676.43 | ⚪ **CASH** | **-1.4 bps** (±0.2) | `[-1.4, -1.1, -1.2, -1.6, -1.1]` | `+0.088` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.49 | ⚪ **CASH** | **-0.9 bps** (±0.3) | `[-0.7, -0.4, -0.7, -0.5, -1.3]` | `+0.052` | `0.59%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 06:02:12 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,674.01 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.4, -0.3, -0.1, -0.4, -0.1]` | `+0.094` | `0.38%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,679.06 | ⚪ **CASH** | **-1.4 bps** (±0.2) | `[-1.4, -1.1, -1.2, -1.6, -1.1]` | `+0.088` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.75 | ⚪ **CASH** | **-0.9 bps** (±0.3) | `[-0.7, -0.4, -0.7, -0.5, -1.3]` | `+0.052` | `0.59%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 05:47:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,637.44 | ⚪ **CASH** | **-0.0 bps** (±0.1) | `[-0.1, +0.1, +0.2, +0.0, +0.1]` | `+0.025` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,676.97 | ⚪ **CASH** | **-1.1 bps** (±0.2) | `[-0.9, -1.1, -0.7, -1.0, -1.2]` | `+0.036` | `0.42%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.59 | ⚪ **CASH** | **-1.8 bps** (±0.2) | `[-1.7, -2.0, -1.6, -1.6, -1.5]` | `+0.077` | `0.60%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 05:32:20 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,634.39 | ⚪ **CASH** | **-0.0 bps** (±0.1) | `[-0.1, +0.1, +0.2, +0.0, +0.1]` | `+0.025` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,678.03 | ⚪ **CASH** | **-1.1 bps** (±0.2) | `[-0.9, -1.1, -0.7, -1.0, -1.2]` | `+0.036` | `0.42%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.61 | ⚪ **CASH** | **-1.8 bps** (±0.2) | `[-1.7, -2.0, -1.6, -1.6, -1.5]` | `+0.077` | `0.60%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 05:17:00 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,570.19 | ⚪ **CASH** | **-0.0 bps** (±0.1) | `[-0.1, +0.1, +0.2, +0.0, +0.1]` | `+0.025` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,676.20 | ⚪ **CASH** | **-1.1 bps** (±0.2) | `[-0.9, -1.1, -0.7, -1.0, -1.2]` | `+0.036` | `0.42%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.34 | ⚪ **CASH** | **-1.8 bps** (±0.2) | `[-1.7, -2.0, -1.6, -1.6, -1.5]` | `+0.077` | `0.60%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 05:02:32 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,557.56 | ⚪ **CASH** | **-0.0 bps** (±0.1) | `[-0.1, +0.1, +0.2, +0.0, +0.1]` | `+0.025` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,674.20 | ⚪ **CASH** | **-1.1 bps** (±0.2) | `[-0.9, -1.1, -0.7, -1.0, -1.2]` | `+0.036` | `0.42%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.11 | ⚪ **CASH** | **-1.8 bps** (±0.2) | `[-1.7, -2.0, -1.6, -1.6, -1.5]` | `+0.077` | `0.60%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 04:47:28 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,572.33 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.4, -0.3, -0.1, -0.4, -0.1]` | `+0.072` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,675.76 | ⚪ **CASH** | **-1.2 bps** (±0.2) | `[-1.3, -0.9, -1.0, -1.4, -1.1]` | `+0.089` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.19 | ⚪ **CASH** | **-1.6 bps** (±0.2) | `[-1.7, -1.5, -1.1, -1.6, -1.5]` | `+0.058` | `0.60%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 04:32:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,544.02 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.4, -0.3, -0.1, -0.4, -0.1]` | `+0.072` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,675.30 | ⚪ **CASH** | **-1.2 bps** (±0.2) | `[-1.3, -0.9, -1.0, -1.4, -1.1]` | `+0.089` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.06 | ⚪ **CASH** | **-1.6 bps** (±0.2) | `[-1.7, -1.5, -1.1, -1.6, -1.5]` | `+0.058` | `0.60%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 04:17:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,609.09 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.4, -0.3, -0.1, -0.4, -0.1]` | `+0.072` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,675.70 | ⚪ **CASH** | **-1.2 bps** (±0.2) | `[-1.3, -0.9, -1.0, -1.4, -1.1]` | `+0.089` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.10 | ⚪ **CASH** | **-1.6 bps** (±0.2) | `[-1.7, -1.5, -1.1, -1.6, -1.5]` | `+0.058` | `0.60%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 04:02:31 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,699.56 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.4, -0.3, -0.1, -0.4, -0.1]` | `+0.072` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,681.70 | ⚪ **CASH** | **-1.2 bps** (±0.2) | `[-1.3, -0.9, -1.0, -1.4, -1.1]` | `+0.089` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.39 | ⚪ **CASH** | **-1.6 bps** (±0.2) | `[-1.7, -1.5, -1.1, -1.6, -1.5]` | `+0.058` | `0.60%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-03 03:47:03 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,655.39 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.4, -0.3, +0.0, -0.4, -0.1]` | `+0.046` | `0.40%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,681.32 | ⚪ **CASH** | **-1.6 bps** (±0.3) | `[-1.4, -1.1, -1.1, -1.9, -1.7]` | `+0.072` | `0.43%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.30 | ⚪ **CASH** | **-1.6 bps** (±0.2) | `[-1.6, -1.9, -1.6, -1.2, -1.3]` | `+0.072` | `0.61%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |
