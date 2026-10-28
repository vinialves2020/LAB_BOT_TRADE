# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-28 11:17:17 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-28 11:17:17 UTC` | Patrimônio: **$997.82 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,367.21 | 🟡 **HOLD** | **+44.4 bps** (±10.7) | `+43.7 bps` | `+0.198 / +0.150` | `0.26%/h` | Liberado ✅ | Posição ativa há 1.3h (PnL: -0.24% | Pico: +0.05%) |
| **ETHUSDT** | $2,362.92 | ⚪ **CASH** | **+13.5 bps** (±6.3) | `+3.7 bps` | `+0.107 / +0.026` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.64 | ⚪ **CASH** | **+10.0 bps** (±29.3) | `-6.0 bps` | `+0.127 / +0.112` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 11:02:35 UTC` | Patrimônio: **$998.25 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,472.65 | 🟡 **HOLD** | **+44.4 bps** (±10.7) | `+43.7 bps` | `+0.198 / +0.150` | `0.26%/h` | Liberado ✅ | Posição ativa há 1.0h (PnL: -0.11% | Pico: +0.05%) |
| **ETHUSDT** | $2,366.81 | ⚪ **CASH** | **+13.5 bps** (±6.3) | `+3.7 bps` | `+0.107 / +0.026` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.85 | ⚪ **CASH** | **+10.0 bps** (±29.3) | `-6.0 bps` | `+0.127 / +0.112` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 10:47:17 UTC` | Patrimônio: **$998.77 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,600.52 | 🟡 **HOLD** | **+41.6 bps** (±11.3) | `+42.4 bps` | `+0.194 / +0.104` | `0.26%/h` | Liberado ✅ | Posição ativa há 0.8h (PnL: +0.05% | Pico: +0.05%) |
| **ETHUSDT** | $2,371.78 | ⚪ **CASH** | **+6.5 bps** (±7.8) | `-5.4 bps` | `+0.099 / -0.010` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.09 | ⚪ **CASH** | **+11.1 bps** (±31.8) | `-2.7 bps` | `+0.125 / +0.103` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 10:32:10 UTC` | Patrimônio: **$998.52 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,539.42 | 🟡 **HOLD** | **+41.6 bps** (±11.3) | `+42.4 bps` | `+0.194 / +0.104` | `0.26%/h` | Liberado ✅ | Posição ativa há 0.5h (PnL: -0.03% | Pico: +0.00%) |
| **ETHUSDT** | $2,370.58 | ⚪ **CASH** | **+6.5 bps** (±7.8) | `-5.4 bps` | `+0.099 / -0.010` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.18 | ⚪ **CASH** | **+11.1 bps** (±31.8) | `-2.7 bps` | `+0.125 / +0.103` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 10:17:07 UTC` | Patrimônio: **$998.48 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,529.93 | 🟡 **HOLD** | **+41.6 bps** (±11.3) | `+42.4 bps` | `+0.194 / +0.104` | `0.26%/h` | Liberado ✅ | Posição ativa há 0.2h (PnL: -0.04% | Pico: +0.00%) |
| **ETHUSDT** | $2,371.30 | ⚪ **CASH** | **+6.5 bps** (±7.8) | `-5.4 bps` | `+0.099 / -0.010` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.01 | ⚪ **CASH** | **+11.1 bps** (±31.8) | `-2.7 bps` | `+0.125 / +0.103` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 10:02:10 UTC` | Patrimônio: **$998.60 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,559.88 | 🟢 **BUY** | **+41.6 bps** (±11.3) | `+42.4 bps` | `+0.194 / +0.104` | `0.26%/h` | Liberado ✅ | Entrada Swing 12h aprovada (Alpha +41.6 bps > 24.0 bps | CVD 24h +0.194) |
| **ETHUSDT** | $2,374.74 | ⚪ **CASH** | **+6.5 bps** (±7.8) | `-5.4 bps` | `+0.099 / -0.010` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.09 | ⚪ **CASH** | **+11.1 bps** (±31.8) | `-2.7 bps` | `+0.125 / +0.103` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 09:47:03 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,527.81 | ⚪ **CASH** | **+40.1 bps** (±8.4) | `+38.5 bps` | `+0.189 / +0.125` | `0.26%/h` | `stretched_top` | Filtro: preço esticado próximo ao topo de 24h |
| **ETHUSDT** | $2,372.05 | ⚪ **CASH** | **+16.3 bps** (±8.0) | `+10.7 bps` | `+0.104 / +0.012` | `0.34%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.85 | ⚪ **CASH** | **+12.9 bps** (±19.4) | `+0.1 bps` | `+0.118 / +0.092` | `0.37%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 09:32:13 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,479.33 | ⚪ **CASH** | **+40.1 bps** (±8.4) | `+38.5 bps` | `+0.189 / +0.125` | `0.26%/h` | `stretched_top` | Filtro: preço esticado próximo ao topo de 24h |
| **ETHUSDT** | $2,369.29 | ⚪ **CASH** | **+16.3 bps** (±8.0) | `+10.7 bps` | `+0.104 / +0.012` | `0.34%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.66 | ⚪ **CASH** | **+12.9 bps** (±19.4) | `+0.1 bps` | `+0.118 / +0.092` | `0.37%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 09:17:07 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,496.40 | ⚪ **CASH** | **+40.1 bps** (±8.4) | `+38.5 bps` | `+0.189 / +0.125` | `0.26%/h` | `stretched_top` | Filtro: preço esticado próximo ao topo de 24h |
| **ETHUSDT** | $2,370.18 | ⚪ **CASH** | **+16.3 bps** (±8.0) | `+10.7 bps` | `+0.104 / +0.012` | `0.34%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.68 | ⚪ **CASH** | **+12.9 bps** (±19.4) | `+0.1 bps` | `+0.118 / +0.092` | `0.37%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 09:02:12 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,466.01 | ⚪ **CASH** | **+40.1 bps** (±8.4) | `+38.5 bps` | `+0.189 / +0.125` | `0.26%/h` | `stretched_top` | Filtro: preço esticado próximo ao topo de 24h |
| **ETHUSDT** | $2,369.49 | ⚪ **CASH** | **+16.3 bps** (±8.0) | `+10.7 bps` | `+0.104 / +0.012` | `0.34%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.62 | ⚪ **CASH** | **+12.9 bps** (±19.4) | `+0.1 bps` | `+0.118 / +0.092` | `0.37%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 08:46:58 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,560.00 | ⚪ **CASH** | **+33.8 bps** (±8.0) | `+31.8 bps` | `+0.188 / +0.051` | `0.25%/h` | `vol_compressed` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,376.24 | ⚪ **CASH** | **+13.2 bps** (±7.0) | `+7.9 bps` | `+0.112 / -0.042` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.91 | ⚪ **CASH** | **+13.2 bps** (±24.3) | `-1.7 bps` | `+0.125 / +0.131` | `0.37%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 08:32:08 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,439.00 | ⚪ **CASH** | **+33.8 bps** (±8.0) | `+31.8 bps` | `+0.188 / +0.051` | `0.25%/h` | `vol_compressed` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,372.85 | ⚪ **CASH** | **+13.2 bps** (±7.0) | `+7.9 bps` | `+0.112 / -0.042` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.95 | ⚪ **CASH** | **+13.2 bps** (±24.3) | `-1.7 bps` | `+0.125 / +0.131` | `0.37%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 08:17:09 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,175.89 | ⚪ **CASH** | **+33.8 bps** (±8.0) | `+31.8 bps` | `+0.188 / +0.051` | `0.25%/h` | `vol_compressed` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,365.61 | ⚪ **CASH** | **+13.2 bps** (±7.0) | `+7.9 bps` | `+0.112 / -0.042` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.35 | ⚪ **CASH** | **+13.2 bps** (±24.3) | `-1.7 bps` | `+0.125 / +0.131` | `0.37%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 08:02:21 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,162.01 | ⚪ **CASH** | **+33.8 bps** (±8.0) | `+31.8 bps` | `+0.188 / +0.051` | `0.25%/h` | `vol_compressed` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,364.87 | ⚪ **CASH** | **+13.2 bps** (±7.0) | `+7.9 bps` | `+0.112 / -0.042` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.46 | ⚪ **CASH** | **+13.2 bps** (±24.3) | `-1.7 bps` | `+0.125 / +0.131` | `0.37%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 07:46:59 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,000.00 | ⚪ **CASH** | **+34.3 bps** (±17.3) | `+29.2 bps` | `+0.189 / +0.130` | `0.25%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,356.47 | ⚪ **CASH** | **+17.0 bps** (±6.2) | `+13.1 bps` | `+0.111 / -0.020` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.14 | ⚪ **CASH** | **+16.3 bps** (±25.5) | `+3.6 bps` | `+0.124 / +0.142` | `0.37%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 07:33:22 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,939.18 | ⚪ **CASH** | **+34.3 bps** (±17.3) | `+29.2 bps` | `+0.189 / +0.130` | `0.25%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **ETHUSDT** | $2,354.30 | ⚪ **CASH** | **+17.0 bps** (±6.2) | `+13.1 bps` | `+0.111 / -0.020` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.00 | ⚪ **CASH** | **+16.3 bps** (±25.5) | `+3.6 bps` | `+0.124 / +0.142` | `0.37%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 07:17:00 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,926.80 | ⚪ **CASH** | **+34.3 bps** (±17.3) | `+29.2 bps` | `+0.189 / +0.130` | `0.25%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,354.42 | ⚪ **CASH** | **+17.0 bps** (±6.2) | `+13.1 bps` | `+0.111 / -0.020` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.99 | ⚪ **CASH** | **+16.3 bps** (±25.5) | `+3.6 bps` | `+0.124 / +0.142` | `0.37%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 07:02:12 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,877.31 | ⚪ **CASH** | **+34.3 bps** (±17.3) | `+29.2 bps` | `+0.189 / +0.130` | `0.25%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,352.73 | ⚪ **CASH** | **+17.0 bps** (±6.2) | `+13.1 bps` | `+0.111 / -0.020` | `0.34%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.99 | ⚪ **CASH** | **+16.3 bps** (±25.5) | `+3.6 bps` | `+0.124 / +0.142` | `0.37%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 06:47:02 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,925.46 | ⚪ **CASH** | **+23.6 bps** (±14.1) | `+15.0 bps` | `+0.184 / +0.050` | `0.26%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,353.98 | ⚪ **CASH** | **+16.6 bps** (±5.9) | `+14.0 bps` | `+0.102 / -0.030` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.08 | ⚪ **CASH** | **+12.0 bps** (±20.4) | `-0.8 bps` | `+0.114 / +0.095` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 06:32:17 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,916.19 | ⚪ **CASH** | **+23.6 bps** (±14.1) | `+15.0 bps` | `+0.184 / +0.050` | `0.26%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,352.66 | ⚪ **CASH** | **+16.6 bps** (±5.9) | `+14.0 bps` | `+0.102 / -0.030` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.03 | ⚪ **CASH** | **+12.0 bps** (±20.4) | `-0.8 bps` | `+0.114 / +0.095` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 06:17:00 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,964.00 | ⚪ **CASH** | **+23.6 bps** (±14.1) | `+15.0 bps` | `+0.184 / +0.050` | `0.26%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,355.98 | ⚪ **CASH** | **+16.6 bps** (±5.9) | `+14.0 bps` | `+0.102 / -0.030` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.09 | ⚪ **CASH** | **+12.0 bps** (±20.4) | `-0.8 bps` | `+0.114 / +0.095` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 06:02:04 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,922.00 | ⚪ **CASH** | **+23.6 bps** (±14.1) | `+15.0 bps` | `+0.184 / +0.050` | `0.26%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,352.99 | ⚪ **CASH** | **+16.6 bps** (±5.9) | `+14.0 bps` | `+0.102 / -0.030` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.88 | ⚪ **CASH** | **+12.0 bps** (±20.4) | `-0.8 bps` | `+0.114 / +0.095` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 05:47:02 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,978.42 | ⚪ **CASH** | **+28.0 bps** (±14.8) | `+22.4 bps` | `+0.185 / +0.062` | `0.26%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,353.74 | ⚪ **CASH** | **+13.9 bps** (±3.8) | `+6.1 bps` | `+0.107 / +0.005` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.89 | ⚪ **CASH** | **+9.3 bps** (±23.3) | `-1.8 bps` | `+0.108 / +0.050` | `0.39%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 05:32:06 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,966.22 | ⚪ **CASH** | **+28.0 bps** (±14.8) | `+22.4 bps` | `+0.185 / +0.062` | `0.26%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,356.33 | ⚪ **CASH** | **+13.9 bps** (±3.8) | `+6.1 bps` | `+0.107 / +0.005` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.03 | ⚪ **CASH** | **+9.3 bps** (±23.3) | `-1.8 bps` | `+0.108 / +0.050` | `0.39%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 05:17:03 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,938.00 | ⚪ **CASH** | **+28.0 bps** (±14.8) | `+22.4 bps` | `+0.185 / +0.062` | `0.26%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,353.51 | ⚪ **CASH** | **+13.9 bps** (±3.8) | `+6.1 bps` | `+0.107 / +0.005` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.94 | ⚪ **CASH** | **+9.3 bps** (±23.3) | `-1.8 bps` | `+0.108 / +0.050` | `0.39%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 05:02:24 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,950.00 | ⚪ **CASH** | **+28.0 bps** (±14.8) | `+22.4 bps` | `+0.185 / +0.062` | `0.26%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,354.41 | ⚪ **CASH** | **+13.9 bps** (±3.8) | `+6.1 bps` | `+0.107 / +0.005` | `0.35%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.99 | ⚪ **CASH** | **+9.3 bps** (±23.3) | `-1.8 bps` | `+0.108 / +0.050` | `0.39%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 04:47:02 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,032.02 | ⚪ **CASH** | **+37.0 bps** (±13.5) | `+36.3 bps` | `+0.194 / +0.073` | `0.26%/h` | `vol_compressed` `stretched_top` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,358.67 | ⚪ **CASH** | **+7.7 bps** (±4.7) | `-6.5 bps` | `+0.108 / +0.019` | `0.36%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.22 | ⚪ **CASH** | **+10.4 bps** (±23.9) | `+0.1 bps` | `+0.109 / +0.045` | `0.39%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 04:32:03 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,036.11 | ⚪ **CASH** | **+37.0 bps** (±13.5) | `+36.3 bps` | `+0.194 / +0.073` | `0.26%/h` | `vol_compressed` `stretched_top` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,356.47 | ⚪ **CASH** | **+7.7 bps** (±4.7) | `-6.5 bps` | `+0.108 / +0.019` | `0.36%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.93 | ⚪ **CASH** | **+10.4 bps** (±23.9) | `+0.1 bps` | `+0.109 / +0.045` | `0.39%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 04:17:33 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$999.00`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,002.41 | 🔴 **SELL** | **+37.0 bps** (±13.5) | `+36.3 bps` | `+0.194 / +0.073` | `0.26%/h` | `vol_compressed` `stretched_top` | Alvo temporal de 12h concluído (+0.57%) |
| **ETHUSDT** | $2,356.89 | ⚪ **CASH** | **+7.7 bps** (±4.7) | `-6.5 bps` | `+0.108 / +0.019` | `0.36%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.94 | ⚪ **CASH** | **+10.4 bps** (±23.9) | `+0.1 bps` | `+0.109 / +0.045` | `0.39%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 04:02:02 UTC` | Patrimônio: **$999.64 USDT** (Caixa: `$778.46`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,138.01 | 🟡 **HOLD** | **+37.0 bps** (±13.5) | `+36.3 bps` | `+0.194 / +0.073` | `0.26%/h` | `vol_compressed` `stretched_top` | Posição ativa há 12.0h (PnL: +0.74% | Pico: +0.83%) |
| **ETHUSDT** | $2,360.17 | ⚪ **CASH** | **+7.7 bps** (±4.7) | `-6.5 bps` | `+0.108 / +0.019` | `0.36%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.06 | ⚪ **CASH** | **+10.4 bps** (±23.9) | `+0.1 bps` | `+0.109 / +0.045` | `0.39%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 03:47:03 UTC` | Patrimônio: **$999.85 USDT** (Caixa: `$778.46`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,214.06 | 🟡 **HOLD** | **+42.2 bps** (±7.7) | `+46.6 bps` | `+0.182 / +0.072` | `0.26%/h` | `vol_compressed` | Posição ativa há 11.7h (PnL: +0.83% | Pico: +0.83%) |
| **ETHUSDT** | $2,366.12 | ⚪ **CASH** | **+14.9 bps** (±4.3) | `+4.9 bps` | `+0.106 / +0.054` | `0.36%/h` | `vol_compressed` `stretched_top` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.25 | ⚪ **CASH** | **+8.6 bps** (±23.8) | `-2.8 bps` | `+0.103 / +0.056` | `0.39%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 03:31:59 UTC` | Patrimônio: **$999.61 USDT** (Caixa: `$778.46`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,127.28 | 🟡 **HOLD** | **+42.2 bps** (±7.7) | `+46.6 bps` | `+0.182 / +0.072` | `0.26%/h` | `vol_compressed` | Posição ativa há 11.5h (PnL: +0.72% | Pico: +0.81%) |
| **ETHUSDT** | $2,364.57 | ⚪ **CASH** | **+14.9 bps** (±4.3) | `+4.9 bps` | `+0.106 / +0.054` | `0.36%/h` | `vol_compressed` `stretched_top` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.22 | ⚪ **CASH** | **+8.6 bps** (±23.8) | `-2.8 bps` | `+0.103 / +0.056` | `0.39%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 03:17:23 UTC` | Patrimônio: **$999.16 USDT** (Caixa: `$778.46`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,962.78 | 🟡 **HOLD** | **+42.2 bps** (±7.7) | `+46.6 bps` | `+0.182 / +0.072` | `0.26%/h` | `vol_compressed` | Posição ativa há 11.3h (PnL: +0.52% | Pico: +0.81%) |
| **ETHUSDT** | $2,358.06 | ⚪ **CASH** | **+14.9 bps** (±4.3) | `+4.9 bps` | `+0.106 / +0.054` | `0.36%/h` | `vol_compressed` `stretched_top` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.69 | ⚪ **CASH** | **+8.6 bps** (±23.8) | `-2.8 bps` | `+0.103 / +0.056` | `0.39%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 03:02:32 UTC` | Patrimônio: **$999.07 USDT** (Caixa: `$778.46`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,928.00 | 🟡 **HOLD** | **+42.2 bps** (±7.7) | `+46.6 bps` | `+0.182 / +0.072` | `0.26%/h` | `vol_compressed` | Posição ativa há 11.0h (PnL: +0.48% | Pico: +0.81%) |
| **ETHUSDT** | $2,357.40 | ⚪ **CASH** | **+14.9 bps** (±4.3) | `+4.9 bps` | `+0.106 / +0.054` | `0.36%/h` | `vol_compressed` `stretched_top` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.62 | ⚪ **CASH** | **+8.6 bps** (±23.8) | `-2.8 bps` | `+0.103 / +0.056` | `0.39%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 02:47:05 UTC` | Patrimônio: **$999.04 USDT** (Caixa: `$778.46`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,919.28 | 🟡 **HOLD** | **+33.3 bps** (±13.7) | `+31.1 bps` | `+0.170 / +0.105` | `0.27%/h` | `vol_compressed` | Posição ativa há 10.7h (PnL: +0.46% | Pico: +0.81%) |
| **ETHUSDT** | $2,357.15 | ⚪ **CASH** | **+9.9 bps** (±6.3) | `-4.4 bps` | `+0.103 / +0.075` | `0.37%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.64 | ⚪ **CASH** | **+7.5 bps** (±21.6) | `-3.3 bps` | `+0.103 / +0.038` | `0.40%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 02:32:17 UTC` | Patrimônio: **$999.12 USDT** (Caixa: `$778.46`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,948.00 | 🟡 **HOLD** | **+33.3 bps** (±13.7) | `+31.1 bps` | `+0.170 / +0.105` | `0.27%/h` | `vol_compressed` | Posição ativa há 10.5h (PnL: +0.50% | Pico: +0.81%) |
| **ETHUSDT** | $2,358.72 | ⚪ **CASH** | **+9.9 bps** (±6.3) | `-4.4 bps` | `+0.103 / +0.075` | `0.37%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.67 | ⚪ **CASH** | **+7.5 bps** (±21.6) | `-3.3 bps` | `+0.103 / +0.038` | `0.40%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
