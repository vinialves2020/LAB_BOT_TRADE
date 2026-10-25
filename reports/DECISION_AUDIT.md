# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-25 19:02:13 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-25 19:02:13 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,666.20 | ⚪ **CASH** | **-0.3 bps** (±3.7) | `+3.8 bps` | `-0.017 / -0.017` | `0.25%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,354.37 | ⚪ **CASH** | **+19.9 bps** (±3.8) | `+25.4 bps` | `+0.053 / +0.108` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.78 | ⚪ **CASH** | **+2.9 bps** (±11.4) | `-2.2 bps` | `+0.062 / +0.066` | `0.42%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 18:47:20 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,683.56 | ⚪ **CASH** | **+3.6 bps** (±4.6) | `+7.5 bps` | `-0.005 / +0.010` | `0.25%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,356.83 | ⚪ **CASH** | **+20.6 bps** (±7.0) | `+24.3 bps` | `+0.075 / +0.110` | `0.43%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.94 | ⚪ **CASH** | **+4.0 bps** (±15.9) | `-0.9 bps` | `+0.073 / +0.064` | `0.42%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 18:32:12 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,678.53 | ⚪ **CASH** | **+3.6 bps** (±4.6) | `+7.5 bps` | `-0.005 / +0.010` | `0.25%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,355.76 | ⚪ **CASH** | **+20.6 bps** (±7.0) | `+24.3 bps` | `+0.075 / +0.110` | `0.43%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.89 | ⚪ **CASH** | **+4.0 bps** (±15.9) | `-0.9 bps` | `+0.073 / +0.064` | `0.42%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 18:16:57 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,710.92 | ⚪ **CASH** | **+3.6 bps** (±4.6) | `+7.5 bps` | `-0.005 / +0.010` | `0.25%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,355.30 | ⚪ **CASH** | **+20.6 bps** (±7.0) | `+24.3 bps` | `+0.075 / +0.110` | `0.43%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.79 | ⚪ **CASH** | **+4.0 bps** (±15.9) | `-0.9 bps` | `+0.073 / +0.064` | `0.42%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 18:02:15 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,818.77 | ⚪ **CASH** | **+3.6 bps** (±4.6) | `+7.5 bps` | `-0.005 / +0.010` | `0.25%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,359.15 | ⚪ **CASH** | **+20.6 bps** (±7.0) | `+24.3 bps` | `+0.075 / +0.110` | `0.43%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.97 | ⚪ **CASH** | **+4.0 bps** (±15.9) | `-0.9 bps` | `+0.073 / +0.064` | `0.42%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 17:47:01 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,795.62 | ⚪ **CASH** | **-0.7 bps** (±2.6) | `-0.7 bps` | `-0.022 / +0.049` | `0.25%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,357.75 | ⚪ **CASH** | **+23.7 bps** (±4.0) | `+31.5 bps` | `+0.064 / +0.109` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.93 | ⚪ **CASH** | **+6.9 bps** (±13.2) | `+2.5 bps` | `+0.078 / +0.090` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 17:32:17 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,755.26 | ⚪ **CASH** | **-0.7 bps** (±2.6) | `-0.7 bps` | `-0.022 / +0.049` | `0.25%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,358.89 | ⚪ **CASH** | **+23.7 bps** (±4.0) | `+31.5 bps` | `+0.064 / +0.109` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.91 | ⚪ **CASH** | **+6.9 bps** (±13.2) | `+2.5 bps` | `+0.078 / +0.090` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 17:17:03 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,812.69 | ⚪ **CASH** | **-0.7 bps** (±2.6) | `-0.7 bps` | `-0.022 / +0.049` | `0.25%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,355.75 | ⚪ **CASH** | **+23.7 bps** (±4.0) | `+31.5 bps` | `+0.064 / +0.109` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.85 | ⚪ **CASH** | **+6.9 bps** (±13.2) | `+2.5 bps` | `+0.078 / +0.090` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 17:02:18 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,796.01 | ⚪ **CASH** | **-0.7 bps** (±2.6) | `-0.7 bps` | `-0.022 / +0.049` | `0.25%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,355.00 | ⚪ **CASH** | **+23.7 bps** (±4.0) | `+31.5 bps` | `+0.064 / +0.109` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.90 | ⚪ **CASH** | **+6.9 bps** (±13.2) | `+2.5 bps` | `+0.078 / +0.090` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 16:47:11 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,625.75 | ⚪ **CASH** | **+3.6 bps** (±5.7) | `+4.1 bps` | `-0.009 / +0.073` | `0.26%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,345.24 | ⚪ **CASH** | **+15.5 bps** (±5.9) | `+17.3 bps` | `+0.077 / +0.073` | `0.43%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.43 | ⚪ **CASH** | **+0.7 bps** (±10.3) | `-8.5 bps` | `+0.074 / +0.074` | `0.43%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 16:32:14 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,631.24 | ⚪ **CASH** | **+3.6 bps** (±5.7) | `+4.1 bps` | `-0.009 / +0.073` | `0.26%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,346.88 | ⚪ **CASH** | **+15.5 bps** (±5.9) | `+17.3 bps` | `+0.077 / +0.073` | `0.43%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.54 | ⚪ **CASH** | **+0.7 bps** (±10.3) | `-8.5 bps` | `+0.074 / +0.074` | `0.43%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 16:17:04 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,604.06 | ⚪ **CASH** | **+3.6 bps** (±5.7) | `+4.1 bps` | `-0.009 / +0.073` | `0.26%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,346.97 | ⚪ **CASH** | **+15.5 bps** (±5.9) | `+17.3 bps` | `+0.077 / +0.073` | `0.43%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.48 | ⚪ **CASH** | **+0.7 bps** (±10.3) | `-8.5 bps` | `+0.074 / +0.074` | `0.43%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 16:02:08 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,605.00 | ⚪ **CASH** | **+3.6 bps** (±5.7) | `+4.1 bps` | `-0.009 / +0.073` | `0.26%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,342.37 | ⚪ **CASH** | **+15.5 bps** (±5.9) | `+17.3 bps` | `+0.077 / +0.073` | `0.43%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.53 | ⚪ **CASH** | **+0.7 bps** (±10.3) | `-8.5 bps` | `+0.074 / +0.074` | `0.43%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 15:47:09 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,667.28 | ⚪ **CASH** | **-4.9 bps** (±2.9) | `-1.4 bps` | `-0.074 / +0.060` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,345.35 | ⚪ **CASH** | **+4.6 bps** (±6.7) | `+16.0 bps` | `-0.019 / -0.015` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.60 | ⚪ **CASH** | **-4.0 bps** (±6.2) | `-7.8 bps` | `+0.011 / +0.066` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 15:32:10 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,640.01 | ⚪ **CASH** | **-4.9 bps** (±2.9) | `-1.4 bps` | `-0.074 / +0.060` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,341.99 | ⚪ **CASH** | **+4.6 bps** (±6.7) | `+16.0 bps` | `-0.019 / -0.015` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.54 | ⚪ **CASH** | **-4.0 bps** (±6.2) | `-7.8 bps` | `+0.011 / +0.066` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 15:17:04 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,664.01 | ⚪ **CASH** | **-4.9 bps** (±2.9) | `-1.4 bps` | `-0.074 / +0.060` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,342.49 | ⚪ **CASH** | **+4.6 bps** (±6.7) | `+16.0 bps` | `-0.019 / -0.015` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.53 | ⚪ **CASH** | **-4.0 bps** (±6.2) | `-7.8 bps` | `+0.011 / +0.066` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 15:02:10 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,734.01 | ⚪ **CASH** | **-4.9 bps** (±2.9) | `-1.4 bps` | `-0.074 / +0.060` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,344.10 | ⚪ **CASH** | **+4.6 bps** (±6.7) | `+16.0 bps` | `-0.019 / -0.015` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.53 | ⚪ **CASH** | **-4.0 bps** (±6.2) | `-7.8 bps` | `+0.011 / +0.066` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 14:46:56 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,398.00 | ⚪ **CASH** | **-13.2 bps** (±5.2) | `-4.6 bps` | `-0.127 / +0.002` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,334.95 | ⚪ **CASH** | **-0.7 bps** (±5.2) | `+14.5 bps` | `-0.042 / -0.067` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.95 | ⚪ **CASH** | **-6.0 bps** (±11.6) | `-1.0 bps` | `-0.041 / +0.038` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 14:32:19 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,354.03 | ⚪ **CASH** | **-13.2 bps** (±5.2) | `-4.6 bps` | `-0.127 / +0.002` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,332.47 | ⚪ **CASH** | **-0.7 bps** (±5.2) | `+14.5 bps` | `-0.042 / -0.067` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.77 | ⚪ **CASH** | **-6.0 bps** (±11.6) | `-1.0 bps` | `-0.041 / +0.038` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 14:16:57 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,364.25 | ⚪ **CASH** | **-13.2 bps** (±5.2) | `-4.6 bps` | `-0.127 / +0.002` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,333.89 | ⚪ **CASH** | **-0.7 bps** (±5.2) | `+14.5 bps` | `-0.042 / -0.067` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.87 | ⚪ **CASH** | **-6.0 bps** (±11.6) | `-1.0 bps` | `-0.041 / +0.038` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 14:02:27 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,376.70 | ⚪ **CASH** | **-13.2 bps** (±5.2) | `-4.6 bps` | `-0.127 / +0.002` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,334.52 | ⚪ **CASH** | **-0.7 bps** (±5.2) | `+14.5 bps` | `-0.042 / -0.067` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.73 | ⚪ **CASH** | **-6.0 bps** (±11.6) | `-1.0 bps` | `-0.041 / +0.038` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 13:47:06 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,394.73 | ⚪ **CASH** | **-12.7 bps** (±5.6) | `-4.2 bps` | `-0.125 / +0.008` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,336.59 | ⚪ **CASH** | **-0.1 bps** (±5.0) | `+14.3 bps` | `-0.046 / -0.046` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.07 | ⚪ **CASH** | **-4.9 bps** (±9.1) | `-6.1 bps` | `-0.034 / +0.128` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 13:32:18 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,290.33 | ⚪ **CASH** | **-12.7 bps** (±5.6) | `-4.2 bps` | `-0.125 / +0.008` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,329.14 | ⚪ **CASH** | **-0.1 bps** (±5.0) | `+14.3 bps` | `-0.046 / -0.046` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.93 | ⚪ **CASH** | **-4.9 bps** (±9.1) | `-6.1 bps` | `-0.034 / +0.128` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 13:17:08 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,420.52 | ⚪ **CASH** | **-12.7 bps** (±5.6) | `-4.2 bps` | `-0.125 / +0.008` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,335.53 | ⚪ **CASH** | **-0.1 bps** (±5.0) | `+14.3 bps` | `-0.046 / -0.046` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.07 | ⚪ **CASH** | **-4.9 bps** (±9.1) | `-6.1 bps` | `-0.034 / +0.128` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 13:02:08 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,454.01 | ⚪ **CASH** | **-12.7 bps** (±5.6) | `-4.2 bps` | `-0.125 / +0.008` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,335.60 | ⚪ **CASH** | **-0.1 bps** (±5.0) | `+14.3 bps` | `-0.046 / -0.046` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.97 | ⚪ **CASH** | **-4.9 bps** (±9.1) | `-6.1 bps` | `-0.034 / +0.128` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 12:47:00 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,427.60 | ⚪ **CASH** | **-14.3 bps** (±4.5) | `-5.2 bps` | `-0.120 / -0.035` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,332.86 | ⚪ **CASH** | **+0.9 bps** (±6.7) | `+17.1 bps` | `-0.042 / -0.066` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.87 | ⚪ **CASH** | **-7.1 bps** (±8.5) | `-8.4 bps` | `-0.039 / +0.105` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 12:32:25 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,354.67 | ⚪ **CASH** | **-14.3 bps** (±4.5) | `-5.2 bps` | `-0.120 / -0.035` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,328.69 | ⚪ **CASH** | **+0.9 bps** (±6.7) | `+17.1 bps` | `-0.042 / -0.066` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.75 | ⚪ **CASH** | **-7.1 bps** (±8.5) | `-8.4 bps` | `-0.039 / +0.105` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 12:17:22 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,466.34 | ⚪ **CASH** | **-14.3 bps** (±4.5) | `-5.2 bps` | `-0.120 / -0.035` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,334.51 | ⚪ **CASH** | **+0.9 bps** (±6.7) | `+17.1 bps` | `-0.042 / -0.066` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.95 | ⚪ **CASH** | **-7.1 bps** (±8.5) | `-8.4 bps` | `-0.039 / +0.105` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 12:02:20 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,566.18 | ⚪ **CASH** | **-14.3 bps** (±4.5) | `-5.2 bps` | `-0.120 / -0.035` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,339.24 | ⚪ **CASH** | **+0.9 bps** (±6.7) | `+17.1 bps` | `-0.042 / -0.066` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.25 | ⚪ **CASH** | **-7.1 bps** (±8.5) | `-8.4 bps` | `-0.039 / +0.105` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 11:47:12 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,532.01 | ⚪ **CASH** | **-14.9 bps** (±6.1) | `-0.2 bps` | `-0.127 / -0.107` | `0.26%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,337.27 | ⚪ **CASH** | **-6.2 bps** (±6.5) | `+8.5 bps` | `-0.047 / -0.119` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.08 | ⚪ **CASH** | **-7.1 bps** (±7.2) | `-2.6 bps` | `-0.049 / +0.031` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 11:32:10 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,397.17 | ⚪ **CASH** | **-14.9 bps** (±6.1) | `-0.2 bps` | `-0.127 / -0.107` | `0.26%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,330.55 | ⚪ **CASH** | **-6.2 bps** (±6.5) | `+8.5 bps` | `-0.047 / -0.119` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.77 | ⚪ **CASH** | **-7.1 bps** (±7.2) | `-2.6 bps` | `-0.049 / +0.031` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 11:17:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,384.85 | ⚪ **CASH** | **-14.9 bps** (±6.1) | `-0.2 bps` | `-0.127 / -0.107` | `0.26%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,331.73 | ⚪ **CASH** | **-6.2 bps** (±6.5) | `+8.5 bps` | `-0.047 / -0.119` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.83 | ⚪ **CASH** | **-7.1 bps** (±7.2) | `-2.6 bps` | `-0.049 / +0.031` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 11:02:23 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,396.67 | ⚪ **CASH** | **-14.9 bps** (±6.1) | `-0.2 bps` | `-0.127 / -0.107` | `0.26%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,332.70 | ⚪ **CASH** | **-6.2 bps** (±6.5) | `+8.5 bps` | `-0.047 / -0.119` | `0.44%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.92 | ⚪ **CASH** | **-7.1 bps** (±7.2) | `-2.6 bps` | `-0.049 / +0.031` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 10:47:32 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,225.41 | ⚪ **CASH** | **-17.0 bps** (±6.3) | `-3.0 bps` | `-0.127 / -0.122` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,323.69 | ⚪ **CASH** | **-3.8 bps** (±4.9) | `+12.1 bps` | `-0.046 / -0.112` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.65 | ⚪ **CASH** | **-9.3 bps** (±7.6) | `-6.7 bps` | `-0.048 / +0.031` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 10:32:06 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,325.27 | ⚪ **CASH** | **-17.0 bps** (±6.3) | `-3.0 bps` | `-0.127 / -0.122` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,326.74 | ⚪ **CASH** | **-3.8 bps** (±4.9) | `+12.1 bps` | `-0.046 / -0.112` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.75 | ⚪ **CASH** | **-9.3 bps** (±7.6) | `-6.7 bps` | `-0.048 / +0.031` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-25 10:16:57 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,395.90 | ⚪ **CASH** | **-17.0 bps** (±6.3) | `-3.0 bps` | `-0.127 / -0.122` | `0.26%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,329.63 | ⚪ **CASH** | **-3.8 bps** (±4.9) | `+12.1 bps` | `-0.046 / -0.112` | `0.45%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.82 | ⚪ **CASH** | **-9.3 bps** (±7.6) | `-6.7 bps` | `-0.048 / +0.031` | `0.43%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
