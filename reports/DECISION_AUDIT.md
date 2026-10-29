# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-29 02:32:48 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-29 02:32:48 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,912.01 | ⚪ **CASH** | **-3.9 bps** (±7.1) | `-26.7 bps` | `+0.140 / +0.005` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,303.62 | ⚪ **CASH** | **+10.6 bps** (±13.3) | `+14.7 bps` | `+0.021 / -0.028` | `0.46%/h` | `weak_order_flow` `stretched_top` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $99.52 | ⚪ **CASH** | **+15.0 bps** (±11.1) | `+13.5 bps` | `+0.112 / -0.032` | `0.54%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 02:02:33 UTC` | Patrimônio: **$992.96 USDT** (Caixa: `$992.96`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,166.06 | ⚪ **CASH** | **-3.9 bps** (±7.1) | `-26.7 bps` | `+0.140 / +0.005` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,317.01 | 🔴 **SELL** | **+10.6 bps** (±13.3) | `+14.7 bps` | `+0.021 / -0.028` | `0.46%/h` | `weak_order_flow` `stretched_top` | Stop Loss técnico acionado (-1.84%) |
| **SOLUSDT** | $100.07 | ⚪ **CASH** | **+15.0 bps** (±11.1) | `+13.5 bps` | `+0.112 / -0.032` | `0.54%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 01:47:43 UTC` | Patrimônio: **$994.27 USDT** (Caixa: `$776.33`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,475.90 | ⚪ **CASH** | **+22.0 bps** (±10.6) | `+2.8 bps` | `+0.178 / +0.198` | `0.28%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,328.22 | 🟡 **HOLD** | **+14.9 bps** (±5.4) | `+3.7 bps` | `+0.059 / +0.152` | `0.35%/h` | Liberado ✅ | Posição ativa há 4.8h (PnL: -1.37% | Pico: +0.28%) |
| **SOLUSDT** | $100.60 | ⚪ **CASH** | **+9.7 bps** (±10.1) | `-9.1 bps` | `+0.139 / +0.095` | `0.42%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 01:32:42 UTC` | Patrimônio: **$995.58 USDT** (Caixa: `$776.33`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,798.86 | ⚪ **CASH** | **+22.0 bps** (±10.6) | `+2.8 bps` | `+0.178 / +0.198` | `0.28%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,342.29 | 🟡 **HOLD** | **+14.9 bps** (±5.4) | `+3.7 bps` | `+0.059 / +0.152` | `0.35%/h` | Liberado ✅ | Posição ativa há 4.5h (PnL: -0.77% | Pico: +0.28%) |
| **SOLUSDT** | $101.34 | ⚪ **CASH** | **+9.7 bps** (±10.1) | `-9.1 bps` | `+0.139 / +0.095` | `0.42%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 01:17:21 UTC` | Patrimônio: **$996.17 USDT** (Caixa: `$776.33`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,992.01 | ⚪ **CASH** | **+22.0 bps** (±10.6) | `+2.8 bps` | `+0.178 / +0.198` | `0.28%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,348.52 | 🟡 **HOLD** | **+14.9 bps** (±5.4) | `+3.7 bps` | `+0.059 / +0.152` | `0.35%/h` | Liberado ✅ | Posição ativa há 4.2h (PnL: -0.51% | Pico: +0.28%) |
| **SOLUSDT** | $101.68 | ⚪ **CASH** | **+9.7 bps** (±10.1) | `-9.1 bps` | `+0.139 / +0.095` | `0.42%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 01:02:33 UTC` | Patrimônio: **$996.48 USDT** (Caixa: `$776.33`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,053.01 | ⚪ **CASH** | **+22.0 bps** (±10.6) | `+2.8 bps` | `+0.178 / +0.198` | `0.28%/h` | `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,351.91 | 🟡 **HOLD** | **+14.9 bps** (±5.4) | `+3.7 bps` | `+0.059 / +0.152` | `0.35%/h` | Liberado ✅ | Posição ativa há 4.0h (PnL: -0.37% | Pico: +0.28%) |
| **SOLUSDT** | $101.72 | ⚪ **CASH** | **+9.7 bps** (±10.1) | `-9.1 bps` | `+0.139 / +0.095` | `0.42%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 00:47:30 UTC` | Patrimônio: **$996.99 USDT** (Caixa: `$776.33`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,170.00 | ⚪ **CASH** | **+25.4 bps** (±9.5) | `+8.3 bps` | `+0.164 / +0.235` | `0.28%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,357.37 | 🟡 **HOLD** | **+18.0 bps** (±5.7) | `+9.6 bps` | `+0.060 / +0.156` | `0.36%/h` | Liberado ✅ | Posição ativa há 3.7h (PnL: -0.13% | Pico: +0.28%) |
| **SOLUSDT** | $102.05 | ⚪ **CASH** | **+10.8 bps** (±7.6) | `-12.9 bps` | `+0.136 / +0.192` | `0.41%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 00:32:34 UTC` | Patrimônio: **$996.85 USDT** (Caixa: `$776.33`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,182.15 | ⚪ **CASH** | **+25.4 bps** (±9.5) | `+8.3 bps` | `+0.164 / +0.235` | `0.28%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,355.79 | 🟡 **HOLD** | **+18.0 bps** (±5.7) | `+9.6 bps` | `+0.060 / +0.156` | `0.36%/h` | Liberado ✅ | Posição ativa há 3.5h (PnL: -0.20% | Pico: +0.28%) |
| **SOLUSDT** | $102.21 | ⚪ **CASH** | **+10.8 bps** (±7.6) | `-12.9 bps` | `+0.136 / +0.192` | `0.41%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 00:17:50 UTC` | Patrimônio: **$997.00 USDT** (Caixa: `$776.33`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,280.00 | ⚪ **CASH** | **+25.4 bps** (±9.5) | `+8.3 bps` | `+0.164 / +0.235` | `0.28%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,357.38 | 🟡 **HOLD** | **+18.0 bps** (±5.7) | `+9.6 bps` | `+0.060 / +0.156` | `0.36%/h` | Liberado ✅ | Posição ativa há 3.3h (PnL: -0.13% | Pico: +0.28%) |
| **SOLUSDT** | $102.40 | ⚪ **CASH** | **+10.8 bps** (±7.6) | `-12.9 bps` | `+0.136 / +0.192` | `0.41%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-29 00:02:41 UTC` | Patrimônio: **$997.11 USDT** (Caixa: `$776.33`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,300.01 | ⚪ **CASH** | **+25.4 bps** (±9.5) | `+8.3 bps` | `+0.164 / +0.235` | `0.28%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **ETHUSDT** | $2,358.61 | 🟡 **HOLD** | **+18.0 bps** (±5.7) | `+9.6 bps` | `+0.060 / +0.156` | `0.36%/h` | Liberado ✅ | Posição ativa há 3.0h (PnL: -0.08% | Pico: +0.28%) |
| **SOLUSDT** | $102.35 | ⚪ **CASH** | **+10.8 bps** (±7.6) | `-12.9 bps` | `+0.136 / +0.192` | `0.41%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 23:47:28 UTC` | Patrimônio: **$997.15 USDT** (Caixa: `$776.33`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,324.00 | ⚪ **CASH** | **+21.5 bps** (±6.7) | `-2.0 bps` | `+0.167 / +0.270` | `0.29%/h` | `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,359.05 | 🟡 **HOLD** | **+22.1 bps** (±8.8) | `+15.9 bps` | `+0.065 / +0.171` | `0.36%/h` | Liberado ✅ | Posição ativa há 2.7h (PnL: -0.06% | Pico: +0.28%) |
| **SOLUSDT** | $102.39 | ⚪ **CASH** | **+19.1 bps** (±8.2) | `+0.9 bps` | `+0.130 / +0.220` | `0.42%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 23:32:19 UTC` | Patrimônio: **$997.22 USDT** (Caixa: `$776.33`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,303.32 | ⚪ **CASH** | **+21.5 bps** (±6.7) | `-2.0 bps` | `+0.167 / +0.270` | `0.29%/h` | `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,359.80 | 🟡 **HOLD** | **+22.1 bps** (±8.8) | `+15.9 bps` | `+0.065 / +0.171` | `0.36%/h` | Liberado ✅ | Posição ativa há 2.5h (PnL: -0.03% | Pico: +0.28%) |
| **SOLUSDT** | $102.40 | ⚪ **CASH** | **+19.1 bps** (±8.2) | `+0.9 bps` | `+0.130 / +0.220` | `0.42%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 23:17:36 UTC` | Patrimônio: **$997.19 USDT** (Caixa: `$776.33`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,302.37 | ⚪ **CASH** | **+21.5 bps** (±6.7) | `-2.0 bps` | `+0.167 / +0.270` | `0.29%/h` | `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,359.44 | 🟡 **HOLD** | **+22.1 bps** (±8.8) | `+15.9 bps` | `+0.065 / +0.171` | `0.36%/h` | Liberado ✅ | Posição ativa há 2.2h (PnL: -0.05% | Pico: +0.28%) |
| **SOLUSDT** | $102.45 | ⚪ **CASH** | **+19.1 bps** (±8.2) | `+0.9 bps` | `+0.130 / +0.220` | `0.42%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 23:02:37 UTC` | Patrimônio: **$996.93 USDT** (Caixa: `$776.33`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,200.01 | ⚪ **CASH** | **+21.5 bps** (±6.7) | `-2.0 bps` | `+0.167 / +0.270` | `0.29%/h` | `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,356.70 | 🟡 **HOLD** | **+22.1 bps** (±8.8) | `+15.9 bps` | `+0.065 / +0.171` | `0.36%/h` | Liberado ✅ | Posição ativa há 2.0h (PnL: -0.16% | Pico: +0.28%) |
| **SOLUSDT** | $102.35 | ⚪ **CASH** | **+19.1 bps** (±8.2) | `+0.9 bps` | `+0.130 / +0.220` | `0.42%/h` | `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 22:47:26 UTC` | Patrimônio: **$997.55 USDT** (Caixa: `$776.33`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,360.01 | ⚪ **CASH** | **+22.3 bps** (±6.2) | `-2.4 bps` | `+0.166 / +0.301` | `0.29%/h` | `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,363.32 | 🟡 **HOLD** | **+20.9 bps** (±10.5) | `+17.3 bps` | `+0.054 / +0.140` | `0.37%/h` | Liberado ✅ | Posição ativa há 1.7h (PnL: +0.12% | Pico: +0.28%) |
| **SOLUSDT** | $102.70 | ⚪ **CASH** | **+26.2 bps** (±8.4) | `+14.2 bps` | `+0.122 / +0.225` | `0.42%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-10-28 22:32:24 UTC` | Patrimônio: **$997.92 USDT** (Caixa: `$776.33`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,432.01 | ⚪ **CASH** | **+22.3 bps** (±6.2) | `-2.4 bps` | `+0.166 / +0.301` | `0.29%/h` | `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,367.21 | 🟡 **HOLD** | **+20.9 bps** (±10.5) | `+17.3 bps` | `+0.054 / +0.140` | `0.37%/h` | Liberado ✅ | Posição ativa há 1.5h (PnL: +0.28% | Pico: +0.28%) |
| **SOLUSDT** | $102.80 | ⚪ **CASH** | **+26.2 bps** (±8.4) | `+14.2 bps` | `+0.122 / +0.225` | `0.42%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-10-28 22:17:26 UTC` | Patrimônio: **$997.03 USDT** (Caixa: `$776.33`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,233.37 | ⚪ **CASH** | **+22.3 bps** (±6.2) | `-2.4 bps` | `+0.166 / +0.301` | `0.29%/h` | `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,357.72 | 🟡 **HOLD** | **+20.9 bps** (±10.5) | `+17.3 bps` | `+0.054 / +0.140` | `0.37%/h` | Liberado ✅ | Posição ativa há 1.2h (PnL: -0.12% | Pico: +0.21%) |
| **SOLUSDT** | $102.42 | ⚪ **CASH** | **+26.2 bps** (±8.4) | `+14.2 bps` | `+0.122 / +0.225` | `0.42%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-10-28 22:04:06 UTC` | Patrimônio: **$997.17 USDT** (Caixa: `$776.33`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,236.06 | 🔴 **SELL** | **+22.3 bps** (±6.2) | `-2.4 bps` | `+0.166 / +0.301` | `0.29%/h` | Liberado ✅ | Alvo temporal de 12h concluído (-0.40%) |
| **ETHUSDT** | $2,359.20 | 🟡 **HOLD** | **+20.9 bps** (±10.5) | `+17.3 bps` | `+0.054 / +0.140` | `0.37%/h` | Liberado ✅ | Posição ativa há 1.0h (PnL: -0.06% | Pico: +0.21%) |
| **SOLUSDT** | $102.46 | ⚪ **CASH** | **+26.2 bps** (±8.4) | `+14.2 bps` | `+0.122 / +0.225` | `0.42%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-10-28 21:47:23 UTC` | Patrimônio: **$998.39 USDT** (Caixa: `$448.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,314.01 | 🟡 **HOLD** | **+21.7 bps** (±8.8) | `-3.1 bps` | `+0.165 / +0.303` | `0.30%/h` | Liberado ✅ | Posição ativa há 11.8h (PnL: -0.30% | Pico: +0.25%) |
| **ETHUSDT** | $2,364.75 | 🟡 **HOLD** | **+27.3 bps** (±15.3) | `+32.1 bps` | `+0.045 / +0.118` | `0.37%/h` | Liberado ✅ | Posição ativa há 0.7h (PnL: +0.18% | Pico: +0.21%) |
| **SOLUSDT** | $102.63 | ⚪ **CASH** | **+29.9 bps** (±11.0) | `+20.8 bps` | `+0.126 / +0.230` | `0.43%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-10-28 21:32:47 UTC` | Patrimônio: **$996.97 USDT** (Caixa: `$448.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,160.00 | 🟡 **HOLD** | **+21.7 bps** (±8.8) | `-3.1 bps` | `+0.165 / +0.303` | `0.30%/h` | Liberado ✅ | Posição ativa há 11.5h (PnL: -0.49% | Pico: +0.25%) |
| **ETHUSDT** | $2,356.20 | 🟡 **HOLD** | **+27.3 bps** (±15.3) | `+32.1 bps` | `+0.045 / +0.118` | `0.37%/h` | Liberado ✅ | Posição ativa há 0.5h (PnL: -0.18% | Pico: +0.21%) |
| **SOLUSDT** | $102.23 | ⚪ **CASH** | **+29.9 bps** (±11.0) | `+20.8 bps` | `+0.126 / +0.230` | `0.43%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-10-28 21:17:27 UTC` | Patrimônio: **$998.94 USDT** (Caixa: `$448.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,432.07 | 🟡 **HOLD** | **+21.7 bps** (±8.8) | `-3.1 bps` | `+0.165 / +0.303` | `0.30%/h` | Liberado ✅ | Posição ativa há 11.3h (PnL: -0.16% | Pico: +0.25%) |
| **ETHUSDT** | $2,365.49 | 🟡 **HOLD** | **+27.3 bps** (±15.3) | `+32.1 bps` | `+0.045 / +0.118` | `0.37%/h` | Liberado ✅ | Posição ativa há 0.2h (PnL: +0.21% | Pico: +0.21%) |
| **SOLUSDT** | $102.83 | ⚪ **CASH** | **+29.9 bps** (±11.0) | `+20.8 bps` | `+0.126 / +0.230` | `0.43%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-10-28 21:02:38 UTC` | Patrimônio: **$997.98 USDT** (Caixa: `$448.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,308.00 | 🟡 **HOLD** | **+21.7 bps** (±8.8) | `-3.1 bps` | `+0.165 / +0.303` | `0.30%/h` | Liberado ✅ | Posição ativa há 11.0h (PnL: -0.31% | Pico: +0.25%) |
| **ETHUSDT** | $2,360.55 | 🟢 **BUY** | **+27.3 bps** (±15.3) | `+32.1 bps` | `+0.045 / +0.118` | `0.37%/h` | Liberado ✅ | Entrada Swing 12h aprovada (Alpha +27.3 bps > 24.0 bps | CVD 24h +0.045) |
| **SOLUSDT** | $102.49 | ⚪ **CASH** | **+29.9 bps** (±11.0) | `+20.8 bps` | `+0.126 / +0.230` | `0.43%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-10-28 20:47:31 UTC` | Patrimônio: **$997.14 USDT** (Caixa: `$669.59`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,036.00 | 🟡 **HOLD** | **+37.9 bps** (±12.8) | `+26.1 bps` | `+0.166 / +0.315` | `0.29%/h` | `stretched_top` | Posição ativa há 10.8h (PnL: -0.64% | Pico: +0.25%) |
| **ETHUSDT** | $2,351.58 | ⚪ **CASH** | **+30.0 bps** (±18.0) | `+36.6 bps` | `+0.047 / +0.130` | `0.37%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $102.08 | ⚪ **CASH** | **+33.8 bps** (±6.1) | `+21.3 bps` | `+0.143 / +0.292` | `0.42%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-10-28 20:32:39 UTC` | Patrimônio: **$997.99 USDT** (Caixa: `$669.59`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,245.99 | 🟡 **HOLD** | **+37.9 bps** (±12.8) | `+26.1 bps` | `+0.166 / +0.315` | `0.29%/h` | `stretched_top` | Posição ativa há 10.5h (PnL: -0.38% | Pico: +0.25%) |
| **ETHUSDT** | $2,357.21 | ⚪ **CASH** | **+30.0 bps** (±18.0) | `+36.6 bps` | `+0.047 / +0.130` | `0.37%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $102.23 | ⚪ **CASH** | **+33.8 bps** (±6.1) | `+21.3 bps` | `+0.143 / +0.292` | `0.42%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-10-28 20:17:27 UTC` | Patrimônio: **$998.13 USDT** (Caixa: `$669.59`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,280.00 | 🟡 **HOLD** | **+37.9 bps** (±12.8) | `+26.1 bps` | `+0.166 / +0.315` | `0.29%/h` | `stretched_top` | Posição ativa há 10.3h (PnL: -0.34% | Pico: +0.25%) |
| **ETHUSDT** | $2,364.97 | ⚪ **CASH** | **+30.0 bps** (±18.0) | `+36.6 bps` | `+0.047 / +0.130` | `0.37%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $102.67 | 🔴 **SELL** | **+33.8 bps** (±6.1) | `+21.3 bps` | `+0.143 / +0.292` | `0.42%/h` | Liberado ✅ | Trailing Stop acionado (pico +1.59%, realizou +0.54%) |

---

### 🕒 Ciclo `2026-10-28 20:02:32 UTC` | Patrimônio: **$1,002.66 USDT** (Caixa: `$447.92`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,763.88 | 🟡 **HOLD** | **+37.9 bps** (±12.8) | `+26.1 bps` | `+0.166 / +0.315` | `0.29%/h` | `stretched_top` | Posição ativa há 10.0h (PnL: +0.25% | Pico: +0.25%) |
| **ETHUSDT** | $2,386.54 | ⚪ **CASH** | **+30.0 bps** (±18.0) | `+36.6 bps` | `+0.047 / +0.130` | `0.37%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $103.74 | 🟡 **HOLD** | **+33.8 bps** (±6.1) | `+21.3 bps` | `+0.143 / +0.292` | `0.42%/h` | Liberado ✅ | Posição ativa há 1.0h (PnL: +1.59% | Pico: +1.59%) |

---

### 🕒 Ciclo `2026-10-28 19:47:27 UTC` | Patrimônio: **$998.49 USDT** (Caixa: `$447.92`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,373.14 | 🟡 **HOLD** | **+29.0 bps** (±8.5) | `+16.8 bps` | `+0.150 / +0.236` | `0.27%/h` | `vol_compressed` | Posição ativa há 9.8h (PnL: -0.23% | Pico: +0.05%) |
| **ETHUSDT** | $2,364.96 | ⚪ **CASH** | **+28.1 bps** (±10.6) | `+39.3 bps` | `+0.032 / +0.050` | `0.36%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $102.54 | 🟡 **HOLD** | **+41.8 bps** (±19.3) | `+43.4 bps` | `+0.127 / +0.249` | `0.40%/h` | Liberado ✅ | Posição ativa há 0.7h (PnL: +0.41% | Pico: +0.41%) |

---

### 🕒 Ciclo `2026-10-28 19:32:25 UTC` | Patrimônio: **$997.27 USDT** (Caixa: `$447.92`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,215.02 | 🟡 **HOLD** | **+29.0 bps** (±8.5) | `+16.8 bps` | `+0.150 / +0.236` | `0.27%/h` | `vol_compressed` | Posição ativa há 9.5h (PnL: -0.42% | Pico: +0.05%) |
| **ETHUSDT** | $2,360.34 | ⚪ **CASH** | **+28.1 bps** (±10.6) | `+39.3 bps` | `+0.032 / +0.050` | `0.36%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $102.27 | 🟡 **HOLD** | **+41.8 bps** (±19.3) | `+43.4 bps` | `+0.127 / +0.249` | `0.40%/h` | Liberado ✅ | Posição ativa há 0.5h (PnL: +0.15% | Pico: +0.15%) |

---

### 🕒 Ciclo `2026-10-28 19:17:21 UTC` | Patrimônio: **$996.35 USDT** (Caixa: `$447.92`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,080.00 | 🟡 **HOLD** | **+29.0 bps** (±8.5) | `+16.8 bps` | `+0.150 / +0.236` | `0.27%/h` | `vol_compressed` | Posição ativa há 9.3h (PnL: -0.59% | Pico: +0.05%) |
| **ETHUSDT** | $2,355.32 | ⚪ **CASH** | **+28.1 bps** (±10.6) | `+39.3 bps` | `+0.032 / +0.050` | `0.36%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $102.10 | 🟡 **HOLD** | **+41.8 bps** (±19.3) | `+43.4 bps` | `+0.127 / +0.249` | `0.40%/h` | Liberado ✅ | Posição ativa há 0.2h (PnL: -0.02% | Pico: +0.00%) |

---

### 🕒 Ciclo `2026-10-28 19:02:47 UTC` | Patrimônio: **$996.26 USDT** (Caixa: `$447.92`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,046.19 | 🟡 **HOLD** | **+29.0 bps** (±8.5) | `+16.8 bps` | `+0.150 / +0.236` | `0.27%/h` | `vol_compressed` | Posição ativa há 9.0h (PnL: -0.63% | Pico: +0.05%) |
| **ETHUSDT** | $2,355.20 | ⚪ **CASH** | **+28.1 bps** (±10.6) | `+39.3 bps` | `+0.032 / +0.050` | `0.36%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $102.12 | 🟢 **BUY** | **+41.8 bps** (±19.3) | `+43.4 bps` | `+0.127 / +0.249` | `0.40%/h` | Liberado ✅ | Entrada Swing 12h aprovada (Alpha +41.8 bps > 24.0 bps | CVD 24h +0.127) |

---

### 🕒 Ciclo `2026-10-28 18:47:40 UTC` | Patrimônio: **$996.58 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,059.39 | 🟡 **HOLD** | **+25.9 bps** (±5.1) | `+13.9 bps` | `+0.153 / +0.179` | `0.27%/h` | Liberado ✅ | Posição ativa há 8.8h (PnL: -0.61% | Pico: +0.05%) |
| **ETHUSDT** | $2,355.50 | ⚪ **CASH** | **-1.6 bps** (±11.1) | `-10.7 bps` | `+0.032 / -0.014` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.16 | ⚪ **CASH** | **+10.0 bps** (±11.6) | `-3.1 bps` | `+0.086 / +0.113` | `0.40%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 18:32:33 UTC` | Patrimônio: **$995.61 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,820.01 | 🟡 **HOLD** | **+25.9 bps** (±5.1) | `+13.9 bps` | `+0.153 / +0.179` | `0.27%/h` | Liberado ✅ | Posição ativa há 8.5h (PnL: -0.91% | Pico: +0.05%) |
| **ETHUSDT** | $2,342.46 | ⚪ **CASH** | **-1.6 bps** (±11.1) | `-10.7 bps` | `+0.032 / -0.014` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.33 | ⚪ **CASH** | **+10.0 bps** (±11.6) | `-3.1 bps` | `+0.086 / +0.113` | `0.40%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 18:19:30 UTC` | Patrimônio: **$995.61 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,819.56 | 🟡 **HOLD** | **+25.9 bps** (±5.1) | `+13.9 bps` | `+0.153 / +0.179` | `0.27%/h` | Liberado ✅ | Posição ativa há 8.3h (PnL: -0.91% | Pico: +0.05%) |
| **ETHUSDT** | $2,344.52 | ⚪ **CASH** | **-1.6 bps** (±11.1) | `-10.7 bps` | `+0.032 / -0.014` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.50 | ⚪ **CASH** | **+10.0 bps** (±11.6) | `-3.1 bps` | `+0.086 / +0.113` | `0.40%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 18:02:31 UTC` | Patrimônio: **$996.15 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,953.88 | 🟡 **HOLD** | **+25.9 bps** (±5.1) | `+13.9 bps` | `+0.153 / +0.179` | `0.27%/h` | Liberado ✅ | Posição ativa há 8.0h (PnL: -0.74% | Pico: +0.05%) |
| **ETHUSDT** | $2,347.83 | ⚪ **CASH** | **-1.6 bps** (±11.1) | `-10.7 bps` | `+0.032 / -0.014` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.73 | ⚪ **CASH** | **+10.0 bps** (±11.6) | `-3.1 bps` | `+0.086 / +0.113` | `0.40%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 17:47:30 UTC` | Patrimônio: **$995.25 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,729.70 | 🟡 **HOLD** | **+23.3 bps** (±6.2) | `+14.8 bps` | `+0.147 / +0.108` | `0.27%/h` | Liberado ✅ | Posição ativa há 7.8h (PnL: -1.02% | Pico: +0.05%) |
| **ETHUSDT** | $2,340.93 | ⚪ **CASH** | **-5.4 bps** (±8.3) | `-15.5 bps` | `+0.030 / -0.046` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.48 | ⚪ **CASH** | **+6.8 bps** (±8.1) | `-2.1 bps` | `+0.068 / +0.032` | `0.40%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 17:32:27 UTC` | Patrimônio: **$994.73 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,602.01 | 🟡 **HOLD** | **+23.3 bps** (±6.2) | `+14.8 bps` | `+0.147 / +0.108` | `0.27%/h` | Liberado ✅ | Posição ativa há 7.5h (PnL: -1.17% | Pico: +0.05%) |
| **ETHUSDT** | $2,334.55 | ⚪ **CASH** | **-5.4 bps** (±8.3) | `-15.5 bps` | `+0.030 / -0.046` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.05 | ⚪ **CASH** | **+6.8 bps** (±8.1) | `-2.1 bps` | `+0.068 / +0.032` | `0.40%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
