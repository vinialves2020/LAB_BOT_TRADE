# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-22 19:32:01 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-22 19:32:01 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,530.16 | ⚪ **CASH** | **-27.5 bps** (±12.2) | `-33.1 bps` | `-0.127 / +0.062` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,391.87 | ⚪ **CASH** | **-28.6 bps** (±13.3) | `-33.0 bps` | `-0.096 / -0.015` | `0.45%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.88 | ⚪ **CASH** | **-21.9 bps** (±15.0) | `-24.2 bps` | `-0.057 / -0.017` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 19:17:10 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,356.00 | ⚪ **CASH** | **-27.5 bps** (±12.2) | `-33.1 bps` | `-0.127 / +0.062` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,382.78 | ⚪ **CASH** | **-28.6 bps** (±13.3) | `-33.0 bps` | `-0.096 / -0.015` | `0.45%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.45 | ⚪ **CASH** | **-21.9 bps** (±15.0) | `-24.2 bps` | `-0.057 / -0.017` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 19:02:10 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,360.01 | ⚪ **CASH** | **-27.5 bps** (±12.2) | `-33.1 bps` | `-0.127 / +0.062` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,382.35 | ⚪ **CASH** | **-28.6 bps** (±13.3) | `-33.0 bps` | `-0.096 / -0.015` | `0.45%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.49 | ⚪ **CASH** | **-21.9 bps** (±15.0) | `-24.2 bps` | `-0.057 / -0.017` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 18:47:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,383.11 | ⚪ **CASH** | **-40.0 bps** (±13.0) | `-52.6 bps` | `-0.134 / +0.030` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,384.10 | ⚪ **CASH** | **-31.1 bps** (±17.4) | `-34.5 bps` | `-0.099 / -0.040` | `0.46%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.82 | ⚪ **CASH** | **-19.0 bps** (±15.2) | `-20.4 bps` | `-0.048 / -0.001` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 18:32:06 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,166.06 | ⚪ **CASH** | **-40.0 bps** (±13.0) | `-52.6 bps` | `-0.134 / +0.030` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,377.91 | ⚪ **CASH** | **-31.1 bps** (±17.4) | `-34.5 bps` | `-0.099 / -0.040` | `0.46%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.54 | ⚪ **CASH** | **-19.0 bps** (±15.2) | `-20.4 bps` | `-0.048 / -0.001` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 18:17:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,136.63 | ⚪ **CASH** | **-40.0 bps** (±13.0) | `-52.6 bps` | `-0.134 / +0.030` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,377.18 | ⚪ **CASH** | **-31.1 bps** (±17.4) | `-34.5 bps` | `-0.099 / -0.040` | `0.46%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.22 | ⚪ **CASH** | **-19.0 bps** (±15.2) | `-20.4 bps` | `-0.048 / -0.001` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 18:02:16 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,135.04 | ⚪ **CASH** | **-40.0 bps** (±13.0) | `-52.6 bps` | `-0.134 / +0.030` | `0.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,377.55 | ⚪ **CASH** | **-31.1 bps** (±17.4) | `-34.5 bps` | `-0.099 / -0.040` | `0.46%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.50 | ⚪ **CASH** | **-19.0 bps** (±15.2) | `-20.4 bps` | `-0.048 / -0.001` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 17:47:10 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,356.00 | ⚪ **CASH** | **-41.3 bps** (±12.3) | `-48.1 bps` | `-0.149 / -0.044` | `0.34%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,383.60 | ⚪ **CASH** | **-36.3 bps** (±14.8) | `-42.5 bps` | `-0.094 / -0.066` | `0.47%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.90 | ⚪ **CASH** | **-10.1 bps** (±20.8) | `-3.9 bps` | `-0.041 / +0.010` | `0.50%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 17:32:17 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,358.00 | ⚪ **CASH** | **-41.3 bps** (±12.3) | `-48.1 bps` | `-0.149 / -0.044` | `0.34%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,382.22 | ⚪ **CASH** | **-36.3 bps** (±14.8) | `-42.5 bps` | `-0.094 / -0.066` | `0.47%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.94 | ⚪ **CASH** | **-10.1 bps** (±20.8) | `-3.9 bps` | `-0.041 / +0.010` | `0.50%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 17:17:23 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,302.00 | ⚪ **CASH** | **-41.3 bps** (±12.3) | `-48.1 bps` | `-0.149 / -0.044` | `0.34%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,382.41 | ⚪ **CASH** | **-36.3 bps** (±14.8) | `-42.5 bps` | `-0.094 / -0.066` | `0.47%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.66 | ⚪ **CASH** | **-10.1 bps** (±20.8) | `-3.9 bps` | `-0.041 / +0.010` | `0.50%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 17:02:19 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,306.46 | ⚪ **CASH** | **-41.3 bps** (±12.3) | `-48.1 bps` | `-0.149 / -0.044` | `0.34%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,381.16 | ⚪ **CASH** | **-36.3 bps** (±14.8) | `-42.5 bps` | `-0.094 / -0.066` | `0.47%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.78 | ⚪ **CASH** | **-10.1 bps** (±20.8) | `-3.9 bps` | `-0.041 / +0.010` | `0.50%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 16:47:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,353.21 | ⚪ **CASH** | **-40.6 bps** (±9.3) | `-46.6 bps` | `-0.152 / -0.047` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,378.82 | ⚪ **CASH** | **-36.4 bps** (±11.9) | `-45.7 bps` | `-0.080 / -0.046` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.89 | ⚪ **CASH** | **-2.7 bps** (±14.7) | `+5.8 bps` | `-0.037 / +0.048` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 16:32:08 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,477.35 | ⚪ **CASH** | **-40.6 bps** (±9.3) | `-46.6 bps` | `-0.152 / -0.047` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,388.93 | ⚪ **CASH** | **-36.4 bps** (±11.9) | `-45.7 bps` | `-0.080 / -0.046` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.08 | ⚪ **CASH** | **-2.7 bps** (±14.7) | `+5.8 bps` | `-0.037 / +0.048` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 16:17:18 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,652.01 | ⚪ **CASH** | **-40.6 bps** (±9.3) | `-46.6 bps` | `-0.152 / -0.047` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,397.87 | ⚪ **CASH** | **-36.4 bps** (±11.9) | `-45.7 bps` | `-0.080 / -0.046` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.50 | ⚪ **CASH** | **-2.7 bps** (±14.7) | `+5.8 bps` | `-0.037 / +0.048` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 16:02:19 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,676.61 | ⚪ **CASH** | **-40.6 bps** (±9.3) | `-46.6 bps` | `-0.152 / -0.047` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,397.85 | ⚪ **CASH** | **-36.4 bps** (±11.9) | `-45.7 bps` | `-0.080 / -0.046` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.65 | ⚪ **CASH** | **-2.7 bps** (±14.7) | `+5.8 bps` | `-0.037 / +0.048` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 15:46:56 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,499.77 | ⚪ **CASH** | **-24.1 bps** (±9.0) | `-14.7 bps` | `-0.163 / -0.051` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,393.50 | ⚪ **CASH** | **-4.9 bps** (±12.3) | `+12.2 bps` | `-0.052 / -0.088` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.37 | ⚪ **CASH** | **-2.9 bps** (±11.6) | `+1.7 bps` | `-0.028 / +0.091` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 15:32:17 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,472.01 | ⚪ **CASH** | **-24.1 bps** (±9.0) | `-14.7 bps` | `-0.163 / -0.051` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,393.74 | ⚪ **CASH** | **-4.9 bps** (±12.3) | `+12.2 bps` | `-0.052 / -0.088` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.30 | ⚪ **CASH** | **-2.9 bps** (±11.6) | `+1.7 bps` | `-0.028 / +0.091` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 15:17:11 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,548.20 | ⚪ **CASH** | **-24.1 bps** (±9.0) | `-14.7 bps` | `-0.163 / -0.051` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,394.99 | ⚪ **CASH** | **-4.9 bps** (±12.3) | `+12.2 bps` | `-0.052 / -0.088` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.27 | ⚪ **CASH** | **-2.9 bps** (±11.6) | `+1.7 bps` | `-0.028 / +0.091` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 15:02:23 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,802.01 | ⚪ **CASH** | **-24.1 bps** (±9.0) | `-14.7 bps` | `-0.163 / -0.051` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,410.83 | ⚪ **CASH** | **-4.9 bps** (±12.3) | `+12.2 bps` | `-0.052 / -0.088` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.70 | ⚪ **CASH** | **-2.9 bps** (±11.6) | `+1.7 bps` | `-0.028 / +0.091` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 14:47:20 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,791.83 | ⚪ **CASH** | **-18.4 bps** (±6.3) | `-6.4 bps` | `-0.137 / -0.088` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,410.31 | ⚪ **CASH** | **-9.7 bps** (±10.6) | `+3.1 bps` | `-0.034 / -0.135` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.49 | ⚪ **CASH** | **+0.9 bps** (±14.4) | `+9.0 bps` | `-0.015 / +0.053` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 14:32:04 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,745.30 | ⚪ **CASH** | **-18.4 bps** (±6.3) | `-6.4 bps` | `-0.137 / -0.088` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,405.10 | ⚪ **CASH** | **-9.7 bps** (±10.6) | `+3.1 bps` | `-0.034 / -0.135` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.78 | ⚪ **CASH** | **+0.9 bps** (±14.4) | `+9.0 bps` | `-0.015 / +0.053` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 14:17:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,607.99 | ⚪ **CASH** | **-18.4 bps** (±6.3) | `-6.4 bps` | `-0.137 / -0.088` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,403.65 | ⚪ **CASH** | **-9.7 bps** (±10.6) | `+3.1 bps` | `-0.034 / -0.135` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.85 | ⚪ **CASH** | **+0.9 bps** (±14.4) | `+9.0 bps` | `-0.015 / +0.053` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 14:02:15 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,840.01 | ⚪ **CASH** | **-18.4 bps** (±6.3) | `-6.4 bps` | `-0.137 / -0.088` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,411.92 | ⚪ **CASH** | **-9.7 bps** (±10.6) | `+3.1 bps` | `-0.034 / -0.135` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.19 | ⚪ **CASH** | **+0.9 bps** (±14.4) | `+9.0 bps` | `-0.015 / +0.053` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 13:47:17 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,541.98 | ⚪ **CASH** | **-14.2 bps** (±2.9) | `+0.9 bps` | `-0.128 / -0.112` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,404.37 | ⚪ **CASH** | **-4.3 bps** (±7.5) | `+10.8 bps` | `-0.020 / -0.136` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.63 | ⚪ **CASH** | **-6.4 bps** (±12.2) | `+1.6 bps` | `-0.022 / -0.041` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 13:32:17 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,785.83 | ⚪ **CASH** | **-14.2 bps** (±2.9) | `+0.9 bps` | `-0.128 / -0.112` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,402.75 | ⚪ **CASH** | **-4.3 bps** (±7.5) | `+10.8 bps` | `-0.020 / -0.136` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.58 | ⚪ **CASH** | **-6.4 bps** (±12.2) | `+1.6 bps` | `-0.022 / -0.041` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 13:17:17 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,740.01 | ⚪ **CASH** | **-14.2 bps** (±2.9) | `+0.9 bps` | `-0.128 / -0.112` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,399.87 | ⚪ **CASH** | **-4.3 bps** (±7.5) | `+10.8 bps` | `-0.020 / -0.136` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.34 | ⚪ **CASH** | **-6.4 bps** (±12.2) | `+1.6 bps` | `-0.022 / -0.041` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 13:02:18 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,705.74 | ⚪ **CASH** | **-14.2 bps** (±2.9) | `+0.9 bps` | `-0.128 / -0.112` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,400.93 | ⚪ **CASH** | **-4.3 bps** (±7.5) | `+10.8 bps` | `-0.020 / -0.136` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.36 | ⚪ **CASH** | **-6.4 bps** (±12.2) | `+1.6 bps` | `-0.022 / -0.041` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 12:47:11 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,766.30 | ⚪ **CASH** | **-11.3 bps** (±1.8) | `+5.2 bps` | `-0.126 / -0.103` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,404.28 | ⚪ **CASH** | **-2.1 bps** (±4.7) | `+14.1 bps` | `-0.018 / -0.141` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.52 | ⚪ **CASH** | **-7.4 bps** (±12.0) | `+3.3 bps` | `-0.024 / -0.092` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 12:32:01 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,716.98 | ⚪ **CASH** | **-11.3 bps** (±1.8) | `+5.2 bps` | `-0.126 / -0.103` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,400.30 | ⚪ **CASH** | **-2.1 bps** (±4.7) | `+14.1 bps` | `-0.018 / -0.141` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.24 | ⚪ **CASH** | **-7.4 bps** (±12.0) | `+3.3 bps` | `-0.024 / -0.092` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 12:17:25 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,874.13 | ⚪ **CASH** | **-11.3 bps** (±1.8) | `+5.2 bps` | `-0.126 / -0.103` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,404.78 | ⚪ **CASH** | **-2.1 bps** (±4.7) | `+14.1 bps` | `-0.018 / -0.141` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.53 | ⚪ **CASH** | **-7.4 bps** (±12.0) | `+3.3 bps` | `-0.024 / -0.092` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 12:02:08 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,785.24 | ⚪ **CASH** | **-11.3 bps** (±1.8) | `+5.2 bps` | `-0.126 / -0.103` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,403.57 | ⚪ **CASH** | **-2.1 bps** (±4.7) | `+14.1 bps` | `-0.018 / -0.141` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.55 | ⚪ **CASH** | **-7.4 bps** (±12.0) | `+3.3 bps` | `-0.024 / -0.092` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 11:47:18 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,862.66 | ⚪ **CASH** | **-11.5 bps** (±1.9) | `+2.7 bps` | `-0.114 / -0.099` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,403.87 | ⚪ **CASH** | **+4.2 bps** (±8.5) | `+25.6 bps` | `-0.011 / -0.148` | `0.47%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.60 | ⚪ **CASH** | **-9.0 bps** (±10.6) | `+5.0 bps` | `-0.023 / -0.176` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 11:32:08 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,922.10 | ⚪ **CASH** | **-11.5 bps** (±1.9) | `+2.7 bps` | `-0.114 / -0.099` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,404.72 | ⚪ **CASH** | **+4.2 bps** (±8.5) | `+25.6 bps` | `-0.011 / -0.148` | `0.47%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.63 | ⚪ **CASH** | **-9.0 bps** (±10.6) | `+5.0 bps` | `-0.023 / -0.176` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 11:16:59 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,983.13 | ⚪ **CASH** | **-11.5 bps** (±1.9) | `+2.7 bps` | `-0.114 / -0.099` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,404.16 | ⚪ **CASH** | **+4.2 bps** (±8.5) | `+25.6 bps` | `-0.011 / -0.148` | `0.47%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.59 | ⚪ **CASH** | **-9.0 bps** (±10.6) | `+5.0 bps` | `-0.023 / -0.176` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 11:02:13 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,992.28 | ⚪ **CASH** | **-11.5 bps** (±1.9) | `+2.7 bps` | `-0.114 / -0.099` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,405.08 | ⚪ **CASH** | **+4.2 bps** (±8.5) | `+25.6 bps` | `-0.011 / -0.148` | `0.47%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.47 | ⚪ **CASH** | **-9.0 bps** (±10.6) | `+5.0 bps` | `-0.023 / -0.176` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 10:47:02 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,086.00 | ⚪ **CASH** | **-10.7 bps** (±3.5) | `+4.9 bps` | `-0.111 / -0.113` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,408.14 | ⚪ **CASH** | **+0.9 bps** (±10.2) | `+20.3 bps` | `-0.006 / -0.163` | `0.48%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.67 | ⚪ **CASH** | **-9.8 bps** (±10.6) | `+4.9 bps` | `-0.028 / -0.194` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
