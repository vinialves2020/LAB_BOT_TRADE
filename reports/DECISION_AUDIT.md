# 📋 BOT_TRADE V5 — Livro de Auditoria de Decisões e Análise de Mercado

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o consenso dos 5 modelos XGBoost, o comportamento do CVD (Cumulative Volume Delta) e o disparo de travas de risco.

**Última Atualização**: `2026-09-12 14:47:19 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-09-12 14:47:19 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,465.79 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.125` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,539.60 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.2, +0.1, +0.3, -0.1, -0.1]` | `-0.034` | `0.80%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.05 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[+0.3, -0.1, -0.4, -0.2, -0.3]` | `+0.080` | `0.70%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 14:32:10 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,451.76 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.125` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,543.06 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.2, +0.1, +0.3, -0.1, -0.1]` | `-0.034` | `0.80%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.05 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[+0.3, -0.1, -0.4, -0.2, -0.3]` | `+0.080` | `0.70%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 14:17:12 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,368.95 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.125` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,541.86 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.2, +0.1, +0.3, -0.1, -0.1]` | `-0.034` | `0.80%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.98 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[+0.3, -0.1, -0.4, -0.2, -0.3]` | `+0.080` | `0.70%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 14:02:07 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,366.53 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.125` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,542.24 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.2, +0.1, +0.3, -0.1, -0.1]` | `-0.034` | `0.80%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.98 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[+0.3, -0.1, -0.4, -0.2, -0.3]` | `+0.080` | `0.70%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 13:47:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,289.20 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.090` | `0.40%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,538.79 | ⚪ **CASH** | **+0.1 bps** (±0.3) | `[+0.2, +0.1, +0.8, -0.1, +0.3]` | `-0.055` | `0.81%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.83 | ⚪ **CASH** | **-0.7 bps** (±0.2) | `[-0.3, -0.8, -0.6, -0.8, -0.6]` | `+0.034` | `0.71%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 13:32:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,300.01 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.090` | `0.40%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,538.98 | ⚪ **CASH** | **+0.1 bps** (±0.3) | `[+0.2, +0.1, +0.8, -0.1, +0.3]` | `-0.055` | `0.81%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.84 | ⚪ **CASH** | **-0.7 bps** (±0.2) | `[-0.3, -0.8, -0.6, -0.8, -0.6]` | `+0.034` | `0.71%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 13:16:58 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,308.15 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.090` | `0.40%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,540.91 | ⚪ **CASH** | **+0.1 bps** (±0.3) | `[+0.2, +0.1, +0.8, -0.1, +0.3]` | `-0.055` | `0.81%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.93 | ⚪ **CASH** | **-0.7 bps** (±0.2) | `[-0.3, -0.8, -0.6, -0.8, -0.6]` | `+0.034` | `0.71%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 13:02:12 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,309.99 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.090` | `0.40%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,534.56 | ⚪ **CASH** | **+0.1 bps** (±0.3) | `[+0.2, +0.1, +0.8, -0.1, +0.3]` | `-0.055` | `0.81%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.04 | ⚪ **CASH** | **-0.7 bps** (±0.2) | `[-0.3, -0.8, -0.6, -0.8, -0.6]` | `+0.034` | `0.71%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 12:47:12 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,323.75 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.129` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,534.78 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.2, +0.0, +0.3, +0.2, +0.6]` | `-0.032` | `0.82%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.26 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.1, -0.9, -0.4, -0.8, -0.6]` | `-0.059` | `0.72%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 12:32:03 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,328.00 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.129` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,533.67 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.2, +0.0, +0.3, +0.2, +0.6]` | `-0.032` | `0.82%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.39 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.1, -0.9, -0.4, -0.8, -0.6]` | `-0.059` | `0.72%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 12:17:19 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,338.00 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.129` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,534.49 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.2, +0.0, +0.3, +0.2, +0.6]` | `-0.032` | `0.82%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.20 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.1, -0.9, -0.4, -0.8, -0.6]` | `-0.059` | `0.72%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 12:02:24 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,359.54 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.129` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,535.01 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.2, +0.0, +0.3, +0.2, +0.6]` | `-0.032` | `0.82%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.18 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.1, -0.9, -0.4, -0.8, -0.6]` | `-0.059` | `0.72%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 11:46:56 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,342.19 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.181` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,537.20 | ⚪ **CASH** | **+0.2 bps** (±0.3) | `[+0.2, +0.1, +0.8, +0.2, +0.5]` | `-0.053` | `0.83%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.08 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.1, -0.9, -0.4, -0.8, -0.6]` | `-0.056` | `0.73%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 11:32:02 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,292.27 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.181` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,533.00 | ⚪ **CASH** | **+0.2 bps** (±0.3) | `[+0.2, +0.1, +0.8, +0.2, +0.5]` | `-0.053` | `0.83%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.03 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.1, -0.9, -0.4, -0.8, -0.6]` | `-0.056` | `0.73%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 11:17:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,327.52 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.181` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,531.54 | ⚪ **CASH** | **+0.2 bps** (±0.3) | `[+0.2, +0.1, +0.8, +0.2, +0.5]` | `-0.053` | `0.83%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.07 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.1, -0.9, -0.4, -0.8, -0.6]` | `-0.056` | `0.73%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 11:02:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,344.01 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.181` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,534.98 | ⚪ **CASH** | **+0.2 bps** (±0.3) | `[+0.2, +0.1, +0.8, +0.2, +0.5]` | `-0.053` | `0.83%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.21 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.1, -0.9, -0.4, -0.8, -0.6]` | `-0.056` | `0.73%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 10:46:55 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,374.01 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.150` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,534.09 | ⚪ **CASH** | **+0.2 bps** (±0.3) | `[+0.2, +0.1, +0.8, +0.2, +0.5]` | `-0.053` | `0.84%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.12 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.1, -0.9, -0.4, -0.8, -0.6]` | `-0.061` | `0.74%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 10:32:02 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,364.01 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.150` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,531.42 | ⚪ **CASH** | **+0.2 bps** (±0.3) | `[+0.2, +0.1, +0.8, +0.2, +0.5]` | `-0.053` | `0.84%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.02 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.1, -0.9, -0.4, -0.8, -0.6]` | `-0.061` | `0.74%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 10:17:32 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,398.00 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.150` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,533.66 | ⚪ **CASH** | **+0.2 bps** (±0.3) | `[+0.2, +0.1, +0.8, +0.2, +0.5]` | `-0.053` | `0.84%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.12 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.1, -0.9, -0.4, -0.8, -0.6]` | `-0.061` | `0.74%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 10:02:09 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,359.99 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.150` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,533.18 | ⚪ **CASH** | **+0.2 bps** (±0.3) | `[+0.2, +0.1, +0.8, +0.2, +0.5]` | `-0.053` | `0.84%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.12 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.1, -0.9, -0.4, -0.8, -0.6]` | `-0.061` | `0.74%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 09:47:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,350.02 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.170` | `0.43%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,531.07 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[+0.1, +0.1, +0.3, +0.2, +0.5]` | `-0.038` | `0.86%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.02 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.1, -0.9, -0.4, -0.8, -0.6]` | `-0.104` | `0.76%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 09:32:29 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,381.60 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.170` | `0.43%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,536.13 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[+0.1, +0.1, +0.3, +0.2, +0.5]` | `-0.038` | `0.86%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.10 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.1, -0.9, -0.4, -0.8, -0.6]` | `-0.104` | `0.76%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 09:17:09 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,382.70 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.170` | `0.43%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,536.93 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[+0.1, +0.1, +0.3, +0.2, +0.5]` | `-0.038` | `0.86%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.08 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.1, -0.9, -0.4, -0.8, -0.6]` | `-0.104` | `0.76%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 09:02:07 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,348.91 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.170` | `0.43%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,532.44 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[+0.1, +0.1, +0.3, +0.2, +0.5]` | `-0.038` | `0.86%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.77 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.1, -0.9, -0.4, -0.8, -0.6]` | `-0.104` | `0.76%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 08:47:26 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,351.43 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.153` | `0.44%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,533.28 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[-0.1, +0.0, +0.4, +0.2, +0.5]` | `-0.023` | `0.87%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.77 | ⚪ **CASH** | **-1.1 bps** (±0.8) | `[+0.5, -1.0, -1.9, -0.7, -0.6]` | `-0.082` | `0.77%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 08:32:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,309.99 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.153` | `0.44%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,529.35 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[-0.1, +0.0, +0.4, +0.2, +0.5]` | `-0.023` | `0.87%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.65 | ⚪ **CASH** | **-1.1 bps** (±0.8) | `[+0.5, -1.0, -1.9, -0.7, -0.6]` | `-0.082` | `0.77%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 08:17:30 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,345.88 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.153` | `0.44%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,528.49 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[-0.1, +0.0, +0.4, +0.2, +0.5]` | `-0.023` | `0.87%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.71 | ⚪ **CASH** | **-1.1 bps** (±0.8) | `[+0.5, -1.0, -1.9, -0.7, -0.6]` | `-0.082` | `0.77%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 08:02:20 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,276.01 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.153` | `0.44%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,523.25 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[-0.1, +0.0, +0.4, +0.2, +0.5]` | `-0.023` | `0.87%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.63 | ⚪ **CASH** | **-1.1 bps** (±0.8) | `[+0.5, -1.0, -1.9, -0.7, -0.6]` | `-0.082` | `0.77%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 07:47:00 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,278.00 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.122` | `0.44%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,522.33 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[-0.1, +0.0, +0.3, +0.2, +0.5]` | `-0.054` | `0.88%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.65 | ⚪ **CASH** | **-0.6 bps** (±0.3) | `[+0.3, -0.6, -0.4, -0.6, -0.6]` | `-0.020` | `0.78%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 07:32:15 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,308.35 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.122` | `0.44%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,522.95 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[-0.1, +0.0, +0.3, +0.2, +0.5]` | `-0.054` | `0.88%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.74 | ⚪ **CASH** | **-0.6 bps** (±0.3) | `[+0.3, -0.6, -0.4, -0.6, -0.6]` | `-0.020` | `0.78%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 07:16:56 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,330.01 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.122` | `0.44%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,522.67 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[-0.1, +0.0, +0.3, +0.2, +0.5]` | `-0.054` | `0.88%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.78 | ⚪ **CASH** | **-0.6 bps** (±0.3) | `[+0.3, -0.6, -0.4, -0.6, -0.6]` | `-0.020` | `0.78%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 07:02:19 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,308.64 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.0, +0.0, +0.0, +0.1, +0.2]` | `+0.122` | `0.44%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,521.43 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[-0.1, +0.0, +0.3, +0.2, +0.5]` | `-0.054` | `0.88%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.73 | ⚪ **CASH** | **-0.6 bps** (±0.3) | `[+0.3, -0.6, -0.4, -0.6, -0.6]` | `-0.020` | `0.78%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 06:47:02 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,324.60 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.093` | `0.45%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,519.39 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[-0.1, +0.0, +0.4, +0.2, +0.5]` | `-0.180` | `0.89%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.82 | ⚪ **CASH** | **-0.8 bps** (±0.3) | `[-0.1, -0.8, -0.4, -1.0, -0.8]` | `+0.018` | `0.79%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 06:32:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,280.01 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.093` | `0.45%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,514.08 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[-0.1, +0.0, +0.4, +0.2, +0.5]` | `-0.180` | `0.89%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.80 | ⚪ **CASH** | **-0.8 bps** (±0.3) | `[-0.1, -0.8, -0.4, -1.0, -0.8]` | `+0.018` | `0.79%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 06:17:09 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,222.00 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.093` | `0.45%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,511.79 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[-0.1, +0.0, +0.4, +0.2, +0.5]` | `-0.180` | `0.89%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.62 | ⚪ **CASH** | **-0.8 bps** (±0.3) | `[-0.1, -0.8, -0.4, -1.0, -0.8]` | `+0.018` | `0.79%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-12 06:02:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,215.36 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `+0.093` | `0.45%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,511.80 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[-0.1, +0.0, +0.4, +0.2, +0.5]` | `-0.180` | `0.89%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.62 | ⚪ **CASH** | **-0.8 bps** (±0.3) | `[-0.1, -0.8, -0.4, -1.0, -0.8]` | `+0.018` | `0.79%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |
