# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-31 01:32:26 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-31 01:32:26 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,434.02 | ⚪ **CASH** | **+6.3 bps** (±2.9) | `+10.1 bps` | `-0.038 / +0.113` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,244.94 | ⚪ **CASH** | **+22.1 bps** (±9.5) | `+14.1 bps` | `+0.161 / +0.214` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.68 | ⚪ **CASH** | **+24.1 bps** (±15.0) | `+24.2 bps` | `+0.078 / +0.252` | `0.85%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-10-31 01:17:27 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,560.01 | ⚪ **CASH** | **+6.3 bps** (±2.9) | `+10.1 bps` | `-0.038 / +0.113` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,248.56 | ⚪ **CASH** | **+22.1 bps** (±9.5) | `+14.1 bps` | `+0.161 / +0.214` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.78 | ⚪ **CASH** | **+24.1 bps** (±15.0) | `+24.2 bps` | `+0.078 / +0.252` | `0.85%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-10-31 01:02:25 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,643.04 | ⚪ **CASH** | **+6.3 bps** (±2.9) | `+10.1 bps` | `-0.038 / +0.113` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,252.03 | ⚪ **CASH** | **+22.1 bps** (±9.5) | `+14.1 bps` | `+0.161 / +0.214` | `0.68%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.99 | ⚪ **CASH** | **+24.1 bps** (±15.0) | `+24.2 bps` | `+0.078 / +0.252` | `0.85%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-10-31 00:47:18 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,435.43 | ⚪ **CASH** | **-2.4 bps** (±2.6) | `+5.0 bps` | `-0.060 / -0.002` | `0.55%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,249.60 | ⚪ **CASH** | **+22.4 bps** (±10.2) | `+15.6 bps` | `+0.124 / +0.271` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.72 | ⚪ **CASH** | **+20.5 bps** (±13.8) | `+22.2 bps` | `+0.048 / +0.242` | `0.85%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 00:32:29 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,277.76 | ⚪ **CASH** | **-2.4 bps** (±2.6) | `+5.0 bps` | `-0.060 / -0.002` | `0.55%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,246.02 | ⚪ **CASH** | **+22.4 bps** (±10.2) | `+15.6 bps` | `+0.124 / +0.271` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.34 | ⚪ **CASH** | **+20.5 bps** (±13.8) | `+22.2 bps` | `+0.048 / +0.242` | `0.85%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 00:17:25 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,418.70 | ⚪ **CASH** | **-2.4 bps** (±2.6) | `+5.0 bps` | `-0.060 / -0.002` | `0.55%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,248.00 | ⚪ **CASH** | **+22.4 bps** (±10.2) | `+15.6 bps` | `+0.124 / +0.271` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.49 | ⚪ **CASH** | **+20.5 bps** (±13.8) | `+22.2 bps` | `+0.048 / +0.242` | `0.85%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-31 00:03:00 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,380.00 | ⚪ **CASH** | **-2.4 bps** (±2.6) | `+5.0 bps` | `-0.060 / -0.002` | `0.55%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,246.11 | ⚪ **CASH** | **+22.4 bps** (±10.2) | `+15.6 bps` | `+0.124 / +0.271` | `0.69%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.46 | ⚪ **CASH** | **+20.5 bps** (±13.8) | `+22.2 bps` | `+0.048 / +0.242` | `0.85%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 23:47:24 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,322.01 | ⚪ **CASH** | **-3.7 bps** (±5.3) | `+5.5 bps` | `-0.070 / -0.016` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,245.22 | ⚪ **CASH** | **+22.1 bps** (±9.6) | `+14.0 bps` | `+0.116 / +0.306` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.36 | ⚪ **CASH** | **+3.0 bps** (±13.6) | `-5.8 bps` | `+0.016 / +0.238` | `0.86%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 23:32:28 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,185.66 | ⚪ **CASH** | **-3.7 bps** (±5.3) | `+5.5 bps` | `-0.070 / -0.016` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,243.75 | ⚪ **CASH** | **+22.1 bps** (±9.6) | `+14.0 bps` | `+0.116 / +0.306` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.16 | ⚪ **CASH** | **+3.0 bps** (±13.6) | `-5.8 bps` | `+0.016 / +0.238` | `0.86%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 23:17:35 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,047.99 | ⚪ **CASH** | **-3.7 bps** (±5.3) | `+5.5 bps` | `-0.070 / -0.016` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,238.79 | ⚪ **CASH** | **+22.1 bps** (±9.6) | `+14.0 bps` | `+0.116 / +0.306` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.93 | ⚪ **CASH** | **+3.0 bps** (±13.6) | `-5.8 bps` | `+0.016 / +0.238` | `0.86%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 23:02:23 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,990.01 | ⚪ **CASH** | **-3.7 bps** (±5.3) | `+5.5 bps` | `-0.070 / -0.016` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,237.56 | ⚪ **CASH** | **+22.1 bps** (±9.6) | `+14.0 bps` | `+0.116 / +0.306` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.92 | ⚪ **CASH** | **+3.0 bps** (±13.6) | `-5.8 bps` | `+0.016 / +0.238` | `0.86%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 22:47:22 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,986.00 | ⚪ **CASH** | **-6.8 bps** (±7.5) | `+1.5 bps` | `-0.072 / -0.029` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,237.77 | ⚪ **CASH** | **+21.4 bps** (±8.4) | `+15.1 bps` | `+0.088 / +0.311` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.84 | ⚪ **CASH** | **-20.6 bps** (±9.1) | `-41.2 bps` | `-0.024 / +0.173` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 22:32:49 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,908.00 | ⚪ **CASH** | **-6.8 bps** (±7.5) | `+1.5 bps` | `-0.072 / -0.029` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,237.58 | ⚪ **CASH** | **+21.4 bps** (±8.4) | `+15.1 bps` | `+0.088 / +0.311` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.77 | ⚪ **CASH** | **-20.6 bps** (±9.1) | `-41.2 bps` | `-0.024 / +0.173` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 22:17:33 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,903.59 | ⚪ **CASH** | **-6.8 bps** (±7.5) | `+1.5 bps` | `-0.072 / -0.029` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,241.24 | ⚪ **CASH** | **+21.4 bps** (±8.4) | `+15.1 bps` | `+0.088 / +0.311` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.68 | ⚪ **CASH** | **-20.6 bps** (±9.1) | `-41.2 bps` | `-0.024 / +0.173` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 22:02:31 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,832.00 | ⚪ **CASH** | **-6.8 bps** (±7.5) | `+1.5 bps` | `-0.072 / -0.029` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,242.78 | ⚪ **CASH** | **+21.4 bps** (±8.4) | `+15.1 bps` | `+0.088 / +0.311` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.56 | ⚪ **CASH** | **-20.6 bps** (±9.1) | `-41.2 bps` | `-0.024 / +0.173` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 21:47:41 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,904.00 | ⚪ **CASH** | **-3.6 bps** (±8.1) | `+6.7 bps` | `-0.071 / -0.020` | `0.56%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,241.59 | ⚪ **CASH** | **+18.1 bps** (±10.1) | `+10.9 bps` | `+0.071 / +0.311` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.58 | ⚪ **CASH** | **-22.4 bps** (±8.7) | `-41.8 bps` | `-0.034 / +0.143` | `0.88%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 21:32:36 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,878.02 | ⚪ **CASH** | **-3.6 bps** (±8.1) | `+6.7 bps` | `-0.071 / -0.020` | `0.56%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,242.51 | ⚪ **CASH** | **+18.1 bps** (±10.1) | `+10.9 bps` | `+0.071 / +0.311` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.50 | ⚪ **CASH** | **-22.4 bps** (±8.7) | `-41.8 bps` | `-0.034 / +0.143` | `0.88%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 21:17:24 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,817.22 | ⚪ **CASH** | **-3.6 bps** (±8.1) | `+6.7 bps` | `-0.071 / -0.020` | `0.56%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,243.45 | ⚪ **CASH** | **+18.1 bps** (±10.1) | `+10.9 bps` | `+0.071 / +0.311` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.33 | ⚪ **CASH** | **-22.4 bps** (±8.7) | `-41.8 bps` | `-0.034 / +0.143` | `0.88%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 21:02:29 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,022.01 | ⚪ **CASH** | **-3.6 bps** (±8.1) | `+6.7 bps` | `-0.071 / -0.020` | `0.56%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,243.66 | ⚪ **CASH** | **+18.1 bps** (±10.1) | `+10.9 bps` | `+0.071 / +0.311` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.48 | ⚪ **CASH** | **-22.4 bps** (±8.7) | `-41.8 bps` | `-0.034 / +0.143` | `0.88%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 20:47:26 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,988.00 | ⚪ **CASH** | **-17.1 bps** (±13.7) | `-17.2 bps` | `-0.093 / +0.035` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,240.60 | ⚪ **CASH** | **+12.1 bps** (±12.1) | `+3.9 bps` | `+0.041 / +0.320` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.10 | ⚪ **CASH** | **-59.9 bps** (±7.8) | `-103.3 bps` | `-0.060 / +0.096` | `0.88%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 20:32:34 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,964.01 | ⚪ **CASH** | **-17.1 bps** (±13.7) | `-17.2 bps` | `-0.093 / +0.035` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,241.30 | ⚪ **CASH** | **+12.1 bps** (±12.1) | `+3.9 bps` | `+0.041 / +0.320` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.09 | ⚪ **CASH** | **-59.9 bps** (±7.8) | `-103.3 bps` | `-0.060 / +0.096` | `0.88%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 20:17:36 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,022.00 | ⚪ **CASH** | **-17.1 bps** (±13.7) | `-17.2 bps` | `-0.093 / +0.035` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,242.79 | ⚪ **CASH** | **+12.1 bps** (±12.1) | `+3.9 bps` | `+0.041 / +0.320` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.11 | ⚪ **CASH** | **-59.9 bps** (±7.8) | `-103.3 bps` | `-0.060 / +0.096` | `0.88%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 20:02:47 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,168.00 | ⚪ **CASH** | **-17.1 bps** (±13.7) | `-17.2 bps` | `-0.093 / +0.035` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,246.35 | ⚪ **CASH** | **+12.1 bps** (±12.1) | `+3.9 bps` | `+0.041 / +0.320` | `0.72%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.09 | ⚪ **CASH** | **-59.9 bps** (±7.8) | `-103.3 bps` | `-0.060 / +0.096` | `0.88%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 19:47:26 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,810.00 | ⚪ **CASH** | **-18.8 bps** (±16.3) | `-16.7 bps` | `-0.091 / -0.017` | `0.57%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,239.68 | ⚪ **CASH** | **+12.0 bps** (±10.9) | `+6.4 bps` | `+0.031 / +0.288` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.75 | ⚪ **CASH** | **-60.9 bps** (±25.6) | `-97.8 bps` | `-0.062 / +0.035` | `0.89%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 19:32:33 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,486.01 | ⚪ **CASH** | **-18.8 bps** (±16.3) | `-16.7 bps` | `-0.091 / -0.017` | `0.57%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,228.22 | ⚪ **CASH** | **+12.0 bps** (±10.9) | `+6.4 bps` | `+0.031 / +0.288` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.35 | ⚪ **CASH** | **-60.9 bps** (±25.6) | `-97.8 bps` | `-0.062 / +0.035` | `0.89%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 19:17:13 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,540.00 | ⚪ **CASH** | **-18.8 bps** (±16.3) | `-16.7 bps` | `-0.091 / -0.017` | `0.57%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,229.89 | ⚪ **CASH** | **+12.0 bps** (±10.9) | `+6.4 bps` | `+0.031 / +0.288` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.30 | ⚪ **CASH** | **-60.9 bps** (±25.6) | `-97.8 bps` | `-0.062 / +0.035` | `0.89%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 19:02:31 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,608.33 | ⚪ **CASH** | **-18.8 bps** (±16.3) | `-16.7 bps` | `-0.091 / -0.017` | `0.57%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,232.33 | ⚪ **CASH** | **+12.0 bps** (±10.9) | `+6.4 bps` | `+0.031 / +0.288` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.28 | ⚪ **CASH** | **-60.9 bps** (±25.6) | `-97.8 bps` | `-0.062 / +0.035` | `0.89%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 18:47:20 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,774.83 | ⚪ **CASH** | **-18.9 bps** (±12.2) | `-20.0 bps` | `-0.087 / +0.010` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,230.46 | ⚪ **CASH** | **+7.6 bps** (±8.6) | `-1.8 bps` | `+0.033 / +0.278` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.11 | ⚪ **CASH** | **-61.6 bps** (±12.6) | `-99.9 bps` | `-0.066 / +0.013` | `0.90%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 18:32:31 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,904.04 | ⚪ **CASH** | **-18.9 bps** (±12.2) | `-20.0 bps` | `-0.087 / +0.010` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,229.46 | ⚪ **CASH** | **+7.6 bps** (±8.6) | `-1.8 bps` | `+0.033 / +0.278` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.06 | ⚪ **CASH** | **-61.6 bps** (±12.6) | `-99.9 bps` | `-0.066 / +0.013` | `0.90%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 18:17:29 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,000.01 | ⚪ **CASH** | **-18.9 bps** (±12.2) | `-20.0 bps` | `-0.087 / +0.010` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,238.33 | ⚪ **CASH** | **+7.6 bps** (±8.6) | `-1.8 bps` | `+0.033 / +0.278` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.21 | ⚪ **CASH** | **-61.6 bps** (±12.6) | `-99.9 bps` | `-0.066 / +0.013` | `0.90%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 18:02:31 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,120.00 | ⚪ **CASH** | **-18.9 bps** (±12.2) | `-20.0 bps` | `-0.087 / +0.010` | `0.57%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,242.04 | ⚪ **CASH** | **+7.6 bps** (±8.6) | `-1.8 bps` | `+0.033 / +0.278` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.32 | ⚪ **CASH** | **-61.6 bps** (±12.6) | `-99.9 bps` | `-0.066 / +0.013` | `0.90%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 17:47:18 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,291.53 | ⚪ **CASH** | **-22.4 bps** (±16.3) | `-23.4 bps` | `-0.086 / -0.026` | `0.58%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,244.78 | ⚪ **CASH** | **+16.6 bps** (±13.4) | `+18.1 bps` | `+0.023 / +0.253` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.58 | ⚪ **CASH** | **-55.9 bps** (±14.7) | `-87.4 bps` | `-0.069 / -0.009` | `0.91%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 17:32:24 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,200.37 | ⚪ **CASH** | **-22.4 bps** (±16.3) | `-23.4 bps` | `-0.086 / -0.026` | `0.58%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,240.35 | ⚪ **CASH** | **+16.6 bps** (±13.4) | `+18.1 bps` | `+0.023 / +0.253` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.66 | ⚪ **CASH** | **-55.9 bps** (±14.7) | `-87.4 bps` | `-0.069 / -0.009` | `0.91%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 17:17:32 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,274.03 | ⚪ **CASH** | **-22.4 bps** (±16.3) | `-23.4 bps` | `-0.086 / -0.026` | `0.58%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,242.34 | ⚪ **CASH** | **+16.6 bps** (±13.4) | `+18.1 bps` | `+0.023 / +0.253` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.95 | ⚪ **CASH** | **-55.9 bps** (±14.7) | `-87.4 bps` | `-0.069 / -0.009` | `0.91%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 17:02:32 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,409.88 | ⚪ **CASH** | **-22.4 bps** (±16.3) | `-23.4 bps` | `-0.086 / -0.026` | `0.58%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,240.58 | ⚪ **CASH** | **+16.6 bps** (±13.4) | `+18.1 bps` | `+0.023 / +0.253` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.04 | ⚪ **CASH** | **-55.9 bps** (±14.7) | `-87.4 bps` | `-0.069 / -0.009` | `0.91%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 16:47:27 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,351.69 | ⚪ **CASH** | **-14.2 bps** (±12.9) | `-8.4 bps` | `-0.085 / -0.038` | `0.58%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,226.69 | ⚪ **CASH** | **+23.7 bps** (±8.9) | `+32.0 bps` | `+0.015 / +0.235` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.86 | ⚪ **CASH** | **-50.2 bps** (±13.3) | `-78.4 bps` | `-0.060 / -0.006` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
