# 📋 BOT_TRADE V5 — Livro de Auditoria de Decisões e Análise de Mercado

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o consenso dos 5 modelos XGBoost, o comportamento do CVD (Cumulative Volume Delta) e o disparo de travas de risco.

**Última Atualização**: `2026-10-07 16:21:12 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-07 16:21:12 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,627.00 | ⚪ **CASH** | **-0.0 bps** (±0.1) | `[-0.2, +0.0, +0.0, +0.1, +0.2]` | `-0.034` | `0.35%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,576.30 | ⚪ **CASH** | **-2.0 bps** (±0.3) | `[-2.3, -1.5, -1.8, -2.0, -1.6]` | `-0.130` | `0.42%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.11 | ⚪ **CASH** | **-2.4 bps** (±0.2) | `[-2.5, -2.4, -2.4, -2.3, -2.0]` | `-0.129` | `0.43%/h` | `btc_dumping` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 16:02:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,367.11 | ⚪ **CASH** | **-0.0 bps** (±0.1) | `[-0.2, +0.0, +0.0, +0.1, +0.2]` | `-0.034` | `0.35%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,567.69 | ⚪ **CASH** | **-2.0 bps** (±0.3) | `[-2.3, -1.5, -1.8, -2.0, -1.6]` | `-0.130` | `0.42%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.63 | ⚪ **CASH** | **-2.4 bps** (±0.2) | `[-2.5, -2.4, -2.4, -2.3, -2.0]` | `-0.129` | `0.43%/h` | `btc_dumping` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 15:47:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,350.02 | ⚪ **CASH** | **+0.5 bps** (±0.3) | `[+0.1, +1.1, +0.4, +0.9, +0.8]` | `-0.054` | `0.34%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,565.99 | ⚪ **CASH** | **-1.3 bps** (±0.1) | `[-1.4, -1.2, -1.4, -1.2, -1.3]` | `-0.119` | `0.42%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.64 | ⚪ **CASH** | **-3.4 bps** (±0.3) | `[-3.5, -3.3, -3.4, -3.5, -2.8]` | `-0.168` | `0.41%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 15:32:36 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,232.23 | ⚪ **CASH** | **+0.5 bps** (±0.3) | `[+0.1, +1.1, +0.4, +0.9, +0.8]` | `-0.054` | `0.34%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,565.46 | ⚪ **CASH** | **-1.3 bps** (±0.1) | `[-1.4, -1.2, -1.4, -1.2, -1.3]` | `-0.119` | `0.42%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.34 | ⚪ **CASH** | **-3.4 bps** (±0.3) | `[-3.5, -3.3, -3.4, -3.5, -2.8]` | `-0.168` | `0.41%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 15:02:22 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,908.01 | ⚪ **CASH** | **+0.5 bps** (±0.3) | `[+0.1, +1.1, +0.4, +0.9, +0.8]` | `-0.054` | `0.34%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,559.00 | ⚪ **CASH** | **-1.3 bps** (±0.1) | `[-1.4, -1.2, -1.4, -1.2, -1.3]` | `-0.119` | `0.42%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.68 | ⚪ **CASH** | **-3.4 bps** (±0.3) | `[-3.5, -3.3, -3.4, -3.5, -2.8]` | `-0.168` | `0.41%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 14:47:07 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,997.76 | ⚪ **CASH** | **+1.1 bps** (±0.7) | `[+0.6, +1.6, +0.9, +1.5, +2.7]` | `-0.028` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,559.60 | ⚪ **CASH** | **-1.2 bps** (±0.4) | `[-1.6, -0.8, -1.3, -0.9, -0.4]` | `-0.009` | `0.42%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.83 | ⚪ **CASH** | **-0.4 bps** (±0.4) | `[-0.5, -0.1, +0.4, -0.6, -0.4]` | `-0.187` | `0.41%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 14:32:38 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,086.01 | ⚪ **CASH** | **+1.1 bps** (±0.7) | `[+0.6, +1.6, +0.9, +1.5, +2.7]` | `-0.028` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,562.75 | ⚪ **CASH** | **-1.2 bps** (±0.4) | `[-1.6, -0.8, -1.3, -0.9, -0.4]` | `-0.009` | `0.42%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.86 | ⚪ **CASH** | **-0.4 bps** (±0.4) | `[-0.5, -0.1, +0.4, -0.6, -0.4]` | `-0.187` | `0.41%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 14:18:56 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,062.67 | ⚪ **CASH** | **+1.1 bps** (±0.7) | `[+0.6, +1.6, +0.9, +1.5, +2.7]` | `-0.028` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,560.24 | ⚪ **CASH** | **-1.2 bps** (±0.4) | `[-1.6, -0.8, -1.3, -0.9, -0.4]` | `-0.009` | `0.42%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.85 | ⚪ **CASH** | **-0.4 bps** (±0.4) | `[-0.5, -0.1, +0.4, -0.6, -0.4]` | `-0.187` | `0.41%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 14:02:43 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,117.00 | ⚪ **CASH** | **+1.1 bps** (±0.7) | `[+0.6, +1.6, +0.9, +1.5, +2.7]` | `-0.028` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,566.21 | ⚪ **CASH** | **-1.2 bps** (±0.4) | `[-1.6, -0.8, -1.3, -0.9, -0.4]` | `-0.009` | `0.42%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.11 | ⚪ **CASH** | **-0.4 bps** (±0.4) | `[-0.5, -0.1, +0.4, -0.6, -0.4]` | `-0.187` | `0.41%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 13:47:21 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,901.46 | ⚪ **CASH** | **+0.9 bps** (±0.7) | `[+0.4, +1.4, +0.6, +1.3, +2.3]` | `-0.004` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,556.34 | ⚪ **CASH** | **-1.3 bps** (±0.4) | `[-1.6, -1.0, -1.3, -1.1, -0.2]` | `+0.014` | `0.43%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.62 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-1.3, -0.6, -1.1, -0.6, -0.4]` | `-0.192` | `0.42%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 13:32:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,408.00 | ⚪ **CASH** | **+0.9 bps** (±0.7) | `[+0.4, +1.4, +0.6, +1.3, +2.3]` | `-0.004` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,567.49 | ⚪ **CASH** | **-1.3 bps** (±0.4) | `[-1.6, -1.0, -1.3, -1.1, -0.2]` | `+0.014` | `0.43%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.41 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-1.3, -0.6, -1.1, -0.6, -0.4]` | `-0.192` | `0.42%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 13:16:57 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,413.55 | ⚪ **CASH** | **+0.9 bps** (±0.7) | `[+0.4, +1.4, +0.6, +1.3, +2.3]` | `-0.004` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,562.92 | ⚪ **CASH** | **-1.3 bps** (±0.4) | `[-1.6, -1.0, -1.3, -1.1, -0.2]` | `+0.014` | `0.43%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.29 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-1.3, -0.6, -1.1, -0.6, -0.4]` | `-0.192` | `0.42%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 13:02:07 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,446.42 | ⚪ **CASH** | **+0.9 bps** (±0.7) | `[+0.4, +1.4, +0.6, +1.3, +2.3]` | `-0.004` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,566.91 | ⚪ **CASH** | **-1.3 bps** (±0.4) | `[-1.6, -1.0, -1.3, -1.1, -0.2]` | `+0.014` | `0.43%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.34 | ⚪ **CASH** | **-1.0 bps** (±0.4) | `[-1.3, -0.6, -1.1, -0.6, -0.4]` | `-0.192` | `0.42%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 12:47:24 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,461.64 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.1, +0.0, +0.1, +0.1, +0.2]` | `-0.009` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,568.22 | ⚪ **CASH** | **-2.0 bps** (±0.4) | `[-2.3, -1.3, -1.5, -2.2, -1.3]` | `-0.059` | `0.44%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.49 | ⚪ **CASH** | **-3.4 bps** (±0.5) | `[-3.7, -3.3, -3.4, -2.7, -2.3]` | `-0.181` | `0.40%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 12:32:15 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,510.02 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.1, +0.0, +0.1, +0.1, +0.2]` | `-0.009` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,574.05 | ⚪ **CASH** | **-2.0 bps** (±0.4) | `[-2.3, -1.3, -1.5, -2.2, -1.3]` | `-0.059` | `0.44%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.71 | ⚪ **CASH** | **-3.4 bps** (±0.5) | `[-3.7, -3.3, -3.4, -2.7, -2.3]` | `-0.181` | `0.40%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 12:17:26 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,586.01 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.1, +0.0, +0.1, +0.1, +0.2]` | `-0.009` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,580.00 | ⚪ **CASH** | **-2.0 bps** (±0.4) | `[-2.3, -1.3, -1.5, -2.2, -1.3]` | `-0.059` | `0.44%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.18 | ⚪ **CASH** | **-3.4 bps** (±0.5) | `[-3.7, -3.3, -3.4, -2.7, -2.3]` | `-0.181` | `0.40%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 12:02:21 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,616.91 | ⚪ **CASH** | **+0.0 bps** (±0.1) | `[-0.1, +0.0, +0.1, +0.1, +0.2]` | `-0.009` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,576.10 | ⚪ **CASH** | **-2.0 bps** (±0.4) | `[-2.3, -1.3, -1.5, -2.2, -1.3]` | `-0.059` | `0.44%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.20 | ⚪ **CASH** | **-3.4 bps** (±0.5) | `[-3.7, -3.3, -3.4, -2.7, -2.3]` | `-0.181` | `0.40%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 11:47:36 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,566.01 | ⚪ **CASH** | **+0.3 bps** (±0.3) | `[-0.1, +0.6, +0.5, +0.5, +0.6]` | `+0.012` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,573.52 | ⚪ **CASH** | **-2.0 bps** (±0.5) | `[-2.3, -1.3, -1.5, -2.3, -1.2]` | `-0.106` | `0.44%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.07 | ⚪ **CASH** | **-3.1 bps** (±0.5) | `[-3.7, -2.9, -2.2, -2.7, -2.3]` | `-0.125` | `0.41%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 11:32:21 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,662.00 | ⚪ **CASH** | **+0.3 bps** (±0.3) | `[-0.1, +0.6, +0.5, +0.5, +0.6]` | `+0.012` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,574.35 | ⚪ **CASH** | **-2.0 bps** (±0.5) | `[-2.3, -1.3, -1.5, -2.3, -1.2]` | `-0.106` | `0.44%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.23 | ⚪ **CASH** | **-3.1 bps** (±0.5) | `[-3.7, -2.9, -2.2, -2.7, -2.3]` | `-0.125` | `0.41%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 11:17:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,800.01 | ⚪ **CASH** | **+0.3 bps** (±0.3) | `[-0.1, +0.6, +0.5, +0.5, +0.6]` | `+0.012` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,582.01 | ⚪ **CASH** | **-2.0 bps** (±0.5) | `[-2.3, -1.3, -1.5, -2.3, -1.2]` | `-0.106` | `0.44%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.66 | ⚪ **CASH** | **-3.1 bps** (±0.5) | `[-3.7, -2.9, -2.2, -2.7, -2.3]` | `-0.125` | `0.41%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 11:02:15 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,788.39 | ⚪ **CASH** | **+0.3 bps** (±0.3) | `[-0.1, +0.6, +0.5, +0.5, +0.6]` | `+0.012` | `0.35%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,581.10 | ⚪ **CASH** | **-2.0 bps** (±0.5) | `[-2.3, -1.3, -1.5, -2.3, -1.2]` | `-0.106` | `0.44%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.67 | ⚪ **CASH** | **-3.1 bps** (±0.5) | `[-3.7, -2.9, -2.2, -2.7, -2.3]` | `-0.125` | `0.41%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 10:47:33 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,708.17 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.3, +0.5, +0.3]` | `+0.020` | `0.36%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,577.91 | ⚪ **CASH** | **-1.4 bps** (±0.2) | `[-1.6, -1.3, -1.1, -1.4, -1.4]` | `-0.165` | `0.44%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.56 | ⚪ **CASH** | **-3.1 bps** (±0.5) | `[-3.7, -2.9, -2.2, -2.7, -2.3]` | `-0.072` | `0.41%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 10:32:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,806.64 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.3, +0.5, +0.3]` | `+0.020` | `0.36%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,582.01 | ⚪ **CASH** | **-1.4 bps** (±0.2) | `[-1.6, -1.3, -1.1, -1.4, -1.4]` | `-0.165` | `0.44%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.69 | ⚪ **CASH** | **-3.1 bps** (±0.5) | `[-3.7, -2.9, -2.2, -2.7, -2.3]` | `-0.072` | `0.41%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 10:17:17 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,836.00 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.3, +0.5, +0.3]` | `+0.020` | `0.36%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,588.74 | ⚪ **CASH** | **-1.4 bps** (±0.2) | `[-1.6, -1.3, -1.1, -1.4, -1.4]` | `-0.165` | `0.44%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.55 | ⚪ **CASH** | **-3.1 bps** (±0.5) | `[-3.7, -2.9, -2.2, -2.7, -2.3]` | `-0.072` | `0.41%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 10:02:16 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,776.01 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.3, +0.5, +0.3]` | `+0.020` | `0.36%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,597.34 | ⚪ **CASH** | **-1.4 bps** (±0.2) | `[-1.6, -1.3, -1.1, -1.4, -1.4]` | `-0.165` | `0.44%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.76 | ⚪ **CASH** | **-3.1 bps** (±0.5) | `[-3.7, -2.9, -2.2, -2.7, -2.3]` | `-0.072` | `0.41%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 09:47:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,786.01 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.3, +0.5, +0.3]` | `+0.044` | `0.36%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,598.41 | ⚪ **CASH** | **-1.2 bps** (±0.5) | `[-0.0, -1.2, -0.8, -1.2, -1.4]` | `-0.208` | `0.44%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.81 | ⚪ **CASH** | **-1.2 bps** (±0.2) | `[-1.1, -1.3, -1.0, -0.9, -1.1]` | `-0.039` | `0.42%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 09:32:20 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,828.68 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.3, +0.5, +0.3]` | `+0.044` | `0.36%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,603.21 | ⚪ **CASH** | **-1.2 bps** (±0.5) | `[-0.0, -1.2, -0.8, -1.2, -1.4]` | `-0.208` | `0.44%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.02 | ⚪ **CASH** | **-1.2 bps** (±0.2) | `[-1.1, -1.3, -1.0, -0.9, -1.1]` | `-0.039` | `0.42%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 09:17:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,877.79 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.3, +0.5, +0.3]` | `+0.044` | `0.36%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,607.32 | ⚪ **CASH** | **-1.2 bps** (±0.5) | `[-0.0, -1.2, -0.8, -1.2, -1.4]` | `-0.208` | `0.44%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.12 | ⚪ **CASH** | **-1.2 bps** (±0.2) | `[-1.1, -1.3, -1.0, -0.9, -1.1]` | `-0.039` | `0.42%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 09:02:33 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,988.01 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.1, +0.5, +0.3, +0.5, +0.3]` | `+0.044` | `0.36%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,611.13 | ⚪ **CASH** | **-1.2 bps** (±0.5) | `[-0.0, -1.2, -0.8, -1.2, -1.4]` | `-0.208` | `0.44%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.25 | ⚪ **CASH** | **-1.2 bps** (±0.2) | `[-1.1, -1.3, -1.0, -0.9, -1.1]` | `-0.039` | `0.42%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 08:47:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,005.72 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.3, +0.3, +0.3, +0.5, +0.3]` | `+0.003` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,612.65 | ⚪ **CASH** | **-1.7 bps** (±0.2) | `[-1.8, -1.3, -1.5, -1.8, -1.6]` | `-0.321` | `0.44%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.44 | ⚪ **CASH** | **-1.9 bps** (±0.1) | `[-1.9, -1.9, -1.9, -1.6, -1.9]` | `-0.101` | `0.42%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 08:32:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,056.00 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.3, +0.3, +0.3, +0.5, +0.3]` | `+0.003` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,615.80 | ⚪ **CASH** | **-1.7 bps** (±0.2) | `[-1.8, -1.3, -1.5, -1.8, -1.6]` | `-0.321` | `0.44%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.49 | ⚪ **CASH** | **-1.9 bps** (±0.1) | `[-1.9, -1.9, -1.9, -1.6, -1.9]` | `-0.101` | `0.42%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 08:17:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,004.79 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.3, +0.3, +0.3, +0.5, +0.3]` | `+0.003` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,615.07 | ⚪ **CASH** | **-1.7 bps** (±0.2) | `[-1.8, -1.3, -1.5, -1.8, -1.6]` | `-0.321` | `0.44%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.50 | ⚪ **CASH** | **-1.9 bps** (±0.1) | `[-1.9, -1.9, -1.9, -1.6, -1.9]` | `-0.101` | `0.42%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 08:02:07 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,100.00 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.3, +0.3, +0.3, +0.5, +0.3]` | `+0.003` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,616.23 | ⚪ **CASH** | **-1.7 bps** (±0.2) | `[-1.8, -1.3, -1.5, -1.8, -1.6]` | `-0.321` | `0.44%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.60 | ⚪ **CASH** | **-1.9 bps** (±0.1) | `[-1.9, -1.9, -1.9, -1.6, -1.9]` | `-0.101` | `0.42%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 07:47:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,260.01 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.3, +0.2, +0.2, +0.5, -0.0]` | `-0.070` | `0.37%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,619.50 | ⚪ **CASH** | **-1.4 bps** (±0.2) | `[-1.5, -0.9, -1.3, -1.4, -1.5]` | `-0.367` | `0.45%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.82 | ⚪ **CASH** | **-2.1 bps** (±0.1) | `[-2.0, -2.1, -2.2, -2.0, -2.0]` | `-0.127` | `0.42%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 07:32:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,288.00 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.3, +0.2, +0.2, +0.5, -0.0]` | `-0.070` | `0.37%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,620.42 | ⚪ **CASH** | **-1.4 bps** (±0.2) | `[-1.5, -0.9, -1.3, -1.4, -1.5]` | `-0.367` | `0.45%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.79 | ⚪ **CASH** | **-2.1 bps** (±0.1) | `[-2.0, -2.1, -2.2, -2.0, -2.0]` | `-0.127` | `0.42%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-07 07:17:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,238.01 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.3, +0.2, +0.2, +0.5, -0.0]` | `-0.070` | `0.37%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,616.64 | ⚪ **CASH** | **-1.4 bps** (±0.2) | `[-1.5, -0.9, -1.3, -1.4, -1.5]` | `-0.367` | `0.45%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $118.85 | ⚪ **CASH** | **-2.1 bps** (±0.1) | `[-2.0, -2.1, -2.2, -2.0, -2.0]` | `-0.127` | `0.42%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |
