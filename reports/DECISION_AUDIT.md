# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-07 14:30:39 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-07 14:30:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,937.68 | ⚪ **CASH** | **+11.1 bps** (±4.6) | `+22.4 bps` | `+0.019 / -0.062` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,245.39 | ⚪ **CASH** | **+0.1 bps** (±3.4) | `+12.2 bps` | `-0.025 / -0.150` | `0.55%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.95 | ⚪ **CASH** | **-12.7 bps** (±12.9) | `-12.4 bps` | `-0.040 / -0.082` | `0.57%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 14:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,945.79 | ⚪ **CASH** | **+11.1 bps** (±4.6) | `+22.4 bps` | `+0.019 / -0.062` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,246.22 | ⚪ **CASH** | **+0.1 bps** (±3.4) | `+12.2 bps` | `-0.025 / -0.150` | `0.55%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.99 | ⚪ **CASH** | **-12.7 bps** (±12.9) | `-12.4 bps` | `-0.040 / -0.082` | `0.57%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 14:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,936.30 | ⚪ **CASH** | **+11.1 bps** (±4.6) | `+22.4 bps` | `+0.019 / -0.062` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,245.83 | ⚪ **CASH** | **+0.1 bps** (±3.4) | `+12.2 bps` | `-0.025 / -0.150` | `0.55%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.99 | ⚪ **CASH** | **-12.7 bps** (±12.9) | `-12.4 bps` | `-0.040 / -0.082` | `0.57%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 13:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,970.54 | ⚪ **CASH** | **+15.2 bps** (±3.7) | `+23.5 bps` | `+0.019 / +0.030` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,246.77 | ⚪ **CASH** | **+0.0 bps** (±3.7) | `+12.5 bps` | `-0.023 / -0.159` | `0.56%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.08 | ⚪ **CASH** | **-14.9 bps** (±9.4) | `-13.8 bps` | `-0.062 / -0.100` | `0.57%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 13:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,913.98 | ⚪ **CASH** | **+15.2 bps** (±3.7) | `+23.5 bps` | `+0.019 / +0.030` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,243.98 | ⚪ **CASH** | **+0.0 bps** (±3.7) | `+12.5 bps` | `-0.023 / -0.159` | `0.56%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.98 | ⚪ **CASH** | **-14.9 bps** (±9.4) | `-13.8 bps` | `-0.062 / -0.100` | `0.57%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 13:15:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,844.00 | ⚪ **CASH** | **+15.2 bps** (±3.7) | `+23.5 bps` | `+0.019 / +0.030` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,240.09 | ⚪ **CASH** | **+0.0 bps** (±3.7) | `+12.5 bps` | `-0.023 / -0.159` | `0.56%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.75 | ⚪ **CASH** | **-14.9 bps** (±9.4) | `-13.8 bps` | `-0.062 / -0.100` | `0.57%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 13:00:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,906.19 | ⚪ **CASH** | **+15.2 bps** (±3.7) | `+23.5 bps` | `+0.019 / +0.030` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,241.82 | ⚪ **CASH** | **+0.0 bps** (±3.7) | `+12.5 bps` | `-0.023 / -0.159` | `0.56%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.79 | ⚪ **CASH** | **-14.9 bps** (±9.4) | `-13.8 bps` | `-0.062 / -0.100` | `0.57%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 12:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,829.00 | ⚪ **CASH** | **+10.2 bps** (±4.7) | `+11.0 bps` | `+0.023 / +0.075` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,239.82 | ⚪ **CASH** | **-10.0 bps** (±6.7) | `-2.6 bps` | `-0.032 / -0.191` | `0.56%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.72 | ⚪ **CASH** | **-25.7 bps** (±14.2) | `-40.6 bps` | `-0.056 / +0.010` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 12:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,007.07 | ⚪ **CASH** | **+10.2 bps** (±4.7) | `+11.0 bps` | `+0.023 / +0.075` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,244.13 | ⚪ **CASH** | **-10.0 bps** (±6.7) | `-2.6 bps` | `-0.032 / -0.191` | `0.56%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.98 | ⚪ **CASH** | **-25.7 bps** (±14.2) | `-40.6 bps` | `-0.056 / +0.010` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 12:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,009.16 | ⚪ **CASH** | **+10.2 bps** (±4.7) | `+11.0 bps` | `+0.023 / +0.075` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,244.09 | ⚪ **CASH** | **-10.0 bps** (±6.7) | `-2.6 bps` | `-0.032 / -0.191` | `0.56%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.94 | ⚪ **CASH** | **-25.7 bps** (±14.2) | `-40.6 bps` | `-0.056 / +0.010` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 12:00:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,993.76 | ⚪ **CASH** | **+10.2 bps** (±4.7) | `+11.0 bps` | `+0.023 / +0.075` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,245.37 | ⚪ **CASH** | **-10.0 bps** (±6.7) | `-2.6 bps` | `-0.032 / -0.191` | `0.56%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.00 | ⚪ **CASH** | **-25.7 bps** (±14.2) | `-40.6 bps` | `-0.056 / +0.010` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 11:45:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,020.99 | ⚪ **CASH** | **+9.4 bps** (±2.2) | `+7.7 bps` | `+0.022 / +0.099` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,246.37 | ⚪ **CASH** | **-7.2 bps** (±5.0) | `-4.3 bps` | `-0.033 / -0.088` | `0.57%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.05 | ⚪ **CASH** | **-29.9 bps** (±17.6) | `-46.6 bps` | `-0.055 / -0.002` | `0.59%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 11:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,975.28 | ⚪ **CASH** | **+9.4 bps** (±2.2) | `+7.7 bps` | `+0.022 / +0.099` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,244.92 | ⚪ **CASH** | **-7.2 bps** (±5.0) | `-4.3 bps` | `-0.033 / -0.088` | `0.57%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.92 | ⚪ **CASH** | **-29.9 bps** (±17.6) | `-46.6 bps` | `-0.055 / -0.002` | `0.59%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 11:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,986.20 | ⚪ **CASH** | **+9.4 bps** (±2.2) | `+7.7 bps` | `+0.022 / +0.099` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,246.09 | ⚪ **CASH** | **-7.2 bps** (±5.0) | `-4.3 bps` | `-0.033 / -0.088` | `0.57%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.95 | ⚪ **CASH** | **-29.9 bps** (±17.6) | `-46.6 bps` | `-0.055 / -0.002` | `0.59%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 11:00:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,988.93 | ⚪ **CASH** | **+9.4 bps** (±2.2) | `+7.7 bps` | `+0.022 / +0.099` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,247.19 | ⚪ **CASH** | **-7.2 bps** (±5.0) | `-4.3 bps` | `-0.033 / -0.088` | `0.57%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.99 | ⚪ **CASH** | **-29.9 bps** (±17.6) | `-46.6 bps` | `-0.055 / -0.002` | `0.59%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 10:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,977.59 | ⚪ **CASH** | **+9.1 bps** (±2.3) | `+4.4 bps` | `+0.025 / +0.136` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,245.53 | ⚪ **CASH** | **-3.6 bps** (±5.9) | `-5.3 bps` | `-0.018 / +0.005` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.91 | ⚪ **CASH** | **-34.0 bps** (±19.4) | `-53.0 bps` | `-0.051 / -0.024` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 10:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,950.35 | ⚪ **CASH** | **+9.1 bps** (±2.3) | `+4.4 bps` | `+0.025 / +0.136` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,242.17 | ⚪ **CASH** | **-3.6 bps** (±5.9) | `-5.3 bps` | `-0.018 / +0.005` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.70 | ⚪ **CASH** | **-34.0 bps** (±19.4) | `-53.0 bps` | `-0.051 / -0.024` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 10:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,045.82 | ⚪ **CASH** | **+9.1 bps** (±2.3) | `+4.4 bps` | `+0.025 / +0.136` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,248.31 | ⚪ **CASH** | **-3.6 bps** (±5.9) | `-5.3 bps` | `-0.018 / +0.005` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.11 | ⚪ **CASH** | **-34.0 bps** (±19.4) | `-53.0 bps` | `-0.051 / -0.024` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 10:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,053.49 | ⚪ **CASH** | **+9.1 bps** (±2.3) | `+4.4 bps` | `+0.025 / +0.136` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,245.50 | ⚪ **CASH** | **-3.6 bps** (±5.9) | `-5.3 bps` | `-0.018 / +0.005` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.09 | ⚪ **CASH** | **-34.0 bps** (±19.4) | `-53.0 bps` | `-0.051 / -0.024` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 09:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,102.00 | ⚪ **CASH** | **+6.7 bps** (±2.1) | `+4.3 bps` | `+0.030 / +0.056` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,246.80 | ⚪ **CASH** | **+1.0 bps** (±3.6) | `+1.0 bps` | `-0.008 / +0.011` | `0.59%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.11 | ⚪ **CASH** | **-36.5 bps** (±16.2) | `-48.8 bps` | `-0.041 / -0.184` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 09:30:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,108.01 | ⚪ **CASH** | **+6.7 bps** (±2.1) | `+4.3 bps` | `+0.030 / +0.056` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,247.39 | ⚪ **CASH** | **+1.0 bps** (±3.6) | `+1.0 bps` | `-0.008 / +0.011` | `0.59%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.14 | ⚪ **CASH** | **-36.5 bps** (±16.2) | `-48.8 bps` | `-0.041 / -0.184` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 09:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,186.00 | ⚪ **CASH** | **+6.7 bps** (±2.1) | `+4.3 bps` | `+0.030 / +0.056` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,248.43 | ⚪ **CASH** | **+1.0 bps** (±3.6) | `+1.0 bps` | `-0.008 / +0.011` | `0.59%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.19 | ⚪ **CASH** | **-36.5 bps** (±16.2) | `-48.8 bps` | `-0.041 / -0.184` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 09:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,244.87 | ⚪ **CASH** | **+6.7 bps** (±2.1) | `+4.3 bps` | `+0.030 / +0.056` | `0.44%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,251.12 | ⚪ **CASH** | **+1.0 bps** (±3.6) | `+1.0 bps` | `-0.008 / +0.011` | `0.59%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.32 | ⚪ **CASH** | **-36.5 bps** (±16.2) | `-48.8 bps` | `-0.041 / -0.184` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 08:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,138.63 | ⚪ **CASH** | **+6.4 bps** (±1.4) | `+3.5 bps` | `+0.055 / +0.006` | `0.45%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,248.85 | ⚪ **CASH** | **+3.2 bps** (±5.5) | `+3.5 bps` | `+0.026 / -0.028` | `0.60%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.34 | ⚪ **CASH** | **-34.6 bps** (±15.0) | `-46.8 bps` | `-0.032 / -0.198` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 08:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,120.75 | ⚪ **CASH** | **+6.4 bps** (±1.4) | `+3.5 bps` | `+0.055 / +0.006` | `0.45%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,248.02 | ⚪ **CASH** | **+3.2 bps** (±5.5) | `+3.5 bps` | `+0.026 / -0.028` | `0.60%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.22 | ⚪ **CASH** | **-34.6 bps** (±15.0) | `-46.8 bps` | `-0.032 / -0.198` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 08:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,119.91 | ⚪ **CASH** | **+6.4 bps** (±1.4) | `+3.5 bps` | `+0.055 / +0.006` | `0.45%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,247.64 | ⚪ **CASH** | **+3.2 bps** (±5.5) | `+3.5 bps` | `+0.026 / -0.028` | `0.60%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.23 | ⚪ **CASH** | **-34.6 bps** (±15.0) | `-46.8 bps` | `-0.032 / -0.198` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 08:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,116.33 | ⚪ **CASH** | **+6.4 bps** (±1.4) | `+3.5 bps` | `+0.055 / +0.006` | `0.45%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,246.47 | ⚪ **CASH** | **+3.2 bps** (±5.5) | `+3.5 bps` | `+0.026 / -0.028` | `0.60%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.24 | ⚪ **CASH** | **-34.6 bps** (±15.0) | `-46.8 bps` | `-0.032 / -0.198` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 07:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,039.47 | ⚪ **CASH** | **-10.9 bps** (±6.5) | `-29.5 bps` | `+0.075 / -0.004` | `0.45%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,245.12 | ⚪ **CASH** | **+6.7 bps** (±7.4) | `+7.8 bps` | `+0.038 / -0.026` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.17 | ⚪ **CASH** | **-31.6 bps** (±15.1) | `-42.7 bps` | `-0.047 / -0.170` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 07:30:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,020.02 | ⚪ **CASH** | **-10.9 bps** (±6.5) | `-29.5 bps` | `+0.075 / -0.004` | `0.45%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,244.56 | ⚪ **CASH** | **+6.7 bps** (±7.4) | `+7.8 bps` | `+0.038 / -0.026` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.14 | ⚪ **CASH** | **-31.6 bps** (±15.1) | `-42.7 bps` | `-0.047 / -0.170` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 07:15:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,023.58 | ⚪ **CASH** | **-10.9 bps** (±6.5) | `-29.5 bps` | `+0.075 / -0.004` | `0.45%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,246.89 | ⚪ **CASH** | **+6.7 bps** (±7.4) | `+7.8 bps` | `+0.038 / -0.026` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.23 | ⚪ **CASH** | **-31.6 bps** (±15.1) | `-42.7 bps` | `-0.047 / -0.170` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 07:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,056.11 | ⚪ **CASH** | **-10.9 bps** (±6.5) | `-29.5 bps` | `+0.075 / -0.004` | `0.45%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,246.69 | ⚪ **CASH** | **+6.7 bps** (±7.4) | `+7.8 bps` | `+0.038 / -0.026` | `0.61%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.25 | ⚪ **CASH** | **-31.6 bps** (±15.1) | `-42.7 bps` | `-0.047 / -0.170` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 06:45:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,046.99 | ⚪ **CASH** | **-8.8 bps** (±6.2) | `-29.5 bps` | `+0.081 / +0.042` | `0.46%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,247.15 | ⚪ **CASH** | **+8.2 bps** (±7.3) | `+7.3 bps` | `+0.044 / +0.009` | `0.62%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.28 | ⚪ **CASH** | **-28.8 bps** (±14.9) | `-37.6 bps` | `-0.049 / -0.172` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 06:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,065.05 | ⚪ **CASH** | **-8.8 bps** (±6.2) | `-29.5 bps` | `+0.081 / +0.042` | `0.46%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,246.00 | ⚪ **CASH** | **+8.2 bps** (±7.3) | `+7.3 bps` | `+0.044 / +0.009` | `0.62%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.16 | ⚪ **CASH** | **-28.8 bps** (±14.9) | `-37.6 bps` | `-0.049 / -0.172` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 06:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,050.01 | ⚪ **CASH** | **-8.8 bps** (±6.2) | `-29.5 bps` | `+0.081 / +0.042` | `0.46%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,247.41 | ⚪ **CASH** | **+8.2 bps** (±7.3) | `+7.3 bps` | `+0.044 / +0.009` | `0.62%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.27 | ⚪ **CASH** | **-28.8 bps** (±14.9) | `-37.6 bps` | `-0.049 / -0.172` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 06:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,034.00 | ⚪ **CASH** | **-8.8 bps** (±6.2) | `-29.5 bps` | `+0.081 / +0.042` | `0.46%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,248.97 | ⚪ **CASH** | **+8.2 bps** (±7.3) | `+7.3 bps` | `+0.044 / +0.009` | `0.62%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.28 | ⚪ **CASH** | **-28.8 bps** (±14.9) | `-37.6 bps` | `-0.049 / -0.172` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 05:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,001.92 | ⚪ **CASH** | **+3.2 bps** (±2.5) | `-3.0 bps` | `+0.074 / -0.024` | `0.47%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,248.48 | ⚪ **CASH** | **+11.6 bps** (±6.9) | `+13.1 bps` | `+0.041 / +0.023` | `0.62%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.15 | ⚪ **CASH** | **-24.0 bps** (±9.1) | `-30.8 bps` | `-0.049 / -0.152` | `0.64%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
