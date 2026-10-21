# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-21 00:47:10 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-10-20 20:32:23 UTC` | Patrimônio: **$1,000.15 USDT** (Caixa: `$669.60`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,686.01 | ⚪ **CASH** | **-10.4 bps** (±6.5) | `-28.8 bps` | `+0.074 / +0.004` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,440.51 | 🟡 **HOLD** | **+32.4 bps** (±8.5) | `+41.3 bps` | `+0.088 / +0.106` | `0.62%/h` | Liberado ✅ | Posição ativa há 1.6h (PnL: +0.17% | Pico: +0.17%) |
| **SOLUSDT** | $106.34 | ⚪ **CASH** | **+0.0 bps** (±4.6) | `-5.4 bps` | `+0.015 / +0.018` | `0.68%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-20 20:17:08 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$669.60`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,628.01 | ⚪ **CASH** | **-10.4 bps** (±6.5) | `-28.8 bps` | `+0.074 / +0.004` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,439.35 | 🟡 **HOLD** | **+32.4 bps** (±8.5) | `+41.3 bps` | `+0.088 / +0.106` | `0.62%/h` | Liberado ✅ | Posição ativa há 1.4h (PnL: +0.12% | Pico: +0.15%) |
| **SOLUSDT** | $106.11 | ⚪ **CASH** | **+0.0 bps** (±4.6) | `-5.4 bps` | `+0.015 / +0.018` | `0.68%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-20 20:02:11 UTC` | Patrimônio: **$999.45 USDT** (Caixa: `$669.60`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,532.01 | ⚪ **CASH** | **-10.4 bps** (±6.5) | `-28.8 bps` | `+0.074 / +0.004` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,435.33 | 🟡 **HOLD** | **+32.4 bps** (±8.5) | `+41.3 bps` | `+0.088 / +0.106` | `0.62%/h` | Liberado ✅ | Posição ativa há 1.1h (PnL: -0.05% | Pico: +0.15%) |
| **SOLUSDT** | $106.02 | ⚪ **CASH** | **+0.0 bps** (±4.6) | `-5.4 bps` | `+0.015 / +0.018` | `0.68%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-20 19:47:15 UTC` | Patrimônio: **$1,000.10 USDT** (Caixa: `$669.60`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,622.01 | ⚪ **CASH** | **-20.2 bps** (±4.2) | `-50.2 bps` | `+0.075 / +0.047` | `0.37%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,440.14 | 🟡 **HOLD** | **+37.0 bps** (±8.7) | `+50.1 bps` | `+0.086 / +0.101` | `0.62%/h` | Liberado ✅ | Posição ativa há 0.9h (PnL: +0.15% | Pico: +0.15%) |
| **SOLUSDT** | $106.08 | ⚪ **CASH** | **+1.8 bps** (±4.3) | `-2.3 bps` | `+0.009 / +0.026` | `0.69%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-20 19:32:20 UTC` | Patrimônio: **$999.00 USDT** (Caixa: `$669.60`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,508.01 | ⚪ **CASH** | **-20.2 bps** (±4.2) | `-50.2 bps` | `+0.075 / +0.047` | `0.37%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,431.97 | 🟡 **HOLD** | **+37.0 bps** (±8.7) | `+50.1 bps` | `+0.086 / +0.101` | `0.62%/h` | Liberado ✅ | Posição ativa há 0.6h (PnL: -0.18% | Pico: +0.09%) |
| **SOLUSDT** | $105.60 | ⚪ **CASH** | **+1.8 bps** (±4.3) | `-2.3 bps` | `+0.009 / +0.026` | `0.69%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-20 19:17:05 UTC` | Patrimônio: **$999.52 USDT** (Caixa: `$669.60`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,550.01 | ⚪ **CASH** | **-20.2 bps** (±4.2) | `-50.2 bps` | `+0.075 / +0.047` | `0.37%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,435.84 | 🟡 **HOLD** | **+37.0 bps** (±8.7) | `+50.1 bps` | `+0.086 / +0.101` | `0.62%/h` | Liberado ✅ | Posição ativa há 0.4h (PnL: -0.03% | Pico: +0.09%) |
| **SOLUSDT** | $105.91 | ⚪ **CASH** | **+1.8 bps** (±4.3) | `-2.3 bps` | `+0.009 / +0.026` | `0.69%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-20 19:02:12 UTC` | Patrimônio: **$999.71 USDT** (Caixa: `$669.60`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,532.20 | ⚪ **CASH** | **-20.2 bps** (±4.2) | `-50.2 bps` | `+0.075 / +0.047` | `0.37%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,437.26 | 🟡 **HOLD** | **+37.0 bps** (±8.7) | `+50.1 bps` | `+0.086 / +0.101` | `0.62%/h` | Liberado ✅ | Posição ativa há 0.1h (PnL: +0.03% | Pico: +0.09%) |
| **SOLUSDT** | $105.85 | ⚪ **CASH** | **+1.8 bps** (±4.3) | `-2.3 bps` | `+0.009 / +0.026` | `0.69%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-20 18:56:35 UTC` | Patrimônio: **$999.90 USDT** (Caixa: `$669.60`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,562.02 | ⚪ **CASH** | **-20.8 bps** (±3.7) | `-53.8 bps` | `+0.084 / +0.065` | `0.37%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,438.62 | 🟡 **HOLD** | **+27.7 bps** (±8.4) | `+32.4 bps` | `+0.089 / +0.099` | `0.63%/h` | Liberado ✅ | Posição ativa há 0.1h (PnL: +0.09% | Pico: +0.09%) |
| **SOLUSDT** | $106.04 | ⚪ **CASH** | **-0.3 bps** (±5.0) | `-8.5 bps` | `+0.018 / +0.044` | `0.68%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-20 18:47:03 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,531.95 | ⚪ **CASH** | **+0.2 bps** (±0.1) | `[+0.3, +0.0, +0.3, +0.1, +0.4]` | `+0.065` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,438.19 | ⚪ **CASH** | **+0.4 bps** (±0.4) | `[+1.1, +0.1, +0.6, +0.2, +1.0]` | `+0.099` | `0.63%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.91 | ⚪ **CASH** | **-0.8 bps** (±0.4) | `[-0.7, -0.5, +0.1, -1.2, -0.6]` | `+0.044` | `0.68%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-20 18:32:31 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,526.25 | ⚪ **CASH** | **+0.2 bps** (±0.1) | `[+0.3, +0.0, +0.3, +0.1, +0.4]` | `+0.065` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,439.19 | ⚪ **CASH** | **+0.4 bps** (±0.4) | `[+1.1, +0.1, +0.6, +0.2, +1.0]` | `+0.099` | `0.63%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.07 | ⚪ **CASH** | **-0.8 bps** (±0.4) | `[-0.7, -0.5, +0.1, -1.2, -0.6]` | `+0.044` | `0.68%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-20 18:17:09 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,670.00 | ⚪ **CASH** | **+0.2 bps** (±0.1) | `[+0.3, +0.0, +0.3, +0.1, +0.4]` | `+0.065` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,445.44 | ⚪ **CASH** | **+0.4 bps** (±0.4) | `[+1.1, +0.1, +0.6, +0.2, +1.0]` | `+0.099` | `0.63%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.42 | ⚪ **CASH** | **-0.8 bps** (±0.4) | `[-0.7, -0.5, +0.1, -1.2, -0.6]` | `+0.044` | `0.68%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-20 18:02:09 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,762.54 | ⚪ **CASH** | **+0.2 bps** (±0.1) | `[+0.3, +0.0, +0.3, +0.1, +0.4]` | `+0.065` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,448.37 | ⚪ **CASH** | **+0.4 bps** (±0.4) | `[+1.1, +0.1, +0.6, +0.2, +1.0]` | `+0.099` | `0.63%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.59 | ⚪ **CASH** | **-0.8 bps** (±0.4) | `[-0.7, -0.5, +0.1, -1.2, -0.6]` | `+0.044` | `0.68%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-20 17:47:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,870.68 | ⚪ **CASH** | **+0.2 bps** (±0.1) | `[+0.2, +0.0, +0.3, +0.1, +0.4]` | `+0.056` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,453.31 | ⚪ **CASH** | **+0.2 bps** (±0.7) | `[+0.1, -0.4, +0.6, +0.5, +1.7]` | `+0.104` | `0.63%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.77 | ⚪ **CASH** | **-0.8 bps** (±0.4) | `[-0.7, -0.5, +0.1, -1.2, -0.6]` | `+0.030` | `0.69%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-20 17:32:24 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,733.41 | ⚪ **CASH** | **+0.2 bps** (±0.1) | `[+0.2, +0.0, +0.3, +0.1, +0.4]` | `+0.056` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,447.29 | ⚪ **CASH** | **+0.2 bps** (±0.7) | `[+0.1, -0.4, +0.6, +0.5, +1.7]` | `+0.104` | `0.63%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.43 | ⚪ **CASH** | **-0.8 bps** (±0.4) | `[-0.7, -0.5, +0.1, -1.2, -0.6]` | `+0.030` | `0.69%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-20 17:17:18 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,781.26 | ⚪ **CASH** | **+0.2 bps** (±0.1) | `[+0.2, +0.0, +0.3, +0.1, +0.4]` | `+0.056` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,452.20 | ⚪ **CASH** | **+0.2 bps** (±0.7) | `[+0.1, -0.4, +0.6, +0.5, +1.7]` | `+0.104` | `0.63%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.59 | ⚪ **CASH** | **-0.8 bps** (±0.4) | `[-0.7, -0.5, +0.1, -1.2, -0.6]` | `+0.030` | `0.69%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-20 17:02:18 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,700.70 | ⚪ **CASH** | **+0.2 bps** (±0.1) | `[+0.2, +0.0, +0.3, +0.1, +0.4]` | `+0.056` | `0.37%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,447.57 | ⚪ **CASH** | **+0.2 bps** (±0.7) | `[+0.1, -0.4, +0.6, +0.5, +1.7]` | `+0.104` | `0.63%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.35 | ⚪ **CASH** | **-0.8 bps** (±0.4) | `[-0.7, -0.5, +0.1, -1.2, -0.6]` | `+0.030` | `0.69%/h` | `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-20 16:47:05 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,594.95 | ⚪ **CASH** | **+4.2 bps** (±0.9) | `[+4.0, +5.0, +3.3, +5.7, +5.0]` | `+0.063` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,444.38 | ⚪ **CASH** | **+3.1 bps** (±0.7) | `[+3.0, +2.5, +3.5, +3.5, +4.8]` | `+0.104` | `0.64%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.26 | ⚪ **CASH** | **+2.8 bps** (±0.4) | `[+3.4, +2.8, +3.5, +3.0, +2.3]` | `-0.010` | `0.69%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-20 16:32:01 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,620.00 | ⚪ **CASH** | **+4.2 bps** (±0.9) | `[+4.0, +5.0, +3.3, +5.7, +5.0]` | `+0.063` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,443.68 | ⚪ **CASH** | **+3.1 bps** (±0.7) | `[+3.0, +2.5, +3.5, +3.5, +4.8]` | `+0.104` | `0.64%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $106.04 | ⚪ **CASH** | **+2.8 bps** (±0.4) | `[+3.4, +2.8, +3.5, +3.0, +2.3]` | `-0.010` | `0.69%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |

---

### 🕒 Ciclo `2026-10-20 16:17:04 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,522.13 | ⚪ **CASH** | **+4.2 bps** (±0.9) | `[+4.0, +5.0, +3.3, +5.7, +5.0]` | `+0.063` | `0.38%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,438.40 | ⚪ **CASH** | **+3.1 bps** (±0.7) | `[+3.0, +2.5, +3.5, +3.5, +4.8]` | `+0.104` | `0.64%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $105.78 | ⚪ **CASH** | **+2.8 bps** (±0.4) | `[+3.4, +2.8, +3.5, +3.0, +2.3]` | `-0.010` | `0.69%/h` | `turbulent_chop` `sol_sideways` | Aguardando sinal com assimetria |
