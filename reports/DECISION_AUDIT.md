# 📋 BOT_TRADE V5 — Livro de Auditoria de Decisões e Análise de Mercado

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o consenso dos 5 modelos XGBoost, o comportamento do CVD (Cumulative Volume Delta) e o disparo de travas de risco.

**Última Atualização**: `2026-09-24 03:32:06 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-09-24 03:32:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,016.01 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.129` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,675.21 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[+0.2, -0.1, +0.3, -0.1, -0.2]` | `-0.005` | `0.42%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.72 | ⚪ **CASH** | **-0.8 bps** (±0.3) | `[-1.1, -0.3, -0.4, -0.6, -0.6]` | `-0.031` | `0.53%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 03:17:19 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,272.00 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.129` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,683.08 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[+0.2, -0.1, +0.3, -0.1, -0.2]` | `-0.005` | `0.42%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.21 | ⚪ **CASH** | **-0.8 bps** (±0.3) | `[-1.1, -0.3, -0.4, -0.6, -0.6]` | `-0.031` | `0.53%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 03:02:17 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,438.01 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.129` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,688.74 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[+0.2, -0.1, +0.3, -0.1, -0.2]` | `-0.005` | `0.42%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.49 | ⚪ **CASH** | **-0.8 bps** (±0.3) | `[-1.1, -0.3, -0.4, -0.6, -0.6]` | `-0.031` | `0.53%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 02:46:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,346.01 | ⚪ **CASH** | **+0.4 bps** (±0.3) | `[+0.9, +0.8, +0.4, +0.3, +0.2]` | `-0.157` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,685.82 | ⚪ **CASH** | **+0.2 bps** (±0.4) | `[+0.3, +0.6, +0.8, +0.5, -0.3]` | `+0.013` | `0.41%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.32 | ⚪ **CASH** | **+0.3 bps** (±0.7) | `[+0.3, +1.7, +0.7, +0.9, -0.4]` | `-0.054` | `0.53%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 02:32:23 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,188.62 | ⚪ **CASH** | **+0.4 bps** (±0.3) | `[+0.9, +0.8, +0.4, +0.3, +0.2]` | `-0.157` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,680.41 | ⚪ **CASH** | **+0.2 bps** (±0.4) | `[+0.3, +0.6, +0.8, +0.5, -0.3]` | `+0.013` | `0.41%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.88 | ⚪ **CASH** | **+0.3 bps** (±0.7) | `[+0.3, +1.7, +0.7, +0.9, -0.4]` | `-0.054` | `0.53%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 02:17:19 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,171.99 | ⚪ **CASH** | **+0.4 bps** (±0.3) | `[+0.9, +0.8, +0.4, +0.3, +0.2]` | `-0.157` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,681.64 | ⚪ **CASH** | **+0.2 bps** (±0.4) | `[+0.3, +0.6, +0.8, +0.5, -0.3]` | `+0.013` | `0.41%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.83 | ⚪ **CASH** | **+0.3 bps** (±0.7) | `[+0.3, +1.7, +0.7, +0.9, -0.4]` | `-0.054` | `0.53%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 02:02:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,094.00 | ⚪ **CASH** | **+0.4 bps** (±0.3) | `[+0.9, +0.8, +0.4, +0.3, +0.2]` | `-0.157` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,675.64 | ⚪ **CASH** | **+0.2 bps** (±0.4) | `[+0.3, +0.6, +0.8, +0.5, -0.3]` | `+0.013` | `0.41%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.77 | ⚪ **CASH** | **+0.3 bps** (±0.7) | `[+0.3, +1.7, +0.7, +0.9, -0.4]` | `-0.054` | `0.53%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 01:47:17 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,126.00 | ⚪ **CASH** | **+0.3 bps** (±0.3) | `[+0.9, +0.5, +0.4, +0.3, +0.1]` | `-0.113` | `0.43%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,678.94 | ⚪ **CASH** | **-0.3 bps** (±0.3) | `[-0.4, -0.2, +0.4, -0.2, -0.3]` | `+0.110` | `0.43%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.73 | ⚪ **CASH** | **-0.8 bps** (±0.3) | `[-1.1, -0.3, -0.4, -0.6, -0.6]` | `-0.068` | `0.54%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 01:32:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,248.16 | ⚪ **CASH** | **+0.3 bps** (±0.3) | `[+0.9, +0.5, +0.4, +0.3, +0.1]` | `-0.113` | `0.43%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,682.85 | ⚪ **CASH** | **-0.3 bps** (±0.3) | `[-0.4, -0.2, +0.4, -0.2, -0.3]` | `+0.110` | `0.43%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.09 | ⚪ **CASH** | **-0.8 bps** (±0.3) | `[-1.1, -0.3, -0.4, -0.6, -0.6]` | `-0.068` | `0.54%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 01:17:25 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,234.01 | ⚪ **CASH** | **+0.3 bps** (±0.3) | `[+0.9, +0.5, +0.4, +0.3, +0.1]` | `-0.113` | `0.43%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,680.01 | ⚪ **CASH** | **-0.3 bps** (±0.3) | `[-0.4, -0.2, +0.4, -0.2, -0.3]` | `+0.110` | `0.43%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.11 | ⚪ **CASH** | **-0.8 bps** (±0.3) | `[-1.1, -0.3, -0.4, -0.6, -0.6]` | `-0.068` | `0.54%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 01:02:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,368.01 | ⚪ **CASH** | **+0.3 bps** (±0.3) | `[+0.9, +0.5, +0.4, +0.3, +0.1]` | `-0.113` | `0.43%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,684.97 | ⚪ **CASH** | **-0.3 bps** (±0.3) | `[-0.4, -0.2, +0.4, -0.2, -0.3]` | `+0.110` | `0.43%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.28 | ⚪ **CASH** | **-0.8 bps** (±0.3) | `[-1.1, -0.3, -0.4, -0.6, -0.6]` | `-0.068` | `0.54%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 00:46:54 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,358.01 | ⚪ **CASH** | **+0.4 bps** (±0.2) | `[+0.9, +0.6, +0.4, +0.3, +0.2]` | `-0.105` | `0.44%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,684.76 | ⚪ **CASH** | **+0.6 bps** (±0.1) | `[+0.6, +0.8, +0.8, +0.6, +0.5]` | `+0.148` | `0.45%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.08 | ⚪ **CASH** | **-0.9 bps** (±0.3) | `[-1.1, -0.3, -0.5, -0.6, -1.1]` | `-0.099` | `0.55%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 00:32:25 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,431.38 | ⚪ **CASH** | **+0.4 bps** (±0.2) | `[+0.9, +0.6, +0.4, +0.3, +0.2]` | `-0.105` | `0.44%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,691.31 | ⚪ **CASH** | **+0.6 bps** (±0.1) | `[+0.6, +0.8, +0.8, +0.6, +0.5]` | `+0.148` | `0.45%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.46 | ⚪ **CASH** | **-0.9 bps** (±0.3) | `[-1.1, -0.3, -0.5, -0.6, -1.1]` | `-0.099` | `0.55%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 00:17:28 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,404.01 | ⚪ **CASH** | **+0.4 bps** (±0.2) | `[+0.9, +0.6, +0.4, +0.3, +0.2]` | `-0.105` | `0.44%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,688.98 | ⚪ **CASH** | **+0.6 bps** (±0.1) | `[+0.6, +0.8, +0.8, +0.6, +0.5]` | `+0.148` | `0.45%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.27 | ⚪ **CASH** | **-0.9 bps** (±0.3) | `[-1.1, -0.3, -0.5, -0.6, -1.1]` | `-0.099` | `0.55%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 00:02:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,446.00 | ⚪ **CASH** | **+0.4 bps** (±0.2) | `[+0.9, +0.6, +0.4, +0.3, +0.2]` | `-0.105` | `0.44%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,685.63 | ⚪ **CASH** | **+0.6 bps** (±0.1) | `[+0.6, +0.8, +0.8, +0.6, +0.5]` | `+0.148` | `0.45%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.03 | ⚪ **CASH** | **-0.9 bps** (±0.3) | `[-1.1, -0.3, -0.5, -0.6, -1.1]` | `-0.099` | `0.55%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 23:47:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,427.99 | ⚪ **CASH** | **+0.2 bps** (±0.6) | `[+0.6, +0.2, +1.7, +0.1, +0.2]` | `-0.028` | `0.44%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,682.36 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.1, -0.1, +0.3, -0.1, -0.0]` | `+0.122` | `0.46%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.89 | ⚪ **CASH** | **-1.2 bps** (±0.5) | `[-1.5, -0.6, -0.4, -1.6, -0.8]` | `-0.113` | `0.56%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 23:32:21 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,466.01 | ⚪ **CASH** | **+0.2 bps** (±0.6) | `[+0.6, +0.2, +1.7, +0.1, +0.2]` | `-0.028` | `0.44%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,684.60 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.1, -0.1, +0.3, -0.1, -0.0]` | `+0.122` | `0.46%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.87 | ⚪ **CASH** | **-1.2 bps** (±0.5) | `[-1.5, -0.6, -0.4, -1.6, -0.8]` | `-0.113` | `0.56%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 23:16:57 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,488.01 | ⚪ **CASH** | **+0.2 bps** (±0.6) | `[+0.6, +0.2, +1.7, +0.1, +0.2]` | `-0.028` | `0.44%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,686.59 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.1, -0.1, +0.3, -0.1, -0.0]` | `+0.122` | `0.46%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.01 | ⚪ **CASH** | **-1.2 bps** (±0.5) | `[-1.5, -0.6, -0.4, -1.6, -0.8]` | `-0.113` | `0.56%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 23:02:32 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,490.00 | ⚪ **CASH** | **+0.2 bps** (±0.6) | `[+0.6, +0.2, +1.7, +0.1, +0.2]` | `-0.028` | `0.44%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,687.37 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.1, -0.1, +0.3, -0.1, -0.0]` | `+0.122` | `0.46%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.96 | ⚪ **CASH** | **-1.2 bps** (±0.5) | `[-1.5, -0.6, -0.4, -1.6, -0.8]` | `-0.113` | `0.56%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 22:47:17 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,579.83 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.035` | `0.45%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,691.20 | ⚪ **CASH** | **-0.2 bps** (±0.2) | `[-0.2, -0.2, +0.3, -0.3, -0.2]` | `+0.115` | `0.45%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.12 | ⚪ **CASH** | **-1.0 bps** (±0.3) | `[-1.1, -0.4, -0.5, -1.2, -1.1]` | `-0.148` | `0.57%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 22:32:18 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,400.01 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.035` | `0.45%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,683.45 | ⚪ **CASH** | **-0.2 bps** (±0.2) | `[-0.2, -0.2, +0.3, -0.3, -0.2]` | `+0.115` | `0.45%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.69 | ⚪ **CASH** | **-1.0 bps** (±0.3) | `[-1.1, -0.4, -0.5, -1.2, -1.1]` | `-0.148` | `0.57%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 22:17:19 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,566.01 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.035` | `0.45%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,689.00 | ⚪ **CASH** | **-0.2 bps** (±0.2) | `[-0.2, -0.2, +0.3, -0.3, -0.2]` | `+0.115` | `0.45%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.32 | ⚪ **CASH** | **-1.0 bps** (±0.3) | `[-1.1, -0.4, -0.5, -1.2, -1.1]` | `-0.148` | `0.57%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 22:02:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,437.66 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.035` | `0.45%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,678.82 | ⚪ **CASH** | **-0.2 bps** (±0.2) | `[-0.2, -0.2, +0.3, -0.3, -0.2]` | `+0.115` | `0.45%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.80 | ⚪ **CASH** | **-1.0 bps** (±0.3) | `[-1.1, -0.4, -0.5, -1.2, -1.1]` | `-0.148` | `0.57%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 21:46:58 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,512.01 | ⚪ **CASH** | **+0.8 bps** (±0.3) | `[+1.4, +0.9, +0.8, +0.6, +0.8]` | `-0.076` | `0.45%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,678.69 | ⚪ **CASH** | **+1.0 bps** (±0.2) | `[+1.2, +1.3, +1.2, +0.8, +1.1]` | `+0.047` | `0.46%/h` | `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.60 | ⚪ **CASH** | **+0.9 bps** (±0.5) | `[+0.5, +1.9, +1.0, +1.1, +1.1]` | `-0.154` | `0.56%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 21:32:19 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,438.01 | ⚪ **CASH** | **+0.8 bps** (±0.3) | `[+1.4, +0.9, +0.8, +0.6, +0.8]` | `-0.076` | `0.45%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,675.75 | ⚪ **CASH** | **+1.0 bps** (±0.2) | `[+1.2, +1.3, +1.2, +0.8, +1.1]` | `+0.047` | `0.46%/h` | `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.37 | ⚪ **CASH** | **+0.9 bps** (±0.5) | `[+0.5, +1.9, +1.0, +1.1, +1.1]` | `-0.154` | `0.56%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 21:17:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,372.08 | ⚪ **CASH** | **+0.8 bps** (±0.3) | `[+1.4, +0.9, +0.8, +0.6, +0.8]` | `-0.076` | `0.45%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,673.34 | ⚪ **CASH** | **+1.0 bps** (±0.2) | `[+1.2, +1.3, +1.2, +0.8, +1.1]` | `+0.047` | `0.46%/h` | `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.39 | ⚪ **CASH** | **+0.9 bps** (±0.5) | `[+0.5, +1.9, +1.0, +1.1, +1.1]` | `-0.154` | `0.56%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 21:02:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,230.01 | ⚪ **CASH** | **+0.8 bps** (±0.3) | `[+1.4, +0.9, +0.8, +0.6, +0.8]` | `-0.076` | `0.45%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,670.60 | ⚪ **CASH** | **+1.0 bps** (±0.2) | `[+1.2, +1.3, +1.2, +0.8, +1.1]` | `+0.047` | `0.46%/h` | `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.03 | ⚪ **CASH** | **+0.9 bps** (±0.5) | `[+0.5, +1.9, +1.0, +1.1, +1.1]` | `-0.154` | `0.56%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 20:46:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,392.35 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.105` | `0.46%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,675.35 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.2, -0.2, +0.2, -0.3, -0.3]` | `-0.005` | `0.46%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.40 | ⚪ **CASH** | **-0.9 bps** (±0.5) | `[-0.7, +0.1, -0.5, -1.2, -1.1]` | `-0.151` | `0.57%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 20:32:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,366.33 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.105` | `0.46%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,674.00 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.2, -0.2, +0.2, -0.3, -0.3]` | `-0.005` | `0.46%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.26 | ⚪ **CASH** | **-0.9 bps** (±0.5) | `[-0.7, +0.1, -0.5, -1.2, -1.1]` | `-0.151` | `0.57%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 20:17:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,353.58 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.105` | `0.46%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,673.85 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.2, -0.2, +0.2, -0.3, -0.3]` | `-0.005` | `0.46%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.33 | ⚪ **CASH** | **-0.9 bps** (±0.5) | `[-0.7, +0.1, -0.5, -1.2, -1.1]` | `-0.151` | `0.57%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 20:02:36 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,442.57 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.105` | `0.46%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,675.21 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.2, -0.2, +0.2, -0.3, -0.3]` | `-0.005` | `0.46%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.47 | ⚪ **CASH** | **-0.9 bps** (±0.5) | `[-0.7, +0.1, -0.5, -1.2, -1.1]` | `-0.151` | `0.57%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 19:47:21 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,500.00 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.7, +0.2, +0.6, +0.1, +0.2]` | `-0.100` | `0.46%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,677.82 | ⚪ **CASH** | **-0.4 bps** (±0.3) | `[-0.2, -0.2, +0.2, -0.5, -0.6]` | `-0.047` | `0.46%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.63 | ⚪ **CASH** | **-1.2 bps** (±0.4) | `[-1.4, -0.4, -0.9, -1.4, -1.1]` | `-0.134` | `0.58%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 19:32:29 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,420.00 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.7, +0.2, +0.6, +0.1, +0.2]` | `-0.100` | `0.46%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,673.72 | ⚪ **CASH** | **-0.4 bps** (±0.3) | `[-0.2, -0.2, +0.2, -0.5, -0.6]` | `-0.047` | `0.46%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.51 | ⚪ **CASH** | **-1.2 bps** (±0.4) | `[-1.4, -0.4, -0.9, -1.4, -1.1]` | `-0.134` | `0.58%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 19:16:57 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,339.61 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.7, +0.2, +0.6, +0.1, +0.2]` | `-0.100` | `0.46%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,666.19 | ⚪ **CASH** | **-0.4 bps** (±0.3) | `[-0.2, -0.2, +0.2, -0.5, -0.6]` | `-0.047` | `0.46%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.28 | ⚪ **CASH** | **-1.2 bps** (±0.4) | `[-1.4, -0.4, -0.9, -1.4, -1.1]` | `-0.134` | `0.58%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 19:02:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,322.01 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.7, +0.2, +0.6, +0.1, +0.2]` | `-0.100` | `0.46%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,667.99 | ⚪ **CASH** | **-0.4 bps** (±0.3) | `[-0.2, -0.2, +0.2, -0.5, -0.6]` | `-0.047` | `0.46%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.23 | ⚪ **CASH** | **-1.2 bps** (±0.4) | `[-1.4, -0.4, -0.9, -1.4, -1.1]` | `-0.134` | `0.58%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 18:47:16 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,221.05 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[+0.6, +0.2, +0.4, -0.1, +0.2]` | `-0.108` | `0.47%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,663.84 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.2, -0.2, +0.2, -0.3, -0.3]` | `-0.079` | `0.47%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.21 | ⚪ **CASH** | **-0.9 bps** (±0.5) | `[-0.7, +0.1, -0.5, -1.2, -1.1]` | `-0.133` | `0.59%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |
