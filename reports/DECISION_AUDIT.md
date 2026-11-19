# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-19 12:15:36 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-19 12:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,810.00 | ⚪ **CASH** | **+32.9 bps** (±14.4) | `+57.5 bps` | `+0.014 / +0.042` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,804.89 | ⚪ **CASH** | **-2.5 bps** (±4.3) | `-6.7 bps` | `-0.004 / +0.041` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $74.71 | ⚪ **CASH** | **+15.9 bps** (±3.9) | `+12.9 bps` | `+0.043 / +0.179` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 12:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,800.28 | ⚪ **CASH** | **+32.9 bps** (±14.4) | `+57.5 bps` | `+0.014 / +0.042` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,802.64 | ⚪ **CASH** | **-2.5 bps** (±4.3) | `-6.7 bps` | `-0.004 / +0.041` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $74.63 | ⚪ **CASH** | **+15.9 bps** (±3.9) | `+12.9 bps` | `+0.043 / +0.179` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 11:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,980.00 | ⚪ **CASH** | **+36.5 bps** (±17.7) | `+69.0 bps` | `+0.006 / -0.005` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,808.98 | ⚪ **CASH** | **-1.0 bps** (±5.0) | `-3.3 bps` | `-0.011 / +0.048` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.92 | ⚪ **CASH** | **+14.7 bps** (±4.8) | `+16.1 bps` | `+0.042 / +0.109` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 11:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,943.99 | ⚪ **CASH** | **+36.5 bps** (±17.7) | `+69.0 bps` | `+0.006 / -0.005` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,809.43 | ⚪ **CASH** | **-1.0 bps** (±5.0) | `-3.3 bps` | `-0.011 / +0.048` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.82 | ⚪ **CASH** | **+14.7 bps** (±4.8) | `+16.1 bps` | `+0.042 / +0.109` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 11:15:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,767.71 | ⚪ **CASH** | **+36.5 bps** (±17.7) | `+69.0 bps` | `+0.006 / -0.005` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,803.59 | ⚪ **CASH** | **-1.0 bps** (±5.0) | `-3.3 bps` | `-0.011 / +0.048` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.52 | ⚪ **CASH** | **+14.7 bps** (±4.8) | `+16.1 bps` | `+0.042 / +0.109` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 11:01:03 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,795.26 | ⚪ **CASH** | **+36.5 bps** (±17.7) | `+69.0 bps` | `+0.006 / -0.005` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,803.37 | ⚪ **CASH** | **-1.0 bps** (±5.0) | `-3.3 bps` | `-0.011 / +0.048` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.44 | ⚪ **CASH** | **+14.7 bps** (±4.8) | `+16.1 bps` | `+0.042 / +0.109` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 10:45:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,884.64 | ⚪ **CASH** | **+43.2 bps** (±14.9) | `+80.3 bps` | `+0.007 / -0.002` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,806.78 | ⚪ **CASH** | **-1.1 bps** (±3.7) | `-2.1 bps` | `-0.014 / +0.028` | `0.62%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $74.59 | ⚪ **CASH** | **+14.1 bps** (±4.3) | `+15.8 bps` | `+0.028 / +0.116` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 10:30:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,844.31 | ⚪ **CASH** | **+43.2 bps** (±14.9) | `+80.3 bps` | `+0.007 / -0.002` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,805.72 | ⚪ **CASH** | **-1.1 bps** (±3.7) | `-2.1 bps` | `-0.014 / +0.028` | `0.62%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $74.56 | ⚪ **CASH** | **+14.1 bps** (±4.3) | `+15.8 bps` | `+0.028 / +0.116` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 10:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,836.48 | ⚪ **CASH** | **+43.2 bps** (±14.9) | `+80.3 bps` | `+0.007 / -0.002` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,806.99 | ⚪ **CASH** | **-1.1 bps** (±3.7) | `-2.1 bps` | `-0.014 / +0.028` | `0.62%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $74.51 | ⚪ **CASH** | **+14.1 bps** (±4.3) | `+15.8 bps` | `+0.028 / +0.116` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 10:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,837.74 | ⚪ **CASH** | **+43.2 bps** (±14.9) | `+80.3 bps` | `+0.007 / -0.002` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,806.60 | ⚪ **CASH** | **-1.1 bps** (±3.7) | `-2.1 bps` | `-0.014 / +0.028` | `0.62%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $74.56 | ⚪ **CASH** | **+14.1 bps** (±4.3) | `+15.8 bps` | `+0.028 / +0.116` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 09:45:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,894.18 | ⚪ **CASH** | **+47.3 bps** (±12.7) | `+85.5 bps` | `+0.006 / +0.028` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,808.37 | ⚪ **CASH** | **+0.0 bps** (±5.3) | `+0.4 bps` | `-0.016 / +0.028` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.59 | ⚪ **CASH** | **+14.3 bps** (±3.3) | `+16.9 bps` | `+0.026 / +0.103` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 09:30:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,717.45 | ⚪ **CASH** | **+47.3 bps** (±12.7) | `+85.5 bps` | `+0.006 / +0.028` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,800.49 | ⚪ **CASH** | **+0.0 bps** (±5.3) | `+0.4 bps` | `-0.016 / +0.028` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.33 | ⚪ **CASH** | **+14.3 bps** (±3.3) | `+16.9 bps` | `+0.026 / +0.103` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 09:16:09 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,776.62 | ⚪ **CASH** | **+47.3 bps** (±12.7) | `+85.5 bps` | `+0.006 / +0.028` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,803.69 | ⚪ **CASH** | **+0.0 bps** (±5.3) | `+0.4 bps` | `-0.016 / +0.028` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.59 | ⚪ **CASH** | **+14.3 bps** (±3.3) | `+16.9 bps` | `+0.026 / +0.103` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 09:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,709.52 | ⚪ **CASH** | **+47.3 bps** (±12.7) | `+85.5 bps` | `+0.006 / +0.028` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,803.18 | ⚪ **CASH** | **+0.0 bps** (±5.3) | `+0.4 bps` | `-0.016 / +0.028` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.59 | ⚪ **CASH** | **+14.3 bps** (±3.3) | `+16.9 bps` | `+0.026 / +0.103` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 08:45:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,615.61 | ⚪ **CASH** | **+44.4 bps** (±13.8) | `+81.4 bps` | `+0.003 / +0.023` | `0.53%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,800.26 | ⚪ **CASH** | **+0.8 bps** (±4.0) | `+1.0 bps` | `-0.013 / +0.034` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.38 | ⚪ **CASH** | **+16.6 bps** (±3.3) | `+19.4 bps` | `+0.026 / +0.133` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 08:30:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,717.73 | ⚪ **CASH** | **+44.4 bps** (±13.8) | `+81.4 bps` | `+0.003 / +0.023` | `0.53%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,803.75 | ⚪ **CASH** | **+0.8 bps** (±4.0) | `+1.0 bps` | `-0.013 / +0.034` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.49 | ⚪ **CASH** | **+16.6 bps** (±3.3) | `+19.4 bps` | `+0.026 / +0.133` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 08:15:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,829.55 | ⚪ **CASH** | **+44.4 bps** (±13.8) | `+81.4 bps` | `+0.003 / +0.023` | `0.53%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,806.94 | ⚪ **CASH** | **+0.8 bps** (±4.0) | `+1.0 bps` | `-0.013 / +0.034` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.72 | ⚪ **CASH** | **+16.6 bps** (±3.3) | `+19.4 bps` | `+0.026 / +0.133` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 08:00:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,713.31 | ⚪ **CASH** | **+44.4 bps** (±13.8) | `+81.4 bps` | `+0.003 / +0.023` | `0.53%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,804.09 | ⚪ **CASH** | **+0.8 bps** (±4.0) | `+1.0 bps` | `-0.013 / +0.034` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.91 | ⚪ **CASH** | **+16.6 bps** (±3.3) | `+19.4 bps` | `+0.026 / +0.133` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 07:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,617.52 | ⚪ **CASH** | **+37.2 bps** (±14.7) | `+67.5 bps` | `+0.009 / +0.023` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,802.45 | ⚪ **CASH** | **+1.3 bps** (±4.4) | `+1.3 bps` | `-0.008 / +0.035` | `0.65%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $74.73 | ⚪ **CASH** | **+18.1 bps** (±6.8) | `+24.1 bps` | `+0.031 / +0.098` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 07:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,616.14 | ⚪ **CASH** | **+37.2 bps** (±14.7) | `+67.5 bps` | `+0.009 / +0.023` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,804.35 | ⚪ **CASH** | **+1.3 bps** (±4.4) | `+1.3 bps` | `-0.008 / +0.035` | `0.65%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $74.72 | ⚪ **CASH** | **+18.1 bps** (±6.8) | `+24.1 bps` | `+0.031 / +0.098` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 07:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,624.48 | ⚪ **CASH** | **+37.2 bps** (±14.7) | `+67.5 bps` | `+0.009 / +0.023` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,803.27 | ⚪ **CASH** | **+1.3 bps** (±4.4) | `+1.3 bps` | `-0.008 / +0.035` | `0.65%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $74.95 | ⚪ **CASH** | **+18.1 bps** (±6.8) | `+24.1 bps` | `+0.031 / +0.098` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 07:00:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,768.07 | ⚪ **CASH** | **+37.2 bps** (±14.7) | `+67.5 bps` | `+0.009 / +0.023` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,808.43 | ⚪ **CASH** | **+1.3 bps** (±4.4) | `+1.3 bps` | `-0.008 / +0.035` | `0.65%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $75.17 | ⚪ **CASH** | **+18.1 bps** (±6.8) | `+24.1 bps` | `+0.031 / +0.098` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 06:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,539.92 | ⚪ **CASH** | **+35.2 bps** (±16.9) | `+66.9 bps` | `+0.000 / +0.002` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,805.56 | ⚪ **CASH** | **+0.7 bps** (±2.5) | `+5.6 bps` | `-0.029 / -0.016` | `0.65%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.93 | ⚪ **CASH** | **+13.2 bps** (±4.0) | `+16.8 bps` | `+0.030 / +0.075` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 06:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,532.34 | ⚪ **CASH** | **+35.2 bps** (±16.9) | `+66.9 bps` | `+0.000 / +0.002` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,803.37 | ⚪ **CASH** | **+0.7 bps** (±2.5) | `+5.6 bps` | `-0.029 / -0.016` | `0.65%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.91 | ⚪ **CASH** | **+13.2 bps** (±4.0) | `+16.8 bps` | `+0.030 / +0.075` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 06:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,479.84 | ⚪ **CASH** | **+35.2 bps** (±16.9) | `+66.9 bps` | `+0.000 / +0.002` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,802.56 | ⚪ **CASH** | **+0.7 bps** (±2.5) | `+5.6 bps` | `-0.029 / -0.016` | `0.65%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.88 | ⚪ **CASH** | **+13.2 bps** (±4.0) | `+16.8 bps` | `+0.030 / +0.075` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 06:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,425.06 | ⚪ **CASH** | **+35.2 bps** (±16.9) | `+66.9 bps` | `+0.000 / +0.002` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,801.77 | ⚪ **CASH** | **+0.7 bps** (±2.5) | `+5.6 bps` | `-0.029 / -0.016` | `0.65%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.73 | ⚪ **CASH** | **+13.2 bps** (±4.0) | `+16.8 bps` | `+0.030 / +0.075` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 05:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,394.06 | ⚪ **CASH** | **+36.3 bps** (±16.9) | `+66.6 bps` | `+0.010 / +0.014` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,800.73 | ⚪ **CASH** | **+5.2 bps** (±4.6) | `+10.0 bps` | `-0.024 / +0.034` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 35.7 bps) |
| **SOLUSDT** | $74.63 | ⚪ **CASH** | **+23.3 bps** (±11.7) | `+30.5 bps` | `+0.044 / +0.140` | `0.72%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 05:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,450.93 | ⚪ **CASH** | **+36.3 bps** (±16.9) | `+66.6 bps` | `+0.010 / +0.014` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,799.63 | ⚪ **CASH** | **+5.2 bps** (±4.6) | `+10.0 bps` | `-0.024 / +0.034` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 35.7 bps) |
| **SOLUSDT** | $74.58 | ⚪ **CASH** | **+23.3 bps** (±11.7) | `+30.5 bps` | `+0.044 / +0.140` | `0.72%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 05:15:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,442.26 | ⚪ **CASH** | **+36.3 bps** (±16.9) | `+66.6 bps` | `+0.010 / +0.014` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,797.29 | ⚪ **CASH** | **+5.2 bps** (±4.6) | `+10.0 bps` | `-0.024 / +0.034` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 35.7 bps) |
| **SOLUSDT** | $74.50 | ⚪ **CASH** | **+23.3 bps** (±11.7) | `+30.5 bps` | `+0.044 / +0.140` | `0.72%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 05:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,531.03 | ⚪ **CASH** | **+36.3 bps** (±16.9) | `+66.6 bps` | `+0.010 / +0.014` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,798.55 | ⚪ **CASH** | **+5.2 bps** (±4.6) | `+10.0 bps` | `-0.024 / +0.034` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 35.7 bps) |
| **SOLUSDT** | $74.53 | ⚪ **CASH** | **+23.3 bps** (±11.7) | `+30.5 bps` | `+0.044 / +0.140` | `0.72%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 04:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,563.69 | ⚪ **CASH** | **+35.0 bps** (±15.8) | `+64.3 bps` | `+0.014 / +0.002` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,802.05 | ⚪ **CASH** | **+11.8 bps** (±6.7) | `+22.9 bps` | `-0.029 / +0.031` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.7 bps) |
| **SOLUSDT** | $74.70 | ⚪ **CASH** | **+12.9 bps** (±5.1) | `+15.2 bps` | `+0.025 / +0.091` | `0.73%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 04:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,370.74 | ⚪ **CASH** | **+35.0 bps** (±15.8) | `+64.3 bps` | `+0.014 / +0.002` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,796.99 | ⚪ **CASH** | **+11.8 bps** (±6.7) | `+22.9 bps` | `-0.029 / +0.031` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.7 bps) |
| **SOLUSDT** | $74.54 | ⚪ **CASH** | **+12.9 bps** (±5.1) | `+15.2 bps` | `+0.025 / +0.091` | `0.73%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 04:15:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,292.03 | ⚪ **CASH** | **+35.0 bps** (±15.8) | `+64.3 bps` | `+0.014 / +0.002` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,796.78 | ⚪ **CASH** | **+11.8 bps** (±6.7) | `+22.9 bps` | `-0.029 / +0.031` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.7 bps) |
| **SOLUSDT** | $74.27 | ⚪ **CASH** | **+12.9 bps** (±5.1) | `+15.2 bps` | `+0.025 / +0.091` | `0.73%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 04:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,274.51 | ⚪ **CASH** | **+35.0 bps** (±15.8) | `+64.3 bps` | `+0.014 / +0.002` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,797.52 | ⚪ **CASH** | **+11.8 bps** (±6.7) | `+22.9 bps` | `-0.029 / +0.031` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.7 bps) |
| **SOLUSDT** | $74.33 | ⚪ **CASH** | **+12.9 bps** (±5.1) | `+15.2 bps` | `+0.025 / +0.091` | `0.73%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 03:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,044.01 | ⚪ **CASH** | **+38.3 bps** (±12.1) | `+72.4 bps` | `+0.006 / -0.024` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,782.59 | ⚪ **CASH** | **+46.1 bps** (±11.1) | `+88.5 bps` | `-0.036 / +0.010` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $73.90 | ⚪ **CASH** | **+13.2 bps** (±6.5) | `+19.2 bps` | `+0.012 / +0.069` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-19 03:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,964.01 | ⚪ **CASH** | **+38.3 bps** (±12.1) | `+72.4 bps` | `+0.006 / -0.024` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,779.99 | ⚪ **CASH** | **+46.1 bps** (±11.1) | `+88.5 bps` | `-0.036 / +0.010` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $73.62 | ⚪ **CASH** | **+13.2 bps** (±6.5) | `+19.2 bps` | `+0.012 / +0.069` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
