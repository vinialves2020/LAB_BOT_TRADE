# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-18 06:00:52 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-18 06:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,640.32 | ⚪ **CASH** | **+4.9 bps** (±13.0) | `-7.0 bps` | `+0.108 / +0.036` | `0.53%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,810.58 | ⚪ **CASH** | **+21.4 bps** (±18.9) | `+47.3 bps` | `-0.074 / -0.044` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.07 | ⚪ **CASH** | **+6.6 bps** (±10.2) | `+22.1 bps` | `-0.072 / -0.098` | `0.73%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 05:45:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,708.00 | ⚪ **CASH** | **+12.0 bps** (±9.0) | `+6.5 bps` | `+0.095 / +0.045` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,813.00 | ⚪ **CASH** | **+19.7 bps** (±19.4) | `+45.3 bps` | `-0.078 / -0.046` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.21 | ⚪ **CASH** | **+9.0 bps** (±9.1) | `+29.3 bps` | `-0.083 / -0.120` | `0.74%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 05:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,772.01 | ⚪ **CASH** | **+12.0 bps** (±9.0) | `+6.5 bps` | `+0.095 / +0.045` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,815.85 | ⚪ **CASH** | **+19.7 bps** (±19.4) | `+45.3 bps` | `-0.078 / -0.046` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.48 | ⚪ **CASH** | **+9.0 bps** (±9.1) | `+29.3 bps` | `-0.083 / -0.120` | `0.74%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 05:15:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,646.00 | ⚪ **CASH** | **+12.0 bps** (±9.0) | `+6.5 bps` | `+0.095 / +0.045` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,809.22 | ⚪ **CASH** | **+19.7 bps** (±19.4) | `+45.3 bps` | `-0.078 / -0.046` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.14 | ⚪ **CASH** | **+9.0 bps** (±9.1) | `+29.3 bps` | `-0.083 / -0.120` | `0.74%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 05:00:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,367.43 | ⚪ **CASH** | **+12.0 bps** (±9.0) | `+6.5 bps` | `+0.095 / +0.045` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,801.68 | ⚪ **CASH** | **+19.7 bps** (±19.4) | `+45.3 bps` | `-0.078 / -0.046` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.83 | ⚪ **CASH** | **+9.0 bps** (±9.1) | `+29.3 bps` | `-0.083 / -0.120` | `0.74%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 04:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,338.95 | ⚪ **CASH** | **+25.1 bps** (±10.7) | `+28.3 bps` | `+0.090 / +0.094` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,799.98 | ⚪ **CASH** | **+23.1 bps** (±19.8) | `+50.5 bps` | `-0.083 / -0.018` | `0.69%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (19.8 bps > 19.5) |
| **SOLUSDT** | $74.81 | ⚪ **CASH** | **+10.3 bps** (±9.2) | `+27.4 bps` | `-0.073 / -0.064` | `0.75%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 04:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,553.50 | ⚪ **CASH** | **+25.1 bps** (±10.7) | `+28.3 bps` | `+0.090 / +0.094` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,808.26 | ⚪ **CASH** | **+23.1 bps** (±19.8) | `+50.5 bps` | `-0.083 / -0.018` | `0.69%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (19.8 bps > 19.5) |
| **SOLUSDT** | $75.03 | ⚪ **CASH** | **+10.3 bps** (±9.2) | `+27.4 bps` | `-0.073 / -0.064` | `0.75%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 04:15:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,442.26 | ⚪ **CASH** | **+25.1 bps** (±10.7) | `+28.3 bps` | `+0.090 / +0.094` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,806.05 | ⚪ **CASH** | **+23.1 bps** (±19.8) | `+50.5 bps` | `-0.083 / -0.018` | `0.69%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (19.8 bps > 19.5) |
| **SOLUSDT** | $74.86 | ⚪ **CASH** | **+10.3 bps** (±9.2) | `+27.4 bps` | `-0.073 / -0.064` | `0.75%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 04:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,392.15 | ⚪ **CASH** | **+25.1 bps** (±10.7) | `+28.3 bps` | `+0.090 / +0.094` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,803.01 | ⚪ **CASH** | **+23.1 bps** (±19.8) | `+50.5 bps` | `-0.083 / -0.018` | `0.69%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (19.8 bps > 19.5) |
| **SOLUSDT** | $74.68 | ⚪ **CASH** | **+10.3 bps** (±9.2) | `+27.4 bps` | `-0.073 / -0.064` | `0.75%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 03:45:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,505.81 | ⚪ **CASH** | **+17.1 bps** (±16.9) | `+15.3 bps` | `+0.094 / +0.075` | `0.55%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,806.44 | ⚪ **CASH** | **+30.0 bps** (±15.3) | `+59.5 bps` | `-0.078 / +0.013` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.95 | ⚪ **CASH** | **+8.3 bps** (±1.4) | `+17.9 bps` | `-0.066 / -0.010` | `0.76%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 03:30:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,540.52 | ⚪ **CASH** | **+17.1 bps** (±16.9) | `+15.3 bps` | `+0.094 / +0.075` | `0.55%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,807.42 | ⚪ **CASH** | **+30.0 bps** (±15.3) | `+59.5 bps` | `-0.078 / +0.013` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.03 | ⚪ **CASH** | **+8.3 bps** (±1.4) | `+17.9 bps` | `-0.066 / -0.010` | `0.76%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 03:15:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,419.86 | ⚪ **CASH** | **+17.1 bps** (±16.9) | `+15.3 bps` | `+0.094 / +0.075` | `0.55%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,806.12 | ⚪ **CASH** | **+30.0 bps** (±15.3) | `+59.5 bps` | `-0.078 / +0.013` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.73 | ⚪ **CASH** | **+8.3 bps** (±1.4) | `+17.9 bps` | `-0.066 / -0.010` | `0.76%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 03:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,422.50 | ⚪ **CASH** | **+17.1 bps** (±16.9) | `+15.3 bps` | `+0.094 / +0.075` | `0.55%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,806.05 | ⚪ **CASH** | **+30.0 bps** (±15.3) | `+59.5 bps` | `-0.078 / +0.013` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.69 | ⚪ **CASH** | **+8.3 bps** (±1.4) | `+17.9 bps` | `-0.066 / -0.010` | `0.76%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 02:45:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,300.00 | ⚪ **CASH** | **+17.0 bps** (±15.5) | `+13.4 bps` | `+0.094 / +0.098` | `0.61%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,801.87 | ⚪ **CASH** | **-0.8 bps** (±16.3) | `+7.7 bps` | `-0.082 / -0.041` | `0.77%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.38 | ⚪ **CASH** | **+16.6 bps** (±11.7) | `+38.9 bps` | `-0.074 / -0.061` | `0.84%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 02:30:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,546.87 | ⚪ **CASH** | **+17.0 bps** (±15.5) | `+13.4 bps` | `+0.094 / +0.098` | `0.61%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,809.01 | ⚪ **CASH** | **-0.8 bps** (±16.3) | `+7.7 bps` | `-0.082 / -0.041` | `0.77%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.77 | ⚪ **CASH** | **+16.6 bps** (±11.7) | `+38.9 bps` | `-0.074 / -0.061` | `0.84%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 02:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,302.64 | ⚪ **CASH** | **+17.0 bps** (±15.5) | `+13.4 bps` | `+0.094 / +0.098` | `0.61%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,801.58 | ⚪ **CASH** | **-0.8 bps** (±16.3) | `+7.7 bps` | `-0.082 / -0.041` | `0.77%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.38 | ⚪ **CASH** | **+16.6 bps** (±11.7) | `+38.9 bps` | `-0.074 / -0.061` | `0.84%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 02:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,347.72 | ⚪ **CASH** | **+17.0 bps** (±15.5) | `+13.4 bps` | `+0.094 / +0.098` | `0.61%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,803.59 | ⚪ **CASH** | **-0.8 bps** (±16.3) | `+7.7 bps` | `-0.082 / -0.041` | `0.77%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.26 | ⚪ **CASH** | **+16.6 bps** (±11.7) | `+38.9 bps` | `-0.074 / -0.061` | `0.84%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 01:45:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,476.49 | ⚪ **CASH** | **+6.3 bps** (±12.1) | `-8.7 bps` | `+0.100 / +0.116` | `0.60%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,809.17 | ⚪ **CASH** | **-16.6 bps** (±26.5) | `-21.1 bps` | `-0.079 / -0.020` | `0.77%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.5 bps > 19.5) |
| **SOLUSDT** | $74.48 | ⚪ **CASH** | **+14.7 bps** (±7.4) | `+34.5 bps` | `-0.081 / -0.051` | `0.84%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 01:30:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,538.77 | ⚪ **CASH** | **+6.3 bps** (±12.1) | `-8.7 bps` | `+0.100 / +0.116` | `0.60%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,809.46 | ⚪ **CASH** | **-16.6 bps** (±26.5) | `-21.1 bps` | `-0.079 / -0.020` | `0.77%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.5 bps > 19.5) |
| **SOLUSDT** | $74.37 | ⚪ **CASH** | **+14.7 bps** (±7.4) | `+34.5 bps` | `-0.081 / -0.051` | `0.84%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 01:15:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,655.51 | ⚪ **CASH** | **+6.3 bps** (±12.1) | `-8.7 bps` | `+0.100 / +0.116` | `0.60%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,815.43 | ⚪ **CASH** | **-16.6 bps** (±26.5) | `-21.1 bps` | `-0.079 / -0.020` | `0.77%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.5 bps > 19.5) |
| **SOLUSDT** | $74.79 | ⚪ **CASH** | **+14.7 bps** (±7.4) | `+34.5 bps` | `-0.081 / -0.051` | `0.84%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 01:01:02 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,684.13 | ⚪ **CASH** | **+6.3 bps** (±12.1) | `-8.7 bps` | `+0.100 / +0.116` | `0.60%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,817.10 | ⚪ **CASH** | **-16.6 bps** (±26.5) | `-21.1 bps` | `-0.079 / -0.020` | `0.77%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.5 bps > 19.5) |
| **SOLUSDT** | $74.81 | ⚪ **CASH** | **+14.7 bps** (±7.4) | `+34.5 bps` | `-0.081 / -0.051` | `0.84%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 00:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,698.70 | ⚪ **CASH** | **+0.6 bps** (±18.7) | `-18.3 bps` | `+0.102 / +0.120` | `0.62%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,817.39 | ⚪ **CASH** | **-15.9 bps** (±26.6) | `-20.2 bps` | `-0.083 / -0.011` | `0.78%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (26.6 bps > 19.5) |
| **SOLUSDT** | $75.08 | ⚪ **CASH** | **+25.1 bps** (±16.8) | `+54.9 bps` | `-0.084 / -0.046` | `0.85%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 00:30:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,839.32 | ⚪ **CASH** | **+0.6 bps** (±18.7) | `-18.3 bps` | `+0.102 / +0.120` | `0.62%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,821.68 | ⚪ **CASH** | **-15.9 bps** (±26.6) | `-20.2 bps` | `-0.083 / -0.011` | `0.78%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (26.6 bps > 19.5) |
| **SOLUSDT** | $75.35 | ⚪ **CASH** | **+25.1 bps** (±16.8) | `+54.9 bps` | `-0.084 / -0.046` | `0.85%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 00:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,884.42 | ⚪ **CASH** | **+0.6 bps** (±18.7) | `-18.3 bps` | `+0.102 / +0.120` | `0.62%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,821.89 | ⚪ **CASH** | **-15.9 bps** (±26.6) | `-20.2 bps` | `-0.083 / -0.011` | `0.78%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (26.6 bps > 19.5) |
| **SOLUSDT** | $74.94 | ⚪ **CASH** | **+25.1 bps** (±16.8) | `+54.9 bps` | `-0.084 / -0.046` | `0.85%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 00:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,926.75 | ⚪ **CASH** | **+0.6 bps** (±18.7) | `-18.3 bps` | `+0.102 / +0.120` | `0.62%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,825.31 | ⚪ **CASH** | **-15.9 bps** (±26.6) | `-20.2 bps` | `-0.083 / -0.011` | `0.78%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (26.6 bps > 19.5) |
| **SOLUSDT** | $75.20 | ⚪ **CASH** | **+25.1 bps** (±16.8) | `+54.9 bps` | `-0.084 / -0.046` | `0.85%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 23:45:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,940.97 | ⚪ **CASH** | **+2.2 bps** (±15.6) | `-13.6 bps` | `+0.093 / +0.102` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,823.71 | ⚪ **CASH** | **-43.6 bps** (±3.9) | `-73.1 bps` | `-0.092 / -0.015` | `0.79%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.97 | ⚪ **CASH** | **+12.1 bps** (±11.3) | `+30.9 bps` | `-0.095 / -0.033` | `0.83%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 23:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,006.77 | ⚪ **CASH** | **+2.2 bps** (±15.6) | `-13.6 bps` | `+0.093 / +0.102` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,824.04 | ⚪ **CASH** | **-43.6 bps** (±3.9) | `-73.1 bps` | `-0.092 / -0.015` | `0.79%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.09 | ⚪ **CASH** | **+12.1 bps** (±11.3) | `+30.9 bps` | `-0.095 / -0.033` | `0.83%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 23:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,085.87 | ⚪ **CASH** | **+2.2 bps** (±15.6) | `-13.6 bps` | `+0.093 / +0.102` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,827.20 | ⚪ **CASH** | **-43.6 bps** (±3.9) | `-73.1 bps` | `-0.092 / -0.015` | `0.79%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.20 | ⚪ **CASH** | **+12.1 bps** (±11.3) | `+30.9 bps` | `-0.095 / -0.033` | `0.83%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 23:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,749.77 | ⚪ **CASH** | **+2.2 bps** (±15.6) | `-13.6 bps` | `+0.093 / +0.102` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,815.71 | ⚪ **CASH** | **-43.6 bps** (±3.9) | `-73.1 bps` | `-0.092 / -0.015` | `0.79%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.01 | ⚪ **CASH** | **+12.1 bps** (±11.3) | `+30.9 bps` | `-0.095 / -0.033` | `0.83%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 22:45:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,833.54 | ⚪ **CASH** | **+12.5 bps** (±11.2) | `+7.8 bps` | `+0.082 / +0.075` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,815.88 | ⚪ **CASH** | **-36.4 bps** (±5.8) | `-57.6 bps` | `-0.095 / -0.036` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.02 | ⚪ **CASH** | **+7.7 bps** (±14.8) | `+25.0 bps` | `-0.102 / -0.036` | `0.84%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 22:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,674.96 | ⚪ **CASH** | **+12.5 bps** (±11.2) | `+7.8 bps` | `+0.082 / +0.075` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,811.73 | ⚪ **CASH** | **-36.4 bps** (±5.8) | `-57.6 bps` | `-0.095 / -0.036` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.92 | ⚪ **CASH** | **+7.7 bps** (±14.8) | `+25.0 bps` | `-0.102 / -0.036` | `0.84%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 22:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,448.61 | ⚪ **CASH** | **+12.5 bps** (±11.2) | `+7.8 bps` | `+0.082 / +0.075` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,805.64 | ⚪ **CASH** | **-36.4 bps** (±5.8) | `-57.6 bps` | `-0.095 / -0.036` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.67 | ⚪ **CASH** | **+7.7 bps** (±14.8) | `+25.0 bps` | `-0.102 / -0.036` | `0.84%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 22:01:05 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,299.40 | ⚪ **CASH** | **+12.5 bps** (±11.2) | `+7.8 bps` | `+0.082 / +0.075` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,803.38 | ⚪ **CASH** | **-36.4 bps** (±5.8) | `-57.6 bps` | `-0.095 / -0.036` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.40 | ⚪ **CASH** | **+7.7 bps** (±14.8) | `+25.0 bps` | `-0.102 / -0.036` | `0.84%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 21:45:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,373.39 | ⚪ **CASH** | **+9.6 bps** (±9.6) | `+3.7 bps` | `+0.087 / +0.040` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.2 bps) |
| **ETHUSDT** | $1,808.01 | ⚪ **CASH** | **-26.3 bps** (±15.4) | `-34.0 bps` | `-0.102 / -0.081` | `0.82%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.3 bps) |
| **SOLUSDT** | $73.54 | ⚪ **CASH** | **+15.0 bps** (±6.0) | `+42.0 bps` | `-0.104 / -0.117` | `0.85%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 21:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,598.48 | ⚪ **CASH** | **+9.6 bps** (±9.6) | `+3.7 bps` | `+0.087 / +0.040` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.2 bps) |
| **ETHUSDT** | $1,816.77 | ⚪ **CASH** | **-26.3 bps** (±15.4) | `-34.0 bps` | `-0.102 / -0.081` | `0.82%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.3 bps) |
| **SOLUSDT** | $73.97 | ⚪ **CASH** | **+15.0 bps** (±6.0) | `+42.0 bps` | `-0.104 / -0.117` | `0.85%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 21:15:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,051.13 | ⚪ **CASH** | **+9.6 bps** (±9.6) | `+3.7 bps` | `+0.087 / +0.040` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.2 bps) |
| **ETHUSDT** | $1,797.58 | ⚪ **CASH** | **-26.3 bps** (±15.4) | `-34.0 bps` | `-0.102 / -0.081` | `0.82%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.3 bps) |
| **SOLUSDT** | $73.12 | ⚪ **CASH** | **+15.0 bps** (±6.0) | `+42.0 bps` | `-0.104 / -0.117` | `0.85%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
