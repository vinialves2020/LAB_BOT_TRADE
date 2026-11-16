# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-16 14:15:59 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-16 14:15:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,578.44 | ⚪ **CASH** | **+17.3 bps** (±18.7) | `+57.1 bps` | `-0.117 / -0.078` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,824.47 | ⚪ **CASH** | **-47.6 bps** (±14.6) | `-67.4 bps` | `-0.101 / -0.015` | `0.89%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.40 | ⚪ **CASH** | **-18.0 bps** (±24.2) | `-6.8 bps` | `-0.110 / -0.076` | `1.01%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 14:01:03 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,171.04 | ⚪ **CASH** | **+17.3 bps** (±18.7) | `+57.1 bps` | `-0.117 / -0.078` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,804.47 | ⚪ **CASH** | **-47.6 bps** (±14.6) | `-67.4 bps` | `-0.101 / -0.015` | `0.89%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $70.83 | ⚪ **CASH** | **-18.0 bps** (±24.2) | `-6.8 bps` | `-0.110 / -0.076` | `1.01%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 13:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,406.46 | ⚪ **CASH** | **+16.9 bps** (±16.2) | `+54.8 bps` | `-0.117 / -0.060` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,805.53 | ⚪ **CASH** | **-48.6 bps** (±13.3) | `-68.5 bps` | `-0.103 / -0.025` | `0.91%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.05 | ⚪ **CASH** | **-21.7 bps** (±28.9) | `-11.3 bps` | `-0.101 / -0.110` | `1.02%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 13:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,340.96 | ⚪ **CASH** | **+16.9 bps** (±16.2) | `+54.8 bps` | `-0.117 / -0.060` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,805.41 | ⚪ **CASH** | **-48.6 bps** (±13.3) | `-68.5 bps` | `-0.103 / -0.025` | `0.91%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.14 | ⚪ **CASH** | **-21.7 bps** (±28.9) | `-11.3 bps` | `-0.101 / -0.110` | `1.02%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 13:16:02 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,294.84 | ⚪ **CASH** | **+16.9 bps** (±16.2) | `+54.8 bps` | `-0.117 / -0.060` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,805.61 | ⚪ **CASH** | **-48.6 bps** (±13.3) | `-68.5 bps` | `-0.103 / -0.025` | `0.91%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.10 | ⚪ **CASH** | **-21.7 bps** (±28.9) | `-11.3 bps` | `-0.101 / -0.110` | `1.02%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 13:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,217.70 | ⚪ **CASH** | **+16.9 bps** (±16.2) | `+54.8 bps` | `-0.117 / -0.060` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,800.99 | ⚪ **CASH** | **-48.6 bps** (±13.3) | `-68.5 bps` | `-0.103 / -0.025` | `0.91%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $70.76 | ⚪ **CASH** | **-21.7 bps** (±28.9) | `-11.3 bps` | `-0.101 / -0.110` | `1.02%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 12:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,268.87 | ⚪ **CASH** | **+20.5 bps** (±16.3) | `+63.2 bps` | `-0.124 / -0.075` | `0.72%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,799.81 | ⚪ **CASH** | **-29.8 bps** (±11.7) | `-33.1 bps` | `-0.102 / -0.045` | `0.92%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $70.83 | ⚪ **CASH** | **-26.3 bps** (±9.3) | `-13.2 bps` | `-0.101 / -0.259` | `1.03%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 12:31:04 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,962.32 | ⚪ **CASH** | **+20.5 bps** (±16.3) | `+63.2 bps` | `-0.124 / -0.075` | `0.72%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,789.63 | ⚪ **CASH** | **-29.8 bps** (±11.7) | `-33.1 bps` | `-0.102 / -0.045` | `0.92%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $70.62 | ⚪ **CASH** | **-26.3 bps** (±9.3) | `-13.2 bps` | `-0.101 / -0.259` | `1.03%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 12:15:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,062.38 | ⚪ **CASH** | **+20.5 bps** (±16.3) | `+63.2 bps` | `-0.124 / -0.075` | `0.72%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,796.83 | ⚪ **CASH** | **-29.8 bps** (±11.7) | `-33.1 bps` | `-0.102 / -0.045` | `0.92%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $70.87 | ⚪ **CASH** | **-26.3 bps** (±9.3) | `-13.2 bps` | `-0.101 / -0.259` | `1.03%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 11:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,557.80 | ⚪ **CASH** | **+23.0 bps** (±18.1) | `+63.7 bps` | `-0.113 / -0.029` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.8 bps) |
| **ETHUSDT** | $1,808.10 | ⚪ **CASH** | **-25.1 bps** (±16.2) | `-22.6 bps` | `-0.107 / -0.060` | `0.93%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.53 | ⚪ **CASH** | **-31.2 bps** (±22.4) | `-16.0 bps` | `-0.098 / -0.328` | `1.04%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 11:30:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,683.06 | ⚪ **CASH** | **+23.0 bps** (±18.1) | `+63.7 bps` | `-0.113 / -0.029` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.8 bps) |
| **ETHUSDT** | $1,810.24 | ⚪ **CASH** | **-25.1 bps** (±16.2) | `-22.6 bps` | `-0.107 / -0.060` | `0.93%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.55 | ⚪ **CASH** | **-31.2 bps** (±22.4) | `-16.0 bps` | `-0.098 / -0.328` | `1.04%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 11:15:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,653.29 | ⚪ **CASH** | **+23.0 bps** (±18.1) | `+63.7 bps` | `-0.113 / -0.029` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.8 bps) |
| **ETHUSDT** | $1,810.86 | ⚪ **CASH** | **-25.1 bps** (±16.2) | `-22.6 bps` | `-0.107 / -0.060` | `0.93%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.67 | ⚪ **CASH** | **-31.2 bps** (±22.4) | `-16.0 bps` | `-0.098 / -0.328` | `1.04%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 11:01:02 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,608.40 | ⚪ **CASH** | **+23.0 bps** (±18.1) | `+63.7 bps` | `-0.113 / -0.029` | `0.73%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.8 bps) |
| **ETHUSDT** | $1,809.96 | ⚪ **CASH** | **-25.1 bps** (±16.2) | `-22.6 bps` | `-0.107 / -0.060` | `0.93%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.74 | ⚪ **CASH** | **-31.2 bps** (±22.4) | `-16.0 bps` | `-0.098 / -0.328` | `1.04%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 10:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,535.45 | ⚪ **CASH** | **+14.8 bps** (±21.1) | `+48.1 bps` | `-0.108 / -0.023` | `0.74%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.1 bps > 19.5) |
| **ETHUSDT** | $1,806.21 | ⚪ **CASH** | **-69.2 bps** (±12.7) | `-100.8 bps` | `-0.107 / -0.105` | `0.94%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.46 | ⚪ **CASH** | **-34.0 bps** (±25.6) | `-20.7 bps` | `-0.093 / -0.336` | `1.03%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 10:30:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,573.24 | ⚪ **CASH** | **+14.8 bps** (±21.1) | `+48.1 bps` | `-0.108 / -0.023` | `0.74%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.1 bps > 19.5) |
| **ETHUSDT** | $1,806.10 | ⚪ **CASH** | **-69.2 bps** (±12.7) | `-100.8 bps` | `-0.107 / -0.105` | `0.94%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.35 | ⚪ **CASH** | **-34.0 bps** (±25.6) | `-20.7 bps` | `-0.093 / -0.336` | `1.03%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 10:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,478.01 | ⚪ **CASH** | **+14.8 bps** (±21.1) | `+48.1 bps` | `-0.108 / -0.023` | `0.74%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.1 bps > 19.5) |
| **ETHUSDT** | $1,802.75 | ⚪ **CASH** | **-69.2 bps** (±12.7) | `-100.8 bps` | `-0.107 / -0.105` | `0.94%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.12 | ⚪ **CASH** | **-34.0 bps** (±25.6) | `-20.7 bps` | `-0.093 / -0.336` | `1.03%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 10:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,374.26 | ⚪ **CASH** | **+14.8 bps** (±21.1) | `+48.1 bps` | `-0.108 / -0.023` | `0.74%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.1 bps > 19.5) |
| **ETHUSDT** | $1,800.06 | ⚪ **CASH** | **-69.2 bps** (±12.7) | `-100.8 bps` | `-0.107 / -0.105` | `0.94%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.01 | ⚪ **CASH** | **-34.0 bps** (±25.6) | `-20.7 bps` | `-0.093 / -0.336` | `1.03%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 09:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,364.59 | ⚪ **CASH** | **+18.5 bps** (±22.1) | `+52.5 bps` | `-0.093 / -0.018` | `0.75%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,796.73 | ⚪ **CASH** | **-16.2 bps** (±14.0) | `-7.0 bps` | `-0.088 / -0.104` | `0.95%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $70.84 | ⚪ **CASH** | **-22.0 bps** (±17.5) | `-1.9 bps` | `-0.086 / -0.335` | `1.04%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 09:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,342.60 | ⚪ **CASH** | **+18.5 bps** (±22.1) | `+52.5 bps` | `-0.093 / -0.018` | `0.75%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,798.14 | ⚪ **CASH** | **-16.2 bps** (±14.0) | `-7.0 bps` | `-0.088 / -0.104` | `0.95%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $70.77 | ⚪ **CASH** | **-22.0 bps** (±17.5) | `-1.9 bps` | `-0.086 / -0.335` | `1.04%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 09:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,144.78 | ⚪ **CASH** | **+18.5 bps** (±22.1) | `+52.5 bps` | `-0.093 / -0.018` | `0.75%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,793.39 | ⚪ **CASH** | **-16.2 bps** (±14.0) | `-7.0 bps` | `-0.088 / -0.104` | `0.95%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $70.49 | ⚪ **CASH** | **-22.0 bps** (±17.5) | `-1.9 bps` | `-0.086 / -0.335` | `1.04%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 09:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,486.94 | ⚪ **CASH** | **+18.5 bps** (±22.1) | `+52.5 bps` | `-0.093 / -0.018` | `0.75%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,806.45 | ⚪ **CASH** | **-16.2 bps** (±14.0) | `-7.0 bps` | `-0.088 / -0.104` | `0.95%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $70.86 | ⚪ **CASH** | **-22.0 bps** (±17.5) | `-1.9 bps` | `-0.086 / -0.335` | `1.04%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 08:53:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,501.93 | ⚪ **CASH** | **+22.5 bps** (±16.0) | `+57.5 bps` | `-0.091 / -0.005` | `0.74%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.1 bps) |
| **ETHUSDT** | $1,806.44 | ⚪ **CASH** | **-23.5 bps** (±13.4) | `-25.3 bps` | `-0.074 / -0.051` | `0.95%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $70.97 | ⚪ **CASH** | **-21.3 bps** (±19.5) | `-4.5 bps` | `-0.078 / -0.283` | `1.05%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 08:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,537.46 | ⚪ **CASH** | **+22.5 bps** (±16.0) | `+57.5 bps` | `-0.091 / -0.005` | `0.74%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.1 bps) |
| **ETHUSDT** | $1,806.20 | ⚪ **CASH** | **-23.5 bps** (±13.4) | `-25.3 bps` | `-0.074 / -0.051` | `0.95%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $70.73 | ⚪ **CASH** | **-21.3 bps** (±19.5) | `-4.5 bps` | `-0.078 / -0.283` | `1.05%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 08:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,717.92 | ⚪ **CASH** | **+22.5 bps** (±16.0) | `+57.5 bps` | `-0.091 / -0.005` | `0.74%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.1 bps) |
| **ETHUSDT** | $1,810.80 | ⚪ **CASH** | **-23.5 bps** (±13.4) | `-25.3 bps` | `-0.074 / -0.051` | `0.95%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $70.98 | ⚪ **CASH** | **-21.3 bps** (±19.5) | `-4.5 bps` | `-0.078 / -0.283` | `1.05%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 08:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,912.33 | ⚪ **CASH** | **+22.5 bps** (±16.0) | `+57.5 bps` | `-0.091 / -0.005` | `0.74%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.1 bps) |
| **ETHUSDT** | $1,818.38 | ⚪ **CASH** | **-23.5 bps** (±13.4) | `-25.3 bps` | `-0.074 / -0.051` | `0.95%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.23 | ⚪ **CASH** | **-21.3 bps** (±19.5) | `-4.5 bps` | `-0.078 / -0.283` | `1.05%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 07:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,902.49 | ⚪ **CASH** | **+24.2 bps** (±9.0) | `+65.8 bps` | `-0.114 / -0.051` | `0.75%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.6 bps) |
| **ETHUSDT** | $1,819.19 | ⚪ **CASH** | **-15.4 bps** (±18.6) | `-8.2 bps` | `-0.073 / -0.055` | `0.96%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.10 | ⚪ **CASH** | **-7.8 bps** (±15.7) | `+17.8 bps` | `-0.074 / -0.247` | `1.07%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |

---

### 🕒 Ciclo `2026-11-16 07:30:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,704.83 | ⚪ **CASH** | **+24.2 bps** (±9.0) | `+65.8 bps` | `-0.114 / -0.051` | `0.75%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.6 bps) |
| **ETHUSDT** | $1,816.60 | ⚪ **CASH** | **-15.4 bps** (±18.6) | `-8.2 bps` | `-0.073 / -0.055` | `0.96%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.17 | ⚪ **CASH** | **-7.8 bps** (±15.7) | `+17.8 bps` | `-0.074 / -0.247` | `1.07%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |

---

### 🕒 Ciclo `2026-11-16 07:15:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,546.30 | ⚪ **CASH** | **+24.2 bps** (±9.0) | `+65.8 bps` | `-0.114 / -0.051` | `0.75%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.6 bps) |
| **ETHUSDT** | $1,810.09 | ⚪ **CASH** | **-15.4 bps** (±18.6) | `-8.2 bps` | `-0.073 / -0.055` | `0.96%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $70.88 | ⚪ **CASH** | **-7.8 bps** (±15.7) | `+17.8 bps` | `-0.074 / -0.247` | `1.07%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |

---

### 🕒 Ciclo `2026-11-16 07:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,778.26 | ⚪ **CASH** | **+24.2 bps** (±9.0) | `+65.8 bps` | `-0.114 / -0.051` | `0.75%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.6 bps) |
| **ETHUSDT** | $1,817.71 | ⚪ **CASH** | **-15.4 bps** (±18.6) | `-8.2 bps` | `-0.073 / -0.055` | `0.96%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.24 | ⚪ **CASH** | **-7.8 bps** (±15.7) | `+17.8 bps` | `-0.074 / -0.247` | `1.07%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.6 bps) |

---

### 🕒 Ciclo `2026-11-16 06:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,640.10 | ⚪ **CASH** | **+18.5 bps** (±16.8) | `+57.5 bps` | `-0.115 / -0.059` | `0.76%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |
| **ETHUSDT** | $1,813.73 | ⚪ **CASH** | **-3.6 bps** (±15.1) | `+14.2 bps` | `-0.086 / -0.061` | `0.98%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |
| **SOLUSDT** | $71.22 | ⚪ **CASH** | **+2.3 bps** (±13.7) | `+26.8 bps` | `-0.060 / -0.132` | `1.09%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.4 bps) |

---

### 🕒 Ciclo `2026-11-16 06:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,514.09 | ⚪ **CASH** | **+18.5 bps** (±16.8) | `+57.5 bps` | `-0.115 / -0.059` | `0.76%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |
| **ETHUSDT** | $1,812.81 | ⚪ **CASH** | **-3.6 bps** (±15.1) | `+14.2 bps` | `-0.086 / -0.061` | `0.98%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |
| **SOLUSDT** | $70.93 | ⚪ **CASH** | **+2.3 bps** (±13.7) | `+26.8 bps` | `-0.060 / -0.132` | `1.09%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.4 bps) |

---

### 🕒 Ciclo `2026-11-16 06:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,335.15 | ⚪ **CASH** | **+18.5 bps** (±16.8) | `+57.5 bps` | `-0.115 / -0.059` | `0.76%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |
| **ETHUSDT** | $1,808.23 | ⚪ **CASH** | **-3.6 bps** (±15.1) | `+14.2 bps` | `-0.086 / -0.061` | `0.98%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |
| **SOLUSDT** | $70.93 | ⚪ **CASH** | **+2.3 bps** (±13.7) | `+26.8 bps` | `-0.060 / -0.132` | `1.09%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.4 bps) |

---

### 🕒 Ciclo `2026-11-16 06:01:03 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,360.51 | ⚪ **CASH** | **+18.5 bps** (±16.8) | `+57.5 bps` | `-0.115 / -0.059` | `0.76%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |
| **ETHUSDT** | $1,810.66 | ⚪ **CASH** | **-3.6 bps** (±15.1) | `+14.2 bps` | `-0.086 / -0.061` | `0.98%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |
| **SOLUSDT** | $71.09 | ⚪ **CASH** | **+2.3 bps** (±13.7) | `+26.8 bps` | `-0.060 / -0.132` | `1.09%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.4 bps) |

---

### 🕒 Ciclo `2026-11-16 05:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,733.12 | ⚪ **CASH** | **+14.1 bps** (±12.4) | `+48.2 bps` | `-0.114 / -0.055` | `0.77%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.6 bps) |
| **ETHUSDT** | $1,815.97 | ⚪ **CASH** | **-12.6 bps** (±21.8) | `+0.3 bps` | `-0.086 / -0.079` | `0.99%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.8 bps > 19.5) |
| **SOLUSDT** | $71.43 | ⚪ **CASH** | **+5.1 bps** (±15.8) | `+24.7 bps` | `-0.051 / -0.030` | `1.10%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.7 bps) |

---

### 🕒 Ciclo `2026-11-16 05:30:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,793.04 | ⚪ **CASH** | **+14.1 bps** (±12.4) | `+48.2 bps` | `-0.114 / -0.055` | `0.77%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.6 bps) |
| **ETHUSDT** | $1,819.57 | ⚪ **CASH** | **-12.6 bps** (±21.8) | `+0.3 bps` | `-0.086 / -0.079` | `0.99%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.8 bps > 19.5) |
| **SOLUSDT** | $71.62 | ⚪ **CASH** | **+5.1 bps** (±15.8) | `+24.7 bps` | `-0.051 / -0.030` | `1.10%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.7 bps) |

---

### 🕒 Ciclo `2026-11-16 05:16:09 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,683.44 | ⚪ **CASH** | **+14.1 bps** (±12.4) | `+48.2 bps` | `-0.114 / -0.055` | `0.77%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.6 bps) |
| **ETHUSDT** | $1,814.43 | ⚪ **CASH** | **-12.6 bps** (±21.8) | `+0.3 bps` | `-0.086 / -0.079` | `0.99%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.8 bps > 19.5) |
| **SOLUSDT** | $71.43 | ⚪ **CASH** | **+5.1 bps** (±15.8) | `+24.7 bps` | `-0.051 / -0.030` | `1.10%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.7 bps) |
