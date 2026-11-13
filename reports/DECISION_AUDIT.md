# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-13 05:45:52 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-11-13 01:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,074.01 | ⚪ **CASH** | **-5.6 bps** (±5.3) | `+3.9 bps` | `-0.036 / -0.120` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,009.53 | ⚪ **CASH** | **+32.3 bps** (±8.7) | `+56.7 bps` | `-0.018 / +0.109` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.51 | ⚪ **CASH** | **-0.7 bps** (±4.3) | `-14.6 bps` | `+0.048 / +0.170` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 00:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $70,930.01 | ⚪ **CASH** | **-2.5 bps** (±2.6) | `+3.8 bps` | `-0.020 / -0.078` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,004.86 | ⚪ **CASH** | **+22.4 bps** (±4.3) | `+33.0 bps` | `-0.008 / +0.157` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.16 | ⚪ **CASH** | **+0.5 bps** (±4.7) | `-15.2 bps` | `+0.044 / +0.206` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 00:30:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,238.95 | ⚪ **CASH** | **-2.5 bps** (±2.6) | `+3.8 bps` | `-0.020 / -0.078` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,013.55 | ⚪ **CASH** | **+22.4 bps** (±4.3) | `+33.0 bps` | `-0.008 / +0.157` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.59 | ⚪ **CASH** | **+0.5 bps** (±4.7) | `-15.2 bps` | `+0.044 / +0.206` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 00:15:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,340.94 | ⚪ **CASH** | **-2.5 bps** (±2.6) | `+3.8 bps` | `-0.020 / -0.078` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,016.15 | ⚪ **CASH** | **+22.4 bps** (±4.3) | `+33.0 bps` | `-0.008 / +0.157` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.66 | ⚪ **CASH** | **+0.5 bps** (±4.7) | `-15.2 bps` | `+0.044 / +0.206` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 00:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,471.03 | ⚪ **CASH** | **-2.5 bps** (±2.6) | `+3.8 bps` | `-0.020 / -0.078` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,020.17 | ⚪ **CASH** | **+22.4 bps** (±4.3) | `+33.0 bps` | `-0.008 / +0.157` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.79 | ⚪ **CASH** | **+0.5 bps** (±4.7) | `-15.2 bps` | `+0.044 / +0.206` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 23:45:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,306.71 | ⚪ **CASH** | **+0.0 bps** (±4.3) | `+6.6 bps` | `-0.019 / -0.046` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,017.65 | ⚪ **CASH** | **+28.3 bps** (±7.9) | `+45.3 bps` | `-0.010 / +0.145` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.69 | ⚪ **CASH** | **-0.1 bps** (±9.1) | `-10.5 bps` | `+0.020 / +0.166` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 23:30:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,397.16 | ⚪ **CASH** | **+0.0 bps** (±4.3) | `+6.6 bps` | `-0.019 / -0.046` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,017.61 | ⚪ **CASH** | **+28.3 bps** (±7.9) | `+45.3 bps` | `-0.010 / +0.145` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.68 | ⚪ **CASH** | **-0.1 bps** (±9.1) | `-10.5 bps` | `+0.020 / +0.166` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 23:15:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,468.30 | ⚪ **CASH** | **+0.0 bps** (±4.3) | `+6.6 bps` | `-0.019 / -0.046` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,017.85 | ⚪ **CASH** | **+28.3 bps** (±7.9) | `+45.3 bps` | `-0.010 / +0.145` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.69 | ⚪ **CASH** | **-0.1 bps** (±9.1) | `-10.5 bps` | `+0.020 / +0.166` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 23:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,340.68 | ⚪ **CASH** | **+0.0 bps** (±4.3) | `+6.6 bps` | `-0.019 / -0.046` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,012.48 | ⚪ **CASH** | **+28.3 bps** (±7.9) | `+45.3 bps` | `-0.010 / +0.145` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.39 | ⚪ **CASH** | **-0.1 bps** (±9.1) | `-10.5 bps` | `+0.020 / +0.166` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 22:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,423.69 | ⚪ **CASH** | **+2.2 bps** (±7.7) | `+9.7 bps` | `-0.019 / -0.023` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,012.57 | ⚪ **CASH** | **+28.5 bps** (±9.1) | `+48.2 bps` | `-0.013 / +0.114` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.37 | ⚪ **CASH** | **-0.3 bps** (±6.9) | `-10.2 bps` | `+0.011 / +0.165` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 22:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,503.76 | ⚪ **CASH** | **+2.2 bps** (±7.7) | `+9.7 bps` | `-0.019 / -0.023` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,014.62 | ⚪ **CASH** | **+28.5 bps** (±9.1) | `+48.2 bps` | `-0.013 / +0.114` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.49 | ⚪ **CASH** | **-0.3 bps** (±6.9) | `-10.2 bps` | `+0.011 / +0.165` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 22:15:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,408.00 | ⚪ **CASH** | **+2.2 bps** (±7.7) | `+9.7 bps` | `-0.019 / -0.023` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,012.46 | ⚪ **CASH** | **+28.5 bps** (±9.1) | `+48.2 bps` | `-0.013 / +0.114` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.36 | ⚪ **CASH** | **-0.3 bps** (±6.9) | `-10.2 bps` | `+0.011 / +0.165` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 22:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,504.00 | ⚪ **CASH** | **+2.2 bps** (±7.7) | `+9.7 bps` | `-0.019 / -0.023` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,015.53 | ⚪ **CASH** | **+28.5 bps** (±9.1) | `+48.2 bps` | `-0.013 / +0.114` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.33 | ⚪ **CASH** | **-0.3 bps** (±6.9) | `-10.2 bps` | `+0.011 / +0.165` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 21:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,555.76 | ⚪ **CASH** | **+2.7 bps** (±5.5) | `+7.5 bps` | `-0.015 / +0.008` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,019.53 | ⚪ **CASH** | **+33.4 bps** (±8.8) | `+58.3 bps` | `-0.013 / +0.094` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.50 | ⚪ **CASH** | **-1.1 bps** (±9.1) | `-10.3 bps` | `+0.001 / +0.161` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 21:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,610.06 | ⚪ **CASH** | **+2.7 bps** (±5.5) | `+7.5 bps` | `-0.015 / +0.008` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,021.36 | ⚪ **CASH** | **+33.4 bps** (±8.8) | `+58.3 bps` | `-0.013 / +0.094` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.60 | ⚪ **CASH** | **-1.1 bps** (±9.1) | `-10.3 bps` | `+0.001 / +0.161` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 21:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,547.60 | ⚪ **CASH** | **+2.7 bps** (±5.5) | `+7.5 bps` | `-0.015 / +0.008` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,018.02 | ⚪ **CASH** | **+33.4 bps** (±8.8) | `+58.3 bps` | `-0.013 / +0.094` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.55 | ⚪ **CASH** | **-1.1 bps** (±9.1) | `-10.3 bps` | `+0.001 / +0.161` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 21:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,499.98 | ⚪ **CASH** | **+2.7 bps** (±5.5) | `+7.5 bps` | `-0.015 / +0.008` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,017.40 | ⚪ **CASH** | **+33.4 bps** (±8.8) | `+58.3 bps` | `-0.013 / +0.094` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.42 | ⚪ **CASH** | **-1.1 bps** (±9.1) | `-10.3 bps` | `+0.001 / +0.161` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
