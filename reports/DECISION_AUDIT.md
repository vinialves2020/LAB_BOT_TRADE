# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-06 21:45:50 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-06 21:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,841.61 | ⚪ **CASH** | **+2.7 bps** (±7.0) | `-0.2 bps` | `+0.034 / +0.020` | `0.53%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,230.56 | ⚪ **CASH** | **+6.6 bps** (±7.5) | `+13.8 bps` | `-0.015 / -0.009` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.07 | ⚪ **CASH** | **-25.2 bps** (±12.2) | `-40.5 bps` | `-0.032 / -0.026` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 21:30:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,776.02 | ⚪ **CASH** | **+2.7 bps** (±7.0) | `-0.2 bps` | `+0.034 / +0.020` | `0.53%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,228.00 | ⚪ **CASH** | **+6.6 bps** (±7.5) | `+13.8 bps` | `-0.015 / -0.009` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.89 | ⚪ **CASH** | **-25.2 bps** (±12.2) | `-40.5 bps` | `-0.032 / -0.026` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 21:15:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,911.28 | ⚪ **CASH** | **+2.7 bps** (±7.0) | `-0.2 bps` | `+0.034 / +0.020` | `0.53%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,231.60 | ⚪ **CASH** | **+6.6 bps** (±7.5) | `+13.8 bps` | `-0.015 / -0.009` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.10 | ⚪ **CASH** | **-25.2 bps** (±12.2) | `-40.5 bps` | `-0.032 / -0.026` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 21:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,903.00 | ⚪ **CASH** | **+2.7 bps** (±7.0) | `-0.2 bps` | `+0.034 / +0.020` | `0.53%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,230.41 | ⚪ **CASH** | **+6.6 bps** (±7.5) | `+13.8 bps` | `-0.015 / -0.009` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.00 | ⚪ **CASH** | **-25.2 bps** (±12.2) | `-40.5 bps` | `-0.032 / -0.026` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 20:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,897.35 | ⚪ **CASH** | **+0.2 bps** (±5.3) | `+0.2 bps` | `+0.024 / -0.037` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,232.91 | ⚪ **CASH** | **+4.1 bps** (±3.4) | `+10.9 bps` | `-0.017 / -0.038` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.00 | ⚪ **CASH** | **-28.0 bps** (±12.4) | `-44.7 bps` | `-0.032 / -0.031` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 20:30:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,818.15 | ⚪ **CASH** | **+0.2 bps** (±5.3) | `+0.2 bps` | `+0.024 / -0.037` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,232.11 | ⚪ **CASH** | **+4.1 bps** (±3.4) | `+10.9 bps` | `-0.017 / -0.038` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.89 | ⚪ **CASH** | **-28.0 bps** (±12.4) | `-44.7 bps` | `-0.032 / -0.031` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 20:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,852.01 | ⚪ **CASH** | **+0.2 bps** (±5.3) | `+0.2 bps` | `+0.024 / -0.037` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,232.48 | ⚪ **CASH** | **+4.1 bps** (±3.4) | `+10.9 bps` | `-0.017 / -0.038` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.26 | ⚪ **CASH** | **-28.0 bps** (±12.4) | `-44.7 bps` | `-0.032 / -0.031` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 20:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,920.32 | ⚪ **CASH** | **+0.2 bps** (±5.3) | `+0.2 bps` | `+0.024 / -0.037` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.33 | ⚪ **CASH** | **+4.1 bps** (±3.4) | `+10.9 bps` | `-0.017 / -0.038` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.25 | ⚪ **CASH** | **-28.0 bps** (±12.4) | `-44.7 bps` | `-0.032 / -0.031` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 19:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,758.01 | ⚪ **CASH** | **-0.3 bps** (±6.2) | `-0.5 bps` | `+0.029 / -0.048` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,231.65 | ⚪ **CASH** | **+2.3 bps** (±6.6) | `+7.9 bps` | `-0.016 / -0.036` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.93 | ⚪ **CASH** | **-29.9 bps** (±8.1) | `-47.2 bps` | `-0.028 / -0.066` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 19:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,706.00 | ⚪ **CASH** | **-0.3 bps** (±6.2) | `-0.5 bps` | `+0.029 / -0.048` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,227.51 | ⚪ **CASH** | **+2.3 bps** (±6.6) | `+7.9 bps` | `-0.016 / -0.036` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.03 | ⚪ **CASH** | **-29.9 bps** (±8.1) | `-47.2 bps` | `-0.028 / -0.066` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 19:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,768.00 | ⚪ **CASH** | **-0.3 bps** (±6.2) | `-0.5 bps` | `+0.029 / -0.048` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,231.09 | ⚪ **CASH** | **+2.3 bps** (±6.6) | `+7.9 bps` | `-0.016 / -0.036` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.28 | ⚪ **CASH** | **-29.9 bps** (±8.1) | `-47.2 bps` | `-0.028 / -0.066` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 19:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,818.33 | ⚪ **CASH** | **-0.3 bps** (±6.2) | `-0.5 bps` | `+0.029 / -0.048` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,231.43 | ⚪ **CASH** | **+2.3 bps** (±6.6) | `+7.9 bps` | `-0.016 / -0.036` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.27 | ⚪ **CASH** | **-29.9 bps** (±8.1) | `-47.2 bps` | `-0.028 / -0.066` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 18:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,875.06 | ⚪ **CASH** | **+7.1 bps** (±3.5) | `+12.2 bps` | `+0.031 / -0.049` | `0.56%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,231.28 | ⚪ **CASH** | **+2.0 bps** (±8.3) | `+8.0 bps` | `-0.014 / -0.048` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.33 | ⚪ **CASH** | **-30.3 bps** (±12.7) | `-47.2 bps` | `-0.019 / -0.080` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 18:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,827.53 | ⚪ **CASH** | **+7.1 bps** (±3.5) | `+12.2 bps` | `+0.031 / -0.049` | `0.56%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,226.62 | ⚪ **CASH** | **+2.0 bps** (±8.3) | `+8.0 bps` | `-0.014 / -0.048` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.37 | ⚪ **CASH** | **-30.3 bps** (±12.7) | `-47.2 bps` | `-0.019 / -0.080` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 18:15:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,800.08 | ⚪ **CASH** | **+7.1 bps** (±3.5) | `+12.2 bps` | `+0.031 / -0.049` | `0.56%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,227.16 | ⚪ **CASH** | **+2.0 bps** (±8.3) | `+8.0 bps` | `-0.014 / -0.048` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.18 | ⚪ **CASH** | **-30.3 bps** (±12.7) | `-47.2 bps` | `-0.019 / -0.080` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 18:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,692.25 | ⚪ **CASH** | **+7.1 bps** (±3.5) | `+12.2 bps` | `+0.031 / -0.049` | `0.56%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,224.35 | ⚪ **CASH** | **+2.0 bps** (±8.3) | `+8.0 bps` | `-0.014 / -0.048` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.94 | ⚪ **CASH** | **-30.3 bps** (±12.7) | `-47.2 bps` | `-0.019 / -0.080` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 17:45:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,695.01 | ⚪ **CASH** | **+4.9 bps** (±2.3) | `+9.6 bps` | `+0.028 / -0.066` | `0.56%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,223.26 | ⚪ **CASH** | **-0.0 bps** (±8.2) | `+5.0 bps` | `-0.010 / -0.061` | `0.73%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.91 | ⚪ **CASH** | **-37.1 bps** (±8.2) | `-59.6 bps` | `-0.026 / -0.079` | `0.74%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 17:30:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,914.01 | ⚪ **CASH** | **+4.9 bps** (±2.3) | `+9.6 bps` | `+0.028 / -0.066` | `0.56%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,232.25 | ⚪ **CASH** | **-0.0 bps** (±8.2) | `+5.0 bps` | `-0.010 / -0.061` | `0.73%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.35 | ⚪ **CASH** | **-37.1 bps** (±8.2) | `-59.6 bps` | `-0.026 / -0.079` | `0.74%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 17:15:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,954.01 | ⚪ **CASH** | **+4.9 bps** (±2.3) | `+9.6 bps` | `+0.028 / -0.066` | `0.56%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,233.67 | ⚪ **CASH** | **-0.0 bps** (±8.2) | `+5.0 bps` | `-0.010 / -0.061` | `0.73%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.58 | ⚪ **CASH** | **-37.1 bps** (±8.2) | `-59.6 bps` | `-0.026 / -0.079` | `0.74%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 17:01:00 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,005.00 | ⚪ **CASH** | **+4.9 bps** (±2.3) | `+9.6 bps` | `+0.028 / -0.066` | `0.56%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.93 | ⚪ **CASH** | **-0.0 bps** (±8.2) | `+5.0 bps` | `-0.010 / -0.061` | `0.73%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.64 | ⚪ **CASH** | **-37.1 bps** (±8.2) | `-59.6 bps` | `-0.026 / -0.079` | `0.74%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 16:45:35 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,674.01 | ⚪ **CASH** | **+4.5 bps** (±4.4) | `+10.7 bps` | `+0.030 / -0.094` | `0.57%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,227.06 | ⚪ **CASH** | **-1.9 bps** (±7.7) | `+2.1 bps` | `-0.011 / -0.071` | `0.74%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.29 | ⚪ **CASH** | **-30.7 bps** (±5.8) | `-47.6 bps` | `-0.023 / -0.096` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 16:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,840.50 | ⚪ **CASH** | **+4.5 bps** (±4.4) | `+10.7 bps` | `+0.030 / -0.094` | `0.57%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,232.41 | ⚪ **CASH** | **-1.9 bps** (±7.7) | `+2.1 bps` | `-0.011 / -0.071` | `0.74%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.56 | ⚪ **CASH** | **-30.7 bps** (±5.8) | `-47.6 bps` | `-0.023 / -0.096` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 16:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,555.03 | ⚪ **CASH** | **+4.5 bps** (±4.4) | `+10.7 bps` | `+0.030 / -0.094` | `0.57%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,223.43 | ⚪ **CASH** | **-1.9 bps** (±7.7) | `+2.1 bps` | `-0.011 / -0.071` | `0.74%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.06 | ⚪ **CASH** | **-30.7 bps** (±5.8) | `-47.6 bps` | `-0.023 / -0.096` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 16:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,752.01 | ⚪ **CASH** | **+4.5 bps** (±4.4) | `+10.7 bps` | `+0.030 / -0.094` | `0.57%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,227.78 | ⚪ **CASH** | **-1.9 bps** (±7.7) | `+2.1 bps` | `-0.011 / -0.071` | `0.74%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.57 | ⚪ **CASH** | **-30.7 bps** (±5.8) | `-47.6 bps` | `-0.023 / -0.096` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 15:45:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,695.52 | ⚪ **CASH** | **+3.8 bps** (±5.0) | `+9.0 bps` | `-0.013 / +0.011` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,225.07 | ⚪ **CASH** | **-12.5 bps** (±5.9) | `-12.9 bps` | `-0.048 / -0.053` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.40 | ⚪ **CASH** | **-33.9 bps** (±4.8) | `-55.2 bps` | `-0.017 / -0.052` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 15:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,452.90 | ⚪ **CASH** | **+3.8 bps** (±5.0) | `+9.0 bps` | `-0.013 / +0.011` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,216.95 | ⚪ **CASH** | **-12.5 bps** (±5.9) | `-12.9 bps` | `-0.048 / -0.053` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.37 | ⚪ **CASH** | **-33.9 bps** (±4.8) | `-55.2 bps` | `-0.017 / -0.052` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 15:15:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,802.00 | ⚪ **CASH** | **+3.8 bps** (±5.0) | `+9.0 bps` | `-0.013 / +0.011` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,232.67 | ⚪ **CASH** | **-12.5 bps** (±5.9) | `-12.9 bps` | `-0.048 / -0.053` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.09 | ⚪ **CASH** | **-33.9 bps** (±4.8) | `-55.2 bps` | `-0.017 / -0.052` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 15:00:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,538.24 | ⚪ **CASH** | **+3.8 bps** (±5.0) | `+9.0 bps` | `-0.013 / +0.011` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,228.10 | ⚪ **CASH** | **-12.5 bps** (±5.9) | `-12.9 bps` | `-0.048 / -0.053` | `0.75%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.96 | ⚪ **CASH** | **-33.9 bps** (±4.8) | `-55.2 bps` | `-0.017 / -0.052` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 14:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,946.01 | ⚪ **CASH** | **-0.2 bps** (±16.6) | `-3.6 bps` | `-0.016 / +0.132` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,243.17 | ⚪ **CASH** | **-8.3 bps** (±6.2) | `-13.6 bps` | `-0.044 / +0.071` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.28 | ⚪ **CASH** | **-54.7 bps** (±20.1) | `-90.4 bps` | `-0.027 / -0.029` | `0.76%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 14:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,774.58 | ⚪ **CASH** | **-0.2 bps** (±16.6) | `-3.6 bps` | `-0.016 / +0.132` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.65 | ⚪ **CASH** | **-8.3 bps** (±6.2) | `-13.6 bps` | `-0.044 / +0.071` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.48 | ⚪ **CASH** | **-54.7 bps** (±20.1) | `-90.4 bps` | `-0.027 / -0.029` | `0.76%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 14:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,583.30 | ⚪ **CASH** | **-0.2 bps** (±16.6) | `-3.6 bps` | `-0.016 / +0.132` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,228.18 | ⚪ **CASH** | **-8.3 bps** (±6.2) | `-13.6 bps` | `-0.044 / +0.071` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.96 | ⚪ **CASH** | **-54.7 bps** (±20.1) | `-90.4 bps` | `-0.027 / -0.029` | `0.76%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 14:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,878.34 | ⚪ **CASH** | **-0.2 bps** (±16.6) | `-3.6 bps` | `-0.016 / +0.132` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.76 | ⚪ **CASH** | **-8.3 bps** (±6.2) | `-13.6 bps` | `-0.044 / +0.071` | `0.76%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.37 | ⚪ **CASH** | **-54.7 bps** (±20.1) | `-90.4 bps` | `-0.027 / -0.029` | `0.76%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 13:45:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,882.00 | ⚪ **CASH** | **-2.4 bps** (±20.0) | `-14.4 bps` | `-0.014 / +0.240` | `0.58%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,237.46 | ⚪ **CASH** | **-5.0 bps** (±8.3) | `-8.7 bps` | `-0.047 / +0.100` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.34 | ⚪ **CASH** | **-69.9 bps** (±19.4) | `-120.1 bps` | `-0.018 / -0.017` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 13:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,888.00 | ⚪ **CASH** | **-2.4 bps** (±20.0) | `-14.4 bps` | `-0.014 / +0.240` | `0.58%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.51 | ⚪ **CASH** | **-5.0 bps** (±8.3) | `-8.7 bps` | `-0.047 / +0.100` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.19 | ⚪ **CASH** | **-69.9 bps** (±19.4) | `-120.1 bps` | `-0.018 / -0.017` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 13:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,897.42 | ⚪ **CASH** | **-2.4 bps** (±20.0) | `-14.4 bps` | `-0.014 / +0.240` | `0.58%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.10 | ⚪ **CASH** | **-5.0 bps** (±8.3) | `-8.7 bps` | `-0.047 / +0.100` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.05 | ⚪ **CASH** | **-69.9 bps** (±19.4) | `-120.1 bps` | `-0.018 / -0.017` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-06 13:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,992.01 | ⚪ **CASH** | **-2.4 bps** (±20.0) | `-14.4 bps` | `-0.014 / +0.240` | `0.58%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,237.37 | ⚪ **CASH** | **-5.0 bps** (±8.3) | `-8.7 bps` | `-0.047 / +0.100` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.13 | ⚪ **CASH** | **-69.9 bps** (±19.4) | `-120.1 bps` | `-0.018 / -0.017` | `0.77%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
