# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-29 17:02:28 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-29 17:02:28 UTC` | Patrimônio: **$992.91 USDT** (Caixa: `$518.31`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,236.38 | 🟡 **HOLD** | **+28.9 bps** (±11.5) | `+27.7 bps` | `+0.134 / +0.110` | `0.40%/h` | Liberado ✅ | Posição ativa há 2.0h (PnL: -0.03% | Pico: +0.74%) |
| **ETHUSDT** | $2,352.78 | ⚪ **CASH** | **+40.1 bps** (±13.3) | `+51.3 bps` | `+0.056 / +0.183` | `0.46%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $101.90 | 🟡 **HOLD** | **+53.1 bps** (±23.6) | `+67.4 bps` | `+0.131 / +0.213` | `0.53%/h` | Liberado ✅ | Posição ativa há 2.0h (PnL: +0.09% | Pico: +0.82%) |

---

### 🕒 Ciclo `2026-10-29 16:47:30 UTC` | Patrimônio: **$993.71 USDT** (Caixa: `$518.31`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,398.65 | 🟡 **HOLD** | **+30.5 bps** (±15.6) | `+25.4 bps` | `+0.155 / +0.154` | `0.39%/h` | `stretched_top` | Posição ativa há 1.7h (PnL: +0.17% | Pico: +0.74%) |
| **ETHUSDT** | $2,358.07 | ⚪ **CASH** | **+52.0 bps** (±15.4) | `+73.8 bps` | `+0.045 / +0.176` | `0.45%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $102.00 | 🟡 **HOLD** | **+59.6 bps** (±24.0) | `+78.4 bps` | `+0.134 / +0.208` | `0.52%/h` | Liberado ✅ | Posição ativa há 1.7h (PnL: +0.19% | Pico: +0.82%) |

---

### 🕒 Ciclo `2026-10-29 16:32:29 UTC` | Patrimônio: **$993.94 USDT** (Caixa: `$518.31`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,414.83 | 🟡 **HOLD** | **+30.5 bps** (±15.6) | `+25.4 bps` | `+0.155 / +0.154` | `0.39%/h` | `stretched_top` | Posição ativa há 1.5h (PnL: +0.19% | Pico: +0.74%) |
| **ETHUSDT** | $2,357.90 | 🔴 **SELL** | **+52.0 bps** (±15.4) | `+73.8 bps` | `+0.045 / +0.176` | `0.45%/h` | Liberado ✅ | Trailing Stop acionado (pico +1.03%, realizou +0.48%) |
| **SOLUSDT** | $102.12 | 🟡 **HOLD** | **+59.6 bps** (±24.0) | `+78.4 bps` | `+0.134 / +0.208` | `0.52%/h` | Liberado ✅ | Posição ativa há 1.5h (PnL: +0.30% | Pico: +0.82%) |

---

### 🕒 Ciclo `2026-10-29 16:17:35 UTC` | Patrimônio: **$995.30 USDT** (Caixa: `$298.12`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,541.11 | 🟡 **HOLD** | **+30.5 bps** (±15.6) | `+25.4 bps` | `+0.155 / +0.154` | `0.39%/h` | `stretched_top` | Posição ativa há 1.2h (PnL: +0.34% | Pico: +0.74%) |
| **ETHUSDT** | $2,360.56 | 🟡 **HOLD** | **+52.0 bps** (±15.4) | `+73.8 bps` | `+0.045 / +0.176` | `0.45%/h` | Liberado ✅ | Posição ativa há 1.2h (PnL: +0.59% | Pico: +1.03%) |
| **SOLUSDT** | $102.35 | 🟡 **HOLD** | **+59.6 bps** (±24.0) | `+78.4 bps` | `+0.134 / +0.208` | `0.52%/h` | Liberado ✅ | Posição ativa há 1.2h (PnL: +0.53% | Pico: +0.82%) |

---

### 🕒 Ciclo `2026-10-29 16:02:39 UTC` | Patrimônio: **$996.52 USDT** (Caixa: `$298.12`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,670.64 | 🟡 **HOLD** | **+30.5 bps** (±15.6) | `+25.4 bps` | `+0.155 / +0.154` | `0.39%/h` | `stretched_top` | Posição ativa há 1.0h (PnL: +0.50% | Pico: +0.74%) |
| **ETHUSDT** | $2,365.73 | 🟡 **HOLD** | **+52.0 bps** (±15.4) | `+73.8 bps` | `+0.045 / +0.176` | `0.45%/h` | Liberado ✅ | Posição ativa há 1.0h (PnL: +0.81% | Pico: +1.03%) |
| **SOLUSDT** | $102.50 | 🟡 **HOLD** | **+59.6 bps** (±24.0) | `+78.4 bps` | `+0.134 / +0.208` | `0.52%/h` | Liberado ✅ | Posição ativa há 1.0h (PnL: +0.68% | Pico: +0.82%) |

---

### 🕒 Ciclo `2026-10-29 15:47:40 UTC` | Patrimônio: **$997.98 USDT** (Caixa: `$298.12`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,865.38 | 🟡 **HOLD** | **+29.9 bps** (±14.2) | `+23.8 bps` | `+0.156 / +0.155` | `0.37%/h` | Liberado ✅ | Posição ativa há 0.7h (PnL: +0.74% | Pico: +0.74%) |
| **ETHUSDT** | $2,370.74 | 🟡 **HOLD** | **+26.6 bps** (±8.8) | `+31.9 bps` | `+0.026 / +0.120` | `0.42%/h` | Liberado ✅ | Posição ativa há 0.7h (PnL: +1.03% | Pico: +1.03%) |
| **SOLUSDT** | $102.64 | 🟡 **HOLD** | **+36.0 bps** (±11.0) | `+37.6 bps` | `+0.122 / +0.156` | `0.51%/h` | Liberado ✅ | Posição ativa há 0.7h (PnL: +0.82% | Pico: +0.82%) |

---

### 🕒 Ciclo `2026-10-29 15:32:46 UTC` | Patrimônio: **$995.42 USDT** (Caixa: `$298.12`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,564.65 | 🟡 **HOLD** | **+29.9 bps** (±14.2) | `+23.8 bps` | `+0.156 / +0.155` | `0.37%/h` | Liberado ✅ | Posição ativa há 0.5h (PnL: +0.37% | Pico: +0.37%) |
| **ETHUSDT** | $2,362.29 | 🟡 **HOLD** | **+26.6 bps** (±8.8) | `+31.9 bps` | `+0.026 / +0.120` | `0.42%/h` | Liberado ✅ | Posição ativa há 0.5h (PnL: +0.67% | Pico: +0.67%) |
| **SOLUSDT** | $102.26 | 🟡 **HOLD** | **+36.0 bps** (±11.0) | `+37.6 bps` | `+0.122 / +0.156` | `0.51%/h` | Liberado ✅ | Posição ativa há 0.5h (PnL: +0.44% | Pico: +0.44%) |

---

### 🕒 Ciclo `2026-10-29 15:17:21 UTC` | Patrimônio: **$994.51 USDT** (Caixa: `$298.12`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,477.27 | 🟡 **HOLD** | **+29.9 bps** (±14.2) | `+23.8 bps` | `+0.156 / +0.155` | `0.37%/h` | Liberado ✅ | Posição ativa há 0.2h (PnL: +0.26% | Pico: +0.26%) |
| **ETHUSDT** | $2,357.84 | 🟡 **HOLD** | **+26.6 bps** (±8.8) | `+31.9 bps` | `+0.026 / +0.120` | `0.42%/h` | Liberado ✅ | Posição ativa há 0.2h (PnL: +0.48% | Pico: +0.48%) |
| **SOLUSDT** | $102.16 | 🟡 **HOLD** | **+36.0 bps** (±11.0) | `+37.6 bps` | `+0.122 / +0.156` | `0.51%/h` | Liberado ✅ | Posição ativa há 0.2h (PnL: +0.34% | Pico: +0.34%) |

---

### 🕒 Ciclo `2026-10-29 15:03:14 UTC` | Patrimônio: **$992.10 USDT** (Caixa: `$298.12`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,263.95 | 🟢 **BUY** | **+29.9 bps** (±14.2) | `+23.8 bps` | `+0.156 / +0.155` | `0.37%/h` | Liberado ✅ | Entrada Swing 12h aprovada (Alpha +29.9 bps > 24.0 bps | CVD 24h +0.156) |
| **ETHUSDT** | $2,346.68 | 🟢 **BUY** | **+26.6 bps** (±8.8) | `+31.9 bps` | `+0.026 / +0.120` | `0.42%/h` | Liberado ✅ | Entrada Swing 12h aprovada (Alpha +26.6 bps > 24.0 bps | CVD 24h +0.026) |
| **SOLUSDT** | $101.81 | 🟢 **BUY** | **+36.0 bps** (±11.0) | `+37.6 bps` | `+0.122 / +0.156` | `0.51%/h` | Liberado ✅ | Entrada Swing 12h aprovada (Alpha +36.0 bps > 24.0 bps | CVD 24h +0.122) |

---

### 🕒 Ciclo `2026-10-29 14:47:17 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,197.66 | ⚪ **CASH** | **+9.5 bps** (±8.1) | `-19.0 bps` | `+0.164 / +0.208` | `0.33%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,344.15 | ⚪ **CASH** | **-5.9 bps** (±9.8) | `-22.7 bps` | `+0.009 / +0.074` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.83 | ⚪ **CASH** | **+4.5 bps** (±14.4) | `-17.5 bps` | `+0.112 / +0.141` | `0.48%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 14:32:36 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,600.52 | ⚪ **CASH** | **+9.5 bps** (±8.1) | `-19.0 bps` | `+0.164 / +0.208` | `0.33%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,334.82 | ⚪ **CASH** | **-5.9 bps** (±9.8) | `-22.7 bps` | `+0.009 / +0.074` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.07 | ⚪ **CASH** | **+4.5 bps** (±14.4) | `-17.5 bps` | `+0.112 / +0.141` | `0.48%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 14:18:17 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,486.46 | ⚪ **CASH** | **+9.5 bps** (±8.1) | `-19.0 bps` | `+0.164 / +0.208` | `0.33%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,331.61 | ⚪ **CASH** | **-5.9 bps** (±9.8) | `-22.7 bps` | `+0.009 / +0.074` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.92 | ⚪ **CASH** | **+4.5 bps** (±14.4) | `-17.5 bps` | `+0.112 / +0.141` | `0.48%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 14:02:27 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,338.00 | ⚪ **CASH** | **+9.5 bps** (±8.1) | `-19.0 bps` | `+0.164 / +0.208` | `0.33%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,326.74 | ⚪ **CASH** | **-5.9 bps** (±9.8) | `-22.7 bps` | `+0.009 / +0.074` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.74 | ⚪ **CASH** | **+4.5 bps** (±14.4) | `-17.5 bps` | `+0.112 / +0.141` | `0.48%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 13:47:44 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,102.00 | ⚪ **CASH** | **+9.8 bps** (±8.7) | `-15.4 bps` | `+0.150 / +0.194` | `0.33%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,320.91 | ⚪ **CASH** | **-0.4 bps** (±8.5) | `-11.5 bps` | `+0.002 / +0.072` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.47 | ⚪ **CASH** | **+5.1 bps** (±17.2) | `-10.1 bps` | `+0.101 / +0.080` | `0.49%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 13:32:23 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,121.38 | ⚪ **CASH** | **+9.8 bps** (±8.7) | `-15.4 bps` | `+0.150 / +0.194` | `0.33%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,325.29 | ⚪ **CASH** | **-0.4 bps** (±8.5) | `-11.5 bps` | `+0.002 / +0.072` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.61 | ⚪ **CASH** | **+5.1 bps** (±17.2) | `-10.1 bps` | `+0.101 / +0.080` | `0.49%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 13:17:18 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,278.00 | ⚪ **CASH** | **+9.8 bps** (±8.7) | `-15.4 bps` | `+0.150 / +0.194` | `0.33%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,329.72 | ⚪ **CASH** | **-0.4 bps** (±8.5) | `-11.5 bps` | `+0.002 / +0.072` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.90 | ⚪ **CASH** | **+5.1 bps** (±17.2) | `-10.1 bps` | `+0.101 / +0.080` | `0.49%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 13:02:53 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,174.00 | ⚪ **CASH** | **+9.8 bps** (±8.7) | `-15.4 bps` | `+0.150 / +0.194` | `0.33%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,327.12 | ⚪ **CASH** | **-0.4 bps** (±8.5) | `-11.5 bps` | `+0.002 / +0.072` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.75 | ⚪ **CASH** | **+5.1 bps** (±17.2) | `-10.1 bps` | `+0.101 / +0.080` | `0.49%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 12:47:48 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,044.01 | ⚪ **CASH** | **+7.7 bps** (±11.9) | `-18.0 bps` | `+0.145 / +0.196` | `0.34%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,321.12 | ⚪ **CASH** | **-4.2 bps** (±9.1) | `-16.2 bps` | `+0.002 / +0.045` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.57 | ⚪ **CASH** | **+3.0 bps** (±16.0) | `-9.5 bps` | `+0.087 / +0.034` | `0.49%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 12:32:27 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,185.81 | ⚪ **CASH** | **+7.7 bps** (±11.9) | `-18.0 bps` | `+0.145 / +0.196` | `0.34%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,325.65 | ⚪ **CASH** | **-4.2 bps** (±9.1) | `-16.2 bps` | `+0.002 / +0.045` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.68 | ⚪ **CASH** | **+3.0 bps** (±16.0) | `-9.5 bps` | `+0.087 / +0.034` | `0.49%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 12:17:23 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,143.82 | ⚪ **CASH** | **+7.7 bps** (±11.9) | `-18.0 bps` | `+0.145 / +0.196` | `0.34%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,324.69 | ⚪ **CASH** | **-4.2 bps** (±9.1) | `-16.2 bps` | `+0.002 / +0.045` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.34 | ⚪ **CASH** | **+3.0 bps** (±16.0) | `-9.5 bps` | `+0.087 / +0.034` | `0.49%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 12:02:27 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,115.57 | ⚪ **CASH** | **+7.7 bps** (±11.9) | `-18.0 bps` | `+0.145 / +0.196` | `0.34%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,322.69 | ⚪ **CASH** | **-4.2 bps** (±9.1) | `-16.2 bps` | `+0.002 / +0.045` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.26 | ⚪ **CASH** | **+3.0 bps** (±16.0) | `-9.5 bps` | `+0.087 / +0.034` | `0.49%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 11:47:17 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,190.78 | ⚪ **CASH** | **+6.4 bps** (±13.8) | `-17.2 bps` | `+0.138 / +0.169` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,325.50 | ⚪ **CASH** | **+1.3 bps** (±8.9) | `-4.3 bps` | `-0.009 / +0.037` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.45 | ⚪ **CASH** | **+4.2 bps** (±16.4) | `-3.5 bps` | `+0.084 / -0.013` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 11:32:17 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,171.33 | ⚪ **CASH** | **+6.4 bps** (±13.8) | `-17.2 bps` | `+0.138 / +0.169` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,325.26 | ⚪ **CASH** | **+1.3 bps** (±8.9) | `-4.3 bps` | `-0.009 / +0.037` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.46 | ⚪ **CASH** | **+4.2 bps** (±16.4) | `-3.5 bps` | `+0.084 / -0.013` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 11:17:38 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,179.57 | ⚪ **CASH** | **+6.4 bps** (±13.8) | `-17.2 bps` | `+0.138 / +0.169` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,324.45 | ⚪ **CASH** | **+1.3 bps** (±8.9) | `-4.3 bps` | `-0.009 / +0.037` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.57 | ⚪ **CASH** | **+4.2 bps** (±16.4) | `-3.5 bps` | `+0.084 / -0.013` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 11:02:18 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,242.87 | ⚪ **CASH** | **+6.4 bps** (±13.8) | `-17.2 bps` | `+0.138 / +0.169` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,325.72 | ⚪ **CASH** | **+1.3 bps** (±8.9) | `-4.3 bps` | `-0.009 / +0.037` | `0.43%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.52 | ⚪ **CASH** | **+4.2 bps** (±16.4) | `-3.5 bps` | `+0.084 / -0.013` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 10:47:14 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,307.50 | ⚪ **CASH** | **+7.3 bps** (±10.8) | `-14.8 bps` | `+0.138 / +0.149` | `0.35%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,326.81 | ⚪ **CASH** | **+1.4 bps** (±9.0) | `-4.7 bps` | `-0.007 / +0.043` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.68 | ⚪ **CASH** | **+3.0 bps** (±15.9) | `-3.7 bps` | `+0.084 / -0.045` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 10:32:15 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,191.21 | ⚪ **CASH** | **+7.3 bps** (±10.8) | `-14.8 bps` | `+0.138 / +0.149` | `0.35%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,320.69 | ⚪ **CASH** | **+1.4 bps** (±9.0) | `-4.7 bps` | `-0.007 / +0.043` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.18 | ⚪ **CASH** | **+3.0 bps** (±15.9) | `-3.7 bps` | `+0.084 / -0.045` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 10:17:19 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,119.82 | ⚪ **CASH** | **+7.3 bps** (±10.8) | `-14.8 bps` | `+0.138 / +0.149` | `0.35%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,317.65 | ⚪ **CASH** | **+1.4 bps** (±9.0) | `-4.7 bps` | `-0.007 / +0.043` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.14 | ⚪ **CASH** | **+3.0 bps** (±15.9) | `-3.7 bps` | `+0.084 / -0.045` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 10:02:26 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,186.01 | ⚪ **CASH** | **+7.3 bps** (±10.8) | `-14.8 bps` | `+0.138 / +0.149` | `0.35%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,320.67 | ⚪ **CASH** | **+1.4 bps** (±9.0) | `-4.7 bps` | `-0.007 / +0.043` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.30 | ⚪ **CASH** | **+3.0 bps** (±15.9) | `-3.7 bps` | `+0.084 / -0.045` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 09:47:17 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,204.66 | ⚪ **CASH** | **+7.3 bps** (±11.5) | `-13.5 bps` | `+0.138 / +0.132` | `0.35%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,321.05 | ⚪ **CASH** | **+4.0 bps** (±11.0) | `+1.2 bps` | `-0.012 / +0.038` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.18 | ⚪ **CASH** | **+9.0 bps** (±14.6) | `+4.9 bps` | `+0.091 / -0.026` | `0.51%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 09:32:25 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,140.01 | ⚪ **CASH** | **+7.3 bps** (±11.5) | `-13.5 bps` | `+0.138 / +0.132` | `0.35%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,319.36 | ⚪ **CASH** | **+4.0 bps** (±11.0) | `+1.2 bps` | `-0.012 / +0.038` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.20 | ⚪ **CASH** | **+9.0 bps** (±14.6) | `+4.9 bps` | `+0.091 / -0.026` | `0.51%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 09:17:20 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,236.89 | ⚪ **CASH** | **+7.3 bps** (±11.5) | `-13.5 bps` | `+0.138 / +0.132` | `0.35%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,322.01 | ⚪ **CASH** | **+4.0 bps** (±11.0) | `+1.2 bps` | `-0.012 / +0.038` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.33 | ⚪ **CASH** | **+9.0 bps** (±14.6) | `+4.9 bps` | `+0.091 / -0.026` | `0.51%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 09:02:43 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,122.57 | ⚪ **CASH** | **+7.3 bps** (±11.5) | `-13.5 bps` | `+0.138 / +0.132` | `0.35%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,320.94 | ⚪ **CASH** | **+4.0 bps** (±11.0) | `+1.2 bps` | `-0.012 / +0.038` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.38 | ⚪ **CASH** | **+9.0 bps** (±14.6) | `+4.9 bps` | `+0.091 / -0.026` | `0.51%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 08:47:12 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,952.41 | ⚪ **CASH** | **+4.4 bps** (±10.5) | `-14.1 bps` | `+0.135 / +0.063` | `0.35%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,314.74 | ⚪ **CASH** | **-4.7 bps** (±5.8) | `-5.0 bps` | `-0.009 / -0.128` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $99.94 | ⚪ **CASH** | **+4.0 bps** (±5.9) | `-5.2 bps` | `+0.083 / -0.018` | `0.51%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 08:32:42 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,061.40 | ⚪ **CASH** | **+4.4 bps** (±10.5) | `-14.1 bps` | `+0.135 / +0.063` | `0.35%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,316.12 | ⚪ **CASH** | **-4.7 bps** (±5.8) | `-5.0 bps` | `-0.009 / -0.128` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.05 | ⚪ **CASH** | **+4.0 bps** (±5.9) | `-5.2 bps` | `+0.083 / -0.018` | `0.51%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 08:17:13 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,019.14 | ⚪ **CASH** | **+4.4 bps** (±10.5) | `-14.1 bps` | `+0.135 / +0.063` | `0.35%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,316.86 | ⚪ **CASH** | **-4.7 bps** (±5.8) | `-5.0 bps` | `-0.009 / -0.128` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.02 | ⚪ **CASH** | **+4.0 bps** (±5.9) | `-5.2 bps` | `+0.083 / -0.018` | `0.51%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
