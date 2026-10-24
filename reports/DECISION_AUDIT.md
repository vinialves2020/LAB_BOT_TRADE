# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-24 17:02:15 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-24 17:02:15 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,206.19 | ⚪ **CASH** | **-20.7 bps** (±2.9) | `-10.9 bps` | `-0.089 / -0.198` | `0.30%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,315.93 | ⚪ **CASH** | **-43.6 bps** (±19.0) | `-58.9 bps` | `-0.050 / -0.116` | `0.49%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.47 | ⚪ **CASH** | **-12.7 bps** (±10.5) | `+1.1 bps` | `-0.091 / -0.137` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 16:47:03 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,895.83 | ⚪ **CASH** | **-33.6 bps** (±12.4) | `-30.8 bps` | `-0.088 / -0.230` | `0.29%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,306.45 | ⚪ **CASH** | **-58.3 bps** (±22.9) | `-80.3 bps` | `-0.063 / -0.169` | `0.48%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.10 | ⚪ **CASH** | **-19.0 bps** (±28.2) | `-5.2 bps` | `-0.097 / -0.157` | `0.40%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 16:32:13 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,617.73 | ⚪ **CASH** | **-33.6 bps** (±12.4) | `-30.8 bps` | `-0.088 / -0.230` | `0.29%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,296.04 | ⚪ **CASH** | **-58.3 bps** (±22.9) | `-80.3 bps` | `-0.063 / -0.169` | `0.48%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $99.56 | ⚪ **CASH** | **-19.0 bps** (±28.2) | `-5.2 bps` | `-0.097 / -0.157` | `0.40%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 16:17:00 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,883.92 | ⚪ **CASH** | **-33.6 bps** (±12.4) | `-30.8 bps` | `-0.088 / -0.230` | `0.29%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,312.29 | ⚪ **CASH** | **-58.3 bps** (±22.9) | `-80.3 bps` | `-0.063 / -0.169` | `0.48%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.30 | ⚪ **CASH** | **-19.0 bps** (±28.2) | `-5.2 bps` | `-0.097 / -0.157` | `0.40%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 16:02:20 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,731.07 | ⚪ **CASH** | **-33.6 bps** (±12.4) | `-30.8 bps` | `-0.088 / -0.230` | `0.29%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,302.78 | ⚪ **CASH** | **-58.3 bps** (±22.9) | `-80.3 bps` | `-0.063 / -0.169` | `0.48%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $99.67 | ⚪ **CASH** | **-19.0 bps** (±28.2) | `-5.2 bps` | `-0.097 / -0.157` | `0.40%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 15:47:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,538.37 | ⚪ **CASH** | **-11.0 bps** (±10.9) | `+0.4 bps` | `-0.042 / -0.187` | `0.28%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,297.24 | ⚪ **CASH** | **-1.0 bps** (±10.0) | `+11.3 bps` | `-0.017 / -0.117` | `0.41%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $99.34 | ⚪ **CASH** | **-9.4 bps** (±12.1) | `+7.0 bps` | `-0.092 / -0.165` | `0.40%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 15:32:06 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,478.57 | ⚪ **CASH** | **-11.0 bps** (±10.9) | `+0.4 bps` | `-0.042 / -0.187` | `0.28%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,295.96 | ⚪ **CASH** | **-1.0 bps** (±10.0) | `+11.3 bps` | `-0.017 / -0.117` | `0.41%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $99.13 | ⚪ **CASH** | **-9.4 bps** (±12.1) | `+7.0 bps` | `-0.092 / -0.165` | `0.40%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 15:17:15 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,517.04 | ⚪ **CASH** | **-11.0 bps** (±10.9) | `+0.4 bps` | `-0.042 / -0.187` | `0.28%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,297.85 | ⚪ **CASH** | **-1.0 bps** (±10.0) | `+11.3 bps` | `-0.017 / -0.117` | `0.41%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $99.34 | ⚪ **CASH** | **-9.4 bps** (±12.1) | `+7.0 bps` | `-0.092 / -0.165` | `0.40%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 15:02:15 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,109.67 | ⚪ **CASH** | **-11.0 bps** (±10.9) | `+0.4 bps` | `-0.042 / -0.187` | `0.28%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,339.46 | ⚪ **CASH** | **-1.0 bps** (±10.0) | `+11.3 bps` | `-0.017 / -0.117` | `0.41%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.29 | ⚪ **CASH** | **-9.4 bps** (±12.1) | `+7.0 bps` | `-0.092 / -0.165` | `0.40%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 14:47:03 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,218.08 | ⚪ **CASH** | **+4.5 bps** (±3.5) | `+3.3 bps` | `+0.009 / +0.065` | `0.27%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,345.53 | ⚪ **CASH** | **-1.7 bps** (±1.8) | `-4.2 bps` | `+0.031 / -0.031` | `0.38%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.61 | ⚪ **CASH** | **+6.8 bps** (±11.3) | `+21.8 bps` | `-0.045 / -0.051` | `0.38%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 14:32:02 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,359.08 | ⚪ **CASH** | **+4.5 bps** (±3.5) | `+3.3 bps` | `+0.009 / +0.065` | `0.27%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,350.05 | ⚪ **CASH** | **-1.7 bps** (±1.8) | `-4.2 bps` | `+0.031 / -0.031` | `0.38%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.70 | ⚪ **CASH** | **+6.8 bps** (±11.3) | `+21.8 bps` | `-0.045 / -0.051` | `0.38%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 14:17:16 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,205.61 | ⚪ **CASH** | **+4.5 bps** (±3.5) | `+3.3 bps` | `+0.009 / +0.065` | `0.27%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,339.21 | ⚪ **CASH** | **-1.7 bps** (±1.8) | `-4.2 bps` | `+0.031 / -0.031` | `0.38%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.14 | ⚪ **CASH** | **+6.8 bps** (±11.3) | `+21.8 bps` | `-0.045 / -0.051` | `0.38%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 14:02:22 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,721.22 | ⚪ **CASH** | **+4.5 bps** (±3.5) | `+3.3 bps` | `+0.009 / +0.065` | `0.27%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,368.79 | ⚪ **CASH** | **-1.7 bps** (±1.8) | `-4.2 bps` | `+0.031 / -0.031` | `0.38%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.45 | ⚪ **CASH** | **+6.8 bps** (±11.3) | `+21.8 bps` | `-0.045 / -0.051` | `0.38%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 13:47:21 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,683.37 | ⚪ **CASH** | **+5.1 bps** (±3.5) | `+2.5 bps` | `+0.017 / +0.074` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,366.78 | ⚪ **CASH** | **+2.2 bps** (±3.9) | `+3.3 bps` | `+0.032 / -0.040` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.36 | ⚪ **CASH** | **+7.3 bps** (±10.8) | `+20.3 bps` | `-0.031 / -0.043` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 13:32:15 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,678.00 | ⚪ **CASH** | **+5.1 bps** (±3.5) | `+2.5 bps` | `+0.017 / +0.074` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,366.09 | ⚪ **CASH** | **+2.2 bps** (±3.9) | `+3.3 bps` | `+0.032 / -0.040` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.29 | ⚪ **CASH** | **+7.3 bps** (±10.8) | `+20.3 bps` | `-0.031 / -0.043` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 13:17:04 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,775.22 | ⚪ **CASH** | **+5.1 bps** (±3.5) | `+2.5 bps` | `+0.017 / +0.074` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,368.89 | ⚪ **CASH** | **+2.2 bps** (±3.9) | `+3.3 bps` | `+0.032 / -0.040` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.52 | ⚪ **CASH** | **+7.3 bps** (±10.8) | `+20.3 bps` | `-0.031 / -0.043` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 13:01:57 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,809.87 | ⚪ **CASH** | **+5.1 bps** (±3.5) | `+2.5 bps` | `+0.017 / +0.074` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,370.68 | ⚪ **CASH** | **+2.2 bps** (±3.9) | `+3.3 bps` | `+0.032 / -0.040` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.68 | ⚪ **CASH** | **+7.3 bps** (±10.8) | `+20.3 bps` | `-0.031 / -0.043` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 12:47:06 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,820.00 | ⚪ **CASH** | **+9.4 bps** (±3.7) | `+9.9 bps` | `+0.017 / +0.082` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,371.48 | ⚪ **CASH** | **-1.4 bps** (±3.6) | `-0.8 bps` | `+0.026 / -0.069` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.65 | ⚪ **CASH** | **+11.7 bps** (±11.3) | `+23.2 bps` | `-0.029 / +0.032` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 12:32:11 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,758.01 | ⚪ **CASH** | **+9.4 bps** (±3.7) | `+9.9 bps` | `+0.017 / +0.082` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,368.93 | ⚪ **CASH** | **-1.4 bps** (±3.6) | `-0.8 bps` | `+0.026 / -0.069` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.63 | ⚪ **CASH** | **+11.7 bps** (±11.3) | `+23.2 bps` | `-0.029 / +0.032` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 12:17:02 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,677.63 | ⚪ **CASH** | **+9.4 bps** (±3.7) | `+9.9 bps` | `+0.017 / +0.082` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,366.64 | ⚪ **CASH** | **-1.4 bps** (±3.6) | `-0.8 bps` | `+0.026 / -0.069` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.52 | ⚪ **CASH** | **+11.7 bps** (±11.3) | `+23.2 bps` | `-0.029 / +0.032` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 12:02:18 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,581.93 | ⚪ **CASH** | **+9.4 bps** (±3.7) | `+9.9 bps` | `+0.017 / +0.082` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,364.36 | ⚪ **CASH** | **-1.4 bps** (±3.6) | `-0.8 bps` | `+0.026 / -0.069` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.44 | ⚪ **CASH** | **+11.7 bps** (±11.3) | `+23.2 bps` | `-0.029 / +0.032` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 11:46:58 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,622.09 | ⚪ **CASH** | **+8.9 bps** (±5.4) | `+8.7 bps` | `+0.017 / +0.091` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,366.15 | ⚪ **CASH** | **-2.3 bps** (±4.2) | `-0.6 bps` | `+0.024 / -0.090` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.39 | ⚪ **CASH** | **+8.0 bps** (±9.0) | `+16.4 bps` | `-0.021 / +0.015` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 11:32:17 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,597.54 | ⚪ **CASH** | **+8.9 bps** (±5.4) | `+8.7 bps` | `+0.017 / +0.091` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,366.10 | ⚪ **CASH** | **-2.3 bps** (±4.2) | `-0.6 bps` | `+0.024 / -0.090` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.44 | ⚪ **CASH** | **+8.0 bps** (±9.0) | `+16.4 bps` | `-0.021 / +0.015` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 11:17:04 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,670.11 | ⚪ **CASH** | **+8.9 bps** (±5.4) | `+8.7 bps` | `+0.017 / +0.091` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,369.77 | ⚪ **CASH** | **-2.3 bps** (±4.2) | `-0.6 bps` | `+0.024 / -0.090` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.65 | ⚪ **CASH** | **+8.0 bps** (±9.0) | `+16.4 bps` | `-0.021 / +0.015` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 11:02:07 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,673.68 | ⚪ **CASH** | **+8.9 bps** (±5.4) | `+8.7 bps` | `+0.017 / +0.091` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,370.55 | ⚪ **CASH** | **-2.3 bps** (±4.2) | `-0.6 bps` | `+0.024 / -0.090` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.69 | ⚪ **CASH** | **+8.0 bps** (±9.0) | `+16.4 bps` | `-0.021 / +0.015` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 10:47:13 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,672.37 | ⚪ **CASH** | **+5.7 bps** (±6.4) | `+5.0 bps` | `+0.020 / +0.056` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,371.00 | ⚪ **CASH** | **-0.8 bps** (±4.0) | `+1.4 bps` | `+0.027 / -0.087` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.74 | ⚪ **CASH** | **+11.8 bps** (±8.5) | `+24.3 bps` | `-0.022 / -0.001` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 10:32:00 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,644.80 | ⚪ **CASH** | **+5.7 bps** (±6.4) | `+5.0 bps` | `+0.020 / +0.056` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,368.89 | ⚪ **CASH** | **-0.8 bps** (±4.0) | `+1.4 bps` | `+0.027 / -0.087` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.67 | ⚪ **CASH** | **+11.8 bps** (±8.5) | `+24.3 bps` | `-0.022 / -0.001` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 10:17:09 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,553.73 | ⚪ **CASH** | **+5.7 bps** (±6.4) | `+5.0 bps` | `+0.020 / +0.056` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,365.45 | ⚪ **CASH** | **-0.8 bps** (±4.0) | `+1.4 bps` | `+0.027 / -0.087` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.43 | ⚪ **CASH** | **+11.8 bps** (±8.5) | `+24.3 bps` | `-0.022 / -0.001` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 10:02:10 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,647.46 | ⚪ **CASH** | **+5.7 bps** (±6.4) | `+5.0 bps` | `+0.020 / +0.056` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,368.34 | ⚪ **CASH** | **-0.8 bps** (±4.0) | `+1.4 bps` | `+0.027 / -0.087` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.43 | ⚪ **CASH** | **+11.8 bps** (±8.5) | `+24.3 bps` | `-0.022 / -0.001` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 09:47:08 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,540.41 | ⚪ **CASH** | **+8.9 bps** (±5.3) | `+6.9 bps` | `+0.020 / +0.111` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,361.21 | ⚪ **CASH** | **+2.0 bps** (±3.6) | `+0.9 bps` | `+0.026 / -0.002` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.23 | ⚪ **CASH** | **+9.9 bps** (±9.1) | `+20.7 bps` | `-0.025 / +0.007` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 09:32:25 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,620.61 | ⚪ **CASH** | **+8.9 bps** (±5.3) | `+6.9 bps` | `+0.020 / +0.111` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,363.27 | ⚪ **CASH** | **+2.0 bps** (±3.6) | `+0.9 bps` | `+0.026 / -0.002` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.47 | ⚪ **CASH** | **+9.9 bps** (±9.1) | `+20.7 bps` | `-0.025 / +0.007` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 09:17:09 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,620.72 | ⚪ **CASH** | **+8.9 bps** (±5.3) | `+6.9 bps` | `+0.020 / +0.111` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,364.15 | ⚪ **CASH** | **+2.0 bps** (±3.6) | `+0.9 bps` | `+0.026 / -0.002` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.60 | ⚪ **CASH** | **+9.9 bps** (±9.1) | `+20.7 bps` | `-0.025 / +0.007` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 09:02:15 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,666.99 | ⚪ **CASH** | **+8.9 bps** (±5.3) | `+6.9 bps` | `+0.020 / +0.111` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,367.91 | ⚪ **CASH** | **+2.0 bps** (±3.6) | `+0.9 bps` | `+0.026 / -0.002` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.85 | ⚪ **CASH** | **+9.9 bps** (±9.1) | `+20.7 bps` | `-0.025 / +0.007` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 08:47:06 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,664.50 | ⚪ **CASH** | **+6.8 bps** (±4.9) | `+6.9 bps` | `+0.004 / +0.088` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,368.38 | ⚪ **CASH** | **+7.2 bps** (±5.2) | `+7.1 bps` | `+0.094 / -0.040` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.92 | ⚪ **CASH** | **+7.8 bps** (±7.6) | `+16.6 bps` | `-0.027 / +0.023` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 08:32:02 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,811.99 | ⚪ **CASH** | **+6.8 bps** (±4.9) | `+6.9 bps` | `+0.004 / +0.088` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,372.71 | ⚪ **CASH** | **+7.2 bps** (±5.2) | `+7.1 bps` | `+0.094 / -0.040` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.11 | ⚪ **CASH** | **+7.8 bps** (±7.6) | `+16.6 bps` | `-0.027 / +0.023` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-24 08:16:59 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,780.49 | ⚪ **CASH** | **+6.8 bps** (±4.9) | `+6.9 bps` | `+0.004 / +0.088` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,374.13 | ⚪ **CASH** | **+7.2 bps** (±5.2) | `+7.1 bps` | `+0.094 / -0.040` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.07 | ⚪ **CASH** | **+7.8 bps** (±7.6) | `+16.6 bps` | `-0.027 / +0.023` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
