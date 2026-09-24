# 📋 BOT_TRADE V5 — Livro de Auditoria de Decisões e Análise de Mercado

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o consenso dos 5 modelos XGBoost, o comportamento do CVD (Cumulative Volume Delta) e o disparo de travas de risco.

**Última Atualização**: `2026-09-24 08:17:17 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-09-24 08:17:17 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,440.17 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[+0.6, +0.2, +0.2, -0.1, +0.0]` | `-0.034` | `0.41%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,689.07 | ⚪ **CASH** | **-0.2 bps** (±0.3) | `[+0.2, -0.3, +0.3, -0.0, -0.4]` | `-0.006` | `0.40%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.27 | ⚪ **CASH** | **-0.9 bps** (±0.3) | `[-1.2, -0.5, -0.4, -0.8, -0.8]` | `+0.049` | `0.53%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 08:02:28 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,550.47 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[+0.6, +0.2, +0.2, -0.1, +0.0]` | `-0.034` | `0.41%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,693.50 | ⚪ **CASH** | **-0.2 bps** (±0.3) | `[+0.2, -0.3, +0.3, -0.0, -0.4]` | `-0.006` | `0.40%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.56 | ⚪ **CASH** | **-0.9 bps** (±0.3) | `[-1.2, -0.5, -0.4, -0.8, -0.8]` | `+0.049` | `0.53%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 07:46:56 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,416.00 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.121` | `0.41%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,695.41 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[+0.2, -0.1, +0.3, -0.1, -0.2]` | `-0.068` | `0.40%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.47 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-1.3, -0.1, -0.4, -1.0, -0.8]` | `+0.004` | `0.53%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 07:32:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,530.00 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.121` | `0.41%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,695.64 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[+0.2, -0.1, +0.3, -0.1, -0.2]` | `-0.068` | `0.40%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.32 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-1.3, -0.1, -0.4, -1.0, -0.8]` | `+0.004` | `0.53%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 07:17:23 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,146.00 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.121` | `0.41%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,685.78 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[+0.2, -0.1, +0.3, -0.1, -0.2]` | `-0.068` | `0.40%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.92 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-1.3, -0.1, -0.4, -1.0, -0.8]` | `+0.004` | `0.53%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 07:02:25 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,970.01 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.121` | `0.41%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,681.13 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[+0.2, -0.1, +0.3, -0.1, -0.2]` | `-0.068` | `0.40%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.64 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-1.3, -0.1, -0.4, -1.0, -0.8]` | `+0.004` | `0.53%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 06:47:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,097.40 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.069` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,687.09 | ⚪ **CASH** | **-0.3 bps** (±0.3) | `[-0.2, -0.2, +0.4, -0.4, -0.6]` | `-0.075` | `0.40%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.84 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-1.3, -0.1, -0.4, -1.0, -0.8]` | `-0.002` | `0.53%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 06:32:00 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,210.00 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.069` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,688.37 | ⚪ **CASH** | **-0.3 bps** (±0.3) | `[-0.2, -0.2, +0.4, -0.4, -0.6]` | `-0.075` | `0.40%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.11 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-1.3, -0.1, -0.4, -1.0, -0.8]` | `-0.002` | `0.53%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 06:17:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,164.49 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.069` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,688.67 | ⚪ **CASH** | **-0.3 bps** (±0.3) | `[-0.2, -0.2, +0.4, -0.4, -0.6]` | `-0.075` | `0.40%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.20 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-1.3, -0.1, -0.4, -1.0, -0.8]` | `-0.002` | `0.53%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 06:02:24 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,928.00 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.069` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,680.36 | ⚪ **CASH** | **-0.3 bps** (±0.3) | `[-0.2, -0.2, +0.4, -0.4, -0.6]` | `-0.075` | `0.40%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.78 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-1.3, -0.1, -0.4, -1.0, -0.8]` | `-0.002` | `0.53%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 05:47:00 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,240.00 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, -0.1, -0.1, +0.0]` | `-0.087` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,692.47 | ⚪ **CASH** | **-0.2 bps** (±0.2) | `[-0.2, -0.2, +0.3, -0.1, -0.3]` | `-0.097` | `0.41%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.47 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.8, -0.1, -0.4, -0.8, -0.8]` | `-0.054` | `0.54%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 05:32:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,140.31 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, -0.1, -0.1, +0.0]` | `-0.087` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,689.48 | ⚪ **CASH** | **-0.2 bps** (±0.2) | `[-0.2, -0.2, +0.3, -0.1, -0.3]` | `-0.097` | `0.41%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.32 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.8, -0.1, -0.4, -0.8, -0.8]` | `-0.054` | `0.54%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 05:16:55 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,172.32 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, -0.1, -0.1, +0.0]` | `-0.087` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,691.10 | ⚪ **CASH** | **-0.2 bps** (±0.2) | `[-0.2, -0.2, +0.3, -0.1, -0.3]` | `-0.097` | `0.41%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.51 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.8, -0.1, -0.4, -0.8, -0.8]` | `-0.054` | `0.54%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 05:02:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,120.00 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, -0.1, -0.1, +0.0]` | `-0.087` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,685.30 | ⚪ **CASH** | **-0.2 bps** (±0.2) | `[-0.2, -0.2, +0.3, -0.1, -0.3]` | `-0.097` | `0.41%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.55 | ⚪ **CASH** | **-0.7 bps** (±0.3) | `[-0.8, -0.1, -0.4, -0.8, -0.8]` | `-0.054` | `0.54%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 04:47:00 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,870.00 | ⚪ **CASH** | **+0.6 bps** (±0.7) | `[+1.4, +1.6, +0.9, -0.3, +1.0]` | `-0.117` | `0.43%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,675.76 | ⚪ **CASH** | **+1.6 bps** (±0.6) | `[+2.7, +2.1, +1.6, +1.8, +1.1]` | `-0.046` | `0.41%/h` | `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.97 | ⚪ **CASH** | **+2.1 bps** (±0.6) | `[+2.1, +3.6, +2.1, +2.7, +1.9]` | `-0.012` | `0.53%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 04:32:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,906.00 | ⚪ **CASH** | **+0.6 bps** (±0.7) | `[+1.4, +1.6, +0.9, -0.3, +1.0]` | `-0.117` | `0.43%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,676.84 | ⚪ **CASH** | **+1.6 bps** (±0.6) | `[+2.7, +2.1, +1.6, +1.8, +1.1]` | `-0.046` | `0.41%/h` | `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.88 | ⚪ **CASH** | **+2.1 bps** (±0.6) | `[+2.1, +3.6, +2.1, +2.7, +1.9]` | `-0.012` | `0.53%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 04:17:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,880.01 | ⚪ **CASH** | **+0.6 bps** (±0.7) | `[+1.4, +1.6, +0.9, -0.3, +1.0]` | `-0.117` | `0.43%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,674.51 | ⚪ **CASH** | **+1.6 bps** (±0.6) | `[+2.7, +2.1, +1.6, +1.8, +1.1]` | `-0.046` | `0.41%/h` | `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.69 | ⚪ **CASH** | **+2.1 bps** (±0.6) | `[+2.1, +3.6, +2.1, +2.7, +1.9]` | `-0.012` | `0.53%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 04:02:22 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,880.01 | ⚪ **CASH** | **+0.6 bps** (±0.7) | `[+1.4, +1.6, +0.9, -0.3, +1.0]` | `-0.117` | `0.43%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,673.01 | ⚪ **CASH** | **+1.6 bps** (±0.6) | `[+2.7, +2.1, +1.6, +1.8, +1.1]` | `-0.046` | `0.41%/h` | `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.57 | ⚪ **CASH** | **+2.1 bps** (±0.6) | `[+2.1, +3.6, +2.1, +2.7, +1.9]` | `-0.012` | `0.53%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 03:46:56 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,008.00 | ⚪ **CASH** | **+0.0 bps** (±0.2) | `[+0.6, +0.2, +0.1, -0.1, +0.0]` | `-0.129` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,676.33 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[+0.2, -0.1, +0.3, -0.1, -0.2]` | `-0.005` | `0.42%/h` | `vol_compressed` `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.85 | ⚪ **CASH** | **-0.8 bps** (±0.3) | `[-1.1, -0.3, -0.4, -0.6, -0.6]` | `-0.031` | `0.53%/h` | `vol_compressed` `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

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
