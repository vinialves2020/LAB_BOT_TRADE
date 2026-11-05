# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-05 17:30:51 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-05 17:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,021.36 | ⚪ **CASH** | **-9.3 bps** (±10.8) | `+9.4 bps` | `-0.117 / -0.110` | `0.72%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,255.30 | ⚪ **CASH** | **-48.4 bps** (±8.5) | `-60.4 bps` | `-0.138 / -0.102` | `0.97%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.83 | ⚪ **CASH** | **-17.3 bps** (±18.3) | `-16.9 bps` | `-0.011 / -0.066` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 17:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,100.01 | ⚪ **CASH** | **-9.3 bps** (±10.8) | `+9.4 bps` | `-0.117 / -0.110` | `0.72%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,254.88 | ⚪ **CASH** | **-48.4 bps** (±8.5) | `-60.4 bps` | `-0.138 / -0.102` | `0.97%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.92 | ⚪ **CASH** | **-17.3 bps** (±18.3) | `-16.9 bps` | `-0.011 / -0.066` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 17:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,365.09 | ⚪ **CASH** | **-9.3 bps** (±10.8) | `+9.4 bps` | `-0.117 / -0.110` | `0.72%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,265.42 | ⚪ **CASH** | **-48.4 bps** (±8.5) | `-60.4 bps` | `-0.138 / -0.102` | `0.97%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.28 | ⚪ **CASH** | **-17.3 bps** (±18.3) | `-16.9 bps` | `-0.011 / -0.066` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 16:45:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,462.40 | ⚪ **CASH** | **-16.7 bps** (±5.6) | `-0.2 bps` | `-0.120 / -0.174` | `0.72%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,265.96 | ⚪ **CASH** | **-51.0 bps** (±19.5) | `-62.5 bps` | `-0.127 / -0.126` | `0.97%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.47 | ⚪ **CASH** | **+9.3 bps** (±13.4) | `+31.8 bps` | `-0.006 / -0.091` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 16:30:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,808.33 | ⚪ **CASH** | **-16.7 bps** (±5.6) | `-0.2 bps` | `-0.120 / -0.174` | `0.72%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,277.00 | ⚪ **CASH** | **-51.0 bps** (±19.5) | `-62.5 bps` | `-0.127 / -0.126` | `0.97%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.19 | ⚪ **CASH** | **+9.3 bps** (±13.4) | `+31.8 bps` | `-0.006 / -0.091` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 16:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,442.10 | ⚪ **CASH** | **-16.7 bps** (±5.6) | `-0.2 bps` | `-0.120 / -0.174` | `0.72%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,262.96 | ⚪ **CASH** | **-51.0 bps** (±19.5) | `-62.5 bps` | `-0.127 / -0.126` | `0.97%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.87 | ⚪ **CASH** | **+9.3 bps** (±13.4) | `+31.8 bps` | `-0.006 / -0.091` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 16:01:05 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,979.99 | ⚪ **CASH** | **-16.7 bps** (±5.6) | `-0.2 bps` | `-0.120 / -0.174` | `0.72%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,250.68 | ⚪ **CASH** | **-51.0 bps** (±19.5) | `-62.5 bps` | `-0.127 / -0.126` | `0.97%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.09 | ⚪ **CASH** | **+9.3 bps** (±13.4) | `+31.8 bps` | `-0.006 / -0.091` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 15:45:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,179.34 | ⚪ **CASH** | **+0.9 bps** (±3.3) | `+15.3 bps` | `-0.030 / -0.133` | `0.51%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,272.80 | ⚪ **CASH** | **-23.9 bps** (±9.7) | `-23.7 bps` | `-0.073 / -0.143` | `0.68%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.67 | ⚪ **CASH** | **-16.0 bps** (±7.4) | `-17.6 bps` | `+0.007 / -0.144` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 15:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,486.81 | ⚪ **CASH** | **+0.9 bps** (±3.3) | `+15.3 bps` | `-0.030 / -0.133` | `0.51%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,276.00 | ⚪ **CASH** | **-23.9 bps** (±9.7) | `-23.7 bps` | `-0.073 / -0.143` | `0.68%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.97 | ⚪ **CASH** | **-16.0 bps** (±7.4) | `-17.6 bps` | `+0.007 / -0.144` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 15:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,176.01 | ⚪ **CASH** | **+0.9 bps** (±3.3) | `+15.3 bps` | `-0.030 / -0.133` | `0.51%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,289.89 | ⚪ **CASH** | **-23.9 bps** (±9.7) | `-23.7 bps` | `-0.073 / -0.143` | `0.68%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.05 | ⚪ **CASH** | **-16.0 bps** (±7.4) | `-17.6 bps` | `+0.007 / -0.144` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 15:00:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,175.30 | ⚪ **CASH** | **+0.9 bps** (±3.3) | `+15.3 bps` | `-0.030 / -0.133` | `0.51%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,340.58 | ⚪ **CASH** | **-23.9 bps** (±9.7) | `-23.7 bps` | `-0.073 / -0.143` | `0.68%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.97 | ⚪ **CASH** | **-16.0 bps** (±7.4) | `-17.6 bps` | `+0.007 / -0.144` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 14:45:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,864.00 | ⚪ **CASH** | **+2.6 bps** (±2.6) | `+18.3 bps` | `-0.012 / -0.174` | `0.41%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,364.32 | ⚪ **CASH** | **-31.3 bps** (±4.9) | `-35.7 bps` | `-0.052 / -0.223` | `0.61%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.92 | ⚪ **CASH** | **-16.9 bps** (±7.9) | `-24.3 bps` | `+0.031 / -0.112` | `0.66%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 14:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,558.59 | ⚪ **CASH** | **+2.6 bps** (±2.6) | `+18.3 bps` | `-0.012 / -0.174` | `0.41%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,387.23 | ⚪ **CASH** | **-31.3 bps** (±4.9) | `-35.7 bps` | `-0.052 / -0.223` | `0.61%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.44 | ⚪ **CASH** | **-16.9 bps** (±7.9) | `-24.3 bps` | `+0.031 / -0.112` | `0.66%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 14:16:21 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,450.19 | ⚪ **CASH** | **+2.6 bps** (±2.6) | `+18.3 bps` | `-0.012 / -0.174` | `0.41%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,381.80 | ⚪ **CASH** | **-31.3 bps** (±4.9) | `-35.7 bps` | `-0.052 / -0.223` | `0.61%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.19 | ⚪ **CASH** | **-16.9 bps** (±7.9) | `-24.3 bps` | `+0.031 / -0.112` | `0.66%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 14:01:29 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,620.01 | ⚪ **CASH** | **+2.6 bps** (±2.6) | `+18.3 bps` | `-0.012 / -0.174` | `0.41%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,386.67 | ⚪ **CASH** | **-31.3 bps** (±4.9) | `-35.7 bps` | `-0.052 / -0.223` | `0.61%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.30 | ⚪ **CASH** | **-16.9 bps** (±7.9) | `-24.3 bps` | `+0.031 / -0.112` | `0.66%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 13:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,809.27 | ⚪ **CASH** | **-2.5 bps** (±4.2) | `+14.0 bps` | `-0.008 / -0.255` | `0.42%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,393.87 | ⚪ **CASH** | **-38.7 bps** (±8.9) | `-45.1 bps` | `-0.048 / -0.283` | `0.61%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.59 | ⚪ **CASH** | **-15.7 bps** (±3.2) | `-24.6 bps` | `+0.040 / -0.106` | `0.67%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 13:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,626.65 | ⚪ **CASH** | **-2.5 bps** (±4.2) | `+14.0 bps` | `-0.008 / -0.255` | `0.42%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,387.27 | ⚪ **CASH** | **-38.7 bps** (±8.9) | `-45.1 bps` | `-0.048 / -0.283` | `0.61%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.31 | ⚪ **CASH** | **-15.7 bps** (±3.2) | `-24.6 bps` | `+0.040 / -0.106` | `0.67%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 13:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,714.01 | ⚪ **CASH** | **-2.5 bps** (±4.2) | `+14.0 bps` | `-0.008 / -0.255` | `0.42%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,390.27 | ⚪ **CASH** | **-38.7 bps** (±8.9) | `-45.1 bps` | `-0.048 / -0.283` | `0.61%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.46 | ⚪ **CASH** | **-15.7 bps** (±3.2) | `-24.6 bps` | `+0.040 / -0.106` | `0.67%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 13:00:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,699.00 | ⚪ **CASH** | **-2.5 bps** (±4.2) | `+14.0 bps` | `-0.008 / -0.255` | `0.42%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,395.30 | ⚪ **CASH** | **-38.7 bps** (±8.9) | `-45.1 bps` | `-0.048 / -0.283` | `0.61%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.44 | ⚪ **CASH** | **-15.7 bps** (±3.2) | `-24.6 bps` | `+0.040 / -0.106` | `0.67%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 12:46:24 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,761.27 | ⚪ **CASH** | **-3.9 bps** (±3.5) | `+10.3 bps` | `-0.004 / -0.247` | `0.39%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,395.15 | ⚪ **CASH** | **-26.5 bps** (±3.5) | `-21.0 bps` | `-0.046 / -0.332` | `0.58%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.31 | ⚪ **CASH** | **-27.8 bps** (±9.8) | `-53.3 bps` | `+0.050 / -0.004` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 12:31:24 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,015.54 | ⚪ **CASH** | **-3.9 bps** (±3.5) | `+10.3 bps` | `-0.004 / -0.247` | `0.39%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,409.01 | ⚪ **CASH** | **-26.5 bps** (±3.5) | `-21.0 bps` | `-0.046 / -0.332` | `0.58%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.76 | ⚪ **CASH** | **-27.8 bps** (±9.8) | `-53.3 bps` | `+0.050 / -0.004` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 12:16:29 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,142.72 | ⚪ **CASH** | **-3.9 bps** (±3.5) | `+10.3 bps` | `-0.004 / -0.247` | `0.39%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,413.11 | ⚪ **CASH** | **-26.5 bps** (±3.5) | `-21.0 bps` | `-0.046 / -0.332` | `0.58%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.04 | ⚪ **CASH** | **-27.8 bps** (±9.8) | `-53.3 bps` | `+0.050 / -0.004` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 12:01:28 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,238.99 | ⚪ **CASH** | **-3.9 bps** (±3.5) | `+10.3 bps` | `-0.004 / -0.247` | `0.39%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,417.08 | ⚪ **CASH** | **-26.5 bps** (±3.5) | `-21.0 bps` | `-0.046 / -0.332` | `0.58%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.27 | ⚪ **CASH** | **-27.8 bps** (±9.8) | `-53.3 bps` | `+0.050 / -0.004` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 11:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,375.10 | ⚪ **CASH** | **-4.3 bps** (±3.9) | `+11.2 bps` | `-0.005 / -0.271` | `0.39%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,420.34 | ⚪ **CASH** | **-25.7 bps** (±4.2) | `-19.3 bps` | `-0.043 / -0.339` | `0.59%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.59 | ⚪ **CASH** | **-27.5 bps** (±9.4) | `-52.0 bps` | `+0.056 / -0.023` | `0.64%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 11:31:18 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,280.81 | ⚪ **CASH** | **-4.3 bps** (±3.9) | `+11.2 bps` | `-0.005 / -0.271` | `0.39%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,417.12 | ⚪ **CASH** | **-25.7 bps** (±4.2) | `-19.3 bps` | `-0.043 / -0.339` | `0.59%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.49 | ⚪ **CASH** | **-27.5 bps** (±9.4) | `-52.0 bps` | `+0.056 / -0.023` | `0.64%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 11:16:10 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,306.42 | ⚪ **CASH** | **-4.3 bps** (±3.9) | `+11.2 bps` | `-0.005 / -0.271` | `0.39%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,419.76 | ⚪ **CASH** | **-25.7 bps** (±4.2) | `-19.3 bps` | `-0.043 / -0.339` | `0.59%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.65 | ⚪ **CASH** | **-27.5 bps** (±9.4) | `-52.0 bps` | `+0.056 / -0.023` | `0.64%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 11:01:19 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,305.65 | ⚪ **CASH** | **-4.3 bps** (±3.9) | `+11.2 bps` | `-0.005 / -0.271` | `0.39%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,420.09 | ⚪ **CASH** | **-25.7 bps** (±4.2) | `-19.3 bps` | `-0.043 / -0.339` | `0.59%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.74 | ⚪ **CASH** | **-27.5 bps** (±9.4) | `-52.0 bps` | `+0.056 / -0.023` | `0.64%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 10:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,305.70 | ⚪ **CASH** | **-2.3 bps** (±3.2) | `+14.2 bps` | `-0.001 / -0.271` | `0.39%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,417.64 | ⚪ **CASH** | **-26.6 bps** (±4.4) | `-21.0 bps` | `-0.036 / -0.352` | `0.59%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.66 | ⚪ **CASH** | **-24.3 bps** (±8.6) | `-48.1 bps` | `+0.063 / -0.012` | `0.65%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 10:31:17 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,508.19 | ⚪ **CASH** | **-2.3 bps** (±3.2) | `+14.2 bps` | `-0.001 / -0.271` | `0.39%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,420.22 | ⚪ **CASH** | **-26.6 bps** (±4.4) | `-21.0 bps` | `-0.036 / -0.352` | `0.59%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.87 | ⚪ **CASH** | **-24.3 bps** (±8.6) | `-48.1 bps` | `+0.063 / -0.012` | `0.65%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 10:16:13 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,388.65 | ⚪ **CASH** | **-2.3 bps** (±3.2) | `+14.2 bps` | `-0.001 / -0.271` | `0.39%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,417.99 | ⚪ **CASH** | **-26.6 bps** (±4.4) | `-21.0 bps` | `-0.036 / -0.352` | `0.59%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.80 | ⚪ **CASH** | **-24.3 bps** (±8.6) | `-48.1 bps` | `+0.063 / -0.012` | `0.65%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 10:01:26 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,412.00 | ⚪ **CASH** | **-2.3 bps** (±3.2) | `+14.2 bps` | `-0.001 / -0.271` | `0.39%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,417.76 | ⚪ **CASH** | **-26.6 bps** (±4.4) | `-21.0 bps` | `-0.036 / -0.352` | `0.59%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.81 | ⚪ **CASH** | **-24.3 bps** (±8.6) | `-48.1 bps` | `+0.063 / -0.012` | `0.65%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 09:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,322.47 | ⚪ **CASH** | **-2.3 bps** (±2.2) | `+11.5 bps` | `+0.012 / -0.262` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,414.10 | ⚪ **CASH** | **-22.9 bps** (±4.6) | `-22.7 bps` | `-0.020 / -0.255` | `0.60%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.68 | ⚪ **CASH** | **-20.3 bps** (±5.8) | `-44.7 bps` | `+0.074 / +0.014` | `0.66%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 09:30:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,293.79 | ⚪ **CASH** | **-2.3 bps** (±2.2) | `+11.5 bps` | `+0.012 / -0.262` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,412.54 | ⚪ **CASH** | **-22.9 bps** (±4.6) | `-22.7 bps` | `-0.020 / -0.255` | `0.60%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.60 | ⚪ **CASH** | **-20.3 bps** (±5.8) | `-44.7 bps` | `+0.074 / +0.014` | `0.66%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 09:16:10 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,347.49 | ⚪ **CASH** | **-2.3 bps** (±2.2) | `+11.5 bps` | `+0.012 / -0.262` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,414.55 | ⚪ **CASH** | **-22.9 bps** (±4.6) | `-22.7 bps` | `-0.020 / -0.255` | `0.60%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.55 | ⚪ **CASH** | **-20.3 bps** (±5.8) | `-44.7 bps` | `+0.074 / +0.014` | `0.66%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 09:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,494.16 | ⚪ **CASH** | **-2.3 bps** (±2.2) | `+11.5 bps` | `+0.012 / -0.262` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,419.70 | ⚪ **CASH** | **-22.9 bps** (±4.6) | `-22.7 bps` | `-0.020 / -0.255` | `0.60%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.80 | ⚪ **CASH** | **-20.3 bps** (±5.8) | `-44.7 bps` | `+0.074 / +0.014` | `0.66%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 08:46:15 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,503.35 | ⚪ **CASH** | **-2.0 bps** (±4.3) | `+10.1 bps` | `+0.028 / -0.263` | `0.40%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,420.34 | ⚪ **CASH** | **-23.5 bps** (±4.7) | `-27.6 bps` | `-0.008 / -0.229` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.59 | ⚪ **CASH** | **-17.5 bps** (±7.1) | `-38.9 bps` | `+0.081 / -0.013` | `0.65%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
