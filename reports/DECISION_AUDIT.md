# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-17 05:15:45 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-17 05:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,801.00 | ⚪ **CASH** | **+27.8 bps** (±7.1) | `+40.4 bps` | `+0.053 / +0.054` | `0.67%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.9 bps) |
| **ETHUSDT** | $1,829.77 | ⚪ **CASH** | **+14.4 bps** (±8.2) | `+36.7 bps` | `-0.030 / -0.134` | `0.86%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.66 | ⚪ **CASH** | **+3.6 bps** (±13.1) | `+34.2 bps` | `-0.172 / -0.168` | `0.91%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 05:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,981.96 | ⚪ **CASH** | **+27.8 bps** (±7.1) | `+40.4 bps` | `+0.053 / +0.054` | `0.67%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.9 bps) |
| **ETHUSDT** | $1,832.71 | ⚪ **CASH** | **+14.4 bps** (±8.2) | `+36.7 bps` | `-0.030 / -0.134` | `0.86%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.96 | ⚪ **CASH** | **+3.6 bps** (±13.1) | `+34.2 bps` | `-0.172 / -0.168` | `0.91%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 04:45:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,022.19 | ⚪ **CASH** | **+28.8 bps** (±13.6) | `+44.1 bps` | `+0.051 / +0.049` | `0.68%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.9 bps) |
| **ETHUSDT** | $1,833.23 | ⚪ **CASH** | **+11.5 bps** (±2.6) | `+26.9 bps` | `-0.024 / -0.087` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.94 | ⚪ **CASH** | **+7.5 bps** (±20.2) | `+45.4 bps` | `-0.180 / -0.198` | `0.93%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (20.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-17 04:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,952.86 | ⚪ **CASH** | **+28.8 bps** (±13.6) | `+44.1 bps` | `+0.051 / +0.049` | `0.68%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.9 bps) |
| **ETHUSDT** | $1,827.09 | ⚪ **CASH** | **+11.5 bps** (±2.6) | `+26.9 bps` | `-0.024 / -0.087` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.66 | ⚪ **CASH** | **+7.5 bps** (±20.2) | `+45.4 bps` | `-0.180 / -0.198` | `0.93%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (20.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-17 04:15:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,941.21 | ⚪ **CASH** | **+28.8 bps** (±13.6) | `+44.1 bps` | `+0.051 / +0.049` | `0.68%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.9 bps) |
| **ETHUSDT** | $1,828.79 | ⚪ **CASH** | **+11.5 bps** (±2.6) | `+26.9 bps` | `-0.024 / -0.087` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.85 | ⚪ **CASH** | **+7.5 bps** (±20.2) | `+45.4 bps` | `-0.180 / -0.198` | `0.93%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (20.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-17 04:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,040.99 | ⚪ **CASH** | **+28.8 bps** (±13.6) | `+44.1 bps` | `+0.051 / +0.049` | `0.68%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.9 bps) |
| **ETHUSDT** | $1,833.12 | ⚪ **CASH** | **+11.5 bps** (±2.6) | `+26.9 bps` | `-0.024 / -0.087` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.86 | ⚪ **CASH** | **+7.5 bps** (±20.2) | `+45.4 bps` | `-0.180 / -0.198` | `0.93%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (20.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-17 03:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,077.95 | ⚪ **CASH** | **+29.2 bps** (±7.5) | `+45.6 bps` | `+0.043 / +0.038` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,831.96 | ⚪ **CASH** | **+25.2 bps** (±3.1) | `+54.1 bps` | `-0.024 / -0.114` | `0.87%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.63 | ⚪ **CASH** | **+2.1 bps** (±13.3) | `+35.5 bps` | `-0.183 / -0.206` | `0.91%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 03:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,123.36 | ⚪ **CASH** | **+29.2 bps** (±7.5) | `+45.6 bps` | `+0.043 / +0.038` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,832.37 | ⚪ **CASH** | **+25.2 bps** (±3.1) | `+54.1 bps` | `-0.024 / -0.114` | `0.87%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.66 | ⚪ **CASH** | **+2.1 bps** (±13.3) | `+35.5 bps` | `-0.183 / -0.206` | `0.91%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 03:15:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,664.07 | ⚪ **CASH** | **+29.2 bps** (±7.5) | `+45.6 bps` | `+0.043 / +0.038` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,819.52 | ⚪ **CASH** | **+25.2 bps** (±3.1) | `+54.1 bps` | `-0.024 / -0.114` | `0.87%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.11 | ⚪ **CASH** | **+2.1 bps** (±13.3) | `+35.5 bps` | `-0.183 / -0.206` | `0.91%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 03:00:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,509.78 | ⚪ **CASH** | **+29.2 bps** (±7.5) | `+45.6 bps` | `+0.043 / +0.038` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,814.54 | ⚪ **CASH** | **+25.2 bps** (±3.1) | `+54.1 bps` | `-0.024 / -0.114` | `0.87%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.77 | ⚪ **CASH** | **+2.1 bps** (±13.3) | `+35.5 bps` | `-0.183 / -0.206` | `0.91%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 02:45:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,552.20 | ⚪ **CASH** | **+25.5 bps** (±11.0) | `+36.6 bps` | `+0.043 / +0.082` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,817.40 | ⚪ **CASH** | **+18.8 bps** (±7.9) | `+41.1 bps` | `-0.020 / -0.086` | `0.88%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.83 | ⚪ **CASH** | **-2.6 bps** (±8.3) | `+21.7 bps` | `-0.168 / -0.160` | `0.92%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 02:31:00 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,425.74 | ⚪ **CASH** | **+25.5 bps** (±11.0) | `+36.6 bps` | `+0.043 / +0.082` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,815.04 | ⚪ **CASH** | **+18.8 bps** (±7.9) | `+41.1 bps` | `-0.020 / -0.086` | `0.88%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.72 | ⚪ **CASH** | **-2.6 bps** (±8.3) | `+21.7 bps` | `-0.168 / -0.160` | `0.92%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 02:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,596.05 | ⚪ **CASH** | **+25.5 bps** (±11.0) | `+36.6 bps` | `+0.043 / +0.082` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,816.80 | ⚪ **CASH** | **+18.8 bps** (±7.9) | `+41.1 bps` | `-0.020 / -0.086` | `0.88%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.70 | ⚪ **CASH** | **-2.6 bps** (±8.3) | `+21.7 bps` | `-0.168 / -0.160` | `0.92%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 02:01:00 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,773.93 | ⚪ **CASH** | **+25.5 bps** (±11.0) | `+36.6 bps` | `+0.043 / +0.082` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,821.44 | ⚪ **CASH** | **+18.8 bps** (±7.9) | `+41.1 bps` | `-0.020 / -0.086` | `0.88%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.86 | ⚪ **CASH** | **-2.6 bps** (±8.3) | `+21.7 bps` | `-0.168 / -0.160` | `0.92%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 01:45:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,871.75 | ⚪ **CASH** | **+15.6 bps** (±16.8) | `+24.3 bps` | `+0.033 / +0.036` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,823.36 | ⚪ **CASH** | **+22.9 bps** (±5.4) | `+48.0 bps` | `-0.024 / -0.071` | `0.89%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.84 | ⚪ **CASH** | **-3.6 bps** (±5.4) | `+17.0 bps` | `-0.158 / -0.134` | `0.93%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 01:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,569.06 | ⚪ **CASH** | **+15.6 bps** (±16.8) | `+24.3 bps` | `+0.033 / +0.036` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,814.16 | ⚪ **CASH** | **+22.9 bps** (±5.4) | `+48.0 bps` | `-0.024 / -0.071` | `0.89%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.53 | ⚪ **CASH** | **-3.6 bps** (±5.4) | `+17.0 bps` | `-0.158 / -0.134` | `0.93%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 01:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,623.85 | ⚪ **CASH** | **+15.6 bps** (±16.8) | `+24.3 bps` | `+0.033 / +0.036` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,817.13 | ⚪ **CASH** | **+22.9 bps** (±5.4) | `+48.0 bps` | `-0.024 / -0.071` | `0.89%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.64 | ⚪ **CASH** | **-3.6 bps** (±5.4) | `+17.0 bps` | `-0.158 / -0.134` | `0.93%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 01:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,627.77 | ⚪ **CASH** | **+15.6 bps** (±16.8) | `+24.3 bps` | `+0.033 / +0.036` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,814.57 | ⚪ **CASH** | **+22.9 bps** (±5.4) | `+48.0 bps` | `-0.024 / -0.071` | `0.89%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.54 | ⚪ **CASH** | **-3.6 bps** (±5.4) | `+17.0 bps` | `-0.158 / -0.134` | `0.93%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 00:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,613.29 | ⚪ **CASH** | **+25.9 bps** (±13.7) | `+41.2 bps` | `+0.027 / +0.065` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,814.38 | ⚪ **CASH** | **+30.2 bps** (±7.0) | `+59.4 bps` | `-0.020 / -0.039` | `0.90%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.48 | ⚪ **CASH** | **+4.1 bps** (±6.8) | `+29.9 bps` | `-0.151 / -0.120` | `0.94%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 00:30:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,554.36 | ⚪ **CASH** | **+25.9 bps** (±13.7) | `+41.2 bps` | `+0.027 / +0.065` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,814.12 | ⚪ **CASH** | **+30.2 bps** (±7.0) | `+59.4 bps` | `-0.020 / -0.039` | `0.90%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.41 | ⚪ **CASH** | **+4.1 bps** (±6.8) | `+29.9 bps` | `-0.151 / -0.120` | `0.94%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 00:16:00 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,709.28 | ⚪ **CASH** | **+25.9 bps** (±13.7) | `+41.2 bps` | `+0.027 / +0.065` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,818.61 | ⚪ **CASH** | **+30.2 bps** (±7.0) | `+59.4 bps` | `-0.020 / -0.039` | `0.90%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.59 | ⚪ **CASH** | **+4.1 bps** (±6.8) | `+29.9 bps` | `-0.151 / -0.120` | `0.94%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 00:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,922.97 | ⚪ **CASH** | **+25.9 bps** (±13.7) | `+41.2 bps` | `+0.027 / +0.065` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,821.99 | ⚪ **CASH** | **+30.2 bps** (±7.0) | `+59.4 bps` | `-0.020 / -0.039` | `0.90%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.61 | ⚪ **CASH** | **+4.1 bps** (±6.8) | `+29.9 bps` | `-0.151 / -0.120` | `0.94%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 23:45:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,854.48 | ⚪ **CASH** | **+22.4 bps** (±26.1) | `+34.0 bps` | `+0.027 / +0.114` | `0.70%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |
| **ETHUSDT** | $1,818.67 | ⚪ **CASH** | **+33.5 bps** (±10.4) | `+66.4 bps` | `-0.021 / -0.045` | `0.91%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.21 | ⚪ **CASH** | **-3.7 bps** (±12.5) | `+15.2 bps` | `-0.139 / -0.112` | `0.96%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 23:30:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,227.38 | ⚪ **CASH** | **+22.4 bps** (±26.1) | `+34.0 bps` | `+0.027 / +0.114` | `0.70%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |
| **ETHUSDT** | $1,822.80 | ⚪ **CASH** | **+33.5 bps** (±10.4) | `+66.4 bps` | `-0.021 / -0.045` | `0.91%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.55 | ⚪ **CASH** | **-3.7 bps** (±12.5) | `+15.2 bps` | `-0.139 / -0.112` | `0.96%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 23:15:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,315.57 | ⚪ **CASH** | **+22.4 bps** (±26.1) | `+34.0 bps` | `+0.027 / +0.114` | `0.70%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |
| **ETHUSDT** | $1,830.12 | ⚪ **CASH** | **+33.5 bps** (±10.4) | `+66.4 bps` | `-0.021 / -0.045` | `0.91%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.83 | ⚪ **CASH** | **-3.7 bps** (±12.5) | `+15.2 bps` | `-0.139 / -0.112` | `0.96%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 23:00:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,262.69 | ⚪ **CASH** | **+22.4 bps** (±26.1) | `+34.0 bps` | `+0.027 / +0.114` | `0.70%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |
| **ETHUSDT** | $1,825.72 | ⚪ **CASH** | **+33.5 bps** (±10.4) | `+66.4 bps` | `-0.021 / -0.045` | `0.91%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.59 | ⚪ **CASH** | **-3.7 bps** (±12.5) | `+15.2 bps` | `-0.139 / -0.112` | `0.96%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 22:45:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,489.23 | ⚪ **CASH** | **+33.8 bps** (±19.4) | `+50.6 bps` | `+0.029 / +0.155` | `0.71%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,833.10 | ⚪ **CASH** | **+35.9 bps** (±14.8) | `+70.7 bps` | `-0.017 / -0.037` | `0.92%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.02 | ⚪ **CASH** | **-0.7 bps** (±15.5) | `+20.4 bps` | `-0.134 / -0.109` | `0.97%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 22:31:04 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,358.82 | ⚪ **CASH** | **+33.8 bps** (±19.4) | `+50.6 bps` | `+0.029 / +0.155` | `0.71%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,833.81 | ⚪ **CASH** | **+35.9 bps** (±14.8) | `+70.7 bps` | `-0.017 / -0.037` | `0.92%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.94 | ⚪ **CASH** | **-0.7 bps** (±15.5) | `+20.4 bps` | `-0.134 / -0.109` | `0.97%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 22:15:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,471.48 | ⚪ **CASH** | **+33.8 bps** (±19.4) | `+50.6 bps` | `+0.029 / +0.155` | `0.71%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,836.72 | ⚪ **CASH** | **+35.9 bps** (±14.8) | `+70.7 bps` | `-0.017 / -0.037` | `0.92%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.12 | ⚪ **CASH** | **-0.7 bps** (±15.5) | `+20.4 bps` | `-0.134 / -0.109` | `0.97%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 22:01:05 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,351.52 | ⚪ **CASH** | **+33.8 bps** (±19.4) | `+50.6 bps` | `+0.029 / +0.155` | `0.71%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,831.50 | ⚪ **CASH** | **+35.9 bps** (±14.8) | `+70.7 bps` | `-0.017 / -0.037` | `0.92%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.98 | ⚪ **CASH** | **-0.7 bps** (±15.5) | `+20.4 bps` | `-0.134 / -0.109` | `0.97%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 21:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,310.41 | ⚪ **CASH** | **+12.3 bps** (±22.8) | `+16.1 bps` | `+0.008 / +0.141` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.8 bps > 19.5) |
| **ETHUSDT** | $1,827.65 | ⚪ **CASH** | **+40.4 bps** (±12.7) | `+78.5 bps` | `-0.017 / -0.021` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $71.93 | ⚪ **CASH** | **-5.2 bps** (±16.2) | `+14.7 bps` | `-0.133 / -0.130` | `0.98%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-16 21:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,256.34 | ⚪ **CASH** | **+12.3 bps** (±22.8) | `+16.1 bps` | `+0.008 / +0.141` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.8 bps > 19.5) |
| **ETHUSDT** | $1,825.83 | ⚪ **CASH** | **+40.4 bps** (±12.7) | `+78.5 bps` | `-0.017 / -0.021` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $71.82 | ⚪ **CASH** | **-5.2 bps** (±16.2) | `+14.7 bps` | `-0.133 / -0.130` | `0.98%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-16 21:16:23 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,010.01 | ⚪ **CASH** | **+12.3 bps** (±22.8) | `+16.1 bps` | `+0.008 / +0.141` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.8 bps > 19.5) |
| **ETHUSDT** | $1,819.68 | ⚪ **CASH** | **+40.4 bps** (±12.7) | `+78.5 bps` | `-0.017 / -0.021` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $71.46 | ⚪ **CASH** | **-5.2 bps** (±16.2) | `+14.7 bps` | `-0.133 / -0.130` | `0.98%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-16 21:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,042.00 | ⚪ **CASH** | **+12.3 bps** (±22.8) | `+16.1 bps` | `+0.008 / +0.141` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.8 bps > 19.5) |
| **ETHUSDT** | $1,819.74 | ⚪ **CASH** | **+40.4 bps** (±12.7) | `+78.5 bps` | `-0.017 / -0.021` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $71.34 | ⚪ **CASH** | **-5.2 bps** (±16.2) | `+14.7 bps` | `-0.133 / -0.130` | `0.98%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-16 20:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,996.01 | ⚪ **CASH** | **+6.3 bps** (±22.5) | `+7.9 bps` | `-0.009 / +0.137` | `0.73%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.5 bps > 19.5) |
| **ETHUSDT** | $1,819.62 | ⚪ **CASH** | **+44.3 bps** (±19.8) | `+85.4 bps` | `-0.020 / +0.017` | `0.95%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (19.8 bps > 19.5) |
| **SOLUSDT** | $71.43 | ⚪ **CASH** | **-11.1 bps** (±14.1) | `+3.5 bps` | `-0.130 / -0.122` | `1.00%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.2 bps) |

---

### 🕒 Ciclo `2026-11-16 20:31:00 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,175.72 | ⚪ **CASH** | **+6.3 bps** (±22.5) | `+7.9 bps` | `-0.009 / +0.137` | `0.73%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.5 bps > 19.5) |
| **ETHUSDT** | $1,821.96 | ⚪ **CASH** | **+44.3 bps** (±19.8) | `+85.4 bps` | `-0.020 / +0.017` | `0.95%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (19.8 bps > 19.5) |
| **SOLUSDT** | $71.50 | ⚪ **CASH** | **-11.1 bps** (±14.1) | `+3.5 bps` | `-0.130 / -0.122` | `1.00%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.2 bps) |
