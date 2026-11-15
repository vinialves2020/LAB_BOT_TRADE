# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-15 13:00:53 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-15 13:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,524.01 | ⚪ **CASH** | **+19.4 bps** (±19.4) | `+51.8 bps` | `-0.057 / -0.071` | `0.91%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.8 bps) |
| **ETHUSDT** | $1,835.88 | ⚪ **CASH** | **+83.0 bps** (±17.2) | `+159.3 bps` | `-0.054 / +0.045` | `1.17%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.89 | ⚪ **CASH** | **+23.1 bps** (±17.9) | `+56.7 bps` | `-0.084 / -0.008` | `1.26%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 35.8 bps) |

---

### 🕒 Ciclo `2026-11-15 12:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,488.85 | ⚪ **CASH** | **+12.3 bps** (±13.3) | `+37.5 bps` | `-0.057 / -0.065` | `0.92%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.5 bps) |
| **ETHUSDT** | $1,831.39 | ⚪ **CASH** | **+67.3 bps** (±18.1) | `+135.4 bps` | `-0.057 / -0.018` | `1.18%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.77 | ⚪ **CASH** | **+0.5 bps** (±24.8) | `+20.2 bps` | `-0.084 / -0.057` | `1.26%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 12:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,438.38 | ⚪ **CASH** | **+12.3 bps** (±13.3) | `+37.5 bps` | `-0.057 / -0.065` | `0.92%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.5 bps) |
| **ETHUSDT** | $1,829.91 | ⚪ **CASH** | **+67.3 bps** (±18.1) | `+135.4 bps` | `-0.057 / -0.018` | `1.18%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.68 | ⚪ **CASH** | **+0.5 bps** (±24.8) | `+20.2 bps` | `-0.084 / -0.057` | `1.26%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 12:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,318.00 | ⚪ **CASH** | **+12.3 bps** (±13.3) | `+37.5 bps` | `-0.057 / -0.065` | `0.92%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.5 bps) |
| **ETHUSDT** | $1,826.44 | ⚪ **CASH** | **+67.3 bps** (±18.1) | `+135.4 bps` | `-0.057 / -0.018` | `1.18%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.39 | ⚪ **CASH** | **+0.5 bps** (±24.8) | `+20.2 bps` | `-0.084 / -0.057` | `1.26%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 12:00:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,320.01 | ⚪ **CASH** | **+12.3 bps** (±13.3) | `+37.5 bps` | `-0.057 / -0.065` | `0.92%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.5 bps) |
| **ETHUSDT** | $1,821.72 | ⚪ **CASH** | **+67.3 bps** (±18.1) | `+135.4 bps` | `-0.057 / -0.018` | `1.18%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.27 | ⚪ **CASH** | **+0.5 bps** (±24.8) | `+20.2 bps` | `-0.084 / -0.057` | `1.26%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 11:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,500.01 | ⚪ **CASH** | **+18.4 bps** (±18.1) | `+49.0 bps` | `-0.057 / -0.060` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.8 bps) |
| **ETHUSDT** | $1,832.22 | ⚪ **CASH** | **+75.5 bps** (±18.0) | `+149.5 bps` | `-0.057 / -0.008` | `1.19%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.54 | ⚪ **CASH** | **-9.6 bps** (±14.2) | `+2.4 bps` | `-0.083 / -0.097` | `1.28%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.3 bps) |

---

### 🕒 Ciclo `2026-11-15 11:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,400.01 | ⚪ **CASH** | **+18.4 bps** (±18.1) | `+49.0 bps` | `-0.057 / -0.060` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.8 bps) |
| **ETHUSDT** | $1,831.09 | ⚪ **CASH** | **+75.5 bps** (±18.0) | `+149.5 bps` | `-0.057 / -0.008` | `1.19%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.38 | ⚪ **CASH** | **-9.6 bps** (±14.2) | `+2.4 bps` | `-0.083 / -0.097` | `1.28%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.3 bps) |

---

### 🕒 Ciclo `2026-11-15 11:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,340.00 | ⚪ **CASH** | **+18.4 bps** (±18.1) | `+49.0 bps` | `-0.057 / -0.060` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.8 bps) |
| **ETHUSDT** | $1,828.29 | ⚪ **CASH** | **+75.5 bps** (±18.0) | `+149.5 bps` | `-0.057 / -0.008` | `1.19%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.22 | ⚪ **CASH** | **-9.6 bps** (±14.2) | `+2.4 bps` | `-0.083 / -0.097` | `1.28%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.3 bps) |

---

### 🕒 Ciclo `2026-11-15 11:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,466.01 | ⚪ **CASH** | **+18.4 bps** (±18.1) | `+49.0 bps` | `-0.057 / -0.060` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.8 bps) |
| **ETHUSDT** | $1,828.00 | ⚪ **CASH** | **+75.5 bps** (±18.0) | `+149.5 bps` | `-0.057 / -0.008` | `1.19%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $71.98 | ⚪ **CASH** | **-9.6 bps** (±14.2) | `+2.4 bps` | `-0.083 / -0.097` | `1.28%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.3 bps) |

---

### 🕒 Ciclo `2026-11-15 10:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,536.05 | ⚪ **CASH** | **+25.6 bps** (±21.3) | `+63.3 bps` | `-0.061 / -0.058` | `0.94%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.3 bps > 19.5) |
| **ETHUSDT** | $1,829.21 | ⚪ **CASH** | **+74.0 bps** (±22.8) | `+148.2 bps` | `-0.060 / -0.008` | `1.21%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.8 bps > 19.5) |
| **SOLUSDT** | $72.01 | ⚪ **CASH** | **-19.3 bps** (±4.3) | `-8.8 bps` | `-0.087 / -0.213` | `1.29%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.6 bps) |

---

### 🕒 Ciclo `2026-11-15 10:30:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,476.00 | ⚪ **CASH** | **+25.6 bps** (±21.3) | `+63.3 bps` | `-0.061 / -0.058` | `0.94%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.3 bps > 19.5) |
| **ETHUSDT** | $1,828.03 | ⚪ **CASH** | **+74.0 bps** (±22.8) | `+148.2 bps` | `-0.060 / -0.008` | `1.21%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.8 bps > 19.5) |
| **SOLUSDT** | $71.91 | ⚪ **CASH** | **-19.3 bps** (±4.3) | `-8.8 bps` | `-0.087 / -0.213` | `1.29%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.6 bps) |

---

### 🕒 Ciclo `2026-11-15 10:15:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,601.63 | ⚪ **CASH** | **+25.6 bps** (±21.3) | `+63.3 bps` | `-0.061 / -0.058` | `0.94%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.3 bps > 19.5) |
| **ETHUSDT** | $1,831.01 | ⚪ **CASH** | **+74.0 bps** (±22.8) | `+148.2 bps` | `-0.060 / -0.008` | `1.21%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.8 bps > 19.5) |
| **SOLUSDT** | $72.23 | ⚪ **CASH** | **-19.3 bps** (±4.3) | `-8.8 bps` | `-0.087 / -0.213` | `1.29%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.6 bps) |

---

### 🕒 Ciclo `2026-11-15 10:00:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,343.57 | ⚪ **CASH** | **+25.6 bps** (±21.3) | `+63.3 bps` | `-0.061 / -0.058` | `0.94%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.3 bps > 19.5) |
| **ETHUSDT** | $1,822.61 | ⚪ **CASH** | **+74.0 bps** (±22.8) | `+148.2 bps` | `-0.060 / -0.008` | `1.21%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.8 bps > 19.5) |
| **SOLUSDT** | $71.71 | ⚪ **CASH** | **-19.3 bps** (±4.3) | `-8.8 bps` | `-0.087 / -0.213` | `1.29%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 33.6 bps) |

---

### 🕒 Ciclo `2026-11-15 09:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,408.35 | ⚪ **CASH** | **+34.5 bps** (±26.6) | `+82.1 bps` | `-0.065 / -0.075` | `0.95%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.6 bps > 19.5) |
| **ETHUSDT** | $1,827.31 | ⚪ **CASH** | **+40.8 bps** (±25.3) | `+89.6 bps` | `-0.065 / -0.017` | `1.21%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.3 bps > 19.5) |
| **SOLUSDT** | $71.93 | ⚪ **CASH** | **-51.3 bps** (±33.7) | `-59.1 bps` | `-0.092 / -0.240` | `1.29%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.7 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 09:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,580.59 | ⚪ **CASH** | **+34.5 bps** (±26.6) | `+82.1 bps` | `-0.065 / -0.075` | `0.95%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.6 bps > 19.5) |
| **ETHUSDT** | $1,830.79 | ⚪ **CASH** | **+40.8 bps** (±25.3) | `+89.6 bps` | `-0.065 / -0.017` | `1.21%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.3 bps > 19.5) |
| **SOLUSDT** | $72.08 | ⚪ **CASH** | **-51.3 bps** (±33.7) | `-59.1 bps` | `-0.092 / -0.240` | `1.29%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.7 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 09:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,898.89 | ⚪ **CASH** | **+34.5 bps** (±26.6) | `+82.1 bps` | `-0.065 / -0.075` | `0.95%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.6 bps > 19.5) |
| **ETHUSDT** | $1,838.97 | ⚪ **CASH** | **+40.8 bps** (±25.3) | `+89.6 bps` | `-0.065 / -0.017` | `1.21%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.3 bps > 19.5) |
| **SOLUSDT** | $72.36 | ⚪ **CASH** | **-51.3 bps** (±33.7) | `-59.1 bps` | `-0.092 / -0.240` | `1.29%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.7 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 09:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,221.74 | ⚪ **CASH** | **+34.5 bps** (±26.6) | `+82.1 bps` | `-0.065 / -0.075` | `0.95%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.6 bps > 19.5) |
| **ETHUSDT** | $1,811.50 | ⚪ **CASH** | **+40.8 bps** (±25.3) | `+89.6 bps` | `-0.065 / -0.017` | `1.21%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.3 bps > 19.5) |
| **SOLUSDT** | $71.13 | ⚪ **CASH** | **-51.3 bps** (±33.7) | `-59.1 bps` | `-0.092 / -0.240` | `1.29%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.7 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 08:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,838.67 | ⚪ **CASH** | **+40.3 bps** (±12.7) | `+88.0 bps` | `-0.068 / -0.037` | `0.89%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,803.95 | ⚪ **CASH** | **+88.4 bps** (±14.2) | `+171.8 bps` | `-0.071 / +0.029` | `1.19%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $70.69 | ⚪ **CASH** | **-39.1 bps** (±25.4) | `-43.9 bps` | `-0.096 / -0.150` | `1.27%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 08:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,596.67 | ⚪ **CASH** | **+40.3 bps** (±12.7) | `+88.0 bps` | `-0.068 / -0.037` | `0.89%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,797.91 | ⚪ **CASH** | **+88.4 bps** (±14.2) | `+171.8 bps` | `-0.071 / +0.029` | `1.19%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $70.70 | ⚪ **CASH** | **-39.1 bps** (±25.4) | `-43.9 bps` | `-0.096 / -0.150` | `1.27%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 08:15:34 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,921.68 | ⚪ **CASH** | **+40.3 bps** (±12.7) | `+88.0 bps` | `-0.068 / -0.037` | `0.89%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,779.55 | ⚪ **CASH** | **+88.4 bps** (±14.2) | `+171.8 bps` | `-0.071 / +0.029` | `1.19%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $69.88 | ⚪ **CASH** | **-39.1 bps** (±25.4) | `-43.9 bps` | `-0.096 / -0.150` | `1.27%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 08:00:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,962.57 | ⚪ **CASH** | **+40.3 bps** (±12.7) | `+88.0 bps` | `-0.068 / -0.037` | `0.89%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,781.43 | ⚪ **CASH** | **+88.4 bps** (±14.2) | `+171.8 bps` | `-0.071 / +0.029` | `1.19%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $69.91 | ⚪ **CASH** | **-39.1 bps** (±25.4) | `-43.9 bps` | `-0.096 / -0.150` | `1.27%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 07:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,887.61 | ⚪ **CASH** | **+60.3 bps** (±16.0) | `+125.0 bps` | `-0.061 / -0.053` | `0.90%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,778.86 | ⚪ **CASH** | **+92.3 bps** (±15.2) | `+181.3 bps` | `-0.078 / -0.002` | `1.20%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $69.73 | ⚪ **CASH** | **-24.0 bps** (±9.8) | `-21.3 bps` | `-0.095 / -0.126` | `1.28%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |

---

### 🕒 Ciclo `2026-11-15 07:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,360.44 | ⚪ **CASH** | **+60.3 bps** (±16.0) | `+125.0 bps` | `-0.061 / -0.053` | `0.90%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,791.66 | ⚪ **CASH** | **+92.3 bps** (±15.2) | `+181.3 bps` | `-0.078 / -0.002` | `1.20%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $70.38 | ⚪ **CASH** | **-24.0 bps** (±9.8) | `-21.3 bps` | `-0.095 / -0.126` | `1.28%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |

---

### 🕒 Ciclo `2026-11-15 07:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,481.00 | ⚪ **CASH** | **+60.3 bps** (±16.0) | `+125.0 bps` | `-0.061 / -0.053` | `0.90%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,793.69 | ⚪ **CASH** | **+92.3 bps** (±15.2) | `+181.3 bps` | `-0.078 / -0.002` | `1.20%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $70.39 | ⚪ **CASH** | **-24.0 bps** (±9.8) | `-21.3 bps` | `-0.095 / -0.126` | `1.28%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |

---

### 🕒 Ciclo `2026-11-15 07:00:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,362.03 | ⚪ **CASH** | **+60.3 bps** (±16.0) | `+125.0 bps` | `-0.061 / -0.053` | `0.90%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,787.92 | ⚪ **CASH** | **+92.3 bps** (±15.2) | `+181.3 bps` | `-0.078 / -0.002` | `1.20%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $70.23 | ⚪ **CASH** | **-24.0 bps** (±9.8) | `-21.3 bps` | `-0.095 / -0.126` | `1.28%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |

---

### 🕒 Ciclo `2026-11-15 06:45:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,493.55 | ⚪ **CASH** | **+55.9 bps** (±8.8) | `+115.0 bps` | `-0.059 / -0.047` | `0.91%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,795.12 | ⚪ **CASH** | **+100.9 bps** (±15.2) | `+197.1 bps` | `-0.070 / -0.018` | `1.22%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $70.54 | ⚪ **CASH** | **-35.4 bps** (±29.2) | `-39.2 bps` | `-0.092 / -0.121` | `1.30%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (29.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 06:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,512.61 | ⚪ **CASH** | **+55.9 bps** (±8.8) | `+115.0 bps` | `-0.059 / -0.047` | `0.91%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,796.52 | ⚪ **CASH** | **+100.9 bps** (±15.2) | `+197.1 bps` | `-0.070 / -0.018` | `1.22%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $70.71 | ⚪ **CASH** | **-35.4 bps** (±29.2) | `-39.2 bps` | `-0.092 / -0.121` | `1.30%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (29.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 06:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,284.44 | ⚪ **CASH** | **+55.9 bps** (±8.8) | `+115.0 bps` | `-0.059 / -0.047` | `0.91%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,788.43 | ⚪ **CASH** | **+100.9 bps** (±15.2) | `+197.1 bps` | `-0.070 / -0.018` | `1.22%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $70.15 | ⚪ **CASH** | **-35.4 bps** (±29.2) | `-39.2 bps` | `-0.092 / -0.121` | `1.30%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (29.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 06:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,408.29 | ⚪ **CASH** | **+55.9 bps** (±8.8) | `+115.0 bps` | `-0.059 / -0.047` | `0.91%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,797.23 | ⚪ **CASH** | **+100.9 bps** (±15.2) | `+197.1 bps` | `-0.070 / -0.018` | `1.22%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $70.65 | ⚪ **CASH** | **-35.4 bps** (±29.2) | `-39.2 bps` | `-0.092 / -0.121` | `1.30%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (29.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 05:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,808.01 | ⚪ **CASH** | **+43.8 bps** (±14.0) | `+91.1 bps` | `-0.059 / -0.004` | `0.92%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,806.41 | ⚪ **CASH** | **+53.4 bps** (±19.9) | `+111.4 bps` | `-0.070 / -0.015` | `1.23%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (19.9 bps > 19.5) |
| **SOLUSDT** | $71.10 | ⚪ **CASH** | **-27.7 bps** (±33.3) | `-27.5 bps` | `-0.081 / -0.089` | `1.32%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.3 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 05:30:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,838.27 | ⚪ **CASH** | **+43.8 bps** (±14.0) | `+91.1 bps` | `-0.059 / -0.004` | `0.92%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,808.21 | ⚪ **CASH** | **+53.4 bps** (±19.9) | `+111.4 bps` | `-0.070 / -0.015` | `1.23%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (19.9 bps > 19.5) |
| **SOLUSDT** | $71.01 | ⚪ **CASH** | **-27.7 bps** (±33.3) | `-27.5 bps` | `-0.081 / -0.089` | `1.32%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.3 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 05:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,955.75 | ⚪ **CASH** | **+43.8 bps** (±14.0) | `+91.1 bps` | `-0.059 / -0.004` | `0.92%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,811.74 | ⚪ **CASH** | **+53.4 bps** (±19.9) | `+111.4 bps` | `-0.070 / -0.015` | `1.23%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (19.9 bps > 19.5) |
| **SOLUSDT** | $70.96 | ⚪ **CASH** | **-27.7 bps** (±33.3) | `-27.5 bps` | `-0.081 / -0.089` | `1.32%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.3 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 05:01:04 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,892.89 | ⚪ **CASH** | **+43.8 bps** (±14.0) | `+91.1 bps` | `-0.059 / -0.004` | `0.92%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **ETHUSDT** | $1,811.80 | ⚪ **CASH** | **+53.4 bps** (±19.9) | `+111.4 bps` | `-0.070 / -0.015` | `1.23%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (19.9 bps > 19.5) |
| **SOLUSDT** | $70.77 | ⚪ **CASH** | **-27.7 bps** (±33.3) | `-27.5 bps` | `-0.081 / -0.089` | `1.32%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.3 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 04:45:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,829.47 | ⚪ **CASH** | **+68.2 bps** (±28.8) | `+138.4 bps` | `-0.060 / -0.005` | `0.93%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.8 bps > 19.5) |
| **ETHUSDT** | $1,815.58 | ⚪ **CASH** | **+51.4 bps** (±33.5) | `+111.6 bps` | `-0.068 / -0.037` | `1.25%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.5 bps > 19.5) |
| **SOLUSDT** | $71.04 | ⚪ **CASH** | **-9.0 bps** (±18.1) | `-4.4 bps` | `-0.049 / -0.015` | `1.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |

---

### 🕒 Ciclo `2026-11-15 04:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,914.89 | ⚪ **CASH** | **+68.2 bps** (±28.8) | `+138.4 bps` | `-0.060 / -0.005` | `0.93%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.8 bps > 19.5) |
| **ETHUSDT** | $1,819.01 | ⚪ **CASH** | **+51.4 bps** (±33.5) | `+111.6 bps` | `-0.068 / -0.037` | `1.25%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.5 bps > 19.5) |
| **SOLUSDT** | $71.40 | ⚪ **CASH** | **-9.0 bps** (±18.1) | `-4.4 bps` | `-0.049 / -0.015` | `1.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |

---

### 🕒 Ciclo `2026-11-15 04:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,948.36 | ⚪ **CASH** | **+68.2 bps** (±28.8) | `+138.4 bps` | `-0.060 / -0.005` | `0.93%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.8 bps > 19.5) |
| **ETHUSDT** | $1,821.84 | ⚪ **CASH** | **+51.4 bps** (±33.5) | `+111.6 bps` | `-0.068 / -0.037` | `1.25%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.5 bps > 19.5) |
| **SOLUSDT** | $71.52 | ⚪ **CASH** | **-9.0 bps** (±18.1) | `-4.4 bps` | `-0.049 / -0.015` | `1.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
