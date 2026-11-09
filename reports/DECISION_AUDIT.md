# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-09 22:00:55 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-11-09 16:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,179.75 | ⚪ **CASH** | **+24.1 bps** (±12.8) | `+25.6 bps` | `+0.041 / +0.222` | `0.46%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,137.74 | ⚪ **CASH** | **-27.3 bps** (±14.1) | `-38.9 bps` | `-0.146 / +0.064` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.33 | ⚪ **CASH** | **+22.7 bps** (±15.6) | `+25.6 bps` | `+0.054 / +0.168` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 16:00:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,509.26 | ⚪ **CASH** | **+24.1 bps** (±12.8) | `+25.6 bps` | `+0.041 / +0.222` | `0.46%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,146.43 | ⚪ **CASH** | **-27.3 bps** (±14.1) | `-38.9 bps` | `-0.146 / +0.064` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.87 | ⚪ **CASH** | **+22.7 bps** (±15.6) | `+25.6 bps` | `+0.054 / +0.168` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 15:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,467.23 | ⚪ **CASH** | **+12.6 bps** (±12.4) | `+13.1 bps` | `+0.020 / +0.138` | `0.44%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,144.25 | ⚪ **CASH** | **-69.8 bps** (±15.5) | `-108.1 bps` | `-0.158 / -0.022` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.83 | ⚪ **CASH** | **-6.2 bps** (±12.1) | `-19.6 bps` | `+0.043 / +0.082` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 15:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,217.61 | ⚪ **CASH** | **+12.6 bps** (±12.4) | `+13.1 bps` | `+0.020 / +0.138` | `0.44%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,134.38 | ⚪ **CASH** | **-69.8 bps** (±15.5) | `-108.1 bps` | `-0.158 / -0.022` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.52 | ⚪ **CASH** | **-6.2 bps** (±12.1) | `-19.6 bps` | `+0.043 / +0.082` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 15:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,854.01 | ⚪ **CASH** | **+12.6 bps** (±12.4) | `+13.1 bps` | `+0.020 / +0.138` | `0.44%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,126.40 | ⚪ **CASH** | **-69.8 bps** (±15.5) | `-108.1 bps` | `-0.158 / -0.022` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.36 | ⚪ **CASH** | **-6.2 bps** (±12.1) | `-19.6 bps` | `+0.043 / +0.082` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 15:01:02 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,710.00 | ⚪ **CASH** | **+12.6 bps** (±12.4) | `+13.1 bps` | `+0.020 / +0.138` | `0.44%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,123.37 | ⚪ **CASH** | **-69.8 bps** (±15.5) | `-108.1 bps` | `-0.158 / -0.022` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.05 | ⚪ **CASH** | **-6.2 bps** (±12.1) | `-19.6 bps` | `+0.043 / +0.082` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 14:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,648.55 | ⚪ **CASH** | **+16.7 bps** (±10.1) | `+18.6 bps` | `+0.013 / +0.180` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,124.48 | ⚪ **CASH** | **-60.5 bps** (±14.8) | `-87.3 bps` | `-0.165 / -0.068` | `0.76%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $87.30 | ⚪ **CASH** | **-10.3 bps** (±16.8) | `-27.3 bps` | `+0.041 / +0.107` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 14:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,596.21 | ⚪ **CASH** | **+16.7 bps** (±10.1) | `+18.6 bps` | `+0.013 / +0.180` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,119.32 | ⚪ **CASH** | **-60.5 bps** (±14.8) | `-87.3 bps` | `-0.165 / -0.068` | `0.76%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.96 | ⚪ **CASH** | **-10.3 bps** (±16.8) | `-27.3 bps` | `+0.041 / +0.107` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 14:15:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,584.01 | ⚪ **CASH** | **+16.7 bps** (±10.1) | `+18.6 bps` | `+0.013 / +0.180` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,121.10 | ⚪ **CASH** | **-60.5 bps** (±14.8) | `-87.3 bps` | `-0.165 / -0.068` | `0.76%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.86 | ⚪ **CASH** | **-10.3 bps** (±16.8) | `-27.3 bps` | `+0.041 / +0.107` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 14:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,720.01 | ⚪ **CASH** | **+16.7 bps** (±10.1) | `+18.6 bps` | `+0.013 / +0.180` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,125.80 | ⚪ **CASH** | **-60.5 bps** (±14.8) | `-87.3 bps` | `-0.165 / -0.068` | `0.76%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.83 | ⚪ **CASH** | **-10.3 bps** (±16.8) | `-27.3 bps` | `+0.041 / +0.107` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 13:45:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,650.00 | ⚪ **CASH** | **+12.7 bps** (±9.4) | `+13.3 bps` | `+0.015 / +0.142` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,118.17 | ⚪ **CASH** | **-57.3 bps** (±18.1) | `-76.2 bps` | `-0.164 / -0.142` | `0.77%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.43 | ⚪ **CASH** | **-12.5 bps** (±18.9) | `-29.0 bps` | `+0.040 / +0.078` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 13:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,812.00 | ⚪ **CASH** | **+12.7 bps** (±9.4) | `+13.3 bps` | `+0.015 / +0.142` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,121.99 | ⚪ **CASH** | **-57.3 bps** (±18.1) | `-76.2 bps` | `-0.164 / -0.142` | `0.77%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.64 | ⚪ **CASH** | **-12.5 bps** (±18.9) | `-29.0 bps` | `+0.040 / +0.078` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 13:15:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,725.56 | ⚪ **CASH** | **+12.7 bps** (±9.4) | `+13.3 bps` | `+0.015 / +0.142` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,121.23 | ⚪ **CASH** | **-57.3 bps** (±18.1) | `-76.2 bps` | `-0.164 / -0.142` | `0.77%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.56 | ⚪ **CASH** | **-12.5 bps** (±18.9) | `-29.0 bps` | `+0.040 / +0.078` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-09 13:00:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,922.01 | ⚪ **CASH** | **+12.7 bps** (±9.4) | `+13.3 bps` | `+0.015 / +0.142` | `0.45%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,123.26 | ⚪ **CASH** | **-57.3 bps** (±18.1) | `-76.2 bps` | `-0.164 / -0.142` | `0.77%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $86.60 | ⚪ **CASH** | **-12.5 bps** (±18.9) | `-29.0 bps` | `+0.040 / +0.078` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
