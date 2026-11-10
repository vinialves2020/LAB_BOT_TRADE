# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-10 01:30:53 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-10 01:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,074.84 | ⚪ **CASH** | **-30.2 bps** (±10.0) | `-85.5 bps` | `+0.116 / +0.234` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,125.80 | ⚪ **CASH** | **-18.1 bps** (±11.3) | `-24.6 bps` | `-0.132 / +0.015` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.48 | ⚪ **CASH** | **+16.9 bps** (±11.8) | `+8.6 bps` | `+0.093 / +0.143` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 01:15:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,142.01 | ⚪ **CASH** | **-30.2 bps** (±10.0) | `-85.5 bps` | `+0.116 / +0.234` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,128.10 | ⚪ **CASH** | **-18.1 bps** (±11.3) | `-24.6 bps` | `-0.132 / +0.015` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.62 | ⚪ **CASH** | **+16.9 bps** (±11.8) | `+8.6 bps` | `+0.093 / +0.143` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 01:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,159.84 | ⚪ **CASH** | **-30.2 bps** (±10.0) | `-85.5 bps` | `+0.116 / +0.234` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,129.38 | ⚪ **CASH** | **-18.1 bps** (±11.3) | `-24.6 bps` | `-0.132 / +0.015` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.67 | ⚪ **CASH** | **+16.9 bps** (±11.8) | `+8.6 bps` | `+0.093 / +0.143` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 00:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,030.01 | ⚪ **CASH** | **-22.1 bps** (±6.1) | `-69.5 bps` | `+0.106 / +0.226` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,125.96 | ⚪ **CASH** | **-20.9 bps** (±13.0) | `-29.0 bps` | `-0.135 / +0.022` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.45 | ⚪ **CASH** | **+12.6 bps** (±10.2) | `+1.7 bps` | `+0.093 / +0.136` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 00:30:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,093.00 | ⚪ **CASH** | **-22.1 bps** (±6.1) | `-69.5 bps` | `+0.106 / +0.226` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,126.27 | ⚪ **CASH** | **-20.9 bps** (±13.0) | `-29.0 bps` | `-0.135 / +0.022` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.45 | ⚪ **CASH** | **+12.6 bps** (±10.2) | `+1.7 bps` | `+0.093 / +0.136` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 00:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,279.18 | ⚪ **CASH** | **-22.1 bps** (±6.1) | `-69.5 bps` | `+0.106 / +0.226` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,132.84 | ⚪ **CASH** | **-20.9 bps** (±13.0) | `-29.0 bps` | `-0.135 / +0.022` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.63 | ⚪ **CASH** | **+12.6 bps** (±10.2) | `+1.7 bps` | `+0.093 / +0.136` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 00:00:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,370.02 | ⚪ **CASH** | **-22.1 bps** (±6.1) | `-69.5 bps` | `+0.106 / +0.226` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,134.70 | ⚪ **CASH** | **-20.9 bps** (±13.0) | `-29.0 bps` | `-0.135 / +0.022` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.74 | ⚪ **CASH** | **+12.6 bps** (±10.2) | `+1.7 bps` | `+0.093 / +0.136` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 23:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,204.01 | ⚪ **CASH** | **-8.8 bps** (±10.5) | `-40.3 bps` | `+0.100 / +0.176` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,132.38 | ⚪ **CASH** | **-18.2 bps** (±14.7) | `-23.7 bps` | `-0.131 / +0.020` | `0.70%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.57 | ⚪ **CASH** | **+10.1 bps** (±10.3) | `-2.7 bps` | `+0.101 / +0.123` | `0.68%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 23:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,286.00 | ⚪ **CASH** | **-8.8 bps** (±10.5) | `-40.3 bps` | `+0.100 / +0.176` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,134.23 | ⚪ **CASH** | **-18.2 bps** (±14.7) | `-23.7 bps` | `-0.131 / +0.020` | `0.70%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.70 | ⚪ **CASH** | **+10.1 bps** (±10.3) | `-2.7 bps` | `+0.101 / +0.123` | `0.68%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 23:15:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,190.01 | ⚪ **CASH** | **-8.8 bps** (±10.5) | `-40.3 bps` | `+0.100 / +0.176` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,133.90 | ⚪ **CASH** | **-18.2 bps** (±14.7) | `-23.7 bps` | `-0.131 / +0.020` | `0.70%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.69 | ⚪ **CASH** | **+10.1 bps** (±10.3) | `-2.7 bps` | `+0.101 / +0.123` | `0.68%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 23:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,260.01 | ⚪ **CASH** | **-8.8 bps** (±10.5) | `-40.3 bps` | `+0.100 / +0.176` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,135.19 | ⚪ **CASH** | **-18.2 bps** (±14.7) | `-23.7 bps` | `-0.131 / +0.020` | `0.70%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.79 | ⚪ **CASH** | **+10.1 bps** (±10.3) | `-2.7 bps` | `+0.101 / +0.123` | `0.68%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 22:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,270.41 | ⚪ **CASH** | **-11.3 bps** (±9.0) | `-44.3 bps` | `+0.099 / +0.167` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,135.25 | ⚪ **CASH** | **-15.3 bps** (±12.9) | `-19.1 bps` | `-0.112 / -0.004` | `0.71%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.98 | ⚪ **CASH** | **+10.3 bps** (±6.9) | `-3.1 bps` | `+0.094 / +0.137` | `0.69%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 22:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,092.01 | ⚪ **CASH** | **-11.3 bps** (±9.0) | `-44.3 bps` | `+0.099 / +0.167` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,130.04 | ⚪ **CASH** | **-15.3 bps** (±12.9) | `-19.1 bps` | `-0.112 / -0.004` | `0.71%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.63 | ⚪ **CASH** | **+10.3 bps** (±6.9) | `-3.1 bps` | `+0.094 / +0.137` | `0.69%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 22:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,132.26 | ⚪ **CASH** | **-11.3 bps** (±9.0) | `-44.3 bps` | `+0.099 / +0.167` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,130.05 | ⚪ **CASH** | **-15.3 bps** (±12.9) | `-19.1 bps` | `-0.112 / -0.004` | `0.71%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.55 | ⚪ **CASH** | **+10.3 bps** (±6.9) | `-3.1 bps` | `+0.094 / +0.137` | `0.69%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 22:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,024.00 | ⚪ **CASH** | **-11.3 bps** (±9.0) | `-44.3 bps` | `+0.099 / +0.167` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,128.78 | ⚪ **CASH** | **-15.3 bps** (±12.9) | `-19.1 bps` | `-0.112 / -0.004` | `0.71%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.45 | ⚪ **CASH** | **+10.3 bps** (±6.9) | `-3.1 bps` | `+0.094 / +0.137` | `0.69%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 21:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,858.00 | ⚪ **CASH** | **+22.6 bps** (±11.9) | `+20.7 bps` | `+0.062 / +0.206` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,126.65 | ⚪ **CASH** | **-35.1 bps** (±16.6) | `-53.0 bps` | `-0.132 / +0.034` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.31 | ⚪ **CASH** | **+2.7 bps** (±19.1) | `-12.3 bps` | `+0.064 / +0.175` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 21:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,000.00 | ⚪ **CASH** | **+22.6 bps** (±11.9) | `+20.7 bps` | `+0.062 / +0.206` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,134.46 | ⚪ **CASH** | **-35.1 bps** (±16.6) | `-53.0 bps` | `-0.132 / +0.034` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.61 | ⚪ **CASH** | **+2.7 bps** (±19.1) | `-12.3 bps` | `+0.064 / +0.175` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 21:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,896.40 | ⚪ **CASH** | **+22.6 bps** (±11.9) | `+20.7 bps` | `+0.062 / +0.206` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,128.65 | ⚪ **CASH** | **-35.1 bps** (±16.6) | `-53.0 bps` | `-0.132 / +0.034` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.54 | ⚪ **CASH** | **+2.7 bps** (±19.1) | `-12.3 bps` | `+0.064 / +0.175` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 21:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,818.01 | ⚪ **CASH** | **+22.6 bps** (±11.9) | `+20.7 bps` | `+0.062 / +0.206` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,128.22 | ⚪ **CASH** | **-35.1 bps** (±16.6) | `-53.0 bps` | `-0.132 / +0.034` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.57 | ⚪ **CASH** | **+2.7 bps** (±19.1) | `-12.3 bps` | `+0.064 / +0.175` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 20:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,818.14 | ⚪ **CASH** | **+27.0 bps** (±9.2) | `+28.7 bps` | `+0.057 / +0.208` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,128.95 | ⚪ **CASH** | **-33.6 bps** (±16.3) | `-51.2 bps` | `-0.136 / +0.053` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.69 | ⚪ **CASH** | **+3.5 bps** (±19.7) | `-10.0 bps` | `+0.062 / +0.167` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 20:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,788.01 | ⚪ **CASH** | **+27.0 bps** (±9.2) | `+28.7 bps` | `+0.057 / +0.208` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,128.75 | ⚪ **CASH** | **-33.6 bps** (±16.3) | `-51.2 bps` | `-0.136 / +0.053` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.80 | ⚪ **CASH** | **+3.5 bps** (±19.7) | `-10.0 bps` | `+0.062 / +0.167` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 20:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,018.01 | ⚪ **CASH** | **+27.0 bps** (±9.2) | `+28.7 bps` | `+0.057 / +0.208` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,133.96 | ⚪ **CASH** | **-33.6 bps** (±16.3) | `-51.2 bps` | `-0.136 / +0.053` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.01 | ⚪ **CASH** | **+3.5 bps** (±19.7) | `-10.0 bps` | `+0.062 / +0.167` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 20:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,918.01 | ⚪ **CASH** | **+27.0 bps** (±9.2) | `+28.7 bps` | `+0.057 / +0.208` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,129.41 | ⚪ **CASH** | **-33.6 bps** (±16.3) | `-51.2 bps` | `-0.136 / +0.053` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.55 | ⚪ **CASH** | **+3.5 bps** (±19.7) | `-10.0 bps` | `+0.062 / +0.167` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 19:45:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,000.01 | ⚪ **CASH** | **+21.4 bps** (±11.7) | `+21.2 bps` | `+0.051 / +0.188` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,134.68 | ⚪ **CASH** | **-34.9 bps** (±15.9) | `-53.0 bps` | `-0.139 / +0.054` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.80 | ⚪ **CASH** | **+2.6 bps** (±14.7) | `-11.5 bps` | `+0.059 / +0.164` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 19:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,612.67 | ⚪ **CASH** | **+21.4 bps** (±11.7) | `+21.2 bps` | `+0.051 / +0.188` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,121.33 | ⚪ **CASH** | **-34.9 bps** (±15.9) | `-53.0 bps` | `-0.139 / +0.054` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.33 | ⚪ **CASH** | **+2.6 bps** (±14.7) | `-11.5 bps` | `+0.059 / +0.164` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 19:15:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,657.07 | ⚪ **CASH** | **+21.4 bps** (±11.7) | `+21.2 bps` | `+0.051 / +0.188` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,123.02 | ⚪ **CASH** | **-34.9 bps** (±15.9) | `-53.0 bps` | `-0.139 / +0.054` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.51 | ⚪ **CASH** | **+2.6 bps** (±14.7) | `-11.5 bps` | `+0.059 / +0.164` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 19:01:00 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,680.65 | ⚪ **CASH** | **+21.4 bps** (±11.7) | `+21.2 bps` | `+0.051 / +0.188` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,125.60 | ⚪ **CASH** | **-34.9 bps** (±15.9) | `-53.0 bps` | `-0.139 / +0.054` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.59 | ⚪ **CASH** | **+2.6 bps** (±14.7) | `-11.5 bps` | `+0.059 / +0.164` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 18:45:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,605.99 | ⚪ **CASH** | **+22.8 bps** (±10.1) | `+22.2 bps` | `+0.051 / +0.207` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,124.61 | ⚪ **CASH** | **-58.0 bps** (±20.1) | `-94.3 bps` | `-0.140 / +0.057` | `0.75%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.61 | ⚪ **CASH** | **-2.8 bps** (±16.5) | `-21.9 bps` | `+0.062 / +0.172` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 18:30:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,653.20 | ⚪ **CASH** | **+22.8 bps** (±10.1) | `+22.2 bps` | `+0.051 / +0.207` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,125.74 | ⚪ **CASH** | **-58.0 bps** (±20.1) | `-94.3 bps` | `-0.140 / +0.057` | `0.75%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.57 | ⚪ **CASH** | **-2.8 bps** (±16.5) | `-21.9 bps` | `+0.062 / +0.172` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 18:01:06 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,736.90 | ⚪ **CASH** | **+22.8 bps** (±10.1) | `+22.2 bps` | `+0.051 / +0.207` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,124.39 | ⚪ **CASH** | **-58.0 bps** (±20.1) | `-94.3 bps` | `-0.140 / +0.057` | `0.75%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.61 | ⚪ **CASH** | **-2.8 bps** (±16.5) | `-21.9 bps` | `+0.062 / +0.172` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 17:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,691.63 | ⚪ **CASH** | **+23.5 bps** (±9.4) | `+22.1 bps` | `+0.050 / +0.227` | `0.47%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,121.84 | ⚪ **CASH** | **-31.0 bps** (±14.4) | `-47.5 bps` | `-0.143 / +0.080` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.48 | ⚪ **CASH** | **+11.3 bps** (±23.4) | `+3.8 bps` | `+0.064 / +0.188` | `0.73%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 17:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,818.00 | ⚪ **CASH** | **+23.5 bps** (±9.4) | `+22.1 bps` | `+0.050 / +0.227` | `0.47%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,125.14 | ⚪ **CASH** | **-31.0 bps** (±14.4) | `-47.5 bps` | `-0.143 / +0.080` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.41 | ⚪ **CASH** | **+11.3 bps** (±23.4) | `+3.8 bps` | `+0.064 / +0.188` | `0.73%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 17:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,932.01 | ⚪ **CASH** | **+23.5 bps** (±9.4) | `+22.1 bps` | `+0.050 / +0.227` | `0.47%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,128.44 | ⚪ **CASH** | **-31.0 bps** (±14.4) | `-47.5 bps` | `-0.143 / +0.080` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.93 | ⚪ **CASH** | **+11.3 bps** (±23.4) | `+3.8 bps` | `+0.064 / +0.188` | `0.73%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 17:01:02 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,036.00 | ⚪ **CASH** | **+23.5 bps** (±9.4) | `+22.1 bps` | `+0.050 / +0.227` | `0.47%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,132.39 | ⚪ **CASH** | **-31.0 bps** (±14.4) | `-47.5 bps` | `-0.143 / +0.080` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.97 | ⚪ **CASH** | **+11.3 bps** (±23.4) | `+3.8 bps` | `+0.064 / +0.188` | `0.73%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 16:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,870.92 | ⚪ **CASH** | **+24.1 bps** (±12.8) | `+25.6 bps` | `+0.041 / +0.222` | `0.46%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,128.92 | ⚪ **CASH** | **-27.3 bps** (±14.1) | `-38.9 bps` | `-0.146 / +0.064` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.81 | ⚪ **CASH** | **+22.7 bps** (±15.6) | `+25.6 bps` | `+0.054 / +0.168` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 16:30:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,874.01 | ⚪ **CASH** | **+24.1 bps** (±12.8) | `+25.6 bps` | `+0.041 / +0.222` | `0.46%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,128.94 | ⚪ **CASH** | **-27.3 bps** (±14.1) | `-38.9 bps` | `-0.146 / +0.064` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.71 | ⚪ **CASH** | **+22.7 bps** (±15.6) | `+25.6 bps` | `+0.054 / +0.168` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
