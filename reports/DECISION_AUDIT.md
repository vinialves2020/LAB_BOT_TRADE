# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-18 13:00:53 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-18 13:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,060.10 | ⚪ **CASH** | **+24.1 bps** (±16.5) | `+40.4 bps` | `+0.048 / -0.010` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,795.11 | ⚪ **CASH** | **+16.9 bps** (±10.2) | `+38.0 bps` | `-0.059 / -0.032` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.29 | ⚪ **CASH** | **+19.8 bps** (±6.7) | `+38.0 bps` | `-0.049 / +0.024` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 12:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,066.62 | ⚪ **CASH** | **+25.7 bps** (±17.6) | `+46.3 bps` | `+0.046 / -0.048` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,793.54 | ⚪ **CASH** | **+10.3 bps** (±11.3) | `+31.6 bps` | `-0.061 / -0.109` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.25 | ⚪ **CASH** | **+17.8 bps** (±4.7) | `+30.9 bps` | `-0.044 / +0.067` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 12:31:00 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,239.60 | ⚪ **CASH** | **+25.7 bps** (±17.6) | `+46.3 bps` | `+0.046 / -0.048` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,799.99 | ⚪ **CASH** | **+10.3 bps** (±11.3) | `+31.6 bps` | `-0.061 / -0.109` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.40 | ⚪ **CASH** | **+17.8 bps** (±4.7) | `+30.9 bps` | `-0.044 / +0.067` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 12:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,255.32 | ⚪ **CASH** | **+25.7 bps** (±17.6) | `+46.3 bps` | `+0.046 / -0.048` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,801.98 | ⚪ **CASH** | **+10.3 bps** (±11.3) | `+31.6 bps` | `-0.061 / -0.109` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.60 | ⚪ **CASH** | **+17.8 bps** (±4.7) | `+30.9 bps` | `-0.044 / +0.067` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 12:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,171.21 | ⚪ **CASH** | **+25.7 bps** (±17.6) | `+46.3 bps` | `+0.046 / -0.048` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,798.72 | ⚪ **CASH** | **+10.3 bps** (±11.3) | `+31.6 bps` | `-0.061 / -0.109` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.36 | ⚪ **CASH** | **+17.8 bps** (±4.7) | `+30.9 bps` | `-0.044 / +0.067` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 11:45:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,174.87 | ⚪ **CASH** | **+33.2 bps** (±14.4) | `+52.7 bps` | `+0.062 / +0.019` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,799.00 | ⚪ **CASH** | **+17.0 bps** (±8.1) | `+37.0 bps` | `-0.052 / -0.040` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.45 | ⚪ **CASH** | **+8.7 bps** (±5.8) | `+12.1 bps` | `-0.043 / +0.092` | `0.71%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 11:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,185.92 | ⚪ **CASH** | **+33.2 bps** (±14.4) | `+52.7 bps` | `+0.062 / +0.019` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,797.89 | ⚪ **CASH** | **+17.0 bps** (±8.1) | `+37.0 bps` | `-0.052 / -0.040` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.54 | ⚪ **CASH** | **+8.7 bps** (±5.8) | `+12.1 bps` | `-0.043 / +0.092` | `0.71%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 11:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,212.49 | ⚪ **CASH** | **+33.2 bps** (±14.4) | `+52.7 bps` | `+0.062 / +0.019` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,799.47 | ⚪ **CASH** | **+17.0 bps** (±8.1) | `+37.0 bps` | `-0.052 / -0.040` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.45 | ⚪ **CASH** | **+8.7 bps** (±5.8) | `+12.1 bps` | `-0.043 / +0.092` | `0.71%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 11:01:00 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,325.67 | ⚪ **CASH** | **+33.2 bps** (±14.4) | `+52.7 bps` | `+0.062 / +0.019` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,805.05 | ⚪ **CASH** | **+17.0 bps** (±8.1) | `+37.0 bps` | `-0.052 / -0.040` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.64 | ⚪ **CASH** | **+8.7 bps** (±5.8) | `+12.1 bps` | `-0.043 / +0.092` | `0.71%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 10:45:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,290.30 | ⚪ **CASH** | **+35.6 bps** (±18.3) | `+56.4 bps` | `+0.061 / +0.040` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,802.97 | ⚪ **CASH** | **+11.3 bps** (±10.2) | `+30.3 bps` | `-0.070 / -0.063` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.64 | ⚪ **CASH** | **+6.8 bps** (±8.9) | `+10.2 bps` | `-0.044 / +0.078` | `0.71%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 10:31:03 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,302.13 | ⚪ **CASH** | **+35.6 bps** (±18.3) | `+56.4 bps` | `+0.061 / +0.040` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,802.60 | ⚪ **CASH** | **+11.3 bps** (±10.2) | `+30.3 bps` | `-0.070 / -0.063` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.50 | ⚪ **CASH** | **+6.8 bps** (±8.9) | `+10.2 bps` | `-0.044 / +0.078` | `0.71%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 10:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,598.97 | ⚪ **CASH** | **+35.6 bps** (±18.3) | `+56.4 bps` | `+0.061 / +0.040` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,811.74 | ⚪ **CASH** | **+11.3 bps** (±10.2) | `+30.3 bps` | `-0.070 / -0.063` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.07 | ⚪ **CASH** | **+6.8 bps** (±8.9) | `+10.2 bps` | `-0.044 / +0.078` | `0.71%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 10:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,630.90 | ⚪ **CASH** | **+35.6 bps** (±18.3) | `+56.4 bps` | `+0.061 / +0.040` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,813.45 | ⚪ **CASH** | **+11.3 bps** (±10.2) | `+30.3 bps` | `-0.070 / -0.063` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.22 | ⚪ **CASH** | **+6.8 bps** (±8.9) | `+10.2 bps` | `-0.044 / +0.078` | `0.71%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 09:45:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,638.53 | ⚪ **CASH** | **+15.6 bps** (±13.9) | `+16.2 bps` | `+0.086 / +0.033` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,813.01 | ⚪ **CASH** | **+2.3 bps** (±15.9) | `+16.5 bps` | `-0.077 / -0.093` | `0.64%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.97 | ⚪ **CASH** | **+6.5 bps** (±6.6) | `+13.1 bps` | `-0.049 / +0.010` | `0.72%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 09:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,698.01 | ⚪ **CASH** | **+15.6 bps** (±13.9) | `+16.2 bps` | `+0.086 / +0.033` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,813.73 | ⚪ **CASH** | **+2.3 bps** (±15.9) | `+16.5 bps` | `-0.077 / -0.093` | `0.64%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.88 | ⚪ **CASH** | **+6.5 bps** (±6.6) | `+13.1 bps` | `-0.049 / +0.010` | `0.72%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 09:15:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,707.95 | ⚪ **CASH** | **+15.6 bps** (±13.9) | `+16.2 bps` | `+0.086 / +0.033` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,812.11 | ⚪ **CASH** | **+2.3 bps** (±15.9) | `+16.5 bps` | `-0.077 / -0.093` | `0.64%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.87 | ⚪ **CASH** | **+6.5 bps** (±6.6) | `+13.1 bps` | `-0.049 / +0.010` | `0.72%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 09:01:03 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,721.55 | ⚪ **CASH** | **+15.6 bps** (±13.9) | `+16.2 bps` | `+0.086 / +0.033` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,813.40 | ⚪ **CASH** | **+2.3 bps** (±15.9) | `+16.5 bps` | `-0.077 / -0.093` | `0.64%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.87 | ⚪ **CASH** | **+6.5 bps** (±6.6) | `+13.1 bps` | `-0.049 / +0.010` | `0.72%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 08:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,790.00 | ⚪ **CASH** | **-11.1 bps** (±9.3) | `-36.9 bps` | `+0.108 / +0.037` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,814.54 | ⚪ **CASH** | **+2.7 bps** (±21.2) | `+15.9 bps` | `-0.080 / -0.070` | `0.65%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.2 bps > 19.5) |
| **SOLUSDT** | $74.88 | ⚪ **CASH** | **+0.4 bps** (±9.6) | `+2.1 bps` | `-0.053 / +0.005` | `0.73%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 08:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,790.00 | ⚪ **CASH** | **-11.1 bps** (±9.3) | `-36.9 bps` | `+0.108 / +0.037` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,813.18 | ⚪ **CASH** | **+2.7 bps** (±21.2) | `+15.9 bps` | `-0.080 / -0.070` | `0.65%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.2 bps > 19.5) |
| **SOLUSDT** | $74.96 | ⚪ **CASH** | **+0.4 bps** (±9.6) | `+2.1 bps` | `-0.053 / +0.005` | `0.73%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 08:15:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,619.99 | ⚪ **CASH** | **-11.1 bps** (±9.3) | `-36.9 bps` | `+0.108 / +0.037` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,809.43 | ⚪ **CASH** | **+2.7 bps** (±21.2) | `+15.9 bps` | `-0.080 / -0.070` | `0.65%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.2 bps > 19.5) |
| **SOLUSDT** | $74.87 | ⚪ **CASH** | **+0.4 bps** (±9.6) | `+2.1 bps` | `-0.053 / +0.005` | `0.73%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 08:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,826.00 | ⚪ **CASH** | **-11.1 bps** (±9.3) | `-36.9 bps` | `+0.108 / +0.037` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,815.64 | ⚪ **CASH** | **+2.7 bps** (±21.2) | `+15.9 bps` | `-0.080 / -0.070` | `0.65%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.2 bps > 19.5) |
| **SOLUSDT** | $75.13 | ⚪ **CASH** | **+0.4 bps** (±9.6) | `+2.1 bps` | `-0.053 / +0.005` | `0.73%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 07:45:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,604.00 | ⚪ **CASH** | **+0.8 bps** (±10.1) | `-15.8 bps` | `+0.113 / +0.036` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,810.92 | ⚪ **CASH** | **+16.3 bps** (±20.4) | `+44.6 bps` | `-0.086 / -0.129` | `0.66%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.4 bps > 19.5) |
| **SOLUSDT** | $74.94 | ⚪ **CASH** | **+2.3 bps** (±5.2) | `+9.4 bps` | `-0.063 / -0.055` | `0.73%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 07:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,726.56 | ⚪ **CASH** | **+0.8 bps** (±10.1) | `-15.8 bps` | `+0.113 / +0.036` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,814.40 | ⚪ **CASH** | **+16.3 bps** (±20.4) | `+44.6 bps` | `-0.086 / -0.129` | `0.66%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.4 bps > 19.5) |
| **SOLUSDT** | $75.07 | ⚪ **CASH** | **+2.3 bps** (±5.2) | `+9.4 bps` | `-0.063 / -0.055` | `0.73%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 07:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,800.00 | ⚪ **CASH** | **+0.8 bps** (±10.1) | `-15.8 bps` | `+0.113 / +0.036` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,818.14 | ⚪ **CASH** | **+16.3 bps** (±20.4) | `+44.6 bps` | `-0.086 / -0.129` | `0.66%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.4 bps > 19.5) |
| **SOLUSDT** | $75.28 | ⚪ **CASH** | **+2.3 bps** (±5.2) | `+9.4 bps` | `-0.063 / -0.055` | `0.73%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 07:00:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,608.01 | ⚪ **CASH** | **+0.8 bps** (±10.1) | `-15.8 bps` | `+0.113 / +0.036` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,809.44 | ⚪ **CASH** | **+16.3 bps** (±20.4) | `+44.6 bps` | `-0.086 / -0.129` | `0.66%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.4 bps > 19.5) |
| **SOLUSDT** | $74.70 | ⚪ **CASH** | **+2.3 bps** (±5.2) | `+9.4 bps` | `-0.063 / -0.055` | `0.73%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 06:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,650.00 | ⚪ **CASH** | **+4.9 bps** (±13.0) | `-7.0 bps` | `+0.108 / +0.036` | `0.53%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,812.60 | ⚪ **CASH** | **+21.4 bps** (±18.9) | `+47.3 bps` | `-0.074 / -0.044` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.86 | ⚪ **CASH** | **+6.6 bps** (±10.2) | `+22.1 bps` | `-0.072 / -0.098` | `0.73%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 06:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,638.00 | ⚪ **CASH** | **+4.9 bps** (±13.0) | `-7.0 bps` | `+0.108 / +0.036` | `0.53%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,811.63 | ⚪ **CASH** | **+21.4 bps** (±18.9) | `+47.3 bps` | `-0.074 / -0.044` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.95 | ⚪ **CASH** | **+6.6 bps** (±10.2) | `+22.1 bps` | `-0.072 / -0.098` | `0.73%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 06:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,678.00 | ⚪ **CASH** | **+4.9 bps** (±13.0) | `-7.0 bps` | `+0.108 / +0.036` | `0.53%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,812.48 | ⚪ **CASH** | **+21.4 bps** (±18.9) | `+47.3 bps` | `-0.074 / -0.044` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.01 | ⚪ **CASH** | **+6.6 bps** (±10.2) | `+22.1 bps` | `-0.072 / -0.098` | `0.73%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

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
