# 📋 BOT_TRADE V5 — Livro de Auditoria de Decisões e Análise de Mercado

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o consenso dos 5 modelos XGBoost, o comportamento do CVD (Cumulative Volume Delta) e o disparo de travas de risco.

**Última Atualização**: `2026-09-25 01:17:17 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-09-25 01:17:17 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,721.78 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.0, -0.0, -0.2, -0.2]` | `-0.023` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,695.37 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.2, +0.1, +0.1, +0.0]` | `+0.069` | `0.44%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.74 | ⚪ **CASH** | **-0.1 bps** (±0.3) | `[-0.1, -0.1, +0.6, -0.2, -0.0]` | `-0.137` | `0.55%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-25 01:02:15 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,644.96 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.0, -0.0, -0.2, -0.2]` | `-0.023` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,694.13 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.2, +0.1, +0.1, +0.0]` | `+0.069` | `0.44%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.61 | ⚪ **CASH** | **-0.1 bps** (±0.3) | `[-0.1, -0.1, +0.6, -0.2, -0.0]` | `-0.137` | `0.55%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-25 00:47:18 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,622.01 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, +0.1, +0.0, -0.1, -0.2]` | `-0.018` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,691.00 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.2, +0.1, +0.1, +0.2]` | `+0.101` | `0.45%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.42 | ⚪ **CASH** | **-0.6 bps** (±0.3) | `[-0.8, -0.5, +0.2, -0.6, -0.4]` | `-0.125` | `0.56%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-25 00:32:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,569.85 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, +0.1, +0.0, -0.1, -0.2]` | `-0.018` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,689.59 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.2, +0.1, +0.1, +0.2]` | `+0.101` | `0.45%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.37 | ⚪ **CASH** | **-0.6 bps** (±0.3) | `[-0.8, -0.5, +0.2, -0.6, -0.4]` | `-0.125` | `0.56%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-25 00:17:15 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,620.07 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, +0.1, +0.0, -0.1, -0.2]` | `-0.018` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,693.61 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.2, +0.1, +0.1, +0.2]` | `+0.101` | `0.45%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.53 | ⚪ **CASH** | **-0.6 bps** (±0.3) | `[-0.8, -0.5, +0.2, -0.6, -0.4]` | `-0.125` | `0.56%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-25 00:02:02 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,438.00 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, +0.1, +0.0, -0.1, -0.2]` | `-0.018` | `0.41%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,688.54 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.2, +0.1, +0.1, +0.2]` | `+0.101` | `0.45%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.09 | ⚪ **CASH** | **-0.6 bps** (±0.3) | `[-0.8, -0.5, +0.2, -0.6, -0.4]` | `-0.125` | `0.56%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 23:47:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,407.57 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.0, +0.1, -0.2, -0.2]` | `-0.058` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,690.16 | ⚪ **CASH** | **-0.2 bps** (±0.1) | `[-0.1, -0.2, +0.1, -0.2, -0.1]` | `+0.104` | `0.46%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.04 | ⚪ **CASH** | **-0.3 bps** (±0.3) | `[-0.3, +0.0, -0.2, +0.2, -0.6]` | `-0.163` | `0.57%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 23:32:12 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,435.25 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.0, +0.1, -0.2, -0.2]` | `-0.058` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,692.63 | ⚪ **CASH** | **-0.2 bps** (±0.1) | `[-0.1, -0.2, +0.1, -0.2, -0.1]` | `+0.104` | `0.46%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.04 | ⚪ **CASH** | **-0.3 bps** (±0.3) | `[-0.3, +0.0, -0.2, +0.2, -0.6]` | `-0.163` | `0.57%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 23:16:58 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,336.01 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.0, +0.1, -0.2, -0.2]` | `-0.058` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,686.86 | ⚪ **CASH** | **-0.2 bps** (±0.1) | `[-0.1, -0.2, +0.1, -0.2, -0.1]` | `+0.104` | `0.46%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.62 | ⚪ **CASH** | **-0.3 bps** (±0.3) | `[-0.3, +0.0, -0.2, +0.2, -0.6]` | `-0.163` | `0.57%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 23:02:29 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,290.00 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.0, +0.1, -0.2, -0.2]` | `-0.058` | `0.42%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,686.62 | ⚪ **CASH** | **-0.2 bps** (±0.1) | `[-0.1, -0.2, +0.1, -0.2, -0.1]` | `+0.104` | `0.46%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.65 | ⚪ **CASH** | **-0.3 bps** (±0.3) | `[-0.3, +0.0, -0.2, +0.2, -0.6]` | `-0.163` | `0.57%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 22:47:02 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,162.68 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, +0.1, +0.2, -0.1, -0.2]` | `-0.013` | `0.43%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,682.77 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.2, +0.1, +0.1, +0.2]` | `+0.110` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.42 | ⚪ **CASH** | **-0.2 bps** (±0.2) | `[-0.3, +0.0, +0.2, -0.2, -0.2]` | `-0.074` | `0.57%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 22:32:22 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,145.26 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, +0.1, +0.2, -0.1, -0.2]` | `-0.013` | `0.43%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,681.31 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.2, +0.1, +0.1, +0.2]` | `+0.110` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.40 | ⚪ **CASH** | **-0.2 bps** (±0.2) | `[-0.3, +0.0, +0.2, -0.2, -0.2]` | `-0.074` | `0.57%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 22:17:21 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,234.00 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, +0.1, +0.2, -0.1, -0.2]` | `-0.013` | `0.43%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,683.17 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.2, +0.1, +0.1, +0.2]` | `+0.110` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.43 | ⚪ **CASH** | **-0.2 bps** (±0.2) | `[-0.3, +0.0, +0.2, -0.2, -0.2]` | `-0.074` | `0.57%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 22:02:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,286.01 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, +0.1, +0.2, -0.1, -0.2]` | `-0.013` | `0.43%/h` | `vol_compressed` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,685.93 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.2, +0.1, +0.1, +0.2]` | `+0.110` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.77 | ⚪ **CASH** | **-0.2 bps** (±0.2) | `[-0.3, +0.0, +0.2, -0.2, -0.2]` | `-0.074` | `0.57%/h` | `vol_compressed` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 21:47:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,462.09 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.0, -0.0, +0.1, -0.2, -0.2]` | `-0.014` | `0.43%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,689.88 | ⚪ **CASH** | **-0.2 bps** (±0.1) | `[-0.1, -0.2, +0.1, -0.2, -0.1]` | `+0.134` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.10 | ⚪ **CASH** | **-0.2 bps** (±0.4) | `[-0.1, -0.5, +0.6, -0.2, -0.0]` | `-0.024` | `0.58%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 21:32:30 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,464.01 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.0, -0.0, +0.1, -0.2, -0.2]` | `-0.014` | `0.43%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,691.08 | ⚪ **CASH** | **-0.2 bps** (±0.1) | `[-0.1, -0.2, +0.1, -0.2, -0.1]` | `+0.134` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.95 | ⚪ **CASH** | **-0.2 bps** (±0.4) | `[-0.1, -0.5, +0.6, -0.2, -0.0]` | `-0.024` | `0.58%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 21:16:57 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,391.49 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.0, -0.0, +0.1, -0.2, -0.2]` | `-0.014` | `0.43%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,688.78 | ⚪ **CASH** | **-0.2 bps** (±0.1) | `[-0.1, -0.2, +0.1, -0.2, -0.1]` | `+0.134` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.80 | ⚪ **CASH** | **-0.2 bps** (±0.4) | `[-0.1, -0.5, +0.6, -0.2, -0.0]` | `-0.024` | `0.58%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 21:02:41 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,358.41 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.0, -0.0, +0.1, -0.2, -0.2]` | `-0.014` | `0.43%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,688.50 | ⚪ **CASH** | **-0.2 bps** (±0.1) | `[-0.1, -0.2, +0.1, -0.2, -0.1]` | `+0.134` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.81 | ⚪ **CASH** | **-0.2 bps** (±0.4) | `[-0.1, -0.5, +0.6, -0.2, -0.0]` | `-0.024` | `0.58%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 20:48:27 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,377.50 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.0, -0.0, +0.1, -0.2, -0.2]` | `-0.106` | `0.44%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,687.67 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.3, +0.2, +0.1, -0.1, -0.1]` | `+0.084` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.88 | ⚪ **CASH** | **-0.2 bps** (±0.3) | `[-0.1, -0.3, +0.6, -0.2, -0.0]` | `-0.004` | `0.59%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 20:32:58 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,238.00 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.0, -0.0, +0.1, -0.2, -0.2]` | `-0.106` | `0.44%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,685.84 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.3, +0.2, +0.1, -0.1, -0.1]` | `+0.084` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.77 | ⚪ **CASH** | **-0.2 bps** (±0.3) | `[-0.1, -0.3, +0.6, -0.2, -0.0]` | `-0.004` | `0.59%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 20:17:45 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,273.90 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.0, -0.0, +0.1, -0.2, -0.2]` | `-0.106` | `0.44%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,690.24 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.3, +0.2, +0.1, -0.1, -0.1]` | `+0.084` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.00 | ⚪ **CASH** | **-0.2 bps** (±0.3) | `[-0.1, -0.3, +0.6, -0.2, -0.0]` | `-0.004` | `0.59%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 20:02:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,334.19 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.0, -0.0, +0.1, -0.2, -0.2]` | `-0.106` | `0.44%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,692.40 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.3, +0.2, +0.1, -0.1, -0.1]` | `+0.084` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.20 | ⚪ **CASH** | **-0.2 bps** (±0.3) | `[-0.1, -0.3, +0.6, -0.2, -0.0]` | `-0.004` | `0.59%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 19:47:14 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,462.01 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.0, -0.0, -0.2, -0.2]` | `-0.071` | `0.45%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,699.00 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.3, -0.2, +0.1, +0.1, +0.2]` | `+0.059` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.46 | ⚪ **CASH** | **-0.2 bps** (±0.3) | `[-0.1, -0.3, +0.6, -0.2, -0.0]` | `+0.040` | `0.59%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 19:32:24 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,594.01 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.0, -0.0, -0.2, -0.2]` | `-0.071` | `0.45%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,695.50 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.3, -0.2, +0.1, +0.1, +0.2]` | `+0.059` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.53 | ⚪ **CASH** | **-0.2 bps** (±0.3) | `[-0.1, -0.3, +0.6, -0.2, -0.0]` | `+0.040` | `0.59%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 19:18:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,589.26 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.0, -0.0, -0.2, -0.2]` | `-0.071` | `0.45%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,693.80 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.3, -0.2, +0.1, +0.1, +0.2]` | `+0.059` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.54 | ⚪ **CASH** | **-0.2 bps** (±0.3) | `[-0.1, -0.3, +0.6, -0.2, -0.0]` | `+0.040` | `0.59%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 19:02:25 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,405.53 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.0, -0.0, -0.2, -0.2]` | `-0.071` | `0.45%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,687.82 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[-0.3, -0.2, +0.1, +0.1, +0.2]` | `+0.059` | `0.48%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.33 | ⚪ **CASH** | **-0.2 bps** (±0.3) | `[-0.1, -0.3, +0.6, -0.2, -0.0]` | `+0.040` | `0.59%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 18:47:17 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,416.01 | ⚪ **CASH** | **+0.8 bps** (±0.2) | `[+1.1, +1.2, +1.0, +0.6, +0.8]` | `-0.074` | `0.45%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,688.15 | ⚪ **CASH** | **+1.3 bps** (±0.2) | `[+1.4, +1.5, +1.3, +1.0, +1.4]` | `+0.055` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.22 | ⚪ **CASH** | **+2.7 bps** (±0.7) | `[+4.1, +2.8, +3.4, +2.8, +2.2]` | `+0.063` | `0.60%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 18:32:27 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,442.00 | ⚪ **CASH** | **+0.8 bps** (±0.2) | `[+1.1, +1.2, +1.0, +0.6, +0.8]` | `-0.074` | `0.45%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,685.49 | ⚪ **CASH** | **+1.3 bps** (±0.2) | `[+1.4, +1.5, +1.3, +1.0, +1.4]` | `+0.055` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.25 | ⚪ **CASH** | **+2.7 bps** (±0.7) | `[+4.1, +2.8, +3.4, +2.8, +2.2]` | `+0.063` | `0.60%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 18:17:30 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,360.02 | ⚪ **CASH** | **+0.8 bps** (±0.2) | `[+1.1, +1.2, +1.0, +0.6, +0.8]` | `-0.074` | `0.45%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,678.34 | ⚪ **CASH** | **+1.3 bps** (±0.2) | `[+1.4, +1.5, +1.3, +1.0, +1.4]` | `+0.055` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.18 | ⚪ **CASH** | **+2.7 bps** (±0.7) | `[+4.1, +2.8, +3.4, +2.8, +2.2]` | `+0.063` | `0.60%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 18:02:10 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,036.01 | ⚪ **CASH** | **+0.8 bps** (±0.2) | `[+1.1, +1.2, +1.0, +0.6, +0.8]` | `-0.074` | `0.45%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,667.21 | ⚪ **CASH** | **+1.3 bps** (±0.2) | `[+1.4, +1.5, +1.3, +1.0, +1.4]` | `+0.055` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.59 | ⚪ **CASH** | **+2.7 bps** (±0.7) | `[+4.1, +2.8, +3.4, +2.8, +2.2]` | `+0.063` | `0.60%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 17:47:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,192.60 | ⚪ **CASH** | **-0.0 bps** (±0.1) | `[+0.1, +0.1, +0.2, -0.1, -0.1]` | `-0.059` | `0.45%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,672.02 | ⚪ **CASH** | **-0.0 bps** (±0.1) | `[-0.1, +0.0, +0.1, +0.1, +0.2]` | `+0.057` | `0.46%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.67 | ⚪ **CASH** | **-0.9 bps** (±0.7) | `[-1.6, -0.9, +0.6, -0.6, -0.2]` | `+0.109` | `0.60%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 17:32:09 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,391.50 | ⚪ **CASH** | **-0.0 bps** (±0.1) | `[+0.1, +0.1, +0.2, -0.1, -0.1]` | `-0.059` | `0.45%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,681.95 | ⚪ **CASH** | **-0.0 bps** (±0.1) | `[-0.1, +0.0, +0.1, +0.1, +0.2]` | `+0.057` | `0.46%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.12 | ⚪ **CASH** | **-0.9 bps** (±0.7) | `[-1.6, -0.9, +0.6, -0.6, -0.2]` | `+0.109` | `0.60%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 17:17:29 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,474.01 | ⚪ **CASH** | **-0.0 bps** (±0.1) | `[+0.1, +0.1, +0.2, -0.1, -0.1]` | `-0.059` | `0.45%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,685.88 | ⚪ **CASH** | **-0.0 bps** (±0.1) | `[-0.1, +0.0, +0.1, +0.1, +0.2]` | `+0.057` | `0.46%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.25 | ⚪ **CASH** | **-0.9 bps** (±0.7) | `[-1.6, -0.9, +0.6, -0.6, -0.2]` | `+0.109` | `0.60%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 17:02:43 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,473.75 | ⚪ **CASH** | **-0.0 bps** (±0.1) | `[+0.1, +0.1, +0.2, -0.1, -0.1]` | `-0.059` | `0.45%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,687.19 | ⚪ **CASH** | **-0.0 bps** (±0.1) | `[-0.1, +0.0, +0.1, +0.1, +0.2]` | `+0.057` | `0.46%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.20 | ⚪ **CASH** | **-0.9 bps** (±0.7) | `[-1.6, -0.9, +0.6, -0.6, -0.2]` | `+0.109` | `0.60%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 16:47:13 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,608.82 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.0, +0.1, -0.2, -0.2]` | `-0.053` | `0.45%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,692.00 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[+0.0, -0.4, +0.1, -0.0, +0.3]` | `+0.030` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $117.33 | ⚪ **CASH** | **-0.3 bps** (±0.4) | `[-0.2, -0.2, +0.6, -0.6, -0.2]` | `+0.101` | `0.60%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-09-24 16:32:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,570.99 | ⚪ **CASH** | **-0.1 bps** (±0.1) | `[-0.1, -0.0, +0.1, -0.2, -0.2]` | `-0.053` | `0.45%/h` | `turbulent_chop` | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,689.86 | ⚪ **CASH** | **-0.1 bps** (±0.2) | `[+0.0, -0.4, +0.1, -0.0, +0.3]` | `+0.030` | `0.47%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $116.98 | ⚪ **CASH** | **-0.3 bps** (±0.4) | `[-0.2, -0.2, +0.6, -0.6, -0.2]` | `+0.101` | `0.60%/h` | `sol_sideways` | Aguardando sinal com assimetria |
