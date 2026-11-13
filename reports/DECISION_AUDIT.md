# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-13 10:00:54 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-13 10:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,111.90 | ⚪ **CASH** | **-16.8 bps** (±6.6) | `-22.6 bps` | `-0.049 / +0.006` | `0.56%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,944.42 | ⚪ **CASH** | **-19.5 bps** (±13.6) | `-20.1 bps` | `-0.061 / -0.069` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |
| **SOLUSDT** | $80.17 | ⚪ **CASH** | **-6.7 bps** (±27.1) | `-0.0 bps` | `-0.004 / -0.067` | `0.71%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (27.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 09:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,055.99 | ⚪ **CASH** | **-1.8 bps** (±10.3) | `+6.3 bps` | `-0.044 / -0.020` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,940.12 | ⚪ **CASH** | **-19.3 bps** (±11.1) | `-17.8 bps` | `-0.063 / -0.107` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $79.91 | ⚪ **CASH** | **-19.2 bps** (±22.1) | `-27.6 bps` | `+0.013 / -0.037` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 09:30:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,943.11 | ⚪ **CASH** | **-1.8 bps** (±10.3) | `+6.3 bps` | `-0.044 / -0.020` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,938.78 | ⚪ **CASH** | **-19.3 bps** (±11.1) | `-17.8 bps` | `-0.063 / -0.107` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $79.77 | ⚪ **CASH** | **-19.2 bps** (±22.1) | `-27.6 bps` | `+0.013 / -0.037` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 09:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,837.63 | ⚪ **CASH** | **-1.8 bps** (±10.3) | `+6.3 bps` | `-0.044 / -0.020` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,936.02 | ⚪ **CASH** | **-19.3 bps** (±11.1) | `-17.8 bps` | `-0.063 / -0.107` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $79.88 | ⚪ **CASH** | **-19.2 bps** (±22.1) | `-27.6 bps` | `+0.013 / -0.037` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 09:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,744.00 | ⚪ **CASH** | **-1.8 bps** (±10.3) | `+6.3 bps` | `-0.044 / -0.020` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,933.41 | ⚪ **CASH** | **-19.3 bps** (±11.1) | `-17.8 bps` | `-0.063 / -0.107` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $79.81 | ⚪ **CASH** | **-19.2 bps** (±22.1) | `-27.6 bps` | `+0.013 / -0.037` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 08:45:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,818.46 | ⚪ **CASH** | **+0.2 bps** (±7.0) | `+11.9 bps` | `-0.048 / -0.049` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,933.58 | ⚪ **CASH** | **-20.8 bps** (±6.2) | `-20.0 bps` | `-0.064 / -0.124` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $79.98 | ⚪ **CASH** | **-5.3 bps** (±26.1) | `-2.7 bps` | `+0.023 / -0.032` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 08:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,773.19 | ⚪ **CASH** | **+0.2 bps** (±7.0) | `+11.9 bps` | `-0.048 / -0.049` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,934.56 | ⚪ **CASH** | **-20.8 bps** (±6.2) | `-20.0 bps` | `-0.064 / -0.124` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $79.95 | ⚪ **CASH** | **-5.3 bps** (±26.1) | `-2.7 bps` | `+0.023 / -0.032` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 08:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,692.00 | ⚪ **CASH** | **+0.2 bps** (±7.0) | `+11.9 bps` | `-0.048 / -0.049` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,932.64 | ⚪ **CASH** | **-20.8 bps** (±6.2) | `-20.0 bps` | `-0.064 / -0.124` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $79.77 | ⚪ **CASH** | **-5.3 bps** (±26.1) | `-2.7 bps` | `+0.023 / -0.032` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 08:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,645.26 | ⚪ **CASH** | **+0.2 bps** (±7.0) | `+11.9 bps` | `-0.048 / -0.049` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,935.46 | ⚪ **CASH** | **-20.8 bps** (±6.2) | `-20.0 bps` | `-0.064 / -0.124` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $79.85 | ⚪ **CASH** | **-5.3 bps** (±26.1) | `-2.7 bps` | `+0.023 / -0.032` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 07:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,818.00 | ⚪ **CASH** | **-16.2 bps** (±11.3) | `-16.1 bps` | `-0.051 / -0.060` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,941.77 | ⚪ **CASH** | **-33.5 bps** (±11.8) | `-41.1 bps` | `-0.065 / -0.135` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $80.19 | ⚪ **CASH** | **-1.7 bps** (±36.6) | `+4.7 bps` | `+0.029 / -0.023` | `0.73%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 07:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,019.67 | ⚪ **CASH** | **-16.2 bps** (±11.3) | `-16.1 bps` | `-0.051 / -0.060` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,943.46 | ⚪ **CASH** | **-33.5 bps** (±11.8) | `-41.1 bps` | `-0.065 / -0.135` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $80.60 | ⚪ **CASH** | **-1.7 bps** (±36.6) | `+4.7 bps` | `+0.029 / -0.023` | `0.73%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 07:15:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,176.99 | ⚪ **CASH** | **-16.2 bps** (±11.3) | `-16.1 bps` | `-0.051 / -0.060` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,944.90 | ⚪ **CASH** | **-33.5 bps** (±11.8) | `-41.1 bps` | `-0.065 / -0.135` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $80.48 | ⚪ **CASH** | **-1.7 bps** (±36.6) | `+4.7 bps` | `+0.029 / -0.023` | `0.73%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 07:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,129.41 | ⚪ **CASH** | **-16.2 bps** (±11.3) | `-16.1 bps` | `-0.051 / -0.060` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,940.42 | ⚪ **CASH** | **-33.5 bps** (±11.8) | `-41.1 bps` | `-0.065 / -0.135` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $80.23 | ⚪ **CASH** | **-1.7 bps** (±36.6) | `+4.7 bps` | `+0.029 / -0.023` | `0.73%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 06:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,948.00 | ⚪ **CASH** | **+4.3 bps** (±5.1) | `+24.3 bps` | `-0.062 / -0.099` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.1 bps) |
| **ETHUSDT** | $1,935.53 | ⚪ **CASH** | **-3.2 bps** (±25.5) | `+18.8 bps` | `-0.070 / -0.152` | `0.66%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.5 bps > 19.5) |
| **SOLUSDT** | $79.95 | ⚪ **CASH** | **-15.0 bps** (±34.1) | `-18.6 bps` | `+0.026 / -0.031` | `0.62%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (34.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 06:30:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,824.01 | ⚪ **CASH** | **+4.3 bps** (±5.1) | `+24.3 bps` | `-0.062 / -0.099` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.1 bps) |
| **ETHUSDT** | $1,935.63 | ⚪ **CASH** | **-3.2 bps** (±25.5) | `+18.8 bps` | `-0.070 / -0.152` | `0.66%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.5 bps > 19.5) |
| **SOLUSDT** | $79.79 | ⚪ **CASH** | **-15.0 bps** (±34.1) | `-18.6 bps` | `+0.026 / -0.031` | `0.62%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (34.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 06:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,374.46 | ⚪ **CASH** | **+4.3 bps** (±5.1) | `+24.3 bps` | `-0.062 / -0.099` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.1 bps) |
| **ETHUSDT** | $1,918.67 | ⚪ **CASH** | **-3.2 bps** (±25.5) | `+18.8 bps` | `-0.070 / -0.152` | `0.66%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.5 bps > 19.5) |
| **SOLUSDT** | $78.93 | ⚪ **CASH** | **-15.0 bps** (±34.1) | `-18.6 bps` | `+0.026 / -0.031` | `0.62%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (34.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 06:00:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,962.51 | ⚪ **CASH** | **+4.3 bps** (±5.1) | `+24.3 bps` | `-0.062 / -0.099` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.1 bps) |
| **ETHUSDT** | $1,905.51 | ⚪ **CASH** | **-3.2 bps** (±25.5) | `+18.8 bps` | `-0.070 / -0.152` | `0.66%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.5 bps > 19.5) |
| **SOLUSDT** | $78.29 | ⚪ **CASH** | **-15.0 bps** (±34.1) | `-18.6 bps` | `+0.026 / -0.031` | `0.62%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (34.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 05:45:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,596.01 | ⚪ **CASH** | **-3.9 bps** (±9.4) | `+12.0 bps` | `-0.066 / -0.117` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,922.03 | ⚪ **CASH** | **+17.6 bps** (±14.3) | `+52.1 bps` | `-0.057 / -0.131` | `0.66%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $78.83 | ⚪ **CASH** | **-1.3 bps** (±25.8) | `+2.1 bps` | `+0.038 / -0.003` | `0.63%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 05:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,568.00 | ⚪ **CASH** | **-3.9 bps** (±9.4) | `+12.0 bps` | `-0.066 / -0.117` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,917.60 | ⚪ **CASH** | **+17.6 bps** (±14.3) | `+52.1 bps` | `-0.057 / -0.131` | `0.66%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $78.52 | ⚪ **CASH** | **-1.3 bps** (±25.8) | `+2.1 bps` | `+0.038 / -0.003` | `0.63%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 05:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,714.02 | ⚪ **CASH** | **-3.9 bps** (±9.4) | `+12.0 bps` | `-0.066 / -0.117` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,927.34 | ⚪ **CASH** | **+17.6 bps** (±14.3) | `+52.1 bps` | `-0.057 / -0.131` | `0.66%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $78.62 | ⚪ **CASH** | **-1.3 bps** (±25.8) | `+2.1 bps` | `+0.038 / -0.003` | `0.63%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 05:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,480.00 | ⚪ **CASH** | **-3.9 bps** (±9.4) | `+12.0 bps` | `-0.066 / -0.117` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,923.48 | ⚪ **CASH** | **+17.6 bps** (±14.3) | `+52.1 bps` | `-0.057 / -0.131` | `0.66%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $78.39 | ⚪ **CASH** | **-1.3 bps** (±25.8) | `+2.1 bps` | `+0.038 / -0.003` | `0.63%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 04:45:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,648.00 | ⚪ **CASH** | **-12.6 bps** (±13.1) | `-4.0 bps` | `-0.060 / -0.115` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,925.14 | ⚪ **CASH** | **+5.8 bps** (±9.8) | `+29.7 bps` | `-0.059 / -0.131` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $78.32 | ⚪ **CASH** | **+0.7 bps** (±22.0) | `+6.2 bps` | `+0.032 / -0.017` | `0.64%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.0 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 04:30:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,972.82 | ⚪ **CASH** | **-12.6 bps** (±13.1) | `-4.0 bps` | `-0.060 / -0.115` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,932.38 | ⚪ **CASH** | **+5.8 bps** (±9.8) | `+29.7 bps` | `-0.059 / -0.131` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $78.42 | ⚪ **CASH** | **+0.7 bps** (±22.0) | `+6.2 bps` | `+0.032 / -0.017` | `0.64%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.0 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 04:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,993.16 | ⚪ **CASH** | **-12.6 bps** (±13.1) | `-4.0 bps` | `-0.060 / -0.115` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,939.58 | ⚪ **CASH** | **+5.8 bps** (±9.8) | `+29.7 bps` | `-0.059 / -0.131` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $78.50 | ⚪ **CASH** | **+0.7 bps** (±22.0) | `+6.2 bps` | `+0.032 / -0.017` | `0.64%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.0 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 04:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,878.02 | ⚪ **CASH** | **-12.6 bps** (±13.1) | `-4.0 bps` | `-0.060 / -0.115` | `0.49%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,932.72 | ⚪ **CASH** | **+5.8 bps** (±9.8) | `+29.7 bps` | `-0.059 / -0.131` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $78.40 | ⚪ **CASH** | **+0.7 bps** (±22.0) | `+6.2 bps` | `+0.032 / -0.017` | `0.64%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.0 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 03:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,144.85 | ⚪ **CASH** | **-1.8 bps** (±11.2) | `+13.7 bps` | `-0.045 / -0.127` | `0.39%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.6 bps) |
| **ETHUSDT** | $1,952.56 | ⚪ **CASH** | **+12.1 bps** (±7.5) | `+32.8 bps` | `-0.035 / -0.058` | `0.47%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $78.95 | ⚪ **CASH** | **-5.0 bps** (±26.0) | `-6.2 bps` | `+0.040 / +0.003` | `0.53%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.0 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 03:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,305.21 | ⚪ **CASH** | **-1.8 bps** (±11.2) | `+13.7 bps` | `-0.045 / -0.127` | `0.39%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.6 bps) |
| **ETHUSDT** | $1,958.47 | ⚪ **CASH** | **+12.1 bps** (±7.5) | `+32.8 bps` | `-0.035 / -0.058` | `0.47%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $79.14 | ⚪ **CASH** | **-5.0 bps** (±26.0) | `-6.2 bps` | `+0.040 / +0.003` | `0.53%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.0 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 03:15:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,687.00 | ⚪ **CASH** | **-1.8 bps** (±11.2) | `+13.7 bps` | `-0.045 / -0.127` | `0.39%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.6 bps) |
| **ETHUSDT** | $1,979.77 | ⚪ **CASH** | **+12.1 bps** (±7.5) | `+32.8 bps` | `-0.035 / -0.058` | `0.47%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $79.74 | ⚪ **CASH** | **-5.0 bps** (±26.0) | `-6.2 bps` | `+0.040 / +0.003` | `0.53%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.0 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 03:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $70,297.92 | ⚪ **CASH** | **-1.8 bps** (±11.2) | `+13.7 bps` | `-0.045 / -0.127` | `0.39%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.6 bps) |
| **ETHUSDT** | $1,991.78 | ⚪ **CASH** | **+12.1 bps** (±7.5) | `+32.8 bps` | `-0.035 / -0.058` | `0.47%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $80.29 | ⚪ **CASH** | **-5.0 bps** (±26.0) | `-6.2 bps` | `+0.040 / +0.003` | `0.53%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.0 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 02:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $70,260.93 | ⚪ **CASH** | **-5.3 bps** (±7.0) | `+1.4 bps` | `-0.028 / -0.086` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,991.08 | ⚪ **CASH** | **+21.9 bps** (±11.8) | `+39.6 bps` | `-0.018 / +0.082` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $80.26 | ⚪ **CASH** | **-10.3 bps** (±9.5) | `-28.7 bps` | `+0.058 / +0.112` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 02:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $70,495.39 | ⚪ **CASH** | **-5.3 bps** (±7.0) | `+1.4 bps` | `-0.028 / -0.086` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,999.44 | ⚪ **CASH** | **+21.9 bps** (±11.8) | `+39.6 bps` | `-0.018 / +0.082` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $80.77 | ⚪ **CASH** | **-10.3 bps** (±9.5) | `-28.7 bps` | `+0.058 / +0.112` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 02:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $70,565.98 | ⚪ **CASH** | **-5.3 bps** (±7.0) | `+1.4 bps` | `-0.028 / -0.086` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,998.70 | ⚪ **CASH** | **+21.9 bps** (±11.8) | `+39.6 bps` | `-0.018 / +0.082` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $80.76 | ⚪ **CASH** | **-10.3 bps** (±9.5) | `-28.7 bps` | `+0.058 / +0.112` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 02:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $70,937.27 | ⚪ **CASH** | **-5.3 bps** (±7.0) | `+1.4 bps` | `-0.028 / -0.086` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,011.02 | ⚪ **CASH** | **+21.9 bps** (±11.8) | `+39.6 bps` | `-0.018 / +0.082` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.26 | ⚪ **CASH** | **-10.3 bps** (±9.5) | `-28.7 bps` | `+0.058 / +0.112` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 01:45:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $70,988.00 | ⚪ **CASH** | **-5.6 bps** (±5.3) | `+3.9 bps` | `-0.036 / -0.120` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,011.66 | ⚪ **CASH** | **+32.3 bps** (±8.7) | `+56.7 bps` | `-0.018 / +0.109` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.42 | ⚪ **CASH** | **-0.7 bps** (±4.3) | `-14.6 bps` | `+0.048 / +0.170` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 01:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,167.73 | ⚪ **CASH** | **-5.6 bps** (±5.3) | `+3.9 bps` | `-0.036 / -0.120` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,015.90 | ⚪ **CASH** | **+32.3 bps** (±8.7) | `+56.7 bps` | `-0.018 / +0.109` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.58 | ⚪ **CASH** | **-0.7 bps** (±4.3) | `-14.6 bps` | `+0.048 / +0.170` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 01:15:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $70,905.44 | ⚪ **CASH** | **-5.6 bps** (±5.3) | `+3.9 bps` | `-0.036 / -0.120` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,009.31 | ⚪ **CASH** | **+32.3 bps** (±8.7) | `+56.7 bps` | `-0.018 / +0.109` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.41 | ⚪ **CASH** | **-0.7 bps** (±4.3) | `-14.6 bps` | `+0.048 / +0.170` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
