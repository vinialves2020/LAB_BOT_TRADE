# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-21 19:46:59 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-21 19:46:59 UTC` | Patrimônio: **$1,000.18 USDT** (Caixa: `$669.53`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,545.39 | ⚪ **CASH** | **+4.6 bps** (±2.5) | `+1.7 bps` | `+0.037 / +0.027` | `0.32%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,495.20 | 🟡 **HOLD** | **+35.0 bps** (±13.9) | `+52.0 bps` | `+0.032 / +0.140` | `0.51%/h` | Liberado ✅ | Posição ativa há 0.7h (PnL: +0.21% | Pico: +0.35%) |
| **SOLUSDT** | $108.34 | ⚪ **CASH** | **+7.6 bps** (±1.6) | `+2.4 bps` | `+0.058 / +0.064` | `0.55%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 19:32:19 UTC` | Patrimônio: **$1,000.66 USDT** (Caixa: `$669.53`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,538.01 | ⚪ **CASH** | **+4.6 bps** (±2.5) | `+1.7 bps` | `+0.037 / +0.027` | `0.32%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,498.81 | 🟡 **HOLD** | **+35.0 bps** (±13.9) | `+52.0 bps` | `+0.032 / +0.140` | `0.51%/h` | Liberado ✅ | Posição ativa há 0.5h (PnL: +0.35% | Pico: +0.35%) |
| **SOLUSDT** | $108.22 | ⚪ **CASH** | **+7.6 bps** (±1.6) | `+2.4 bps` | `+0.058 / +0.064` | `0.55%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 19:17:23 UTC` | Patrimônio: **$1,000.58 USDT** (Caixa: `$669.53`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,460.01 | ⚪ **CASH** | **+4.6 bps** (±2.5) | `+1.7 bps` | `+0.037 / +0.027` | `0.32%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,498.21 | 🟡 **HOLD** | **+35.0 bps** (±13.9) | `+52.0 bps` | `+0.032 / +0.140` | `0.51%/h` | Liberado ✅ | Posição ativa há 0.3h (PnL: +0.33% | Pico: +0.33%) |
| **SOLUSDT** | $108.02 | ⚪ **CASH** | **+7.6 bps** (±1.6) | `+2.4 bps` | `+0.058 / +0.064` | `0.55%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 19:02:11 UTC` | Patrimônio: **$999.49 USDT** (Caixa: `$669.53`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,237.25 | ⚪ **CASH** | **+4.6 bps** (±2.5) | `+1.7 bps` | `+0.037 / +0.027` | `0.32%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,489.99 | 🟢 **BUY** | **+35.0 bps** (±13.9) | `+52.0 bps` | `+0.032 / +0.140` | `0.51%/h` | Liberado ✅ | Entrada Swing 12h aprovada (Alpha +35.0 bps > 24.0 bps | CVD 24h +0.032) |
| **SOLUSDT** | $107.70 | ⚪ **CASH** | **+7.6 bps** (±1.6) | `+2.4 bps` | `+0.058 / +0.064` | `0.55%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 18:47:01 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,693.98 | ⚪ **CASH** | **+4.2 bps** (±7.0) | `+0.3 bps` | `+0.042 / +0.038` | `0.32%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,514.85 | ⚪ **CASH** | **+25.3 bps** (±5.5) | `+33.0 bps` | `+0.032 / +0.135` | `0.50%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $108.91 | ⚪ **CASH** | **+12.9 bps** (±8.8) | `+14.7 bps` | `+0.049 / +0.054` | `0.54%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 18:32:41 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,764.36 | ⚪ **CASH** | **+4.2 bps** (±7.0) | `+0.3 bps` | `+0.042 / +0.038` | `0.32%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,516.47 | ⚪ **CASH** | **+25.3 bps** (±5.5) | `+33.0 bps` | `+0.032 / +0.135` | `0.50%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $109.12 | ⚪ **CASH** | **+12.9 bps** (±8.8) | `+14.7 bps` | `+0.049 / +0.054` | `0.54%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 18:17:20 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,744.00 | ⚪ **CASH** | **+4.2 bps** (±7.0) | `+0.3 bps` | `+0.042 / +0.038` | `0.32%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,519.19 | ⚪ **CASH** | **+25.3 bps** (±5.5) | `+33.0 bps` | `+0.032 / +0.135` | `0.50%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $108.89 | ⚪ **CASH** | **+12.9 bps** (±8.8) | `+14.7 bps` | `+0.049 / +0.054` | `0.54%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 18:02:45 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,710.19 | ⚪ **CASH** | **+4.2 bps** (±7.0) | `+0.3 bps` | `+0.042 / +0.038` | `0.32%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,516.02 | ⚪ **CASH** | **+25.3 bps** (±5.5) | `+33.0 bps` | `+0.032 / +0.135` | `0.50%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $108.74 | ⚪ **CASH** | **+12.9 bps** (±8.8) | `+14.7 bps` | `+0.049 / +0.054` | `0.54%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 17:47:40 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,628.60 | ⚪ **CASH** | **+7.4 bps** (±6.9) | `+3.3 bps` | `+0.051 / +0.061` | `0.32%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,516.78 | ⚪ **CASH** | **+27.8 bps** (±4.9) | `+38.4 bps` | `+0.026 / +0.122` | `0.50%/h` | `vol_compressed` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $108.60 | ⚪ **CASH** | **+12.8 bps** (±8.2) | `+14.3 bps` | `+0.053 / +0.044` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 17:32:42 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,574.91 | ⚪ **CASH** | **+7.4 bps** (±6.9) | `+3.3 bps` | `+0.051 / +0.061` | `0.32%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,513.96 | ⚪ **CASH** | **+27.8 bps** (±4.9) | `+38.4 bps` | `+0.026 / +0.122` | `0.50%/h` | `vol_compressed` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $108.49 | ⚪ **CASH** | **+12.8 bps** (±8.2) | `+14.3 bps` | `+0.053 / +0.044` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 17:17:40 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,454.50 | ⚪ **CASH** | **+7.4 bps** (±6.9) | `+3.3 bps` | `+0.051 / +0.061` | `0.32%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,509.34 | ⚪ **CASH** | **+27.8 bps** (±4.9) | `+38.4 bps` | `+0.026 / +0.122` | `0.50%/h` | `vol_compressed` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $108.12 | ⚪ **CASH** | **+12.8 bps** (±8.2) | `+14.3 bps` | `+0.053 / +0.044` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 17:02:46 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,471.60 | ⚪ **CASH** | **+7.4 bps** (±6.9) | `+3.3 bps` | `+0.051 / +0.061` | `0.32%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,506.07 | ⚪ **CASH** | **+27.8 bps** (±4.9) | `+38.4 bps` | `+0.026 / +0.122` | `0.50%/h` | `vol_compressed` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $108.12 | ⚪ **CASH** | **+12.8 bps** (±8.2) | `+14.3 bps` | `+0.053 / +0.044` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 16:47:44 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,692.01 | ⚪ **CASH** | **+6.3 bps** (±5.9) | `-1.9 bps` | `+0.060 / +0.086` | `0.33%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,516.99 | ⚪ **CASH** | **+38.1 bps** (±5.8) | `+56.5 bps` | `+0.026 / +0.127` | `0.51%/h` | `vol_compressed` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $108.59 | ⚪ **CASH** | **+6.4 bps** (±6.8) | `-0.7 bps` | `+0.079 / +0.046` | `0.56%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 16:32:48 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,630.81 | ⚪ **CASH** | **+6.3 bps** (±5.9) | `-1.9 bps` | `+0.060 / +0.086` | `0.33%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,504.98 | ⚪ **CASH** | **+38.1 bps** (±5.8) | `+56.5 bps` | `+0.026 / +0.127` | `0.51%/h` | `vol_compressed` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $108.32 | ⚪ **CASH** | **+6.4 bps** (±6.8) | `-0.7 bps` | `+0.079 / +0.046` | `0.56%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 16:17:05 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,588.49 | ⚪ **CASH** | **+6.3 bps** (±5.9) | `-1.9 bps` | `+0.060 / +0.086` | `0.33%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,508.34 | ⚪ **CASH** | **+38.1 bps** (±5.8) | `+56.5 bps` | `+0.026 / +0.127` | `0.51%/h` | `vol_compressed` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $108.42 | ⚪ **CASH** | **+6.4 bps** (±6.8) | `-0.7 bps` | `+0.079 / +0.046` | `0.56%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 16:02:09 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $84,512.00 | ⚪ **CASH** | **+6.3 bps** (±5.9) | `-1.9 bps` | `+0.060 / +0.086` | `0.33%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,509.54 | ⚪ **CASH** | **+38.1 bps** (±5.8) | `+56.5 bps` | `+0.026 / +0.127` | `0.51%/h` | `vol_compressed` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $108.42 | ⚪ **CASH** | **+6.4 bps** (±6.8) | `-0.7 bps` | `+0.079 / +0.046` | `0.56%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

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
