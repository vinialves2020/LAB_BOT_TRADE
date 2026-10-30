# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-30 10:47:16 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-30 10:47:16 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,609.52 | ⚪ **CASH** | **-30.8 bps** (±15.5) | `-38.4 bps` | `-0.058 / -0.094` | `0.61%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,241.83 | ⚪ **CASH** | **-24.0 bps** (±11.4) | `-45.0 bps` | `-0.016 / +0.121` | `0.78%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.95 | ⚪ **CASH** | **-59.8 bps** (±13.3) | `-105.5 bps` | `-0.035 / +0.083` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 10:32:42 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,512.00 | ⚪ **CASH** | **-30.8 bps** (±15.5) | `-38.4 bps` | `-0.058 / -0.094` | `0.61%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,236.56 | ⚪ **CASH** | **-24.0 bps** (±11.4) | `-45.0 bps` | `-0.016 / +0.121` | `0.78%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.90 | ⚪ **CASH** | **-59.8 bps** (±13.3) | `-105.5 bps` | `-0.035 / +0.083` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 10:17:26 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,405.24 | ⚪ **CASH** | **-30.8 bps** (±15.5) | `-38.4 bps` | `-0.058 / -0.094` | `0.61%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,223.42 | ⚪ **CASH** | **-24.0 bps** (±11.4) | `-45.0 bps` | `-0.016 / +0.121` | `0.78%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.40 | ⚪ **CASH** | **-59.8 bps** (±13.3) | `-105.5 bps` | `-0.035 / +0.083` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 10:02:57 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,600.01 | ⚪ **CASH** | **-30.8 bps** (±15.5) | `-38.4 bps` | `-0.058 / -0.094` | `0.61%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,226.05 | ⚪ **CASH** | **-24.0 bps** (±11.4) | `-45.0 bps` | `-0.016 / +0.121` | `0.78%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.64 | ⚪ **CASH** | **-59.8 bps** (±13.3) | `-105.5 bps` | `-0.035 / +0.083` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 09:47:25 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,600.02 | ⚪ **CASH** | **-29.5 bps** (±9.6) | `-44.4 bps` | `-0.047 / -0.009` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,228.19 | ⚪ **CASH** | **-12.7 bps** (±11.3) | `-24.2 bps` | `-0.019 / +0.112` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.85 | ⚪ **CASH** | **-67.5 bps** (±14.7) | `-120.2 bps` | `-0.036 / +0.091` | `0.94%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 09:32:27 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,641.27 | ⚪ **CASH** | **-29.5 bps** (±9.6) | `-44.4 bps` | `-0.047 / -0.009` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,223.54 | ⚪ **CASH** | **-12.7 bps** (±11.3) | `-24.2 bps` | `-0.019 / +0.112` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.87 | ⚪ **CASH** | **-67.5 bps** (±14.7) | `-120.2 bps` | `-0.036 / +0.091` | `0.94%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 09:17:12 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,817.69 | ⚪ **CASH** | **-29.5 bps** (±9.6) | `-44.4 bps` | `-0.047 / -0.009` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,224.80 | ⚪ **CASH** | **-12.7 bps** (±11.3) | `-24.2 bps` | `-0.019 / +0.112` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.10 | ⚪ **CASH** | **-67.5 bps** (±14.7) | `-120.2 bps` | `-0.036 / +0.091` | `0.94%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 09:02:16 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,994.14 | ⚪ **CASH** | **-29.5 bps** (±9.6) | `-44.4 bps` | `-0.047 / -0.009` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,229.17 | ⚪ **CASH** | **-12.7 bps** (±11.3) | `-24.2 bps` | `-0.019 / +0.112` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.35 | ⚪ **CASH** | **-67.5 bps** (±14.7) | `-120.2 bps` | `-0.036 / +0.091` | `0.94%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 08:47:10 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,966.01 | ⚪ **CASH** | **-9.7 bps** (±5.6) | `-11.8 bps` | `-0.034 / +0.002` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,225.15 | ⚪ **CASH** | **-1.1 bps** (±10.5) | `-3.0 bps` | `-0.020 / +0.100` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.11 | ⚪ **CASH** | **-49.3 bps** (±20.7) | `-86.8 bps` | `-0.037 / +0.095` | `0.95%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 08:34:17 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,051.50 | ⚪ **CASH** | **-9.7 bps** (±5.6) | `-11.8 bps` | `-0.034 / +0.002` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,231.05 | ⚪ **CASH** | **-1.1 bps** (±10.5) | `-3.0 bps` | `-0.020 / +0.100` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.37 | ⚪ **CASH** | **-49.3 bps** (±20.7) | `-86.8 bps` | `-0.037 / +0.095` | `0.95%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 08:17:25 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,143.24 | ⚪ **CASH** | **-9.7 bps** (±5.6) | `-11.8 bps` | `-0.034 / +0.002` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,233.86 | ⚪ **CASH** | **-1.1 bps** (±10.5) | `-3.0 bps` | `-0.020 / +0.100` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.41 | ⚪ **CASH** | **-49.3 bps** (±20.7) | `-86.8 bps` | `-0.037 / +0.095` | `0.95%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 08:02:27 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,125.13 | ⚪ **CASH** | **-9.7 bps** (±5.6) | `-11.8 bps` | `-0.034 / +0.002` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,233.32 | ⚪ **CASH** | **-1.1 bps** (±10.5) | `-3.0 bps` | `-0.020 / +0.100` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.28 | ⚪ **CASH** | **-49.3 bps** (±20.7) | `-86.8 bps` | `-0.037 / +0.095` | `0.95%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 07:47:30 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,262.00 | ⚪ **CASH** | **-8.2 bps** (±6.6) | `-8.1 bps` | `-0.033 / -0.012` | `0.63%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,237.96 | ⚪ **CASH** | **+4.5 bps** (±4.9) | `+12.9 bps` | `-0.026 / +0.005` | `0.80%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.55 | ⚪ **CASH** | **-41.5 bps** (±17.2) | `-70.7 bps` | `-0.039 / +0.058` | `0.95%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 07:32:19 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,550.01 | ⚪ **CASH** | **-8.2 bps** (±6.6) | `-8.1 bps` | `-0.033 / -0.012` | `0.63%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,249.42 | ⚪ **CASH** | **+4.5 bps** (±4.9) | `+12.9 bps` | `-0.026 / +0.005` | `0.80%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $98.23 | ⚪ **CASH** | **-41.5 bps** (±17.2) | `-70.7 bps` | `-0.039 / +0.058` | `0.95%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 07:17:33 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,480.00 | ⚪ **CASH** | **-8.2 bps** (±6.6) | `-8.1 bps` | `-0.033 / -0.012` | `0.63%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,250.82 | ⚪ **CASH** | **+4.5 bps** (±4.9) | `+12.9 bps` | `-0.026 / +0.005` | `0.80%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $98.06 | ⚪ **CASH** | **-41.5 bps** (±17.2) | `-70.7 bps` | `-0.039 / +0.058` | `0.95%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 07:02:39 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,640.61 | ⚪ **CASH** | **-8.2 bps** (±6.6) | `-8.1 bps` | `-0.033 / -0.012` | `0.63%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,254.12 | ⚪ **CASH** | **+4.5 bps** (±4.9) | `+12.9 bps` | `-0.026 / +0.005` | `0.80%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $98.27 | ⚪ **CASH** | **-41.5 bps** (±17.2) | `-70.7 bps` | `-0.039 / +0.058` | `0.95%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 06:47:20 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,480.01 | ⚪ **CASH** | **-25.0 bps** (±8.4) | `-34.8 bps` | `-0.035 / -0.061` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,245.37 | ⚪ **CASH** | **-15.3 bps** (±4.8) | `-19.1 bps` | `-0.032 / -0.045` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.92 | ⚪ **CASH** | **-51.1 bps** (±23.6) | `-83.2 bps` | `-0.041 / +0.004` | `0.97%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 06:32:15 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,682.01 | ⚪ **CASH** | **-25.0 bps** (±8.4) | `-34.8 bps` | `-0.035 / -0.061` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,252.21 | ⚪ **CASH** | **-15.3 bps** (±4.8) | `-19.1 bps` | `-0.032 / -0.045` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $98.24 | ⚪ **CASH** | **-51.1 bps** (±23.6) | `-83.2 bps` | `-0.041 / +0.004` | `0.97%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 06:17:19 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,617.94 | ⚪ **CASH** | **-25.0 bps** (±8.4) | `-34.8 bps` | `-0.035 / -0.061` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,247.50 | ⚪ **CASH** | **-15.3 bps** (±4.8) | `-19.1 bps` | `-0.032 / -0.045` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $98.13 | ⚪ **CASH** | **-51.1 bps** (±23.6) | `-83.2 bps` | `-0.041 / +0.004` | `0.97%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 06:02:28 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,600.00 | ⚪ **CASH** | **-25.0 bps** (±8.4) | `-34.8 bps` | `-0.035 / -0.061` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,241.46 | ⚪ **CASH** | **-15.3 bps** (±4.8) | `-19.1 bps` | `-0.032 / -0.045` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $98.06 | ⚪ **CASH** | **-51.1 bps** (±23.6) | `-83.2 bps` | `-0.041 / +0.004` | `0.97%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 05:47:16 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,746.70 | ⚪ **CASH** | **-13.1 bps** (±4.5) | `-12.6 bps` | `-0.034 / -0.082` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,250.16 | ⚪ **CASH** | **-1.4 bps** (±9.6) | `+7.3 bps` | `-0.034 / -0.047` | `0.81%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $98.44 | ⚪ **CASH** | **-48.9 bps** (±19.0) | `-76.8 bps` | `-0.045 / -0.041` | `0.97%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 05:32:45 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,731.75 | ⚪ **CASH** | **-13.1 bps** (±4.5) | `-12.6 bps` | `-0.034 / -0.082` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,252.24 | ⚪ **CASH** | **-1.4 bps** (±9.6) | `+7.3 bps` | `-0.034 / -0.047` | `0.81%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $98.27 | ⚪ **CASH** | **-48.9 bps** (±19.0) | `-76.8 bps` | `-0.045 / -0.041` | `0.97%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 05:17:39 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,612.23 | ⚪ **CASH** | **-13.1 bps** (±4.5) | `-12.6 bps` | `-0.034 / -0.082` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,249.55 | ⚪ **CASH** | **-1.4 bps** (±9.6) | `+7.3 bps` | `-0.034 / -0.047` | `0.81%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.88 | ⚪ **CASH** | **-48.9 bps** (±19.0) | `-76.8 bps` | `-0.045 / -0.041` | `0.97%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 05:02:23 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,440.52 | ⚪ **CASH** | **-13.1 bps** (±4.5) | `-12.6 bps` | `-0.034 / -0.082` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,247.12 | ⚪ **CASH** | **-1.4 bps** (±9.6) | `+7.3 bps` | `-0.034 / -0.047` | `0.81%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.62 | ⚪ **CASH** | **-48.9 bps** (±19.0) | `-76.8 bps` | `-0.045 / -0.041` | `0.97%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 04:47:37 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,418.12 | ⚪ **CASH** | **-14.5 bps** (±5.5) | `-14.9 bps` | `-0.032 / -0.088` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,247.90 | ⚪ **CASH** | **-10.1 bps** (±6.1) | `-6.3 bps` | `-0.036 / -0.091` | `0.82%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.44 | ⚪ **CASH** | **-43.0 bps** (±16.5) | `-61.3 bps` | `-0.051 / -0.110` | `0.98%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 04:32:29 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,445.09 | ⚪ **CASH** | **-14.5 bps** (±5.5) | `-14.9 bps` | `-0.032 / -0.088` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,246.03 | ⚪ **CASH** | **-10.1 bps** (±6.1) | `-6.3 bps` | `-0.036 / -0.091` | `0.82%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.51 | ⚪ **CASH** | **-43.0 bps** (±16.5) | `-61.3 bps` | `-0.051 / -0.110` | `0.98%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 04:17:15 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,316.24 | ⚪ **CASH** | **-14.5 bps** (±5.5) | `-14.9 bps` | `-0.032 / -0.088` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,241.50 | ⚪ **CASH** | **-10.1 bps** (±6.1) | `-6.3 bps` | `-0.036 / -0.091` | `0.82%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.49 | ⚪ **CASH** | **-43.0 bps** (±16.5) | `-61.3 bps` | `-0.051 / -0.110` | `0.98%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 04:02:30 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,060.01 | ⚪ **CASH** | **-14.5 bps** (±5.5) | `-14.9 bps` | `-0.032 / -0.088` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,232.67 | ⚪ **CASH** | **-10.1 bps** (±6.1) | `-6.3 bps` | `-0.036 / -0.091` | `0.82%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.01 | ⚪ **CASH** | **-43.0 bps** (±16.5) | `-61.3 bps` | `-0.051 / -0.110` | `0.98%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 03:47:27 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,092.00 | ⚪ **CASH** | **-24.8 bps** (±14.3) | `-30.8 bps` | `-0.038 / -0.094` | `0.63%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,234.52 | ⚪ **CASH** | **-6.5 bps** (±11.4) | `+3.0 bps` | `-0.041 / -0.105` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $97.14 | ⚪ **CASH** | **-47.1 bps** (±12.8) | `-68.3 bps` | `-0.054 / -0.119` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 03:32:51 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,802.63 | ⚪ **CASH** | **-24.8 bps** (±14.3) | `-30.8 bps` | `-0.038 / -0.094` | `0.63%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,224.34 | ⚪ **CASH** | **-6.5 bps** (±11.4) | `+3.0 bps` | `-0.041 / -0.105` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $96.41 | ⚪ **CASH** | **-47.1 bps** (±12.8) | `-68.3 bps` | `-0.054 / -0.119` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 03:17:19 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,358.24 | ⚪ **CASH** | **-24.8 bps** (±14.3) | `-30.8 bps` | `-0.038 / -0.094` | `0.63%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,213.05 | ⚪ **CASH** | **-6.5 bps** (±11.4) | `+3.0 bps` | `-0.041 / -0.105` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.67 | ⚪ **CASH** | **-47.1 bps** (±12.8) | `-68.3 bps` | `-0.054 / -0.119` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 03:02:49 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,534.83 | ⚪ **CASH** | **-24.8 bps** (±14.3) | `-30.8 bps` | `-0.038 / -0.094` | `0.63%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,216.17 | ⚪ **CASH** | **-6.5 bps** (±11.4) | `+3.0 bps` | `-0.041 / -0.105` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.83 | ⚪ **CASH** | **-47.1 bps** (±12.8) | `-68.3 bps` | `-0.054 / -0.119` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 02:47:49 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,402.67 | ⚪ **CASH** | **-16.8 bps** (±12.7) | `-14.5 bps` | `-0.033 / -0.135` | `0.61%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,211.32 | ⚪ **CASH** | **+17.9 bps** (±8.4) | `+49.0 bps` | `-0.055 / -0.121` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.30 | ⚪ **CASH** | **-4.3 bps** (±25.9) | `+13.4 bps` | `-0.056 / -0.143` | `0.89%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 02:32:46 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,340.20 | ⚪ **CASH** | **-16.8 bps** (±12.7) | `-14.5 bps` | `-0.033 / -0.135` | `0.61%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,213.86 | ⚪ **CASH** | **+17.9 bps** (±8.4) | `+49.0 bps` | `-0.055 / -0.121` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.21 | ⚪ **CASH** | **-4.3 bps** (±25.9) | `+13.4 bps` | `-0.056 / -0.143` | `0.89%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 02:17:22 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,079.86 | ⚪ **CASH** | **-16.8 bps** (±12.7) | `-14.5 bps` | `-0.033 / -0.135` | `0.61%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,206.44 | ⚪ **CASH** | **+17.9 bps** (±8.4) | `+49.0 bps` | `-0.055 / -0.121` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.59 | ⚪ **CASH** | **-4.3 bps** (±25.9) | `+13.4 bps` | `-0.056 / -0.143` | `0.89%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-30 02:02:21 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,715.99 | ⚪ **CASH** | **-16.8 bps** (±12.7) | `-14.5 bps` | `-0.033 / -0.135` | `0.61%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,192.26 | ⚪ **CASH** | **+17.9 bps** (±8.4) | `+49.0 bps` | `-0.055 / -0.121` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $93.83 | ⚪ **CASH** | **-4.3 bps** (±25.9) | `+13.4 bps` | `-0.056 / -0.143` | `0.89%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
