# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-28 16:32:50 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-28 16:32:50 UTC` | Patrimônio: **$994.50 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,545.45 | 🟡 **HOLD** | **+21.0 bps** (±8.7) | `+11.7 bps` | `+0.156 / +0.077` | `0.27%/h` | Liberado ✅ | Posição ativa há 6.5h (PnL: -1.24% | Pico: +0.05%) |
| **ETHUSDT** | $2,333.60 | ⚪ **CASH** | **+7.4 bps** (±7.1) | `+3.7 bps` | `+0.048 / -0.021` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.08 | ⚪ **CASH** | **+4.2 bps** (±9.3) | `-2.6 bps` | `+0.054 / -0.016` | `0.40%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 16:17:40 UTC` | Patrimônio: **$994.51 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,547.04 | 🟡 **HOLD** | **+21.0 bps** (±8.7) | `+11.7 bps` | `+0.156 / +0.077` | `0.27%/h` | Liberado ✅ | Posição ativa há 6.3h (PnL: -1.24% | Pico: +0.05%) |
| **ETHUSDT** | $2,332.87 | ⚪ **CASH** | **+7.4 bps** (±7.1) | `+3.7 bps` | `+0.048 / -0.021` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.96 | ⚪ **CASH** | **+4.2 bps** (±9.3) | `-2.6 bps` | `+0.054 / -0.016` | `0.40%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 16:02:50 UTC` | Patrimônio: **$994.55 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,558.01 | 🟡 **HOLD** | **+21.0 bps** (±8.7) | `+11.7 bps` | `+0.156 / +0.077` | `0.27%/h` | Liberado ✅ | Posição ativa há 6.0h (PnL: -1.23% | Pico: +0.05%) |
| **ETHUSDT** | $2,333.68 | ⚪ **CASH** | **+7.4 bps** (±7.1) | `+3.7 bps` | `+0.048 / -0.021` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.01 | ⚪ **CASH** | **+4.2 bps** (±9.3) | `-2.6 bps` | `+0.054 / -0.016` | `0.40%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 15:47:23 UTC` | Patrimônio: **$994.78 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,614.02 | 🟡 **HOLD** | **+22.9 bps** (±7.6) | `+12.6 bps` | `+0.170 / +0.080` | `0.28%/h` | Liberado ✅ | Posição ativa há 5.8h (PnL: -1.16% | Pico: +0.05%) |
| **ETHUSDT** | $2,335.03 | ⚪ **CASH** | **-1.1 bps** (±10.1) | `-12.0 bps` | `+0.074 / -0.059` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.06 | ⚪ **CASH** | **+5.2 bps** (±9.3) | `-4.1 bps` | `+0.066 / +0.006` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 15:32:27 UTC` | Patrimônio: **$994.63 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,578.00 | 🟡 **HOLD** | **+22.9 bps** (±7.6) | `+12.6 bps` | `+0.170 / +0.080` | `0.28%/h` | Liberado ✅ | Posição ativa há 5.5h (PnL: -1.20% | Pico: +0.05%) |
| **ETHUSDT** | $2,332.42 | ⚪ **CASH** | **-1.1 bps** (±10.1) | `-12.0 bps` | `+0.074 / -0.059` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.95 | ⚪ **CASH** | **+5.2 bps** (±9.3) | `-4.1 bps` | `+0.066 / +0.006` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 15:17:19 UTC` | Patrimônio: **$995.10 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,693.60 | 🟡 **HOLD** | **+22.9 bps** (±7.6) | `+12.6 bps` | `+0.170 / +0.080` | `0.28%/h` | Liberado ✅ | Posição ativa há 5.3h (PnL: -1.06% | Pico: +0.05%) |
| **ETHUSDT** | $2,336.63 | ⚪ **CASH** | **-1.1 bps** (±10.1) | `-12.0 bps` | `+0.074 / -0.059` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.09 | ⚪ **CASH** | **+5.2 bps** (±9.3) | `-4.1 bps` | `+0.066 / +0.006` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 15:02:09 UTC` | Patrimônio: **$995.03 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,677.13 | 🟡 **HOLD** | **+22.9 bps** (±7.6) | `+12.6 bps` | `+0.170 / +0.080` | `0.28%/h` | Liberado ✅ | Posição ativa há 5.0h (PnL: -1.08% | Pico: +0.05%) |
| **ETHUSDT** | $2,336.56 | ⚪ **CASH** | **-1.1 bps** (±10.1) | `-12.0 bps` | `+0.074 / -0.059` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.10 | ⚪ **CASH** | **+5.2 bps** (±9.3) | `-4.1 bps` | `+0.066 / +0.006` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 14:47:06 UTC` | Patrimônio: **$994.71 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,596.01 | 🟡 **HOLD** | **+22.3 bps** (±9.3) | `+11.5 bps` | `+0.170 / +0.087` | `0.28%/h` | Liberado ✅ | Posição ativa há 4.7h (PnL: -1.18% | Pico: +0.05%) |
| **ETHUSDT** | $2,333.32 | ⚪ **CASH** | **+17.7 bps** (±2.8) | `+18.4 bps` | `+0.075 / -0.023` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.95 | ⚪ **CASH** | **+5.5 bps** (±15.8) | `-4.0 bps` | `+0.078 / +0.014` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 14:32:08 UTC` | Patrimônio: **$994.52 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,550.01 | 🟡 **HOLD** | **+22.3 bps** (±9.3) | `+11.5 bps` | `+0.170 / +0.087` | `0.28%/h` | Liberado ✅ | Posição ativa há 4.5h (PnL: -1.24% | Pico: +0.05%) |
| **ETHUSDT** | $2,330.36 | ⚪ **CASH** | **+17.7 bps** (±2.8) | `+18.4 bps` | `+0.075 / -0.023` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.63 | ⚪ **CASH** | **+5.5 bps** (±15.8) | `-4.0 bps` | `+0.078 / +0.014` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 14:17:03 UTC` | Patrimônio: **$994.49 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,542.40 | 🟡 **HOLD** | **+22.3 bps** (±9.3) | `+11.5 bps` | `+0.170 / +0.087` | `0.28%/h` | Liberado ✅ | Posição ativa há 4.2h (PnL: -1.25% | Pico: +0.05%) |
| **ETHUSDT** | $2,327.86 | ⚪ **CASH** | **+17.7 bps** (±2.8) | `+18.4 bps` | `+0.075 / -0.023` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.65 | ⚪ **CASH** | **+5.5 bps** (±15.8) | `-4.0 bps` | `+0.078 / +0.014` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 14:02:10 UTC` | Patrimônio: **$995.15 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,705.98 | 🟡 **HOLD** | **+22.3 bps** (±9.3) | `+11.5 bps` | `+0.170 / +0.087` | `0.28%/h` | Liberado ✅ | Posição ativa há 4.0h (PnL: -1.05% | Pico: +0.05%) |
| **ETHUSDT** | $2,334.96 | ⚪ **CASH** | **+17.7 bps** (±2.8) | `+18.4 bps` | `+0.075 / -0.023` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.01 | ⚪ **CASH** | **+5.5 bps** (±15.8) | `-4.0 bps` | `+0.078 / +0.014` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 13:47:03 UTC` | Patrimônio: **$994.71 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,595.83 | 🟡 **HOLD** | **+21.3 bps** (±10.2) | `+8.2 bps` | `+0.175 / +0.100` | `0.29%/h` | Liberado ✅ | Posição ativa há 3.7h (PnL: -1.18% | Pico: +0.05%) |
| **ETHUSDT** | $2,330.73 | ⚪ **CASH** | **+19.9 bps** (±12.4) | `+21.4 bps` | `+0.081 / +0.008` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.27 | ⚪ **CASH** | **+1.5 bps** (±16.3) | `-12.9 bps` | `+0.085 / +0.026` | `0.41%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 13:32:28 UTC` | Patrimônio: **$995.34 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,753.38 | 🟡 **HOLD** | **+21.3 bps** (±10.2) | `+8.2 bps` | `+0.175 / +0.100` | `0.29%/h` | Liberado ✅ | Posição ativa há 3.5h (PnL: -0.99% | Pico: +0.05%) |
| **ETHUSDT** | $2,341.88 | ⚪ **CASH** | **+19.9 bps** (±12.4) | `+21.4 bps` | `+0.081 / +0.008` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.49 | ⚪ **CASH** | **+1.5 bps** (±16.3) | `-12.9 bps` | `+0.085 / +0.026` | `0.41%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 13:17:13 UTC` | Patrimônio: **$995.30 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,742.76 | 🟡 **HOLD** | **+21.3 bps** (±10.2) | `+8.2 bps` | `+0.175 / +0.100` | `0.29%/h` | Liberado ✅ | Posição ativa há 3.3h (PnL: -1.00% | Pico: +0.05%) |
| **ETHUSDT** | $2,339.43 | ⚪ **CASH** | **+19.9 bps** (±12.4) | `+21.4 bps` | `+0.081 / +0.008` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.46 | ⚪ **CASH** | **+1.5 bps** (±16.3) | `-12.9 bps` | `+0.085 / +0.026` | `0.41%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 13:02:02 UTC` | Patrimônio: **$995.35 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,755.93 | 🟡 **HOLD** | **+21.3 bps** (±10.2) | `+8.2 bps` | `+0.175 / +0.100` | `0.29%/h` | Liberado ✅ | Posição ativa há 3.0h (PnL: -0.99% | Pico: +0.05%) |
| **ETHUSDT** | $2,340.89 | ⚪ **CASH** | **+19.9 bps** (±12.4) | `+21.4 bps` | `+0.081 / +0.008` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.62 | ⚪ **CASH** | **+1.5 bps** (±16.3) | `-12.9 bps` | `+0.085 / +0.026` | `0.41%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 12:47:00 UTC` | Patrimônio: **$995.41 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,770.00 | 🟡 **HOLD** | **+30.8 bps** (±10.8) | `+21.9 bps` | `+0.192 / +0.118` | `0.26%/h` | Liberado ✅ | Posição ativa há 2.7h (PnL: -0.97% | Pico: +0.05%) |
| **ETHUSDT** | $2,340.04 | ⚪ **CASH** | **+24.6 bps** (±10.9) | `+26.0 bps` | `+0.096 / +0.030` | `0.33%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $101.59 | ⚪ **CASH** | **+11.5 bps** (±24.3) | `-1.5 bps` | `+0.117 / +0.090` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 12:32:02 UTC` | Patrimônio: **$996.12 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,945.09 | 🟡 **HOLD** | **+30.8 bps** (±10.8) | `+21.9 bps` | `+0.192 / +0.118` | `0.26%/h` | Liberado ✅ | Posição ativa há 2.5h (PnL: -0.75% | Pico: +0.05%) |
| **ETHUSDT** | $2,349.05 | ⚪ **CASH** | **+24.6 bps** (±10.9) | `+26.0 bps` | `+0.096 / +0.030` | `0.33%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $102.05 | ⚪ **CASH** | **+11.5 bps** (±24.3) | `-1.5 bps` | `+0.117 / +0.090` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 12:16:59 UTC` | Patrimônio: **$996.39 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,012.00 | 🟡 **HOLD** | **+30.8 bps** (±10.8) | `+21.9 bps` | `+0.192 / +0.118` | `0.26%/h` | Liberado ✅ | Posição ativa há 2.2h (PnL: -0.67% | Pico: +0.05%) |
| **ETHUSDT** | $2,348.60 | ⚪ **CASH** | **+24.6 bps** (±10.9) | `+26.0 bps` | `+0.096 / +0.030` | `0.33%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $102.05 | ⚪ **CASH** | **+11.5 bps** (±24.3) | `-1.5 bps` | `+0.117 / +0.090` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 12:02:27 UTC` | Patrimônio: **$997.59 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,309.10 | 🟡 **HOLD** | **+30.8 bps** (±10.8) | `+21.9 bps` | `+0.192 / +0.118` | `0.26%/h` | Liberado ✅ | Posição ativa há 2.0h (PnL: -0.31% | Pico: +0.05%) |
| **ETHUSDT** | $2,361.28 | ⚪ **CASH** | **+24.6 bps** (±10.9) | `+26.0 bps` | `+0.096 / +0.030` | `0.33%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $102.74 | ⚪ **CASH** | **+11.5 bps** (±24.3) | `-1.5 bps` | `+0.117 / +0.090` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 11:47:16 UTC` | Patrimônio: **$998.00 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,411.74 | 🟡 **HOLD** | **+44.4 bps** (±10.7) | `+43.7 bps` | `+0.198 / +0.150` | `0.26%/h` | Liberado ✅ | Posição ativa há 1.8h (PnL: -0.18% | Pico: +0.05%) |
| **ETHUSDT** | $2,366.55 | ⚪ **CASH** | **+13.5 bps** (±6.3) | `+3.7 bps` | `+0.107 / +0.026` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.93 | ⚪ **CASH** | **+10.0 bps** (±29.3) | `-6.0 bps` | `+0.127 / +0.112` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 11:32:14 UTC` | Patrimônio: **$998.01 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,412.58 | 🟡 **HOLD** | **+44.4 bps** (±10.7) | `+43.7 bps` | `+0.198 / +0.150` | `0.26%/h` | Liberado ✅ | Posição ativa há 1.5h (PnL: -0.18% | Pico: +0.05%) |
| **ETHUSDT** | $2,364.04 | ⚪ **CASH** | **+13.5 bps** (±6.3) | `+3.7 bps` | `+0.107 / +0.026` | `0.34%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.84 | ⚪ **CASH** | **+10.0 bps** (±29.3) | `-6.0 bps` | `+0.127 / +0.112` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

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
