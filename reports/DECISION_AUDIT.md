# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-21 15:46:59 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-21 15:46:59 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,468.01 | ⚪ **CASH** | **+3.6 bps** (±15.7) | `-8.4 bps` | `+0.073 / +0.107` | `0.33%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,512.82 | ⚪ **CASH** | **+30.4 bps** (±10.4) | `+54.5 bps` | `+0.007 / -0.024` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $108.56 | ⚪ **CASH** | **-1.7 bps** (±4.8) | `-14.0 bps` | `+0.053 / +0.045` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 15:32:09 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,527.72 | ⚪ **CASH** | **+3.6 bps** (±15.7) | `-8.4 bps` | `+0.073 / +0.107` | `0.33%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,508.00 | ⚪ **CASH** | **+30.4 bps** (±10.4) | `+54.5 bps` | `+0.007 / -0.024` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $108.67 | ⚪ **CASH** | **-1.7 bps** (±4.8) | `-14.0 bps` | `+0.053 / +0.045` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 15:17:08 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,598.06 | ⚪ **CASH** | **+3.6 bps** (±15.7) | `-8.4 bps` | `+0.073 / +0.107` | `0.33%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,505.13 | ⚪ **CASH** | **+30.4 bps** (±10.4) | `+54.5 bps` | `+0.007 / -0.024` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $108.03 | ⚪ **CASH** | **-1.7 bps** (±4.8) | `-14.0 bps` | `+0.053 / +0.045` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 15:02:16 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,551.54 | ⚪ **CASH** | **+3.6 bps** (±15.7) | `-8.4 bps` | `+0.073 / +0.107` | `0.33%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,499.59 | ⚪ **CASH** | **+30.4 bps** (±10.4) | `+54.5 bps` | `+0.007 / -0.024` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $107.71 | ⚪ **CASH** | **-1.7 bps** (±4.8) | `-14.0 bps` | `+0.053 / +0.045` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 14:47:09 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,209.70 | ⚪ **CASH** | **+8.1 bps** (±3.1) | `+4.7 bps` | `+0.041 / +0.069` | `0.30%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,481.71 | ⚪ **CASH** | **+24.0 bps** (±16.6) | `+45.8 bps` | `+0.022 / -0.049` | `0.50%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $107.35 | ⚪ **CASH** | **-12.8 bps** (±2.8) | `-27.1 bps` | `+0.028 / -0.006` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 14:32:17 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,962.43 | ⚪ **CASH** | **+8.1 bps** (±3.1) | `+4.7 bps` | `+0.041 / +0.069` | `0.30%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,473.84 | ⚪ **CASH** | **+24.0 bps** (±16.6) | `+45.8 bps` | `+0.022 / -0.049` | `0.50%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $106.90 | ⚪ **CASH** | **-12.8 bps** (±2.8) | `-27.1 bps` | `+0.028 / -0.006` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 14:16:55 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,843.40 | ⚪ **CASH** | **+8.1 bps** (±3.1) | `+4.7 bps` | `+0.041 / +0.069` | `0.30%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,468.08 | ⚪ **CASH** | **+24.0 bps** (±16.6) | `+45.8 bps` | `+0.022 / -0.049` | `0.50%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $106.56 | ⚪ **CASH** | **-12.8 bps** (±2.8) | `-27.1 bps` | `+0.028 / -0.006` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 14:02:14 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,718.00 | ⚪ **CASH** | **+8.1 bps** (±3.1) | `+4.7 bps` | `+0.041 / +0.069` | `0.30%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,469.45 | ⚪ **CASH** | **+24.0 bps** (±16.6) | `+45.8 bps` | `+0.022 / -0.049` | `0.50%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $106.51 | ⚪ **CASH** | **-12.8 bps** (±2.8) | `-27.1 bps` | `+0.028 / -0.006` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 13:47:11 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,618.00 | ⚪ **CASH** | **+5.1 bps** (±6.5) | `+1.1 bps` | `+0.046 / +0.040` | `0.30%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,463.00 | ⚪ **CASH** | **+12.9 bps** (±10.1) | `+26.2 bps` | `+0.012 / -0.069` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.56 | ⚪ **CASH** | **-4.3 bps** (±6.3) | `-15.3 bps` | `+0.038 / +0.041` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 13:32:03 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,514.76 | ⚪ **CASH** | **+5.1 bps** (±6.5) | `+1.1 bps` | `+0.046 / +0.040` | `0.30%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,470.75 | ⚪ **CASH** | **+12.9 bps** (±10.1) | `+26.2 bps` | `+0.012 / -0.069` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.64 | ⚪ **CASH** | **-4.3 bps** (±6.3) | `-15.3 bps` | `+0.038 / +0.041` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 13:17:19 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,898.07 | ⚪ **CASH** | **+5.1 bps** (±6.5) | `+1.1 bps` | `+0.046 / +0.040` | `0.30%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,487.35 | ⚪ **CASH** | **+12.9 bps** (±10.1) | `+26.2 bps` | `+0.012 / -0.069` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $107.55 | ⚪ **CASH** | **-4.3 bps** (±6.3) | `-15.3 bps` | `+0.038 / +0.041` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 13:02:32 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,647.71 | ⚪ **CASH** | **+5.1 bps** (±6.5) | `+1.1 bps` | `+0.046 / +0.040` | `0.30%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,474.87 | ⚪ **CASH** | **+12.9 bps** (±10.1) | `+26.2 bps` | `+0.012 / -0.069` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $107.28 | ⚪ **CASH** | **-4.3 bps** (±6.3) | `-15.3 bps` | `+0.038 / +0.041` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 12:47:12 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,550.00 | ⚪ **CASH** | **+6.4 bps** (±6.2) | `+0.7 bps` | `+0.053 / +0.062` | `0.31%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,469.60 | ⚪ **CASH** | **+5.2 bps** (±9.0) | `+12.4 bps` | `+0.013 / -0.079` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.93 | ⚪ **CASH** | **-13.8 bps** (±9.4) | `-35.0 bps` | `+0.045 / +0.070` | `0.56%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 12:32:02 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,520.00 | ⚪ **CASH** | **+6.4 bps** (±6.2) | `+0.7 bps` | `+0.053 / +0.062` | `0.31%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,467.22 | ⚪ **CASH** | **+5.2 bps** (±9.0) | `+12.4 bps` | `+0.013 / -0.079` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.93 | ⚪ **CASH** | **-13.8 bps** (±9.4) | `-35.0 bps` | `+0.045 / +0.070` | `0.56%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 12:16:58 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,564.24 | ⚪ **CASH** | **+6.4 bps** (±6.2) | `+0.7 bps` | `+0.053 / +0.062` | `0.31%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,468.93 | ⚪ **CASH** | **+5.2 bps** (±9.0) | `+12.4 bps` | `+0.013 / -0.079` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $107.04 | ⚪ **CASH** | **-13.8 bps** (±9.4) | `-35.0 bps` | `+0.045 / +0.070` | `0.56%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 12:02:16 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,557.61 | ⚪ **CASH** | **+6.4 bps** (±6.2) | `+0.7 bps` | `+0.053 / +0.062` | `0.31%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,471.14 | ⚪ **CASH** | **+5.2 bps** (±9.0) | `+12.4 bps` | `+0.013 / -0.079` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.97 | ⚪ **CASH** | **-13.8 bps** (±9.4) | `-35.0 bps` | `+0.045 / +0.070` | `0.56%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 11:47:01 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,456.00 | ⚪ **CASH** | **+5.3 bps** (±3.7) | `+0.1 bps` | `+0.048 / +0.048` | `0.31%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,463.00 | ⚪ **CASH** | **+13.6 bps** (±9.6) | `+28.8 bps` | `+0.010 / -0.087` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.73 | ⚪ **CASH** | **-14.6 bps** (±6.3) | `-37.9 bps` | `+0.044 / +0.088` | `0.57%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 11:32:00 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,518.02 | ⚪ **CASH** | **+5.3 bps** (±3.7) | `+0.1 bps` | `+0.048 / +0.048` | `0.31%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,464.79 | ⚪ **CASH** | **+13.6 bps** (±9.6) | `+28.8 bps` | `+0.010 / -0.087` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.91 | ⚪ **CASH** | **-14.6 bps** (±6.3) | `-37.9 bps` | `+0.044 / +0.088` | `0.57%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 11:17:07 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,401.04 | ⚪ **CASH** | **+5.3 bps** (±3.7) | `+0.1 bps` | `+0.048 / +0.048` | `0.31%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,463.60 | ⚪ **CASH** | **+13.6 bps** (±9.6) | `+28.8 bps` | `+0.010 / -0.087` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.82 | ⚪ **CASH** | **-14.6 bps** (±6.3) | `-37.9 bps` | `+0.044 / +0.088` | `0.57%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 11:02:07 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,456.00 | ⚪ **CASH** | **+5.3 bps** (±3.7) | `+0.1 bps` | `+0.048 / +0.048` | `0.31%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,460.21 | ⚪ **CASH** | **+13.6 bps** (±9.6) | `+28.8 bps` | `+0.010 / -0.087` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.74 | ⚪ **CASH** | **-14.6 bps** (±6.3) | `-37.9 bps` | `+0.044 / +0.088` | `0.57%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 10:47:16 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,438.00 | ⚪ **CASH** | **+4.8 bps** (±4.5) | `-2.1 bps` | `+0.049 / +0.067` | `0.32%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,456.60 | ⚪ **CASH** | **+9.0 bps** (±7.4) | `+20.7 bps` | `+0.009 / -0.095` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.62 | ⚪ **CASH** | **-16.4 bps** (±9.8) | `-42.8 bps` | `+0.050 / +0.114` | `0.58%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 10:17:22 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,271.68 | ⚪ **CASH** | **+4.8 bps** (±4.5) | `-2.1 bps` | `+0.049 / +0.067` | `0.32%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,447.14 | ⚪ **CASH** | **+9.0 bps** (±7.4) | `+20.7 bps` | `+0.009 / -0.095` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.03 | ⚪ **CASH** | **-16.4 bps** (±9.8) | `-42.8 bps` | `+0.050 / +0.114` | `0.58%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 10:02:42 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,416.00 | ⚪ **CASH** | **+4.8 bps** (±4.5) | `-2.1 bps` | `+0.049 / +0.067` | `0.32%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,453.47 | ⚪ **CASH** | **+9.0 bps** (±7.4) | `+20.7 bps` | `+0.009 / -0.095` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.48 | ⚪ **CASH** | **-16.4 bps** (±9.8) | `-42.8 bps` | `+0.050 / +0.114` | `0.58%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 09:47:09 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,451.69 | ⚪ **CASH** | **+2.2 bps** (±12.5) | `-13.1 bps` | `+0.067 / +0.145` | `0.32%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,460.51 | ⚪ **CASH** | **+2.1 bps** (±10.9) | `-5.8 bps` | `+0.062 / +0.036` | `0.53%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.84 | ⚪ **CASH** | **-11.8 bps** (±4.8) | `-36.3 bps` | `+0.049 / +0.118` | `0.59%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 09:32:21 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,554.92 | ⚪ **CASH** | **+2.2 bps** (±12.5) | `-13.1 bps` | `+0.067 / +0.145` | `0.32%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,464.15 | ⚪ **CASH** | **+2.1 bps** (±10.9) | `-5.8 bps` | `+0.062 / +0.036` | `0.53%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $107.03 | ⚪ **CASH** | **-11.8 bps** (±4.8) | `-36.3 bps` | `+0.049 / +0.118` | `0.59%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 09:16:51 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,592.43 | ⚪ **CASH** | **+2.2 bps** (±12.5) | `-13.1 bps` | `+0.067 / +0.145` | `0.32%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,465.00 | ⚪ **CASH** | **+2.1 bps** (±10.9) | `-5.8 bps` | `+0.062 / +0.036` | `0.53%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $107.05 | ⚪ **CASH** | **-11.8 bps** (±4.8) | `-36.3 bps` | `+0.049 / +0.118` | `0.59%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 09:02:21 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,294.73 | ⚪ **CASH** | **+2.2 bps** (±12.5) | `-13.1 bps` | `+0.067 / +0.145` | `0.32%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,455.61 | ⚪ **CASH** | **+2.1 bps** (±10.9) | `-5.8 bps` | `+0.062 / +0.036` | `0.53%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.71 | ⚪ **CASH** | **-11.8 bps** (±4.8) | `-36.3 bps` | `+0.049 / +0.118` | `0.59%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 08:47:13 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,366.28 | ⚪ **CASH** | **-8.1 bps** (±11.1) | `-29.4 bps` | `+0.074 / +0.086` | `0.32%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,458.68 | ⚪ **CASH** | **-4.4 bps** (±10.9) | `-15.0 bps` | `+0.061 / -0.009` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.81 | ⚪ **CASH** | **-12.2 bps** (±9.3) | `-32.5 bps` | `+0.045 / +0.061` | `0.59%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 08:32:06 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,236.01 | ⚪ **CASH** | **-8.1 bps** (±11.1) | `-29.4 bps` | `+0.074 / +0.086` | `0.32%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,455.47 | ⚪ **CASH** | **-4.4 bps** (±10.9) | `-15.0 bps` | `+0.061 / -0.009` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.69 | ⚪ **CASH** | **-12.2 bps** (±9.3) | `-32.5 bps` | `+0.045 / +0.061` | `0.59%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 08:17:12 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,124.00 | ⚪ **CASH** | **-8.1 bps** (±11.1) | `-29.4 bps` | `+0.074 / +0.086` | `0.32%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,452.96 | ⚪ **CASH** | **-4.4 bps** (±10.9) | `-15.0 bps` | `+0.061 / -0.009` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.56 | ⚪ **CASH** | **-12.2 bps** (±9.3) | `-32.5 bps` | `+0.045 / +0.061` | `0.59%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 08:02:03 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,169.66 | ⚪ **CASH** | **-8.1 bps** (±11.1) | `-29.4 bps` | `+0.074 / +0.086` | `0.32%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,458.03 | ⚪ **CASH** | **-4.4 bps** (±10.9) | `-15.0 bps` | `+0.061 / -0.009` | `0.54%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.83 | ⚪ **CASH** | **-12.2 bps** (±9.3) | `-32.5 bps` | `+0.045 / +0.061` | `0.59%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 07:47:18 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,108.01 | ⚪ **CASH** | **-15.5 bps** (±6.7) | `-42.4 bps` | `+0.090 / +0.034` | `0.32%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,452.39 | ⚪ **CASH** | **+3.6 bps** (±7.8) | `-3.4 bps` | `+0.078 / -0.012` | `0.53%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.67 | ⚪ **CASH** | **-8.1 bps** (±9.5) | `-21.8 bps` | `+0.038 / +0.009` | `0.59%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 07:32:08 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,122.91 | ⚪ **CASH** | **-15.5 bps** (±6.7) | `-42.4 bps` | `+0.090 / +0.034` | `0.32%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,451.72 | ⚪ **CASH** | **+3.6 bps** (±7.8) | `-3.4 bps` | `+0.078 / -0.012` | `0.53%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.67 | ⚪ **CASH** | **-8.1 bps** (±9.5) | `-21.8 bps` | `+0.038 / +0.009` | `0.59%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 07:17:35 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,807.01 | ⚪ **CASH** | **-15.5 bps** (±6.7) | `-42.4 bps` | `+0.090 / +0.034` | `0.32%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,444.04 | ⚪ **CASH** | **+3.6 bps** (±7.8) | `-3.4 bps` | `+0.078 / -0.012` | `0.53%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.18 | ⚪ **CASH** | **-8.1 bps** (±9.5) | `-21.8 bps` | `+0.038 / +0.009` | `0.59%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 07:02:16 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,836.01 | ⚪ **CASH** | **-15.5 bps** (±6.7) | `-42.4 bps` | `+0.090 / +0.034` | `0.32%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,441.19 | ⚪ **CASH** | **+3.6 bps** (±7.8) | `-3.4 bps` | `+0.078 / -0.012` | `0.53%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.05 | ⚪ **CASH** | **-8.1 bps** (±9.5) | `-21.8 bps` | `+0.038 / +0.009` | `0.59%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 06:47:05 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,858.00 | ⚪ **CASH** | **-19.1 bps** (±3.3) | `-47.6 bps` | `+0.082 / +0.021` | `0.33%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,444.32 | ⚪ **CASH** | **+3.9 bps** (±7.5) | `-5.2 bps` | `+0.082 / +0.025` | `0.54%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.16 | ⚪ **CASH** | **-10.3 bps** (±7.9) | `-24.3 bps` | `+0.029 / +0.004` | `0.59%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
