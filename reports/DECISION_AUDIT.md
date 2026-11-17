# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-17 18:31:03 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-17 18:31:03 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,895.78 | ⚪ **CASH** | **+11.2 bps** (±9.4) | `+6.2 bps` | `+0.092 / +0.037` | `0.66%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |
| **ETHUSDT** | $1,798.18 | ⚪ **CASH** | **-19.6 bps** (±8.8) | `-24.3 bps` | `-0.093 / -0.077` | `0.87%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |
| **SOLUSDT** | $72.72 | ⚪ **CASH** | **+13.6 bps** (±12.8) | `+35.9 bps` | `-0.097 / -0.059` | `0.90%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |

---

### 🕒 Ciclo `2026-11-17 18:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,660.71 | ⚪ **CASH** | **+11.2 bps** (±9.4) | `+6.2 bps` | `+0.092 / +0.037` | `0.66%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |
| **ETHUSDT** | $1,784.48 | ⚪ **CASH** | **-19.6 bps** (±8.8) | `-24.3 bps` | `-0.093 / -0.077` | `0.87%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |
| **SOLUSDT** | $72.06 | ⚪ **CASH** | **+13.6 bps** (±12.8) | `+35.9 bps` | `-0.097 / -0.059` | `0.90%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |

---

### 🕒 Ciclo `2026-11-17 18:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,825.65 | ⚪ **CASH** | **+11.2 bps** (±9.4) | `+6.2 bps` | `+0.092 / +0.037` | `0.66%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |
| **ETHUSDT** | $1,787.88 | ⚪ **CASH** | **-19.6 bps** (±8.8) | `-24.3 bps` | `-0.093 / -0.077` | `0.87%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.5 bps) |
| **SOLUSDT** | $72.39 | ⚪ **CASH** | **+13.6 bps** (±12.8) | `+35.9 bps` | `-0.097 / -0.059` | `0.90%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.9 bps) |

---

### 🕒 Ciclo `2026-11-17 17:45:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,781.34 | ⚪ **CASH** | **-2.6 bps** (±5.6) | `-21.6 bps` | `+0.095 / +0.058` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.4 bps) |
| **ETHUSDT** | $1,784.12 | ⚪ **CASH** | **-35.5 bps** (±7.7) | `-52.7 bps` | `-0.101 / -0.079` | `0.88%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.4 bps) |
| **SOLUSDT** | $72.36 | ⚪ **CASH** | **+27.1 bps** (±14.5) | `+61.8 bps` | `-0.108 / -0.060` | `0.91%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.3 bps) |

---

### 🕒 Ciclo `2026-11-17 17:30:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,741.65 | ⚪ **CASH** | **-2.6 bps** (±5.6) | `-21.6 bps` | `+0.095 / +0.058` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.4 bps) |
| **ETHUSDT** | $1,784.03 | ⚪ **CASH** | **-35.5 bps** (±7.7) | `-52.7 bps` | `-0.101 / -0.079` | `0.88%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.4 bps) |
| **SOLUSDT** | $72.26 | ⚪ **CASH** | **+27.1 bps** (±14.5) | `+61.8 bps` | `-0.108 / -0.060` | `0.91%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.3 bps) |

---

### 🕒 Ciclo `2026-11-17 17:15:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,907.15 | ⚪ **CASH** | **-2.6 bps** (±5.6) | `-21.6 bps` | `+0.095 / +0.058` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.4 bps) |
| **ETHUSDT** | $1,787.39 | ⚪ **CASH** | **-35.5 bps** (±7.7) | `-52.7 bps` | `-0.101 / -0.079` | `0.88%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.4 bps) |
| **SOLUSDT** | $72.67 | ⚪ **CASH** | **+27.1 bps** (±14.5) | `+61.8 bps` | `-0.108 / -0.060` | `0.91%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.3 bps) |

---

### 🕒 Ciclo `2026-11-17 17:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,656.07 | ⚪ **CASH** | **-2.6 bps** (±5.6) | `-21.6 bps` | `+0.095 / +0.058` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.4 bps) |
| **ETHUSDT** | $1,776.54 | ⚪ **CASH** | **-35.5 bps** (±7.7) | `-52.7 bps` | `-0.101 / -0.079` | `0.88%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.4 bps) |
| **SOLUSDT** | $71.93 | ⚪ **CASH** | **+27.1 bps** (±14.5) | `+61.8 bps` | `-0.108 / -0.060` | `0.91%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.3 bps) |

---

### 🕒 Ciclo `2026-11-17 16:45:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,795.85 | ⚪ **CASH** | **-1.1 bps** (±10.1) | `-17.4 bps` | `+0.098 / +0.044` | `0.68%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 29.7 bps) |
| **ETHUSDT** | $1,779.09 | ⚪ **CASH** | **-20.6 bps** (±11.4) | `-22.5 bps` | `-0.100 / -0.119` | `0.89%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $72.20 | ⚪ **CASH** | **+1.2 bps** (±10.4) | `+16.2 bps` | `-0.117 / -0.082` | `0.92%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 29.9 bps) |

---

### 🕒 Ciclo `2026-11-17 16:31:01 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,881.66 | ⚪ **CASH** | **-1.1 bps** (±10.1) | `-17.4 bps` | `+0.098 / +0.044` | `0.68%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 29.7 bps) |
| **ETHUSDT** | $1,780.48 | ⚪ **CASH** | **-20.6 bps** (±11.4) | `-22.5 bps` | `-0.100 / -0.119` | `0.89%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $72.43 | ⚪ **CASH** | **+1.2 bps** (±10.4) | `+16.2 bps` | `-0.117 / -0.082` | `0.92%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 29.9 bps) |

---

### 🕒 Ciclo `2026-11-17 16:15:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,192.30 | ⚪ **CASH** | **-1.1 bps** (±10.1) | `-17.4 bps` | `+0.098 / +0.044` | `0.68%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 29.7 bps) |
| **ETHUSDT** | $1,786.20 | ⚪ **CASH** | **-20.6 bps** (±11.4) | `-22.5 bps` | `-0.100 / -0.119` | `0.89%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $72.64 | ⚪ **CASH** | **+1.2 bps** (±10.4) | `+16.2 bps` | `-0.117 / -0.082` | `0.92%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 29.9 bps) |

---

### 🕒 Ciclo `2026-11-17 16:01:02 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,093.07 | ⚪ **CASH** | **-1.1 bps** (±10.1) | `-17.4 bps` | `+0.098 / +0.044` | `0.68%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 29.7 bps) |
| **ETHUSDT** | $1,785.86 | ⚪ **CASH** | **-20.6 bps** (±11.4) | `-22.5 bps` | `-0.100 / -0.119` | `0.89%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $72.55 | ⚪ **CASH** | **+1.2 bps** (±10.4) | `+16.2 bps` | `-0.117 / -0.082` | `0.92%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 29.9 bps) |

---

### 🕒 Ciclo `2026-11-17 15:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,198.11 | ⚪ **CASH** | **-2.0 bps** (±4.8) | `-29.2 bps` | `+0.113 / +0.150` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.7 bps) |
| **ETHUSDT** | $1,780.22 | ⚪ **CASH** | **-15.6 bps** (±10.0) | `-15.7 bps` | `-0.085 / -0.122` | `0.85%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 30.9 bps) |
| **SOLUSDT** | $72.24 | ⚪ **CASH** | **+19.4 bps** (±16.9) | `+45.2 bps` | `-0.106 / -0.030` | `0.87%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 15:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,951.05 | ⚪ **CASH** | **-2.0 bps** (±4.8) | `-29.2 bps` | `+0.113 / +0.150` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.7 bps) |
| **ETHUSDT** | $1,805.87 | ⚪ **CASH** | **-15.6 bps** (±10.0) | `-15.7 bps` | `-0.085 / -0.122` | `0.85%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 30.9 bps) |
| **SOLUSDT** | $73.40 | ⚪ **CASH** | **+19.4 bps** (±16.9) | `+45.2 bps` | `-0.106 / -0.030` | `0.87%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 15:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,576.00 | ⚪ **CASH** | **-2.0 bps** (±4.8) | `-29.2 bps` | `+0.113 / +0.150` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.7 bps) |
| **ETHUSDT** | $1,798.48 | ⚪ **CASH** | **-15.6 bps** (±10.0) | `-15.7 bps` | `-0.085 / -0.122` | `0.85%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 30.9 bps) |
| **SOLUSDT** | $73.14 | ⚪ **CASH** | **+19.4 bps** (±16.9) | `+45.2 bps` | `-0.106 / -0.030` | `0.87%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 15:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,938.01 | ⚪ **CASH** | **-2.0 bps** (±4.8) | `-29.2 bps` | `+0.113 / +0.150` | `0.64%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.7 bps) |
| **ETHUSDT** | $1,811.52 | ⚪ **CASH** | **-15.6 bps** (±10.0) | `-15.7 bps` | `-0.085 / -0.122` | `0.85%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 30.9 bps) |
| **SOLUSDT** | $73.68 | ⚪ **CASH** | **+19.4 bps** (±16.9) | `+45.2 bps` | `-0.106 / -0.030` | `0.87%/h` | `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 14:45:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,052.01 | ⚪ **CASH** | **-1.7 bps** (±9.2) | `-29.4 bps` | `+0.110 / +0.178` | `0.66%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.5 bps) |
| **ETHUSDT** | $1,818.27 | ⚪ **CASH** | **-11.9 bps** (±2.6) | `-10.4 bps` | `-0.065 / -0.150` | `0.86%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.1 bps) |
| **SOLUSDT** | $73.94 | ⚪ **CASH** | **+11.5 bps** (±12.9) | `+33.6 bps` | `-0.113 / -0.072` | `0.89%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 14:30:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,002.01 | ⚪ **CASH** | **-1.7 bps** (±9.2) | `-29.4 bps` | `+0.110 / +0.178` | `0.66%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.5 bps) |
| **ETHUSDT** | $1,823.04 | ⚪ **CASH** | **-11.9 bps** (±2.6) | `-10.4 bps` | `-0.065 / -0.150` | `0.86%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.1 bps) |
| **SOLUSDT** | $73.73 | ⚪ **CASH** | **+11.5 bps** (±12.9) | `+33.6 bps` | `-0.113 / -0.072` | `0.89%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 14:15:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,006.50 | ⚪ **CASH** | **-1.7 bps** (±9.2) | `-29.4 bps` | `+0.110 / +0.178` | `0.66%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.5 bps) |
| **ETHUSDT** | $1,825.67 | ⚪ **CASH** | **-11.9 bps** (±2.6) | `-10.4 bps` | `-0.065 / -0.150` | `0.86%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.1 bps) |
| **SOLUSDT** | $73.88 | ⚪ **CASH** | **+11.5 bps** (±12.9) | `+33.6 bps` | `-0.113 / -0.072` | `0.89%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 14:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,075.51 | ⚪ **CASH** | **-1.7 bps** (±9.2) | `-29.4 bps` | `+0.110 / +0.178` | `0.66%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.5 bps) |
| **ETHUSDT** | $1,827.55 | ⚪ **CASH** | **-11.9 bps** (±2.6) | `-10.4 bps` | `-0.065 / -0.150` | `0.86%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.1 bps) |
| **SOLUSDT** | $73.71 | ⚪ **CASH** | **+11.5 bps** (±12.9) | `+33.6 bps` | `-0.113 / -0.072` | `0.89%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 13:45:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,944.29 | ⚪ **CASH** | **+3.8 bps** (±10.2) | `-24.0 bps` | `+0.120 / +0.232` | `0.66%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.5 bps) |
| **ETHUSDT** | $1,821.52 | ⚪ **CASH** | **+1.0 bps** (±6.9) | `+13.2 bps` | `-0.063 / -0.151` | `0.87%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.3 bps) |
| **SOLUSDT** | $73.39 | ⚪ **CASH** | **+16.2 bps** (±4.5) | `+40.0 bps` | `-0.115 / -0.066` | `0.91%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 13:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,984.00 | ⚪ **CASH** | **+3.8 bps** (±10.2) | `-24.0 bps` | `+0.120 / +0.232` | `0.66%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.5 bps) |
| **ETHUSDT** | $1,822.64 | ⚪ **CASH** | **+1.0 bps** (±6.9) | `+13.2 bps` | `-0.063 / -0.151` | `0.87%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.3 bps) |
| **SOLUSDT** | $73.92 | ⚪ **CASH** | **+16.2 bps** (±4.5) | `+40.0 bps` | `-0.115 / -0.066` | `0.91%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 13:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,075.01 | ⚪ **CASH** | **+3.8 bps** (±10.2) | `-24.0 bps` | `+0.120 / +0.232` | `0.66%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.5 bps) |
| **ETHUSDT** | $1,823.65 | ⚪ **CASH** | **+1.0 bps** (±6.9) | `+13.2 bps` | `-0.063 / -0.151` | `0.87%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.3 bps) |
| **SOLUSDT** | $74.01 | ⚪ **CASH** | **+16.2 bps** (±4.5) | `+40.0 bps` | `-0.115 / -0.066` | `0.91%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 13:01:03 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,076.01 | ⚪ **CASH** | **+3.8 bps** (±10.2) | `-24.0 bps` | `+0.120 / +0.232` | `0.66%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.5 bps) |
| **ETHUSDT** | $1,823.87 | ⚪ **CASH** | **+1.0 bps** (±6.9) | `+13.2 bps` | `-0.063 / -0.151` | `0.87%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.3 bps) |
| **SOLUSDT** | $73.71 | ⚪ **CASH** | **+16.2 bps** (±4.5) | `+40.0 bps` | `-0.115 / -0.066` | `0.91%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 12:45:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,966.33 | ⚪ **CASH** | **+1.1 bps** (±10.0) | `-27.7 bps` | `+0.121 / +0.208` | `0.67%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 32.9 bps) |
| **ETHUSDT** | $1,822.09 | ⚪ **CASH** | **+2.0 bps** (±7.0) | `+14.1 bps` | `-0.056 / -0.146` | `0.89%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.1 bps) |
| **SOLUSDT** | $73.76 | ⚪ **CASH** | **+8.2 bps** (±16.1) | `+30.3 bps` | `-0.120 / -0.101` | `0.92%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 12:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,947.93 | ⚪ **CASH** | **+1.1 bps** (±10.0) | `-27.7 bps` | `+0.121 / +0.208` | `0.67%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 32.9 bps) |
| **ETHUSDT** | $1,817.73 | ⚪ **CASH** | **+2.0 bps** (±7.0) | `+14.1 bps` | `-0.056 / -0.146` | `0.89%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.1 bps) |
| **SOLUSDT** | $73.53 | ⚪ **CASH** | **+8.2 bps** (±16.1) | `+30.3 bps` | `-0.120 / -0.101` | `0.92%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 12:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,837.18 | ⚪ **CASH** | **+1.1 bps** (±10.0) | `-27.7 bps` | `+0.121 / +0.208` | `0.67%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 32.9 bps) |
| **ETHUSDT** | $1,813.35 | ⚪ **CASH** | **+2.0 bps** (±7.0) | `+14.1 bps` | `-0.056 / -0.146` | `0.89%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.1 bps) |
| **SOLUSDT** | $73.13 | ⚪ **CASH** | **+8.2 bps** (±16.1) | `+30.3 bps` | `-0.120 / -0.101` | `0.92%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 12:01:06 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,001.64 | ⚪ **CASH** | **+1.1 bps** (±10.0) | `-27.7 bps` | `+0.121 / +0.208` | `0.67%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 32.9 bps) |
| **ETHUSDT** | $1,821.43 | ⚪ **CASH** | **+2.0 bps** (±7.0) | `+14.1 bps` | `-0.056 / -0.146` | `0.89%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.1 bps) |
| **SOLUSDT** | $73.44 | ⚪ **CASH** | **+8.2 bps** (±16.1) | `+30.3 bps` | `-0.120 / -0.101` | `0.92%/h` | `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-17 11:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,834.70 | ⚪ **CASH** | **+13.6 bps** (±7.6) | `+1.1 bps` | `+0.099 / +0.159` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,816.47 | ⚪ **CASH** | **+18.8 bps** (±7.3) | `+47.2 bps` | `-0.056 / -0.169` | `0.83%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.29 | ⚪ **CASH** | **-0.1 bps** (±12.8) | `+19.0 bps` | `-0.126 / -0.141` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 11:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,442.72 | ⚪ **CASH** | **+13.6 bps** (±7.6) | `+1.1 bps` | `+0.099 / +0.159` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,806.98 | ⚪ **CASH** | **+18.8 bps** (±7.3) | `+47.2 bps` | `-0.056 / -0.169` | `0.83%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.96 | ⚪ **CASH** | **-0.1 bps** (±12.8) | `+19.0 bps` | `-0.126 / -0.141` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 11:15:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,338.01 | ⚪ **CASH** | **+13.6 bps** (±7.6) | `+1.1 bps` | `+0.099 / +0.159` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,800.37 | ⚪ **CASH** | **+18.8 bps** (±7.3) | `+47.2 bps` | `-0.056 / -0.169` | `0.83%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.73 | ⚪ **CASH** | **-0.1 bps** (±12.8) | `+19.0 bps` | `-0.126 / -0.141` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 11:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,157.01 | ⚪ **CASH** | **+13.6 bps** (±7.6) | `+1.1 bps` | `+0.099 / +0.159` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,789.59 | ⚪ **CASH** | **+18.8 bps** (±7.3) | `+47.2 bps` | `-0.056 / -0.169` | `0.83%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.18 | ⚪ **CASH** | **-0.1 bps** (±12.8) | `+19.0 bps` | `-0.126 / -0.141` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 10:45:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,242.01 | ⚪ **CASH** | **+9.5 bps** (±7.1) | `-4.9 bps` | `+0.095 / +0.145` | `0.64%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,791.68 | ⚪ **CASH** | **+14.7 bps** (±6.7) | `+36.5 bps` | `-0.031 / -0.155` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.34 | ⚪ **CASH** | **+0.9 bps** (±5.7) | `+17.0 bps` | `-0.123 / -0.106` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 10:31:01 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,226.00 | ⚪ **CASH** | **+9.5 bps** (±7.1) | `-4.9 bps` | `+0.095 / +0.145` | `0.64%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,793.68 | ⚪ **CASH** | **+14.7 bps** (±6.7) | `+36.5 bps` | `-0.031 / -0.155` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.33 | ⚪ **CASH** | **+0.9 bps** (±5.7) | `+17.0 bps` | `-0.123 / -0.106` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 10:15:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,364.01 | ⚪ **CASH** | **+9.5 bps** (±7.1) | `-4.9 bps` | `+0.095 / +0.145` | `0.64%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,803.15 | ⚪ **CASH** | **+14.7 bps** (±6.7) | `+36.5 bps` | `-0.031 / -0.155` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.52 | ⚪ **CASH** | **+0.9 bps** (±5.7) | `+17.0 bps` | `-0.123 / -0.106` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 10:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,359.17 | ⚪ **CASH** | **+9.5 bps** (±7.1) | `-4.9 bps` | `+0.095 / +0.145` | `0.64%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,811.61 | ⚪ **CASH** | **+14.7 bps** (±6.7) | `+36.5 bps` | `-0.031 / -0.155` | `0.81%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.64 | ⚪ **CASH** | **+0.9 bps** (±5.7) | `+17.0 bps` | `-0.123 / -0.106` | `0.87%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-17 09:45:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,442.56 | ⚪ **CASH** | **+21.7 bps** (±7.6) | `+24.3 bps` | `+0.069 / +0.097` | `0.65%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,815.01 | ⚪ **CASH** | **+19.4 bps** (±9.3) | `+42.1 bps` | `-0.022 / -0.098` | `0.82%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.56 | ⚪ **CASH** | **-0.2 bps** (±9.2) | `+16.1 bps` | `-0.121 / -0.095` | `0.88%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |
