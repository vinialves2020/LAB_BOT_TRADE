# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-08 03:31:01 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-08 03:31:01 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,878.59 | ⚪ **CASH** | **+9.8 bps** (±8.2) | `+13.6 bps` | `+0.013 / +0.058` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,237.24 | ⚪ **CASH** | **-37.4 bps** (±17.1) | `-58.2 bps` | `-0.076 / +0.002` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.26 | ⚪ **CASH** | **-8.6 bps** (±12.3) | `-6.7 bps` | `-0.077 / +0.005` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 03:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,913.82 | ⚪ **CASH** | **+9.8 bps** (±8.2) | `+13.6 bps` | `+0.013 / +0.058` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,239.43 | ⚪ **CASH** | **-37.4 bps** (±17.1) | `-58.2 bps` | `-0.076 / +0.002` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.40 | ⚪ **CASH** | **-8.6 bps** (±12.3) | `-6.7 bps` | `-0.077 / +0.005` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 03:00:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,818.00 | ⚪ **CASH** | **+9.8 bps** (±8.2) | `+13.6 bps` | `+0.013 / +0.058` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.38 | ⚪ **CASH** | **-37.4 bps** (±17.1) | `-58.2 bps` | `-0.076 / +0.002` | `0.42%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.22 | ⚪ **CASH** | **-8.6 bps** (±12.3) | `-6.7 bps` | `-0.077 / +0.005` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 02:45:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,700.00 | ⚪ **CASH** | **+9.9 bps** (±9.5) | `+12.9 bps` | `+0.012 / +0.079` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,230.51 | ⚪ **CASH** | **-37.8 bps** (±16.2) | `-59.9 bps` | `-0.075 / +0.012` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $88.91 | ⚪ **CASH** | **-7.0 bps** (±12.1) | `-3.2 bps` | `-0.071 / -0.015` | `0.47%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 02:30:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,734.29 | ⚪ **CASH** | **+9.9 bps** (±9.5) | `+12.9 bps` | `+0.012 / +0.079` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,233.51 | ⚪ **CASH** | **-37.8 bps** (±16.2) | `-59.9 bps` | `-0.075 / +0.012` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.07 | ⚪ **CASH** | **-7.0 bps** (±12.1) | `-3.2 bps` | `-0.071 / -0.015` | `0.47%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 02:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,670.49 | ⚪ **CASH** | **+9.9 bps** (±9.5) | `+12.9 bps` | `+0.012 / +0.079` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,231.22 | ⚪ **CASH** | **-37.8 bps** (±16.2) | `-59.9 bps` | `-0.075 / +0.012` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $88.92 | ⚪ **CASH** | **-7.0 bps** (±12.1) | `-3.2 bps` | `-0.071 / -0.015` | `0.47%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 02:00:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,731.39 | ⚪ **CASH** | **+9.9 bps** (±9.5) | `+12.9 bps` | `+0.012 / +0.079` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.01 | ⚪ **CASH** | **-37.8 bps** (±16.2) | `-59.9 bps` | `-0.075 / +0.012` | `0.43%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.08 | ⚪ **CASH** | **-7.0 bps** (±12.1) | `-3.2 bps` | `-0.071 / -0.015` | `0.47%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 01:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,779.40 | ⚪ **CASH** | **+5.3 bps** (±7.5) | `+9.6 bps` | `-0.006 / +0.033` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.82 | ⚪ **CASH** | **-36.2 bps** (±14.7) | `-57.1 bps` | `-0.074 / +0.024` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.22 | ⚪ **CASH** | **-8.8 bps** (±12.4) | `-4.7 bps` | `-0.068 / -0.032` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 01:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,786.86 | ⚪ **CASH** | **+5.3 bps** (±7.5) | `+9.6 bps` | `-0.006 / +0.033` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.00 | ⚪ **CASH** | **-36.2 bps** (±14.7) | `-57.1 bps` | `-0.074 / +0.024` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.34 | ⚪ **CASH** | **-8.8 bps** (±12.4) | `-4.7 bps` | `-0.068 / -0.032` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 01:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,830.01 | ⚪ **CASH** | **+5.3 bps** (±7.5) | `+9.6 bps` | `-0.006 / +0.033` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.57 | ⚪ **CASH** | **-36.2 bps** (±14.7) | `-57.1 bps` | `-0.074 / +0.024` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.50 | ⚪ **CASH** | **-8.8 bps** (±12.4) | `-4.7 bps` | `-0.068 / -0.032` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 01:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,798.86 | ⚪ **CASH** | **+5.3 bps** (±7.5) | `+9.6 bps` | `-0.006 / +0.033` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.54 | ⚪ **CASH** | **-36.2 bps** (±14.7) | `-57.1 bps` | `-0.074 / +0.024` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.43 | ⚪ **CASH** | **-8.8 bps** (±12.4) | `-4.7 bps` | `-0.068 / -0.032` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 00:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,755.65 | ⚪ **CASH** | **+9.5 bps** (±8.8) | `+11.2 bps` | `+0.020 / +0.073` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.94 | ⚪ **CASH** | **-37.0 bps** (±15.6) | `-60.1 bps` | `-0.076 / +0.031` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.44 | ⚪ **CASH** | **-41.1 bps** (±10.8) | `-67.6 bps` | `-0.063 / +0.003` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 00:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,781.76 | ⚪ **CASH** | **+9.5 bps** (±8.8) | `+11.2 bps` | `+0.020 / +0.073` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,237.44 | ⚪ **CASH** | **-37.0 bps** (±15.6) | `-60.1 bps` | `-0.076 / +0.031` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.49 | ⚪ **CASH** | **-41.1 bps** (±10.8) | `-67.6 bps` | `-0.063 / +0.003` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 00:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,815.15 | ⚪ **CASH** | **+9.5 bps** (±8.8) | `+11.2 bps` | `+0.020 / +0.073` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.51 | ⚪ **CASH** | **-37.0 bps** (±15.6) | `-60.1 bps` | `-0.076 / +0.031` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.68 | ⚪ **CASH** | **-41.1 bps** (±10.8) | `-67.6 bps` | `-0.063 / +0.003` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-08 00:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,846.95 | ⚪ **CASH** | **+9.5 bps** (±8.8) | `+11.2 bps` | `+0.020 / +0.073` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,239.25 | ⚪ **CASH** | **-37.0 bps** (±15.6) | `-60.1 bps` | `-0.076 / +0.031` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.77 | ⚪ **CASH** | **-41.1 bps** (±10.8) | `-67.6 bps` | `-0.063 / +0.003` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 23:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,874.01 | ⚪ **CASH** | **+5.3 bps** (±8.1) | `+9.6 bps` | `-0.005 / +0.035` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,238.43 | ⚪ **CASH** | **-20.5 bps** (±7.5) | `-26.7 bps` | `-0.068 / -0.036` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.73 | ⚪ **CASH** | **-60.0 bps** (±8.6) | `-105.2 bps` | `-0.059 / +0.058` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 23:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,790.43 | ⚪ **CASH** | **+5.3 bps** (±8.1) | `+9.6 bps` | `-0.005 / +0.035` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.34 | ⚪ **CASH** | **-20.5 bps** (±7.5) | `-26.7 bps` | `-0.068 / -0.036` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.48 | ⚪ **CASH** | **-60.0 bps** (±8.6) | `-105.2 bps` | `-0.059 / +0.058` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 23:15:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,760.34 | ⚪ **CASH** | **+5.3 bps** (±8.1) | `+9.6 bps` | `-0.005 / +0.035` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.20 | ⚪ **CASH** | **-20.5 bps** (±7.5) | `-26.7 bps` | `-0.068 / -0.036` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.38 | ⚪ **CASH** | **-60.0 bps** (±8.6) | `-105.2 bps` | `-0.059 / +0.058` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 23:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,743.96 | ⚪ **CASH** | **+5.3 bps** (±8.1) | `+9.6 bps` | `-0.005 / +0.035` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,233.69 | ⚪ **CASH** | **-20.5 bps** (±7.5) | `-26.7 bps` | `-0.068 / -0.036` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.23 | ⚪ **CASH** | **-60.0 bps** (±8.6) | `-105.2 bps` | `-0.059 / +0.058` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 22:45:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,797.24 | ⚪ **CASH** | **+6.9 bps** (±5.6) | `+12.3 bps` | `+0.012 / -0.009` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.51 | ⚪ **CASH** | **-4.9 bps** (±7.8) | `+1.6 bps` | `-0.049 / -0.073` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.31 | ⚪ **CASH** | **-55.8 bps** (±8.1) | `-96.7 bps` | `-0.055 / +0.022` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 22:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,758.45 | ⚪ **CASH** | **+6.9 bps** (±5.6) | `+12.3 bps` | `+0.012 / -0.009` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.13 | ⚪ **CASH** | **-4.9 bps** (±7.8) | `+1.6 bps` | `-0.049 / -0.073` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.32 | ⚪ **CASH** | **-55.8 bps** (±8.1) | `-96.7 bps` | `-0.055 / +0.022` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 22:15:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,753.33 | ⚪ **CASH** | **+6.9 bps** (±5.6) | `+12.3 bps` | `+0.012 / -0.009` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,232.58 | ⚪ **CASH** | **-4.9 bps** (±7.8) | `+1.6 bps` | `-0.049 / -0.073` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.22 | ⚪ **CASH** | **-55.8 bps** (±8.1) | `-96.7 bps` | `-0.055 / +0.022` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 22:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,763.26 | ⚪ **CASH** | **+6.9 bps** (±5.6) | `+12.3 bps` | `+0.012 / -0.009` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,233.03 | ⚪ **CASH** | **-4.9 bps** (±7.8) | `+1.6 bps` | `-0.049 / -0.073` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.23 | ⚪ **CASH** | **-55.8 bps** (±8.1) | `-96.7 bps` | `-0.055 / +0.022` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 21:45:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,698.01 | ⚪ **CASH** | **+11.4 bps** (±7.4) | `+20.4 bps` | `+0.021 / -0.022` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,230.00 | ⚪ **CASH** | **-0.1 bps** (±6.8) | `+11.9 bps` | `-0.038 / -0.124` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.15 | ⚪ **CASH** | **-55.2 bps** (±4.9) | `-91.9 bps` | `-0.059 / -0.043` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 21:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,628.44 | ⚪ **CASH** | **+11.4 bps** (±7.4) | `+20.4 bps` | `+0.021 / -0.022` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,226.39 | ⚪ **CASH** | **-0.1 bps** (±6.8) | `+11.9 bps` | `-0.038 / -0.124` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $88.87 | ⚪ **CASH** | **-55.2 bps** (±4.9) | `-91.9 bps` | `-0.059 / -0.043` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 21:15:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,647.67 | ⚪ **CASH** | **+11.4 bps** (±7.4) | `+20.4 bps` | `+0.021 / -0.022` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,226.60 | ⚪ **CASH** | **-0.1 bps** (±6.8) | `+11.9 bps` | `-0.038 / -0.124` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $88.88 | ⚪ **CASH** | **-55.2 bps** (±4.9) | `-91.9 bps` | `-0.059 / -0.043` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 21:00:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,695.49 | ⚪ **CASH** | **+11.4 bps** (±7.4) | `+20.4 bps` | `+0.021 / -0.022` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,228.29 | ⚪ **CASH** | **-0.1 bps** (±6.8) | `+11.9 bps` | `-0.038 / -0.124` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.04 | ⚪ **CASH** | **-55.2 bps** (±4.9) | `-91.9 bps` | `-0.059 / -0.043` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 20:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,723.86 | ⚪ **CASH** | **+12.9 bps** (±6.6) | `+15.5 bps` | `+0.064 / -0.002` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,230.67 | ⚪ **CASH** | **+1.0 bps** (±4.2) | `+12.6 bps` | `-0.038 / -0.142` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.35 | ⚪ **CASH** | **-64.8 bps** (±7.9) | `-114.9 bps` | `-0.041 / -0.009` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 20:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,753.88 | ⚪ **CASH** | **+12.9 bps** (±6.6) | `+15.5 bps` | `+0.064 / -0.002` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,232.50 | ⚪ **CASH** | **+1.0 bps** (±4.2) | `+12.6 bps` | `-0.038 / -0.142` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.54 | ⚪ **CASH** | **-64.8 bps** (±7.9) | `-114.9 bps` | `-0.041 / -0.009` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 20:15:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,799.00 | ⚪ **CASH** | **+12.9 bps** (±6.6) | `+15.5 bps` | `+0.064 / -0.002` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.36 | ⚪ **CASH** | **+1.0 bps** (±4.2) | `+12.6 bps` | `-0.038 / -0.142` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.64 | ⚪ **CASH** | **-64.8 bps** (±7.9) | `-114.9 bps` | `-0.041 / -0.009` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 20:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,805.18 | ⚪ **CASH** | **+12.9 bps** (±6.6) | `+15.5 bps` | `+0.064 / -0.002` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,235.51 | ⚪ **CASH** | **+1.0 bps** (±4.2) | `+12.6 bps` | `-0.038 / -0.142` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.65 | ⚪ **CASH** | **-64.8 bps** (±7.9) | `-114.9 bps` | `-0.041 / -0.009` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 19:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,759.17 | ⚪ **CASH** | **+11.4 bps** (±2.9) | `+19.2 bps` | `+0.063 / -0.111` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.35 | ⚪ **CASH** | **+0.0 bps** (±5.1) | `+10.7 bps` | `-0.036 / -0.142` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.60 | ⚪ **CASH** | **-61.6 bps** (±7.6) | `-110.6 bps` | `-0.037 / +0.008` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 19:30:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,799.10 | ⚪ **CASH** | **+11.4 bps** (±2.9) | `+19.2 bps` | `+0.063 / -0.111` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.31 | ⚪ **CASH** | **+0.0 bps** (±5.1) | `+10.7 bps` | `-0.036 / -0.142` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.68 | ⚪ **CASH** | **-61.6 bps** (±7.6) | `-110.6 bps` | `-0.037 / +0.008` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 19:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,795.75 | ⚪ **CASH** | **+11.4 bps** (±2.9) | `+19.2 bps` | `+0.063 / -0.111` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,234.58 | ⚪ **CASH** | **+0.0 bps** (±5.1) | `+10.7 bps` | `-0.036 / -0.142` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.68 | ⚪ **CASH** | **-61.6 bps** (±7.6) | `-110.6 bps` | `-0.037 / +0.008` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 19:00:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,800.00 | ⚪ **CASH** | **+11.4 bps** (±2.9) | `+19.2 bps` | `+0.063 / -0.111` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.38 | ⚪ **CASH** | **+0.0 bps** (±5.1) | `+10.7 bps` | `-0.036 / -0.142` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.75 | ⚪ **CASH** | **-61.6 bps** (±7.6) | `-110.6 bps` | `-0.037 / +0.008` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-07 18:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $75,830.76 | ⚪ **CASH** | **+10.2 bps** (±3.7) | `+19.0 bps` | `+0.064 / -0.141` | `0.38%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,236.99 | ⚪ **CASH** | **-2.6 bps** (±9.1) | `+10.3 bps` | `-0.050 / -0.178` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $89.66 | ⚪ **CASH** | **-58.1 bps** (±7.0) | `-99.7 bps` | `-0.031 / -0.072` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
