# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-19 00:00:58 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-19 00:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,954.42 | ⚪ **CASH** | **+35.1 bps** (±20.0) | `+65.3 bps` | `+0.007 / +0.018` | `0.53%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.0 bps > 19.5) |
| **ETHUSDT** | $1,775.32 | ⚪ **CASH** | **+33.9 bps** (±13.7) | `+68.2 bps` | `-0.034 / -0.017` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.54 | ⚪ **CASH** | **+12.5 bps** (±9.4) | `+24.8 bps` | `-0.006 / -0.001` | `0.73%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 23:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,070.43 | ⚪ **CASH** | **+39.0 bps** (±14.3) | `+65.8 bps` | `+0.016 / +0.084` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,780.75 | ⚪ **CASH** | **+62.5 bps** (±9.0) | `+118.8 bps` | `-0.041 / -0.005` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $73.74 | ⚪ **CASH** | **+21.4 bps** (±10.7) | `+40.9 bps` | `-0.017 / +0.012` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 23:30:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,795.26 | ⚪ **CASH** | **+39.0 bps** (±14.3) | `+65.8 bps` | `+0.016 / +0.084` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,772.69 | ⚪ **CASH** | **+62.5 bps** (±9.0) | `+118.8 bps` | `-0.041 / -0.005` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $73.42 | ⚪ **CASH** | **+21.4 bps** (±10.7) | `+40.9 bps` | `-0.017 / +0.012` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 23:15:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,598.65 | ⚪ **CASH** | **+39.0 bps** (±14.3) | `+65.8 bps` | `+0.016 / +0.084` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,768.35 | ⚪ **CASH** | **+62.5 bps** (±9.0) | `+118.8 bps` | `-0.041 / -0.005` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $73.19 | ⚪ **CASH** | **+21.4 bps** (±10.7) | `+40.9 bps` | `-0.017 / +0.012` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 23:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,319.38 | ⚪ **CASH** | **+39.0 bps** (±14.3) | `+65.8 bps` | `+0.016 / +0.084` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,759.51 | ⚪ **CASH** | **+62.5 bps** (±9.0) | `+118.8 bps` | `-0.041 / -0.005` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.68 | ⚪ **CASH** | **+21.4 bps** (±10.7) | `+40.9 bps` | `-0.017 / +0.012` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 22:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,510.01 | ⚪ **CASH** | **+37.2 bps** (±17.2) | `+64.3 bps` | `+0.033 / +0.024` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,765.47 | ⚪ **CASH** | **+57.1 bps** (±8.2) | `+108.0 bps` | `-0.039 / -0.009` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.90 | ⚪ **CASH** | **+25.8 bps** (±9.3) | `+45.5 bps` | `-0.009 / +0.038` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.8 bps) |

---

### 🕒 Ciclo `2026-11-18 22:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,568.35 | ⚪ **CASH** | **+37.2 bps** (±17.2) | `+64.3 bps` | `+0.033 / +0.024` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,765.02 | ⚪ **CASH** | **+57.1 bps** (±8.2) | `+108.0 bps` | `-0.039 / -0.009` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.96 | ⚪ **CASH** | **+25.8 bps** (±9.3) | `+45.5 bps` | `-0.009 / +0.038` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.8 bps) |

---

### 🕒 Ciclo `2026-11-18 22:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,421.87 | ⚪ **CASH** | **+37.2 bps** (±17.2) | `+64.3 bps` | `+0.033 / +0.024` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,765.35 | ⚪ **CASH** | **+57.1 bps** (±8.2) | `+108.0 bps` | `-0.039 / -0.009` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.88 | ⚪ **CASH** | **+25.8 bps** (±9.3) | `+45.5 bps` | `-0.009 / +0.038` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.8 bps) |

---

### 🕒 Ciclo `2026-11-18 22:00:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,377.00 | ⚪ **CASH** | **+37.2 bps** (±17.2) | `+64.3 bps` | `+0.033 / +0.024` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,764.94 | ⚪ **CASH** | **+57.1 bps** (±8.2) | `+108.0 bps` | `-0.039 / -0.009` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $73.02 | ⚪ **CASH** | **+25.8 bps** (±9.3) | `+45.5 bps` | `-0.009 / +0.038` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.8 bps) |

---

### 🕒 Ciclo `2026-11-18 21:45:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,365.16 | ⚪ **CASH** | **+33.3 bps** (±13.8) | `+59.9 bps` | `+0.029 / -0.018` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,764.68 | ⚪ **CASH** | **+39.6 bps** (±8.1) | `+75.8 bps` | `-0.033 / -0.006` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $73.00 | ⚪ **CASH** | **+23.8 bps** (±10.2) | `+42.7 bps` | `-0.004 / +0.023` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-18 21:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,432.53 | ⚪ **CASH** | **+33.3 bps** (±13.8) | `+59.9 bps` | `+0.029 / -0.018` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,761.94 | ⚪ **CASH** | **+39.6 bps** (±8.1) | `+75.8 bps` | `-0.033 / -0.006` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $73.08 | ⚪ **CASH** | **+23.8 bps** (±10.2) | `+42.7 bps` | `-0.004 / +0.023` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-18 21:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,477.10 | ⚪ **CASH** | **+33.3 bps** (±13.8) | `+59.9 bps` | `+0.029 / -0.018` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,755.61 | ⚪ **CASH** | **+39.6 bps** (±8.1) | `+75.8 bps` | `-0.033 / -0.006` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $73.06 | ⚪ **CASH** | **+23.8 bps** (±10.2) | `+42.7 bps` | `-0.004 / +0.023` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-18 21:00:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,648.00 | ⚪ **CASH** | **+33.3 bps** (±13.8) | `+59.9 bps` | `+0.029 / -0.018` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,755.24 | ⚪ **CASH** | **+39.6 bps** (±8.1) | `+75.8 bps` | `-0.033 / -0.006` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $73.13 | ⚪ **CASH** | **+23.8 bps** (±10.2) | `+42.7 bps` | `-0.004 / +0.023` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-18 20:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,504.00 | ⚪ **CASH** | **+34.5 bps** (±8.0) | `+59.1 bps` | `+0.034 / +0.002` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,748.71 | ⚪ **CASH** | **+38.7 bps** (±7.4) | `+73.7 bps` | `-0.035 / -0.003` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.92 | ⚪ **CASH** | **+19.0 bps** (±11.2) | `+36.2 bps` | `-0.018 / +0.007` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-18 20:30:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,588.01 | ⚪ **CASH** | **+34.5 bps** (±8.0) | `+59.1 bps` | `+0.034 / +0.002` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,750.32 | ⚪ **CASH** | **+38.7 bps** (±7.4) | `+73.7 bps` | `-0.035 / -0.003` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.87 | ⚪ **CASH** | **+19.0 bps** (±11.2) | `+36.2 bps` | `-0.018 / +0.007` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-18 20:15:33 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,796.00 | ⚪ **CASH** | **+34.5 bps** (±8.0) | `+59.1 bps` | `+0.034 / +0.002` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,756.87 | ⚪ **CASH** | **+38.7 bps** (±7.4) | `+73.7 bps` | `-0.035 / -0.003` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $73.18 | ⚪ **CASH** | **+19.0 bps** (±11.2) | `+36.2 bps` | `-0.018 / +0.007` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-18 20:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,756.00 | ⚪ **CASH** | **+34.5 bps** (±8.0) | `+59.1 bps` | `+0.034 / +0.002` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,755.96 | ⚪ **CASH** | **+38.7 bps** (±7.4) | `+73.7 bps` | `-0.035 / -0.003` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $73.15 | ⚪ **CASH** | **+19.0 bps** (±11.2) | `+36.2 bps` | `-0.018 / +0.007` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-18 19:45:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,662.39 | ⚪ **CASH** | **+31.6 bps** (±16.5) | `+53.6 bps` | `+0.040 / +0.015` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,756.96 | ⚪ **CASH** | **+47.2 bps** (±10.9) | `+89.1 bps` | `-0.032 / -0.002` | `0.63%/h` | `weak_order_flow` | Filtro: confluência Dual-Setup (A/B) e absorção CVD insuficiente |
| **SOLUSDT** | $73.16 | ⚪ **CASH** | **+19.7 bps** (±7.8) | `+35.6 bps` | `-0.014 / +0.014` | `0.70%/h` | `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 19:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,867.41 | ⚪ **CASH** | **+31.6 bps** (±16.5) | `+53.6 bps` | `+0.040 / +0.015` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,762.06 | ⚪ **CASH** | **+47.2 bps** (±10.9) | `+89.1 bps` | `-0.032 / -0.002` | `0.63%/h` | `weak_order_flow` | Filtro: confluência Dual-Setup (A/B) e absorção CVD insuficiente |
| **SOLUSDT** | $73.44 | ⚪ **CASH** | **+19.7 bps** (±7.8) | `+35.6 bps` | `-0.014 / +0.014` | `0.70%/h` | `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 19:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,876.01 | ⚪ **CASH** | **+31.6 bps** (±16.5) | `+53.6 bps` | `+0.040 / +0.015` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,762.09 | ⚪ **CASH** | **+47.2 bps** (±10.9) | `+89.1 bps` | `-0.032 / -0.002` | `0.63%/h` | `weak_order_flow` | Filtro: confluência Dual-Setup (A/B) e absorção CVD insuficiente |
| **SOLUSDT** | $73.52 | ⚪ **CASH** | **+19.7 bps** (±7.8) | `+35.6 bps` | `-0.014 / +0.014` | `0.70%/h` | `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 19:00:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,046.01 | ⚪ **CASH** | **+31.6 bps** (±16.5) | `+53.6 bps` | `+0.040 / +0.015` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,764.06 | ⚪ **CASH** | **+47.2 bps** (±10.9) | `+89.1 bps` | `-0.032 / -0.002` | `0.63%/h` | `weak_order_flow` | Filtro: confluência Dual-Setup (A/B) e absorção CVD insuficiente |
| **SOLUSDT** | $73.68 | ⚪ **CASH** | **+19.7 bps** (±7.8) | `+35.6 bps` | `-0.014 / +0.014` | `0.70%/h` | `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 18:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,232.04 | ⚪ **CASH** | **+33.9 bps** (±16.7) | `+59.1 bps` | `+0.034 / +0.008` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,772.95 | ⚪ **CASH** | **+59.6 bps** (±14.0) | `+112.9 bps` | `-0.031 / -0.008` | `0.64%/h` | `weak_order_flow` | Filtro: confluência Dual-Setup (A/B) e absorção CVD insuficiente |
| **SOLUSDT** | $73.99 | ⚪ **CASH** | **+28.9 bps** (±13.2) | `+54.6 bps` | `-0.017 / +0.006` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 18:30:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,179.81 | ⚪ **CASH** | **+33.9 bps** (±16.7) | `+59.1 bps` | `+0.034 / +0.008` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,769.12 | ⚪ **CASH** | **+59.6 bps** (±14.0) | `+112.9 bps` | `-0.031 / -0.008` | `0.64%/h` | `weak_order_flow` | Filtro: confluência Dual-Setup (A/B) e absorção CVD insuficiente |
| **SOLUSDT** | $73.75 | ⚪ **CASH** | **+28.9 bps** (±13.2) | `+54.6 bps` | `-0.017 / +0.006` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 18:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,248.03 | ⚪ **CASH** | **+33.9 bps** (±16.7) | `+59.1 bps` | `+0.034 / +0.008` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,770.58 | ⚪ **CASH** | **+59.6 bps** (±14.0) | `+112.9 bps` | `-0.031 / -0.008` | `0.64%/h` | `weak_order_flow` | Filtro: confluência Dual-Setup (A/B) e absorção CVD insuficiente |
| **SOLUSDT** | $73.77 | ⚪ **CASH** | **+28.9 bps** (±13.2) | `+54.6 bps` | `-0.017 / +0.006` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 18:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,104.00 | ⚪ **CASH** | **+33.9 bps** (±16.7) | `+59.1 bps` | `+0.034 / +0.008` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,768.21 | ⚪ **CASH** | **+59.6 bps** (±14.0) | `+112.9 bps` | `-0.031 / -0.008` | `0.64%/h` | `weak_order_flow` | Filtro: confluência Dual-Setup (A/B) e absorção CVD insuficiente |
| **SOLUSDT** | $73.62 | ⚪ **CASH** | **+28.9 bps** (±13.2) | `+54.6 bps` | `-0.017 / +0.006` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 17:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,183.86 | ⚪ **CASH** | **+34.3 bps** (±13.0) | `+64.0 bps` | `+0.024 / -0.042` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,772.52 | ⚪ **CASH** | **+47.5 bps** (±7.1) | `+94.8 bps` | `-0.043 / -0.062` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $73.68 | ⚪ **CASH** | **+19.4 bps** (±18.9) | `+41.4 bps` | `-0.026 / -0.020` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 17:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,257.29 | ⚪ **CASH** | **+34.3 bps** (±13.0) | `+64.0 bps` | `+0.024 / -0.042` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,772.78 | ⚪ **CASH** | **+47.5 bps** (±7.1) | `+94.8 bps` | `-0.043 / -0.062` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $73.83 | ⚪ **CASH** | **+19.4 bps** (±18.9) | `+41.4 bps` | `-0.026 / -0.020` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 17:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,723.20 | ⚪ **CASH** | **+34.3 bps** (±13.0) | `+64.0 bps` | `+0.024 / -0.042` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,753.28 | ⚪ **CASH** | **+47.5 bps** (±7.1) | `+94.8 bps` | `-0.043 / -0.062` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $72.91 | ⚪ **CASH** | **+19.4 bps** (±18.9) | `+41.4 bps` | `-0.026 / -0.020` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 17:01:01 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,762.41 | ⚪ **CASH** | **+34.3 bps** (±13.0) | `+64.0 bps` | `+0.024 / -0.042` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,750.19 | ⚪ **CASH** | **+47.5 bps** (±7.1) | `+94.8 bps` | `-0.043 / -0.062` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $72.99 | ⚪ **CASH** | **+19.4 bps** (±18.9) | `+41.4 bps` | `-0.026 / -0.020` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 16:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,492.81 | ⚪ **CASH** | **+30.0 bps** (±20.5) | `+50.9 bps` | `+0.051 / -0.001` | `0.49%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.5 bps > 19.5) |
| **ETHUSDT** | $1,740.15 | ⚪ **CASH** | **+58.4 bps** (±6.5) | `+114.5 bps` | `-0.048 / -0.075` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $72.61 | ⚪ **CASH** | **+10.0 bps** (±12.6) | `+25.2 bps` | `-0.030 / -0.066` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 16:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,476.01 | ⚪ **CASH** | **+30.0 bps** (±20.5) | `+50.9 bps` | `+0.051 / -0.001` | `0.49%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.5 bps > 19.5) |
| **ETHUSDT** | $1,752.20 | ⚪ **CASH** | **+58.4 bps** (±6.5) | `+114.5 bps` | `-0.048 / -0.075` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $72.74 | ⚪ **CASH** | **+10.0 bps** (±12.6) | `+25.2 bps` | `-0.030 / -0.066` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 16:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,832.01 | ⚪ **CASH** | **+30.0 bps** (±20.5) | `+50.9 bps` | `+0.051 / -0.001` | `0.49%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.5 bps > 19.5) |
| **ETHUSDT** | $1,763.90 | ⚪ **CASH** | **+58.4 bps** (±6.5) | `+114.5 bps` | `-0.048 / -0.075` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $73.20 | ⚪ **CASH** | **+10.0 bps** (±12.6) | `+25.2 bps` | `-0.030 / -0.066` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 16:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,097.91 | ⚪ **CASH** | **+30.0 bps** (±20.5) | `+50.9 bps` | `+0.051 / -0.001` | `0.49%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.5 bps > 19.5) |
| **ETHUSDT** | $1,768.33 | ⚪ **CASH** | **+58.4 bps** (±6.5) | `+114.5 bps` | `-0.048 / -0.075` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $73.37 | ⚪ **CASH** | **+10.0 bps** (±12.6) | `+25.2 bps` | `-0.030 / -0.066` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 15:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,200.01 | ⚪ **CASH** | **+30.8 bps** (±14.6) | `+47.5 bps` | `+0.051 / +0.056` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,765.58 | ⚪ **CASH** | **+55.2 bps** (±10.6) | `+111.5 bps` | `-0.063 / -0.085` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $73.30 | ⚪ **CASH** | **+10.6 bps** (±6.1) | `+26.2 bps` | `-0.055 / -0.044` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 15:31:01 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,577.87 | ⚪ **CASH** | **+30.8 bps** (±14.6) | `+47.5 bps` | `+0.051 / +0.056` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,771.64 | ⚪ **CASH** | **+55.2 bps** (±10.6) | `+111.5 bps` | `-0.063 / -0.085` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $73.94 | ⚪ **CASH** | **+10.6 bps** (±6.1) | `+26.2 bps` | `-0.055 / -0.044` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 15:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,648.42 | ⚪ **CASH** | **+30.8 bps** (±14.6) | `+47.5 bps` | `+0.051 / +0.056` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,775.80 | ⚪ **CASH** | **+55.2 bps** (±10.6) | `+111.5 bps` | `-0.063 / -0.085` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $74.12 | ⚪ **CASH** | **+10.6 bps** (±6.1) | `+26.2 bps` | `-0.055 / -0.044` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |
