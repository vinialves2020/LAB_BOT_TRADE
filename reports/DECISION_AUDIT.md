# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-19 19:26:20 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-19 19:26:20 UTC` | Patrimônio: **$960.07 USDT** (Caixa: `$593.76`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $62,822.89 | 🔴 **SHORT** | **-3.50%** | `MACRO_BEAR` | `60%` | `+75.4 bps` | Entrada CTA SHORT 1x [A Favor do Macro] | Spread EMA48/168: -3.50% | Peso: 13.3% | Stop ATR: $65,692.32 |
| **ETHUSDT** | $1,779.62 | 🔴 **SHORT** | **-3.48%** | `MACRO_BEAR` | `77%` | `+21.4 bps` | Entrada CTA SHORT 1x [A Favor do Macro] | Spread EMA48/168: -3.48% | Peso: 13.0% | Stop ATR: $1,879.89 |
| **SOLUSDT** | $73.86 | 🔴 **SHORT** | **-2.01%** | `MACRO_BEAR` | `85%` | `+14.3 bps` | Entrada CTA SHORT 1x [A Favor do Macro] | Spread EMA48/168: -2.01% | Peso: 11.8% | Stop ATR: $78.51 |

---

### 🕒 Ciclo `2026-11-19 19:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,795.19 | ⚪ **CASH** | **+37.4 bps** (±16.2) | `+75.4 bps` | `-0.012 / -0.042` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,774.98 | ⚪ **CASH** | **+7.0 bps** (±6.5) | `+21.4 bps` | `-0.015 / -0.082` | `0.58%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.89 | ⚪ **CASH** | **+10.6 bps** (±7.4) | `+14.3 bps` | `+0.051 / +0.028` | `0.70%/h` | `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 18:46:03 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,054.00 | ⚪ **CASH** | **+38.9 bps** (±13.8) | `+77.6 bps` | `-0.006 / -0.053` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,783.16 | ⚪ **CASH** | **+13.3 bps** (±10.6) | `+31.0 bps` | `-0.018 / -0.043` | `0.59%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.42 | ⚪ **CASH** | **+16.0 bps** (±7.8) | `+25.3 bps` | `+0.047 / +0.015` | `0.71%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.3 bps) |

---

### 🕒 Ciclo `2026-11-19 18:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,262.06 | ⚪ **CASH** | **+38.9 bps** (±13.8) | `+77.6 bps` | `-0.006 / -0.053` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,787.53 | ⚪ **CASH** | **+13.3 bps** (±10.6) | `+31.0 bps` | `-0.018 / -0.043` | `0.59%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.57 | ⚪ **CASH** | **+16.0 bps** (±7.8) | `+25.3 bps` | `+0.047 / +0.015` | `0.71%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.3 bps) |

---

### 🕒 Ciclo `2026-11-19 18:15:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,808.41 | ⚪ **CASH** | **+38.9 bps** (±13.8) | `+77.6 bps` | `-0.006 / -0.053` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,775.25 | ⚪ **CASH** | **+13.3 bps** (±10.6) | `+31.0 bps` | `-0.018 / -0.043` | `0.59%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.85 | ⚪ **CASH** | **+16.0 bps** (±7.8) | `+25.3 bps` | `+0.047 / +0.015` | `0.71%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.3 bps) |

---

### 🕒 Ciclo `2026-11-19 18:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,720.01 | ⚪ **CASH** | **+38.9 bps** (±13.8) | `+77.6 bps` | `-0.006 / -0.053` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,769.57 | ⚪ **CASH** | **+13.3 bps** (±10.6) | `+31.0 bps` | `-0.018 / -0.043` | `0.59%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.74 | ⚪ **CASH** | **+16.0 bps** (±7.8) | `+25.3 bps` | `+0.047 / +0.015` | `0.71%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.3 bps) |

---

### 🕒 Ciclo `2026-11-19 17:45:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,922.42 | ⚪ **CASH** | **+42.3 bps** (±16.2) | `+79.9 bps` | `+0.015 / -0.033` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,774.93 | ⚪ **CASH** | **+6.8 bps** (±8.7) | `+16.6 bps` | `-0.003 / -0.047` | `0.59%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.90 | ⚪ **CASH** | **+18.6 bps** (±12.3) | `+28.2 bps` | `+0.059 / +0.021` | `0.70%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-19 17:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,060.73 | ⚪ **CASH** | **+42.3 bps** (±16.2) | `+79.9 bps` | `+0.015 / -0.033` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,778.10 | ⚪ **CASH** | **+6.8 bps** (±8.7) | `+16.6 bps` | `-0.003 / -0.047` | `0.59%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.96 | ⚪ **CASH** | **+18.6 bps** (±12.3) | `+28.2 bps` | `+0.059 / +0.021` | `0.70%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-19 17:16:06 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,424.00 | ⚪ **CASH** | **+42.3 bps** (±16.2) | `+79.9 bps` | `+0.015 / -0.033` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,755.58 | ⚪ **CASH** | **+6.8 bps** (±8.7) | `+16.6 bps` | `-0.003 / -0.047` | `0.59%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.02 | ⚪ **CASH** | **+18.6 bps** (±12.3) | `+28.2 bps` | `+0.059 / +0.021` | `0.70%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-19 17:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,751.91 | ⚪ **CASH** | **+42.3 bps** (±16.2) | `+79.9 bps` | `+0.015 / -0.033` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **ETHUSDT** | $1,768.16 | ⚪ **CASH** | **+6.8 bps** (±8.7) | `+16.6 bps` | `-0.003 / -0.047` | `0.59%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.21 | ⚪ **CASH** | **+18.6 bps** (±12.3) | `+28.2 bps` | `+0.059 / +0.021` | `0.70%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-19 16:45:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,129.78 | ⚪ **CASH** | **+35.8 bps** (±12.1) | `+65.4 bps` | `+0.010 / +0.007` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,779.95 | ⚪ **CASH** | **+11.0 bps** (±7.6) | `+20.2 bps` | `+0.008 / -0.001` | `0.59%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.76 | ⚪ **CASH** | **+14.8 bps** (±8.7) | `+16.5 bps` | `+0.071 / +0.070` | `0.71%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-19 16:31:00 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,095.18 | ⚪ **CASH** | **+35.8 bps** (±12.1) | `+65.4 bps` | `+0.010 / +0.007` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,778.91 | ⚪ **CASH** | **+11.0 bps** (±7.6) | `+20.2 bps` | `+0.008 / -0.001` | `0.59%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.64 | ⚪ **CASH** | **+14.8 bps** (±8.7) | `+16.5 bps` | `+0.071 / +0.070` | `0.71%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-19 16:15:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,091.21 | ⚪ **CASH** | **+35.8 bps** (±12.1) | `+65.4 bps` | `+0.010 / +0.007` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,776.97 | ⚪ **CASH** | **+11.0 bps** (±7.6) | `+20.2 bps` | `+0.008 / -0.001` | `0.59%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.63 | ⚪ **CASH** | **+14.8 bps** (±8.7) | `+16.5 bps` | `+0.071 / +0.070` | `0.71%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-19 16:01:08 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,122.61 | ⚪ **CASH** | **+35.8 bps** (±12.1) | `+65.4 bps` | `+0.010 / +0.007` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,780.52 | ⚪ **CASH** | **+11.0 bps** (±7.6) | `+20.2 bps` | `+0.008 / -0.001` | `0.59%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.60 | ⚪ **CASH** | **+14.8 bps** (±8.7) | `+16.5 bps` | `+0.071 / +0.070` | `0.71%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |

---

### 🕒 Ciclo `2026-11-19 15:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,887.55 | ⚪ **CASH** | **+32.6 bps** (±11.0) | `+61.5 bps` | `-0.005 / +0.009` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,776.84 | ⚪ **CASH** | **+7.7 bps** (±5.8) | `+6.7 bps` | `+0.026 / +0.093` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.61 | ⚪ **CASH** | **+27.7 bps** (±16.4) | `+34.1 bps` | `+0.082 / +0.175` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 15:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,306.68 | ⚪ **CASH** | **+32.6 bps** (±11.0) | `+61.5 bps` | `-0.005 / +0.009` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,786.18 | ⚪ **CASH** | **+7.7 bps** (±5.8) | `+6.7 bps` | `+0.026 / +0.093` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.53 | ⚪ **CASH** | **+27.7 bps** (±16.4) | `+34.1 bps` | `+0.082 / +0.175` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 15:15:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,423.77 | ⚪ **CASH** | **+32.6 bps** (±11.0) | `+61.5 bps` | `-0.005 / +0.009` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,796.24 | ⚪ **CASH** | **+7.7 bps** (±5.8) | `+6.7 bps` | `+0.026 / +0.093` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.84 | ⚪ **CASH** | **+27.7 bps** (±16.4) | `+34.1 bps` | `+0.082 / +0.175` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 15:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,649.46 | ⚪ **CASH** | **+32.6 bps** (±11.0) | `+61.5 bps` | `-0.005 / +0.009` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,802.74 | ⚪ **CASH** | **+7.7 bps** (±5.8) | `+6.7 bps` | `+0.026 / +0.093` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.14 | ⚪ **CASH** | **+27.7 bps** (±16.4) | `+34.1 bps` | `+0.082 / +0.175` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 14:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,960.00 | ⚪ **CASH** | **+29.5 bps** (±17.9) | `+54.1 bps` | `+0.007 / +0.029` | `0.49%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,808.30 | ⚪ **CASH** | **+1.4 bps** (±3.5) | `-4.3 bps` | `+0.016 / +0.084` | `0.59%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $75.34 | ⚪ **CASH** | **+11.2 bps** (±4.2) | `+7.9 bps` | `+0.053 / +0.118` | `0.65%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 14:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,941.38 | ⚪ **CASH** | **+29.5 bps** (±17.9) | `+54.1 bps` | `+0.007 / +0.029` | `0.49%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,808.91 | ⚪ **CASH** | **+1.4 bps** (±3.5) | `-4.3 bps` | `+0.016 / +0.084` | `0.59%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $75.17 | ⚪ **CASH** | **+11.2 bps** (±4.2) | `+7.9 bps` | `+0.053 / +0.118` | `0.65%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 14:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,940.01 | ⚪ **CASH** | **+29.5 bps** (±17.9) | `+54.1 bps` | `+0.007 / +0.029` | `0.49%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,810.71 | ⚪ **CASH** | **+1.4 bps** (±3.5) | `-4.3 bps` | `+0.016 / +0.084` | `0.59%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $75.10 | ⚪ **CASH** | **+11.2 bps** (±4.2) | `+7.9 bps` | `+0.053 / +0.118` | `0.65%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 14:00:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,008.69 | ⚪ **CASH** | **+29.5 bps** (±17.9) | `+54.1 bps` | `+0.007 / +0.029` | `0.49%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,811.91 | ⚪ **CASH** | **+1.4 bps** (±3.5) | `-4.3 bps` | `+0.016 / +0.084` | `0.59%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $75.21 | ⚪ **CASH** | **+11.2 bps** (±4.2) | `+7.9 bps` | `+0.053 / +0.118` | `0.65%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 13:45:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,744.40 | ⚪ **CASH** | **+25.9 bps** (±15.4) | `+49.6 bps` | `+0.008 / -0.013` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,806.35 | ⚪ **CASH** | **+7.1 bps** (±6.4) | `+7.1 bps` | `+0.013 / +0.082` | `0.59%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $74.98 | ⚪ **CASH** | **+9.8 bps** (±2.7) | `+6.7 bps` | `+0.045 / +0.103` | `0.66%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 13:30:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,750.01 | ⚪ **CASH** | **+25.9 bps** (±15.4) | `+49.6 bps` | `+0.008 / -0.013` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,805.65 | ⚪ **CASH** | **+7.1 bps** (±6.4) | `+7.1 bps` | `+0.013 / +0.082` | `0.59%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $74.86 | ⚪ **CASH** | **+9.8 bps** (±2.7) | `+6.7 bps` | `+0.045 / +0.103` | `0.66%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 13:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,774.01 | ⚪ **CASH** | **+25.9 bps** (±15.4) | `+49.6 bps` | `+0.008 / -0.013` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,806.25 | ⚪ **CASH** | **+7.1 bps** (±6.4) | `+7.1 bps` | `+0.013 / +0.082` | `0.59%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $74.70 | ⚪ **CASH** | **+9.8 bps** (±2.7) | `+6.7 bps` | `+0.045 / +0.103` | `0.66%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 13:00:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,910.01 | ⚪ **CASH** | **+25.9 bps** (±15.4) | `+49.6 bps` | `+0.008 / -0.013` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,809.26 | ⚪ **CASH** | **+7.1 bps** (±6.4) | `+7.1 bps` | `+0.013 / +0.082` | `0.59%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $74.96 | ⚪ **CASH** | **+9.8 bps** (±2.7) | `+6.7 bps` | `+0.045 / +0.103` | `0.66%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 12:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,812.42 | ⚪ **CASH** | **+32.9 bps** (±14.4) | `+57.5 bps` | `+0.014 / +0.042` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,797.77 | ⚪ **CASH** | **-2.5 bps** (±4.3) | `-6.7 bps` | `-0.004 / +0.041` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $74.49 | ⚪ **CASH** | **+15.9 bps** (±3.9) | `+12.9 bps` | `+0.043 / +0.179` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-19 12:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,754.01 | ⚪ **CASH** | **+32.9 bps** (±14.4) | `+57.5 bps` | `+0.014 / +0.042` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,797.14 | ⚪ **CASH** | **-2.5 bps** (±4.3) | `-6.7 bps` | `-0.004 / +0.041` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
| **SOLUSDT** | $74.31 | ⚪ **CASH** | **+15.9 bps** (±3.9) | `+12.9 bps` | `+0.043 / +0.179` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

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
