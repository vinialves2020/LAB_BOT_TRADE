# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-29 19:47:35 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-29 19:47:35 UTC` | Patrimônio: **$988.65 USDT** (Caixa: `$443.80`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,886.27 | 🟡 **HOLD** | **+29.4 bps** (±8.2) | `+33.8 bps` | `+0.103 / +0.092` | `0.40%/h` | Liberado ✅ | Posição ativa há 4.7h (PnL: -0.46% | Pico: +0.74%) |
| **ETHUSDT** | $2,335.54 | 🟢 **BUY** | **+33.0 bps** (±4.8) | `+36.2 bps` | `+0.065 / +0.201` | `0.46%/h` | Liberado ✅ | Entrada Swing 12h aprovada (Alpha +33.0 bps > 24.0 bps | CVD 24h +0.065) |
| **SOLUSDT** | $100.15 | ⚪ **CASH** | **+26.1 bps** (±16.7) | `+25.3 bps` | `+0.082 / +0.186` | `0.54%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-10-29 19:32:18 UTC` | Patrimônio: **$988.97 USDT** (Caixa: `$662.78`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,899.59 | 🟡 **HOLD** | **+29.4 bps** (±8.2) | `+33.8 bps` | `+0.103 / +0.092` | `0.40%/h` | Liberado ✅ | Posição ativa há 4.5h (PnL: -0.45% | Pico: +0.74%) |
| **ETHUSDT** | $2,335.34 | ⚪ **CASH** | **+33.0 bps** (±4.8) | `+36.2 bps` | `+0.065 / +0.201` | `0.46%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $100.31 | ⚪ **CASH** | **+26.1 bps** (±16.7) | `+25.3 bps` | `+0.082 / +0.186` | `0.54%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-10-29 19:17:16 UTC` | Patrimônio: **$988.47 USDT** (Caixa: `$662.78`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,778.00 | 🟡 **HOLD** | **+29.4 bps** (±8.2) | `+33.8 bps` | `+0.103 / +0.092` | `0.40%/h` | Liberado ✅ | Posição ativa há 4.2h (PnL: -0.60% | Pico: +0.74%) |
| **ETHUSDT** | $2,327.12 | ⚪ **CASH** | **+33.0 bps** (±4.8) | `+36.2 bps` | `+0.065 / +0.201` | `0.46%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $100.23 | 🔴 **SELL** | **+26.1 bps** (±16.7) | `+25.3 bps` | `+0.082 / +0.186` | `0.54%/h` | Liberado ✅ | Stop Loss técnico acionado (-1.55%) |

---

### 🕒 Ciclo `2026-10-29 19:02:44 UTC` | Patrimônio: **$989.18 USDT** (Caixa: `$518.31`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,830.01 | 🟡 **HOLD** | **+29.4 bps** (±8.2) | `+33.8 bps` | `+0.103 / +0.092` | `0.40%/h` | Liberado ✅ | Posição ativa há 4.0h (PnL: -0.53% | Pico: +0.74%) |
| **ETHUSDT** | $2,328.66 | ⚪ **CASH** | **+33.0 bps** (±4.8) | `+36.2 bps` | `+0.065 / +0.201` | `0.46%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $100.45 | 🟡 **HOLD** | **+26.1 bps** (±16.7) | `+25.3 bps` | `+0.082 / +0.186` | `0.54%/h` | Liberado ✅ | Posição ativa há 4.0h (PnL: -1.34% | Pico: +0.82%) |

---

### 🕒 Ciclo `2026-10-29 18:47:34 UTC` | Patrimônio: **$988.49 USDT** (Caixa: `$518.31`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,671.28 | 🟡 **HOLD** | **+21.2 bps** (±12.5) | `+17.7 bps` | `+0.118 / +0.089` | `0.41%/h` | Liberado ✅ | Posição ativa há 3.7h (PnL: -0.73% | Pico: +0.74%) |
| **ETHUSDT** | $2,327.52 | ⚪ **CASH** | **+33.2 bps** (±10.6) | `+41.1 bps` | `+0.053 / +0.154` | `0.47%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $100.42 | 🟡 **HOLD** | **+31.7 bps** (±7.7) | `+29.6 bps` | `+0.114 / +0.190` | `0.55%/h` | Liberado ✅ | Posição ativa há 3.7h (PnL: -1.37% | Pico: +0.82%) |

---

### 🕒 Ciclo `2026-10-29 18:32:30 UTC` | Patrimônio: **$988.29 USDT** (Caixa: `$518.31`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,624.01 | 🟡 **HOLD** | **+21.2 bps** (±12.5) | `+17.7 bps` | `+0.118 / +0.089` | `0.41%/h` | Liberado ✅ | Posição ativa há 3.5h (PnL: -0.79% | Pico: +0.74%) |
| **ETHUSDT** | $2,326.61 | ⚪ **CASH** | **+33.2 bps** (±10.6) | `+41.1 bps` | `+0.053 / +0.154` | `0.47%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $100.41 | 🟡 **HOLD** | **+31.7 bps** (±7.7) | `+29.6 bps` | `+0.114 / +0.190` | `0.55%/h` | Liberado ✅ | Posição ativa há 3.5h (PnL: -1.38% | Pico: +0.82%) |

---

### 🕒 Ciclo `2026-10-29 18:17:14 UTC` | Patrimônio: **$990.15 USDT** (Caixa: `$518.31`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,842.01 | 🟡 **HOLD** | **+21.2 bps** (±12.5) | `+17.7 bps` | `+0.118 / +0.089` | `0.41%/h` | Liberado ✅ | Posição ativa há 3.2h (PnL: -0.52% | Pico: +0.74%) |
| **ETHUSDT** | $2,340.43 | ⚪ **CASH** | **+33.2 bps** (±10.6) | `+41.1 bps` | `+0.053 / +0.154` | `0.47%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $101.09 | 🟡 **HOLD** | **+31.7 bps** (±7.7) | `+29.6 bps` | `+0.114 / +0.190` | `0.55%/h` | Liberado ✅ | Posição ativa há 3.2h (PnL: -0.71% | Pico: +0.82%) |

---

### 🕒 Ciclo `2026-10-29 18:02:30 UTC` | Patrimônio: **$989.94 USDT** (Caixa: `$518.31`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,813.10 | 🟡 **HOLD** | **+21.2 bps** (±12.5) | `+17.7 bps` | `+0.118 / +0.089` | `0.41%/h` | Liberado ✅ | Posição ativa há 3.0h (PnL: -0.55% | Pico: +0.74%) |
| **ETHUSDT** | $2,338.32 | ⚪ **CASH** | **+33.2 bps** (±10.6) | `+41.1 bps` | `+0.053 / +0.154` | `0.47%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $101.03 | 🟡 **HOLD** | **+31.7 bps** (±7.7) | `+29.6 bps` | `+0.114 / +0.190` | `0.55%/h` | Liberado ✅ | Posição ativa há 3.0h (PnL: -0.77% | Pico: +0.82%) |

---

### 🕒 Ciclo `2026-10-29 17:47:33 UTC` | Patrimônio: **$989.68 USDT** (Caixa: `$518.31`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,793.48 | 🟡 **HOLD** | **+28.9 bps** (±11.5) | `+27.7 bps` | `+0.134 / +0.110` | `0.40%/h` | Liberado ✅ | Posição ativa há 2.7h (PnL: -0.58% | Pico: +0.74%) |
| **ETHUSDT** | $2,334.83 | ⚪ **CASH** | **+40.1 bps** (±13.3) | `+51.3 bps` | `+0.056 / +0.183` | `0.46%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $100.90 | 🟡 **HOLD** | **+53.1 bps** (±23.6) | `+67.4 bps` | `+0.131 / +0.213` | `0.53%/h` | Liberado ✅ | Posição ativa há 2.7h (PnL: -0.89% | Pico: +0.82%) |

---

### 🕒 Ciclo `2026-10-29 17:32:34 UTC` | Patrimônio: **$992.38 USDT** (Caixa: `$518.31`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,160.61 | 🟡 **HOLD** | **+28.9 bps** (±11.5) | `+27.7 bps` | `+0.134 / +0.110` | `0.40%/h` | Liberado ✅ | Posição ativa há 2.5h (PnL: -0.13% | Pico: +0.74%) |
| **ETHUSDT** | $2,352.78 | ⚪ **CASH** | **+40.1 bps** (±13.3) | `+51.3 bps` | `+0.056 / +0.183` | `0.46%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $101.75 | 🟡 **HOLD** | **+53.1 bps** (±23.6) | `+67.4 bps` | `+0.131 / +0.213` | `0.53%/h` | Liberado ✅ | Posição ativa há 2.5h (PnL: -0.06% | Pico: +0.82%) |

---

### 🕒 Ciclo `2026-10-29 17:17:26 UTC` | Patrimônio: **$991.66 USDT** (Caixa: `$518.31`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,020.85 | 🟡 **HOLD** | **+28.9 bps** (±11.5) | `+27.7 bps` | `+0.134 / +0.110` | `0.40%/h` | Liberado ✅ | Posição ativa há 2.2h (PnL: -0.30% | Pico: +0.74%) |
| **ETHUSDT** | $2,350.08 | ⚪ **CASH** | **+40.1 bps** (±13.3) | `+51.3 bps` | `+0.056 / +0.183` | `0.46%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |
| **SOLUSDT** | $101.64 | 🟡 **HOLD** | **+53.1 bps** (±23.6) | `+67.4 bps` | `+0.131 / +0.213` | `0.53%/h` | Liberado ✅ | Posição ativa há 2.2h (PnL: -0.17% | Pico: +0.82%) |

---

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
