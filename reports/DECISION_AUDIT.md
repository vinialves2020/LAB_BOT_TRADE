# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-10 20:00:49 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-10 20:00:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,451.78 | ⚪ **CASH** | **+15.7 bps** (±4.1) | `+22.8 bps` | `+0.044 / -0.000` | `0.51%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,044.06 | ⚪ **CASH** | **-67.1 bps** (±18.0) | `-105.3 bps` | `-0.082 / -0.115` | `0.80%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.91 | ⚪ **CASH** | **+4.9 bps** (±8.0) | `+12.1 bps` | `-0.023 / -0.025` | `0.74%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 19:45:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,404.00 | ⚪ **CASH** | **+14.8 bps** (±4.7) | `+22.7 bps` | `+0.044 / -0.020` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,042.10 | ⚪ **CASH** | **-67.9 bps** (±15.3) | `-107.9 bps` | `-0.082 / -0.103` | `0.81%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.69 | ⚪ **CASH** | **+7.2 bps** (±8.9) | `+16.7 bps` | `-0.019 / -0.036` | `0.75%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 19:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,420.22 | ⚪ **CASH** | **+14.8 bps** (±4.7) | `+22.7 bps` | `+0.044 / -0.020` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,042.43 | ⚪ **CASH** | **-67.9 bps** (±15.3) | `-107.9 bps` | `-0.082 / -0.103` | `0.81%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.69 | ⚪ **CASH** | **+7.2 bps** (±8.9) | `+16.7 bps` | `-0.019 / -0.036` | `0.75%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 19:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,385.21 | ⚪ **CASH** | **+14.8 bps** (±4.7) | `+22.7 bps` | `+0.044 / -0.020` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,042.30 | ⚪ **CASH** | **-67.9 bps** (±15.3) | `-107.9 bps` | `-0.082 / -0.103` | `0.81%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.80 | ⚪ **CASH** | **+7.2 bps** (±8.9) | `+16.7 bps` | `-0.019 / -0.036` | `0.75%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 19:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,474.53 | ⚪ **CASH** | **+14.8 bps** (±4.7) | `+22.7 bps` | `+0.044 / -0.020` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,043.55 | ⚪ **CASH** | **-67.9 bps** (±15.3) | `-107.9 bps` | `-0.082 / -0.103` | `0.81%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.96 | ⚪ **CASH** | **+7.2 bps** (±8.9) | `+16.7 bps` | `-0.019 / -0.036` | `0.75%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 18:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,540.30 | ⚪ **CASH** | **+12.6 bps** (±3.8) | `+18.5 bps` | `+0.045 / -0.023` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,044.60 | ⚪ **CASH** | **-63.5 bps** (±18.8) | `-100.7 bps` | `-0.074 / -0.095` | `0.81%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.10 | ⚪ **CASH** | **+6.7 bps** (±10.1) | `+17.2 bps` | `-0.023 / -0.048` | `0.74%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 18:30:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,332.00 | ⚪ **CASH** | **+12.6 bps** (±3.8) | `+18.5 bps` | `+0.045 / -0.023` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,032.42 | ⚪ **CASH** | **-63.5 bps** (±18.8) | `-100.7 bps` | `-0.074 / -0.095` | `0.81%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.75 | ⚪ **CASH** | **+6.7 bps** (±10.1) | `+17.2 bps` | `-0.023 / -0.048` | `0.74%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 18:15:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,214.10 | ⚪ **CASH** | **+12.6 bps** (±3.8) | `+18.5 bps` | `+0.045 / -0.023` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,026.32 | ⚪ **CASH** | **-63.5 bps** (±18.8) | `-100.7 bps` | `-0.074 / -0.095` | `0.81%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.31 | ⚪ **CASH** | **+6.7 bps** (±10.1) | `+17.2 bps` | `-0.023 / -0.048` | `0.74%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 18:00:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,276.05 | ⚪ **CASH** | **+12.6 bps** (±3.8) | `+18.5 bps` | `+0.045 / -0.023` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,027.95 | ⚪ **CASH** | **-63.5 bps** (±18.8) | `-100.7 bps` | `-0.074 / -0.095` | `0.81%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.29 | ⚪ **CASH** | **+6.7 bps** (±10.1) | `+17.2 bps` | `-0.023 / -0.048` | `0.74%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 17:45:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $72,880.01 | ⚪ **CASH** | **+10.4 bps** (±5.4) | `+15.2 bps` | `+0.041 / -0.022` | `0.52%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,017.30 | ⚪ **CASH** | **-53.6 bps** (±20.0) | `-83.5 bps` | `-0.071 / -0.083` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.94 | ⚪ **CASH** | **+0.2 bps** (±4.7) | `+3.5 bps` | `-0.019 / -0.039` | `0.74%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 17:30:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,098.65 | ⚪ **CASH** | **+10.4 bps** (±5.4) | `+15.2 bps` | `+0.041 / -0.022` | `0.52%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,026.67 | ⚪ **CASH** | **-53.6 bps** (±20.0) | `-83.5 bps` | `-0.071 / -0.083` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.48 | ⚪ **CASH** | **+0.2 bps** (±4.7) | `+3.5 bps` | `-0.019 / -0.039` | `0.74%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 17:15:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,036.32 | ⚪ **CASH** | **+10.4 bps** (±5.4) | `+15.2 bps` | `+0.041 / -0.022` | `0.52%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,024.10 | ⚪ **CASH** | **-53.6 bps** (±20.0) | `-83.5 bps` | `-0.071 / -0.083` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.30 | ⚪ **CASH** | **+0.2 bps** (±4.7) | `+3.5 bps` | `-0.019 / -0.039` | `0.74%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 17:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $72,973.51 | ⚪ **CASH** | **+10.4 bps** (±5.4) | `+15.2 bps` | `+0.041 / -0.022` | `0.52%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,021.19 | ⚪ **CASH** | **-53.6 bps** (±20.0) | `-83.5 bps` | `-0.071 / -0.083` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.06 | ⚪ **CASH** | **+0.2 bps** (±4.7) | `+3.5 bps` | `-0.019 / -0.039` | `0.74%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 16:45:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,019.20 | ⚪ **CASH** | **+11.7 bps** (±6.9) | `+15.6 bps` | `+0.057 / -0.023` | `0.52%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,019.30 | ⚪ **CASH** | **-23.2 bps** (±12.9) | `-33.5 bps` | `-0.053 / -0.058` | `0.82%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.08 | ⚪ **CASH** | **+8.4 bps** (±9.3) | `+21.1 bps` | `-0.020 / -0.075` | `0.75%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 16:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,210.20 | ⚪ **CASH** | **+11.7 bps** (±6.9) | `+15.6 bps` | `+0.057 / -0.023` | `0.52%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,024.79 | ⚪ **CASH** | **-23.2 bps** (±12.9) | `-33.5 bps` | `-0.053 / -0.058` | `0.82%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.17 | ⚪ **CASH** | **+8.4 bps** (±9.3) | `+21.1 bps` | `-0.020 / -0.075` | `0.75%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 16:15:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,403.42 | ⚪ **CASH** | **+11.7 bps** (±6.9) | `+15.6 bps` | `+0.057 / -0.023` | `0.52%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,032.87 | ⚪ **CASH** | **-23.2 bps** (±12.9) | `-33.5 bps` | `-0.053 / -0.058` | `0.82%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.37 | ⚪ **CASH** | **+8.4 bps** (±9.3) | `+21.1 bps` | `-0.020 / -0.075` | `0.75%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 16:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,361.01 | ⚪ **CASH** | **+11.7 bps** (±6.9) | `+15.6 bps` | `+0.057 / -0.023` | `0.52%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,032.63 | ⚪ **CASH** | **-23.2 bps** (±12.9) | `-33.5 bps` | `-0.053 / -0.058` | `0.82%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.59 | ⚪ **CASH** | **+8.4 bps** (±9.3) | `+21.1 bps` | `-0.020 / -0.075` | `0.75%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 15:45:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,009.40 | ⚪ **CASH** | **-37.6 bps** (±9.0) | `-84.0 bps` | `+0.108 / +0.021` | `0.44%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,014.36 | ⚪ **CASH** | **-17.3 bps** (±6.3) | `-29.6 bps` | `-0.029 / -0.050` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.87 | ⚪ **CASH** | **-1.6 bps** (±4.6) | `+0.6 bps` | `+0.004 / -0.130` | `0.63%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 15:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,064.75 | ⚪ **CASH** | **-37.6 bps** (±9.0) | `-84.0 bps` | `+0.108 / +0.021` | `0.44%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,062.95 | ⚪ **CASH** | **-17.3 bps** (±6.3) | `-29.6 bps` | `-0.029 / -0.050` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.60 | ⚪ **CASH** | **-1.6 bps** (±4.6) | `+0.6 bps` | `+0.004 / -0.130` | `0.63%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 15:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,397.48 | ⚪ **CASH** | **-37.6 bps** (±9.0) | `-84.0 bps` | `+0.108 / +0.021` | `0.44%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,073.85 | ⚪ **CASH** | **-17.3 bps** (±6.3) | `-29.6 bps` | `-0.029 / -0.050` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.41 | ⚪ **CASH** | **-1.6 bps** (±4.6) | `+0.6 bps` | `+0.004 / -0.130` | `0.63%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 15:00:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,582.00 | ⚪ **CASH** | **-37.6 bps** (±9.0) | `-84.0 bps` | `+0.108 / +0.021` | `0.44%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,088.78 | ⚪ **CASH** | **-17.3 bps** (±6.3) | `-29.6 bps` | `-0.029 / -0.050` | `0.67%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.70 | ⚪ **CASH** | **-1.6 bps** (±4.6) | `+0.6 bps` | `+0.004 / -0.130` | `0.63%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 14:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,229.21 | ⚪ **CASH** | **-38.5 bps** (±7.5) | `-87.8 bps` | `+0.116 / +0.031` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,078.31 | ⚪ **CASH** | **-11.0 bps** (±7.4) | `-18.2 bps` | `-0.024 / -0.057` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.29 | ⚪ **CASH** | **-5.6 bps** (±11.8) | `-10.7 bps` | `+0.040 / -0.106` | `0.63%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 14:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,692.46 | ⚪ **CASH** | **-38.5 bps** (±7.5) | `-87.8 bps` | `+0.116 / +0.031` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,062.47 | ⚪ **CASH** | **-11.0 bps** (±7.4) | `-18.2 bps` | `-0.024 / -0.057` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.63 | ⚪ **CASH** | **-5.6 bps** (±11.8) | `-10.7 bps` | `+0.040 / -0.106` | `0.63%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 14:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,917.61 | ⚪ **CASH** | **-38.5 bps** (±7.5) | `-87.8 bps` | `+0.116 / +0.031` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,068.13 | ⚪ **CASH** | **-11.0 bps** (±7.4) | `-18.2 bps` | `-0.024 / -0.057` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.11 | ⚪ **CASH** | **-5.6 bps** (±11.8) | `-10.7 bps` | `+0.040 / -0.106` | `0.63%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 14:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,871.55 | ⚪ **CASH** | **-38.5 bps** (±7.5) | `-87.8 bps` | `+0.116 / +0.031` | `0.42%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,069.87 | ⚪ **CASH** | **-11.0 bps** (±7.4) | `-18.2 bps` | `-0.024 / -0.057` | `0.66%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.30 | ⚪ **CASH** | **-5.6 bps** (±11.8) | `-10.7 bps` | `+0.040 / -0.106` | `0.63%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 13:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,930.26 | ⚪ **CASH** | **-32.1 bps** (±8.0) | `-86.5 bps` | `+0.141 / +0.134` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,070.62 | ⚪ **CASH** | **-4.6 bps** (±3.2) | `-8.9 bps` | `-0.017 / -0.063` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.32 | ⚪ **CASH** | **+6.8 bps** (±6.1) | `+8.2 bps` | `+0.060 / -0.116` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 13:30:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,042.27 | ⚪ **CASH** | **-32.1 bps** (±8.0) | `-86.5 bps` | `+0.141 / +0.134` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,060.84 | ⚪ **CASH** | **-4.6 bps** (±3.2) | `-8.9 bps` | `-0.017 / -0.063` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.77 | ⚪ **CASH** | **+6.8 bps** (±6.1) | `+8.2 bps` | `+0.060 / -0.116` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 13:15:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,308.70 | ⚪ **CASH** | **-32.1 bps** (±8.0) | `-86.5 bps` | `+0.141 / +0.134` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,094.73 | ⚪ **CASH** | **-4.6 bps** (±3.2) | `-8.9 bps` | `-0.017 / -0.063` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.75 | ⚪ **CASH** | **+6.8 bps** (±6.1) | `+8.2 bps` | `+0.060 / -0.116` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 13:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,343.35 | ⚪ **CASH** | **-32.1 bps** (±8.0) | `-86.5 bps` | `+0.141 / +0.134` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,098.30 | ⚪ **CASH** | **-4.6 bps** (±3.2) | `-8.9 bps` | `-0.017 / -0.063` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.95 | ⚪ **CASH** | **+6.8 bps** (±6.1) | `+8.2 bps` | `+0.060 / -0.116` | `0.62%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 12:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,251.20 | ⚪ **CASH** | **-34.0 bps** (±9.4) | `-89.1 bps` | `+0.153 / +0.100` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,090.32 | ⚪ **CASH** | **-21.2 bps** (±5.3) | `-40.1 bps` | `-0.010 / -0.060` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.83 | ⚪ **CASH** | **+3.8 bps** (±6.2) | `+1.3 bps` | `+0.065 / -0.109` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 12:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,219.78 | ⚪ **CASH** | **-34.0 bps** (±9.4) | `-89.1 bps` | `+0.153 / +0.100` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,089.54 | ⚪ **CASH** | **-21.2 bps** (±5.3) | `-40.1 bps` | `-0.010 / -0.060` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.67 | ⚪ **CASH** | **+3.8 bps** (±6.2) | `+1.3 bps` | `+0.065 / -0.109` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 12:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,387.30 | ⚪ **CASH** | **-34.0 bps** (±9.4) | `-89.1 bps` | `+0.153 / +0.100` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,093.89 | ⚪ **CASH** | **-21.2 bps** (±5.3) | `-40.1 bps` | `-0.010 / -0.060` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.84 | ⚪ **CASH** | **+3.8 bps** (±6.2) | `+1.3 bps` | `+0.065 / -0.109` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 12:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,414.78 | ⚪ **CASH** | **-34.0 bps** (±9.4) | `-89.1 bps` | `+0.153 / +0.100` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,094.06 | ⚪ **CASH** | **-21.2 bps** (±5.3) | `-40.1 bps` | `-0.010 / -0.060` | `0.61%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.68 | ⚪ **CASH** | **+3.8 bps** (±6.2) | `+1.3 bps` | `+0.065 / -0.109` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 11:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,391.77 | ⚪ **CASH** | **-39.7 bps** (±9.2) | `-96.0 bps` | `+0.151 / +0.049` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,093.72 | ⚪ **CASH** | **-23.0 bps** (±8.8) | `-42.2 bps` | `-0.009 / -0.071` | `0.62%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.68 | ⚪ **CASH** | **+6.9 bps** (±5.9) | `+7.5 bps` | `+0.069 / -0.124` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 11:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,238.58 | ⚪ **CASH** | **-39.7 bps** (±9.2) | `-96.0 bps` | `+0.151 / +0.049` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,093.86 | ⚪ **CASH** | **-23.0 bps** (±8.8) | `-42.2 bps` | `-0.009 / -0.071` | `0.62%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.47 | ⚪ **CASH** | **+6.9 bps** (±5.9) | `+7.5 bps` | `+0.069 / -0.124` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-10 11:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $74,397.66 | ⚪ **CASH** | **-39.7 bps** (±9.2) | `-96.0 bps` | `+0.151 / +0.049` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,100.28 | ⚪ **CASH** | **-23.0 bps** (±8.8) | `-42.2 bps` | `-0.009 / -0.071` | `0.62%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $84.87 | ⚪ **CASH** | **+6.9 bps** (±5.9) | `+7.5 bps` | `+0.069 / -0.124` | `0.63%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
