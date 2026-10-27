# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-27 09:17:17 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-27 09:17:17 UTC` | Patrimônio: **$993.64 USDT** (Caixa: `$993.64`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,718.08 | ⚪ **CASH** | **+11.2 bps** (±10.6) | `-7.4 bps` | `+0.154 / +0.105` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,309.97 | ⚪ **CASH** | **+10.5 bps** (±7.0) | `+4.4 bps` | `+0.067 / +0.028` | `0.41%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $99.74 | ⚪ **CASH** | **-0.1 bps** (±5.8) | `-16.9 bps` | `+0.086 / +0.028` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 09:02:14 UTC` | Patrimônio: **$993.64 USDT** (Caixa: `$993.64`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,868.00 | ⚪ **CASH** | **+11.2 bps** (±10.6) | `-7.4 bps` | `+0.154 / +0.105` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,314.06 | ⚪ **CASH** | **+10.5 bps** (±7.0) | `+4.4 bps` | `+0.067 / +0.028` | `0.41%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $99.98 | ⚪ **CASH** | **-0.1 bps** (±5.8) | `-16.9 bps` | `+0.086 / +0.028` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 08:47:10 UTC` | Patrimônio: **$993.64 USDT** (Caixa: `$993.64`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,821.48 | ⚪ **CASH** | **+5.5 bps** (±10.0) | `-12.8 bps` | `+0.150 / +0.039` | `0.29%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,311.91 | ⚪ **CASH** | **+9.0 bps** (±5.8) | `+8.8 bps` | `+0.068 / -0.085` | `0.41%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $99.85 | ⚪ **CASH** | **-1.7 bps** (±5.6) | `-20.6 bps` | `+0.086 / +0.040` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 08:32:25 UTC` | Patrimônio: **$993.64 USDT** (Caixa: `$993.64`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,786.00 | ⚪ **CASH** | **+5.5 bps** (±10.0) | `-12.8 bps` | `+0.150 / +0.039` | `0.29%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,313.32 | ⚪ **CASH** | **+9.0 bps** (±5.8) | `+8.8 bps` | `+0.068 / -0.085` | `0.41%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $99.86 | ⚪ **CASH** | **-1.7 bps** (±5.6) | `-20.6 bps` | `+0.086 / +0.040` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 08:17:03 UTC` | Patrimônio: **$993.64 USDT** (Caixa: `$993.64`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,843.14 | ⚪ **CASH** | **+5.5 bps** (±10.0) | `-12.8 bps` | `+0.150 / +0.039` | `0.29%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,314.14 | ⚪ **CASH** | **+9.0 bps** (±5.8) | `+8.8 bps` | `+0.068 / -0.085` | `0.41%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $99.88 | ⚪ **CASH** | **-1.7 bps** (±5.6) | `-20.6 bps` | `+0.086 / +0.040` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 08:02:28 UTC` | Patrimônio: **$993.64 USDT** (Caixa: `$993.64`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,904.40 | ⚪ **CASH** | **+5.5 bps** (±10.0) | `-12.8 bps` | `+0.150 / +0.039` | `0.29%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,316.86 | 🔴 **SELL** | **+9.0 bps** (±5.8) | `+8.8 bps` | `+0.068 / -0.085` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Alvo temporal de 12h concluído (+0.03%) |
| **SOLUSDT** | $100.13 | ⚪ **CASH** | **-1.7 bps** (±5.6) | `-20.6 bps` | `+0.086 / +0.040` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 07:46:59 UTC` | Patrimônio: **$992.93 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,656.00 | ⚪ **CASH** | **+7.0 bps** (±5.0) | `-13.0 bps` | `+0.157 / +0.052` | `0.29%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,309.03 | 🟡 **HOLD** | **+3.4 bps** (±5.2) | `-0.0 bps` | `+0.067 / -0.110` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 11.7h (PnL: -0.30% | Pico: +0.63%) |
| **SOLUSDT** | $99.79 | ⚪ **CASH** | **-0.2 bps** (±5.8) | `-16.1 bps` | `+0.086 / +0.012` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 07:32:03 UTC` | Patrimônio: **$992.93 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,736.34 | ⚪ **CASH** | **+7.0 bps** (±5.0) | `-13.0 bps` | `+0.157 / +0.052` | `0.29%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,309.04 | 🟡 **HOLD** | **+3.4 bps** (±5.2) | `-0.0 bps` | `+0.067 / -0.110` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 11.5h (PnL: -0.30% | Pico: +0.63%) |
| **SOLUSDT** | $99.77 | ⚪ **CASH** | **-0.2 bps** (±5.8) | `-16.1 bps` | `+0.086 / +0.012` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 07:17:22 UTC` | Patrimônio: **$992.29 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,656.35 | ⚪ **CASH** | **+7.0 bps** (±5.0) | `-13.0 bps` | `+0.157 / +0.052` | `0.29%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,304.56 | 🟡 **HOLD** | **+3.4 bps** (±5.2) | `-0.0 bps` | `+0.067 / -0.110` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 11.3h (PnL: -0.50% | Pico: +0.63%) |
| **SOLUSDT** | $99.67 | ⚪ **CASH** | **-0.2 bps** (±5.8) | `-16.1 bps` | `+0.086 / +0.012` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 07:02:29 UTC` | Patrimônio: **$991.83 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,603.40 | ⚪ **CASH** | **+7.0 bps** (±5.0) | `-13.0 bps` | `+0.157 / +0.052` | `0.29%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,301.31 | 🟡 **HOLD** | **+3.4 bps** (±5.2) | `-0.0 bps` | `+0.067 / -0.110` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 11.0h (PnL: -0.64% | Pico: +0.63%) |
| **SOLUSDT** | $99.54 | ⚪ **CASH** | **-0.2 bps** (±5.8) | `-16.1 bps` | `+0.086 / +0.012` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 06:46:52 UTC` | Patrimônio: **$992.68 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,700.01 | ⚪ **CASH** | **+9.2 bps** (±5.7) | `-13.5 bps` | `+0.162 / +0.113` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,307.32 | 🟡 **HOLD** | **+11.8 bps** (±6.1) | `+7.0 bps` | `+0.070 / +0.009` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 10.7h (PnL: -0.38% | Pico: +0.63%) |
| **SOLUSDT** | $99.82 | ⚪ **CASH** | **-1.8 bps** (±6.2) | `-20.8 bps` | `+0.090 / +0.030` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 06:32:08 UTC` | Patrimônio: **$993.34 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,817.61 | ⚪ **CASH** | **+9.2 bps** (±5.7) | `-13.5 bps` | `+0.162 / +0.113` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,311.92 | 🟡 **HOLD** | **+11.8 bps** (±6.1) | `+7.0 bps` | `+0.070 / +0.009` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 10.5h (PnL: -0.18% | Pico: +0.63%) |
| **SOLUSDT** | $99.99 | ⚪ **CASH** | **-1.8 bps** (±6.2) | `-20.8 bps` | `+0.090 / +0.030` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 06:16:57 UTC` | Patrimônio: **$993.14 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,870.81 | ⚪ **CASH** | **+9.2 bps** (±5.7) | `-13.5 bps` | `+0.162 / +0.113` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,310.53 | 🟡 **HOLD** | **+11.8 bps** (±6.1) | `+7.0 bps` | `+0.070 / +0.009` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 10.2h (PnL: -0.24% | Pico: +0.63%) |
| **SOLUSDT** | $99.87 | ⚪ **CASH** | **-1.8 bps** (±6.2) | `-20.8 bps` | `+0.090 / +0.030` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 06:02:11 UTC` | Patrimônio: **$993.64 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,906.00 | ⚪ **CASH** | **+9.2 bps** (±5.7) | `-13.5 bps` | `+0.162 / +0.113` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,314.07 | 🟡 **HOLD** | **+11.8 bps** (±6.1) | `+7.0 bps` | `+0.070 / +0.009` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 10.0h (PnL: -0.09% | Pico: +0.63%) |
| **SOLUSDT** | $100.10 | ⚪ **CASH** | **-1.8 bps** (±6.2) | `-20.8 bps` | `+0.090 / +0.030` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 05:47:28 UTC` | Patrimônio: **$993.88 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,966.65 | ⚪ **CASH** | **+8.6 bps** (±6.4) | `-14.1 bps` | `+0.165 / +0.101` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,315.77 | 🟡 **HOLD** | **+13.7 bps** (±10.5) | `+9.6 bps` | `+0.074 / +0.029` | `0.41%/h` | `vol_compressed` | Posição ativa há 9.8h (PnL: -0.01% | Pico: +0.63%) |
| **SOLUSDT** | $100.22 | ⚪ **CASH** | **+0.3 bps** (±6.0) | `-17.0 bps` | `+0.093 / +0.023` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 05:32:14 UTC` | Patrimônio: **$993.04 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,799.77 | ⚪ **CASH** | **+8.6 bps** (±6.4) | `-14.1 bps` | `+0.165 / +0.101` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,309.85 | 🟡 **HOLD** | **+13.7 bps** (±10.5) | `+9.6 bps` | `+0.074 / +0.029` | `0.41%/h` | `vol_compressed` | Posição ativa há 9.5h (PnL: -0.27% | Pico: +0.63%) |
| **SOLUSDT** | $99.86 | ⚪ **CASH** | **+0.3 bps** (±6.0) | `-17.0 bps` | `+0.093 / +0.023` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 05:17:05 UTC` | Patrimônio: **$993.64 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,800.01 | ⚪ **CASH** | **+8.6 bps** (±6.4) | `-14.1 bps` | `+0.165 / +0.101` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,314.08 | 🟡 **HOLD** | **+13.7 bps** (±10.5) | `+9.6 bps` | `+0.074 / +0.029` | `0.41%/h` | `vol_compressed` | Posição ativa há 9.2h (PnL: -0.09% | Pico: +0.63%) |
| **SOLUSDT** | $100.10 | ⚪ **CASH** | **+0.3 bps** (±6.0) | `-17.0 bps` | `+0.093 / +0.023` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 05:02:17 UTC` | Patrimônio: **$993.90 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,806.82 | ⚪ **CASH** | **+8.6 bps** (±6.4) | `-14.1 bps` | `+0.165 / +0.101` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,315.92 | 🟡 **HOLD** | **+13.7 bps** (±10.5) | `+9.6 bps` | `+0.074 / +0.029` | `0.41%/h` | `vol_compressed` | Posição ativa há 9.0h (PnL: -0.01% | Pico: +0.63%) |
| **SOLUSDT** | $100.24 | ⚪ **CASH** | **+0.3 bps** (±6.0) | `-17.0 bps` | `+0.093 / +0.023` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 04:47:17 UTC` | Patrimônio: **$993.12 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,659.57 | ⚪ **CASH** | **+2.7 bps** (±9.4) | `-21.7 bps` | `+0.164 / +0.065` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,310.43 | 🟡 **HOLD** | **+21.7 bps** (±11.3) | `+20.7 bps` | `+0.079 / +0.075` | `0.42%/h` | `vol_compressed` | Posição ativa há 8.7h (PnL: -0.24% | Pico: +0.63%) |
| **SOLUSDT** | $100.01 | ⚪ **CASH** | **-0.7 bps** (±6.5) | `-20.4 bps` | `+0.092 / +0.049` | `0.45%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 04:32:10 UTC` | Patrimônio: **$993.71 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,748.00 | ⚪ **CASH** | **+2.7 bps** (±9.4) | `-21.7 bps` | `+0.164 / +0.065` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,314.59 | 🟡 **HOLD** | **+21.7 bps** (±11.3) | `+20.7 bps` | `+0.079 / +0.075` | `0.42%/h` | `vol_compressed` | Posição ativa há 8.5h (PnL: -0.06% | Pico: +0.63%) |
| **SOLUSDT** | $100.19 | ⚪ **CASH** | **-0.7 bps** (±6.5) | `-20.4 bps` | `+0.092 / +0.049` | `0.45%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 04:16:53 UTC` | Patrimônio: **$993.60 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,780.00 | ⚪ **CASH** | **+2.7 bps** (±9.4) | `-21.7 bps` | `+0.164 / +0.065` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,313.81 | 🟡 **HOLD** | **+21.7 bps** (±11.3) | `+20.7 bps` | `+0.079 / +0.075` | `0.42%/h` | `vol_compressed` | Posição ativa há 8.2h (PnL: -0.10% | Pico: +0.63%) |
| **SOLUSDT** | $100.13 | ⚪ **CASH** | **-0.7 bps** (±6.5) | `-20.4 bps` | `+0.092 / +0.049` | `0.45%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 04:02:01 UTC` | Patrimônio: **$993.41 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,800.01 | ⚪ **CASH** | **+2.7 bps** (±9.4) | `-21.7 bps` | `+0.164 / +0.065` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,312.44 | 🟡 **HOLD** | **+21.7 bps** (±11.3) | `+20.7 bps` | `+0.079 / +0.075` | `0.42%/h` | `vol_compressed` | Posição ativa há 8.0h (PnL: -0.16% | Pico: +0.63%) |
| **SOLUSDT** | $100.12 | ⚪ **CASH** | **-0.7 bps** (±6.5) | `-20.4 bps` | `+0.092 / +0.049` | `0.45%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 03:47:11 UTC` | Patrimônio: **$993.95 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,858.35 | ⚪ **CASH** | **+4.4 bps** (±11.3) | `-20.7 bps` | `+0.156 / +0.117` | `0.30%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,316.22 | 🟡 **HOLD** | **+21.1 bps** (±8.0) | `+19.5 bps` | `+0.072 / +0.084` | `0.42%/h` | `vol_compressed` | Posição ativa há 7.7h (PnL: +0.01% | Pico: +0.63%) |
| **SOLUSDT** | $100.17 | ⚪ **CASH** | **-3.4 bps** (±5.2) | `-24.5 bps` | `+0.080 / +0.056` | `0.46%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 03:32:14 UTC` | Patrimônio: **$993.94 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,819.42 | ⚪ **CASH** | **+4.4 bps** (±11.3) | `-20.7 bps` | `+0.156 / +0.117` | `0.30%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,316.18 | 🟡 **HOLD** | **+21.1 bps** (±8.0) | `+19.5 bps` | `+0.072 / +0.084` | `0.42%/h` | `vol_compressed` | Posição ativa há 7.5h (PnL: +0.00% | Pico: +0.63%) |
| **SOLUSDT** | $100.28 | ⚪ **CASH** | **-3.4 bps** (±5.2) | `-24.5 bps` | `+0.080 / +0.056` | `0.46%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 03:17:08 UTC` | Patrimônio: **$993.07 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,668.73 | ⚪ **CASH** | **+4.4 bps** (±11.3) | `-20.7 bps` | `+0.156 / +0.117` | `0.30%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,310.03 | 🟡 **HOLD** | **+21.1 bps** (±8.0) | `+19.5 bps` | `+0.072 / +0.084` | `0.42%/h` | `vol_compressed` | Posição ativa há 7.2h (PnL: -0.26% | Pico: +0.63%) |
| **SOLUSDT** | $99.99 | ⚪ **CASH** | **-3.4 bps** (±5.2) | `-24.5 bps` | `+0.080 / +0.056` | `0.46%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 03:02:08 UTC` | Patrimônio: **$993.41 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,782.01 | ⚪ **CASH** | **+4.4 bps** (±11.3) | `-20.7 bps` | `+0.156 / +0.117` | `0.30%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,312.41 | 🟡 **HOLD** | **+21.1 bps** (±8.0) | `+19.5 bps` | `+0.072 / +0.084` | `0.42%/h` | `vol_compressed` | Posição ativa há 7.0h (PnL: -0.16% | Pico: +0.63%) |
| **SOLUSDT** | $100.20 | ⚪ **CASH** | **-3.4 bps** (±5.2) | `-24.5 bps` | `+0.080 / +0.056` | `0.46%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 02:47:02 UTC` | Patrimônio: **$994.07 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,958.69 | ⚪ **CASH** | **+6.8 bps** (±9.2) | `-21.0 bps` | `+0.160 / +0.175` | `0.30%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,317.13 | 🟡 **HOLD** | **+21.7 bps** (±7.1) | `+22.7 bps` | `+0.063 / +0.062` | `0.42%/h` | `vol_compressed` | Posição ativa há 6.7h (PnL: +0.05% | Pico: +0.63%) |
| **SOLUSDT** | $100.31 | ⚪ **CASH** | **-2.7 bps** (±9.9) | `-23.2 bps` | `+0.067 / +0.086` | `0.46%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 02:32:12 UTC` | Patrimônio: **$994.35 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,986.73 | ⚪ **CASH** | **+6.8 bps** (±9.2) | `-21.0 bps` | `+0.160 / +0.175` | `0.30%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,319.11 | 🟡 **HOLD** | **+21.7 bps** (±7.1) | `+22.7 bps` | `+0.063 / +0.062` | `0.42%/h` | `vol_compressed` | Posição ativa há 6.5h (PnL: +0.13% | Pico: +0.63%) |
| **SOLUSDT** | $100.50 | ⚪ **CASH** | **-2.7 bps** (±9.9) | `-23.2 bps` | `+0.067 / +0.086` | `0.46%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 02:17:11 UTC` | Patrimônio: **$994.78 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,079.86 | ⚪ **CASH** | **+6.8 bps** (±9.2) | `-21.0 bps` | `+0.160 / +0.175` | `0.30%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,322.09 | 🟡 **HOLD** | **+21.7 bps** (±7.1) | `+22.7 bps` | `+0.063 / +0.062` | `0.42%/h` | `vol_compressed` | Posição ativa há 6.2h (PnL: +0.26% | Pico: +0.63%) |
| **SOLUSDT** | $100.62 | ⚪ **CASH** | **-2.7 bps** (±9.9) | `-23.2 bps` | `+0.067 / +0.086` | `0.46%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 02:02:30 UTC` | Patrimônio: **$994.73 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,042.00 | ⚪ **CASH** | **+6.8 bps** (±9.2) | `-21.0 bps` | `+0.160 / +0.175` | `0.30%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,321.75 | 🟡 **HOLD** | **+21.7 bps** (±7.1) | `+22.7 bps` | `+0.063 / +0.062` | `0.42%/h` | `vol_compressed` | Posição ativa há 6.0h (PnL: +0.25% | Pico: +0.63%) |
| **SOLUSDT** | $100.60 | ⚪ **CASH** | **-2.7 bps** (±9.9) | `-23.2 bps` | `+0.067 / +0.086` | `0.46%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 01:47:01 UTC` | Patrimônio: **$996.00 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,312.28 | ⚪ **CASH** | **+6.8 bps** (±8.7) | `-21.4 bps` | `+0.151 / +0.201` | `0.30%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,330.73 | 🟡 **HOLD** | **+21.8 bps** (±7.5) | `+25.4 bps` | `+0.046 / +0.055` | `0.43%/h` | `vol_compressed` | Posição ativa há 5.7h (PnL: +0.63% | Pico: +0.63%) |
| **SOLUSDT** | $100.92 | ⚪ **CASH** | **+1.8 bps** (±3.8) | `-19.3 bps` | `+0.064 / +0.146` | `0.47%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 01:32:09 UTC` | Patrimônio: **$994.93 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,168.00 | ⚪ **CASH** | **+6.8 bps** (±8.7) | `-21.4 bps` | `+0.151 / +0.201` | `0.30%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,323.16 | 🟡 **HOLD** | **+21.8 bps** (±7.5) | `+25.4 bps` | `+0.046 / +0.055` | `0.43%/h` | `vol_compressed` | Posição ativa há 5.5h (PnL: +0.31% | Pico: +0.59%) |
| **SOLUSDT** | $100.64 | ⚪ **CASH** | **+1.8 bps** (±3.8) | `-19.3 bps` | `+0.064 / +0.146` | `0.47%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 01:17:11 UTC` | Patrimônio: **$995.85 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,286.87 | ⚪ **CASH** | **+6.8 bps** (±8.7) | `-21.4 bps` | `+0.151 / +0.201` | `0.30%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,329.65 | 🟡 **HOLD** | **+21.8 bps** (±7.5) | `+25.4 bps` | `+0.046 / +0.055` | `0.43%/h` | `vol_compressed` | Posição ativa há 5.2h (PnL: +0.59% | Pico: +0.59%) |
| **SOLUSDT** | $100.90 | ⚪ **CASH** | **+1.8 bps** (±3.8) | `-19.3 bps` | `+0.064 / +0.146` | `0.47%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 01:02:16 UTC` | Patrimônio: **$995.53 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,244.91 | ⚪ **CASH** | **+6.8 bps** (±8.7) | `-21.4 bps` | `+0.151 / +0.201` | `0.30%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,327.40 | 🟡 **HOLD** | **+21.8 bps** (±7.5) | `+25.4 bps` | `+0.046 / +0.055` | `0.43%/h` | `vol_compressed` | Posição ativa há 5.0h (PnL: +0.49% | Pico: +0.57%) |
| **SOLUSDT** | $100.87 | ⚪ **CASH** | **+1.8 bps** (±3.8) | `-19.3 bps` | `+0.064 / +0.146` | `0.47%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 00:47:08 UTC` | Patrimônio: **$995.73 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,292.01 | ⚪ **CASH** | **+14.1 bps** (±9.2) | `-6.1 bps` | `+0.137 / +0.201` | `0.31%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,328.82 | 🟡 **HOLD** | **+19.2 bps** (±8.5) | `+23.5 bps` | `+0.035 / +0.042` | `0.44%/h` | Liberado ✅ | Posição ativa há 4.7h (PnL: +0.55% | Pico: +0.57%) |
| **SOLUSDT** | $100.93 | ⚪ **CASH** | **-1.4 bps** (±6.3) | `-24.2 bps` | `+0.063 / +0.152` | `0.47%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 00:32:08 UTC` | Patrimônio: **$995.78 USDT** (Caixa: `$665.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,290.00 | ⚪ **CASH** | **+14.1 bps** (±9.2) | `-6.1 bps` | `+0.137 / +0.201` | `0.31%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,329.16 | 🟡 **HOLD** | **+19.2 bps** (±8.5) | `+23.5 bps` | `+0.035 / +0.042` | `0.44%/h` | Liberado ✅ | Posição ativa há 4.5h (PnL: +0.57% | Pico: +0.57%) |
| **SOLUSDT** | $100.96 | ⚪ **CASH** | **-1.4 bps** (±6.3) | `-24.2 bps` | `+0.063 / +0.152` | `0.47%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
