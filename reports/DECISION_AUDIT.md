# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-05 22:15:39 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-05 22:15:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,100.01 | ⚪ **CASH** | **+14.4 bps** (±22.0) | `+41.9 bps` | `-0.107 / +0.062` | `0.68%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,242.13 | ⚪ **CASH** | **-20.1 bps** (±19.6) | `-12.4 bps` | `-0.130 / -0.039` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.20 | ⚪ **CASH** | **-26.0 bps** (±32.3) | `-36.1 bps` | `-0.016 / +0.024` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 22:00:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,794.55 | ⚪ **CASH** | **+14.4 bps** (±22.0) | `+41.9 bps` | `-0.107 / +0.062` | `0.68%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,226.88 | ⚪ **CASH** | **-20.1 bps** (±19.6) | `-12.4 bps` | `-0.130 / -0.039` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.85 | ⚪ **CASH** | **-26.0 bps** (±32.3) | `-36.1 bps` | `-0.016 / +0.024` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 21:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,965.21 | ⚪ **CASH** | **-9.5 bps** (±18.0) | `+5.7 bps` | `-0.105 / -0.066` | `0.69%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.04 | ⚪ **CASH** | **-38.5 bps** (±16.4) | `-44.4 bps` | `-0.122 / -0.084` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.11 | ⚪ **CASH** | **-17.1 bps** (±22.6) | `-20.6 bps` | `-0.014 / +0.003` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 21:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,016.01 | ⚪ **CASH** | **-9.5 bps** (±18.0) | `+5.7 bps` | `-0.105 / -0.066` | `0.69%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.13 | ⚪ **CASH** | **-38.5 bps** (±16.4) | `-44.4 bps` | `-0.122 / -0.084` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.99 | ⚪ **CASH** | **-17.1 bps** (±22.6) | `-20.6 bps` | `-0.014 / +0.003` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 21:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,005.92 | ⚪ **CASH** | **-9.5 bps** (±18.0) | `+5.7 bps` | `-0.105 / -0.066` | `0.69%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.70 | ⚪ **CASH** | **-38.5 bps** (±16.4) | `-44.4 bps` | `-0.122 / -0.084` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.68 | ⚪ **CASH** | **-17.1 bps** (±22.6) | `-20.6 bps` | `-0.014 / +0.003` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 21:01:04 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,130.74 | ⚪ **CASH** | **-9.5 bps** (±18.0) | `+5.7 bps` | `-0.105 / -0.066` | `0.69%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,246.70 | ⚪ **CASH** | **-38.5 bps** (±16.4) | `-44.4 bps` | `-0.122 / -0.084` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.80 | ⚪ **CASH** | **-17.1 bps** (±22.6) | `-20.6 bps` | `-0.014 / +0.003` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 20:46:02 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,182.77 | ⚪ **CASH** | **-18.0 bps** (±7.7) | `-9.9 bps` | `-0.111 / -0.078` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,250.32 | ⚪ **CASH** | **-52.1 bps** (±9.2) | `-70.4 bps` | `-0.124 / -0.078` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.17 | ⚪ **CASH** | **-8.6 bps** (±16.7) | `-4.3 bps` | `-0.015 / -0.021` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 20:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,004.16 | ⚪ **CASH** | **-18.0 bps** (±7.7) | `-9.9 bps` | `-0.111 / -0.078` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,246.10 | ⚪ **CASH** | **-52.1 bps** (±9.2) | `-70.4 bps` | `-0.124 / -0.078` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.86 | ⚪ **CASH** | **-8.6 bps** (±16.7) | `-4.3 bps` | `-0.015 / -0.021` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 20:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,054.21 | ⚪ **CASH** | **-18.0 bps** (±7.7) | `-9.9 bps` | `-0.111 / -0.078` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,250.04 | ⚪ **CASH** | **-52.1 bps** (±9.2) | `-70.4 bps` | `-0.124 / -0.078` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.87 | ⚪ **CASH** | **-8.6 bps** (±16.7) | `-4.3 bps` | `-0.015 / -0.021` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 20:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,320.01 | ⚪ **CASH** | **-18.0 bps** (±7.7) | `-9.9 bps` | `-0.111 / -0.078` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,260.39 | ⚪ **CASH** | **-52.1 bps** (±9.2) | `-70.4 bps` | `-0.124 / -0.078` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.06 | ⚪ **CASH** | **-8.6 bps** (±16.7) | `-4.3 bps` | `-0.015 / -0.021` | `0.92%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 19:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,428.01 | ⚪ **CASH** | **-11.5 bps** (±11.2) | `+5.5 bps` | `-0.127 / -0.087` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,265.30 | ⚪ **CASH** | **-43.6 bps** (±16.0) | `-51.8 bps` | `-0.130 / -0.086` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.00 | ⚪ **CASH** | **-28.4 bps** (±26.8) | `-36.4 bps` | `-0.022 / -0.029` | `0.93%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 19:30:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,038.01 | ⚪ **CASH** | **-11.5 bps** (±11.2) | `+5.5 bps` | `-0.127 / -0.087` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,251.14 | ⚪ **CASH** | **-43.6 bps** (±16.0) | `-51.8 bps` | `-0.130 / -0.086` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.34 | ⚪ **CASH** | **-28.4 bps** (±26.8) | `-36.4 bps` | `-0.022 / -0.029` | `0.93%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 19:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,262.01 | ⚪ **CASH** | **-11.5 bps** (±11.2) | `+5.5 bps` | `-0.127 / -0.087` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,258.60 | ⚪ **CASH** | **-43.6 bps** (±16.0) | `-51.8 bps` | `-0.130 / -0.086` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.74 | ⚪ **CASH** | **-28.4 bps** (±26.8) | `-36.4 bps` | `-0.022 / -0.029` | `0.93%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 19:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,088.91 | ⚪ **CASH** | **-11.5 bps** (±11.2) | `+5.5 bps` | `-0.127 / -0.087` | `0.70%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,250.71 | ⚪ **CASH** | **-43.6 bps** (±16.0) | `-51.8 bps` | `-0.130 / -0.086` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.58 | ⚪ **CASH** | **-28.4 bps** (±26.8) | `-36.4 bps` | `-0.022 / -0.029` | `0.93%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 18:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,236.01 | ⚪ **CASH** | **-6.0 bps** (±9.1) | `+15.7 bps` | `-0.124 / -0.101` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,254.11 | ⚪ **CASH** | **-33.5 bps** (±8.9) | `-34.5 bps` | `-0.129 / -0.092` | `0.96%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.57 | ⚪ **CASH** | **-8.9 bps** (±20.0) | `+0.7 bps` | `-0.026 / -0.070` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 18:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,160.01 | ⚪ **CASH** | **-6.0 bps** (±9.1) | `+15.7 bps` | `-0.124 / -0.101` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,254.50 | ⚪ **CASH** | **-33.5 bps** (±8.9) | `-34.5 bps` | `-0.129 / -0.092` | `0.96%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.59 | ⚪ **CASH** | **-8.9 bps** (±20.0) | `+0.7 bps` | `-0.026 / -0.070` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 18:15:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,124.16 | ⚪ **CASH** | **-6.0 bps** (±9.1) | `+15.7 bps` | `-0.124 / -0.101` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,258.06 | ⚪ **CASH** | **-33.5 bps** (±8.9) | `-34.5 bps` | `-0.129 / -0.092` | `0.96%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.57 | ⚪ **CASH** | **-8.9 bps** (±20.0) | `+0.7 bps` | `-0.026 / -0.070` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 18:00:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,856.87 | ⚪ **CASH** | **-6.0 bps** (±9.1) | `+15.7 bps` | `-0.124 / -0.101` | `0.71%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,252.27 | ⚪ **CASH** | **-33.5 bps** (±8.9) | `-34.5 bps` | `-0.129 / -0.092` | `0.96%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.04 | ⚪ **CASH** | **-8.9 bps** (±20.0) | `+0.7 bps` | `-0.026 / -0.070` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 17:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,936.15 | ⚪ **CASH** | **-9.3 bps** (±10.8) | `+9.4 bps` | `-0.117 / -0.110` | `0.72%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,251.40 | ⚪ **CASH** | **-48.4 bps** (±8.5) | `-60.4 bps` | `-0.138 / -0.102` | `0.97%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.39 | ⚪ **CASH** | **-17.3 bps** (±18.3) | `-16.9 bps` | `-0.011 / -0.066` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 17:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,021.36 | ⚪ **CASH** | **-9.3 bps** (±10.8) | `+9.4 bps` | `-0.117 / -0.110` | `0.72%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,255.30 | ⚪ **CASH** | **-48.4 bps** (±8.5) | `-60.4 bps` | `-0.138 / -0.102` | `0.97%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.83 | ⚪ **CASH** | **-17.3 bps** (±18.3) | `-16.9 bps` | `-0.011 / -0.066` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 17:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,100.01 | ⚪ **CASH** | **-9.3 bps** (±10.8) | `+9.4 bps` | `-0.117 / -0.110` | `0.72%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,254.88 | ⚪ **CASH** | **-48.4 bps** (±8.5) | `-60.4 bps` | `-0.138 / -0.102` | `0.97%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.92 | ⚪ **CASH** | **-17.3 bps** (±18.3) | `-16.9 bps` | `-0.011 / -0.066` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 17:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,365.09 | ⚪ **CASH** | **-9.3 bps** (±10.8) | `+9.4 bps` | `-0.117 / -0.110` | `0.72%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,265.42 | ⚪ **CASH** | **-48.4 bps** (±8.5) | `-60.4 bps` | `-0.138 / -0.102` | `0.97%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.28 | ⚪ **CASH** | **-17.3 bps** (±18.3) | `-16.9 bps` | `-0.011 / -0.066` | `0.93%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 16:45:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,462.40 | ⚪ **CASH** | **-16.7 bps** (±5.6) | `-0.2 bps` | `-0.120 / -0.174` | `0.72%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,265.96 | ⚪ **CASH** | **-51.0 bps** (±19.5) | `-62.5 bps` | `-0.127 / -0.126` | `0.97%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.47 | ⚪ **CASH** | **+9.3 bps** (±13.4) | `+31.8 bps` | `-0.006 / -0.091` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 16:30:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,808.33 | ⚪ **CASH** | **-16.7 bps** (±5.6) | `-0.2 bps` | `-0.120 / -0.174` | `0.72%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,277.00 | ⚪ **CASH** | **-51.0 bps** (±19.5) | `-62.5 bps` | `-0.127 / -0.126` | `0.97%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.19 | ⚪ **CASH** | **+9.3 bps** (±13.4) | `+31.8 bps` | `-0.006 / -0.091` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 16:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,442.10 | ⚪ **CASH** | **-16.7 bps** (±5.6) | `-0.2 bps` | `-0.120 / -0.174` | `0.72%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,262.96 | ⚪ **CASH** | **-51.0 bps** (±19.5) | `-62.5 bps` | `-0.127 / -0.126` | `0.97%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.87 | ⚪ **CASH** | **+9.3 bps** (±13.4) | `+31.8 bps` | `-0.006 / -0.091` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 16:01:05 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,979.99 | ⚪ **CASH** | **-16.7 bps** (±5.6) | `-0.2 bps` | `-0.120 / -0.174` | `0.72%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,250.68 | ⚪ **CASH** | **-51.0 bps** (±19.5) | `-62.5 bps` | `-0.127 / -0.126` | `0.97%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.09 | ⚪ **CASH** | **+9.3 bps** (±13.4) | `+31.8 bps` | `-0.006 / -0.091` | `0.94%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 15:45:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,179.34 | ⚪ **CASH** | **+0.9 bps** (±3.3) | `+15.3 bps` | `-0.030 / -0.133` | `0.51%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,272.80 | ⚪ **CASH** | **-23.9 bps** (±9.7) | `-23.7 bps` | `-0.073 / -0.143` | `0.68%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.67 | ⚪ **CASH** | **-16.0 bps** (±7.4) | `-17.6 bps` | `+0.007 / -0.144` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 15:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $76,486.81 | ⚪ **CASH** | **+0.9 bps** (±3.3) | `+15.3 bps` | `-0.030 / -0.133` | `0.51%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,276.00 | ⚪ **CASH** | **-23.9 bps** (±9.7) | `-23.7 bps` | `-0.073 / -0.143` | `0.68%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $90.97 | ⚪ **CASH** | **-16.0 bps** (±7.4) | `-17.6 bps` | `+0.007 / -0.144` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 15:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,176.01 | ⚪ **CASH** | **+0.9 bps** (±3.3) | `+15.3 bps` | `-0.030 / -0.133` | `0.51%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,289.89 | ⚪ **CASH** | **-23.9 bps** (±9.7) | `-23.7 bps` | `-0.073 / -0.143` | `0.68%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $91.05 | ⚪ **CASH** | **-16.0 bps** (±7.4) | `-17.6 bps` | `+0.007 / -0.144` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 15:00:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,175.30 | ⚪ **CASH** | **+0.9 bps** (±3.3) | `+15.3 bps` | `-0.030 / -0.133` | `0.51%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,340.58 | ⚪ **CASH** | **-23.9 bps** (±9.7) | `-23.7 bps` | `-0.073 / -0.143` | `0.68%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $92.97 | ⚪ **CASH** | **-16.0 bps** (±7.4) | `-17.6 bps` | `+0.007 / -0.144` | `0.79%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 14:45:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,864.00 | ⚪ **CASH** | **+2.6 bps** (±2.6) | `+18.3 bps` | `-0.012 / -0.174` | `0.41%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,364.32 | ⚪ **CASH** | **-31.3 bps** (±4.9) | `-35.7 bps` | `-0.052 / -0.223` | `0.61%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $93.92 | ⚪ **CASH** | **-16.9 bps** (±7.9) | `-24.3 bps` | `+0.031 / -0.112` | `0.66%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 14:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,558.59 | ⚪ **CASH** | **+2.6 bps** (±2.6) | `+18.3 bps` | `-0.012 / -0.174` | `0.41%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,387.23 | ⚪ **CASH** | **-31.3 bps** (±4.9) | `-35.7 bps` | `-0.052 / -0.223` | `0.61%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.44 | ⚪ **CASH** | **-16.9 bps** (±7.9) | `-24.3 bps` | `+0.031 / -0.112` | `0.66%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 14:16:21 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,450.19 | ⚪ **CASH** | **+2.6 bps** (±2.6) | `+18.3 bps` | `-0.012 / -0.174` | `0.41%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,381.80 | ⚪ **CASH** | **-31.3 bps** (±4.9) | `-35.7 bps` | `-0.052 / -0.223` | `0.61%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.19 | ⚪ **CASH** | **-16.9 bps** (±7.9) | `-24.3 bps` | `+0.031 / -0.112` | `0.66%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 14:01:29 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,620.01 | ⚪ **CASH** | **+2.6 bps** (±2.6) | `+18.3 bps` | `-0.012 / -0.174` | `0.41%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,386.67 | ⚪ **CASH** | **-31.3 bps** (±4.9) | `-35.7 bps` | `-0.052 / -0.223` | `0.61%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.30 | ⚪ **CASH** | **-16.9 bps** (±7.9) | `-24.3 bps` | `+0.031 / -0.112` | `0.66%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 13:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,809.27 | ⚪ **CASH** | **-2.5 bps** (±4.2) | `+14.0 bps` | `-0.008 / -0.255` | `0.42%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,393.87 | ⚪ **CASH** | **-38.7 bps** (±8.9) | `-45.1 bps` | `-0.048 / -0.283` | `0.61%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.59 | ⚪ **CASH** | **-15.7 bps** (±3.2) | `-24.6 bps` | `+0.040 / -0.106` | `0.67%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-05 13:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,626.65 | ⚪ **CASH** | **-2.5 bps** (±4.2) | `+14.0 bps` | `-0.008 / -0.255` | `0.42%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,387.27 | ⚪ **CASH** | **-38.7 bps** (±8.9) | `-45.1 bps` | `-0.048 / -0.283` | `0.61%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $95.31 | ⚪ **CASH** | **-15.7 bps** (±3.2) | `-24.6 bps` | `+0.040 / -0.106` | `0.67%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
