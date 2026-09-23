# 📋 BOT_TRADE V5 — Livro de Auditoria de Decisões e Análise de Mercado

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o consenso dos 5 modelos XGBoost, o comportamento do CVD (Cumulative Volume Delta) e o disparo de travas de risco.

**Última Atualização**: `2026-09-23 23:02:32 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-09-23 18:32:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,168.09 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[+0.6, +0.2, +0.4, -0.1, +0.2]` | `-0.108` | `0.47%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,661.55 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.2, -0.2, +0.2, -0.3, -0.3]` | `-0.079` | `0.47%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.11 | ⚪ **CASH** | **-0.9 bps** (±0.5) | `[-0.7, +0.1, -0.5, -1.2, -1.1]` | `-0.133` | `0.59%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 18:17:19 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,197.95 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[+0.6, +0.2, +0.4, -0.1, +0.2]` | `-0.108` | `0.47%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,662.80 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.2, -0.2, +0.2, -0.3, -0.3]` | `-0.079` | `0.47%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.14 | ⚪ **CASH** | **-0.9 bps** (±0.5) | `[-0.7, +0.1, -0.5, -1.2, -1.1]` | `-0.133` | `0.59%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 18:02:23 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,308.82 | ⚪ **CASH** | **+0.1 bps** (±0.2) | `[+0.6, +0.2, +0.4, -0.1, +0.2]` | `-0.108` | `0.47%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,667.06 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.2, -0.2, +0.2, -0.3, -0.3]` | `-0.079` | `0.47%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.35 | ⚪ **CASH** | **-0.9 bps** (±0.5) | `[-0.7, +0.1, -0.5, -1.2, -1.1]` | `-0.133` | `0.59%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 17:47:31 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,334.38 | ⚪ **CASH** | **+1.1 bps** (±0.8) | `[+2.4, +1.7, +2.0, +1.3, +0.0]` | `-0.140` | `0.47%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,667.95 | ⚪ **CASH** | **+0.5 bps** (±0.4) | `[+0.7, +1.1, +0.7, -0.0, +0.8]` | `-0.103` | `0.47%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.69 | ⚪ **CASH** | **-1.2 bps** (±0.4) | `[-1.4, -0.4, -0.9, -1.4, -1.1]` | `-0.141` | `0.59%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 17:32:03 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,043.81 | ⚪ **CASH** | **+1.1 bps** (±0.8) | `[+2.4, +1.7, +2.0, +1.3, +0.0]` | `-0.140` | `0.47%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,662.47 | ⚪ **CASH** | **+0.5 bps** (±0.4) | `[+0.7, +1.1, +0.7, -0.0, +0.8]` | `-0.103` | `0.47%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.23 | ⚪ **CASH** | **-1.2 bps** (±0.4) | `[-1.4, -0.4, -0.9, -1.4, -1.1]` | `-0.141` | `0.59%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 17:17:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,950.01 | ⚪ **CASH** | **+1.1 bps** (±0.8) | `[+2.4, +1.7, +2.0, +1.3, +0.0]` | `-0.140` | `0.47%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,657.98 | ⚪ **CASH** | **+0.5 bps** (±0.4) | `[+0.7, +1.1, +0.7, -0.0, +0.8]` | `-0.103` | `0.47%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.16 | ⚪ **CASH** | **-1.2 bps** (±0.4) | `[-1.4, -0.4, -0.9, -1.4, -1.1]` | `-0.141` | `0.59%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 17:02:22 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,970.00 | ⚪ **CASH** | **+1.1 bps** (±0.8) | `[+2.4, +1.7, +2.0, +1.3, +0.0]` | `-0.140` | `0.47%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,657.62 | ⚪ **CASH** | **+0.5 bps** (±0.4) | `[+0.7, +1.1, +0.7, -0.0, +0.8]` | `-0.103` | `0.47%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.10 | ⚪ **CASH** | **-1.2 bps** (±0.4) | `[-1.4, -0.4, -0.9, -1.4, -1.1]` | `-0.141` | `0.59%/h` | `btc_dumping` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 16:47:10 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,014.01 | ⚪ **CASH** | **+0.5 bps** (±1.1) | `[+2.6, +1.5, -0.5, +0.1, +1.6]` | `-0.128` | `0.48%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,661.98 | ⚪ **CASH** | **+3.0 bps** (±0.4) | `[+3.3, +3.8, +2.7, +3.2, +2.9]` | `-0.137` | `0.48%/h` | `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.39 | ⚪ **CASH** | **+2.5 bps** (±0.8) | `[+3.3, +2.9, +4.2, +2.4, +1.8]` | `-0.124` | `0.60%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 16:32:30 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,258.01 | ⚪ **CASH** | **+0.5 bps** (±1.1) | `[+2.6, +1.5, -0.5, +0.1, +1.6]` | `-0.128` | `0.48%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,665.55 | ⚪ **CASH** | **+3.0 bps** (±0.4) | `[+3.3, +3.8, +2.7, +3.2, +2.9]` | `-0.137` | `0.48%/h` | `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.72 | ⚪ **CASH** | **+2.5 bps** (±0.8) | `[+3.3, +2.9, +4.2, +2.4, +1.8]` | `-0.124` | `0.60%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 16:16:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,298.01 | ⚪ **CASH** | **+0.5 bps** (±1.1) | `[+2.6, +1.5, -0.5, +0.1, +1.6]` | `-0.128` | `0.48%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,663.26 | ⚪ **CASH** | **+3.0 bps** (±0.4) | `[+3.3, +3.8, +2.7, +3.2, +2.9]` | `-0.137` | `0.48%/h` | `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.92 | ⚪ **CASH** | **+2.5 bps** (±0.8) | `[+3.3, +2.9, +4.2, +2.4, +1.8]` | `-0.124` | `0.60%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 16:02:22 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,546.08 | ⚪ **CASH** | **+0.5 bps** (±1.1) | `[+2.6, +1.5, -0.5, +0.1, +1.6]` | `-0.128` | `0.48%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,637.41 | ⚪ **CASH** | **+3.0 bps** (±0.4) | `[+3.3, +3.8, +2.7, +3.2, +2.9]` | `-0.137` | `0.48%/h` | `btc_dumping` | Aguardando sinal com assimetria |
| **SOLUSDT** | $113.25 | ⚪ **CASH** | **+2.5 bps** (±0.8) | `[+3.3, +2.9, +4.2, +2.4, +1.8]` | `-0.124` | `0.60%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 15:46:55 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,290.01 | ⚪ **CASH** | **+2.0 bps** (±0.5) | `[+2.9, +2.1, +1.5, +2.2, +2.4]` | `-0.112` | `0.47%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,662.05 | ⚪ **CASH** | **+2.6 bps** (±0.2) | `[+2.9, +3.1, +2.5, +2.6, +2.5]` | `-0.124` | `0.48%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.36 | ⚪ **CASH** | **+2.2 bps** (±2.1) | `[+5.5, +6.0, +2.1, +2.1, +0.7]` | `-0.096` | `0.58%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 15:32:23 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,415.52 | ⚪ **CASH** | **+2.0 bps** (±0.5) | `[+2.9, +2.1, +1.5, +2.2, +2.4]` | `-0.112` | `0.47%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,669.19 | ⚪ **CASH** | **+2.6 bps** (±0.2) | `[+2.9, +3.1, +2.5, +2.6, +2.5]` | `-0.124` | `0.48%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.79 | ⚪ **CASH** | **+2.2 bps** (±2.1) | `[+5.5, +6.0, +2.1, +2.1, +0.7]` | `-0.096` | `0.58%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 15:17:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,697.42 | ⚪ **CASH** | **+2.0 bps** (±0.5) | `[+2.9, +2.1, +1.5, +2.2, +2.4]` | `-0.112` | `0.47%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,680.29 | ⚪ **CASH** | **+2.6 bps** (±0.2) | `[+2.9, +3.1, +2.5, +2.6, +2.5]` | `-0.124` | `0.48%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.71 | ⚪ **CASH** | **+2.2 bps** (±2.1) | `[+5.5, +6.0, +2.1, +2.1, +0.7]` | `-0.096` | `0.58%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 15:02:36 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,625.98 | ⚪ **CASH** | **+2.0 bps** (±0.5) | `[+2.9, +2.1, +1.5, +2.2, +2.4]` | `-0.112` | `0.47%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,681.29 | ⚪ **CASH** | **+2.6 bps** (±0.2) | `[+2.9, +3.1, +2.5, +2.6, +2.5]` | `-0.124` | `0.48%/h` | `btc_dumping` `turbulent_chop` | Aguardando sinal com assimetria |
| **SOLUSDT** | $115.45 | ⚪ **CASH** | **+2.2 bps** (±2.1) | `[+5.5, +6.0, +2.1, +2.1, +0.7]` | `-0.096` | `0.58%/h` | `btc_dumping` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 14:47:25 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,214.29 | ⚪ **CASH** | **+0.4 bps** (±0.3) | `[+1.2, +0.3, +0.5, +0.4, +0.5]` | `-0.099` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,663.31 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.4, -0.1, +0.0, -0.4, -0.2]` | `-0.194` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.21 | ⚪ **CASH** | **-1.0 bps** (±0.3) | `[-1.1, -0.6, -0.4, -1.3, -0.6]` | `-0.048` | `0.53%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 14:32:18 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,012.94 | ⚪ **CASH** | **+0.4 bps** (±0.3) | `[+1.2, +0.3, +0.5, +0.4, +0.5]` | `-0.099` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,654.86 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.4, -0.1, +0.0, -0.4, -0.2]` | `-0.194` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $113.46 | ⚪ **CASH** | **-1.0 bps** (±0.3) | `[-1.1, -0.6, -0.4, -1.3, -0.6]` | `-0.048` | `0.53%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-23 14:16:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,622.46 | ⚪ **CASH** | **+0.4 bps** (±0.3) | `[+1.2, +0.3, +0.5, +0.4, +0.5]` | `-0.099` | `0.39%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,671.03 | ⚪ **CASH** | **-0.3 bps** (±0.2) | `[-0.4, -0.1, +0.0, -0.4, -0.2]` | `-0.194` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $114.25 | ⚪ **CASH** | **-1.0 bps** (±0.3) | `[-1.1, -0.6, -0.4, -1.3, -0.6]` | `-0.048` | `0.53%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |
