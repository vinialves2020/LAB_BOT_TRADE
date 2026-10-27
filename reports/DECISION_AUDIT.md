# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-27 20:47:15 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-10-27 17:47:13 UTC` | Patrimônio: **$998.19 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,682.06 | 🟡 **HOLD** | **+40.8 bps** (±14.9) | `+32.8 bps` | `+0.181 / +0.266` | `0.29%/h` | `stretched_top` | Posição ativa há 1.8h (PnL: +0.17% | Pico: +0.28%) |
| **ETHUSDT** | $2,351.32 | 🟡 **HOLD** | **+29.2 bps** (±11.5) | `+19.9 bps` | `+0.118 / +0.225` | `0.40%/h` | `stretched_top` | Posição ativa há 3.7h (PnL: +1.47% | Pico: +1.57%) |
| **SOLUSDT** | $101.11 | ⚪ **CASH** | **+21.5 bps** (±19.7) | `+8.8 bps` | `+0.095 / +0.240` | `0.44%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 17:32:16 UTC` | Patrimônio: **$998.77 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,772.01 | 🟡 **HOLD** | **+40.8 bps** (±14.9) | `+32.8 bps` | `+0.181 / +0.266` | `0.29%/h` | `stretched_top` | Posição ativa há 1.5h (PnL: +0.28% | Pico: +0.28%) |
| **ETHUSDT** | $2,353.68 | 🟡 **HOLD** | **+29.2 bps** (±11.5) | `+19.9 bps` | `+0.118 / +0.225` | `0.40%/h` | `stretched_top` | Posição ativa há 3.5h (PnL: +1.57% | Pico: +1.57%) |
| **SOLUSDT** | $101.16 | ⚪ **CASH** | **+21.5 bps** (±19.7) | `+8.8 bps` | `+0.095 / +0.240` | `0.44%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 17:16:59 UTC` | Patrimônio: **$997.99 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,632.77 | 🟡 **HOLD** | **+40.8 bps** (±14.9) | `+32.8 bps` | `+0.181 / +0.266` | `0.29%/h` | `stretched_top` | Posição ativa há 1.2h (PnL: +0.11% | Pico: +0.12%) |
| **ETHUSDT** | $2,350.90 | 🟡 **HOLD** | **+29.2 bps** (±11.5) | `+19.9 bps` | `+0.118 / +0.225` | `0.40%/h` | `stretched_top` | Posição ativa há 3.2h (PnL: +1.45% | Pico: +1.54%) |
| **SOLUSDT** | $101.05 | ⚪ **CASH** | **+21.5 bps** (±19.7) | `+8.8 bps` | `+0.095 / +0.240` | `0.44%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 17:02:17 UTC` | Patrimônio: **$997.45 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,579.66 | 🟡 **HOLD** | **+40.8 bps** (±14.9) | `+32.8 bps` | `+0.181 / +0.266` | `0.29%/h` | `stretched_top` | Posição ativa há 1.0h (PnL: +0.04% | Pico: +0.12%) |
| **ETHUSDT** | $2,348.07 | 🟡 **HOLD** | **+29.2 bps** (±11.5) | `+19.9 bps` | `+0.118 / +0.225` | `0.40%/h` | `stretched_top` | Posição ativa há 3.0h (PnL: +1.33% | Pico: +1.54%) |
| **SOLUSDT** | $101.12 | ⚪ **CASH** | **+21.5 bps** (±19.7) | `+8.8 bps` | `+0.095 / +0.240` | `0.44%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 16:47:16 UTC` | Patrimônio: **$997.37 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,575.70 | 🟡 **HOLD** | **+27.4 bps** (±8.0) | `+13.7 bps` | `+0.162 / +0.210` | `0.30%/h` | Liberado ✅ | Posição ativa há 0.8h (PnL: +0.04% | Pico: +0.12%) |
| **ETHUSDT** | $2,347.60 | 🟡 **HOLD** | **+37.7 bps** (±7.7) | `+40.4 bps` | `+0.109 / +0.166` | `0.41%/h` | `stretched_top` | Posição ativa há 2.8h (PnL: +1.31% | Pico: +1.54%) |
| **SOLUSDT** | $100.92 | ⚪ **CASH** | **+20.7 bps** (±10.6) | `+8.1 bps` | `+0.092 / +0.223` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 16:32:10 UTC` | Patrimônio: **$998.10 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,639.44 | 🟡 **HOLD** | **+27.4 bps** (±8.0) | `+13.7 bps` | `+0.162 / +0.210` | `0.30%/h` | Liberado ✅ | Posição ativa há 0.5h (PnL: +0.12% | Pico: +0.12%) |
| **ETHUSDT** | $2,351.52 | 🟡 **HOLD** | **+37.7 bps** (±7.7) | `+40.4 bps` | `+0.109 / +0.166` | `0.41%/h` | `stretched_top` | Posição ativa há 2.5h (PnL: +1.48% | Pico: +1.54%) |
| **SOLUSDT** | $101.20 | ⚪ **CASH** | **+20.7 bps** (±10.6) | `+8.1 bps` | `+0.092 / +0.223` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 16:17:12 UTC` | Patrimônio: **$997.04 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,515.76 | 🟡 **HOLD** | **+27.4 bps** (±8.0) | `+13.7 bps` | `+0.162 / +0.210` | `0.30%/h` | Liberado ✅ | Posição ativa há 0.3h (PnL: -0.04% | Pico: +0.00%) |
| **ETHUSDT** | $2,346.39 | 🟡 **HOLD** | **+37.7 bps** (±7.7) | `+40.4 bps` | `+0.109 / +0.166` | `0.41%/h` | `stretched_top` | Posição ativa há 2.2h (PnL: +1.26% | Pico: +1.54%) |
| **SOLUSDT** | $100.97 | ⚪ **CASH** | **+20.7 bps** (±10.6) | `+8.1 bps` | `+0.092 / +0.223` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 16:02:07 UTC` | Patrimônio: **$997.12 USDT** (Caixa: `$445.52`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,544.86 | 🟢 **BUY** | **+27.4 bps** (±8.0) | `+13.7 bps` | `+0.162 / +0.210` | `0.30%/h` | Liberado ✅ | Entrada Swing 12h aprovada (Alpha +27.4 bps > 24.0 bps | CVD 24h +0.162) |
| **ETHUSDT** | $2,346.44 | 🟡 **HOLD** | **+37.7 bps** (±7.7) | `+40.4 bps` | `+0.109 / +0.166` | `0.41%/h` | `stretched_top` | Posição ativa há 2.0h (PnL: +1.26% | Pico: +1.54%) |
| **SOLUSDT** | $100.95 | ⚪ **CASH** | **+20.7 bps** (±10.6) | `+8.1 bps` | `+0.092 / +0.223` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 15:47:15 UTC` | Patrimônio: **$998.29 USDT** (Caixa: `$665.35`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,672.00 | ⚪ **CASH** | **+21.5 bps** (±4.6) | `+8.2 bps` | `+0.152 / +0.143` | `0.30%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,352.80 | 🟡 **HOLD** | **+18.6 bps** (±10.8) | `+14.3 bps` | `+0.084 / +0.088` | `0.42%/h` | Liberado ✅ | Posição ativa há 1.7h (PnL: +1.54% | Pico: +1.54%) |
| **SOLUSDT** | $101.18 | ⚪ **CASH** | **+11.3 bps** (±15.0) | `-3.9 bps` | `+0.075 / +0.189` | `0.46%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 15:17:13 UTC` | Patrimônio: **$996.00 USDT** (Caixa: `$665.35`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,420.43 | ⚪ **CASH** | **+21.5 bps** (±4.6) | `+8.2 bps` | `+0.152 / +0.143` | `0.30%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,336.66 | 🟡 **HOLD** | **+18.6 bps** (±10.8) | `+14.3 bps` | `+0.084 / +0.088` | `0.42%/h` | Liberado ✅ | Posição ativa há 1.2h (PnL: +0.84% | Pico: +0.90%) |
| **SOLUSDT** | $100.75 | ⚪ **CASH** | **+11.3 bps** (±15.0) | `-3.9 bps` | `+0.075 / +0.189` | `0.46%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 15:01:58 UTC` | Patrimônio: **$996.21 USDT** (Caixa: `$665.35`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,477.21 | ⚪ **CASH** | **+21.5 bps** (±4.6) | `+8.2 bps` | `+0.152 / +0.143` | `0.30%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,338.15 | 🟡 **HOLD** | **+18.6 bps** (±10.8) | `+14.3 bps` | `+0.084 / +0.088` | `0.42%/h` | Liberado ✅ | Posição ativa há 1.0h (PnL: +0.90% | Pico: +0.90%) |
| **SOLUSDT** | $100.84 | ⚪ **CASH** | **+11.3 bps** (±15.0) | `-3.9 bps` | `+0.075 / +0.189` | `0.46%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 14:47:03 UTC` | Patrimônio: **$994.99 USDT** (Caixa: `$665.35`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,240.44 | ⚪ **CASH** | **+15.2 bps** (±7.8) | `-4.1 bps` | `+0.165 / +0.136` | `0.30%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,329.49 | 🟡 **HOLD** | **+40.8 bps** (±11.9) | `+51.2 bps` | `+0.089 / +0.128` | `0.42%/h` | Liberado ✅ | Posição ativa há 0.7h (PnL: +0.53% | Pico: +0.53%) |
| **SOLUSDT** | $100.51 | ⚪ **CASH** | **+5.2 bps** (±9.7) | `-13.2 bps` | `+0.069 / +0.145` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 14:32:17 UTC` | Patrimônio: **$994.83 USDT** (Caixa: `$665.35`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,242.07 | ⚪ **CASH** | **+15.2 bps** (±7.8) | `-4.1 bps` | `+0.165 / +0.136` | `0.30%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,328.34 | 🟡 **HOLD** | **+40.8 bps** (±11.9) | `+51.2 bps` | `+0.089 / +0.128` | `0.42%/h` | Liberado ✅ | Posição ativa há 0.5h (PnL: +0.48% | Pico: +0.48%) |
| **SOLUSDT** | $100.50 | ⚪ **CASH** | **+5.2 bps** (±9.7) | `-13.2 bps` | `+0.069 / +0.145` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 14:17:12 UTC` | Patrimônio: **$993.75 USDT** (Caixa: `$665.35`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,028.01 | ⚪ **CASH** | **+15.2 bps** (±7.8) | `-4.1 bps` | `+0.165 / +0.136` | `0.30%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,320.74 | 🟡 **HOLD** | **+40.8 bps** (±11.9) | `+51.2 bps` | `+0.089 / +0.128` | `0.42%/h` | Liberado ✅ | Posição ativa há 0.2h (PnL: +0.15% | Pico: +0.15%) |
| **SOLUSDT** | $100.18 | ⚪ **CASH** | **+5.2 bps** (±9.7) | `-13.2 bps` | `+0.069 / +0.145` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 14:02:17 UTC` | Patrimônio: **$993.25 USDT** (Caixa: `$665.35`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,902.01 | ⚪ **CASH** | **+15.2 bps** (±7.8) | `-4.1 bps` | `+0.165 / +0.136` | `0.30%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,317.20 | 🟢 **BUY** | **+40.8 bps** (±11.9) | `+51.2 bps` | `+0.089 / +0.128` | `0.42%/h` | Liberado ✅ | Entrada Swing 12h aprovada (Alpha +40.8 bps > 24.0 bps | CVD 24h +0.089) |
| **SOLUSDT** | $99.95 | ⚪ **CASH** | **+5.2 bps** (±9.7) | `-13.2 bps` | `+0.069 / +0.145` | `0.45%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 13:47:09 UTC` | Patrimônio: **$993.64 USDT** (Caixa: `$993.64`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,211.49 | ⚪ **CASH** | **+15.1 bps** (±3.6) | `-4.0 bps` | `+0.150 / +0.154` | `0.29%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,329.32 | ⚪ **CASH** | **+38.7 bps** (±11.8) | `+48.5 bps` | `+0.073 / +0.145` | `0.41%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $100.54 | ⚪ **CASH** | **+0.8 bps** (±11.2) | `-19.3 bps` | `+0.063 / +0.143` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 13:32:04 UTC` | Patrimônio: **$993.64 USDT** (Caixa: `$993.64`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,075.73 | ⚪ **CASH** | **+15.1 bps** (±3.6) | `-4.0 bps` | `+0.150 / +0.154` | `0.29%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,325.97 | ⚪ **CASH** | **+38.7 bps** (±11.8) | `+48.5 bps` | `+0.073 / +0.145` | `0.41%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $100.37 | ⚪ **CASH** | **+0.8 bps** (±11.2) | `-19.3 bps` | `+0.063 / +0.143` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 13:17:08 UTC` | Patrimônio: **$993.64 USDT** (Caixa: `$993.64`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,255.86 | ⚪ **CASH** | **+15.1 bps** (±3.6) | `-4.0 bps` | `+0.150 / +0.154` | `0.29%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,328.89 | ⚪ **CASH** | **+38.7 bps** (±11.8) | `+48.5 bps` | `+0.073 / +0.145` | `0.41%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $100.68 | ⚪ **CASH** | **+0.8 bps** (±11.2) | `-19.3 bps` | `+0.063 / +0.143` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 13:02:11 UTC` | Patrimônio: **$993.64 USDT** (Caixa: `$993.64`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,321.15 | ⚪ **CASH** | **+15.1 bps** (±3.6) | `-4.0 bps` | `+0.150 / +0.154` | `0.29%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,336.00 | ⚪ **CASH** | **+38.7 bps** (±11.8) | `+48.5 bps` | `+0.073 / +0.145` | `0.41%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $100.94 | ⚪ **CASH** | **+0.8 bps** (±11.2) | `-19.3 bps` | `+0.063 / +0.143` | `0.44%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 12:46:57 UTC` | Patrimônio: **$993.64 USDT** (Caixa: `$993.64`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,357.26 | ⚪ **CASH** | **+11.6 bps** (±6.8) | `-4.9 bps` | `+0.147 / +0.084` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,335.02 | ⚪ **CASH** | **+13.2 bps** (±6.4) | `+7.6 bps` | `+0.055 / +0.076` | `0.39%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.78 | ⚪ **CASH** | **+1.0 bps** (±2.5) | `-15.3 bps` | `+0.057 / +0.075` | `0.42%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 12:32:11 UTC` | Patrimônio: **$993.64 USDT** (Caixa: `$993.64`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,248.51 | ⚪ **CASH** | **+11.6 bps** (±6.8) | `-4.9 bps` | `+0.147 / +0.084` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,327.30 | ⚪ **CASH** | **+13.2 bps** (±6.4) | `+7.6 bps` | `+0.055 / +0.076` | `0.39%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.54 | ⚪ **CASH** | **+1.0 bps** (±2.5) | `-15.3 bps` | `+0.057 / +0.075` | `0.42%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 12:16:59 UTC` | Patrimônio: **$993.64 USDT** (Caixa: `$993.64`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,995.59 | ⚪ **CASH** | **+11.6 bps** (±6.8) | `-4.9 bps` | `+0.147 / +0.084` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,317.87 | ⚪ **CASH** | **+13.2 bps** (±6.4) | `+7.6 bps` | `+0.055 / +0.076` | `0.39%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.15 | ⚪ **CASH** | **+1.0 bps** (±2.5) | `-15.3 bps` | `+0.057 / +0.075` | `0.42%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 12:02:09 UTC` | Patrimônio: **$993.64 USDT** (Caixa: `$993.64`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,843.11 | ⚪ **CASH** | **+11.6 bps** (±6.8) | `-4.9 bps` | `+0.147 / +0.084` | `0.28%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,313.27 | ⚪ **CASH** | **+13.2 bps** (±6.4) | `+7.6 bps` | `+0.055 / +0.076` | `0.39%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $99.96 | ⚪ **CASH** | **+1.0 bps** (±2.5) | `-15.3 bps` | `+0.057 / +0.075` | `0.42%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-27 11:47:26 UTC` | Patrimônio: **$993.64 USDT** (Caixa: `$993.64`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,896.00 | ⚪ **CASH** | **+12.2 bps** (±9.8) | `-4.5 bps` | `+0.150 / +0.096` | `0.28%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,315.29 | ⚪ **CASH** | **+15.4 bps** (±2.8) | `+14.2 bps` | `+0.048 / +0.034` | `0.40%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.24 | ⚪ **CASH** | **-0.9 bps** (±9.1) | `-16.2 bps` | `+0.062 / +0.043` | `0.43%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
