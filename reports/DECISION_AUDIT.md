# 📋 BOT_TRADE V5 — Livro de Auditoria de Decisões e Análise de Mercado

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o consenso dos 5 modelos XGBoost, o comportamento do CVD (Cumulative Volume Delta) e o disparo de travas de risco.

**Última Atualização**: `2026-09-28 10:02:14 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-09-28 10:02:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,744.92 | ⚪ **CASH** | **+0.6 bps** (±0.4) | `[+0.2, +1.2, +0.8, +0.6, +1.2]` | `-0.057` | `0.24%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,646.41 | ⚪ **CASH** | **-1.0 bps** (±0.1) | `[-1.1, -0.8, -1.0, -0.9, -0.9]` | `-0.047` | `0.27%/h` | `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.10 | ⚪ **CASH** | **+0.0 bps** (±0.3) | `[+0.1, +0.4, +0.2, -0.4, +0.7]` | `+0.006` | `0.58%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 09:46:58 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,664.88 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.038` | `0.24%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,639.43 | ⚪ **CASH** | **-1.7 bps** (±0.2) | `[-1.8, -1.3, -1.4, -1.9, -1.6]` | `-0.050` | `0.27%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.71 | ⚪ **CASH** | **-1.8 bps** (±0.4) | `[-1.1, -2.2, -1.9, -1.6, -1.3]` | `+0.025` | `0.58%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 09:32:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,824.00 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.038` | `0.24%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,647.05 | ⚪ **CASH** | **-1.7 bps** (±0.2) | `[-1.8, -1.3, -1.4, -1.9, -1.6]` | `-0.050` | `0.27%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.06 | ⚪ **CASH** | **-1.8 bps** (±0.4) | `[-1.1, -2.2, -1.9, -1.6, -1.3]` | `+0.025` | `0.58%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 09:17:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,829.95 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.038` | `0.24%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,648.73 | ⚪ **CASH** | **-1.7 bps** (±0.2) | `[-1.8, -1.3, -1.4, -1.9, -1.6]` | `-0.050` | `0.27%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.35 | ⚪ **CASH** | **-1.8 bps** (±0.4) | `[-1.1, -2.2, -1.9, -1.6, -1.3]` | `+0.025` | `0.58%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 09:02:20 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,914.01 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.038` | `0.24%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,650.21 | ⚪ **CASH** | **-1.7 bps** (±0.2) | `[-1.8, -1.3, -1.4, -1.9, -1.6]` | `-0.050` | `0.27%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.22 | ⚪ **CASH** | **-1.8 bps** (±0.4) | `[-1.1, -2.2, -1.9, -1.6, -1.3]` | `+0.025` | `0.58%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 08:47:22 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,972.38 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.2, +0.1, +0.0, +0.0, -0.1]` | `-0.147` | `0.24%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,645.78 | ⚪ **CASH** | **-1.2 bps** (±0.3) | `[-0.7, -1.1, -1.0, -1.2, -1.4]` | `-0.198` | `0.28%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.29 | ⚪ **CASH** | **-1.0 bps** (±0.3) | `[-0.7, -0.9, -1.0, -0.5, -1.3]` | `+0.026` | `0.59%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 08:32:20 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,904.05 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.2, +0.1, +0.0, +0.0, -0.1]` | `-0.147` | `0.24%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,649.65 | ⚪ **CASH** | **-1.2 bps** (±0.3) | `[-0.7, -1.1, -1.0, -1.2, -1.4]` | `-0.198` | `0.28%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.39 | ⚪ **CASH** | **-1.0 bps** (±0.3) | `[-0.7, -0.9, -1.0, -0.5, -1.3]` | `+0.026` | `0.59%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 08:17:02 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,069.71 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.2, +0.1, +0.0, +0.0, -0.1]` | `-0.147` | `0.24%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,652.52 | ⚪ **CASH** | **-1.2 bps** (±0.3) | `[-0.7, -1.1, -1.0, -1.2, -1.4]` | `-0.198` | `0.28%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.60 | ⚪ **CASH** | **-1.0 bps** (±0.3) | `[-0.7, -0.9, -1.0, -0.5, -1.3]` | `+0.026` | `0.59%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 08:02:18 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,093.88 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.2, +0.1, +0.0, +0.0, -0.1]` | `-0.147` | `0.24%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,648.23 | ⚪ **CASH** | **-1.2 bps** (±0.3) | `[-0.7, -1.1, -1.0, -1.2, -1.4]` | `-0.198` | `0.28%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.41 | ⚪ **CASH** | **-1.0 bps** (±0.3) | `[-0.7, -0.9, -1.0, -0.5, -1.3]` | `+0.026` | `0.59%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 07:46:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,955.47 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.212` | `0.24%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,644.48 | ⚪ **CASH** | **-1.8 bps** (±0.4) | `[-1.5, -1.2, -1.3, -2.2, -2.0]` | `-0.249` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.19 | ⚪ **CASH** | **-2.0 bps** (±0.1) | `[-2.0, -1.8, -1.7, -2.0, -2.0]` | `-0.004` | `0.59%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 07:32:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,968.00 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.212` | `0.24%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,643.76 | ⚪ **CASH** | **-1.8 bps** (±0.4) | `[-1.5, -1.2, -1.3, -2.2, -2.0]` | `-0.249` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.15 | ⚪ **CASH** | **-2.0 bps** (±0.1) | `[-2.0, -1.8, -1.7, -2.0, -2.0]` | `-0.004` | `0.59%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 07:17:09 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,150.00 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.212` | `0.24%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,651.15 | ⚪ **CASH** | **-1.8 bps** (±0.4) | `[-1.5, -1.2, -1.3, -2.2, -2.0]` | `-0.249` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.72 | ⚪ **CASH** | **-2.0 bps** (±0.1) | `[-2.0, -1.8, -1.7, -2.0, -2.0]` | `-0.004` | `0.59%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 07:02:09 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,253.48 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.212` | `0.24%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,655.51 | ⚪ **CASH** | **-1.8 bps** (±0.4) | `[-1.5, -1.2, -1.3, -2.2, -2.0]` | `-0.249` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.08 | ⚪ **CASH** | **-2.0 bps** (±0.1) | `[-2.0, -1.8, -1.7, -2.0, -2.0]` | `-0.004` | `0.59%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 06:47:23 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,174.00 | ⚪ **CASH** | **+0.7 bps** (±0.4) | `[+0.2, +1.2, +0.8, +1.0, +1.2]` | `-0.197` | `0.25%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,650.50 | ⚪ **CASH** | **-0.8 bps** (±0.1) | `[-0.8, -0.7, -0.8, -0.9, -0.9]` | `-0.243` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.78 | ⚪ **CASH** | **+0.5 bps** (±0.7) | `[+0.4, +2.3, +0.5, +0.8, +0.3]` | `-0.013` | `0.60%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 06:32:02 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,128.01 | ⚪ **CASH** | **+0.7 bps** (±0.4) | `[+0.2, +1.2, +0.8, +1.0, +1.2]` | `-0.197` | `0.25%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,649.68 | ⚪ **CASH** | **-0.8 bps** (±0.1) | `[-0.8, -0.7, -0.8, -0.9, -0.9]` | `-0.243` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.59 | ⚪ **CASH** | **+0.5 bps** (±0.7) | `[+0.4, +2.3, +0.5, +0.8, +0.3]` | `-0.013` | `0.60%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 06:17:12 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,238.22 | ⚪ **CASH** | **+0.7 bps** (±0.4) | `[+0.2, +1.2, +0.8, +1.0, +1.2]` | `-0.197` | `0.25%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,653.23 | ⚪ **CASH** | **-0.8 bps** (±0.1) | `[-0.8, -0.7, -0.8, -0.9, -0.9]` | `-0.243` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.16 | ⚪ **CASH** | **+0.5 bps** (±0.7) | `[+0.4, +2.3, +0.5, +0.8, +0.3]` | `-0.013` | `0.60%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 06:02:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,150.55 | ⚪ **CASH** | **+0.7 bps** (±0.4) | `[+0.2, +1.2, +0.8, +1.0, +1.2]` | `-0.197` | `0.25%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,649.44 | ⚪ **CASH** | **-0.8 bps** (±0.1) | `[-0.8, -0.7, -0.8, -0.9, -0.9]` | `-0.243` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.04 | ⚪ **CASH** | **+0.5 bps** (±0.7) | `[+0.4, +2.3, +0.5, +0.8, +0.3]` | `-0.013` | `0.60%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 05:46:57 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,150.01 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.3, -0.4, -0.3]` | `-0.137` | `0.24%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,652.17 | ⚪ **CASH** | **-1.6 bps** (±0.3) | `[-1.5, -1.2, -1.2, -1.9, -1.6]` | `-0.202` | `0.28%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.13 | ⚪ **CASH** | **-1.3 bps** (±0.5) | `[-1.3, -0.1, -1.0, -1.2, -1.6]` | `-0.004` | `0.59%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 05:32:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,050.00 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.3, -0.4, -0.3]` | `-0.137` | `0.24%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,645.18 | ⚪ **CASH** | **-1.6 bps** (±0.3) | `[-1.5, -1.2, -1.2, -1.9, -1.6]` | `-0.202` | `0.28%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.91 | ⚪ **CASH** | **-1.3 bps** (±0.5) | `[-1.3, -0.1, -1.0, -1.2, -1.6]` | `-0.004` | `0.59%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 05:17:22 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,248.01 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.3, -0.4, -0.3]` | `-0.137` | `0.24%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,649.55 | ⚪ **CASH** | **-1.6 bps** (±0.3) | `[-1.5, -1.2, -1.2, -1.9, -1.6]` | `-0.202` | `0.28%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.40 | ⚪ **CASH** | **-1.3 bps** (±0.5) | `[-1.3, -0.1, -1.0, -1.2, -1.6]` | `-0.004` | `0.59%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 05:02:12 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,496.69 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.3, -0.4, -0.3]` | `-0.137` | `0.24%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,658.93 | ⚪ **CASH** | **-1.6 bps** (±0.3) | `[-1.5, -1.2, -1.2, -1.9, -1.6]` | `-0.202` | `0.28%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $120.02 | ⚪ **CASH** | **-1.3 bps** (±0.5) | `[-1.3, -0.1, -1.0, -1.2, -1.6]` | `-0.004` | `0.59%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 04:47:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,470.10 | ⚪ **CASH** | **+0.2 bps** (±0.4) | `[-0.2, +0.7, +0.3, +0.4, +0.8]` | `-0.183` | `0.24%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,657.91 | ⚪ **CASH** | **-1.7 bps** (±0.3) | `[-1.5, -1.2, -1.3, -2.0, -2.0]` | `-0.218` | `0.28%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.95 | ⚪ **CASH** | **-1.0 bps** (±0.5) | `[-0.9, +0.1, -0.7, -0.8, -1.4]` | `-0.049` | `0.60%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 04:32:20 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,462.01 | ⚪ **CASH** | **+0.2 bps** (±0.4) | `[-0.2, +0.7, +0.3, +0.4, +0.8]` | `-0.183` | `0.24%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,658.01 | ⚪ **CASH** | **-1.7 bps** (±0.3) | `[-1.5, -1.2, -1.3, -2.0, -2.0]` | `-0.218` | `0.28%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.90 | ⚪ **CASH** | **-1.0 bps** (±0.5) | `[-0.9, +0.1, -0.7, -0.8, -1.4]` | `-0.049` | `0.60%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 04:16:55 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,376.01 | ⚪ **CASH** | **+0.2 bps** (±0.4) | `[-0.2, +0.7, +0.3, +0.4, +0.8]` | `-0.183` | `0.24%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,653.15 | ⚪ **CASH** | **-1.7 bps** (±0.3) | `[-1.5, -1.2, -1.3, -2.0, -2.0]` | `-0.218` | `0.28%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.60 | ⚪ **CASH** | **-1.0 bps** (±0.5) | `[-0.9, +0.1, -0.7, -0.8, -1.4]` | `-0.049` | `0.60%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 04:02:22 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,259.78 | ⚪ **CASH** | **+0.2 bps** (±0.4) | `[-0.2, +0.7, +0.3, +0.4, +0.8]` | `-0.183` | `0.24%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,649.09 | ⚪ **CASH** | **-1.7 bps** (±0.3) | `[-1.5, -1.2, -1.3, -2.0, -2.0]` | `-0.218` | `0.28%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.46 | ⚪ **CASH** | **-1.0 bps** (±0.5) | `[-0.9, +0.1, -0.7, -0.8, -1.4]` | `-0.049` | `0.60%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 03:47:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,424.48 | ⚪ **CASH** | **+0.3 bps** (±0.3) | `[+0.2, +0.6, +0.5, +0.1, +0.8]` | `-0.167` | `0.25%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,652.42 | ⚪ **CASH** | **-0.9 bps** (±0.1) | `[-0.8, -0.7, -1.0, -0.9, -0.7]` | `-0.231` | `0.29%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $120.15 | ⚪ **CASH** | **+0.9 bps** (±0.5) | `[+0.8, +2.2, +0.9, +1.3, +0.6]` | `-0.042` | `0.61%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 03:32:07 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,276.00 | ⚪ **CASH** | **+0.3 bps** (±0.3) | `[+0.2, +0.6, +0.5, +0.1, +0.8]` | `-0.167` | `0.25%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,647.30 | ⚪ **CASH** | **-0.9 bps** (±0.1) | `[-0.8, -0.7, -1.0, -0.9, -0.7]` | `-0.231` | `0.29%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $119.74 | ⚪ **CASH** | **+0.9 bps** (±0.5) | `[+0.8, +2.2, +0.9, +1.3, +0.6]` | `-0.042` | `0.61%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 03:17:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,460.55 | ⚪ **CASH** | **+0.3 bps** (±0.3) | `[+0.2, +0.6, +0.5, +0.1, +0.8]` | `-0.167` | `0.25%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,656.40 | ⚪ **CASH** | **-0.9 bps** (±0.1) | `[-0.8, -0.7, -1.0, -0.9, -0.7]` | `-0.231` | `0.29%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $120.34 | ⚪ **CASH** | **+0.9 bps** (±0.5) | `[+0.8, +2.2, +0.9, +1.3, +0.6]` | `-0.042` | `0.61%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 03:02:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,500.01 | ⚪ **CASH** | **+0.3 bps** (±0.3) | `[+0.2, +0.6, +0.5, +0.1, +0.8]` | `-0.167` | `0.25%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,655.43 | ⚪ **CASH** | **-0.9 bps** (±0.1) | `[-0.8, -0.7, -1.0, -0.9, -0.7]` | `-0.231` | `0.29%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $120.27 | ⚪ **CASH** | **+0.9 bps** (±0.5) | `[+0.8, +2.2, +0.9, +1.3, +0.6]` | `-0.042` | `0.61%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 02:46:56 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,441.32 | ⚪ **CASH** | **+1.0 bps** (±0.3) | `[+0.9, +1.1, +1.0, +0.8, +1.7]` | `-0.116` | `0.24%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,652.28 | ⚪ **CASH** | **-0.1 bps** (±0.3) | `[+0.2, +0.3, -0.3, +0.0, -0.3]` | `-0.215` | `0.29%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $120.15 | ⚪ **CASH** | **+2.4 bps** (±0.5) | `[+2.1, +3.6, +2.7, +2.5, +2.4]` | `-0.067` | `0.61%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 02:32:15 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,559.94 | ⚪ **CASH** | **+1.0 bps** (±0.3) | `[+0.9, +1.1, +1.0, +0.8, +1.7]` | `-0.116` | `0.24%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,652.78 | ⚪ **CASH** | **-0.1 bps** (±0.3) | `[+0.2, +0.3, -0.3, +0.0, -0.3]` | `-0.215` | `0.29%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $120.57 | ⚪ **CASH** | **+2.4 bps** (±0.5) | `[+2.1, +3.6, +2.7, +2.5, +2.4]` | `-0.067` | `0.61%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 02:16:57 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,718.67 | ⚪ **CASH** | **+1.0 bps** (±0.3) | `[+0.9, +1.1, +1.0, +0.8, +1.7]` | `-0.116` | `0.24%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,659.09 | ⚪ **CASH** | **-0.1 bps** (±0.3) | `[+0.2, +0.3, -0.3, +0.0, -0.3]` | `-0.215` | `0.29%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $121.01 | ⚪ **CASH** | **+2.4 bps** (±0.5) | `[+2.1, +3.6, +2.7, +2.5, +2.4]` | `-0.067` | `0.61%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 02:02:30 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,550.01 | ⚪ **CASH** | **+1.0 bps** (±0.3) | `[+0.9, +1.1, +1.0, +0.8, +1.7]` | `-0.116` | `0.24%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,652.07 | ⚪ **CASH** | **-0.1 bps** (±0.3) | `[+0.2, +0.3, -0.3, +0.0, -0.3]` | `-0.215` | `0.29%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $120.41 | ⚪ **CASH** | **+2.4 bps** (±0.5) | `[+2.1, +3.6, +2.7, +2.5, +2.4]` | `-0.067` | `0.61%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 01:47:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,832.76 | ⚪ **CASH** | **+0.9 bps** (±0.3) | `[+0.8, +1.0, +0.8, +0.9, +1.5]` | `-0.060` | `0.23%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,665.48 | ⚪ **CASH** | **-0.8 bps** (±0.1) | `[-0.8, -0.7, -0.8, -0.8, -0.9]` | `-0.127` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $121.03 | ⚪ **CASH** | **+1.6 bps** (±0.4) | `[+1.4, +2.3, +2.3, +1.6, +1.6]` | `-0.039` | `0.60%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 01:31:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,081.77 | ⚪ **CASH** | **+0.9 bps** (±0.3) | `[+0.8, +1.0, +0.8, +0.9, +1.5]` | `-0.060` | `0.23%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,673.98 | ⚪ **CASH** | **-0.8 bps** (±0.1) | `[-0.8, -0.7, -0.8, -0.8, -0.9]` | `-0.127` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $121.93 | ⚪ **CASH** | **+1.6 bps** (±0.4) | `[+1.4, +2.3, +2.3, +1.6, +1.6]` | `-0.039` | `0.60%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-28 01:16:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,947.90 | ⚪ **CASH** | **+0.9 bps** (±0.3) | `[+0.8, +1.0, +0.8, +0.9, +1.5]` | `-0.060` | `0.23%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,669.42 | ⚪ **CASH** | **-0.8 bps** (±0.1) | `[-0.8, -0.7, -0.8, -0.8, -0.9]` | `-0.127` | `0.28%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $121.42 | ⚪ **CASH** | **+1.6 bps** (±0.4) | `[+1.4, +2.3, +2.3, +1.6, +1.6]` | `-0.039` | `0.60%/h` | `sol_sideways` | Aguardando sinal com assimetria |
