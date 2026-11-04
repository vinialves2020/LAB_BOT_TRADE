# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-04 19:16:28 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-04 19:16:28 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,298.01 | ⚪ **CASH** | **-16.8 bps** (±10.2) | `-54.2 bps` | `+0.098 / +0.169` | `0.45%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,424.92 | ⚪ **CASH** | **+42.5 bps** (±13.6) | `+68.0 bps` | `+0.024 / +0.069` | `0.67%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $95.40 | ⚪ **CASH** | **+26.9 bps** (±11.0) | `+33.6 bps` | `+0.071 / +0.085` | `0.71%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 19:01:25 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,273.59 | ⚪ **CASH** | **-16.8 bps** (±10.2) | `-54.2 bps` | `+0.098 / +0.169` | `0.45%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,419.80 | ⚪ **CASH** | **+42.5 bps** (±13.6) | `+68.0 bps` | `+0.024 / +0.069` | `0.67%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $95.09 | ⚪ **CASH** | **+26.9 bps** (±11.0) | `+33.6 bps` | `+0.071 / +0.085` | `0.71%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 18:46:30 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,365.47 | ⚪ **CASH** | **-18.2 bps** (±15.7) | `-53.8 bps` | `+0.094 / +0.149` | `0.45%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,422.40 | ⚪ **CASH** | **+51.0 bps** (±14.3) | `+84.8 bps` | `+0.022 / +0.058` | `0.67%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $95.39 | ⚪ **CASH** | **+23.4 bps** (±12.8) | `+28.9 bps` | `+0.068 / +0.070` | `0.71%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 18:30:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,613.00 | ⚪ **CASH** | **-18.2 bps** (±15.7) | `-53.8 bps` | `+0.094 / +0.149` | `0.45%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,433.45 | ⚪ **CASH** | **+51.0 bps** (±14.3) | `+84.8 bps` | `+0.022 / +0.058` | `0.67%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $95.81 | ⚪ **CASH** | **+23.4 bps** (±12.8) | `+28.9 bps` | `+0.068 / +0.070` | `0.71%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 18:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,646.01 | ⚪ **CASH** | **-18.2 bps** (±15.7) | `-53.8 bps` | `+0.094 / +0.149` | `0.45%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,434.75 | ⚪ **CASH** | **+51.0 bps** (±14.3) | `+84.8 bps` | `+0.022 / +0.058` | `0.67%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $96.07 | ⚪ **CASH** | **+23.4 bps** (±12.8) | `+28.9 bps` | `+0.068 / +0.070` | `0.71%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 18:01:29 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,600.00 | ⚪ **CASH** | **-18.2 bps** (±15.7) | `-53.8 bps` | `+0.094 / +0.149` | `0.45%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,430.00 | ⚪ **CASH** | **+51.0 bps** (±14.3) | `+84.8 bps` | `+0.022 / +0.058` | `0.67%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $96.02 | ⚪ **CASH** | **+23.4 bps** (±12.8) | `+28.9 bps` | `+0.068 / +0.070` | `0.71%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 17:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,362.00 | ⚪ **CASH** | **-5.4 bps** (±14.6) | `-28.5 bps` | `+0.087 / +0.131` | `0.46%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,425.76 | ⚪ **CASH** | **+70.8 bps** (±14.3) | `+119.8 bps` | `+0.026 / +0.072` | `0.68%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $95.75 | ⚪ **CASH** | **+23.6 bps** (±17.9) | `+31.3 bps` | `+0.065 / +0.064` | `0.69%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 17:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,422.46 | ⚪ **CASH** | **-5.4 bps** (±14.6) | `-28.5 bps` | `+0.087 / +0.131` | `0.46%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,427.45 | ⚪ **CASH** | **+70.8 bps** (±14.3) | `+119.8 bps` | `+0.026 / +0.072` | `0.68%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $95.92 | ⚪ **CASH** | **+23.6 bps** (±17.9) | `+31.3 bps` | `+0.065 / +0.064` | `0.69%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 17:16:29 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,320.00 | ⚪ **CASH** | **-5.4 bps** (±14.6) | `-28.5 bps` | `+0.087 / +0.131` | `0.46%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,425.40 | ⚪ **CASH** | **+70.8 bps** (±14.3) | `+119.8 bps` | `+0.026 / +0.072` | `0.68%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $95.97 | ⚪ **CASH** | **+23.6 bps** (±17.9) | `+31.3 bps` | `+0.065 / +0.064` | `0.69%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 17:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,537.74 | ⚪ **CASH** | **-5.4 bps** (±14.6) | `-28.5 bps` | `+0.087 / +0.131` | `0.46%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,433.57 | ⚪ **CASH** | **+70.8 bps** (±14.3) | `+119.8 bps` | `+0.026 / +0.072` | `0.68%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $96.64 | ⚪ **CASH** | **+23.6 bps** (±17.9) | `+31.3 bps` | `+0.065 / +0.064` | `0.69%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 16:46:30 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,690.00 | ⚪ **CASH** | **+12.3 bps** (±14.0) | `+7.6 bps` | `+0.073 / +0.101` | `0.46%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,438.35 | ⚪ **CASH** | **+79.8 bps** (±15.6) | `+139.1 bps` | `+0.013 / +0.060` | `0.68%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $96.99 | ⚪ **CASH** | **+25.5 bps** (±10.1) | `+34.4 bps` | `+0.059 / +0.067` | `0.70%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 16:31:21 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,598.00 | ⚪ **CASH** | **+12.3 bps** (±14.0) | `+7.6 bps` | `+0.073 / +0.101` | `0.46%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,432.28 | ⚪ **CASH** | **+79.8 bps** (±15.6) | `+139.1 bps` | `+0.013 / +0.060` | `0.68%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $96.64 | ⚪ **CASH** | **+25.5 bps** (±10.1) | `+34.4 bps` | `+0.059 / +0.067` | `0.70%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 16:16:16 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,576.01 | ⚪ **CASH** | **+12.3 bps** (±14.0) | `+7.6 bps` | `+0.073 / +0.101` | `0.46%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,438.70 | ⚪ **CASH** | **+79.8 bps** (±15.6) | `+139.1 bps` | `+0.013 / +0.060` | `0.68%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $97.10 | ⚪ **CASH** | **+25.5 bps** (±10.1) | `+34.4 bps` | `+0.059 / +0.067` | `0.70%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 16:01:25 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,433.54 | ⚪ **CASH** | **+12.3 bps** (±14.0) | `+7.6 bps` | `+0.073 / +0.101` | `0.46%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,432.11 | ⚪ **CASH** | **+79.8 bps** (±15.6) | `+139.1 bps` | `+0.013 / +0.060` | `0.68%/h` | `weak_order_flow` `stretched_top` | Filtro: absorção institucional CVD 24h/6h insuficiente |
| **SOLUSDT** | $97.06 | ⚪ **CASH** | **+25.5 bps** (±10.1) | `+34.4 bps` | `+0.059 / +0.067` | `0.70%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 15:45:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,409.68 | ⚪ **CASH** | **+13.9 bps** (±12.4) | `+16.9 bps` | `+0.055 / +0.039` | `0.42%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,427.36 | ⚪ **CASH** | **+32.7 bps** (±18.8) | `+55.0 bps` | `+0.013 / +0.059` | `0.61%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.63 | ⚪ **CASH** | **+14.4 bps** (±4.9) | `+7.9 bps` | `+0.071 / +0.147` | `0.66%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 15:31:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,579.25 | ⚪ **CASH** | **+13.9 bps** (±12.4) | `+16.9 bps` | `+0.055 / +0.039` | `0.42%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,438.10 | ⚪ **CASH** | **+32.7 bps** (±18.8) | `+55.0 bps` | `+0.013 / +0.059` | `0.61%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $96.85 | ⚪ **CASH** | **+14.4 bps** (±4.9) | `+7.9 bps` | `+0.071 / +0.147` | `0.66%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 15:01:31 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,550.28 | ⚪ **CASH** | **+13.9 bps** (±12.4) | `+16.9 bps` | `+0.055 / +0.039` | `0.42%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,400.63 | ⚪ **CASH** | **+32.7 bps** (±18.8) | `+55.0 bps` | `+0.013 / +0.059` | `0.61%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.76 | ⚪ **CASH** | **+14.4 bps** (±4.9) | `+7.9 bps` | `+0.071 / +0.147` | `0.66%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 14:46:15 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,219.85 | ⚪ **CASH** | **+20.1 bps** (±6.1) | `+28.9 bps` | `+0.044 / +0.033` | `0.37%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,348.45 | ⚪ **CASH** | **+17.8 bps** (±10.4) | `+32.2 bps` | `-0.007 / +0.009` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $94.54 | ⚪ **CASH** | **+15.2 bps** (±13.1) | `+9.4 bps` | `+0.058 / +0.193` | `0.51%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 14:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,527.34 | ⚪ **CASH** | **+20.1 bps** (±6.1) | `+28.9 bps` | `+0.044 / +0.033` | `0.37%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,323.16 | ⚪ **CASH** | **+17.8 bps** (±10.4) | `+32.2 bps` | `-0.007 / +0.009` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.17 | ⚪ **CASH** | **+15.2 bps** (±13.1) | `+9.4 bps` | `+0.058 / +0.193` | `0.51%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 14:16:30 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,399.18 | ⚪ **CASH** | **+20.1 bps** (±6.1) | `+28.9 bps` | `+0.044 / +0.033` | `0.37%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,320.20 | ⚪ **CASH** | **+17.8 bps** (±10.4) | `+32.2 bps` | `-0.007 / +0.009` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.03 | ⚪ **CASH** | **+15.2 bps** (±13.1) | `+9.4 bps` | `+0.058 / +0.193` | `0.51%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 14:01:28 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,320.00 | ⚪ **CASH** | **+20.1 bps** (±6.1) | `+28.9 bps` | `+0.044 / +0.033` | `0.37%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,315.99 | ⚪ **CASH** | **+17.8 bps** (±10.4) | `+32.2 bps` | `-0.007 / +0.009` | `0.43%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.81 | ⚪ **CASH** | **+15.2 bps** (±13.1) | `+9.4 bps` | `+0.058 / +0.193` | `0.51%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 13:45:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,409.85 | ⚪ **CASH** | **+22.8 bps** (±4.3) | `+31.2 bps` | `+0.061 / +0.031` | `0.37%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,319.68 | ⚪ **CASH** | **+20.8 bps** (±12.6) | `+35.1 bps` | `+0.012 / +0.012` | `0.44%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.94 | ⚪ **CASH** | **+10.8 bps** (±13.0) | `+3.9 bps` | `+0.046 / +0.161` | `0.52%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 13:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,400.00 | ⚪ **CASH** | **+22.8 bps** (±4.3) | `+31.2 bps` | `+0.061 / +0.031` | `0.37%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,318.81 | ⚪ **CASH** | **+20.8 bps** (±12.6) | `+35.1 bps` | `+0.012 / +0.012` | `0.44%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.79 | ⚪ **CASH** | **+10.8 bps** (±13.0) | `+3.9 bps` | `+0.046 / +0.161` | `0.52%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 13:16:17 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,364.00 | ⚪ **CASH** | **+22.8 bps** (±4.3) | `+31.2 bps` | `+0.061 / +0.031` | `0.37%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,316.86 | ⚪ **CASH** | **+20.8 bps** (±12.6) | `+35.1 bps` | `+0.012 / +0.012` | `0.44%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.64 | ⚪ **CASH** | **+10.8 bps** (±13.0) | `+3.9 bps` | `+0.046 / +0.161` | `0.52%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 13:01:34 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,470.72 | ⚪ **CASH** | **+22.8 bps** (±4.3) | `+31.2 bps` | `+0.061 / +0.031` | `0.37%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,320.05 | ⚪ **CASH** | **+20.8 bps** (±12.6) | `+35.1 bps` | `+0.012 / +0.012` | `0.44%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.85 | ⚪ **CASH** | **+10.8 bps** (±13.0) | `+3.9 bps` | `+0.046 / +0.161` | `0.52%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 12:46:10 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,260.00 | ⚪ **CASH** | **+17.1 bps** (±12.9) | `+17.0 bps` | `+0.079 / +0.074` | `0.38%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,317.84 | ⚪ **CASH** | **+9.3 bps** (±11.4) | `+13.0 bps` | `+0.021 / -0.000` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.82 | ⚪ **CASH** | **+17.1 bps** (±17.3) | `+12.3 bps` | `+0.053 / +0.196` | `0.49%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 12:30:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,285.14 | ⚪ **CASH** | **+17.1 bps** (±12.9) | `+17.0 bps` | `+0.079 / +0.074` | `0.38%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,318.85 | ⚪ **CASH** | **+9.3 bps** (±11.4) | `+13.0 bps` | `+0.021 / -0.000` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.92 | ⚪ **CASH** | **+17.1 bps** (±17.3) | `+12.3 bps` | `+0.053 / +0.196` | `0.49%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 12:16:17 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,087.28 | ⚪ **CASH** | **+17.1 bps** (±12.9) | `+17.0 bps` | `+0.079 / +0.074` | `0.38%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,314.49 | ⚪ **CASH** | **+9.3 bps** (±11.4) | `+13.0 bps` | `+0.021 / -0.000` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.71 | ⚪ **CASH** | **+17.1 bps** (±17.3) | `+12.3 bps` | `+0.053 / +0.196` | `0.49%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 12:01:19 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,499.99 | ⚪ **CASH** | **+17.1 bps** (±12.9) | `+17.0 bps` | `+0.079 / +0.074` | `0.38%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,328.96 | ⚪ **CASH** | **+9.3 bps** (±11.4) | `+13.0 bps` | `+0.021 / -0.000` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.60 | ⚪ **CASH** | **+17.1 bps** (±17.3) | `+12.3 bps` | `+0.053 / +0.196` | `0.49%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 11:46:12 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,699.99 | ⚪ **CASH** | **+20.2 bps** (±10.8) | `+20.3 bps` | `+0.086 / +0.087` | `0.38%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,337.45 | ⚪ **CASH** | **+13.4 bps** (±17.3) | `+22.1 bps` | `+0.013 / -0.001` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $94.08 | ⚪ **CASH** | **+16.7 bps** (±16.1) | `+11.4 bps` | `+0.052 / +0.192` | `0.50%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 11:31:28 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,695.63 | ⚪ **CASH** | **+20.2 bps** (±10.8) | `+20.3 bps` | `+0.086 / +0.087` | `0.38%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,336.55 | ⚪ **CASH** | **+13.4 bps** (±17.3) | `+22.1 bps` | `+0.013 / -0.001` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $94.01 | ⚪ **CASH** | **+16.7 bps** (±16.1) | `+11.4 bps` | `+0.052 / +0.192` | `0.50%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 11:15:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,609.79 | ⚪ **CASH** | **+20.2 bps** (±10.8) | `+20.3 bps` | `+0.086 / +0.087` | `0.38%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,331.73 | ⚪ **CASH** | **+13.4 bps** (±17.3) | `+22.1 bps` | `+0.013 / -0.001` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.76 | ⚪ **CASH** | **+16.7 bps** (±16.1) | `+11.4 bps` | `+0.052 / +0.192` | `0.50%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 11:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,602.58 | ⚪ **CASH** | **+20.2 bps** (±10.8) | `+20.3 bps` | `+0.086 / +0.087` | `0.38%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,328.71 | ⚪ **CASH** | **+13.4 bps** (±17.3) | `+22.1 bps` | `+0.013 / -0.001` | `0.43%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.57 | ⚪ **CASH** | **+16.7 bps** (±16.1) | `+11.4 bps` | `+0.052 / +0.192` | `0.50%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 10:46:18 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,526.42 | ⚪ **CASH** | **+20.1 bps** (±14.4) | `+18.2 bps` | `+0.091 / +0.114` | `0.38%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,327.27 | ⚪ **CASH** | **+19.4 bps** (±17.4) | `+33.8 bps` | `+0.008 / -0.008` | `0.44%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.46 | ⚪ **CASH** | **+17.4 bps** (±16.0) | `+14.9 bps` | `+0.042 / +0.170` | `0.49%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 10:31:15 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,548.46 | ⚪ **CASH** | **+20.1 bps** (±14.4) | `+18.2 bps` | `+0.091 / +0.114` | `0.38%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,327.70 | ⚪ **CASH** | **+19.4 bps** (±17.4) | `+33.8 bps` | `+0.008 / -0.008` | `0.44%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.54 | ⚪ **CASH** | **+17.4 bps** (±16.0) | `+14.9 bps` | `+0.042 / +0.170` | `0.49%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-04 10:16:26 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,524.54 | ⚪ **CASH** | **+20.1 bps** (±14.4) | `+18.2 bps` | `+0.091 / +0.114` | `0.38%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,327.30 | ⚪ **CASH** | **+19.4 bps** (±17.4) | `+33.8 bps` | `+0.008 / -0.008` | `0.44%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.45 | ⚪ **CASH** | **+17.4 bps** (±16.0) | `+14.9 bps` | `+0.042 / +0.170` | `0.49%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
