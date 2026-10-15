# 📋 BOT_TRADE V5 — Livro de Auditoria de Decisões e Análise de Mercado

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o consenso dos 5 modelos XGBoost, o comportamento do CVD (Cumulative Volume Delta) e o disparo de travas de risco.

**Última Atualização**: `2026-10-15 04:32:06 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-10-15 03:32:15 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,985.02 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.3, +0.3, +0.1, +0.1, -0.1]` | `-0.025` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,363.37 | ⚪ **CASH** | **-4.1 bps** (±0.9) | `[-4.2, -3.6, -2.6, -5.0, -2.8]` | `-0.107` | `0.52%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.38 | ⚪ **CASH** | **-5.0 bps** (±1.8) | `[-5.0, -6.1, -5.6, -1.6, -2.2]` | `-0.130` | `0.61%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 03:17:07 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,368.13 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.3, +0.3, +0.1, +0.1, -0.1]` | `-0.025` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,375.09 | ⚪ **CASH** | **-4.1 bps** (±0.9) | `[-4.2, -3.6, -2.6, -5.0, -2.8]` | `-0.107` | `0.52%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.88 | ⚪ **CASH** | **-5.0 bps** (±1.8) | `[-5.0, -6.1, -5.6, -1.6, -2.2]` | `-0.130` | `0.61%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 03:02:33 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,189.41 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.3, +0.3, +0.1, +0.1, -0.1]` | `-0.025` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,367.13 | ⚪ **CASH** | **-4.1 bps** (±0.9) | `[-4.2, -3.6, -2.6, -5.0, -2.8]` | `-0.107` | `0.52%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.43 | ⚪ **CASH** | **-5.0 bps** (±1.8) | `[-5.0, -6.1, -5.6, -1.6, -2.2]` | `-0.130` | `0.61%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 02:46:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,276.01 | ⚪ **CASH** | **-0.4 bps** (±0.2) | `[-0.7, -0.2, -0.1, -0.3, -0.3]` | `-0.033` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,372.35 | ⚪ **CASH** | **-2.0 bps** (±0.3) | `[-1.8, -1.3, -1.8, -2.2, -2.0]` | `-0.117` | `0.47%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $103.22 | ⚪ **CASH** | **-2.1 bps** (±0.4) | `[-2.1, -1.9, -1.5, -1.6, -2.5]` | `+0.028` | `0.61%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 02:32:09 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,661.25 | ⚪ **CASH** | **-0.4 bps** (±0.2) | `[-0.7, -0.2, -0.1, -0.3, -0.3]` | `-0.033` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,348.22 | ⚪ **CASH** | **-2.0 bps** (±0.3) | `[-1.8, -1.3, -1.8, -2.2, -2.0]` | `-0.117` | `0.47%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $101.63 | ⚪ **CASH** | **-2.1 bps** (±0.4) | `[-2.1, -1.9, -1.5, -1.6, -2.5]` | `+0.028` | `0.61%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 02:17:07 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,506.00 | ⚪ **CASH** | **-0.4 bps** (±0.2) | `[-0.7, -0.2, -0.1, -0.3, -0.3]` | `-0.033` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,408.01 | ⚪ **CASH** | **-2.0 bps** (±0.3) | `[-1.8, -1.3, -1.8, -2.2, -2.0]` | `-0.117` | `0.47%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $103.65 | ⚪ **CASH** | **-2.1 bps** (±0.4) | `[-2.1, -1.9, -1.5, -1.6, -2.5]` | `+0.028` | `0.61%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 02:02:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,574.01 | ⚪ **CASH** | **-0.4 bps** (±0.2) | `[-0.7, -0.2, -0.1, -0.3, -0.3]` | `-0.033` | `0.32%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,410.33 | ⚪ **CASH** | **-2.0 bps** (±0.3) | `[-1.8, -1.3, -1.8, -2.2, -2.0]` | `-0.117` | `0.47%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $103.82 | ⚪ **CASH** | **-2.1 bps** (±0.4) | `[-2.1, -1.9, -1.5, -1.6, -2.5]` | `+0.028` | `0.61%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 01:47:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,802.01 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.037` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,420.19 | ⚪ **CASH** | **-1.8 bps** (±0.2) | `[-1.8, -1.3, -1.8, -1.9, -1.7]` | `-0.122` | `0.48%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.42 | ⚪ **CASH** | **-2.4 bps** (±0.3) | `[-2.5, -2.1, -1.9, -2.0, -2.7]` | `+0.048` | `0.62%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 01:32:12 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,789.25 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.037` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,420.12 | ⚪ **CASH** | **-1.8 bps** (±0.2) | `[-1.8, -1.3, -1.8, -1.9, -1.7]` | `-0.122` | `0.48%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.52 | ⚪ **CASH** | **-2.4 bps** (±0.3) | `[-2.5, -2.1, -1.9, -2.0, -2.7]` | `+0.048` | `0.62%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 01:17:21 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,663.59 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.037` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,418.29 | ⚪ **CASH** | **-1.8 bps** (±0.2) | `[-1.8, -1.3, -1.8, -1.9, -1.7]` | `-0.122` | `0.48%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.34 | ⚪ **CASH** | **-2.4 bps** (±0.3) | `[-2.5, -2.1, -1.9, -2.0, -2.7]` | `+0.048` | `0.62%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 01:02:03 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,870.42 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.037` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,426.67 | ⚪ **CASH** | **-1.8 bps** (±0.2) | `[-1.8, -1.3, -1.8, -1.9, -1.7]` | `-0.122` | `0.48%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.79 | ⚪ **CASH** | **-2.4 bps** (±0.3) | `[-2.5, -2.1, -1.9, -2.0, -2.7]` | `+0.048` | `0.62%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 00:46:49 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,511.00 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.028` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,417.96 | ⚪ **CASH** | **-1.9 bps** (±0.3) | `[-1.8, -1.3, -1.6, -2.2, -1.8]` | `-0.064` | `0.49%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.34 | ⚪ **CASH** | **-2.5 bps** (±0.4) | `[-2.7, -2.5, -1.9, -2.0, -2.7]` | `-0.002` | `0.62%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 00:32:28 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,740.01 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.028` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,425.50 | ⚪ **CASH** | **-1.9 bps** (±0.3) | `[-1.8, -1.3, -1.6, -2.2, -1.8]` | `-0.064` | `0.49%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.51 | ⚪ **CASH** | **-2.5 bps** (±0.4) | `[-2.7, -2.5, -1.9, -2.0, -2.7]` | `-0.002` | `0.62%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 00:17:16 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,744.00 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.028` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,425.32 | ⚪ **CASH** | **-1.9 bps** (±0.3) | `[-1.8, -1.3, -1.6, -2.2, -1.8]` | `-0.064` | `0.49%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.47 | ⚪ **CASH** | **-2.5 bps** (±0.4) | `[-2.7, -2.5, -1.9, -2.0, -2.7]` | `-0.002` | `0.62%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 00:02:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,686.00 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `-0.028` | `0.33%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,422.23 | ⚪ **CASH** | **-1.9 bps** (±0.3) | `[-1.8, -1.3, -1.6, -2.2, -1.8]` | `-0.064` | `0.49%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.23 | ⚪ **CASH** | **-2.5 bps** (±0.4) | `[-2.7, -2.5, -1.9, -2.0, -2.7]` | `-0.002` | `0.62%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-14 23:46:56 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,641.74 | ⚪ **CASH** | **-0.2 bps** (±0.2) | `[-0.2, +0.1, +0.0, -0.4, -0.1]` | `-0.051` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,422.45 | ⚪ **CASH** | **-1.5 bps** (±0.2) | `[-1.3, -1.3, -1.1, -1.4, -1.7]` | `-0.082` | `0.49%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.34 | ⚪ **CASH** | **-2.1 bps** (±0.4) | `[-2.1, -1.9, -1.5, -1.6, -2.5]` | `+0.011` | `0.63%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-14 23:32:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,533.02 | ⚪ **CASH** | **-0.2 bps** (±0.2) | `[-0.2, +0.1, +0.0, -0.4, -0.1]` | `-0.051` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,417.52 | ⚪ **CASH** | **-1.5 bps** (±0.2) | `[-1.3, -1.3, -1.1, -1.4, -1.7]` | `-0.082` | `0.49%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.35 | ⚪ **CASH** | **-2.1 bps** (±0.4) | `[-2.1, -1.9, -1.5, -1.6, -2.5]` | `+0.011` | `0.63%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-14 23:16:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,646.00 | ⚪ **CASH** | **-0.2 bps** (±0.2) | `[-0.2, +0.1, +0.0, -0.4, -0.1]` | `-0.051` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,421.02 | ⚪ **CASH** | **-1.5 bps** (±0.2) | `[-1.3, -1.3, -1.1, -1.4, -1.7]` | `-0.082` | `0.49%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.62 | ⚪ **CASH** | **-2.1 bps** (±0.4) | `[-2.1, -1.9, -1.5, -1.6, -2.5]` | `+0.011` | `0.63%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-14 23:02:30 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,644.05 | ⚪ **CASH** | **-0.2 bps** (±0.2) | `[-0.2, +0.1, +0.0, -0.4, -0.1]` | `-0.051` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,418.61 | ⚪ **CASH** | **-1.5 bps** (±0.2) | `[-1.3, -1.3, -1.1, -1.4, -1.7]` | `-0.082` | `0.49%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.54 | ⚪ **CASH** | **-2.1 bps** (±0.4) | `[-2.1, -1.9, -1.5, -1.6, -2.5]` | `+0.011` | `0.63%/h` | `vol_compressed` `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-14 22:46:57 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,522.00 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `+0.012` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,414.64 | ⚪ **CASH** | **-1.8 bps** (±0.2) | `[-1.8, -1.3, -1.5, -1.9, -1.6]` | `-0.052` | `0.50%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.34 | ⚪ **CASH** | **-2.5 bps** (±0.4) | `[-2.7, -2.5, -1.9, -2.0, -2.7]` | `+0.080` | `0.64%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-14 22:32:20 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,644.01 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `+0.012` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,418.30 | ⚪ **CASH** | **-1.8 bps** (±0.2) | `[-1.8, -1.3, -1.5, -1.9, -1.6]` | `-0.052` | `0.50%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.58 | ⚪ **CASH** | **-2.5 bps** (±0.4) | `[-2.7, -2.5, -1.9, -2.0, -2.7]` | `+0.080` | `0.64%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-14 22:17:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,666.01 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `+0.012` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,412.64 | ⚪ **CASH** | **-1.8 bps** (±0.2) | `[-1.8, -1.3, -1.5, -1.9, -1.6]` | `-0.052` | `0.50%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.48 | ⚪ **CASH** | **-2.5 bps** (±0.4) | `[-2.7, -2.5, -1.9, -2.0, -2.7]` | `+0.080` | `0.64%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-14 22:02:10 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,747.24 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.1, -0.4, -0.3]` | `+0.012` | `0.34%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,420.34 | ⚪ **CASH** | **-1.8 bps** (±0.2) | `[-1.8, -1.3, -1.5, -1.9, -1.6]` | `-0.052` | `0.50%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.79 | ⚪ **CASH** | **-2.5 bps** (±0.4) | `[-2.7, -2.5, -1.9, -2.0, -2.7]` | `+0.080` | `0.64%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-14 21:47:12 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,946.68 | ⚪ **CASH** | **-0.4 bps** (±0.2) | `[-0.7, -0.3, -0.1, -0.4, -0.3]` | `+0.025` | `0.35%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,426.06 | ⚪ **CASH** | **-2.0 bps** (±0.4) | `[-2.3, -1.3, -1.8, -2.2, -1.5]` | `-0.157` | `0.51%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.83 | ⚪ **CASH** | **-2.0 bps** (±0.2) | `[-2.1, -1.9, -1.5, -1.8, -2.0]` | `+0.036` | `0.64%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-14 21:32:12 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,931.83 | ⚪ **CASH** | **-0.4 bps** (±0.2) | `[-0.7, -0.3, -0.1, -0.4, -0.3]` | `+0.025` | `0.35%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,427.08 | ⚪ **CASH** | **-2.0 bps** (±0.4) | `[-2.3, -1.3, -1.8, -2.2, -1.5]` | `-0.157` | `0.51%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.85 | ⚪ **CASH** | **-2.0 bps** (±0.2) | `[-2.1, -1.9, -1.5, -1.8, -2.0]` | `+0.036` | `0.64%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-14 21:17:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,808.00 | ⚪ **CASH** | **-0.4 bps** (±0.2) | `[-0.7, -0.3, -0.1, -0.4, -0.3]` | `+0.025` | `0.35%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,418.34 | ⚪ **CASH** | **-2.0 bps** (±0.4) | `[-2.3, -1.3, -1.8, -2.2, -1.5]` | `-0.157` | `0.51%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.17 | ⚪ **CASH** | **-2.0 bps** (±0.2) | `[-2.1, -1.9, -1.5, -1.8, -2.0]` | `+0.036` | `0.64%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-14 21:02:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,822.56 | ⚪ **CASH** | **-0.4 bps** (±0.2) | `[-0.7, -0.3, -0.1, -0.4, -0.3]` | `+0.025` | `0.35%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,417.50 | ⚪ **CASH** | **-2.0 bps** (±0.4) | `[-2.3, -1.3, -1.8, -2.2, -1.5]` | `-0.157` | `0.51%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.17 | ⚪ **CASH** | **-2.0 bps** (±0.2) | `[-2.1, -1.9, -1.5, -1.8, -2.0]` | `+0.036` | `0.64%/h` | `btc_dumping` `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-14 20:47:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,717.13 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.3, -0.4, -0.3]` | `+0.035` | `0.35%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,419.63 | ⚪ **CASH** | **-1.9 bps** (±0.3) | `[-1.8, -1.3, -1.6, -2.2, -1.8]` | `-0.227` | `0.51%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $103.93 | ⚪ **CASH** | **-2.1 bps** (±0.1) | `[-2.3, -2.1, -1.9, -2.0, -2.0]` | `+0.030` | `0.65%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-14 20:32:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,806.01 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.3, -0.4, -0.3]` | `+0.035` | `0.35%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,418.39 | ⚪ **CASH** | **-1.9 bps** (±0.3) | `[-1.8, -1.3, -1.6, -2.2, -1.8]` | `-0.227` | `0.51%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $103.92 | ⚪ **CASH** | **-2.1 bps** (±0.1) | `[-2.3, -2.1, -1.9, -2.0, -2.0]` | `+0.030` | `0.65%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-14 20:17:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,944.51 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.3, -0.4, -0.3]` | `+0.035` | `0.35%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,432.27 | ⚪ **CASH** | **-1.9 bps** (±0.3) | `[-1.8, -1.3, -1.6, -2.2, -1.8]` | `-0.227` | `0.51%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.24 | ⚪ **CASH** | **-2.1 bps** (±0.1) | `[-2.3, -2.1, -1.9, -2.0, -2.0]` | `+0.030` | `0.65%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-14 20:02:20 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,898.09 | ⚪ **CASH** | **-0.4 bps** (±0.1) | `[-0.5, -0.3, -0.3, -0.4, -0.3]` | `+0.035` | `0.35%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,434.39 | ⚪ **CASH** | **-1.9 bps** (±0.3) | `[-1.8, -1.3, -1.6, -2.2, -1.8]` | `-0.227` | `0.51%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.36 | ⚪ **CASH** | **-2.1 bps** (±0.1) | `[-2.3, -2.1, -1.9, -2.0, -2.0]` | `+0.030` | `0.65%/h` | `alt_downtrend` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-14 19:46:58 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,713.94 | ⚪ **CASH** | **-0.5 bps** (±0.2) | `[-0.5, -0.3, -0.3, -0.7, -0.3]` | `-0.028` | `0.35%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,429.08 | ⚪ **CASH** | **-1.9 bps** (±0.3) | `[-1.8, -1.3, -1.6, -2.2, -1.8]` | `-0.266` | `0.51%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $104.21 | ⚪ **CASH** | **-1.8 bps** (±0.2) | `[-1.9, -1.9, -1.5, -1.6, -1.9]` | `+0.029` | `0.66%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
