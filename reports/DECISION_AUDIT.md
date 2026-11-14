# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-14 17:45:46 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-14 17:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,918.05 | ⚪ **CASH** | **-29.9 bps** (±31.8) | `-27.5 bps` | `-0.096 / -0.106` | `0.52%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (31.8 bps > 19.5) |
| **ETHUSDT** | $1,849.28 | ⚪ **CASH** | **+5.6 bps** (±25.3) | `+35.5 bps` | `-0.099 / -0.096` | `0.70%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.3 bps > 19.5) |
| **SOLUSDT** | $73.09 | ⚪ **CASH** | **-37.1 bps** (±21.8) | `-49.5 bps` | `-0.045 / -0.073` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 17:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,637.26 | ⚪ **CASH** | **-29.9 bps** (±31.8) | `-27.5 bps` | `-0.096 / -0.106` | `0.52%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (31.8 bps > 19.5) |
| **ETHUSDT** | $1,845.04 | ⚪ **CASH** | **+5.6 bps** (±25.3) | `+35.5 bps` | `-0.099 / -0.096` | `0.70%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.3 bps > 19.5) |
| **SOLUSDT** | $73.06 | ⚪ **CASH** | **-37.1 bps** (±21.8) | `-49.5 bps` | `-0.045 / -0.073` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 17:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,250.01 | ⚪ **CASH** | **-29.9 bps** (±31.8) | `-27.5 bps` | `-0.096 / -0.106` | `0.52%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (31.8 bps > 19.5) |
| **ETHUSDT** | $1,820.17 | ⚪ **CASH** | **+5.6 bps** (±25.3) | `+35.5 bps` | `-0.099 / -0.096` | `0.70%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.3 bps > 19.5) |
| **SOLUSDT** | $72.42 | ⚪ **CASH** | **-37.1 bps** (±21.8) | `-49.5 bps` | `-0.045 / -0.073` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 17:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,193.13 | ⚪ **CASH** | **-29.9 bps** (±31.8) | `-27.5 bps` | `-0.096 / -0.106` | `0.52%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (31.8 bps > 19.5) |
| **ETHUSDT** | $1,818.14 | ⚪ **CASH** | **+5.6 bps** (±25.3) | `+35.5 bps` | `-0.099 / -0.096` | `0.70%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.3 bps > 19.5) |
| **SOLUSDT** | $72.13 | ⚪ **CASH** | **-37.1 bps** (±21.8) | `-49.5 bps` | `-0.045 / -0.073` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 16:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,209.72 | ⚪ **CASH** | **-32.0 bps** (±31.6) | `-30.2 bps` | `-0.098 / -0.120` | `0.53%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (31.6 bps > 19.5) |
| **ETHUSDT** | $1,818.89 | ⚪ **CASH** | **+26.7 bps** (±19.4) | `+74.8 bps` | `-0.105 / -0.116` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.8 bps) |
| **SOLUSDT** | $72.36 | ⚪ **CASH** | **-25.9 bps** (±19.2) | `-27.7 bps` | `-0.049 / -0.096` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.3 bps) |

---

### 🕒 Ciclo `2026-11-14 16:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,354.77 | ⚪ **CASH** | **-32.0 bps** (±31.6) | `-30.2 bps` | `-0.098 / -0.120` | `0.53%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (31.6 bps > 19.5) |
| **ETHUSDT** | $1,823.47 | ⚪ **CASH** | **+26.7 bps** (±19.4) | `+74.8 bps` | `-0.105 / -0.116` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.8 bps) |
| **SOLUSDT** | $72.58 | ⚪ **CASH** | **-25.9 bps** (±19.2) | `-27.7 bps` | `-0.049 / -0.096` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.3 bps) |

---

### 🕒 Ciclo `2026-11-14 16:15:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,367.83 | ⚪ **CASH** | **-32.0 bps** (±31.6) | `-30.2 bps` | `-0.098 / -0.120` | `0.53%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (31.6 bps > 19.5) |
| **ETHUSDT** | $1,829.30 | ⚪ **CASH** | **+26.7 bps** (±19.4) | `+74.8 bps` | `-0.105 / -0.116` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.8 bps) |
| **SOLUSDT** | $72.94 | ⚪ **CASH** | **-25.9 bps** (±19.2) | `-27.7 bps` | `-0.049 / -0.096` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.3 bps) |

---

### 🕒 Ciclo `2026-11-14 16:00:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,716.00 | ⚪ **CASH** | **-32.0 bps** (±31.6) | `-30.2 bps` | `-0.098 / -0.120` | `0.53%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (31.6 bps > 19.5) |
| **ETHUSDT** | $1,840.75 | ⚪ **CASH** | **+26.7 bps** (±19.4) | `+74.8 bps` | `-0.105 / -0.116` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.8 bps) |
| **SOLUSDT** | $73.88 | ⚪ **CASH** | **-25.9 bps** (±19.2) | `-27.7 bps` | `-0.049 / -0.096` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.3 bps) |

---

### 🕒 Ciclo `2026-11-14 15:45:31 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,680.12 | ⚪ **CASH** | **-53.5 bps** (±36.6) | `-72.3 bps` | `-0.075 / -0.111` | `0.54%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |
| **ETHUSDT** | $1,839.76 | ⚪ **CASH** | **+4.4 bps** (±33.2) | `+34.8 bps` | `-0.113 / -0.093` | `0.71%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.2 bps > 19.5) |
| **SOLUSDT** | $73.88 | ⚪ **CASH** | **-5.1 bps** (±14.0) | `+10.3 bps` | `-0.044 / -0.137` | `0.77%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.2 bps) |

---

### 🕒 Ciclo `2026-11-14 15:30:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,130.70 | ⚪ **CASH** | **-53.5 bps** (±36.6) | `-72.3 bps` | `-0.075 / -0.111` | `0.54%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |
| **ETHUSDT** | $1,825.47 | ⚪ **CASH** | **+4.4 bps** (±33.2) | `+34.8 bps` | `-0.113 / -0.093` | `0.71%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.2 bps > 19.5) |
| **SOLUSDT** | $73.23 | ⚪ **CASH** | **-5.1 bps** (±14.0) | `+10.3 bps` | `-0.044 / -0.137` | `0.77%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.2 bps) |

---

### 🕒 Ciclo `2026-11-14 15:15:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,566.46 | ⚪ **CASH** | **-53.5 bps** (±36.6) | `-72.3 bps` | `-0.075 / -0.111` | `0.54%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |
| **ETHUSDT** | $1,840.11 | ⚪ **CASH** | **+4.4 bps** (±33.2) | `+34.8 bps` | `-0.113 / -0.093` | `0.71%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.2 bps > 19.5) |
| **SOLUSDT** | $73.96 | ⚪ **CASH** | **-5.1 bps** (±14.0) | `+10.3 bps` | `-0.044 / -0.137` | `0.77%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.2 bps) |

---

### 🕒 Ciclo `2026-11-14 15:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,937.50 | ⚪ **CASH** | **-53.5 bps** (±36.6) | `-72.3 bps` | `-0.075 / -0.111` | `0.54%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |
| **ETHUSDT** | $1,854.45 | ⚪ **CASH** | **+4.4 bps** (±33.2) | `+34.8 bps` | `-0.113 / -0.093` | `0.71%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.2 bps > 19.5) |
| **SOLUSDT** | $74.16 | ⚪ **CASH** | **-5.1 bps** (±14.0) | `+10.3 bps` | `-0.044 / -0.137` | `0.77%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.2 bps) |

---

### 🕒 Ciclo `2026-11-14 14:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $66,143.12 | ⚪ **CASH** | **-43.5 bps** (±27.9) | `-57.4 bps` | `-0.066 / -0.106` | `0.50%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (27.9 bps > 19.5) |
| **ETHUSDT** | $1,857.94 | ⚪ **CASH** | **-44.8 bps** (±15.2) | `-59.8 bps` | `-0.107 / -0.079` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.22 | ⚪ **CASH** | **-6.4 bps** (±10.5) | `-2.4 bps` | `-0.022 / -0.031` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 14:30:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $66,346.07 | ⚪ **CASH** | **-43.5 bps** (±27.9) | `-57.4 bps` | `-0.066 / -0.106` | `0.50%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (27.9 bps > 19.5) |
| **ETHUSDT** | $1,862.34 | ⚪ **CASH** | **-44.8 bps** (±15.2) | `-59.8 bps` | `-0.107 / -0.079` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.43 | ⚪ **CASH** | **-6.4 bps** (±10.5) | `-2.4 bps` | `-0.022 / -0.031` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 14:15:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $66,443.27 | ⚪ **CASH** | **-43.5 bps** (±27.9) | `-57.4 bps` | `-0.066 / -0.106` | `0.50%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (27.9 bps > 19.5) |
| **ETHUSDT** | $1,872.44 | ⚪ **CASH** | **-44.8 bps** (±15.2) | `-59.8 bps` | `-0.107 / -0.079` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.94 | ⚪ **CASH** | **-6.4 bps** (±10.5) | `-2.4 bps` | `-0.022 / -0.031` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 14:00:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $66,822.53 | ⚪ **CASH** | **-43.5 bps** (±27.9) | `-57.4 bps` | `-0.066 / -0.106` | `0.50%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (27.9 bps > 19.5) |
| **ETHUSDT** | $1,893.82 | ⚪ **CASH** | **-44.8 bps** (±15.2) | `-59.8 bps` | `-0.107 / -0.079` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.51 | ⚪ **CASH** | **-6.4 bps** (±10.5) | `-2.4 bps` | `-0.022 / -0.031` | `0.72%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 13:45:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $66,828.81 | ⚪ **CASH** | **-36.8 bps** (±16.4) | `-49.5 bps` | `-0.046 / -0.116` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,893.30 | ⚪ **CASH** | **-44.5 bps** (±12.0) | `-58.9 bps` | `-0.084 / -0.143` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.60 | ⚪ **CASH** | **+4.7 bps** (±7.9) | `+17.6 bps` | `-0.012 / -0.065` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 13:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $66,657.58 | ⚪ **CASH** | **-36.8 bps** (±16.4) | `-49.5 bps` | `-0.046 / -0.116` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,889.34 | ⚪ **CASH** | **-44.5 bps** (±12.0) | `-58.9 bps` | `-0.084 / -0.143` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.27 | ⚪ **CASH** | **+4.7 bps** (±7.9) | `+17.6 bps` | `-0.012 / -0.065` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 13:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $66,807.14 | ⚪ **CASH** | **-36.8 bps** (±16.4) | `-49.5 bps` | `-0.046 / -0.116` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,893.96 | ⚪ **CASH** | **-44.5 bps** (±12.0) | `-58.9 bps` | `-0.084 / -0.143` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.62 | ⚪ **CASH** | **+4.7 bps** (±7.9) | `+17.6 bps` | `-0.012 / -0.065` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 13:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $66,992.01 | ⚪ **CASH** | **-36.8 bps** (±16.4) | `-49.5 bps` | `-0.046 / -0.116` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,898.75 | ⚪ **CASH** | **-44.5 bps** (±12.0) | `-58.9 bps` | `-0.084 / -0.143` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.57 | ⚪ **CASH** | **+4.7 bps** (±7.9) | `+17.6 bps` | `-0.012 / -0.065` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 12:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,095.43 | ⚪ **CASH** | **-42.3 bps** (±14.7) | `-62.3 bps` | `-0.044 / -0.084` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,903.30 | ⚪ **CASH** | **-38.9 bps** (±6.2) | `-51.2 bps` | `-0.083 / -0.124` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.63 | ⚪ **CASH** | **-3.6 bps** (±10.1) | `+5.9 bps` | `-0.010 / -0.114` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 12:30:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,181.03 | ⚪ **CASH** | **-42.3 bps** (±14.7) | `-62.3 bps` | `-0.044 / -0.084` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,907.89 | ⚪ **CASH** | **-38.9 bps** (±6.2) | `-51.2 bps` | `-0.083 / -0.124` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.85 | ⚪ **CASH** | **-3.6 bps** (±10.1) | `+5.9 bps` | `-0.010 / -0.114` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 12:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,183.30 | ⚪ **CASH** | **-42.3 bps** (±14.7) | `-62.3 bps` | `-0.044 / -0.084` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,907.08 | ⚪ **CASH** | **-38.9 bps** (±6.2) | `-51.2 bps` | `-0.083 / -0.124` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.77 | ⚪ **CASH** | **-3.6 bps** (±10.1) | `+5.9 bps` | `-0.010 / -0.114` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 12:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,292.01 | ⚪ **CASH** | **-42.3 bps** (±14.7) | `-62.3 bps` | `-0.044 / -0.084` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,910.83 | ⚪ **CASH** | **-38.9 bps** (±6.2) | `-51.2 bps` | `-0.083 / -0.124` | `0.63%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $76.04 | ⚪ **CASH** | **-3.6 bps** (±10.1) | `+5.9 bps` | `-0.010 / -0.114` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-14 11:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,238.00 | ⚪ **CASH** | **-43.4 bps** (±13.7) | `-64.7 bps` | `-0.044 / -0.082` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,909.63 | ⚪ **CASH** | **-36.4 bps** (±5.6) | `-49.2 bps` | `-0.075 / -0.098` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.95 | ⚪ **CASH** | **-1.4 bps** (±9.6) | `+8.9 bps` | `-0.012 / -0.098` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-14 11:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,211.40 | ⚪ **CASH** | **-43.4 bps** (±13.7) | `-64.7 bps` | `-0.044 / -0.082` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,907.11 | ⚪ **CASH** | **-36.4 bps** (±5.6) | `-49.2 bps` | `-0.075 / -0.098` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.74 | ⚪ **CASH** | **-1.4 bps** (±9.6) | `+8.9 bps` | `-0.012 / -0.098` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-14 11:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,252.50 | ⚪ **CASH** | **-43.4 bps** (±13.7) | `-64.7 bps` | `-0.044 / -0.082` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,907.39 | ⚪ **CASH** | **-36.4 bps** (±5.6) | `-49.2 bps` | `-0.075 / -0.098` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.85 | ⚪ **CASH** | **-1.4 bps** (±9.6) | `+8.9 bps` | `-0.012 / -0.098` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-14 11:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,294.72 | ⚪ **CASH** | **-43.4 bps** (±13.7) | `-64.7 bps` | `-0.044 / -0.082` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,909.55 | ⚪ **CASH** | **-36.4 bps** (±5.6) | `-49.2 bps` | `-0.075 / -0.098` | `0.64%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.79 | ⚪ **CASH** | **-1.4 bps** (±9.6) | `+8.9 bps` | `-0.012 / -0.098` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-14 10:45:35 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,266.91 | ⚪ **CASH** | **-48.0 bps** (±17.5) | `-75.0 bps` | `-0.041 / -0.047` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,909.38 | ⚪ **CASH** | **-31.3 bps** (±6.1) | `-43.9 bps` | `-0.068 / -0.049` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.78 | ⚪ **CASH** | **-0.1 bps** (±8.8) | `+7.3 bps` | `-0.009 / -0.045` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.4 bps) |

---

### 🕒 Ciclo `2026-11-14 10:30:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,282.90 | ⚪ **CASH** | **-48.0 bps** (±17.5) | `-75.0 bps` | `-0.041 / -0.047` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,909.60 | ⚪ **CASH** | **-31.3 bps** (±6.1) | `-43.9 bps` | `-0.068 / -0.049` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.82 | ⚪ **CASH** | **-0.1 bps** (±8.8) | `+7.3 bps` | `-0.009 / -0.045` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.4 bps) |

---

### 🕒 Ciclo `2026-11-14 10:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,232.00 | ⚪ **CASH** | **-48.0 bps** (±17.5) | `-75.0 bps` | `-0.041 / -0.047` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,907.01 | ⚪ **CASH** | **-31.3 bps** (±6.1) | `-43.9 bps` | `-0.068 / -0.049` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.77 | ⚪ **CASH** | **-0.1 bps** (±8.8) | `+7.3 bps` | `-0.009 / -0.045` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.4 bps) |

---

### 🕒 Ciclo `2026-11-14 10:00:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,390.00 | ⚪ **CASH** | **-48.0 bps** (±17.5) | `-75.0 bps` | `-0.041 / -0.047` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,912.13 | ⚪ **CASH** | **-31.3 bps** (±6.1) | `-43.9 bps` | `-0.068 / -0.049` | `0.65%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.90 | ⚪ **CASH** | **-0.1 bps** (±8.8) | `+7.3 bps` | `-0.009 / -0.045` | `0.75%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.4 bps) |

---

### 🕒 Ciclo `2026-11-14 09:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,196.00 | ⚪ **CASH** | **-41.7 bps** (±16.9) | `-61.1 bps` | `-0.048 / -0.072` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.3 bps) |
| **ETHUSDT** | $1,909.79 | ⚪ **CASH** | **-37.3 bps** (±18.8) | `-46.1 bps` | `-0.073 / -0.133` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.5 bps) |
| **SOLUSDT** | $75.75 | ⚪ **CASH** | **-4.2 bps** (±4.6) | `+1.7 bps` | `-0.018 / -0.068` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.2 bps) |

---

### 🕒 Ciclo `2026-11-14 09:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,194.00 | ⚪ **CASH** | **-41.7 bps** (±16.9) | `-61.1 bps` | `-0.048 / -0.072` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.3 bps) |
| **ETHUSDT** | $1,906.82 | ⚪ **CASH** | **-37.3 bps** (±18.8) | `-46.1 bps` | `-0.073 / -0.133` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.5 bps) |
| **SOLUSDT** | $75.73 | ⚪ **CASH** | **-4.2 bps** (±4.6) | `+1.7 bps` | `-0.018 / -0.068` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.2 bps) |

---

### 🕒 Ciclo `2026-11-14 09:15:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,155.68 | ⚪ **CASH** | **-41.7 bps** (±16.9) | `-61.1 bps` | `-0.048 / -0.072` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.3 bps) |
| **ETHUSDT** | $1,903.36 | ⚪ **CASH** | **-37.3 bps** (±18.8) | `-46.1 bps` | `-0.073 / -0.133` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.5 bps) |
| **SOLUSDT** | $75.55 | ⚪ **CASH** | **-4.2 bps** (±4.6) | `+1.7 bps` | `-0.018 / -0.068` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.2 bps) |

---

### 🕒 Ciclo `2026-11-14 09:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,003.12 | ⚪ **CASH** | **-41.7 bps** (±16.9) | `-61.1 bps` | `-0.048 / -0.072` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.3 bps) |
| **ETHUSDT** | $1,895.32 | ⚪ **CASH** | **-37.3 bps** (±18.8) | `-46.1 bps` | `-0.073 / -0.133` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.5 bps) |
| **SOLUSDT** | $75.27 | ⚪ **CASH** | **-4.2 bps** (±4.6) | `+1.7 bps` | `-0.018 / -0.068` | `0.74%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.2 bps) |
