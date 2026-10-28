# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-28 02:47:05 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-10-28 02:17:16 UTC` | Patrimônio: **$999.60 USDT** (Caixa: `$778.46`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,122.00 | 🟡 **HOLD** | **+33.3 bps** (±13.7) | `+31.1 bps` | `+0.170 / +0.105` | `0.27%/h` | `vol_compressed` | Posição ativa há 10.3h (PnL: +0.72% | Pico: +0.81%) |
| **ETHUSDT** | $2,362.52 | ⚪ **CASH** | **+9.9 bps** (±6.3) | `-4.4 bps` | `+0.103 / +0.075` | `0.37%/h` | `vol_compressed` `cooldown_active` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.94 | ⚪ **CASH** | **+7.5 bps** (±21.6) | `-3.3 bps` | `+0.103 / +0.038` | `0.40%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 02:02:37 UTC` | Patrimônio: **$999.01 USDT** (Caixa: `$778.46`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,906.02 | 🟡 **HOLD** | **+33.3 bps** (±13.7) | `+31.1 bps` | `+0.170 / +0.105` | `0.27%/h` | `vol_compressed` | Posição ativa há 10.0h (PnL: +0.45% | Pico: +0.81%) |
| **ETHUSDT** | $2,355.61 | 🔴 **SELL** | **+9.9 bps** (±6.3) | `-4.4 bps` | `+0.103 / +0.075` | `0.37%/h` | `vol_compressed` | Alvo temporal de 12h concluído (+1.66%) |
| **SOLUSDT** | $101.67 | ⚪ **CASH** | **+7.5 bps** (±21.6) | `-3.3 bps` | `+0.103 / +0.038` | `0.40%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 01:47:12 UTC` | Patrimônio: **$999.44 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,923.29 | 🟡 **HOLD** | **+32.5 bps** (±7.9) | `+30.5 bps` | `+0.167 / +0.083` | `0.27%/h` | `vol_compressed` | Posição ativa há 9.8h (PnL: +0.47% | Pico: +0.81%) |
| **ETHUSDT** | $2,355.53 | 🟡 **HOLD** | **+10.3 bps** (±5.0) | `-3.7 bps` | `+0.102 / +0.078` | `0.37%/h` | `vol_compressed` | Posição ativa há 11.7h (PnL: +1.65% | Pico: +1.65%) |
| **SOLUSDT** | $101.64 | ⚪ **CASH** | **+5.0 bps** (±15.0) | `-5.1 bps` | `+0.094 / -0.008` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 01:32:10 UTC` | Patrimônio: **$998.00 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,774.00 | 🟡 **HOLD** | **+32.5 bps** (±7.9) | `+30.5 bps` | `+0.167 / +0.083` | `0.27%/h` | `vol_compressed` | Posição ativa há 9.5h (PnL: +0.28% | Pico: +0.81%) |
| **ETHUSDT** | $2,348.25 | 🟡 **HOLD** | **+10.3 bps** (±5.0) | `-3.7 bps` | `+0.102 / +0.078` | `0.37%/h` | `vol_compressed` | Posição ativa há 11.5h (PnL: +1.34% | Pico: +1.64%) |
| **SOLUSDT** | $101.37 | ⚪ **CASH** | **+5.0 bps** (±15.0) | `-5.1 bps` | `+0.094 / -0.008` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 01:16:55 UTC` | Patrimônio: **$997.03 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,677.89 | 🟡 **HOLD** | **+32.5 bps** (±7.9) | `+30.5 bps` | `+0.167 / +0.083` | `0.27%/h` | `vol_compressed` | Posição ativa há 9.2h (PnL: +0.17% | Pico: +0.81%) |
| **ETHUSDT** | $2,343.20 | 🟡 **HOLD** | **+10.3 bps** (±5.0) | `-3.7 bps` | `+0.102 / +0.078` | `0.37%/h` | `vol_compressed` | Posição ativa há 11.2h (PnL: +1.12% | Pico: +1.64%) |
| **SOLUSDT** | $101.16 | ⚪ **CASH** | **+5.0 bps** (±15.0) | `-5.1 bps` | `+0.094 / -0.008` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 01:02:15 UTC` | Patrimônio: **$996.82 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,672.84 | 🟡 **HOLD** | **+32.5 bps** (±7.9) | `+30.5 bps` | `+0.167 / +0.083` | `0.27%/h` | `vol_compressed` | Posição ativa há 9.0h (PnL: +0.16% | Pico: +0.81%) |
| **ETHUSDT** | $2,341.83 | 🟡 **HOLD** | **+10.3 bps** (±5.0) | `-3.7 bps` | `+0.102 / +0.078` | `0.37%/h` | `vol_compressed` | Posição ativa há 11.0h (PnL: +1.06% | Pico: +1.64%) |
| **SOLUSDT** | $101.08 | ⚪ **CASH** | **+5.0 bps** (±15.0) | `-5.1 bps` | `+0.094 / -0.008` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 00:47:15 UTC` | Patrimônio: **$997.57 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,758.00 | 🟡 **HOLD** | **+48.0 bps** (±9.4) | `+45.3 bps` | `+0.192 / +0.235` | `0.27%/h` | `vol_compressed` | Posição ativa há 8.8h (PnL: +0.26% | Pico: +0.81%) |
| **ETHUSDT** | $2,345.48 | 🟡 **HOLD** | **+36.3 bps** (±14.3) | `+38.1 bps` | `+0.110 / +0.157` | `0.37%/h` | `vol_compressed` | Posição ativa há 10.7h (PnL: +1.22% | Pico: +1.64%) |
| **SOLUSDT** | $101.26 | ⚪ **CASH** | **+8.3 bps** (±13.8) | `-2.7 bps` | `+0.098 / +0.021` | `0.40%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 00:32:03 UTC` | Patrimônio: **$997.74 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,796.00 | 🟡 **HOLD** | **+48.0 bps** (±9.4) | `+45.3 bps` | `+0.192 / +0.235` | `0.27%/h` | `vol_compressed` | Posição ativa há 8.5h (PnL: +0.31% | Pico: +0.81%) |
| **ETHUSDT** | $2,345.95 | 🟡 **HOLD** | **+36.3 bps** (±14.3) | `+38.1 bps` | `+0.110 / +0.157` | `0.37%/h` | `vol_compressed` | Posição ativa há 10.5h (PnL: +1.24% | Pico: +1.64%) |
| **SOLUSDT** | $101.26 | ⚪ **CASH** | **+8.3 bps** (±13.8) | `-2.7 bps` | `+0.098 / +0.021` | `0.40%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 00:17:09 UTC` | Patrimônio: **$997.75 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,766.66 | 🟡 **HOLD** | **+48.0 bps** (±9.4) | `+45.3 bps` | `+0.192 / +0.235` | `0.27%/h` | `vol_compressed` | Posição ativa há 8.3h (PnL: +0.28% | Pico: +0.81%) |
| **ETHUSDT** | $2,346.61 | 🟡 **HOLD** | **+36.3 bps** (±14.3) | `+38.1 bps` | `+0.110 / +0.157` | `0.37%/h` | `vol_compressed` | Posição ativa há 10.2h (PnL: +1.27% | Pico: +1.64%) |
| **SOLUSDT** | $101.20 | ⚪ **CASH** | **+8.3 bps** (±13.8) | `-2.7 bps` | `+0.098 / +0.021` | `0.40%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 00:02:18 UTC` | Patrimônio: **$998.16 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,844.53 | 🟡 **HOLD** | **+48.0 bps** (±9.4) | `+45.3 bps` | `+0.192 / +0.235` | `0.27%/h` | `vol_compressed` | Posição ativa há 8.0h (PnL: +0.37% | Pico: +0.81%) |
| **ETHUSDT** | $2,347.98 | 🟡 **HOLD** | **+36.3 bps** (±14.3) | `+38.1 bps` | `+0.110 / +0.157` | `0.37%/h` | `vol_compressed` | Posição ativa há 10.0h (PnL: +1.33% | Pico: +1.64%) |
| **SOLUSDT** | $101.22 | ⚪ **CASH** | **+8.3 bps** (±13.8) | `-2.7 bps` | `+0.098 / +0.021` | `0.40%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 23:47:10 UTC` | Patrimônio: **$999.26 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,988.83 | 🟡 **HOLD** | **+49.1 bps** (±7.1) | `+46.2 bps` | `+0.189 / +0.252` | `0.27%/h` | `vol_compressed` | Posição ativa há 7.8h (PnL: +0.55% | Pico: +0.81%) |
| **ETHUSDT** | $2,352.99 | 🟡 **HOLD** | **+22.2 bps** (±12.2) | `+17.1 bps` | `+0.111 / +0.082` | `0.38%/h` | `vol_compressed` | Posição ativa há 9.7h (PnL: +1.54% | Pico: +1.64%) |
| **SOLUSDT** | $101.43 | ⚪ **CASH** | **+10.1 bps** (±25.6) | `-0.8 bps` | `+0.101 / +0.072` | `0.41%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 23:32:15 UTC` | Patrimônio: **$998.72 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,915.17 | 🟡 **HOLD** | **+49.1 bps** (±7.1) | `+46.2 bps` | `+0.189 / +0.252` | `0.27%/h` | `vol_compressed` | Posição ativa há 7.5h (PnL: +0.46% | Pico: +0.81%) |
| **ETHUSDT** | $2,350.61 | 🟡 **HOLD** | **+22.2 bps** (±12.2) | `+17.1 bps` | `+0.111 / +0.082` | `0.38%/h` | `vol_compressed` | Posição ativa há 9.5h (PnL: +1.44% | Pico: +1.64%) |
| **SOLUSDT** | $101.30 | ⚪ **CASH** | **+10.1 bps** (±25.6) | `-0.8 bps` | `+0.101 / +0.072` | `0.41%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 23:16:54 UTC` | Patrimônio: **$998.65 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,904.93 | 🟡 **HOLD** | **+49.1 bps** (±7.1) | `+46.2 bps` | `+0.189 / +0.252` | `0.27%/h` | `vol_compressed` | Posição ativa há 7.2h (PnL: +0.45% | Pico: +0.81%) |
| **ETHUSDT** | $2,350.32 | 🟡 **HOLD** | **+22.2 bps** (±12.2) | `+17.1 bps` | `+0.111 / +0.082` | `0.38%/h` | `vol_compressed` | Posição ativa há 9.2h (PnL: +1.43% | Pico: +1.64%) |
| **SOLUSDT** | $101.29 | ⚪ **CASH** | **+10.1 bps** (±25.6) | `-0.8 bps` | `+0.101 / +0.072` | `0.41%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 23:02:09 UTC` | Patrimônio: **$998.56 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,885.80 | 🟡 **HOLD** | **+49.1 bps** (±7.1) | `+46.2 bps` | `+0.189 / +0.252` | `0.27%/h` | `vol_compressed` | Posição ativa há 7.0h (PnL: +0.42% | Pico: +0.81%) |
| **ETHUSDT** | $2,350.01 | 🟡 **HOLD** | **+22.2 bps** (±12.2) | `+17.1 bps` | `+0.111 / +0.082` | `0.38%/h` | `vol_compressed` | Posição ativa há 9.0h (PnL: +1.42% | Pico: +1.64%) |
| **SOLUSDT** | $101.31 | ⚪ **CASH** | **+10.1 bps** (±25.6) | `-0.8 bps` | `+0.101 / +0.072` | `0.41%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 22:47:01 UTC` | Patrimônio: **$998.54 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,895.51 | 🟡 **HOLD** | **+51.9 bps** (±7.2) | `+47.6 bps` | `+0.186 / +0.314` | `0.28%/h` | `vol_compressed` `stretched_top` | Posição ativa há 6.7h (PnL: +0.44% | Pico: +0.81%) |
| **ETHUSDT** | $2,349.68 | 🟡 **HOLD** | **+18.7 bps** (±9.2) | `+7.8 bps` | `+0.116 / +0.114` | `0.38%/h` | `vol_compressed` | Posição ativa há 8.7h (PnL: +1.40% | Pico: +1.64%) |
| **SOLUSDT** | $101.27 | ⚪ **CASH** | **+10.1 bps** (±22.4) | `-2.9 bps` | `+0.108 / +0.085` | `0.42%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 22:32:17 UTC` | Patrimônio: **$998.68 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,929.49 | 🟡 **HOLD** | **+51.9 bps** (±7.2) | `+47.6 bps` | `+0.186 / +0.314` | `0.28%/h` | `vol_compressed` `stretched_top` | Posição ativa há 6.5h (PnL: +0.48% | Pico: +0.81%) |
| **ETHUSDT** | $2,350.01 | 🟡 **HOLD** | **+18.7 bps** (±9.2) | `+7.8 bps` | `+0.116 / +0.114` | `0.38%/h` | `vol_compressed` | Posição ativa há 8.5h (PnL: +1.42% | Pico: +1.64%) |
| **SOLUSDT** | $101.30 | ⚪ **CASH** | **+10.1 bps** (±22.4) | `-2.9 bps` | `+0.108 / +0.085` | `0.42%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 22:17:09 UTC` | Patrimônio: **$999.43 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,997.07 | 🟡 **HOLD** | **+51.9 bps** (±7.2) | `+47.6 bps` | `+0.186 / +0.314` | `0.28%/h` | `vol_compressed` `stretched_top` | Posição ativa há 6.3h (PnL: +0.56% | Pico: +0.81%) |
| **ETHUSDT** | $2,354.05 | 🟡 **HOLD** | **+18.7 bps** (±9.2) | `+7.8 bps` | `+0.116 / +0.114` | `0.38%/h` | `vol_compressed` | Posição ativa há 8.2h (PnL: +1.59% | Pico: +1.64%) |
| **SOLUSDT** | $101.47 | ⚪ **CASH** | **+10.1 bps** (±22.4) | `-2.9 bps` | `+0.108 / +0.085` | `0.42%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 22:02:10 UTC` | Patrimônio: **$998.38 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,863.10 | 🟡 **HOLD** | **+51.9 bps** (±7.2) | `+47.6 bps` | `+0.186 / +0.314` | `0.28%/h` | `vol_compressed` `stretched_top` | Posição ativa há 6.0h (PnL: +0.40% | Pico: +0.81%) |
| **ETHUSDT** | $2,349.15 | 🟡 **HOLD** | **+18.7 bps** (±9.2) | `+7.8 bps` | `+0.116 / +0.114` | `0.38%/h` | `vol_compressed` | Posição ativa há 8.0h (PnL: +1.38% | Pico: +1.64%) |
| **SOLUSDT** | $101.20 | ⚪ **CASH** | **+10.1 bps** (±22.4) | `-2.9 bps` | `+0.108 / +0.085` | `0.42%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 21:47:08 UTC` | Patrimônio: **$999.68 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,033.12 | 🟡 **HOLD** | **+50.8 bps** (±6.4) | `+43.2 bps` | `+0.192 / +0.336` | `0.28%/h` | `vol_compressed` `stretched_top` | Posição ativa há 5.8h (PnL: +0.61% | Pico: +0.81%) |
| **ETHUSDT** | $2,355.13 | 🟡 **HOLD** | **+27.2 bps** (±11.3) | `+20.8 bps` | `+0.111 / +0.157` | `0.38%/h` | `vol_compressed` | Posição ativa há 7.7h (PnL: +1.64% | Pico: +1.64%) |
| **SOLUSDT** | $101.60 | ⚪ **CASH** | **+12.2 bps** (±25.8) | `+0.0 bps` | `+0.102 / +0.113` | `0.42%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 21:32:26 UTC` | Patrimônio: **$999.97 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,196.64 | 🟡 **HOLD** | **+50.8 bps** (±6.4) | `+43.2 bps` | `+0.192 / +0.336` | `0.28%/h` | `vol_compressed` `stretched_top` | Posição ativa há 5.5h (PnL: +0.81% | Pico: +0.81%) |
| **ETHUSDT** | $2,354.01 | 🟡 **HOLD** | **+27.2 bps** (±11.3) | `+20.8 bps` | `+0.111 / +0.157` | `0.38%/h` | `vol_compressed` | Posição ativa há 7.5h (PnL: +1.59% | Pico: +1.59%) |
| **SOLUSDT** | $101.45 | ⚪ **CASH** | **+12.2 bps** (±25.8) | `+0.0 bps` | `+0.102 / +0.113` | `0.42%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 21:17:25 UTC` | Patrimônio: **$997.47 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,740.12 | 🟡 **HOLD** | **+50.8 bps** (±6.4) | `+43.2 bps` | `+0.192 / +0.336` | `0.28%/h` | `vol_compressed` `stretched_top` | Posição ativa há 5.3h (PnL: +0.24% | Pico: +0.35%) |
| **ETHUSDT** | $2,345.10 | 🟡 **HOLD** | **+27.2 bps** (±11.3) | `+20.8 bps` | `+0.111 / +0.157` | `0.38%/h` | `vol_compressed` | Posição ativa há 7.3h (PnL: +1.20% | Pico: +1.57%) |
| **SOLUSDT** | $101.12 | ⚪ **CASH** | **+12.2 bps** (±25.8) | `+0.0 bps` | `+0.102 / +0.113` | `0.42%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 21:02:29 UTC` | Patrimônio: **$997.68 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,791.76 | 🟡 **HOLD** | **+50.8 bps** (±6.4) | `+43.2 bps` | `+0.192 / +0.336` | `0.28%/h` | `vol_compressed` `stretched_top` | Posição ativa há 5.0h (PnL: +0.31% | Pico: +0.35%) |
| **ETHUSDT** | $2,345.64 | 🟡 **HOLD** | **+27.2 bps** (±11.3) | `+20.8 bps` | `+0.111 / +0.157` | `0.38%/h` | `vol_compressed` | Posição ativa há 7.0h (PnL: +1.23% | Pico: +1.57%) |
| **SOLUSDT** | $101.09 | ⚪ **CASH** | **+12.2 bps** (±25.8) | `+0.0 bps` | `+0.102 / +0.113` | `0.42%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 20:47:15 UTC` | Patrimônio: **$997.03 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,699.57 | 🟡 **HOLD** | **+44.9 bps** (±9.6) | `+34.0 bps` | `+0.187 / +0.334` | `0.28%/h` | `vol_compressed` `stretched_top` | Posição ativa há 4.8h (PnL: +0.19% | Pico: +0.35%) |
| **ETHUSDT** | $2,342.78 | 🟡 **HOLD** | **+24.3 bps** (±9.3) | `+16.7 bps` | `+0.102 / +0.151` | `0.39%/h` | `vol_compressed` | Posição ativa há 6.7h (PnL: +1.10% | Pico: +1.57%) |
| **SOLUSDT** | $101.01 | ⚪ **CASH** | **+17.3 bps** (±17.6) | `+3.6 bps` | `+0.111 / +0.167` | `0.43%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 20:32:43 UTC` | Patrimônio: **$997.32 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,705.52 | 🟡 **HOLD** | **+44.9 bps** (±9.6) | `+34.0 bps` | `+0.187 / +0.334` | `0.28%/h` | `vol_compressed` `stretched_top` | Posição ativa há 4.5h (PnL: +0.20% | Pico: +0.35%) |
| **ETHUSDT** | $2,344.73 | 🟡 **HOLD** | **+24.3 bps** (±9.3) | `+16.7 bps` | `+0.102 / +0.151` | `0.39%/h` | `vol_compressed` | Posição ativa há 6.5h (PnL: +1.19% | Pico: +1.57%) |
| **SOLUSDT** | $101.09 | ⚪ **CASH** | **+17.3 bps** (±17.6) | `+3.6 bps` | `+0.111 / +0.167` | `0.43%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 20:17:23 UTC` | Patrimônio: **$998.09 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,792.86 | 🟡 **HOLD** | **+44.9 bps** (±9.6) | `+34.0 bps` | `+0.187 / +0.334` | `0.28%/h` | `vol_compressed` `stretched_top` | Posição ativa há 4.3h (PnL: +0.31% | Pico: +0.35%) |
| **ETHUSDT** | $2,348.52 | 🟡 **HOLD** | **+24.3 bps** (±9.3) | `+16.7 bps` | `+0.102 / +0.151` | `0.39%/h` | `vol_compressed` | Posição ativa há 6.3h (PnL: +1.35% | Pico: +1.57%) |
| **SOLUSDT** | $101.27 | ⚪ **CASH** | **+17.3 bps** (±17.6) | `+3.6 bps` | `+0.111 / +0.167` | `0.43%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 20:02:17 UTC` | Patrimônio: **$997.84 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,798.05 | 🟡 **HOLD** | **+44.9 bps** (±9.6) | `+34.0 bps` | `+0.187 / +0.334` | `0.28%/h` | `vol_compressed` `stretched_top` | Posição ativa há 4.0h (PnL: +0.31% | Pico: +0.35%) |
| **ETHUSDT** | $2,346.61 | 🟡 **HOLD** | **+24.3 bps** (±9.3) | `+16.7 bps` | `+0.102 / +0.151` | `0.39%/h` | `vol_compressed` | Posição ativa há 6.0h (PnL: +1.27% | Pico: +1.57%) |
| **SOLUSDT** | $101.12 | ⚪ **CASH** | **+17.3 bps** (±17.6) | `+3.6 bps` | `+0.111 / +0.167` | `0.43%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 19:47:05 UTC` | Patrimônio: **$998.72 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,824.00 | 🟡 **HOLD** | **+37.1 bps** (±7.2) | `+20.3 bps` | `+0.193 / +0.306` | `0.29%/h` | `stretched_top` | Posição ativa há 3.7h (PnL: +0.35% | Pico: +0.35%) |
| **ETHUSDT** | $2,352.33 | 🟡 **HOLD** | **+24.9 bps** (±6.8) | `+18.3 bps` | `+0.099 / +0.138` | `0.39%/h` | Liberado ✅ | Posição ativa há 5.7h (PnL: +1.52% | Pico: +1.57%) |
| **SOLUSDT** | $101.31 | ⚪ **CASH** | **+14.0 bps** (±18.5) | `-5.5 bps` | `+0.125 / +0.192` | `0.43%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 19:32:21 UTC` | Patrimônio: **$996.78 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,628.01 | 🟡 **HOLD** | **+37.1 bps** (±7.2) | `+20.3 bps` | `+0.193 / +0.306` | `0.29%/h` | `stretched_top` | Posição ativa há 3.5h (PnL: +0.10% | Pico: +0.28%) |
| **ETHUSDT** | $2,342.39 | 🟡 **HOLD** | **+24.9 bps** (±6.8) | `+18.3 bps` | `+0.099 / +0.138` | `0.39%/h` | Liberado ✅ | Posição ativa há 5.5h (PnL: +1.09% | Pico: +1.57%) |
| **SOLUSDT** | $101.02 | ⚪ **CASH** | **+14.0 bps** (±18.5) | `-5.5 bps` | `+0.125 / +0.192` | `0.43%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 19:16:56 UTC` | Patrimônio: **$996.94 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,664.53 | 🟡 **HOLD** | **+37.1 bps** (±7.2) | `+20.3 bps` | `+0.193 / +0.306` | `0.29%/h` | `stretched_top` | Posição ativa há 3.2h (PnL: +0.15% | Pico: +0.28%) |
| **ETHUSDT** | $2,342.86 | 🟡 **HOLD** | **+24.9 bps** (±6.8) | `+18.3 bps` | `+0.099 / +0.138` | `0.39%/h` | Liberado ✅ | Posição ativa há 5.2h (PnL: +1.11% | Pico: +1.57%) |
| **SOLUSDT** | $101.14 | ⚪ **CASH** | **+14.0 bps** (±18.5) | `-5.5 bps` | `+0.125 / +0.192` | `0.43%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 19:02:15 UTC` | Patrimônio: **$997.43 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,660.34 | 🟡 **HOLD** | **+37.1 bps** (±7.2) | `+20.3 bps` | `+0.193 / +0.306` | `0.29%/h` | `stretched_top` | Posição ativa há 3.0h (PnL: +0.14% | Pico: +0.28%) |
| **ETHUSDT** | $2,346.36 | 🟡 **HOLD** | **+24.9 bps** (±6.8) | `+18.3 bps` | `+0.099 / +0.138` | `0.39%/h` | Liberado ✅ | Posição ativa há 5.0h (PnL: +1.26% | Pico: +1.57%) |
| **SOLUSDT** | $101.05 | ⚪ **CASH** | **+14.0 bps** (±18.5) | `-5.5 bps` | `+0.125 / +0.192` | `0.43%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 18:47:11 UTC` | Patrimônio: **$997.91 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,717.64 | 🟡 **HOLD** | **+32.6 bps** (±4.9) | `+14.9 bps` | `+0.183 / +0.278` | `0.29%/h` | `stretched_top` | Posição ativa há 2.8h (PnL: +0.21% | Pico: +0.28%) |
| **ETHUSDT** | $2,348.70 | 🟡 **HOLD** | **+26.4 bps** (±15.7) | `+24.2 bps` | `+0.093 / +0.130` | `0.40%/h` | Liberado ✅ | Posição ativa há 4.7h (PnL: +1.36% | Pico: +1.57%) |
| **SOLUSDT** | $101.10 | ⚪ **CASH** | **+21.3 bps** (±11.9) | `+5.0 bps` | `+0.124 / +0.224` | `0.44%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 18:32:14 UTC` | Patrimônio: **$996.90 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,574.42 | 🟡 **HOLD** | **+32.6 bps** (±4.9) | `+14.9 bps` | `+0.183 / +0.278` | `0.29%/h` | `stretched_top` | Posição ativa há 2.5h (PnL: +0.04% | Pico: +0.28%) |
| **ETHUSDT** | $2,344.28 | 🟡 **HOLD** | **+26.4 bps** (±15.7) | `+24.2 bps` | `+0.093 / +0.130` | `0.40%/h` | Liberado ✅ | Posição ativa há 4.5h (PnL: +1.17% | Pico: +1.57%) |
| **SOLUSDT** | $100.86 | ⚪ **CASH** | **+21.3 bps** (±11.9) | `+5.0 bps` | `+0.124 / +0.224` | `0.44%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 18:17:08 UTC` | Patrimônio: **$997.53 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,617.05 | 🟡 **HOLD** | **+32.6 bps** (±4.9) | `+14.9 bps` | `+0.183 / +0.278` | `0.29%/h` | `stretched_top` | Posição ativa há 2.3h (PnL: +0.09% | Pico: +0.28%) |
| **ETHUSDT** | $2,347.89 | 🟡 **HOLD** | **+26.4 bps** (±15.7) | `+24.2 bps` | `+0.093 / +0.130` | `0.40%/h` | Liberado ✅ | Posição ativa há 4.2h (PnL: +1.32% | Pico: +1.57%) |
| **SOLUSDT** | $100.91 | ⚪ **CASH** | **+21.3 bps** (±11.9) | `+5.0 bps` | `+0.124 / +0.224` | `0.44%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 18:02:17 UTC` | Patrimônio: **$996.77 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,500.00 | 🟡 **HOLD** | **+32.6 bps** (±4.9) | `+14.9 bps` | `+0.183 / +0.278` | `0.29%/h` | `stretched_top` | Posição ativa há 2.0h (PnL: -0.06% | Pico: +0.28%) |
| **ETHUSDT** | $2,344.78 | 🟡 **HOLD** | **+26.4 bps** (±15.7) | `+24.2 bps` | `+0.093 / +0.130` | `0.40%/h` | Liberado ✅ | Posição ativa há 4.0h (PnL: +1.19% | Pico: +1.57%) |
| **SOLUSDT** | $100.73 | ⚪ **CASH** | **+21.3 bps** (±11.9) | `+5.0 bps` | `+0.124 / +0.224` | `0.44%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
