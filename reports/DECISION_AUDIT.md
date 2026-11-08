# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-08 23:15:37 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-08 23:15:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,384.05 | ⚪ **CASH** | **-29.2 bps** (±5.4) | `-42.3 bps` | `-0.030 / -0.081` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,157.97 | ⚪ **CASH** | **-42.5 bps** (±27.1) | `-53.5 bps` | `-0.094 / -0.124` | `0.82%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.88 | ⚪ **CASH** | **-24.3 bps** (±8.8) | `-40.9 bps` | `+0.007 / -0.014` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 23:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,787.56 | ⚪ **CASH** | **-29.2 bps** (±5.4) | `-42.3 bps` | `-0.030 / -0.081` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,135.32 | ⚪ **CASH** | **-42.5 bps** (±27.1) | `-53.5 bps` | `-0.094 / -0.124` | `0.82%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.76 | ⚪ **CASH** | **-24.3 bps** (±8.8) | `-40.9 bps` | `+0.007 / -0.014` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 22:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,290.00 | ⚪ **CASH** | **-53.3 bps** (±14.4) | `-75.6 bps` | `-0.050 / -0.174` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,123.03 | ⚪ **CASH** | **-60.8 bps** (±19.6) | `-77.3 bps` | `-0.140 / -0.205` | `0.83%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.87 | ⚪ **CASH** | **-15.1 bps** (±11.4) | `-20.2 bps` | `+0.000 / -0.044` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 22:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,344.84 | ⚪ **CASH** | **-53.3 bps** (±14.4) | `-75.6 bps` | `-0.050 / -0.174` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,121.98 | ⚪ **CASH** | **-60.8 bps** (±19.6) | `-77.3 bps` | `-0.140 / -0.205` | `0.83%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $85.95 | ⚪ **CASH** | **-15.1 bps** (±11.4) | `-20.2 bps` | `+0.000 / -0.044` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 22:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,602.43 | ⚪ **CASH** | **-53.3 bps** (±14.4) | `-75.6 bps` | `-0.050 / -0.174` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,134.98 | ⚪ **CASH** | **-60.8 bps** (±19.6) | `-77.3 bps` | `-0.140 / -0.205` | `0.83%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.86 | ⚪ **CASH** | **-15.1 bps** (±11.4) | `-20.2 bps` | `+0.000 / -0.044` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 22:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,261.37 | ⚪ **CASH** | **-53.3 bps** (±14.4) | `-75.6 bps` | `-0.050 / -0.174` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,130.95 | ⚪ **CASH** | **-60.8 bps** (±19.6) | `-77.3 bps` | `-0.140 / -0.205` | `0.83%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.31 | ⚪ **CASH** | **-15.1 bps** (±11.4) | `-20.2 bps` | `+0.000 / -0.044` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 21:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,424.07 | ⚪ **CASH** | **+21.6 bps** (±8.3) | `+51.4 bps` | `+0.006 / -0.175` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,218.28 | ⚪ **CASH** | **+9.8 bps** (±7.8) | `+31.8 bps` | `-0.032 / -0.148` | `0.21%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $88.60 | ⚪ **CASH** | **+26.4 bps** (±13.9) | `+35.5 bps` | `+0.071 / +0.118` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 21:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,701.54 | ⚪ **CASH** | **+21.6 bps** (±8.3) | `+51.4 bps` | `+0.006 / -0.175` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,224.79 | ⚪ **CASH** | **+9.8 bps** (±7.8) | `+31.8 bps` | `-0.032 / -0.148` | `0.21%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.04 | ⚪ **CASH** | **+26.4 bps** (±13.9) | `+35.5 bps` | `+0.071 / +0.118` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 21:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,765.55 | ⚪ **CASH** | **+21.6 bps** (±8.3) | `+51.4 bps` | `+0.006 / -0.175` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,226.79 | ⚪ **CASH** | **+9.8 bps** (±7.8) | `+31.8 bps` | `-0.032 / -0.148` | `0.21%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.13 | ⚪ **CASH** | **+26.4 bps** (±13.9) | `+35.5 bps` | `+0.071 / +0.118` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 21:00:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,769.69 | ⚪ **CASH** | **+21.6 bps** (±8.3) | `+51.4 bps` | `+0.006 / -0.175` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,227.71 | ⚪ **CASH** | **+9.8 bps** (±7.8) | `+31.8 bps` | `-0.032 / -0.148` | `0.21%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.17 | ⚪ **CASH** | **+26.4 bps** (±13.9) | `+35.5 bps` | `+0.071 / +0.118` | `0.33%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 20:45:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,838.42 | ⚪ **CASH** | **+19.5 bps** (±9.4) | `+41.1 bps` | `+0.017 / -0.097` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,228.35 | ⚪ **CASH** | **+14.9 bps** (±9.7) | `+33.7 bps` | `-0.014 / -0.066` | `0.21%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.35 | ⚪ **CASH** | **+24.8 bps** (±10.2) | `+32.0 bps` | `+0.058 / +0.129` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 20:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,900.12 | ⚪ **CASH** | **+19.5 bps** (±9.4) | `+41.1 bps` | `+0.017 / -0.097` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,230.59 | ⚪ **CASH** | **+14.9 bps** (±9.7) | `+33.7 bps` | `-0.014 / -0.066` | `0.21%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.55 | ⚪ **CASH** | **+24.8 bps** (±10.2) | `+32.0 bps` | `+0.058 / +0.129` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 20:15:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,892.26 | ⚪ **CASH** | **+19.5 bps** (±9.4) | `+41.1 bps` | `+0.017 / -0.097` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,228.90 | ⚪ **CASH** | **+14.9 bps** (±9.7) | `+33.7 bps` | `-0.014 / -0.066` | `0.21%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.49 | ⚪ **CASH** | **+24.8 bps** (±10.2) | `+32.0 bps` | `+0.058 / +0.129` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 20:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,929.04 | ⚪ **CASH** | **+19.5 bps** (±9.4) | `+41.1 bps` | `+0.017 / -0.097` | `0.16%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,231.57 | ⚪ **CASH** | **+14.9 bps** (±9.7) | `+33.7 bps` | `-0.014 / -0.066` | `0.21%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.53 | ⚪ **CASH** | **+24.8 bps** (±10.2) | `+32.0 bps` | `+0.058 / +0.129` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 19:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,913.61 | ⚪ **CASH** | **+32.1 bps** (±16.9) | `+57.0 bps` | `+0.028 / +0.004` | `0.17%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,233.52 | ⚪ **CASH** | **+16.2 bps** (±10.2) | `+33.0 bps` | `-0.018 / -0.021` | `0.22%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.66 | ⚪ **CASH** | **+25.7 bps** (±7.7) | `+31.9 bps` | `+0.058 / +0.142` | `0.33%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 19:30:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,904.04 | ⚪ **CASH** | **+32.1 bps** (±16.9) | `+57.0 bps` | `+0.028 / +0.004` | `0.17%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,233.36 | ⚪ **CASH** | **+16.2 bps** (±10.2) | `+33.0 bps` | `-0.018 / -0.021` | `0.22%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.61 | ⚪ **CASH** | **+25.7 bps** (±7.7) | `+31.9 bps` | `+0.058 / +0.142` | `0.33%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 19:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,857.43 | ⚪ **CASH** | **+32.1 bps** (±16.9) | `+57.0 bps` | `+0.028 / +0.004` | `0.17%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,233.01 | ⚪ **CASH** | **+16.2 bps** (±10.2) | `+33.0 bps` | `-0.018 / -0.021` | `0.22%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.34 | ⚪ **CASH** | **+25.7 bps** (±7.7) | `+31.9 bps` | `+0.058 / +0.142` | `0.33%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 19:00:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,914.43 | ⚪ **CASH** | **+32.1 bps** (±16.9) | `+57.0 bps` | `+0.028 / +0.004` | `0.17%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.17 | ⚪ **CASH** | **+16.2 bps** (±10.2) | `+33.0 bps` | `-0.018 / -0.021` | `0.22%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.46 | ⚪ **CASH** | **+25.7 bps** (±7.7) | `+31.9 bps` | `+0.058 / +0.142` | `0.33%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 18:45:34 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,934.81 | ⚪ **CASH** | **+32.4 bps** (±6.4) | `+57.4 bps` | `+0.021 / -0.008` | `0.16%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.49 | ⚪ **CASH** | **+11.7 bps** (±6.6) | `+25.0 bps` | `-0.011 / -0.038` | `0.21%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.59 | ⚪ **CASH** | **+25.1 bps** (±14.0) | `+38.6 bps` | `+0.043 / +0.066` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 18:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,942.01 | ⚪ **CASH** | **+32.4 bps** (±6.4) | `+57.4 bps` | `+0.021 / -0.008` | `0.16%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.26 | ⚪ **CASH** | **+11.7 bps** (±6.6) | `+25.0 bps` | `-0.011 / -0.038` | `0.21%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.67 | ⚪ **CASH** | **+25.1 bps** (±14.0) | `+38.6 bps` | `+0.043 / +0.066` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 18:15:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,920.01 | ⚪ **CASH** | **+32.4 bps** (±6.4) | `+57.4 bps` | `+0.021 / -0.008` | `0.16%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.74 | ⚪ **CASH** | **+11.7 bps** (±6.6) | `+25.0 bps` | `-0.011 / -0.038` | `0.21%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.54 | ⚪ **CASH** | **+25.1 bps** (±14.0) | `+38.6 bps` | `+0.043 / +0.066` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

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
