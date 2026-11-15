# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-15 07:30:52 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-11-15 04:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,927.83 | ⚪ **CASH** | **+68.2 bps** (±28.8) | `+138.4 bps` | `-0.060 / -0.005` | `0.93%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.8 bps > 19.5) |
| **ETHUSDT** | $1,821.92 | ⚪ **CASH** | **+51.4 bps** (±33.5) | `+111.6 bps` | `-0.068 / -0.037` | `1.25%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.5 bps > 19.5) |
| **SOLUSDT** | $71.54 | ⚪ **CASH** | **-9.0 bps** (±18.1) | `-4.4 bps` | `-0.049 / -0.015` | `1.33%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |

---

### 🕒 Ciclo `2026-11-15 03:45:33 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,162.46 | ⚪ **CASH** | **+69.1 bps** (±25.8) | `+141.2 bps` | `-0.065 / -0.022` | `0.94%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.8 bps > 19.5) |
| **ETHUSDT** | $1,826.34 | ⚪ **CASH** | **+36.5 bps** (±32.1) | `+87.1 bps` | `-0.083 / -0.057` | `1.26%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (32.1 bps > 19.5) |
| **SOLUSDT** | $71.82 | ⚪ **CASH** | **+7.9 bps** (±23.2) | `+28.4 bps` | `-0.051 / -0.024` | `1.35%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 03:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,911.07 | ⚪ **CASH** | **+69.1 bps** (±25.8) | `+141.2 bps` | `-0.065 / -0.022` | `0.94%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.8 bps > 19.5) |
| **ETHUSDT** | $1,817.04 | ⚪ **CASH** | **+36.5 bps** (±32.1) | `+87.1 bps` | `-0.083 / -0.057` | `1.26%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (32.1 bps > 19.5) |
| **SOLUSDT** | $71.23 | ⚪ **CASH** | **+7.9 bps** (±23.2) | `+28.4 bps` | `-0.051 / -0.024` | `1.35%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 03:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,208.33 | ⚪ **CASH** | **+69.1 bps** (±25.8) | `+141.2 bps` | `-0.065 / -0.022` | `0.94%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.8 bps > 19.5) |
| **ETHUSDT** | $1,823.70 | ⚪ **CASH** | **+36.5 bps** (±32.1) | `+87.1 bps` | `-0.083 / -0.057` | `1.26%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (32.1 bps > 19.5) |
| **SOLUSDT** | $71.82 | ⚪ **CASH** | **+7.9 bps** (±23.2) | `+28.4 bps` | `-0.051 / -0.024` | `1.35%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 03:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,055.99 | ⚪ **CASH** | **+69.1 bps** (±25.8) | `+141.2 bps` | `-0.065 / -0.022` | `0.94%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.8 bps > 19.5) |
| **ETHUSDT** | $1,820.16 | ⚪ **CASH** | **+36.5 bps** (±32.1) | `+87.1 bps` | `-0.083 / -0.057` | `1.26%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (32.1 bps > 19.5) |
| **SOLUSDT** | $71.52 | ⚪ **CASH** | **+7.9 bps** (±23.2) | `+28.4 bps` | `-0.051 / -0.024` | `1.35%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 02:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,785.29 | ⚪ **CASH** | **-2.5 bps** (±40.2) | `+18.3 bps` | `-0.080 / -0.057` | `0.66%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (40.2 bps > 19.5) |
| **ETHUSDT** | $1,811.09 | ⚪ **CASH** | **+11.1 bps** (±35.5) | `+50.4 bps` | `-0.114 / -0.134` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (35.5 bps > 19.5) |
| **SOLUSDT** | $71.13 | ⚪ **CASH** | **+1.1 bps** (±46.4) | `+25.9 bps` | `-0.066 / -0.078` | `0.97%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 02:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,522.75 | ⚪ **CASH** | **-2.5 bps** (±40.2) | `+18.3 bps` | `-0.080 / -0.057` | `0.66%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (40.2 bps > 19.5) |
| **ETHUSDT** | $1,803.90 | ⚪ **CASH** | **+11.1 bps** (±35.5) | `+50.4 bps` | `-0.114 / -0.134` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (35.5 bps > 19.5) |
| **SOLUSDT** | $70.67 | ⚪ **CASH** | **+1.1 bps** (±46.4) | `+25.9 bps` | `-0.066 / -0.078` | `0.97%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 02:15:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,970.01 | ⚪ **CASH** | **-2.5 bps** (±40.2) | `+18.3 bps` | `-0.080 / -0.057` | `0.66%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (40.2 bps > 19.5) |
| **ETHUSDT** | $1,780.19 | ⚪ **CASH** | **+11.1 bps** (±35.5) | `+50.4 bps` | `-0.114 / -0.134` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (35.5 bps > 19.5) |
| **SOLUSDT** | $70.21 | ⚪ **CASH** | **+1.1 bps** (±46.4) | `+25.9 bps` | `-0.066 / -0.078` | `0.97%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 02:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,819.18 | ⚪ **CASH** | **-2.5 bps** (±40.2) | `+18.3 bps` | `-0.080 / -0.057` | `0.66%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (40.2 bps > 19.5) |
| **ETHUSDT** | $1,734.40 | ⚪ **CASH** | **+11.1 bps** (±35.5) | `+50.4 bps` | `-0.114 / -0.134` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (35.5 bps > 19.5) |
| **SOLUSDT** | $68.08 | ⚪ **CASH** | **+1.1 bps** (±46.4) | `+25.9 bps` | `-0.066 / -0.078` | `0.97%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 01:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,098.35 | ⚪ **CASH** | **+6.4 bps** (±22.5) | `+26.7 bps` | `-0.070 / -0.012` | `0.64%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.5 bps > 19.5) |
| **ETHUSDT** | $1,714.87 | ⚪ **CASH** | **+8.8 bps** (±36.6) | `+45.9 bps` | `-0.113 / -0.134` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |
| **SOLUSDT** | $67.53 | ⚪ **CASH** | **-21.5 bps** (±48.4) | `-15.5 bps` | `-0.064 / -0.079` | `0.92%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (48.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 01:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,536.43 | ⚪ **CASH** | **+6.4 bps** (±22.5) | `+26.7 bps` | `-0.070 / -0.012` | `0.64%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.5 bps > 19.5) |
| **ETHUSDT** | $1,724.35 | ⚪ **CASH** | **+8.8 bps** (±36.6) | `+45.9 bps` | `-0.113 / -0.134` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |
| **SOLUSDT** | $68.44 | ⚪ **CASH** | **-21.5 bps** (±48.4) | `-15.5 bps` | `-0.064 / -0.079` | `0.92%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (48.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 01:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,781.00 | ⚪ **CASH** | **+6.4 bps** (±22.5) | `+26.7 bps` | `-0.070 / -0.012` | `0.64%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.5 bps > 19.5) |
| **ETHUSDT** | $1,729.44 | ⚪ **CASH** | **+8.8 bps** (±36.6) | `+45.9 bps` | `-0.113 / -0.134` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |
| **SOLUSDT** | $69.03 | ⚪ **CASH** | **-21.5 bps** (±48.4) | `-15.5 bps` | `-0.064 / -0.079` | `0.92%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (48.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 01:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,420.97 | ⚪ **CASH** | **+6.4 bps** (±22.5) | `+26.7 bps` | `-0.070 / -0.012` | `0.64%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.5 bps > 19.5) |
| **ETHUSDT** | $1,740.37 | ⚪ **CASH** | **+8.8 bps** (±36.6) | `+45.9 bps` | `-0.113 / -0.134` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |
| **SOLUSDT** | $69.38 | ⚪ **CASH** | **-21.5 bps** (±48.4) | `-15.5 bps` | `-0.064 / -0.079` | `0.92%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (48.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 00:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,899.82 | ⚪ **CASH** | **-8.4 bps** (±15.8) | `-0.8 bps` | `-0.072 / -0.014` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,758.86 | ⚪ **CASH** | **+26.9 bps** (±40.4) | `+76.7 bps` | `-0.102 / -0.107` | `0.89%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (40.4 bps > 19.5) |
| **SOLUSDT** | $70.11 | ⚪ **CASH** | **-16.3 bps** (±43.2) | `-9.2 bps` | `-0.055 / -0.057` | `0.92%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (43.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 00:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,747.57 | ⚪ **CASH** | **-8.4 bps** (±15.8) | `-0.8 bps` | `-0.072 / -0.014` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,752.75 | ⚪ **CASH** | **+26.9 bps** (±40.4) | `+76.7 bps` | `-0.102 / -0.107` | `0.89%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (40.4 bps > 19.5) |
| **SOLUSDT** | $69.77 | ⚪ **CASH** | **-16.3 bps** (±43.2) | `-9.2 bps` | `-0.055 / -0.057` | `0.92%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (43.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 00:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,323.07 | ⚪ **CASH** | **-8.4 bps** (±15.8) | `-0.8 bps` | `-0.072 / -0.014` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,769.38 | ⚪ **CASH** | **+26.9 bps** (±40.4) | `+76.7 bps` | `-0.102 / -0.107` | `0.89%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (40.4 bps > 19.5) |
| **SOLUSDT** | $70.37 | ⚪ **CASH** | **-16.3 bps** (±43.2) | `-9.2 bps` | `-0.055 / -0.057` | `0.92%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (43.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 00:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,120.01 | ⚪ **CASH** | **-8.4 bps** (±15.8) | `-0.8 bps` | `-0.072 / -0.014` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,767.44 | ⚪ **CASH** | **+26.9 bps** (±40.4) | `+76.7 bps` | `-0.102 / -0.107` | `0.89%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (40.4 bps > 19.5) |
| **SOLUSDT** | $70.23 | ⚪ **CASH** | **-16.3 bps** (±43.2) | `-9.2 bps` | `-0.055 / -0.057` | `0.92%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (43.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 23:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,897.90 | ⚪ **CASH** | **+5.7 bps** (±22.1) | `+33.2 bps` | `-0.093 / -0.078` | `0.60%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,759.75 | ⚪ **CASH** | **+54.3 bps** (±24.4) | `+124.8 bps` | `-0.106 / -0.103` | `0.85%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.4 bps > 19.5) |
| **SOLUSDT** | $69.91 | ⚪ **CASH** | **-4.0 bps** (±46.4) | `+15.6 bps` | `-0.053 / -0.071` | `0.86%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 23:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,656.14 | ⚪ **CASH** | **+5.7 bps** (±22.1) | `+33.2 bps` | `-0.093 / -0.078` | `0.60%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,745.12 | ⚪ **CASH** | **+54.3 bps** (±24.4) | `+124.8 bps` | `-0.106 / -0.103` | `0.85%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.4 bps > 19.5) |
| **SOLUSDT** | $69.21 | ⚪ **CASH** | **-4.0 bps** (±46.4) | `+15.6 bps` | `-0.053 / -0.071` | `0.86%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 23:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,725.13 | ⚪ **CASH** | **+5.7 bps** (±22.1) | `+33.2 bps` | `-0.093 / -0.078` | `0.60%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,746.27 | ⚪ **CASH** | **+54.3 bps** (±24.4) | `+124.8 bps` | `-0.106 / -0.103` | `0.85%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.4 bps > 19.5) |
| **SOLUSDT** | $69.41 | ⚪ **CASH** | **-4.0 bps** (±46.4) | `+15.6 bps` | `-0.053 / -0.071` | `0.86%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 23:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,703.69 | ⚪ **CASH** | **+5.7 bps** (±22.1) | `+33.2 bps` | `-0.093 / -0.078` | `0.60%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,751.09 | ⚪ **CASH** | **+54.3 bps** (±24.4) | `+124.8 bps` | `-0.106 / -0.103` | `0.85%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.4 bps > 19.5) |
| **SOLUSDT** | $69.43 | ⚪ **CASH** | **-4.0 bps** (±46.4) | `+15.6 bps` | `-0.053 / -0.071` | `0.86%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 22:45:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,884.29 | ⚪ **CASH** | **-25.3 bps** (±33.5) | `-17.4 bps` | `-0.105 / -0.108` | `0.57%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.5 bps > 19.5) |
| **ETHUSDT** | $1,760.83 | ⚪ **CASH** | **+48.2 bps** (±21.5) | `+112.5 bps` | `-0.105 / -0.083` | `0.83%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.5 bps > 19.5) |
| **SOLUSDT** | $69.59 | ⚪ **CASH** | **+10.6 bps** (±46.1) | `+42.7 bps` | `-0.055 / -0.070` | `0.86%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.1 bps > 19.5) |
