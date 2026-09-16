# 📋 BOT_TRADE V5 — Livro de Auditoria de Decisões e Análise de Mercado

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o consenso dos 5 modelos XGBoost, o comportamento do CVD (Cumulative Volume Delta) e o disparo de travas de risco.

**Última Atualização**: `2026-09-16 18:17:29 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-09-16 18:17:29 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,893.01 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.020` | `0.36%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,405.47 | ⚪ **CASH** | **-0.6 bps** (±0.1) | `[-0.7, -0.5, -0.6, -0.4, -0.4]` | `-0.004` | `0.51%/h` | `vol_compressed` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.89 | ⚪ **CASH** | **-2.0 bps** (±0.2) | `[-1.9, -2.2, -2.1, -1.6, -1.9]` | `-0.050` | `0.53%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 18:02:39 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,438.04 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.020` | `0.36%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,381.02 | ⚪ **CASH** | **-0.6 bps** (±0.1) | `[-0.7, -0.5, -0.6, -0.4, -0.4]` | `-0.004` | `0.51%/h` | `vol_compressed` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $96.68 | ⚪ **CASH** | **-2.0 bps** (±0.2) | `[-1.9, -2.2, -2.1, -1.6, -1.9]` | `-0.050` | `0.53%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 17:47:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,454.26 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.028` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,376.81 | ⚪ **CASH** | **-0.6 bps** (±0.2) | `[-0.9, -0.6, -0.3, -0.3, -0.3]` | `+0.024` | `0.51%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $96.39 | ⚪ **CASH** | **-2.4 bps** (±0.2) | `[-2.5, -2.4, -2.4, -2.0, -2.0]` | `+0.014` | `0.54%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 17:32:28 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,728.00 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.028` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,388.46 | ⚪ **CASH** | **-0.6 bps** (±0.2) | `[-0.9, -0.6, -0.3, -0.3, -0.3]` | `+0.024` | `0.51%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $96.98 | ⚪ **CASH** | **-2.4 bps** (±0.2) | `[-2.5, -2.4, -2.4, -2.0, -2.0]` | `+0.014` | `0.54%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 17:16:58 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,776.00 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.028` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,392.96 | ⚪ **CASH** | **-0.6 bps** (±0.2) | `[-0.9, -0.6, -0.3, -0.3, -0.3]` | `+0.024` | `0.51%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.28 | ⚪ **CASH** | **-2.4 bps** (±0.2) | `[-2.5, -2.4, -2.4, -2.0, -2.0]` | `+0.014` | `0.54%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 17:02:38 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,756.01 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.028` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,390.62 | ⚪ **CASH** | **-0.6 bps** (±0.2) | `[-0.9, -0.6, -0.3, -0.3, -0.3]` | `+0.024` | `0.51%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.17 | ⚪ **CASH** | **-2.4 bps** (±0.2) | `[-2.5, -2.4, -2.4, -2.0, -2.0]` | `+0.014` | `0.54%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 16:47:09 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,766.00 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.033` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,392.89 | ⚪ **CASH** | **-0.6 bps** (±0.2) | `[-0.9, -0.6, -0.4, -0.3, -0.3]` | `-0.006` | `0.52%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.27 | ⚪ **CASH** | **-2.4 bps** (±0.2) | `[-2.5, -2.4, -2.4, -2.0, -2.0]` | `+0.022` | `0.55%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 16:32:29 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,755.60 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.033` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,393.27 | ⚪ **CASH** | **-0.6 bps** (±0.2) | `[-0.9, -0.6, -0.4, -0.3, -0.3]` | `-0.006` | `0.52%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.17 | ⚪ **CASH** | **-2.4 bps** (±0.2) | `[-2.5, -2.4, -2.4, -2.0, -2.0]` | `+0.022` | `0.55%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 16:17:10 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,782.01 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.033` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,395.01 | ⚪ **CASH** | **-0.6 bps** (±0.2) | `[-0.9, -0.6, -0.4, -0.3, -0.3]` | `-0.006` | `0.52%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.27 | ⚪ **CASH** | **-2.4 bps** (±0.2) | `[-2.5, -2.4, -2.4, -2.0, -2.0]` | `+0.022` | `0.55%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 16:02:35 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,787.18 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.033` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,392.60 | ⚪ **CASH** | **-0.6 bps** (±0.2) | `[-0.9, -0.6, -0.4, -0.3, -0.3]` | `-0.006` | `0.52%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.14 | ⚪ **CASH** | **-2.4 bps** (±0.2) | `[-2.5, -2.4, -2.4, -2.0, -2.0]` | `+0.022` | `0.55%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 15:47:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,818.53 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `-0.010` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,394.58 | ⚪ **CASH** | **-0.7 bps** (±0.2) | `[-0.9, -0.6, -0.5, -0.6, -0.3]` | `-0.022` | `0.53%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.26 | ⚪ **CASH** | **-2.2 bps** (±0.2) | `[-2.1, -2.4, -2.1, -1.8, -2.0]` | `+0.013` | `0.55%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 15:32:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,605.09 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `-0.010` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,385.58 | ⚪ **CASH** | **-0.7 bps** (±0.2) | `[-0.9, -0.6, -0.5, -0.6, -0.3]` | `-0.022` | `0.53%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $96.92 | ⚪ **CASH** | **-2.2 bps** (±0.2) | `[-2.1, -2.4, -2.1, -1.8, -2.0]` | `+0.013` | `0.55%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 15:17:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,665.99 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `-0.010` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,389.96 | ⚪ **CASH** | **-0.7 bps** (±0.2) | `[-0.9, -0.6, -0.5, -0.6, -0.3]` | `-0.022` | `0.53%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.07 | ⚪ **CASH** | **-2.2 bps** (±0.2) | `[-2.1, -2.4, -2.1, -1.8, -2.0]` | `+0.013` | `0.55%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 15:02:09 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,744.00 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `-0.010` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,394.06 | ⚪ **CASH** | **-0.7 bps** (±0.2) | `[-0.9, -0.6, -0.5, -0.6, -0.3]` | `-0.022` | `0.53%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.17 | ⚪ **CASH** | **-2.2 bps** (±0.2) | `[-2.1, -2.4, -2.1, -1.8, -2.0]` | `+0.013` | `0.55%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 14:48:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,680.01 | ⚪ **CASH** | **+0.8 bps** (±0.1) | `[+0.8, +0.8, +0.9, +0.9, +0.9]` | `-0.047` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,388.19 | ⚪ **CASH** | **+0.6 bps** (±0.2) | `[+0.7, +1.0, +0.3, +0.9, +0.5]` | `-0.069` | `0.54%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $96.89 | ⚪ **CASH** | **+0.5 bps** (±0.3) | `[+0.3, +0.9, +0.7, +0.9, +0.3]` | `+0.001` | `0.56%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 14:32:19 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,681.75 | ⚪ **CASH** | **+0.8 bps** (±0.1) | `[+0.8, +0.8, +0.9, +0.9, +0.9]` | `-0.047` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,391.18 | ⚪ **CASH** | **+0.6 bps** (±0.2) | `[+0.7, +1.0, +0.3, +0.9, +0.5]` | `-0.069` | `0.54%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $96.96 | ⚪ **CASH** | **+0.5 bps** (±0.3) | `[+0.3, +0.9, +0.7, +0.9, +0.3]` | `+0.001` | `0.56%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 14:17:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,714.39 | ⚪ **CASH** | **+0.8 bps** (±0.1) | `[+0.8, +0.8, +0.9, +0.9, +0.9]` | `-0.047` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,396.47 | ⚪ **CASH** | **+0.6 bps** (±0.2) | `[+0.7, +1.0, +0.3, +0.9, +0.5]` | `-0.069` | `0.54%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.17 | ⚪ **CASH** | **+0.5 bps** (±0.3) | `[+0.3, +0.9, +0.7, +0.9, +0.3]` | `+0.001` | `0.56%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 14:02:12 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,562.77 | ⚪ **CASH** | **+0.8 bps** (±0.1) | `[+0.8, +0.8, +0.9, +0.9, +0.9]` | `-0.047` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,390.01 | ⚪ **CASH** | **+0.6 bps** (±0.2) | `[+0.7, +1.0, +0.3, +0.9, +0.5]` | `-0.069` | `0.54%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.04 | ⚪ **CASH** | **+0.5 bps** (±0.3) | `[+0.3, +0.9, +0.7, +0.9, +0.3]` | `+0.001` | `0.56%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 13:47:15 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,723.45 | ⚪ **CASH** | **+0.8 bps** (±0.1) | `[+0.8, +0.8, +0.8, +0.8, +0.9]` | `-0.076` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,395.89 | ⚪ **CASH** | **+0.8 bps** (±0.4) | `[+1.3, +1.2, +0.3, +0.9, +1.4]` | `-0.050` | `0.54%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.26 | ⚪ **CASH** | **+0.3 bps** (±0.3) | `[+0.3, +0.9, +0.1, +0.9, +0.3]` | `+0.019` | `0.57%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 13:32:07 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,750.01 | ⚪ **CASH** | **+0.8 bps** (±0.1) | `[+0.8, +0.8, +0.8, +0.8, +0.9]` | `-0.076` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,400.58 | ⚪ **CASH** | **+0.8 bps** (±0.4) | `[+1.3, +1.2, +0.3, +0.9, +1.4]` | `-0.050` | `0.54%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.33 | ⚪ **CASH** | **+0.3 bps** (±0.3) | `[+0.3, +0.9, +0.1, +0.9, +0.3]` | `+0.019` | `0.57%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 13:17:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,822.01 | ⚪ **CASH** | **+0.8 bps** (±0.1) | `[+0.8, +0.8, +0.8, +0.8, +0.9]` | `-0.076` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,403.35 | ⚪ **CASH** | **+0.8 bps** (±0.4) | `[+1.3, +1.2, +0.3, +0.9, +1.4]` | `-0.050` | `0.54%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.34 | ⚪ **CASH** | **+0.3 bps** (±0.3) | `[+0.3, +0.9, +0.1, +0.9, +0.3]` | `+0.019` | `0.57%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 13:02:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,819.23 | ⚪ **CASH** | **+0.8 bps** (±0.1) | `[+0.8, +0.8, +0.8, +0.8, +0.9]` | `-0.076` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,402.38 | ⚪ **CASH** | **+0.8 bps** (±0.4) | `[+1.3, +1.2, +0.3, +0.9, +1.4]` | `-0.050` | `0.54%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.35 | ⚪ **CASH** | **+0.3 bps** (±0.3) | `[+0.3, +0.9, +0.1, +0.9, +0.3]` | `+0.019` | `0.57%/h` | `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 12:47:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,995.00 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `-0.063` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,407.57 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.1, -0.4, -0.4, -0.1, -0.1]` | `-0.061` | `0.53%/h` | `vol_compressed` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.51 | ⚪ **CASH** | **-2.2 bps** (±0.2) | `[-2.4, -2.2, -1.7, -2.0, -1.9]` | `+0.059` | `0.57%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 12:32:28 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,819.55 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `-0.063` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,403.98 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.1, -0.4, -0.4, -0.1, -0.1]` | `-0.061` | `0.53%/h` | `vol_compressed` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.27 | ⚪ **CASH** | **-2.2 bps** (±0.2) | `[-2.4, -2.2, -1.7, -2.0, -1.9]` | `+0.059` | `0.57%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 12:17:09 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,132.00 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `-0.063` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,415.00 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.1, -0.4, -0.4, -0.1, -0.1]` | `-0.061` | `0.53%/h` | `vol_compressed` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.85 | ⚪ **CASH** | **-2.2 bps** (±0.2) | `[-2.4, -2.2, -1.7, -2.0, -1.9]` | `+0.059` | `0.57%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 12:02:28 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,238.01 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `-0.063` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,421.18 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.1, -0.4, -0.4, -0.1, -0.1]` | `-0.061` | `0.53%/h` | `vol_compressed` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $98.00 | ⚪ **CASH** | **-2.2 bps** (±0.2) | `[-2.4, -2.2, -1.7, -2.0, -1.9]` | `+0.059` | `0.57%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 11:47:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,201.89 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `-0.064` | `0.38%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,423.02 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.1, -0.4, -0.4, -0.1, -0.2]` | `-0.121` | `0.53%/h` | `vol_compressed` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $98.02 | ⚪ **CASH** | **-2.5 bps** (±0.3) | `[-2.7, -2.7, -2.4, -2.0, -2.0]` | `+0.007` | `0.56%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 11:32:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,032.00 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `-0.064` | `0.38%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,411.80 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.1, -0.4, -0.4, -0.1, -0.2]` | `-0.121` | `0.53%/h` | `vol_compressed` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.49 | ⚪ **CASH** | **-2.5 bps** (±0.3) | `[-2.7, -2.7, -2.4, -2.0, -2.0]` | `+0.007` | `0.56%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 11:17:18 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,936.01 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `-0.064` | `0.38%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,405.11 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.1, -0.4, -0.4, -0.1, -0.2]` | `-0.121` | `0.53%/h` | `vol_compressed` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.14 | ⚪ **CASH** | **-2.5 bps** (±0.3) | `[-2.7, -2.7, -2.4, -2.0, -2.0]` | `+0.007` | `0.56%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 11:02:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,958.00 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `-0.064` | `0.38%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,406.66 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.1, -0.4, -0.4, -0.1, -0.2]` | `-0.121` | `0.53%/h` | `vol_compressed` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.28 | ⚪ **CASH** | **-2.5 bps** (±0.3) | `[-2.7, -2.7, -2.4, -2.0, -2.0]` | `+0.007` | `0.56%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 10:47:00 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,973.28 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `-0.059` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,406.23 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.1, -0.4, -0.4, -0.1, -0.2]` | `-0.109` | `0.53%/h` | `vol_compressed` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.33 | ⚪ **CASH** | **-2.2 bps** (±0.3) | `[-2.3, -2.6, -2.1, -1.6, -1.9]` | `+0.020` | `0.57%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 10:32:32 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,950.01 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `-0.059` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,402.00 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.1, -0.4, -0.4, -0.1, -0.2]` | `-0.109` | `0.53%/h` | `vol_compressed` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.33 | ⚪ **CASH** | **-2.2 bps** (±0.3) | `[-2.3, -2.6, -2.1, -1.6, -1.9]` | `+0.020` | `0.57%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 10:16:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,957.99 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `-0.059` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,400.44 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.1, -0.4, -0.4, -0.1, -0.2]` | `-0.109` | `0.53%/h` | `vol_compressed` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.19 | ⚪ **CASH** | **-2.2 bps** (±0.3) | `[-2.3, -2.6, -2.1, -1.6, -1.9]` | `+0.020` | `0.57%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 10:02:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,034.01 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `-0.059` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,405.17 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.1, -0.4, -0.4, -0.1, -0.2]` | `-0.109` | `0.53%/h` | `vol_compressed` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.35 | ⚪ **CASH** | **-2.2 bps** (±0.3) | `[-2.3, -2.6, -2.1, -1.6, -1.9]` | `+0.020` | `0.57%/h` | `vol_compressed` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 09:48:12 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,916.00 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `-0.048` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,402.46 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.4, -0.4, -0.3, -0.1, -0.2]` | `-0.128` | `0.54%/h` | `vol_compressed` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.22 | ⚪ **CASH** | **-2.1 bps** (±0.2) | `[-2.1, -2.2, -2.1, -1.6, -1.9]` | `+0.047` | `0.58%/h` | `vol_compressed` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-16 09:32:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,850.00 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `-0.048` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,402.48 | ⚪ **CASH** | **-0.3 bps** (±0.1) | `[-0.4, -0.4, -0.3, -0.1, -0.2]` | `-0.128` | `0.54%/h` | `vol_compressed` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $97.17 | ⚪ **CASH** | **-2.1 bps** (±0.2) | `[-2.1, -2.2, -2.1, -1.6, -1.9]` | `+0.047` | `0.58%/h` | `vol_compressed` `alt_downtrend` | Aguardando sinal com assimetria |
