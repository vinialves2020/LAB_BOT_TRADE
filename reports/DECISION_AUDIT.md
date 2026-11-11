# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-11 06:15:43 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-11 06:15:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,845.83 | ⚪ **CASH** | **+23.1 bps** (±5.1) | `+36.6 bps` | `+0.026 / +0.037` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,067.67 | ⚪ **CASH** | **-28.0 bps** (±2.9) | `-41.8 bps` | `-0.075 / -0.038` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.15 | ⚪ **CASH** | **+2.5 bps** (±4.6) | `+8.6 bps` | `-0.035 / -0.016` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 06:00:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,926.00 | ⚪ **CASH** | **+23.1 bps** (±5.1) | `+36.6 bps` | `+0.026 / +0.037` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,071.18 | ⚪ **CASH** | **-28.0 bps** (±2.9) | `-41.8 bps` | `-0.075 / -0.038` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.38 | ⚪ **CASH** | **+2.5 bps** (±4.6) | `+8.6 bps` | `-0.035 / -0.016` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 05:45:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,811.43 | ⚪ **CASH** | **+18.9 bps** (±6.1) | `+30.2 bps` | `+0.024 / +0.027` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,067.21 | ⚪ **CASH** | **-27.8 bps** (±6.1) | `-40.0 bps` | `-0.073 / -0.054` | `0.73%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.15 | ⚪ **CASH** | **+4.0 bps** (±7.7) | `+13.2 bps` | `-0.035 / -0.035` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 05:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,790.01 | ⚪ **CASH** | **+18.9 bps** (±6.1) | `+30.2 bps` | `+0.024 / +0.027` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,067.07 | ⚪ **CASH** | **-27.8 bps** (±6.1) | `-40.0 bps` | `-0.073 / -0.054` | `0.73%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.09 | ⚪ **CASH** | **+4.0 bps** (±7.7) | `+13.2 bps` | `-0.035 / -0.035` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 05:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,818.00 | ⚪ **CASH** | **+18.9 bps** (±6.1) | `+30.2 bps` | `+0.024 / +0.027` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,065.91 | ⚪ **CASH** | **-27.8 bps** (±6.1) | `-40.0 bps` | `-0.073 / -0.054` | `0.73%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.90 | ⚪ **CASH** | **+4.0 bps** (±7.7) | `+13.2 bps` | `-0.035 / -0.035` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 05:00:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,724.00 | ⚪ **CASH** | **+18.9 bps** (±6.1) | `+30.2 bps` | `+0.024 / +0.027` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,064.04 | ⚪ **CASH** | **-27.8 bps** (±6.1) | `-40.0 bps` | `-0.073 / -0.054` | `0.73%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.79 | ⚪ **CASH** | **+4.0 bps** (±7.7) | `+13.2 bps` | `-0.035 / -0.035` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 04:45:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,792.02 | ⚪ **CASH** | **+27.6 bps** (±8.5) | `+47.1 bps` | `+0.024 / +0.018` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,068.07 | ⚪ **CASH** | **-25.7 bps** (±7.7) | `-38.4 bps` | `-0.072 / -0.017` | `0.74%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.07 | ⚪ **CASH** | **+4.2 bps** (±4.9) | `+11.9 bps` | `-0.029 / -0.026` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 04:30:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,694.00 | ⚪ **CASH** | **+27.6 bps** (±8.5) | `+47.1 bps` | `+0.024 / +0.018` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,065.45 | ⚪ **CASH** | **-25.7 bps** (±7.7) | `-38.4 bps` | `-0.072 / -0.017` | `0.74%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.05 | ⚪ **CASH** | **+4.2 bps** (±4.9) | `+11.9 bps` | `-0.029 / -0.026` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 04:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,632.01 | ⚪ **CASH** | **+27.6 bps** (±8.5) | `+47.1 bps` | `+0.024 / +0.018` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,061.84 | ⚪ **CASH** | **-25.7 bps** (±7.7) | `-38.4 bps` | `-0.072 / -0.017` | `0.74%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.12 | ⚪ **CASH** | **+4.2 bps** (±4.9) | `+11.9 bps` | `-0.029 / -0.026` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 04:00:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,786.01 | ⚪ **CASH** | **+27.6 bps** (±8.5) | `+47.1 bps` | `+0.024 / +0.018` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,063.27 | ⚪ **CASH** | **-25.7 bps** (±7.7) | `-38.4 bps` | `-0.072 / -0.017` | `0.74%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.35 | ⚪ **CASH** | **+4.2 bps** (±4.9) | `+11.9 bps` | `-0.029 / -0.026` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 03:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,744.01 | ⚪ **CASH** | **+28.6 bps** (±7.5) | `+49.4 bps` | `+0.022 / +0.012` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,062.08 | ⚪ **CASH** | **-29.8 bps** (±4.3) | `-45.6 bps` | `-0.075 / -0.023` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.38 | ⚪ **CASH** | **+3.5 bps** (±5.8) | `+9.2 bps` | `-0.028 / -0.003` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 03:30:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,768.01 | ⚪ **CASH** | **+28.6 bps** (±7.5) | `+49.4 bps` | `+0.022 / +0.012` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,063.09 | ⚪ **CASH** | **-29.8 bps** (±4.3) | `-45.6 bps` | `-0.075 / -0.023` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.60 | ⚪ **CASH** | **+3.5 bps** (±5.8) | `+9.2 bps` | `-0.028 / -0.003` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 03:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,840.01 | ⚪ **CASH** | **+28.6 bps** (±7.5) | `+49.4 bps` | `+0.022 / +0.012` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,066.74 | ⚪ **CASH** | **-29.8 bps** (±4.3) | `-45.6 bps` | `-0.075 / -0.023` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.62 | ⚪ **CASH** | **+3.5 bps** (±5.8) | `+9.2 bps` | `-0.028 / -0.003` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 03:01:00 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,632.01 | ⚪ **CASH** | **+28.6 bps** (±7.5) | `+49.4 bps` | `+0.022 / +0.012` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,058.18 | ⚪ **CASH** | **-29.8 bps** (±4.3) | `-45.6 bps` | `-0.075 / -0.023` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.22 | ⚪ **CASH** | **+3.5 bps** (±5.8) | `+9.2 bps` | `-0.028 / -0.003` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 02:45:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,765.53 | ⚪ **CASH** | **+30.6 bps** (±5.6) | `+50.0 bps` | `+0.024 / +0.046` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,062.39 | ⚪ **CASH** | **-32.1 bps** (±12.4) | `-50.7 bps` | `-0.077 / +0.015` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.58 | ⚪ **CASH** | **+3.0 bps** (±3.2) | `+5.1 bps` | `-0.029 / +0.040` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 02:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,319.76 | ⚪ **CASH** | **+30.6 bps** (±5.6) | `+50.0 bps` | `+0.024 / +0.046` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,051.98 | ⚪ **CASH** | **-32.1 bps** (±12.4) | `-50.7 bps` | `-0.077 / +0.015` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.09 | ⚪ **CASH** | **+3.0 bps** (±3.2) | `+5.1 bps` | `-0.029 / +0.040` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 02:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,411.65 | ⚪ **CASH** | **+30.6 bps** (±5.6) | `+50.0 bps` | `+0.024 / +0.046` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,049.47 | ⚪ **CASH** | **-32.1 bps** (±12.4) | `-50.7 bps` | `-0.077 / +0.015` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.05 | ⚪ **CASH** | **+3.0 bps** (±3.2) | `+5.1 bps` | `-0.029 / +0.040` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 02:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,666.00 | ⚪ **CASH** | **+30.6 bps** (±5.6) | `+50.0 bps` | `+0.024 / +0.046` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,055.84 | ⚪ **CASH** | **-32.1 bps** (±12.4) | `-50.7 bps` | `-0.077 / +0.015` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.32 | ⚪ **CASH** | **+3.0 bps** (±3.2) | `+5.1 bps` | `-0.029 / +0.040` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 01:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,850.11 | ⚪ **CASH** | **+32.3 bps** (±5.9) | `+50.3 bps` | `+0.025 / +0.088` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,061.49 | ⚪ **CASH** | **-23.6 bps** (±9.8) | `-35.9 bps` | `-0.079 / +0.019` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.74 | ⚪ **CASH** | **+6.1 bps** (±11.7) | `+14.2 bps` | `-0.036 / +0.020` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 01:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,802.16 | ⚪ **CASH** | **+32.3 bps** (±5.9) | `+50.3 bps` | `+0.025 / +0.088` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,057.48 | ⚪ **CASH** | **-23.6 bps** (±9.8) | `-35.9 bps` | `-0.079 / +0.019` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.48 | ⚪ **CASH** | **+6.1 bps** (±11.7) | `+14.2 bps` | `-0.036 / +0.020` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 01:15:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,366.27 | ⚪ **CASH** | **+32.3 bps** (±5.9) | `+50.3 bps` | `+0.025 / +0.088` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,044.49 | ⚪ **CASH** | **-23.6 bps** (±9.8) | `-35.9 bps` | `-0.079 / +0.019` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.88 | ⚪ **CASH** | **+6.1 bps** (±11.7) | `+14.2 bps` | `-0.036 / +0.020` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 01:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,553.13 | ⚪ **CASH** | **+32.3 bps** (±5.9) | `+50.3 bps` | `+0.025 / +0.088` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,050.31 | ⚪ **CASH** | **-23.6 bps** (±9.8) | `-35.9 bps` | `-0.079 / +0.019` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.18 | ⚪ **CASH** | **+6.1 bps** (±11.7) | `+14.2 bps` | `-0.036 / +0.020` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 00:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,557.07 | ⚪ **CASH** | **+26.7 bps** (±7.1) | `+40.1 bps` | `+0.029 / +0.083` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,051.28 | ⚪ **CASH** | **-28.8 bps** (±6.7) | `-41.2 bps` | `-0.080 / -0.052` | `0.78%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.32 | ⚪ **CASH** | **+11.1 bps** (±5.1) | `+15.9 bps` | `-0.029 / +0.104` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 00:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,662.82 | ⚪ **CASH** | **+26.7 bps** (±7.1) | `+40.1 bps` | `+0.029 / +0.083` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,051.78 | ⚪ **CASH** | **-28.8 bps** (±6.7) | `-41.2 bps` | `-0.080 / -0.052` | `0.78%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.40 | ⚪ **CASH** | **+11.1 bps** (±5.1) | `+15.9 bps` | `-0.029 / +0.104` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 00:15:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,684.00 | ⚪ **CASH** | **+26.7 bps** (±7.1) | `+40.1 bps` | `+0.029 / +0.083` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,052.13 | ⚪ **CASH** | **-28.8 bps** (±6.7) | `-41.2 bps` | `-0.080 / -0.052` | `0.78%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.43 | ⚪ **CASH** | **+11.1 bps** (±5.1) | `+15.9 bps` | `-0.029 / +0.104` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 00:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,747.99 | ⚪ **CASH** | **+26.7 bps** (±7.1) | `+40.1 bps` | `+0.029 / +0.083` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,051.53 | ⚪ **CASH** | **-28.8 bps** (±6.7) | `-41.2 bps` | `-0.080 / -0.052` | `0.78%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.34 | ⚪ **CASH** | **+11.1 bps** (±5.1) | `+15.9 bps` | `-0.029 / +0.104` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 23:45:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,778.01 | ⚪ **CASH** | **+18.8 bps** (±6.0) | `+23.5 bps` | `+0.037 / +0.096` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,052.59 | ⚪ **CASH** | **-68.1 bps** (±20.5) | `-110.5 bps` | `-0.079 / -0.056` | `0.79%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.38 | ⚪ **CASH** | **+6.4 bps** (±2.5) | `+7.9 bps` | `-0.027 / +0.079` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 23:30:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,694.01 | ⚪ **CASH** | **+18.8 bps** (±6.0) | `+23.5 bps` | `+0.037 / +0.096` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,050.83 | ⚪ **CASH** | **-68.1 bps** (±20.5) | `-110.5 bps` | `-0.079 / -0.056` | `0.79%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.08 | ⚪ **CASH** | **+6.4 bps** (±2.5) | `+7.9 bps` | `-0.027 / +0.079` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 23:15:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,726.01 | ⚪ **CASH** | **+18.8 bps** (±6.0) | `+23.5 bps` | `+0.037 / +0.096` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,050.63 | ⚪ **CASH** | **-68.1 bps** (±20.5) | `-110.5 bps` | `-0.079 / -0.056` | `0.79%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.91 | ⚪ **CASH** | **+6.4 bps** (±2.5) | `+7.9 bps` | `-0.027 / +0.079` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 23:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,615.37 | ⚪ **CASH** | **+18.8 bps** (±6.0) | `+23.5 bps` | `+0.037 / +0.096` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,044.80 | ⚪ **CASH** | **-68.1 bps** (±20.5) | `-110.5 bps` | `-0.079 / -0.056` | `0.79%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.79 | ⚪ **CASH** | **+6.4 bps** (±2.5) | `+7.9 bps` | `-0.027 / +0.079` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 22:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,727.65 | ⚪ **CASH** | **+20.7 bps** (±4.8) | `+28.3 bps` | `+0.042 / +0.060` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,049.90 | ⚪ **CASH** | **-69.2 bps** (±13.4) | `-110.3 bps` | `-0.078 / -0.114` | `0.79%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.04 | ⚪ **CASH** | **+5.9 bps** (±2.6) | `+5.3 bps` | `-0.021 / +0.091` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 22:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,655.00 | ⚪ **CASH** | **+20.7 bps** (±4.8) | `+28.3 bps` | `+0.042 / +0.060` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,051.16 | ⚪ **CASH** | **-69.2 bps** (±13.4) | `-110.3 bps` | `-0.078 / -0.114` | `0.79%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.14 | ⚪ **CASH** | **+5.9 bps** (±2.6) | `+5.3 bps` | `-0.021 / +0.091` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 22:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,919.95 | ⚪ **CASH** | **+20.7 bps** (±4.8) | `+28.3 bps` | `+0.042 / +0.060` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,058.03 | ⚪ **CASH** | **-69.2 bps** (±13.4) | `-110.3 bps` | `-0.078 / -0.114` | `0.79%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.40 | ⚪ **CASH** | **+5.9 bps** (±2.6) | `+5.3 bps` | `-0.021 / +0.091` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 22:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,895.39 | ⚪ **CASH** | **+20.7 bps** (±4.8) | `+28.3 bps` | `+0.042 / +0.060` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,058.18 | ⚪ **CASH** | **-69.2 bps** (±13.4) | `-110.3 bps` | `-0.078 / -0.114` | `0.79%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.40 | ⚪ **CASH** | **+5.9 bps** (±2.6) | `+5.3 bps` | `-0.021 / +0.091` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 21:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,898.90 | ⚪ **CASH** | **+18.4 bps** (±3.8) | `+26.2 bps` | `+0.049 / +0.010` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,059.86 | ⚪ **CASH** | **-64.4 bps** (±15.8) | `-102.2 bps` | `-0.075 / -0.108` | `0.81%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.53 | ⚪ **CASH** | **+6.3 bps** (±1.4) | `+8.6 bps` | `-0.020 / +0.041` | `0.73%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 21:30:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,966.98 | ⚪ **CASH** | **+18.4 bps** (±3.8) | `+26.2 bps` | `+0.049 / +0.010` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,061.11 | ⚪ **CASH** | **-64.4 bps** (±15.8) | `-102.2 bps` | `-0.075 / -0.108` | `0.81%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.48 | ⚪ **CASH** | **+6.3 bps** (±1.4) | `+8.6 bps` | `-0.020 / +0.041` | `0.73%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
