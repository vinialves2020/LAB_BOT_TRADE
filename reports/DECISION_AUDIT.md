# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-12 03:30:53 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-12 03:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,826.01 | ⚪ **CASH** | **+3.2 bps** (±5.1) | `+6.1 bps` | `+0.020 / -0.034` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,055.41 | ⚪ **CASH** | **+40.3 bps** (±9.7) | `+66.9 bps` | `+0.037 / +0.053` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.30 | ⚪ **CASH** | **-14.9 bps** (±5.8) | `-18.6 bps` | `+0.022 / -0.163` | `0.62%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 03:15:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,733.24 | ⚪ **CASH** | **+3.2 bps** (±5.1) | `+6.1 bps` | `+0.020 / -0.034` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,053.48 | ⚪ **CASH** | **+40.3 bps** (±9.7) | `+66.9 bps` | `+0.037 / +0.053` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.22 | ⚪ **CASH** | **-14.9 bps** (±5.8) | `-18.6 bps` | `+0.022 / -0.163` | `0.62%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 03:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,814.46 | ⚪ **CASH** | **+3.2 bps** (±5.1) | `+6.1 bps` | `+0.020 / -0.034` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,058.59 | ⚪ **CASH** | **+40.3 bps** (±9.7) | `+66.9 bps` | `+0.037 / +0.053` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.48 | ⚪ **CASH** | **-14.9 bps** (±5.8) | `-18.6 bps` | `+0.022 / -0.163` | `0.62%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 02:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,843.03 | ⚪ **CASH** | **+2.7 bps** (±4.7) | `+8.3 bps` | `+0.019 / -0.083` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,057.88 | ⚪ **CASH** | **+36.5 bps** (±10.5) | `+61.1 bps` | `+0.035 / +0.043` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.38 | ⚪ **CASH** | **-13.7 bps** (±8.1) | `-17.7 bps` | `+0.028 / -0.144` | `0.62%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 02:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,985.95 | ⚪ **CASH** | **+2.7 bps** (±4.7) | `+8.3 bps` | `+0.019 / -0.083` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,061.13 | ⚪ **CASH** | **+36.5 bps** (±10.5) | `+61.1 bps` | `+0.035 / +0.043` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.55 | ⚪ **CASH** | **-13.7 bps** (±8.1) | `-17.7 bps` | `+0.028 / -0.144` | `0.62%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 02:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,825.09 | ⚪ **CASH** | **+2.7 bps** (±4.7) | `+8.3 bps` | `+0.019 / -0.083` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,057.88 | ⚪ **CASH** | **+36.5 bps** (±10.5) | `+61.1 bps` | `+0.035 / +0.043` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.48 | ⚪ **CASH** | **-13.7 bps** (±8.1) | `-17.7 bps` | `+0.028 / -0.144` | `0.62%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 02:00:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,636.89 | ⚪ **CASH** | **+2.7 bps** (±4.7) | `+8.3 bps` | `+0.019 / -0.083` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,049.11 | ⚪ **CASH** | **+36.5 bps** (±10.5) | `+61.1 bps` | `+0.035 / +0.043` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.04 | ⚪ **CASH** | **-13.7 bps** (±8.1) | `-17.7 bps` | `+0.028 / -0.144` | `0.62%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 01:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,704.70 | ⚪ **CASH** | **+2.4 bps** (±5.8) | `+2.0 bps` | `+0.024 / -0.003` | `0.40%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,052.46 | ⚪ **CASH** | **+45.6 bps** (±9.2) | `+77.5 bps` | `+0.037 / +0.035` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.36 | ⚪ **CASH** | **-13.7 bps** (±2.5) | `-22.8 bps` | `+0.041 / -0.107` | `0.62%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 01:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,654.95 | ⚪ **CASH** | **+2.4 bps** (±5.8) | `+2.0 bps` | `+0.024 / -0.003` | `0.40%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,053.01 | ⚪ **CASH** | **+45.6 bps** (±9.2) | `+77.5 bps` | `+0.037 / +0.035` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.16 | ⚪ **CASH** | **-13.7 bps** (±2.5) | `-22.8 bps` | `+0.041 / -0.107` | `0.62%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 01:15:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,799.02 | ⚪ **CASH** | **+2.4 bps** (±5.8) | `+2.0 bps` | `+0.024 / -0.003` | `0.40%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,053.94 | ⚪ **CASH** | **+45.6 bps** (±9.2) | `+77.5 bps` | `+0.037 / +0.035` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.20 | ⚪ **CASH** | **-13.7 bps** (±2.5) | `-22.8 bps` | `+0.041 / -0.107` | `0.62%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 01:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,032.00 | ⚪ **CASH** | **+2.4 bps** (±5.8) | `+2.0 bps` | `+0.024 / -0.003` | `0.40%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,060.31 | ⚪ **CASH** | **+45.6 bps** (±9.2) | `+77.5 bps` | `+0.037 / +0.035` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.60 | ⚪ **CASH** | **-13.7 bps** (±2.5) | `-22.8 bps` | `+0.041 / -0.107` | `0.62%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 00:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,078.01 | ⚪ **CASH** | **+6.0 bps** (±4.4) | `+8.7 bps` | `+0.022 / -0.003` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,063.05 | ⚪ **CASH** | **+42.5 bps** (±7.7) | `+73.5 bps` | `+0.030 / +0.017` | `0.57%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.73 | ⚪ **CASH** | **-18.1 bps** (±5.4) | `-31.9 bps` | `+0.039 / -0.076` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 00:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,128.69 | ⚪ **CASH** | **+6.0 bps** (±4.4) | `+8.7 bps` | `+0.022 / -0.003` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,063.72 | ⚪ **CASH** | **+42.5 bps** (±7.7) | `+73.5 bps` | `+0.030 / +0.017` | `0.57%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.72 | ⚪ **CASH** | **-18.1 bps** (±5.4) | `-31.9 bps` | `+0.039 / -0.076` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 00:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,919.86 | ⚪ **CASH** | **+6.0 bps** (±4.4) | `+8.7 bps` | `+0.022 / -0.003` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,054.03 | ⚪ **CASH** | **+42.5 bps** (±7.7) | `+73.5 bps` | `+0.030 / +0.017` | `0.57%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.38 | ⚪ **CASH** | **-18.1 bps** (±5.4) | `-31.9 bps` | `+0.039 / -0.076` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 00:00:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,045.98 | ⚪ **CASH** | **+6.0 bps** (±4.4) | `+8.7 bps` | `+0.022 / -0.003` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,056.89 | ⚪ **CASH** | **+42.5 bps** (±7.7) | `+73.5 bps` | `+0.030 / +0.017` | `0.57%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.29 | ⚪ **CASH** | **-18.1 bps** (±5.4) | `-31.9 bps` | `+0.039 / -0.076` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 23:45:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,913.97 | ⚪ **CASH** | **+14.6 bps** (±6.0) | `+22.8 bps` | `+0.024 / +0.021` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,052.41 | ⚪ **CASH** | **+46.1 bps** (±7.3) | `+76.4 bps` | `+0.029 / +0.072` | `0.58%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.05 | ⚪ **CASH** | **+5.8 bps** (±11.5) | `+3.6 bps` | `+0.057 / +0.036` | `0.64%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 23:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,792.12 | ⚪ **CASH** | **+14.6 bps** (±6.0) | `+22.8 bps` | `+0.024 / +0.021` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,048.76 | ⚪ **CASH** | **+46.1 bps** (±7.3) | `+76.4 bps` | `+0.029 / +0.072` | `0.58%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.77 | ⚪ **CASH** | **+5.8 bps** (±11.5) | `+3.6 bps` | `+0.057 / +0.036` | `0.64%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 23:15:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,593.49 | ⚪ **CASH** | **+14.6 bps** (±6.0) | `+22.8 bps` | `+0.024 / +0.021` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,042.02 | ⚪ **CASH** | **+46.1 bps** (±7.3) | `+76.4 bps` | `+0.029 / +0.072` | `0.58%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.55 | ⚪ **CASH** | **+5.8 bps** (±11.5) | `+3.6 bps` | `+0.057 / +0.036` | `0.64%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 23:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,918.08 | ⚪ **CASH** | **+14.6 bps** (±6.0) | `+22.8 bps` | `+0.024 / +0.021` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,056.15 | ⚪ **CASH** | **+46.1 bps** (±7.3) | `+76.4 bps` | `+0.029 / +0.072` | `0.58%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.43 | ⚪ **CASH** | **+5.8 bps** (±11.5) | `+3.6 bps` | `+0.057 / +0.036` | `0.64%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 22:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,109.57 | ⚪ **CASH** | **+13.6 bps** (±4.9) | `+19.4 bps` | `+0.026 / +0.036` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,059.56 | ⚪ **CASH** | **+48.7 bps** (±11.1) | `+79.4 bps` | `+0.030 / +0.104` | `0.58%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.80 | ⚪ **CASH** | **+10.0 bps** (±5.9) | `+6.4 bps` | `+0.064 / +0.081` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 22:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,331.43 | ⚪ **CASH** | **+13.6 bps** (±4.9) | `+19.4 bps` | `+0.026 / +0.036` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,072.78 | ⚪ **CASH** | **+48.7 bps** (±11.1) | `+79.4 bps` | `+0.030 / +0.104` | `0.58%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $84.44 | ⚪ **CASH** | **+10.0 bps** (±5.9) | `+6.4 bps` | `+0.064 / +0.081` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 22:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,466.01 | ⚪ **CASH** | **+13.6 bps** (±4.9) | `+19.4 bps` | `+0.026 / +0.036` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,073.49 | ⚪ **CASH** | **+48.7 bps** (±11.1) | `+79.4 bps` | `+0.030 / +0.104` | `0.58%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $84.69 | ⚪ **CASH** | **+10.0 bps** (±5.9) | `+6.4 bps` | `+0.064 / +0.081` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 22:00:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,385.35 | ⚪ **CASH** | **+13.6 bps** (±4.9) | `+19.4 bps` | `+0.026 / +0.036` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,070.99 | ⚪ **CASH** | **+48.7 bps** (±11.1) | `+79.4 bps` | `+0.030 / +0.104` | `0.58%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $84.59 | ⚪ **CASH** | **+10.0 bps** (±5.9) | `+6.4 bps` | `+0.064 / +0.081` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 21:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,500.12 | ⚪ **CASH** | **+8.7 bps** (±4.0) | `+8.3 bps` | `+0.027 / +0.066` | `0.43%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,075.53 | ⚪ **CASH** | **+60.4 bps** (±13.0) | `+100.6 bps` | `+0.020 / +0.128` | `0.65%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $84.73 | ⚪ **CASH** | **+31.5 bps** (±16.3) | `+42.2 bps` | `+0.076 / +0.140` | `0.65%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 21:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,734.07 | ⚪ **CASH** | **+8.7 bps** (±4.0) | `+8.3 bps` | `+0.027 / +0.066` | `0.43%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,081.46 | ⚪ **CASH** | **+60.4 bps** (±13.0) | `+100.6 bps` | `+0.020 / +0.128` | `0.65%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $85.01 | ⚪ **CASH** | **+31.5 bps** (±16.3) | `+42.2 bps` | `+0.076 / +0.140` | `0.65%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 21:15:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,676.00 | ⚪ **CASH** | **+8.7 bps** (±4.0) | `+8.3 bps` | `+0.027 / +0.066` | `0.43%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,079.93 | ⚪ **CASH** | **+60.4 bps** (±13.0) | `+100.6 bps` | `+0.020 / +0.128` | `0.65%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $84.95 | ⚪ **CASH** | **+31.5 bps** (±16.3) | `+42.2 bps` | `+0.076 / +0.140` | `0.65%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 21:01:04 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,648.01 | ⚪ **CASH** | **+8.7 bps** (±4.0) | `+8.3 bps` | `+0.027 / +0.066` | `0.43%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,081.41 | ⚪ **CASH** | **+60.4 bps** (±13.0) | `+100.6 bps` | `+0.020 / +0.128` | `0.65%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $84.96 | ⚪ **CASH** | **+31.5 bps** (±16.3) | `+42.2 bps` | `+0.076 / +0.140` | `0.65%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 20:15:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,594.18 | ⚪ **CASH** | **+5.2 bps** (±2.1) | `-1.2 bps` | `+0.045 / +0.065` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,082.93 | ⚪ **CASH** | **+53.1 bps** (±16.9) | `+86.9 bps` | `+0.028 / +0.116` | `0.66%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $85.06 | ⚪ **CASH** | **+21.2 bps** (±7.5) | `+20.4 bps` | `+0.084 / +0.137` | `0.66%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 20:01:02 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,402.03 | ⚪ **CASH** | **+5.2 bps** (±2.1) | `-1.2 bps` | `+0.045 / +0.065` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,078.31 | ⚪ **CASH** | **+53.1 bps** (±16.9) | `+86.9 bps` | `+0.028 / +0.116` | `0.66%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $84.87 | ⚪ **CASH** | **+21.2 bps** (±7.5) | `+20.4 bps` | `+0.084 / +0.137` | `0.66%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 19:45:35 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,435.00 | ⚪ **CASH** | **+6.0 bps** (±6.1) | `+3.6 bps` | `+0.045 / +0.028` | `0.44%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,078.94 | ⚪ **CASH** | **+53.6 bps** (±14.5) | `+86.0 bps` | `+0.034 / +0.131` | `0.67%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $84.66 | ⚪ **CASH** | **+22.2 bps** (±8.6) | `+22.7 bps` | `+0.084 / +0.132` | `0.67%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 19:30:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,400.00 | ⚪ **CASH** | **+6.0 bps** (±6.1) | `+3.6 bps` | `+0.045 / +0.028` | `0.44%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,081.04 | ⚪ **CASH** | **+53.6 bps** (±14.5) | `+86.0 bps` | `+0.034 / +0.131` | `0.67%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $84.84 | ⚪ **CASH** | **+22.2 bps** (±8.6) | `+22.7 bps` | `+0.084 / +0.132` | `0.67%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 19:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,223.62 | ⚪ **CASH** | **+6.0 bps** (±6.1) | `+3.6 bps` | `+0.045 / +0.028` | `0.44%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,073.44 | ⚪ **CASH** | **+53.6 bps** (±14.5) | `+86.0 bps` | `+0.034 / +0.131` | `0.67%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $84.55 | ⚪ **CASH** | **+22.2 bps** (±8.6) | `+22.7 bps` | `+0.084 / +0.132` | `0.67%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 19:01:02 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,454.01 | ⚪ **CASH** | **+6.0 bps** (±6.1) | `+3.6 bps` | `+0.045 / +0.028` | `0.44%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,082.26 | ⚪ **CASH** | **+53.6 bps** (±14.5) | `+86.0 bps` | `+0.034 / +0.131` | `0.67%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $84.95 | ⚪ **CASH** | **+22.2 bps** (±8.6) | `+22.7 bps` | `+0.084 / +0.132` | `0.67%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 18:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,506.00 | ⚪ **CASH** | **+5.9 bps** (±6.1) | `+5.6 bps` | `+0.040 / +0.004` | `0.44%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,086.55 | ⚪ **CASH** | **+42.8 bps** (±15.2) | `+69.5 bps` | `+0.012 / +0.121` | `0.67%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $85.18 | ⚪ **CASH** | **+18.9 bps** (±10.6) | `+18.0 bps` | `+0.088 / +0.119` | `0.68%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 18:30:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,510.01 | ⚪ **CASH** | **+5.9 bps** (±6.1) | `+5.6 bps` | `+0.040 / +0.004` | `0.44%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,089.54 | ⚪ **CASH** | **+42.8 bps** (±15.2) | `+69.5 bps` | `+0.012 / +0.121` | `0.67%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $85.22 | ⚪ **CASH** | **+18.9 bps** (±10.6) | `+18.0 bps` | `+0.088 / +0.119` | `0.68%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 18:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,454.00 | ⚪ **CASH** | **+5.9 bps** (±6.1) | `+5.6 bps` | `+0.040 / +0.004` | `0.44%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,088.57 | ⚪ **CASH** | **+42.8 bps** (±15.2) | `+69.5 bps` | `+0.012 / +0.121` | `0.67%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $85.22 | ⚪ **CASH** | **+18.9 bps** (±10.6) | `+18.0 bps` | `+0.088 / +0.119` | `0.68%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
