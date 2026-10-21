# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-21 05:32:00 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-21 05:32:00 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,903.70 | ⚪ **CASH** | **-21.0 bps** (±6.2) | `-50.2 bps` | `+0.079 / +0.023` | `0.33%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,448.40 | ⚪ **CASH** | **+3.4 bps** (±11.8) | `-6.8 bps` | `+0.087 / +0.041` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.10 | ⚪ **CASH** | **-13.2 bps** (±4.7) | `-26.7 bps` | `+0.022 / -0.038` | `0.60%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 05:16:58 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,875.54 | ⚪ **CASH** | **-21.0 bps** (±6.2) | `-50.2 bps` | `+0.079 / +0.023` | `0.33%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,447.47 | ⚪ **CASH** | **+3.4 bps** (±11.8) | `-6.8 bps` | `+0.087 / +0.041` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.97 | ⚪ **CASH** | **-13.2 bps** (±4.7) | `-26.7 bps` | `+0.022 / -0.038` | `0.60%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 05:02:02 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,859.57 | ⚪ **CASH** | **-21.0 bps** (±6.2) | `-50.2 bps` | `+0.079 / +0.023` | `0.33%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,447.73 | ⚪ **CASH** | **+3.4 bps** (±11.8) | `-6.8 bps` | `+0.087 / +0.041` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.01 | ⚪ **CASH** | **-13.2 bps** (±4.7) | `-26.7 bps` | `+0.022 / -0.038` | `0.60%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 04:47:02 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,789.08 | ⚪ **CASH** | **-11.3 bps** (±10.8) | `-29.6 bps` | `+0.072 / +0.008` | `0.33%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,443.51 | ⚪ **CASH** | **+5.9 bps** (±10.3) | `-1.9 bps` | `+0.083 / +0.042` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.80 | ⚪ **CASH** | **-10.2 bps** (±6.8) | `-18.7 bps` | `+0.019 / -0.061` | `0.61%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 04:32:18 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,879.99 | ⚪ **CASH** | **-11.3 bps** (±10.8) | `-29.6 bps` | `+0.072 / +0.008` | `0.33%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,447.35 | ⚪ **CASH** | **+5.9 bps** (±10.3) | `-1.9 bps` | `+0.083 / +0.042` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.03 | ⚪ **CASH** | **-10.2 bps** (±6.8) | `-18.7 bps` | `+0.019 / -0.061` | `0.61%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 04:17:03 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,801.38 | ⚪ **CASH** | **-11.3 bps** (±10.8) | `-29.6 bps` | `+0.072 / +0.008` | `0.33%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,444.53 | ⚪ **CASH** | **+5.9 bps** (±10.3) | `-1.9 bps` | `+0.083 / +0.042` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.82 | ⚪ **CASH** | **-10.2 bps** (±6.8) | `-18.7 bps` | `+0.019 / -0.061` | `0.61%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 04:02:07 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,780.20 | ⚪ **CASH** | **-11.3 bps** (±10.8) | `-29.6 bps` | `+0.072 / +0.008` | `0.33%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,445.82 | ⚪ **CASH** | **+5.9 bps** (±10.3) | `-1.9 bps` | `+0.083 / +0.042` | `0.55%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.86 | ⚪ **CASH** | **-10.2 bps** (±6.8) | `-18.7 bps` | `+0.019 / -0.061` | `0.61%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 03:47:04 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,784.60 | ⚪ **CASH** | **-13.9 bps** (±9.6) | `-36.6 bps` | `+0.075 / +0.032` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,447.85 | ⚪ **CASH** | **-1.0 bps** (±10.5) | `-14.9 bps` | `+0.087 / +0.041` | `0.56%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.08 | ⚪ **CASH** | **-13.0 bps** (±4.9) | `-27.4 bps` | `+0.020 / -0.016` | `0.62%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 03:32:01 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,818.00 | ⚪ **CASH** | **-13.9 bps** (±9.6) | `-36.6 bps` | `+0.075 / +0.032` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,449.00 | ⚪ **CASH** | **-1.0 bps** (±10.5) | `-14.9 bps` | `+0.087 / +0.041` | `0.56%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.10 | ⚪ **CASH** | **-13.0 bps** (±4.9) | `-27.4 bps` | `+0.020 / -0.016` | `0.62%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 03:17:12 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,745.16 | ⚪ **CASH** | **-13.9 bps** (±9.6) | `-36.6 bps` | `+0.075 / +0.032` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,446.45 | ⚪ **CASH** | **-1.0 bps** (±10.5) | `-14.9 bps` | `+0.087 / +0.041` | `0.56%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.04 | ⚪ **CASH** | **-13.0 bps** (±4.9) | `-27.4 bps` | `+0.020 / -0.016` | `0.62%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 03:02:30 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,780.02 | ⚪ **CASH** | **-13.9 bps** (±9.6) | `-36.6 bps` | `+0.075 / +0.032` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,447.29 | ⚪ **CASH** | **-1.0 bps** (±10.5) | `-14.9 bps` | `+0.087 / +0.041` | `0.56%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.18 | ⚪ **CASH** | **-13.0 bps** (±4.9) | `-27.4 bps` | `+0.020 / -0.016` | `0.62%/h` | `vol_compressed` `weak_order_flow` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 02:47:07 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,818.01 | ⚪ **CASH** | **-20.1 bps** (±5.2) | `-48.5 bps` | `+0.076 / +0.025` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,449.44 | ⚪ **CASH** | **-1.9 bps** (±11.1) | `-18.1 bps` | `+0.093 / +0.058` | `0.57%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.30 | ⚪ **CASH** | **-10.9 bps** (±6.4) | `-29.8 bps` | `+0.025 / +0.076` | `0.62%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 02:32:07 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,732.55 | ⚪ **CASH** | **-20.1 bps** (±5.2) | `-48.5 bps` | `+0.076 / +0.025` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,446.77 | ⚪ **CASH** | **-1.9 bps** (±11.1) | `-18.1 bps` | `+0.093 / +0.058` | `0.57%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.08 | ⚪ **CASH** | **-10.9 bps** (±6.4) | `-29.8 bps` | `+0.025 / +0.076` | `0.62%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 02:17:09 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,811.34 | ⚪ **CASH** | **-20.1 bps** (±5.2) | `-48.5 bps` | `+0.076 / +0.025` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,449.66 | ⚪ **CASH** | **-1.9 bps** (±11.1) | `-18.1 bps` | `+0.093 / +0.058` | `0.57%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.31 | ⚪ **CASH** | **-10.9 bps** (±6.4) | `-29.8 bps` | `+0.025 / +0.076` | `0.62%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-21 02:02:10 UTC` | Patrimônio: **$999.89 USDT** (Caixa: `$999.89`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,994.00 | ⚪ **CASH** | **-20.1 bps** (±5.2) | `-48.5 bps` | `+0.076 / +0.025` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,455.21 | ⚪ **CASH** | **-1.9 bps** (±11.1) | `-18.1 bps` | `+0.093 / +0.058` | `0.57%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.60 | 🔴 **SELL** | **-10.9 bps** (±6.4) | `-29.8 bps` | `+0.025 / +0.076` | `0.62%/h` | `vol_compressed` | Reversão de fluxo/modelo (-10.9 bps) |

---

### 🕒 Ciclo `2026-10-21 01:46:59 UTC` | Patrimônio: **$1,000.61 USDT** (Caixa: `$779.62`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,037.26 | ⚪ **CASH** | **-17.8 bps** (±4.2) | `-47.9 bps` | `+0.081 / +0.066` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,455.77 | ⚪ **CASH** | **+1.4 bps** (±8.0) | `-9.7 bps` | `+0.082 / +0.025` | `0.57%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.82 | 🟡 **HOLD** | **-8.5 bps** (±5.4) | `-27.8 bps` | `+0.026 / +0.102` | `0.63%/h` | `vol_compressed` | Posição ativa há 3.7h (PnL: +0.01% | Pico: +0.25%) |

---

### 🕒 Ciclo `2026-10-21 01:32:13 UTC` | Patrimônio: **$1,000.15 USDT** (Caixa: `$779.62`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,932.00 | ⚪ **CASH** | **-17.8 bps** (±4.2) | `-47.9 bps` | `+0.081 / +0.066` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,451.71 | ⚪ **CASH** | **+1.4 bps** (±8.0) | `-9.7 bps` | `+0.082 / +0.025` | `0.57%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.60 | 🟡 **HOLD** | **-8.5 bps** (±5.4) | `-27.8 bps` | `+0.026 / +0.102` | `0.63%/h` | `vol_compressed` | Posição ativa há 3.5h (PnL: -0.20% | Pico: +0.25%) |

---

### 🕒 Ciclo `2026-10-21 01:17:02 UTC` | Patrimônio: **$999.72 USDT** (Caixa: `$779.62`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,817.66 | ⚪ **CASH** | **-17.8 bps** (±4.2) | `-47.9 bps` | `+0.081 / +0.066` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,445.63 | ⚪ **CASH** | **+1.4 bps** (±8.0) | `-9.7 bps` | `+0.082 / +0.025` | `0.57%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.39 | 🟡 **HOLD** | **-8.5 bps** (±5.4) | `-27.8 bps` | `+0.026 / +0.102` | `0.63%/h` | `vol_compressed` | Posição ativa há 3.2h (PnL: -0.39% | Pico: +0.25%) |

---

### 🕒 Ciclo `2026-10-21 01:01:51 UTC` | Patrimônio: **$999.59 USDT** (Caixa: `$779.62`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,888.70 | ⚪ **CASH** | **-17.8 bps** (±4.2) | `-47.9 bps` | `+0.081 / +0.066` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,446.56 | ⚪ **CASH** | **+1.4 bps** (±8.0) | `-9.7 bps` | `+0.082 / +0.025` | `0.57%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.33 | 🟡 **HOLD** | **-8.5 bps** (±5.4) | `-27.8 bps` | `+0.026 / +0.102` | `0.63%/h` | `vol_compressed` | Posição ativa há 3.0h (PnL: -0.45% | Pico: +0.25%) |

---

### 🕒 Ciclo `2026-10-21 00:47:10 UTC` | Patrimônio: **$1,000.61 USDT** (Caixa: `$779.62`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,146.00 | ⚪ **CASH** | **-8.7 bps** (±10.2) | `-26.9 bps` | `+0.070 / +0.038` | `0.35%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,455.17 | ⚪ **CASH** | **+5.1 bps** (±7.9) | `-2.0 bps` | `+0.080 / +0.022` | `0.58%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.82 | 🟡 **HOLD** | **-1.1 bps** (±4.1) | `-10.4 bps` | `+0.021 / +0.057` | `0.64%/h` | `vol_compressed` | Posição ativa há 2.7h (PnL: +0.01% | Pico: +0.25%) |

---

### 🕒 Ciclo `2026-10-21 00:32:01 UTC` | Patrimônio: **$1,000.71 USDT** (Caixa: `$779.62`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,213.13 | ⚪ **CASH** | **-8.7 bps** (±10.2) | `-26.9 bps` | `+0.070 / +0.038` | `0.35%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,456.34 | ⚪ **CASH** | **+5.1 bps** (±7.9) | `-2.0 bps` | `+0.080 / +0.022` | `0.58%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.87 | 🟡 **HOLD** | **-1.1 bps** (±4.1) | `-10.4 bps` | `+0.021 / +0.057` | `0.64%/h` | `vol_compressed` | Posição ativa há 2.5h (PnL: +0.06% | Pico: +0.25%) |

---

### 🕒 Ciclo `2026-10-21 00:17:02 UTC` | Patrimônio: **$1,000.46 USDT** (Caixa: `$779.62`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,133.07 | ⚪ **CASH** | **-8.7 bps** (±10.2) | `-26.9 bps` | `+0.070 / +0.038` | `0.35%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,452.92 | ⚪ **CASH** | **+5.1 bps** (±7.9) | `-2.0 bps` | `+0.080 / +0.022` | `0.58%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.75 | 🟡 **HOLD** | **-1.1 bps** (±4.1) | `-10.4 bps` | `+0.021 / +0.057` | `0.64%/h` | `vol_compressed` | Posição ativa há 2.2h (PnL: -0.06% | Pico: +0.25%) |

---

### 🕒 Ciclo `2026-10-21 00:02:09 UTC` | Patrimônio: **$999.57 USDT** (Caixa: `$779.62`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,908.17 | ⚪ **CASH** | **-8.7 bps** (±10.2) | `-26.9 bps` | `+0.070 / +0.038` | `0.35%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,445.54 | ⚪ **CASH** | **+5.1 bps** (±7.9) | `-2.0 bps` | `+0.080 / +0.022` | `0.58%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.32 | 🟡 **HOLD** | **-1.1 bps** (±4.1) | `-10.4 bps` | `+0.021 / +0.057` | `0.64%/h` | `vol_compressed` | Posição ativa há 2.0h (PnL: -0.46% | Pico: +0.25%) |

---

### 🕒 Ciclo `2026-10-20 23:47:11 UTC` | Patrimônio: **$1,000.13 USDT** (Caixa: `$779.62`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,066.01 | ⚪ **CASH** | **-12.3 bps** (±9.1) | `-34.8 bps` | `+0.073 / +0.053` | `0.35%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,450.41 | ⚪ **CASH** | **-3.2 bps** (±6.2) | `-17.0 bps` | `+0.080 / +0.016` | `0.59%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.59 | 🟡 **HOLD** | **-1.5 bps** (±4.2) | `-15.4 bps` | `+0.025 / +0.112` | `0.64%/h` | `vol_compressed` | Posição ativa há 1.7h (PnL: -0.21% | Pico: +0.25%) |

---

### 🕒 Ciclo `2026-10-20 23:32:08 UTC` | Patrimônio: **$999.80 USDT** (Caixa: `$779.62`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,924.01 | ⚪ **CASH** | **-12.3 bps** (±9.1) | `-34.8 bps` | `+0.073 / +0.053` | `0.35%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,447.51 | ⚪ **CASH** | **-3.2 bps** (±6.2) | `-17.0 bps` | `+0.080 / +0.016` | `0.59%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $106.43 | 🟡 **HOLD** | **-1.5 bps** (±4.2) | `-15.4 bps` | `+0.025 / +0.112` | `0.64%/h` | `vol_compressed` | Posição ativa há 1.5h (PnL: -0.36% | Pico: +0.25%) |

---

### 🕒 Ciclo `2026-10-20 23:17:02 UTC` | Patrimônio: **$999.88 USDT** (Caixa: `$779.62`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,938.75 | ⚪ **CASH** | **-12.3 bps** (±9.1) | `-34.8 bps` | `+0.073 / +0.053` | `0.35%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,448.60 | 🔴 **SELL** | **-3.2 bps** (±6.2) | `-17.0 bps` | `+0.080 / +0.016` | `0.59%/h` | `vol_compressed` | Trailing Stop acionado (pico +1.10%, realizou +0.50%) |
| **SOLUSDT** | $106.47 | 🟡 **HOLD** | **-1.5 bps** (±4.2) | `-15.4 bps` | `+0.025 / +0.112` | `0.64%/h` | `vol_compressed` | Posição ativa há 1.2h (PnL: -0.32% | Pico: +0.25%) |

---

### 🕒 Ciclo `2026-10-20 23:02:12 UTC` | Patrimônio: **$1,001.50 USDT** (Caixa: `$448.37`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,056.01 | ⚪ **CASH** | **-12.3 bps** (±9.1) | `-34.8 bps` | `+0.073 / +0.053` | `0.35%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,454.26 | 🟡 **HOLD** | **-3.2 bps** (±6.2) | `-17.0 bps` | `+0.080 / +0.016` | `0.59%/h` | `vol_compressed` | Posição ativa há 4.1h (PnL: +0.73% | Pico: +1.10%) |
| **SOLUSDT** | $106.69 | 🟡 **HOLD** | **-1.5 bps** (±4.2) | `-15.4 bps` | `+0.025 / +0.112` | `0.64%/h` | `vol_compressed` | Posição ativa há 1.0h (PnL: -0.11% | Pico: +0.25%) |

---

### 🕒 Ciclo `2026-10-20 22:46:58 UTC` | Patrimônio: **$1,002.55 USDT** (Caixa: `$448.37`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,019.79 | ⚪ **CASH** | **-13.9 bps** (±8.3) | `-36.3 bps` | `+0.071 / +0.033` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,457.73 | 🟡 **HOLD** | **-2.8 bps** (±7.0) | `-16.6 bps` | `+0.080 / +0.021` | `0.60%/h` | `vol_compressed` | Posição ativa há 3.9h (PnL: +0.87% | Pico: +1.10%) |
| **SOLUSDT** | $106.97 | 🟡 **HOLD** | **+27.0 bps** (±8.6) | `+31.2 bps` | `+0.032 / +0.196` | `0.65%/h` | Liberado ✅ | Posição ativa há 0.7h (PnL: +0.15% | Pico: +0.25%) |

---

### 🕒 Ciclo `2026-10-20 22:32:23 UTC` | Patrimônio: **$1,002.37 USDT** (Caixa: `$448.37`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,037.42 | ⚪ **CASH** | **-13.9 bps** (±8.3) | `-36.3 bps` | `+0.071 / +0.033` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,457.03 | 🟡 **HOLD** | **-2.8 bps** (±7.0) | `-16.6 bps` | `+0.080 / +0.021` | `0.60%/h` | `vol_compressed` | Posição ativa há 3.6h (PnL: +0.84% | Pico: +1.10%) |
| **SOLUSDT** | $106.93 | 🟡 **HOLD** | **+27.0 bps** (±8.6) | `+31.2 bps` | `+0.032 / +0.196` | `0.65%/h` | Liberado ✅ | Posição ativa há 0.5h (PnL: +0.11% | Pico: +0.25%) |

---

### 🕒 Ciclo `2026-10-20 22:17:08 UTC` | Patrimônio: **$1,003.53 USDT** (Caixa: `$448.37`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $83,125.48 | ⚪ **CASH** | **-13.9 bps** (±8.3) | `-36.3 bps` | `+0.071 / +0.033` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,463.25 | 🟡 **HOLD** | **-2.8 bps** (±7.0) | `-16.6 bps` | `+0.080 / +0.021` | `0.60%/h` | `vol_compressed` | Posição ativa há 3.4h (PnL: +1.10% | Pico: +1.10%) |
| **SOLUSDT** | $107.08 | 🟡 **HOLD** | **+27.0 bps** (±8.6) | `+31.2 bps` | `+0.032 / +0.196` | `0.65%/h` | Liberado ✅ | Posição ativa há 0.2h (PnL: +0.25% | Pico: +0.25%) |

---

### 🕒 Ciclo `2026-10-20 22:02:23 UTC` | Patrimônio: **$1,002.35 USDT** (Caixa: `$448.37`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,990.26 | ⚪ **CASH** | **-13.9 bps** (±8.3) | `-36.3 bps` | `+0.071 / +0.033` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,458.70 | 🟡 **HOLD** | **-2.8 bps** (±7.0) | `-16.6 bps` | `+0.080 / +0.021` | `0.60%/h` | `vol_compressed` | Posição ativa há 3.1h (PnL: +0.91% | Pico: +0.91%) |
| **SOLUSDT** | $106.81 | 🟢 **BUY** | **+27.0 bps** (±8.6) | `+31.2 bps` | `+0.032 / +0.196` | `0.65%/h` | Liberado ✅ | Entrada Swing 12h aprovada (Alpha +27.0 bps > 24.0 bps | CVD 24h +0.032) |

---

### 🕒 Ciclo `2026-10-20 21:47:07 UTC` | Patrimônio: **$1,001.55 USDT** (Caixa: `$669.60`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,862.37 | ⚪ **CASH** | **-11.4 bps** (±7.1) | `-28.2 bps` | `+0.070 / -0.025` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,450.82 | 🟡 **HOLD** | **+14.8 bps** (±2.1) | `+14.6 bps` | `+0.087 / +0.011` | `0.61%/h` | `weak_order_flow` | Posição ativa há 2.9h (PnL: +0.59% | Pico: +0.78%) |
| **SOLUSDT** | $106.61 | ⚪ **CASH** | **+2.0 bps** (±4.8) | `-5.8 bps` | `+0.026 / +0.066` | `0.67%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-20 21:32:07 UTC` | Patrimônio: **$1,001.71 USDT** (Caixa: `$669.60`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,875.99 | ⚪ **CASH** | **-11.4 bps** (±7.1) | `-28.2 bps` | `+0.070 / -0.025` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,451.98 | 🟡 **HOLD** | **+14.8 bps** (±2.1) | `+14.6 bps` | `+0.087 / +0.011` | `0.61%/h` | `weak_order_flow` | Posição ativa há 2.6h (PnL: +0.64% | Pico: +0.78%) |
| **SOLUSDT** | $106.61 | ⚪ **CASH** | **+2.0 bps** (±4.8) | `-5.8 bps` | `+0.026 / +0.066` | `0.67%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-20 21:17:07 UTC` | Patrimônio: **$1,002.18 USDT** (Caixa: `$669.60`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,983.21 | ⚪ **CASH** | **-11.4 bps** (±7.1) | `-28.2 bps` | `+0.070 / -0.025` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,455.47 | 🟡 **HOLD** | **+14.8 bps** (±2.1) | `+14.6 bps` | `+0.087 / +0.011` | `0.61%/h` | `weak_order_flow` | Posição ativa há 2.4h (PnL: +0.78% | Pico: +0.78%) |
| **SOLUSDT** | $106.92 | ⚪ **CASH** | **+2.0 bps** (±4.8) | `-5.8 bps` | `+0.026 / +0.066` | `0.67%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-20 21:02:10 UTC` | Patrimônio: **$1,001.41 USDT** (Caixa: `$669.60`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,857.59 | ⚪ **CASH** | **-11.4 bps** (±7.1) | `-28.2 bps` | `+0.070 / -0.025` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,449.75 | 🟡 **HOLD** | **+14.8 bps** (±2.1) | `+14.6 bps` | `+0.087 / +0.011` | `0.61%/h` | `weak_order_flow` | Posição ativa há 2.1h (PnL: +0.55% | Pico: +0.55%) |
| **SOLUSDT** | $106.78 | ⚪ **CASH** | **+2.0 bps** (±4.8) | `-5.8 bps` | `+0.026 / +0.066` | `0.67%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-20 20:46:59 UTC` | Patrimônio: **$1,000.80 USDT** (Caixa: `$669.60`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,798.01 | ⚪ **CASH** | **-10.4 bps** (±6.5) | `-28.8 bps` | `+0.074 / +0.004` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,445.30 | 🟡 **HOLD** | **+32.4 bps** (±8.5) | `+41.3 bps` | `+0.088 / +0.106` | `0.62%/h` | Liberado ✅ | Posição ativa há 1.9h (PnL: +0.36% | Pico: +0.36%) |
| **SOLUSDT** | $106.59 | ⚪ **CASH** | **+0.0 bps** (±4.6) | `-5.4 bps` | `+0.015 / +0.018` | `0.68%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
