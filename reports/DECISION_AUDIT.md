# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-11 22:00:51 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-11-11 18:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,533.06 | ⚪ **CASH** | **+5.9 bps** (±6.1) | `+5.6 bps` | `+0.040 / +0.004` | `0.44%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,092.01 | ⚪ **CASH** | **+42.8 bps** (±15.2) | `+69.5 bps` | `+0.012 / +0.121` | `0.67%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $85.38 | ⚪ **CASH** | **+18.9 bps** (±10.6) | `+18.0 bps` | `+0.088 / +0.119` | `0.68%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 17:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,574.64 | ⚪ **CASH** | **+4.9 bps** (±7.3) | `+5.1 bps` | `+0.042 / -0.016` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,093.31 | ⚪ **CASH** | **+40.5 bps** (±13.1) | `+69.1 bps` | `-0.007 / +0.084` | `0.67%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $85.58 | ⚪ **CASH** | **+16.7 bps** (±10.6) | `+18.1 bps` | `+0.067 / +0.084` | `0.68%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 17:30:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,495.44 | ⚪ **CASH** | **+4.9 bps** (±7.3) | `+5.1 bps` | `+0.042 / -0.016` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,093.31 | ⚪ **CASH** | **+40.5 bps** (±13.1) | `+69.1 bps` | `-0.007 / +0.084` | `0.67%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $85.43 | ⚪ **CASH** | **+16.7 bps** (±10.6) | `+18.1 bps` | `+0.067 / +0.084` | `0.68%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 17:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,345.13 | ⚪ **CASH** | **+4.9 bps** (±7.3) | `+5.1 bps` | `+0.042 / -0.016` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,084.88 | ⚪ **CASH** | **+40.5 bps** (±13.1) | `+69.1 bps` | `-0.007 / +0.084` | `0.67%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $85.09 | ⚪ **CASH** | **+16.7 bps** (±10.6) | `+18.1 bps` | `+0.067 / +0.084` | `0.68%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 17:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,269.81 | ⚪ **CASH** | **+4.9 bps** (±7.3) | `+5.1 bps` | `+0.042 / -0.016` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,077.81 | ⚪ **CASH** | **+40.5 bps** (±13.1) | `+69.1 bps` | `-0.007 / +0.084` | `0.67%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $84.95 | ⚪ **CASH** | **+16.7 bps** (±10.6) | `+18.1 bps` | `+0.067 / +0.084` | `0.68%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 16:45:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,227.43 | ⚪ **CASH** | **+3.7 bps** (±6.8) | `+4.6 bps` | `+0.033 / -0.022` | `0.45%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,074.20 | ⚪ **CASH** | **+54.7 bps** (±14.1) | `+101.5 bps` | `-0.045 / +0.050` | `0.68%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $84.60 | ⚪ **CASH** | **+21.4 bps** (±17.2) | `+24.3 bps` | `+0.069 / +0.143` | `0.69%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 16:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,356.18 | ⚪ **CASH** | **+3.7 bps** (±6.8) | `+4.6 bps` | `+0.033 / -0.022` | `0.45%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,080.81 | ⚪ **CASH** | **+54.7 bps** (±14.1) | `+101.5 bps` | `-0.045 / +0.050` | `0.68%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $84.97 | ⚪ **CASH** | **+21.4 bps** (±17.2) | `+24.3 bps` | `+0.069 / +0.143` | `0.69%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 16:15:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,251.62 | ⚪ **CASH** | **+3.7 bps** (±6.8) | `+4.6 bps` | `+0.033 / -0.022` | `0.45%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,080.71 | ⚪ **CASH** | **+54.7 bps** (±14.1) | `+101.5 bps` | `-0.045 / +0.050` | `0.68%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $84.98 | ⚪ **CASH** | **+21.4 bps** (±17.2) | `+24.3 bps` | `+0.069 / +0.143` | `0.69%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 16:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,008.01 | ⚪ **CASH** | **+3.7 bps** (±6.8) | `+4.6 bps` | `+0.033 / -0.022` | `0.45%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,075.46 | ⚪ **CASH** | **+54.7 bps** (±14.1) | `+101.5 bps` | `-0.045 / +0.050` | `0.68%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $84.80 | ⚪ **CASH** | **+21.4 bps** (±17.2) | `+24.3 bps` | `+0.069 / +0.143` | `0.69%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 15:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,961.99 | ⚪ **CASH** | **+9.9 bps** (±8.0) | `+24.1 bps` | `+0.009 / -0.091` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,073.67 | ⚪ **CASH** | **-14.7 bps** (±15.4) | `-12.8 bps` | `-0.075 / -0.066` | `0.66%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.86 | ⚪ **CASH** | **+22.0 bps** (±15.8) | `+28.0 bps` | `+0.045 / +0.154` | `0.68%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 15:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,680.01 | ⚪ **CASH** | **+9.9 bps** (±8.0) | `+24.1 bps` | `+0.009 / -0.091` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,061.12 | ⚪ **CASH** | **-14.7 bps** (±15.4) | `-12.8 bps` | `-0.075 / -0.066` | `0.66%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.12 | ⚪ **CASH** | **+22.0 bps** (±15.8) | `+28.0 bps` | `+0.045 / +0.154` | `0.68%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 15:15:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,549.01 | ⚪ **CASH** | **+9.9 bps** (±8.0) | `+24.1 bps` | `+0.009 / -0.091` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,058.40 | ⚪ **CASH** | **-14.7 bps** (±15.4) | `-12.8 bps` | `-0.075 / -0.066` | `0.66%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.97 | ⚪ **CASH** | **+22.0 bps** (±15.8) | `+28.0 bps` | `+0.045 / +0.154` | `0.68%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 15:01:00 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,550.00 | ⚪ **CASH** | **+9.9 bps** (±8.0) | `+24.1 bps` | `+0.009 / -0.091` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,054.51 | ⚪ **CASH** | **-14.7 bps** (±15.4) | `-12.8 bps` | `-0.075 / -0.066` | `0.66%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.94 | ⚪ **CASH** | **+22.0 bps** (±15.8) | `+28.0 bps` | `+0.045 / +0.154` | `0.68%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 14:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,586.01 | ⚪ **CASH** | **+12.8 bps** (±5.4) | `+22.2 bps` | `+0.021 / -0.017` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,053.96 | ⚪ **CASH** | **-29.7 bps** (±3.8) | `-42.1 bps` | `-0.074 / -0.078` | `0.67%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.17 | ⚪ **CASH** | **+21.1 bps** (±15.9) | `+27.1 bps` | `+0.016 / +0.177` | `0.68%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 14:30:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,650.01 | ⚪ **CASH** | **+12.8 bps** (±5.4) | `+22.2 bps` | `+0.021 / -0.017` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,055.14 | ⚪ **CASH** | **-29.7 bps** (±3.8) | `-42.1 bps` | `-0.074 / -0.078` | `0.67%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.31 | ⚪ **CASH** | **+21.1 bps** (±15.9) | `+27.1 bps` | `+0.016 / +0.177` | `0.68%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 14:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,698.47 | ⚪ **CASH** | **+12.8 bps** (±5.4) | `+22.2 bps` | `+0.021 / -0.017` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,050.52 | ⚪ **CASH** | **-29.7 bps** (±3.8) | `-42.1 bps` | `-0.074 / -0.078` | `0.67%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.08 | ⚪ **CASH** | **+21.1 bps** (±15.9) | `+27.1 bps` | `+0.016 / +0.177` | `0.68%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 14:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,842.00 | ⚪ **CASH** | **+12.8 bps** (±5.4) | `+22.2 bps` | `+0.021 / -0.017` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,059.51 | ⚪ **CASH** | **-29.7 bps** (±3.8) | `-42.1 bps` | `-0.074 / -0.078` | `0.67%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.68 | ⚪ **CASH** | **+21.1 bps** (±15.9) | `+27.1 bps` | `+0.016 / +0.177` | `0.68%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 13:45:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,770.01 | ⚪ **CASH** | **+19.9 bps** (±5.9) | `+31.1 bps` | `+0.019 / +0.051` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,051.66 | ⚪ **CASH** | **+0.5 bps** (±13.8) | `+12.0 bps` | `-0.070 / -0.040` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.30 | ⚪ **CASH** | **+20.1 bps** (±16.6) | `+28.3 bps` | `+0.005 / +0.150` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 13:30:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,814.00 | ⚪ **CASH** | **+19.9 bps** (±5.9) | `+31.1 bps` | `+0.019 / +0.051` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,053.47 | ⚪ **CASH** | **+0.5 bps** (±13.8) | `+12.0 bps` | `-0.070 / -0.040` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.11 | ⚪ **CASH** | **+20.1 bps** (±16.6) | `+28.3 bps` | `+0.005 / +0.150` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 13:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,966.01 | ⚪ **CASH** | **+19.9 bps** (±5.9) | `+31.1 bps` | `+0.019 / +0.051` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,055.29 | ⚪ **CASH** | **+0.5 bps** (±13.8) | `+12.0 bps` | `-0.070 / -0.040` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.19 | ⚪ **CASH** | **+20.1 bps** (±16.6) | `+28.3 bps` | `+0.005 / +0.150` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 13:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,873.23 | ⚪ **CASH** | **+19.9 bps** (±5.9) | `+31.1 bps` | `+0.019 / +0.051` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,051.71 | ⚪ **CASH** | **+0.5 bps** (±13.8) | `+12.0 bps` | `-0.070 / -0.040` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.87 | ⚪ **CASH** | **+20.1 bps** (±16.6) | `+28.3 bps` | `+0.005 / +0.150` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 12:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,012.00 | ⚪ **CASH** | **+19.5 bps** (±7.0) | `+30.5 bps` | `+0.020 / +0.049` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,056.05 | ⚪ **CASH** | **-28.0 bps** (±3.6) | `-42.5 bps` | `-0.072 / -0.026` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.95 | ⚪ **CASH** | **+14.8 bps** (±7.7) | `+18.2 bps` | `+0.006 / +0.130` | `0.68%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
