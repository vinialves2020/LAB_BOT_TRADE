# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-06 07:15:39 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-06 07:15:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,446.48 | ⚪ **CASH** | **-1.3 bps** (±29.0) | `+17.2 bps` | `-0.088 / -0.019` | `0.62%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,223.31 | ⚪ **CASH** | **-49.6 bps** (±31.9) | `-67.3 bps` | `-0.115 / -0.023` | `0.83%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.54 | ⚪ **CASH** | **-58.7 bps** (±37.3) | `-91.2 bps` | `-0.030 / -0.024` | `0.83%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 07:00:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,705.03 | ⚪ **CASH** | **-1.3 bps** (±29.0) | `+17.2 bps` | `-0.088 / -0.019` | `0.62%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,227.81 | ⚪ **CASH** | **-49.6 bps** (±31.9) | `-67.3 bps` | `-0.115 / -0.023` | `0.83%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.62 | ⚪ **CASH** | **-58.7 bps** (±37.3) | `-91.2 bps` | `-0.030 / -0.024` | `0.83%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 06:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,721.00 | ⚪ **CASH** | **+9.4 bps** (±16.7) | `+36.2 bps` | `-0.092 / -0.040` | `0.62%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,231.06 | ⚪ **CASH** | **-46.3 bps** (±31.8) | `-62.7 bps` | `-0.119 / +0.007` | `0.84%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.83 | ⚪ **CASH** | **-53.7 bps** (±34.5) | `-83.6 bps` | `-0.028 / -0.008` | `0.84%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 06:30:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,677.26 | ⚪ **CASH** | **+9.4 bps** (±16.7) | `+36.2 bps` | `-0.092 / -0.040` | `0.62%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,228.44 | ⚪ **CASH** | **-46.3 bps** (±31.8) | `-62.7 bps` | `-0.119 / +0.007` | `0.84%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.82 | ⚪ **CASH** | **-53.7 bps** (±34.5) | `-83.6 bps` | `-0.028 / -0.008` | `0.84%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 06:15:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,520.71 | ⚪ **CASH** | **+9.4 bps** (±16.7) | `+36.2 bps` | `-0.092 / -0.040` | `0.62%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,218.76 | ⚪ **CASH** | **-46.3 bps** (±31.8) | `-62.7 bps` | `-0.119 / +0.007` | `0.84%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.26 | ⚪ **CASH** | **-53.7 bps** (±34.5) | `-83.6 bps` | `-0.028 / -0.008` | `0.84%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 06:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,645.07 | ⚪ **CASH** | **+9.4 bps** (±16.7) | `+36.2 bps` | `-0.092 / -0.040` | `0.62%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,224.01 | ⚪ **CASH** | **-46.3 bps** (±31.8) | `-62.7 bps` | `-0.119 / +0.007` | `0.84%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.40 | ⚪ **CASH** | **-53.7 bps** (±34.5) | `-83.6 bps` | `-0.028 / -0.008` | `0.84%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 05:45:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,706.00 | ⚪ **CASH** | **+9.6 bps** (±18.8) | `+39.0 bps` | `-0.094 / -0.065` | `0.63%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,225.32 | ⚪ **CASH** | **-45.8 bps** (±32.7) | `-56.7 bps` | `-0.123 / -0.061` | `0.85%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.43 | ⚪ **CASH** | **-56.9 bps** (±30.2) | `-90.0 bps` | `-0.032 / -0.002` | `0.85%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 05:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,409.00 | ⚪ **CASH** | **+9.6 bps** (±18.8) | `+39.0 bps` | `-0.094 / -0.065` | `0.63%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,217.93 | ⚪ **CASH** | **-45.8 bps** (±32.7) | `-56.7 bps` | `-0.123 / -0.061` | `0.85%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.08 | ⚪ **CASH** | **-56.9 bps** (±30.2) | `-90.0 bps` | `-0.032 / -0.002` | `0.85%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 05:15:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,578.26 | ⚪ **CASH** | **+9.6 bps** (±18.8) | `+39.0 bps` | `-0.094 / -0.065` | `0.63%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,223.65 | ⚪ **CASH** | **-45.8 bps** (±32.7) | `-56.7 bps` | `-0.123 / -0.061` | `0.85%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.19 | ⚪ **CASH** | **-56.9 bps** (±30.2) | `-90.0 bps` | `-0.032 / -0.002` | `0.85%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 05:00:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,784.67 | ⚪ **CASH** | **+9.6 bps** (±18.8) | `+39.0 bps` | `-0.094 / -0.065` | `0.63%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,233.47 | ⚪ **CASH** | **-45.8 bps** (±32.7) | `-56.7 bps` | `-0.123 / -0.061` | `0.85%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.53 | ⚪ **CASH** | **-56.9 bps** (±30.2) | `-90.0 bps` | `-0.032 / -0.002` | `0.85%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 04:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,756.00 | ⚪ **CASH** | **+0.8 bps** (±23.9) | `+21.3 bps` | `-0.094 / -0.026` | `0.64%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,232.77 | ⚪ **CASH** | **-45.1 bps** (±31.2) | `-54.8 bps` | `-0.123 / -0.074` | `0.86%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.48 | ⚪ **CASH** | **-48.2 bps** (±30.2) | `-75.0 bps` | `-0.030 / +0.004` | `0.86%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 04:30:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,650.83 | ⚪ **CASH** | **+0.8 bps** (±23.9) | `+21.3 bps` | `-0.094 / -0.026` | `0.64%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,229.57 | ⚪ **CASH** | **-45.1 bps** (±31.2) | `-54.8 bps` | `-0.123 / -0.074` | `0.86%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.34 | ⚪ **CASH** | **-48.2 bps** (±30.2) | `-75.0 bps` | `-0.030 / +0.004` | `0.86%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 04:15:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,708.66 | ⚪ **CASH** | **+0.8 bps** (±23.9) | `+21.3 bps` | `-0.094 / -0.026` | `0.64%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,233.43 | ⚪ **CASH** | **-45.1 bps** (±31.2) | `-54.8 bps` | `-0.123 / -0.074` | `0.86%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.48 | ⚪ **CASH** | **-48.2 bps** (±30.2) | `-75.0 bps` | `-0.030 / +0.004` | `0.86%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 04:00:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,887.58 | ⚪ **CASH** | **+0.8 bps** (±23.9) | `+21.3 bps` | `-0.094 / -0.026` | `0.64%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.79 | ⚪ **CASH** | **-45.1 bps** (±31.2) | `-54.8 bps` | `-0.123 / -0.074` | `0.86%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.73 | ⚪ **CASH** | **-48.2 bps** (±30.2) | `-75.0 bps` | `-0.030 / +0.004` | `0.86%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 03:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,952.96 | ⚪ **CASH** | **-1.4 bps** (±26.9) | `+20.5 bps` | `-0.099 / -0.054` | `0.65%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.39 | ⚪ **CASH** | **-38.5 bps** (±17.7) | `-42.0 bps` | `-0.123 / -0.119` | `0.87%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.91 | ⚪ **CASH** | **-33.1 bps** (±15.0) | `-50.2 bps` | `-0.027 / +0.004` | `0.87%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 03:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,970.01 | ⚪ **CASH** | **-1.4 bps** (±26.9) | `+20.5 bps` | `-0.099 / -0.054` | `0.65%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.19 | ⚪ **CASH** | **-38.5 bps** (±17.7) | `-42.0 bps` | `-0.123 / -0.119` | `0.87%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.02 | ⚪ **CASH** | **-33.1 bps** (±15.0) | `-50.2 bps` | `-0.027 / +0.004` | `0.87%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 03:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,123.01 | ⚪ **CASH** | **-1.4 bps** (±26.9) | `+20.5 bps` | `-0.099 / -0.054` | `0.65%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,240.44 | ⚪ **CASH** | **-38.5 bps** (±17.7) | `-42.0 bps` | `-0.123 / -0.119` | `0.87%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.19 | ⚪ **CASH** | **-33.1 bps** (±15.0) | `-50.2 bps` | `-0.027 / +0.004` | `0.87%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 03:00:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,168.01 | ⚪ **CASH** | **-1.4 bps** (±26.9) | `+20.5 bps` | `-0.099 / -0.054` | `0.65%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,242.15 | ⚪ **CASH** | **-38.5 bps** (±17.7) | `-42.0 bps` | `-0.123 / -0.119` | `0.87%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.32 | ⚪ **CASH** | **-33.1 bps** (±15.0) | `-50.2 bps` | `-0.027 / +0.004` | `0.87%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 02:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,158.77 | ⚪ **CASH** | **+8.3 bps** (±17.6) | `+36.0 bps` | `-0.104 / -0.037` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,242.42 | ⚪ **CASH** | **-19.7 bps** (±21.2) | `-7.2 bps` | `-0.124 / -0.116` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.33 | ⚪ **CASH** | **-28.0 bps** (±21.0) | `-41.3 bps` | `-0.023 / +0.024` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 02:30:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,180.01 | ⚪ **CASH** | **+8.3 bps** (±17.6) | `+36.0 bps` | `-0.104 / -0.037` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,242.15 | ⚪ **CASH** | **-19.7 bps** (±21.2) | `-7.2 bps` | `-0.124 / -0.116` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.22 | ⚪ **CASH** | **-28.0 bps** (±21.0) | `-41.3 bps` | `-0.023 / +0.024` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 02:15:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,108.34 | ⚪ **CASH** | **+8.3 bps** (±17.6) | `+36.0 bps` | `-0.104 / -0.037` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,239.30 | ⚪ **CASH** | **-19.7 bps** (±21.2) | `-7.2 bps` | `-0.124 / -0.116` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.03 | ⚪ **CASH** | **-28.0 bps** (±21.0) | `-41.3 bps` | `-0.023 / +0.024` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 02:00:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,162.01 | ⚪ **CASH** | **+8.3 bps** (±17.6) | `+36.0 bps` | `-0.104 / -0.037` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,242.08 | ⚪ **CASH** | **-19.7 bps** (±21.2) | `-7.2 bps` | `-0.124 / -0.116` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.25 | ⚪ **CASH** | **-28.0 bps** (±21.0) | `-41.3 bps` | `-0.023 / +0.024` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 01:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,152.00 | ⚪ **CASH** | **-8.6 bps** (±19.2) | `+3.1 bps` | `-0.102 / -0.003` | `0.67%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,240.03 | ⚪ **CASH** | **-28.0 bps** (±12.6) | `-24.6 bps` | `-0.126 / -0.101` | `0.89%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.13 | ⚪ **CASH** | **-35.1 bps** (±21.9) | `-52.6 bps` | `-0.031 / +0.012` | `0.89%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 01:30:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,086.00 | ⚪ **CASH** | **-8.6 bps** (±19.2) | `+3.1 bps` | `-0.102 / -0.003` | `0.67%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.54 | ⚪ **CASH** | **-28.0 bps** (±12.6) | `-24.6 bps` | `-0.126 / -0.101` | `0.89%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.88 | ⚪ **CASH** | **-35.1 bps** (±21.9) | `-52.6 bps` | `-0.031 / +0.012` | `0.89%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 01:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,252.65 | ⚪ **CASH** | **-8.6 bps** (±19.2) | `+3.1 bps` | `-0.102 / -0.003` | `0.67%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,243.71 | ⚪ **CASH** | **-28.0 bps** (±12.6) | `-24.6 bps` | `-0.126 / -0.101` | `0.89%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.39 | ⚪ **CASH** | **-35.1 bps** (±21.9) | `-52.6 bps` | `-0.031 / +0.012` | `0.89%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 01:00:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,285.54 | ⚪ **CASH** | **-8.6 bps** (±19.2) | `+3.1 bps` | `-0.102 / -0.003` | `0.67%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,244.51 | ⚪ **CASH** | **-28.0 bps** (±12.6) | `-24.6 bps` | `-0.126 / -0.101` | `0.89%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.23 | ⚪ **CASH** | **-35.1 bps** (±21.9) | `-52.6 bps` | `-0.031 / +0.012` | `0.89%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 00:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,362.53 | ⚪ **CASH** | **+12.1 bps** (±19.6) | `+40.7 bps` | `-0.106 / +0.006` | `0.67%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,248.10 | ⚪ **CASH** | **-12.3 bps** (±21.5) | `+8.3 bps` | `-0.136 / -0.126` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.45 | ⚪ **CASH** | **-33.2 bps** (±31.4) | `-49.6 bps` | `-0.028 / +0.044` | `0.87%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 00:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,225.01 | ⚪ **CASH** | **+12.1 bps** (±19.6) | `+40.7 bps` | `-0.106 / +0.006` | `0.67%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,242.87 | ⚪ **CASH** | **-12.3 bps** (±21.5) | `+8.3 bps` | `-0.136 / -0.126` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.02 | ⚪ **CASH** | **-33.2 bps** (±31.4) | `-49.6 bps` | `-0.028 / +0.044` | `0.87%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 00:15:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,188.00 | ⚪ **CASH** | **+12.1 bps** (±19.6) | `+40.7 bps` | `-0.106 / +0.006` | `0.67%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,239.51 | ⚪ **CASH** | **-12.3 bps** (±21.5) | `+8.3 bps` | `-0.136 / -0.126` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.84 | ⚪ **CASH** | **-33.2 bps** (±31.4) | `-49.6 bps` | `-0.028 / +0.044` | `0.87%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 00:00:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,072.85 | ⚪ **CASH** | **+12.1 bps** (±19.6) | `+40.7 bps` | `-0.106 / +0.006` | `0.67%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.43 | ⚪ **CASH** | **-12.3 bps** (±21.5) | `+8.3 bps` | `-0.136 / -0.126` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.38 | ⚪ **CASH** | **-33.2 bps** (±31.4) | `-49.6 bps` | `-0.028 / +0.044` | `0.87%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 23:45:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,074.22 | ⚪ **CASH** | **+25.7 bps** (±24.9) | `+63.6 bps` | `-0.105 / +0.047` | `0.67%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,239.25 | ⚪ **CASH** | **-24.1 bps** (±29.9) | `-14.4 bps` | `-0.136 / -0.084` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.36 | ⚪ **CASH** | **-26.9 bps** (±24.9) | `-37.4 bps` | `-0.026 / +0.010` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 23:30:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,852.00 | ⚪ **CASH** | **+25.7 bps** (±24.9) | `+63.6 bps` | `-0.105 / +0.047` | `0.67%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,230.87 | ⚪ **CASH** | **-24.1 bps** (±29.9) | `-14.4 bps` | `-0.136 / -0.084` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.06 | ⚪ **CASH** | **-26.9 bps** (±24.9) | `-37.4 bps` | `-0.026 / +0.010` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 23:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,423.06 | ⚪ **CASH** | **+25.7 bps** (±24.9) | `+63.6 bps` | `-0.105 / +0.047` | `0.67%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,216.79 | ⚪ **CASH** | **-24.1 bps** (±29.9) | `-14.4 bps` | `-0.136 / -0.084` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $88.76 | ⚪ **CASH** | **-26.9 bps** (±24.9) | `-37.4 bps` | `-0.026 / +0.010` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 23:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,650.01 | ⚪ **CASH** | **+25.7 bps** (±24.9) | `+63.6 bps` | `-0.105 / +0.047` | `0.67%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,228.67 | ⚪ **CASH** | **-24.1 bps** (±29.9) | `-14.4 bps` | `-0.136 / -0.084` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.61 | ⚪ **CASH** | **-26.9 bps** (±24.9) | `-37.4 bps` | `-0.026 / +0.010` | `0.88%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 22:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,822.38 | ⚪ **CASH** | **+14.4 bps** (±22.0) | `+41.9 bps` | `-0.107 / +0.062` | `0.68%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,233.38 | ⚪ **CASH** | **-20.1 bps** (±19.6) | `-12.4 bps` | `-0.130 / -0.039` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.74 | ⚪ **CASH** | **-26.0 bps** (±32.3) | `-36.1 bps` | `-0.016 / +0.024` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 22:30:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,017.19 | ⚪ **CASH** | **+14.4 bps** (±22.0) | `+41.9 bps` | `-0.107 / +0.062` | `0.68%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,237.95 | ⚪ **CASH** | **-20.1 bps** (±19.6) | `-12.4 bps` | `-0.130 / -0.039` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.02 | ⚪ **CASH** | **-26.0 bps** (±32.3) | `-36.1 bps` | `-0.016 / +0.024` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
