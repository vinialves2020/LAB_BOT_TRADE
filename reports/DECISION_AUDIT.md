# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-14 14:00:51 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-14 14:00:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $66,822.53 | ⚪ **CASH** | **-43.5 bps** (±27.9) | `-57.4 bps` | `-0.066 / -0.106` | `0.50%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (27.9 bps > 19.5) |
| **ETHUSDT** | $1,893.82 | ⚪ **CASH** | **-44.8 bps** (±15.2) | `-59.8 bps` | `-0.107 / -0.079` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.51 | ⚪ **CASH** | **-6.4 bps** (±10.5) | `-2.4 bps` | `-0.022 / -0.031` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 13:45:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $66,828.81 | ⚪ **CASH** | **-36.8 bps** (±16.4) | `-49.5 bps` | `-0.046 / -0.116` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,893.30 | ⚪ **CASH** | **-44.5 bps** (±12.0) | `-58.9 bps` | `-0.084 / -0.143` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.60 | ⚪ **CASH** | **+4.7 bps** (±7.9) | `+17.6 bps` | `-0.012 / -0.065` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 13:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $66,657.58 | ⚪ **CASH** | **-36.8 bps** (±16.4) | `-49.5 bps` | `-0.046 / -0.116` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,889.34 | ⚪ **CASH** | **-44.5 bps** (±12.0) | `-58.9 bps` | `-0.084 / -0.143` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.27 | ⚪ **CASH** | **+4.7 bps** (±7.9) | `+17.6 bps` | `-0.012 / -0.065` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 13:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $66,807.14 | ⚪ **CASH** | **-36.8 bps** (±16.4) | `-49.5 bps` | `-0.046 / -0.116` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,893.96 | ⚪ **CASH** | **-44.5 bps** (±12.0) | `-58.9 bps` | `-0.084 / -0.143` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.62 | ⚪ **CASH** | **+4.7 bps** (±7.9) | `+17.6 bps` | `-0.012 / -0.065` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 13:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $66,992.01 | ⚪ **CASH** | **-36.8 bps** (±16.4) | `-49.5 bps` | `-0.046 / -0.116` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,898.75 | ⚪ **CASH** | **-44.5 bps** (±12.0) | `-58.9 bps` | `-0.084 / -0.143` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.57 | ⚪ **CASH** | **+4.7 bps** (±7.9) | `+17.6 bps` | `-0.012 / -0.065` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 12:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,095.43 | ⚪ **CASH** | **-42.3 bps** (±14.7) | `-62.3 bps` | `-0.044 / -0.084` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,903.30 | ⚪ **CASH** | **-38.9 bps** (±6.2) | `-51.2 bps` | `-0.083 / -0.124` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.63 | ⚪ **CASH** | **-3.6 bps** (±10.1) | `+5.9 bps` | `-0.010 / -0.114` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 12:30:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,181.03 | ⚪ **CASH** | **-42.3 bps** (±14.7) | `-62.3 bps` | `-0.044 / -0.084` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,907.89 | ⚪ **CASH** | **-38.9 bps** (±6.2) | `-51.2 bps` | `-0.083 / -0.124` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.85 | ⚪ **CASH** | **-3.6 bps** (±10.1) | `+5.9 bps` | `-0.010 / -0.114` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 12:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,183.30 | ⚪ **CASH** | **-42.3 bps** (±14.7) | `-62.3 bps` | `-0.044 / -0.084` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,907.08 | ⚪ **CASH** | **-38.9 bps** (±6.2) | `-51.2 bps` | `-0.083 / -0.124` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.77 | ⚪ **CASH** | **-3.6 bps** (±10.1) | `+5.9 bps` | `-0.010 / -0.114` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 12:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,292.01 | ⚪ **CASH** | **-42.3 bps** (±14.7) | `-62.3 bps` | `-0.044 / -0.084` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,910.83 | ⚪ **CASH** | **-38.9 bps** (±6.2) | `-51.2 bps` | `-0.083 / -0.124` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $76.04 | ⚪ **CASH** | **-3.6 bps** (±10.1) | `+5.9 bps` | `-0.010 / -0.114` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 11:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,238.00 | ⚪ **CASH** | **-43.4 bps** (±13.7) | `-64.7 bps` | `-0.044 / -0.082` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,909.63 | ⚪ **CASH** | **-36.4 bps** (±5.6) | `-49.2 bps` | `-0.075 / -0.098` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.95 | ⚪ **CASH** | **-1.4 bps** (±9.6) | `+8.9 bps` | `-0.012 / -0.098` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-14 11:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,211.40 | ⚪ **CASH** | **-43.4 bps** (±13.7) | `-64.7 bps` | `-0.044 / -0.082` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,907.11 | ⚪ **CASH** | **-36.4 bps** (±5.6) | `-49.2 bps` | `-0.075 / -0.098` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.74 | ⚪ **CASH** | **-1.4 bps** (±9.6) | `+8.9 bps` | `-0.012 / -0.098` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-14 11:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,252.50 | ⚪ **CASH** | **-43.4 bps** (±13.7) | `-64.7 bps` | `-0.044 / -0.082` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,907.39 | ⚪ **CASH** | **-36.4 bps** (±5.6) | `-49.2 bps` | `-0.075 / -0.098` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.85 | ⚪ **CASH** | **-1.4 bps** (±9.6) | `+8.9 bps` | `-0.012 / -0.098` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-14 11:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,294.72 | ⚪ **CASH** | **-43.4 bps** (±13.7) | `-64.7 bps` | `-0.044 / -0.082` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,909.55 | ⚪ **CASH** | **-36.4 bps** (±5.6) | `-49.2 bps` | `-0.075 / -0.098` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.79 | ⚪ **CASH** | **-1.4 bps** (±9.6) | `+8.9 bps` | `-0.012 / -0.098` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-14 10:45:35 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,266.91 | ⚪ **CASH** | **-48.0 bps** (±17.5) | `-75.0 bps` | `-0.041 / -0.047` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,909.38 | ⚪ **CASH** | **-31.3 bps** (±6.1) | `-43.9 bps` | `-0.068 / -0.049` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.78 | ⚪ **CASH** | **-0.1 bps** (±8.8) | `+7.3 bps` | `-0.009 / -0.045` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.4 bps) |

---

### 🕒 Ciclo `2026-11-14 10:30:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,282.90 | ⚪ **CASH** | **-48.0 bps** (±17.5) | `-75.0 bps` | `-0.041 / -0.047` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,909.60 | ⚪ **CASH** | **-31.3 bps** (±6.1) | `-43.9 bps` | `-0.068 / -0.049` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.82 | ⚪ **CASH** | **-0.1 bps** (±8.8) | `+7.3 bps` | `-0.009 / -0.045` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.4 bps) |

---

### 🕒 Ciclo `2026-11-14 10:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,232.00 | ⚪ **CASH** | **-48.0 bps** (±17.5) | `-75.0 bps` | `-0.041 / -0.047` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,907.01 | ⚪ **CASH** | **-31.3 bps** (±6.1) | `-43.9 bps` | `-0.068 / -0.049` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.77 | ⚪ **CASH** | **-0.1 bps** (±8.8) | `+7.3 bps` | `-0.009 / -0.045` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.4 bps) |

---

### 🕒 Ciclo `2026-11-14 10:00:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,390.00 | ⚪ **CASH** | **-48.0 bps** (±17.5) | `-75.0 bps` | `-0.041 / -0.047` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,912.13 | ⚪ **CASH** | **-31.3 bps** (±6.1) | `-43.9 bps` | `-0.068 / -0.049` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.90 | ⚪ **CASH** | **-0.1 bps** (±8.8) | `+7.3 bps` | `-0.009 / -0.045` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.4 bps) |

---

### 🕒 Ciclo `2026-11-14 09:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,196.00 | ⚪ **CASH** | **-41.7 bps** (±16.9) | `-61.1 bps` | `-0.048 / -0.072` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.3 bps) |
| **ETHUSDT** | $1,909.79 | ⚪ **CASH** | **-37.3 bps** (±18.8) | `-46.1 bps` | `-0.073 / -0.133` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.5 bps) |
| **SOLUSDT** | $75.75 | ⚪ **CASH** | **-4.2 bps** (±4.6) | `+1.7 bps` | `-0.018 / -0.068` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.2 bps) |

---

### 🕒 Ciclo `2026-11-14 09:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,194.00 | ⚪ **CASH** | **-41.7 bps** (±16.9) | `-61.1 bps` | `-0.048 / -0.072` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.3 bps) |
| **ETHUSDT** | $1,906.82 | ⚪ **CASH** | **-37.3 bps** (±18.8) | `-46.1 bps` | `-0.073 / -0.133` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.5 bps) |
| **SOLUSDT** | $75.73 | ⚪ **CASH** | **-4.2 bps** (±4.6) | `+1.7 bps` | `-0.018 / -0.068` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.2 bps) |

---

### 🕒 Ciclo `2026-11-14 09:15:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,155.68 | ⚪ **CASH** | **-41.7 bps** (±16.9) | `-61.1 bps` | `-0.048 / -0.072` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.3 bps) |
| **ETHUSDT** | $1,903.36 | ⚪ **CASH** | **-37.3 bps** (±18.8) | `-46.1 bps` | `-0.073 / -0.133` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.5 bps) |
| **SOLUSDT** | $75.55 | ⚪ **CASH** | **-4.2 bps** (±4.6) | `+1.7 bps` | `-0.018 / -0.068` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.2 bps) |

---

### 🕒 Ciclo `2026-11-14 09:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,003.12 | ⚪ **CASH** | **-41.7 bps** (±16.9) | `-61.1 bps` | `-0.048 / -0.072` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.3 bps) |
| **ETHUSDT** | $1,895.32 | ⚪ **CASH** | **-37.3 bps** (±18.8) | `-46.1 bps` | `-0.073 / -0.133` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.5 bps) |
| **SOLUSDT** | $75.27 | ⚪ **CASH** | **-4.2 bps** (±4.6) | `+1.7 bps` | `-0.018 / -0.068` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.2 bps) |

---

### 🕒 Ciclo `2026-11-14 08:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,106.00 | ⚪ **CASH** | **-47.9 bps** (±15.8) | `-73.1 bps` | `-0.035 / -0.092` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,900.56 | ⚪ **CASH** | **-30.9 bps** (±18.9) | `-33.2 bps` | `-0.068 / -0.169` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.7 bps) |
| **SOLUSDT** | $75.36 | ⚪ **CASH** | **-12.3 bps** (±15.4) | `-12.3 bps` | `-0.024 / -0.050` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.2 bps) |

---

### 🕒 Ciclo `2026-11-14 08:30:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,234.01 | ⚪ **CASH** | **-47.9 bps** (±15.8) | `-73.1 bps` | `-0.035 / -0.092` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,904.76 | ⚪ **CASH** | **-30.9 bps** (±18.9) | `-33.2 bps` | `-0.068 / -0.169` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.7 bps) |
| **SOLUSDT** | $75.47 | ⚪ **CASH** | **-12.3 bps** (±15.4) | `-12.3 bps` | `-0.024 / -0.050` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.2 bps) |

---

### 🕒 Ciclo `2026-11-14 08:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,274.00 | ⚪ **CASH** | **-47.9 bps** (±15.8) | `-73.1 bps` | `-0.035 / -0.092` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,902.57 | ⚪ **CASH** | **-30.9 bps** (±18.9) | `-33.2 bps` | `-0.068 / -0.169` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.7 bps) |
| **SOLUSDT** | $75.41 | ⚪ **CASH** | **-12.3 bps** (±15.4) | `-12.3 bps` | `-0.024 / -0.050` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.2 bps) |

---

### 🕒 Ciclo `2026-11-14 08:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,291.99 | ⚪ **CASH** | **-47.9 bps** (±15.8) | `-73.1 bps` | `-0.035 / -0.092` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,902.26 | ⚪ **CASH** | **-30.9 bps** (±18.9) | `-33.2 bps` | `-0.068 / -0.169` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.7 bps) |
| **SOLUSDT** | $75.40 | ⚪ **CASH** | **-12.3 bps** (±15.4) | `-12.3 bps` | `-0.024 / -0.050` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.2 bps) |

---

### 🕒 Ciclo `2026-11-14 07:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,057.00 | ⚪ **CASH** | **-50.2 bps** (±16.8) | `-79.3 bps` | `-0.021 / -0.088` | `0.53%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,893.11 | ⚪ **CASH** | **+10.2 bps** (±7.2) | `+34.4 bps` | `-0.050 / -0.132` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.7 bps) |
| **SOLUSDT** | $75.07 | ⚪ **CASH** | **-0.0 bps** (±6.8) | `+6.1 bps` | `-0.019 / -0.030` | `0.76%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.9 bps) |

---

### 🕒 Ciclo `2026-11-14 07:30:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,218.00 | ⚪ **CASH** | **-50.2 bps** (±16.8) | `-79.3 bps` | `-0.021 / -0.088` | `0.53%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,897.41 | ⚪ **CASH** | **+10.2 bps** (±7.2) | `+34.4 bps` | `-0.050 / -0.132` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.7 bps) |
| **SOLUSDT** | $75.41 | ⚪ **CASH** | **-0.0 bps** (±6.8) | `+6.1 bps` | `-0.019 / -0.030` | `0.76%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.9 bps) |

---

### 🕒 Ciclo `2026-11-14 07:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,432.01 | ⚪ **CASH** | **-50.2 bps** (±16.8) | `-79.3 bps` | `-0.021 / -0.088` | `0.53%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,903.90 | ⚪ **CASH** | **+10.2 bps** (±7.2) | `+34.4 bps` | `-0.050 / -0.132` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.7 bps) |
| **SOLUSDT** | $75.53 | ⚪ **CASH** | **-0.0 bps** (±6.8) | `+6.1 bps` | `-0.019 / -0.030` | `0.76%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.9 bps) |

---

### 🕒 Ciclo `2026-11-14 07:00:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,366.66 | ⚪ **CASH** | **-50.2 bps** (±16.8) | `-79.3 bps` | `-0.021 / -0.088` | `0.53%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,904.31 | ⚪ **CASH** | **+10.2 bps** (±7.2) | `+34.4 bps` | `-0.050 / -0.132` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.7 bps) |
| **SOLUSDT** | $75.72 | ⚪ **CASH** | **-0.0 bps** (±6.8) | `+6.1 bps` | `-0.019 / -0.030` | `0.76%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.9 bps) |

---

### 🕒 Ciclo `2026-11-14 06:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,328.06 | ⚪ **CASH** | **-46.3 bps** (±12.2) | `-73.5 bps` | `-0.014 / -0.100` | `0.53%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,903.25 | ⚪ **CASH** | **+13.1 bps** (±6.0) | `+38.5 bps` | `-0.047 / -0.127` | `0.66%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |
| **SOLUSDT** | $75.48 | ⚪ **CASH** | **-4.0 bps** (±11.9) | `-3.7 bps` | `-0.006 / -0.001` | `0.77%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 30.8 bps) |

---

### 🕒 Ciclo `2026-11-14 06:30:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,376.01 | ⚪ **CASH** | **-46.3 bps** (±12.2) | `-73.5 bps` | `-0.014 / -0.100` | `0.53%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,907.46 | ⚪ **CASH** | **+13.1 bps** (±6.0) | `+38.5 bps` | `-0.047 / -0.127` | `0.66%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |
| **SOLUSDT** | $75.72 | ⚪ **CASH** | **-4.0 bps** (±11.9) | `-3.7 bps` | `-0.006 / -0.001` | `0.77%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 30.8 bps) |

---

### 🕒 Ciclo `2026-11-14 06:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,262.13 | ⚪ **CASH** | **-46.3 bps** (±12.2) | `-73.5 bps` | `-0.014 / -0.100` | `0.53%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,904.39 | ⚪ **CASH** | **+13.1 bps** (±6.0) | `+38.5 bps` | `-0.047 / -0.127` | `0.66%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |
| **SOLUSDT** | $75.85 | ⚪ **CASH** | **-4.0 bps** (±11.9) | `-3.7 bps` | `-0.006 / -0.001` | `0.77%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 30.8 bps) |

---

### 🕒 Ciclo `2026-11-14 06:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,246.03 | ⚪ **CASH** | **-46.3 bps** (±12.2) | `-73.5 bps` | `-0.014 / -0.100` | `0.53%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,906.50 | ⚪ **CASH** | **+13.1 bps** (±6.0) | `+38.5 bps` | `-0.047 / -0.127` | `0.66%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |
| **SOLUSDT** | $76.04 | ⚪ **CASH** | **-4.0 bps** (±11.9) | `-3.7 bps` | `-0.006 / -0.001` | `0.77%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 30.8 bps) |

---

### 🕒 Ciclo `2026-11-14 05:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $66,898.00 | ⚪ **CASH** | **-41.2 bps** (±16.8) | `-63.1 bps` | `-0.013 / -0.104` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.4 bps) |
| **ETHUSDT** | $1,896.01 | ⚪ **CASH** | **-0.1 bps** (±18.8) | `+18.7 bps` | `-0.064 / -0.130` | `0.66%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |
| **SOLUSDT** | $75.71 | ⚪ **CASH** | **+1.4 bps** (±20.6) | `+8.2 bps` | `-0.018 / +0.008` | `0.77%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 05:30:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,116.00 | ⚪ **CASH** | **-41.2 bps** (±16.8) | `-63.1 bps` | `-0.013 / -0.104` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.4 bps) |
| **ETHUSDT** | $1,901.18 | ⚪ **CASH** | **-0.1 bps** (±18.8) | `+18.7 bps` | `-0.064 / -0.130` | `0.66%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |
| **SOLUSDT** | $75.60 | ⚪ **CASH** | **+1.4 bps** (±20.6) | `+8.2 bps` | `-0.018 / +0.008` | `0.77%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 05:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,216.01 | ⚪ **CASH** | **-41.2 bps** (±16.8) | `-63.1 bps` | `-0.013 / -0.104` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.4 bps) |
| **ETHUSDT** | $1,901.60 | ⚪ **CASH** | **-0.1 bps** (±18.8) | `+18.7 bps` | `-0.064 / -0.130` | `0.66%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |
| **SOLUSDT** | $75.61 | ⚪ **CASH** | **+1.4 bps** (±20.6) | `+8.2 bps` | `-0.018 / +0.008` | `0.77%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.6 bps > 19.5) |
