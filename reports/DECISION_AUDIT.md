# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-08 18:00:42 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-08 18:00:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,754.01 | ⚪ **CASH** | **+32.4 bps** (±6.4) | `+57.4 bps` | `+0.021 / -0.008` | `0.16%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,230.82 | ⚪ **CASH** | **+11.7 bps** (±6.6) | `+25.0 bps` | `-0.011 / -0.038` | `0.21%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.19 | ⚪ **CASH** | **+25.1 bps** (±14.0) | `+38.6 bps` | `+0.043 / +0.066` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 17:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,763.98 | ⚪ **CASH** | **+34.9 bps** (±6.3) | `+58.6 bps` | `+0.026 / +0.033` | `0.17%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,230.13 | ⚪ **CASH** | **+11.3 bps** (±8.2) | `+20.5 bps` | `-0.010 / +0.018` | `0.22%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.09 | ⚪ **CASH** | **+23.5 bps** (±19.0) | `+36.4 bps` | `+0.045 / +0.063` | `0.34%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 17:30:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,682.50 | ⚪ **CASH** | **+34.9 bps** (±6.3) | `+58.6 bps` | `+0.026 / +0.033` | `0.17%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,225.98 | ⚪ **CASH** | **+11.3 bps** (±8.2) | `+20.5 bps` | `-0.010 / +0.018` | `0.22%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.05 | ⚪ **CASH** | **+23.5 bps** (±19.0) | `+36.4 bps` | `+0.045 / +0.063` | `0.34%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 17:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,688.68 | ⚪ **CASH** | **+34.9 bps** (±6.3) | `+58.6 bps` | `+0.026 / +0.033` | `0.17%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,225.48 | ⚪ **CASH** | **+11.3 bps** (±8.2) | `+20.5 bps` | `-0.010 / +0.018` | `0.22%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.01 | ⚪ **CASH** | **+23.5 bps** (±19.0) | `+36.4 bps` | `+0.045 / +0.063` | `0.34%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 17:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,786.00 | ⚪ **CASH** | **+34.9 bps** (±6.3) | `+58.6 bps` | `+0.026 / +0.033` | `0.17%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,231.19 | ⚪ **CASH** | **+11.3 bps** (±8.2) | `+20.5 bps` | `-0.010 / +0.018` | `0.22%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.08 | ⚪ **CASH** | **+23.5 bps** (±19.0) | `+36.4 bps` | `+0.045 / +0.063` | `0.34%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 16:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,011.96 | ⚪ **CASH** | **+17.9 bps** (±11.6) | `+23.3 bps` | `+0.039 / +0.085` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.71 | ⚪ **CASH** | **+10.9 bps** (±9.5) | `+18.9 bps` | `-0.013 / +0.030` | `0.21%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.44 | ⚪ **CASH** | **+16.8 bps** (±18.3) | `+20.2 bps` | `+0.050 / +0.105` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 16:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,993.04 | ⚪ **CASH** | **+17.9 bps** (±11.6) | `+23.3 bps` | `+0.039 / +0.085` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.44 | ⚪ **CASH** | **+10.9 bps** (±9.5) | `+18.9 bps` | `-0.013 / +0.030` | `0.21%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.44 | ⚪ **CASH** | **+16.8 bps** (±18.3) | `+20.2 bps` | `+0.050 / +0.105` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 16:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,041.79 | ⚪ **CASH** | **+17.9 bps** (±11.6) | `+23.3 bps` | `+0.039 / +0.085` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,240.58 | ⚪ **CASH** | **+10.9 bps** (±9.5) | `+18.9 bps` | `-0.013 / +0.030` | `0.21%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.68 | ⚪ **CASH** | **+16.8 bps** (±18.3) | `+20.2 bps` | `+0.050 / +0.105` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 16:00:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,078.58 | ⚪ **CASH** | **+17.9 bps** (±11.6) | `+23.3 bps` | `+0.039 / +0.085` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,243.01 | ⚪ **CASH** | **+10.9 bps** (±9.5) | `+18.9 bps` | `-0.013 / +0.030` | `0.21%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.78 | ⚪ **CASH** | **+16.8 bps** (±18.3) | `+20.2 bps` | `+0.050 / +0.105` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 15:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,083.94 | ⚪ **CASH** | **+5.0 bps** (±4.3) | `+3.0 bps` | `+0.039 / +0.018` | `0.25%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,241.68 | ⚪ **CASH** | **-7.6 bps** (±4.9) | `-13.4 bps` | `-0.030 / +0.023` | `0.34%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.68 | ⚪ **CASH** | **+9.2 bps** (±14.4) | `+11.3 bps` | `+0.021 / +0.064` | `0.38%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 15:30:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,064.02 | ⚪ **CASH** | **+5.0 bps** (±4.3) | `+3.0 bps` | `+0.039 / +0.018` | `0.25%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,240.99 | ⚪ **CASH** | **-7.6 bps** (±4.9) | `-13.4 bps` | `-0.030 / +0.023` | `0.34%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.77 | ⚪ **CASH** | **+9.2 bps** (±14.4) | `+11.3 bps` | `+0.021 / +0.064` | `0.38%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 15:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,035.64 | ⚪ **CASH** | **+5.0 bps** (±4.3) | `+3.0 bps` | `+0.039 / +0.018` | `0.25%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,239.92 | ⚪ **CASH** | **-7.6 bps** (±4.9) | `-13.4 bps` | `-0.030 / +0.023` | `0.34%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.61 | ⚪ **CASH** | **+9.2 bps** (±14.4) | `+11.3 bps` | `+0.021 / +0.064` | `0.38%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 15:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,057.71 | ⚪ **CASH** | **+5.0 bps** (±4.3) | `+3.0 bps` | `+0.039 / +0.018` | `0.25%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,241.15 | ⚪ **CASH** | **-7.6 bps** (±4.9) | `-13.4 bps` | `-0.030 / +0.023` | `0.34%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.63 | ⚪ **CASH** | **+9.2 bps** (±14.4) | `+11.3 bps` | `+0.021 / +0.064` | `0.38%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 14:45:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,014.09 | ⚪ **CASH** | **+3.5 bps** (±4.5) | `-0.5 bps` | `+0.037 / +0.034` | `0.28%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,240.91 | ⚪ **CASH** | **-8.6 bps** (±4.9) | `-15.1 bps` | `-0.033 / +0.029` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.42 | ⚪ **CASH** | **-0.0 bps** (±15.3) | `-3.9 bps` | `+0.014 / +0.053` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 14:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,968.56 | ⚪ **CASH** | **+3.5 bps** (±4.5) | `-0.5 bps` | `+0.037 / +0.034` | `0.28%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.19 | ⚪ **CASH** | **-8.6 bps** (±4.9) | `-15.1 bps` | `-0.033 / +0.029` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.23 | ⚪ **CASH** | **-0.0 bps** (±15.3) | `-3.9 bps` | `+0.014 / +0.053` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 14:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,982.00 | ⚪ **CASH** | **+3.5 bps** (±4.5) | `-0.5 bps` | `+0.037 / +0.034` | `0.28%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,240.37 | ⚪ **CASH** | **-8.6 bps** (±4.9) | `-15.1 bps` | `-0.033 / +0.029` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.37 | ⚪ **CASH** | **-0.0 bps** (±15.3) | `-3.9 bps` | `+0.014 / +0.053` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 14:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,933.47 | ⚪ **CASH** | **+3.5 bps** (±4.5) | `-0.5 bps` | `+0.037 / +0.034` | `0.28%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.26 | ⚪ **CASH** | **-8.6 bps** (±4.9) | `-15.1 bps` | `-0.033 / +0.029` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.21 | ⚪ **CASH** | **-0.0 bps** (±15.3) | `-3.9 bps` | `+0.014 / +0.053` | `0.41%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 13:45:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,934.01 | ⚪ **CASH** | **+4.5 bps** (±6.3) | `+3.0 bps` | `+0.008 / +0.079` | `0.28%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,237.17 | ⚪ **CASH** | **-9.6 bps** (±6.6) | `-15.5 bps` | `-0.051 / +0.060` | `0.37%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.32 | ⚪ **CASH** | **+1.8 bps** (±12.8) | `-3.1 bps` | `+0.011 / +0.111` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 13:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,077.47 | ⚪ **CASH** | **+4.5 bps** (±6.3) | `+3.0 bps` | `+0.008 / +0.079` | `0.28%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,242.38 | ⚪ **CASH** | **-9.6 bps** (±6.6) | `-15.5 bps` | `-0.051 / +0.060` | `0.37%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.66 | ⚪ **CASH** | **+1.8 bps** (±12.8) | `-3.1 bps` | `+0.011 / +0.111` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 13:15:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,122.07 | ⚪ **CASH** | **+4.5 bps** (±6.3) | `+3.0 bps` | `+0.008 / +0.079` | `0.28%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,243.47 | ⚪ **CASH** | **-9.6 bps** (±6.6) | `-15.5 bps` | `-0.051 / +0.060` | `0.37%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.76 | ⚪ **CASH** | **+1.8 bps** (±12.8) | `-3.1 bps` | `+0.011 / +0.111` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 13:00:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,984.99 | ⚪ **CASH** | **+4.5 bps** (±6.3) | `+3.0 bps` | `+0.008 / +0.079` | `0.28%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,239.65 | ⚪ **CASH** | **-9.6 bps** (±6.6) | `-15.5 bps` | `-0.051 / +0.060` | `0.37%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.52 | ⚪ **CASH** | **+1.8 bps** (±12.8) | `-3.1 bps` | `+0.011 / +0.111` | `0.42%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 12:45:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,928.95 | ⚪ **CASH** | **+4.5 bps** (±9.3) | `+9.7 bps` | `-0.006 / +0.015` | `0.29%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,237.88 | ⚪ **CASH** | **-10.3 bps** (±6.5) | `-13.2 bps` | `-0.054 / +0.018` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.44 | ⚪ **CASH** | **+0.7 bps** (±12.9) | `-4.3 bps` | `+0.000 / +0.125` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 12:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,985.69 | ⚪ **CASH** | **+4.5 bps** (±9.3) | `+9.7 bps` | `-0.006 / +0.015` | `0.29%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,240.19 | ⚪ **CASH** | **-10.3 bps** (±6.5) | `-13.2 bps` | `-0.054 / +0.018` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.60 | ⚪ **CASH** | **+0.7 bps** (±12.9) | `-4.3 bps` | `+0.000 / +0.125` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 12:15:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,964.00 | ⚪ **CASH** | **+4.5 bps** (±9.3) | `+9.7 bps` | `-0.006 / +0.015` | `0.29%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,240.86 | ⚪ **CASH** | **-10.3 bps** (±6.5) | `-13.2 bps` | `-0.054 / +0.018` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.66 | ⚪ **CASH** | **+0.7 bps** (±12.9) | `-4.3 bps` | `+0.000 / +0.125` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 12:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,981.09 | ⚪ **CASH** | **+4.5 bps** (±9.3) | `+9.7 bps` | `-0.006 / +0.015` | `0.29%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,241.02 | ⚪ **CASH** | **-10.3 bps** (±6.5) | `-13.2 bps` | `-0.054 / +0.018` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.69 | ⚪ **CASH** | **+0.7 bps** (±12.9) | `-4.3 bps` | `+0.000 / +0.125` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 11:45:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,976.76 | ⚪ **CASH** | **+4.2 bps** (±5.9) | `+12.2 bps` | `-0.010 / -0.028` | `0.30%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,240.11 | ⚪ **CASH** | **-28.5 bps** (±6.7) | `-41.0 bps` | `-0.069 / -0.035` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.63 | ⚪ **CASH** | **-0.7 bps** (±12.4) | `-5.6 bps` | `-0.009 / +0.121` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 11:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,992.72 | ⚪ **CASH** | **+4.2 bps** (±5.9) | `+12.2 bps` | `-0.010 / -0.028` | `0.30%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,240.76 | ⚪ **CASH** | **-28.5 bps** (±6.7) | `-41.0 bps` | `-0.069 / -0.035` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.69 | ⚪ **CASH** | **-0.7 bps** (±12.4) | `-5.6 bps` | `-0.009 / +0.121` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 11:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,954.01 | ⚪ **CASH** | **+4.2 bps** (±5.9) | `+12.2 bps` | `-0.010 / -0.028` | `0.30%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,237.95 | ⚪ **CASH** | **-28.5 bps** (±6.7) | `-41.0 bps` | `-0.069 / -0.035` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.33 | ⚪ **CASH** | **-0.7 bps** (±12.4) | `-5.6 bps` | `-0.009 / +0.121` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 11:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,921.30 | ⚪ **CASH** | **+4.2 bps** (±5.9) | `+12.2 bps` | `-0.010 / -0.028` | `0.30%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.96 | ⚪ **CASH** | **-28.5 bps** (±6.7) | `-41.0 bps` | `-0.069 / -0.035` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.25 | ⚪ **CASH** | **-0.7 bps** (±12.4) | `-5.6 bps` | `-0.009 / +0.121` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 10:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,899.28 | ⚪ **CASH** | **+2.5 bps** (±8.6) | `+7.7 bps` | `-0.008 / -0.005` | `0.30%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.09 | ⚪ **CASH** | **-34.3 bps** (±6.1) | `-51.8 bps` | `-0.081 / -0.014` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.22 | ⚪ **CASH** | **-2.6 bps** (±13.5) | `-5.5 bps` | `-0.016 / +0.080` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 10:30:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,877.96 | ⚪ **CASH** | **+2.5 bps** (±8.6) | `+7.7 bps` | `-0.008 / -0.005` | `0.30%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.82 | ⚪ **CASH** | **-34.3 bps** (±6.1) | `-51.8 bps` | `-0.081 / -0.014` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.09 | ⚪ **CASH** | **-2.6 bps** (±13.5) | `-5.5 bps` | `-0.016 / +0.080` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 10:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,889.77 | ⚪ **CASH** | **+2.5 bps** (±8.6) | `+7.7 bps` | `-0.008 / -0.005` | `0.30%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.07 | ⚪ **CASH** | **-34.3 bps** (±6.1) | `-51.8 bps` | `-0.081 / -0.014` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.26 | ⚪ **CASH** | **-2.6 bps** (±13.5) | `-5.5 bps` | `-0.016 / +0.080` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 10:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,933.45 | ⚪ **CASH** | **+2.5 bps** (±8.6) | `+7.7 bps` | `-0.008 / -0.005` | `0.30%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.79 | ⚪ **CASH** | **-34.3 bps** (±6.1) | `-51.8 bps` | `-0.081 / -0.014` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.27 | ⚪ **CASH** | **-2.6 bps** (±13.5) | `-5.5 bps` | `-0.016 / +0.080` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 09:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,957.13 | ⚪ **CASH** | **+8.7 bps** (±10.2) | `+11.8 bps` | `+0.013 / +0.063` | `0.31%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,237.99 | ⚪ **CASH** | **-33.0 bps** (±8.0) | `-50.7 bps` | `-0.084 / -0.004` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.26 | ⚪ **CASH** | **-2.8 bps** (±13.7) | `-6.5 bps` | `-0.019 / +0.079` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 09:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,900.62 | ⚪ **CASH** | **+8.7 bps** (±10.2) | `+11.8 bps` | `+0.013 / +0.063` | `0.31%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.68 | ⚪ **CASH** | **-33.0 bps** (±8.0) | `-50.7 bps` | `-0.084 / -0.004` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.27 | ⚪ **CASH** | **-2.8 bps** (±13.7) | `-6.5 bps` | `-0.019 / +0.079` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 09:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,881.97 | ⚪ **CASH** | **+8.7 bps** (±10.2) | `+11.8 bps` | `+0.013 / +0.063` | `0.31%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.00 | ⚪ **CASH** | **-33.0 bps** (±8.0) | `-50.7 bps` | `-0.084 / -0.004` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.11 | ⚪ **CASH** | **-2.8 bps** (±13.7) | `-6.5 bps` | `-0.019 / +0.079` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
