# 📋 BOT_TRADE V5 — Livro de Auditoria de Decisões e Análise de Mercado

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o consenso dos 5 modelos XGBoost, o comportamento do CVD (Cumulative Volume Delta) e o disparo de travas de risco.

**Última Atualização**: `2026-10-16 00:02:15 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-16 00:02:15 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,252.60 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.0, +0.2, +0.3, +0.0, +0.0]` | `-0.224` | `0.52%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,442.64 | ⚪ **CASH** | **+1.3 bps** (±0.3) | `[+1.4, +1.5, +0.9, +1.8, +1.5]` | `-0.044` | `0.71%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.49 | ⚪ **CASH** | **+1.5 bps** (±0.4) | `[+2.1, +2.1, +1.2, +2.0, +1.3]` | `-0.008` | `0.84%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 23:47:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,199.99 | ⚪ **CASH** | **-0.2 bps** (±0.1) | `[-0.1, -0.2, +0.1, -0.3, -0.2]` | `-0.194` | `0.52%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,441.28 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.5, +0.5, +0.1, +0.3, +0.2]` | `+0.060` | `0.71%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.42 | ⚪ **CASH** | **-0.5 bps** (±0.3) | `[+0.0, -0.9, -0.1, -0.5, -0.4]` | `+0.008` | `0.85%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 23:32:16 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,230.01 | ⚪ **CASH** | **-0.2 bps** (±0.1) | `[-0.1, -0.2, +0.1, -0.3, -0.2]` | `-0.194` | `0.52%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,443.77 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.5, +0.5, +0.1, +0.3, +0.2]` | `+0.060` | `0.71%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.44 | ⚪ **CASH** | **-0.5 bps** (±0.3) | `[+0.0, -0.9, -0.1, -0.5, -0.4]` | `+0.008` | `0.85%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 23:16:52 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,196.00 | ⚪ **CASH** | **-0.2 bps** (±0.1) | `[-0.1, -0.2, +0.1, -0.3, -0.2]` | `-0.194` | `0.52%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,441.61 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.5, +0.5, +0.1, +0.3, +0.2]` | `+0.060` | `0.71%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.41 | ⚪ **CASH** | **-0.5 bps** (±0.3) | `[+0.0, -0.9, -0.1, -0.5, -0.4]` | `+0.008` | `0.85%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 23:02:16 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,346.00 | ⚪ **CASH** | **-0.2 bps** (±0.1) | `[-0.1, -0.2, +0.1, -0.3, -0.2]` | `-0.194` | `0.52%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,452.66 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.5, +0.5, +0.1, +0.3, +0.2]` | `+0.060` | `0.71%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.58 | ⚪ **CASH** | **-0.5 bps** (±0.3) | `[+0.0, -0.9, -0.1, -0.5, -0.4]` | `+0.008` | `0.85%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 22:47:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,495.86 | ⚪ **CASH** | **-0.2 bps** (±0.1) | `[-0.3, -0.2, -0.1, -0.3, -0.2]` | `-0.171` | `0.53%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,458.09 | ⚪ **CASH** | **+0.3 bps** (±0.2) | `[+0.4, +0.5, +0.1, +0.6, +0.4]` | `+0.092` | `0.72%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.87 | ⚪ **CASH** | **-0.6 bps** (±0.4) | `[-0.3, -0.8, +0.1, -0.8, -0.4]` | `+0.010` | `0.86%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 22:32:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,455.01 | ⚪ **CASH** | **-0.2 bps** (±0.1) | `[-0.3, -0.2, -0.1, -0.3, -0.2]` | `-0.171` | `0.53%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,458.51 | ⚪ **CASH** | **+0.3 bps** (±0.2) | `[+0.4, +0.5, +0.1, +0.6, +0.4]` | `+0.092` | `0.72%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.92 | ⚪ **CASH** | **-0.6 bps** (±0.4) | `[-0.3, -0.8, +0.1, -0.8, -0.4]` | `+0.010` | `0.86%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 22:17:10 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,434.75 | ⚪ **CASH** | **-0.2 bps** (±0.1) | `[-0.3, -0.2, -0.1, -0.3, -0.2]` | `-0.171` | `0.53%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,461.74 | ⚪ **CASH** | **+0.3 bps** (±0.2) | `[+0.4, +0.5, +0.1, +0.6, +0.4]` | `+0.092` | `0.72%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.07 | ⚪ **CASH** | **-0.6 bps** (±0.4) | `[-0.3, -0.8, +0.1, -0.8, -0.4]` | `+0.010` | `0.86%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 22:02:12 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,562.01 | ⚪ **CASH** | **-0.2 bps** (±0.1) | `[-0.3, -0.2, -0.1, -0.3, -0.2]` | `-0.171` | `0.53%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,466.59 | ⚪ **CASH** | **+0.3 bps** (±0.2) | `[+0.4, +0.5, +0.1, +0.6, +0.4]` | `+0.092` | `0.72%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.25 | ⚪ **CASH** | **-0.6 bps** (±0.4) | `[-0.3, -0.8, +0.1, -0.8, -0.4]` | `+0.010` | `0.86%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 21:47:09 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,220.87 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.4, +0.6, +0.5, +0.2, +0.2]` | `-0.133` | `0.53%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,456.49 | ⚪ **CASH** | **+1.6 bps** (±0.6) | `[+1.7, +1.9, +1.0, +2.3, +2.9]` | `+0.148` | `0.74%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.90 | ⚪ **CASH** | **+1.8 bps** (±0.4) | `[+2.2, +1.4, +1.8, +2.6, +1.8]` | `+0.026` | `0.88%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 21:32:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,331.07 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.4, +0.6, +0.5, +0.2, +0.2]` | `-0.133` | `0.53%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,461.03 | ⚪ **CASH** | **+1.6 bps** (±0.6) | `[+1.7, +1.9, +1.0, +2.3, +2.9]` | `+0.148` | `0.74%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.13 | ⚪ **CASH** | **+1.8 bps** (±0.4) | `[+2.2, +1.4, +1.8, +2.6, +1.8]` | `+0.026` | `0.88%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 21:17:02 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,164.28 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.4, +0.6, +0.5, +0.2, +0.2]` | `-0.133` | `0.53%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,453.33 | ⚪ **CASH** | **+1.6 bps** (±0.6) | `[+1.7, +1.9, +1.0, +2.3, +2.9]` | `+0.148` | `0.74%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.83 | ⚪ **CASH** | **+1.8 bps** (±0.4) | `[+2.2, +1.4, +1.8, +2.6, +1.8]` | `+0.026` | `0.88%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 21:02:07 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,038.49 | ⚪ **CASH** | **+0.3 bps** (±0.1) | `[+0.4, +0.6, +0.5, +0.2, +0.2]` | `-0.133` | `0.53%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,450.77 | ⚪ **CASH** | **+1.6 bps** (±0.6) | `[+1.7, +1.9, +1.0, +2.3, +2.9]` | `+0.148` | `0.74%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.56 | ⚪ **CASH** | **+1.8 bps** (±0.4) | `[+2.2, +1.4, +1.8, +2.6, +1.8]` | `+0.026` | `0.88%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 20:47:00 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,394.01 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.3, -0.1, +0.2, +0.3, +0.2]` | `-0.049` | `0.54%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,461.19 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.3, +0.3, +0.0, +0.6, +0.4]` | `+0.184` | `0.75%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.08 | ⚪ **CASH** | **-1.3 bps** (±0.6) | `[-0.3, -0.5, -2.1, -0.8, -1.2]` | `+0.070` | `0.89%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 20:32:02 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,379.53 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.3, -0.1, +0.2, +0.3, +0.2]` | `-0.049` | `0.54%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,461.15 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.3, +0.3, +0.0, +0.6, +0.4]` | `+0.184` | `0.75%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.99 | ⚪ **CASH** | **-1.3 bps** (±0.6) | `[-0.3, -0.5, -2.1, -0.8, -1.2]` | `+0.070` | `0.89%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 20:17:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,342.90 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.3, -0.1, +0.2, +0.3, +0.2]` | `-0.049` | `0.54%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,458.27 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.3, +0.3, +0.0, +0.6, +0.4]` | `+0.184` | `0.75%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.00 | ⚪ **CASH** | **-1.3 bps** (±0.6) | `[-0.3, -0.5, -2.1, -0.8, -1.2]` | `+0.070` | `0.89%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 20:02:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,380.01 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.3, -0.1, +0.2, +0.3, +0.2]` | `-0.049` | `0.54%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,453.07 | ⚪ **CASH** | **+0.2 bps** (±0.2) | `[+0.3, +0.3, +0.0, +0.6, +0.4]` | `+0.184` | `0.75%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.95 | ⚪ **CASH** | **-1.3 bps** (±0.6) | `[-0.3, -0.5, -2.1, -0.8, -1.2]` | `+0.070` | `0.89%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 19:47:02 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,449.36 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, -0.1, +0.2, +0.3, +0.2]` | `-0.074` | `0.55%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,456.95 | ⚪ **CASH** | **+0.2 bps** (±0.1) | `[+0.3, +0.2, +0.0, +0.4, +0.4]` | `+0.152` | `0.76%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.09 | ⚪ **CASH** | **-1.3 bps** (±0.6) | `[-0.3, -0.5, -2.1, -0.8, -1.2]` | `+0.052` | `0.90%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 19:32:06 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,444.50 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, -0.1, +0.2, +0.3, +0.2]` | `-0.074` | `0.55%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,453.94 | ⚪ **CASH** | **+0.2 bps** (±0.1) | `[+0.3, +0.2, +0.0, +0.4, +0.4]` | `+0.152` | `0.76%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.83 | ⚪ **CASH** | **-1.3 bps** (±0.6) | `[-0.3, -0.5, -2.1, -0.8, -1.2]` | `+0.052` | `0.90%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 19:17:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,530.01 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, -0.1, +0.2, +0.3, +0.2]` | `-0.074` | `0.55%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,455.28 | ⚪ **CASH** | **+0.2 bps** (±0.1) | `[+0.3, +0.2, +0.0, +0.4, +0.4]` | `+0.152` | `0.76%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.20 | ⚪ **CASH** | **-1.3 bps** (±0.6) | `[-0.3, -0.5, -2.1, -0.8, -1.2]` | `+0.052` | `0.90%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 19:02:36 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,461.12 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, -0.1, +0.2, +0.3, +0.2]` | `-0.074` | `0.55%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,453.05 | ⚪ **CASH** | **+0.2 bps** (±0.1) | `[+0.3, +0.2, +0.0, +0.4, +0.4]` | `+0.152` | `0.76%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.18 | ⚪ **CASH** | **-1.3 bps** (±0.6) | `[-0.3, -0.5, -2.1, -0.8, -1.2]` | `+0.052` | `0.90%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 18:46:59 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,338.81 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `-0.087` | `0.55%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,450.13 | ⚪ **CASH** | **+0.5 bps** (±0.3) | `[+0.6, +0.8, +0.4, +0.4, +1.0]` | `+0.117` | `0.77%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.83 | ⚪ **CASH** | **-0.4 bps** (±0.5) | `[+0.2, -0.5, +0.4, -0.8, -0.1]` | `+0.020` | `0.91%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 18:32:02 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,207.63 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `-0.087` | `0.55%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,441.92 | ⚪ **CASH** | **+0.5 bps** (±0.3) | `[+0.6, +0.8, +0.4, +0.4, +1.0]` | `+0.117` | `0.77%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.47 | ⚪ **CASH** | **-0.4 bps** (±0.5) | `[+0.2, -0.5, +0.4, -0.8, -0.1]` | `+0.020` | `0.91%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 18:17:07 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,188.01 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `-0.087` | `0.55%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,438.90 | ⚪ **CASH** | **+0.5 bps** (±0.3) | `[+0.6, +0.8, +0.4, +0.4, +1.0]` | `+0.117` | `0.77%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.40 | ⚪ **CASH** | **-0.4 bps** (±0.5) | `[+0.2, -0.5, +0.4, -0.8, -0.1]` | `+0.020` | `0.91%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 18:02:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,366.26 | ⚪ **CASH** | **+0.1 bps** (±0.0) | `[+0.1, +0.0, +0.2, +0.1, +0.2]` | `-0.087` | `0.55%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,442.54 | ⚪ **CASH** | **+0.5 bps** (±0.3) | `[+0.6, +0.8, +0.4, +0.4, +1.0]` | `+0.117` | `0.77%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.68 | ⚪ **CASH** | **-0.4 bps** (±0.5) | `[+0.2, -0.5, +0.4, -0.8, -0.1]` | `+0.020` | `0.91%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 17:47:03 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,516.00 | ⚪ **CASH** | **+0.9 bps** (±0.2) | `[+0.8, +1.4, +0.9, +1.1, +0.9]` | `-0.074` | `0.56%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,450.50 | ⚪ **CASH** | **+2.3 bps** (±1.2) | `[+1.9, +1.8, +4.7, +2.3, +3.9]` | `+0.085` | `0.77%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.22 | ⚪ **CASH** | **+2.7 bps** (±0.6) | `[+3.9, +3.5, +2.7, +2.6, +2.2]` | `+0.016` | `0.92%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 17:32:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,370.00 | ⚪ **CASH** | **+0.9 bps** (±0.2) | `[+0.8, +1.4, +0.9, +1.1, +0.9]` | `-0.074` | `0.56%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,444.80 | ⚪ **CASH** | **+2.3 bps** (±1.2) | `[+1.9, +1.8, +4.7, +2.3, +3.9]` | `+0.085` | `0.77%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.03 | ⚪ **CASH** | **+2.7 bps** (±0.6) | `[+3.9, +3.5, +2.7, +2.6, +2.2]` | `+0.016` | `0.92%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 17:17:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,610.33 | ⚪ **CASH** | **+0.9 bps** (±0.2) | `[+0.8, +1.4, +0.9, +1.1, +0.9]` | `-0.074` | `0.56%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,453.88 | ⚪ **CASH** | **+2.3 bps** (±1.2) | `[+1.9, +1.8, +4.7, +2.3, +3.9]` | `+0.085` | `0.77%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.44 | ⚪ **CASH** | **+2.7 bps** (±0.6) | `[+3.9, +3.5, +2.7, +2.6, +2.2]` | `+0.016` | `0.92%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 17:02:07 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,122.01 | ⚪ **CASH** | **+0.9 bps** (±0.2) | `[+0.8, +1.4, +0.9, +1.1, +0.9]` | `-0.074` | `0.56%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,434.42 | ⚪ **CASH** | **+2.3 bps** (±1.2) | `[+1.9, +1.8, +4.7, +2.3, +3.9]` | `+0.085` | `0.77%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.60 | ⚪ **CASH** | **+2.7 bps** (±0.6) | `[+3.9, +3.5, +2.7, +2.6, +2.2]` | `+0.016` | `0.92%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 16:47:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,190.01 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.3, +0.1, +0.2]` | `-0.070` | `0.56%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,433.74 | ⚪ **CASH** | **+1.3 bps** (±0.7) | `[+2.7, +1.3, +0.8, +1.1, +2.3]` | `+0.074` | `0.78%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.73 | ⚪ **CASH** | **-2.5 bps** (±2.5) | `[-2.5, -5.2, +0.8, -1.5, +1.9]` | `+0.014` | `0.93%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 16:32:21 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,984.01 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.3, +0.1, +0.2]` | `-0.070` | `0.56%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,424.78 | ⚪ **CASH** | **+1.3 bps** (±0.7) | `[+2.7, +1.3, +0.8, +1.1, +2.3]` | `+0.074` | `0.78%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.20 | ⚪ **CASH** | **-2.5 bps** (±2.5) | `[-2.5, -5.2, +0.8, -1.5, +1.9]` | `+0.014` | `0.93%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 16:17:09 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,400.00 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.3, +0.1, +0.2]` | `-0.070` | `0.56%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,439.00 | ⚪ **CASH** | **+1.3 bps** (±0.7) | `[+2.7, +1.3, +0.8, +1.1, +2.3]` | `+0.074` | `0.78%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.75 | ⚪ **CASH** | **-2.5 bps** (±2.5) | `[-2.5, -5.2, +0.8, -1.5, +1.9]` | `+0.014` | `0.93%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 16:02:18 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,431.28 | ⚪ **CASH** | **+0.1 bps** (±0.1) | `[+0.1, +0.0, +0.3, +0.1, +0.2]` | `-0.070` | `0.56%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,442.96 | ⚪ **CASH** | **+1.3 bps** (±0.7) | `[+2.7, +1.3, +0.8, +1.1, +2.3]` | `+0.074` | `0.78%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.99 | ⚪ **CASH** | **-2.5 bps** (±2.5) | `[-2.5, -5.2, +0.8, -1.5, +1.9]` | `+0.014` | `0.93%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 15:47:03 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,304.01 | ⚪ **CASH** | **+0.3 bps** (±1.1) | `[+0.8, +1.3, +2.2, +0.8, -1.0]` | `-0.087` | `0.56%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,438.41 | ⚪ **CASH** | **+2.3 bps** (±1.7) | `[+2.0, +6.5, +1.7, +2.7, +3.1]` | `+0.007` | `0.72%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.86 | ⚪ **CASH** | **-4.1 bps** (±3.2) | `[+3.0, -1.7, -4.9, -6.2, -2.8]` | `+0.001` | `0.92%/h` | `alt_downtrend` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 15:32:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,224.24 | ⚪ **CASH** | **+0.3 bps** (±1.1) | `[+0.8, +1.3, +2.2, +0.8, -1.0]` | `-0.087` | `0.56%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,422.48 | ⚪ **CASH** | **+2.3 bps** (±1.7) | `[+2.0, +6.5, +1.7, +2.7, +3.1]` | `+0.007` | `0.72%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.41 | ⚪ **CASH** | **-4.1 bps** (±3.2) | `[+3.0, -1.7, -4.9, -6.2, -2.8]` | `+0.001` | `0.92%/h` | `alt_downtrend` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-15 15:17:11 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,219.65 | ⚪ **CASH** | **+0.3 bps** (±1.1) | `[+0.8, +1.3, +2.2, +0.8, -1.0]` | `-0.087` | `0.56%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,421.66 | ⚪ **CASH** | **+2.3 bps** (±1.7) | `[+2.0, +6.5, +1.7, +2.7, +3.1]` | `+0.007` | `0.72%/h` | `alt_downtrend` | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.57 | ⚪ **CASH** | **-4.1 bps** (±3.2) | `[+3.0, -1.7, -4.9, -6.2, -2.8]` | `+0.001` | `0.92%/h` | `alt_downtrend` `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |
