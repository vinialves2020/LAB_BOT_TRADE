# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-11 17:45:47 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-11-11 12:31:04 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,936.01 | ⚪ **CASH** | **+19.5 bps** (±7.0) | `+30.5 bps` | `+0.020 / +0.049` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,054.17 | ⚪ **CASH** | **-28.0 bps** (±3.6) | `-42.5 bps` | `-0.072 / -0.026` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.79 | ⚪ **CASH** | **+14.8 bps** (±7.7) | `+18.2 bps` | `+0.006 / +0.130` | `0.68%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 12:16:01 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,960.01 | ⚪ **CASH** | **+19.5 bps** (±7.0) | `+30.5 bps` | `+0.020 / +0.049` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,054.88 | ⚪ **CASH** | **-28.0 bps** (±3.6) | `-42.5 bps` | `-0.072 / -0.026` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.79 | ⚪ **CASH** | **+14.8 bps** (±7.7) | `+18.2 bps` | `+0.006 / +0.130` | `0.68%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 12:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,938.01 | ⚪ **CASH** | **+19.5 bps** (±7.0) | `+30.5 bps` | `+0.020 / +0.049` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,055.01 | ⚪ **CASH** | **-28.0 bps** (±3.6) | `-42.5 bps` | `-0.072 / -0.026` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.89 | ⚪ **CASH** | **+14.8 bps** (±7.7) | `+18.2 bps` | `+0.006 / +0.130` | `0.68%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 11:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,032.00 | ⚪ **CASH** | **+19.4 bps** (±7.2) | `+28.9 bps` | `+0.028 / +0.056` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,056.81 | ⚪ **CASH** | **+7.6 bps** (±11.9) | `+21.4 bps` | `-0.065 / -0.008` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.93 | ⚪ **CASH** | **+12.6 bps** (±7.8) | `+13.7 bps` | `+0.008 / +0.131` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 11:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,054.00 | ⚪ **CASH** | **+19.4 bps** (±7.2) | `+28.9 bps` | `+0.028 / +0.056` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,059.51 | ⚪ **CASH** | **+7.6 bps** (±11.9) | `+21.4 bps` | `-0.065 / -0.008` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.97 | ⚪ **CASH** | **+12.6 bps** (±7.8) | `+13.7 bps` | `+0.008 / +0.131` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 11:15:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,063.12 | ⚪ **CASH** | **+19.4 bps** (±7.2) | `+28.9 bps` | `+0.028 / +0.056` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,062.53 | ⚪ **CASH** | **+7.6 bps** (±11.9) | `+21.4 bps` | `-0.065 / -0.008` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.94 | ⚪ **CASH** | **+12.6 bps** (±7.8) | `+13.7 bps` | `+0.008 / +0.131` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 11:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,000.01 | ⚪ **CASH** | **+19.4 bps** (±7.2) | `+28.9 bps` | `+0.028 / +0.056` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,058.69 | ⚪ **CASH** | **+7.6 bps** (±11.9) | `+21.4 bps` | `-0.065 / -0.008` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.79 | ⚪ **CASH** | **+12.6 bps** (±7.8) | `+13.7 bps` | `+0.008 / +0.131` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 10:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,006.80 | ⚪ **CASH** | **+24.6 bps** (±8.1) | `+39.0 bps` | `+0.023 / +0.058` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,060.32 | ⚪ **CASH** | **+1.8 bps** (±8.6) | `+12.4 bps` | `-0.066 / -0.035` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.84 | ⚪ **CASH** | **+5.9 bps** (±7.8) | `+10.5 bps` | `-0.013 / +0.025` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 10:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,034.01 | ⚪ **CASH** | **+24.6 bps** (±8.1) | `+39.0 bps` | `+0.023 / +0.058` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,063.01 | ⚪ **CASH** | **+1.8 bps** (±8.6) | `+12.4 bps` | `-0.066 / -0.035` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.95 | ⚪ **CASH** | **+5.9 bps** (±7.8) | `+10.5 bps` | `-0.013 / +0.025` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 10:15:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,722.66 | ⚪ **CASH** | **+24.6 bps** (±8.1) | `+39.0 bps` | `+0.023 / +0.058` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,055.00 | ⚪ **CASH** | **+1.8 bps** (±8.6) | `+12.4 bps` | `-0.066 / -0.035` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.43 | ⚪ **CASH** | **+5.9 bps** (±7.8) | `+10.5 bps` | `-0.013 / +0.025` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 10:00:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,842.01 | ⚪ **CASH** | **+24.6 bps** (±8.1) | `+39.0 bps` | `+0.023 / +0.058` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,059.61 | ⚪ **CASH** | **+1.8 bps** (±8.6) | `+12.4 bps` | `-0.066 / -0.035` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.64 | ⚪ **CASH** | **+5.9 bps** (±7.8) | `+10.5 bps` | `-0.013 / +0.025` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 09:45:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,655.66 | ⚪ **CASH** | **+26.2 bps** (±6.4) | `+40.1 bps` | `+0.027 / +0.072` | `0.47%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,052.37 | ⚪ **CASH** | **+2.9 bps** (±8.3) | `+12.9 bps` | `-0.067 / -0.014` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.32 | ⚪ **CASH** | **+7.8 bps** (±5.9) | `+19.6 bps` | `-0.039 / -0.029` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 09:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,756.15 | ⚪ **CASH** | **+26.2 bps** (±6.4) | `+40.1 bps` | `+0.027 / +0.072` | `0.47%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,056.88 | ⚪ **CASH** | **+2.9 bps** (±8.3) | `+12.9 bps` | `-0.067 / -0.014` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.24 | ⚪ **CASH** | **+7.8 bps** (±5.9) | `+19.6 bps` | `-0.039 / -0.029` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 09:15:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,650.00 | ⚪ **CASH** | **+26.2 bps** (±6.4) | `+40.1 bps` | `+0.027 / +0.072` | `0.47%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,054.11 | ⚪ **CASH** | **+2.9 bps** (±8.3) | `+12.9 bps` | `-0.067 / -0.014` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.87 | ⚪ **CASH** | **+7.8 bps** (±5.9) | `+19.6 bps` | `-0.039 / -0.029` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-11 09:00:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,731.25 | ⚪ **CASH** | **+26.2 bps** (±6.4) | `+40.1 bps` | `+0.027 / +0.072` | `0.47%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,059.17 | ⚪ **CASH** | **+2.9 bps** (±8.3) | `+12.9 bps` | `-0.067 / -0.014` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.01 | ⚪ **CASH** | **+7.8 bps** (±5.9) | `+19.6 bps` | `-0.039 / -0.029` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
