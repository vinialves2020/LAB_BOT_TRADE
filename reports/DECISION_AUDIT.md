# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-22 15:17:11 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-22 15:17:11 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,548.20 | ⚪ **CASH** | **-24.1 bps** (±9.0) | `-14.7 bps` | `-0.163 / -0.051` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,394.99 | ⚪ **CASH** | **-4.9 bps** (±12.3) | `+12.2 bps` | `-0.052 / -0.088` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.27 | ⚪ **CASH** | **-2.9 bps** (±11.6) | `+1.7 bps` | `-0.028 / +0.091` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 15:02:23 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,802.01 | ⚪ **CASH** | **-24.1 bps** (±9.0) | `-14.7 bps` | `-0.163 / -0.051` | `0.33%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,410.83 | ⚪ **CASH** | **-4.9 bps** (±12.3) | `+12.2 bps` | `-0.052 / -0.088` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.70 | ⚪ **CASH** | **-2.9 bps** (±11.6) | `+1.7 bps` | `-0.028 / +0.091` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 14:47:20 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,791.83 | ⚪ **CASH** | **-18.4 bps** (±6.3) | `-6.4 bps` | `-0.137 / -0.088` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,410.31 | ⚪ **CASH** | **-9.7 bps** (±10.6) | `+3.1 bps` | `-0.034 / -0.135` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.49 | ⚪ **CASH** | **+0.9 bps** (±14.4) | `+9.0 bps` | `-0.015 / +0.053` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 14:32:04 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,745.30 | ⚪ **CASH** | **-18.4 bps** (±6.3) | `-6.4 bps` | `-0.137 / -0.088` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,405.10 | ⚪ **CASH** | **-9.7 bps** (±10.6) | `+3.1 bps` | `-0.034 / -0.135` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.78 | ⚪ **CASH** | **+0.9 bps** (±14.4) | `+9.0 bps` | `-0.015 / +0.053` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 14:17:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,607.99 | ⚪ **CASH** | **-18.4 bps** (±6.3) | `-6.4 bps` | `-0.137 / -0.088` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,403.65 | ⚪ **CASH** | **-9.7 bps** (±10.6) | `+3.1 bps` | `-0.034 / -0.135` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.85 | ⚪ **CASH** | **+0.9 bps** (±14.4) | `+9.0 bps` | `-0.015 / +0.053` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 14:02:15 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,840.01 | ⚪ **CASH** | **-18.4 bps** (±6.3) | `-6.4 bps` | `-0.137 / -0.088` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,411.92 | ⚪ **CASH** | **-9.7 bps** (±10.6) | `+3.1 bps` | `-0.034 / -0.135` | `0.46%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $105.19 | ⚪ **CASH** | **+0.9 bps** (±14.4) | `+9.0 bps` | `-0.015 / +0.053` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 13:47:17 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,541.98 | ⚪ **CASH** | **-14.2 bps** (±2.9) | `+0.9 bps` | `-0.128 / -0.112` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,404.37 | ⚪ **CASH** | **-4.3 bps** (±7.5) | `+10.8 bps` | `-0.020 / -0.136` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.63 | ⚪ **CASH** | **-6.4 bps** (±12.2) | `+1.6 bps` | `-0.022 / -0.041` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 13:32:17 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,785.83 | ⚪ **CASH** | **-14.2 bps** (±2.9) | `+0.9 bps` | `-0.128 / -0.112` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,402.75 | ⚪ **CASH** | **-4.3 bps** (±7.5) | `+10.8 bps` | `-0.020 / -0.136` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.58 | ⚪ **CASH** | **-6.4 bps** (±12.2) | `+1.6 bps` | `-0.022 / -0.041` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 13:17:17 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,740.01 | ⚪ **CASH** | **-14.2 bps** (±2.9) | `+0.9 bps` | `-0.128 / -0.112` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,399.87 | ⚪ **CASH** | **-4.3 bps** (±7.5) | `+10.8 bps` | `-0.020 / -0.136` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.34 | ⚪ **CASH** | **-6.4 bps** (±12.2) | `+1.6 bps` | `-0.022 / -0.041` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 13:02:18 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,705.74 | ⚪ **CASH** | **-14.2 bps** (±2.9) | `+0.9 bps` | `-0.128 / -0.112` | `0.34%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,400.93 | ⚪ **CASH** | **-4.3 bps** (±7.5) | `+10.8 bps` | `-0.020 / -0.136` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.36 | ⚪ **CASH** | **-6.4 bps** (±12.2) | `+1.6 bps` | `-0.022 / -0.041` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 12:47:11 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,766.30 | ⚪ **CASH** | **-11.3 bps** (±1.8) | `+5.2 bps` | `-0.126 / -0.103` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,404.28 | ⚪ **CASH** | **-2.1 bps** (±4.7) | `+14.1 bps` | `-0.018 / -0.141` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.52 | ⚪ **CASH** | **-7.4 bps** (±12.0) | `+3.3 bps` | `-0.024 / -0.092` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 12:32:01 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,716.98 | ⚪ **CASH** | **-11.3 bps** (±1.8) | `+5.2 bps` | `-0.126 / -0.103` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,400.30 | ⚪ **CASH** | **-2.1 bps** (±4.7) | `+14.1 bps` | `-0.018 / -0.141` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.24 | ⚪ **CASH** | **-7.4 bps** (±12.0) | `+3.3 bps` | `-0.024 / -0.092` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 12:17:25 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,874.13 | ⚪ **CASH** | **-11.3 bps** (±1.8) | `+5.2 bps` | `-0.126 / -0.103` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,404.78 | ⚪ **CASH** | **-2.1 bps** (±4.7) | `+14.1 bps` | `-0.018 / -0.141` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.53 | ⚪ **CASH** | **-7.4 bps** (±12.0) | `+3.3 bps` | `-0.024 / -0.092` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 12:02:08 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,785.24 | ⚪ **CASH** | **-11.3 bps** (±1.8) | `+5.2 bps` | `-0.126 / -0.103` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,403.57 | ⚪ **CASH** | **-2.1 bps** (±4.7) | `+14.1 bps` | `-0.018 / -0.141` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.55 | ⚪ **CASH** | **-7.4 bps** (±12.0) | `+3.3 bps` | `-0.024 / -0.092` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 11:47:18 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,862.66 | ⚪ **CASH** | **-11.5 bps** (±1.9) | `+2.7 bps` | `-0.114 / -0.099` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,403.87 | ⚪ **CASH** | **+4.2 bps** (±8.5) | `+25.6 bps` | `-0.011 / -0.148` | `0.47%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.60 | ⚪ **CASH** | **-9.0 bps** (±10.6) | `+5.0 bps` | `-0.023 / -0.176` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 11:32:08 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,922.10 | ⚪ **CASH** | **-11.5 bps** (±1.9) | `+2.7 bps` | `-0.114 / -0.099` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,404.72 | ⚪ **CASH** | **+4.2 bps** (±8.5) | `+25.6 bps` | `-0.011 / -0.148` | `0.47%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.63 | ⚪ **CASH** | **-9.0 bps** (±10.6) | `+5.0 bps` | `-0.023 / -0.176` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 11:16:59 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,983.13 | ⚪ **CASH** | **-11.5 bps** (±1.9) | `+2.7 bps` | `-0.114 / -0.099` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,404.16 | ⚪ **CASH** | **+4.2 bps** (±8.5) | `+25.6 bps` | `-0.011 / -0.148` | `0.47%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.59 | ⚪ **CASH** | **-9.0 bps** (±10.6) | `+5.0 bps` | `-0.023 / -0.176` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 11:02:13 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,992.28 | ⚪ **CASH** | **-11.5 bps** (±1.9) | `+2.7 bps` | `-0.114 / -0.099` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,405.08 | ⚪ **CASH** | **+4.2 bps** (±8.5) | `+25.6 bps` | `-0.011 / -0.148` | `0.47%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.47 | ⚪ **CASH** | **-9.0 bps** (±10.6) | `+5.0 bps` | `-0.023 / -0.176` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 10:47:02 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,086.00 | ⚪ **CASH** | **-10.7 bps** (±3.5) | `+4.9 bps` | `-0.111 / -0.113` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,408.14 | ⚪ **CASH** | **+0.9 bps** (±10.2) | `+20.3 bps` | `-0.006 / -0.163` | `0.48%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.67 | ⚪ **CASH** | **-9.8 bps** (±10.6) | `+4.9 bps` | `-0.028 / -0.194` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 10:32:04 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,060.03 | ⚪ **CASH** | **-10.7 bps** (±3.5) | `+4.9 bps` | `-0.111 / -0.113` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,411.12 | ⚪ **CASH** | **+0.9 bps** (±10.2) | `+20.3 bps` | `-0.006 / -0.163` | `0.48%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.67 | ⚪ **CASH** | **-9.8 bps** (±10.6) | `+4.9 bps` | `-0.028 / -0.194` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 10:17:01 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,051.25 | ⚪ **CASH** | **-10.7 bps** (±3.5) | `+4.9 bps` | `-0.111 / -0.113` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,409.24 | ⚪ **CASH** | **+0.9 bps** (±10.2) | `+20.3 bps` | `-0.006 / -0.163` | `0.48%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.52 | ⚪ **CASH** | **-9.8 bps** (±10.6) | `+4.9 bps` | `-0.028 / -0.194` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 10:02:13 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,028.01 | ⚪ **CASH** | **-10.7 bps** (±3.5) | `+4.9 bps` | `-0.111 / -0.113` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,411.19 | ⚪ **CASH** | **+0.9 bps** (±10.2) | `+20.3 bps` | `-0.006 / -0.163` | `0.48%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.49 | ⚪ **CASH** | **-9.8 bps** (±10.6) | `+4.9 bps` | `-0.028 / -0.194` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 09:47:08 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,834.01 | ⚪ **CASH** | **-12.7 bps** (±3.1) | `+5.9 bps` | `-0.121 / -0.164` | `0.36%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,401.43 | ⚪ **CASH** | **+3.8 bps** (±6.7) | `+26.3 bps` | `-0.035 / -0.136` | `0.49%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.89 | ⚪ **CASH** | **-13.3 bps** (±7.7) | `+4.4 bps` | `-0.032 / -0.275` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 09:32:16 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,825.26 | ⚪ **CASH** | **-12.7 bps** (±3.1) | `+5.9 bps` | `-0.121 / -0.164` | `0.36%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,402.66 | ⚪ **CASH** | **+3.8 bps** (±6.7) | `+26.3 bps` | `-0.035 / -0.136` | `0.49%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.85 | ⚪ **CASH** | **-13.3 bps** (±7.7) | `+4.4 bps` | `-0.032 / -0.275` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 09:17:02 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,913.31 | ⚪ **CASH** | **-12.7 bps** (±3.1) | `+5.9 bps` | `-0.121 / -0.164` | `0.36%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,406.90 | ⚪ **CASH** | **+3.8 bps** (±6.7) | `+26.3 bps` | `-0.035 / -0.136` | `0.49%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.02 | ⚪ **CASH** | **-13.3 bps** (±7.7) | `+4.4 bps` | `-0.032 / -0.275` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 09:02:05 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,837.50 | ⚪ **CASH** | **-12.7 bps** (±3.1) | `+5.9 bps` | `-0.121 / -0.164` | `0.36%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,406.71 | ⚪ **CASH** | **+3.8 bps** (±6.7) | `+26.3 bps` | `-0.035 / -0.136` | `0.49%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.79 | ⚪ **CASH** | **-13.3 bps** (±7.7) | `+4.4 bps` | `-0.032 / -0.275` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 08:47:04 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,950.01 | ⚪ **CASH** | **-13.5 bps** (±3.2) | `+6.4 bps` | `-0.109 / -0.217` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,409.22 | ⚪ **CASH** | **+2.2 bps** (±10.1) | `+20.2 bps` | `-0.018 / -0.110` | `0.47%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $103.80 | ⚪ **CASH** | **-1.6 bps** (±7.5) | `+23.0 bps` | `-0.026 / -0.255` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 08:32:18 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,982.49 | ⚪ **CASH** | **-13.5 bps** (±3.2) | `+6.4 bps` | `-0.109 / -0.217` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,413.18 | ⚪ **CASH** | **+2.2 bps** (±10.1) | `+20.2 bps` | `-0.018 / -0.110` | `0.47%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.01 | ⚪ **CASH** | **-1.6 bps** (±7.5) | `+23.0 bps` | `-0.026 / -0.255` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 08:17:12 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,138.07 | ⚪ **CASH** | **-13.5 bps** (±3.2) | `+6.4 bps` | `-0.109 / -0.217` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,417.44 | ⚪ **CASH** | **+2.2 bps** (±10.1) | `+20.2 bps` | `-0.018 / -0.110` | `0.47%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.05 | ⚪ **CASH** | **-1.6 bps** (±7.5) | `+23.0 bps` | `-0.026 / -0.255` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 08:02:14 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,223.84 | ⚪ **CASH** | **-13.5 bps** (±3.2) | `+6.4 bps` | `-0.109 / -0.217` | `0.35%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,428.47 | ⚪ **CASH** | **+2.2 bps** (±10.1) | `+20.2 bps` | `-0.018 / -0.110` | `0.47%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.37 | ⚪ **CASH** | **-1.6 bps** (±7.5) | `+23.0 bps` | `-0.026 / -0.255` | `0.51%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 07:47:02 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,302.78 | ⚪ **CASH** | **-11.3 bps** (±3.9) | `+12.3 bps` | `-0.102 / -0.262` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,431.43 | ⚪ **CASH** | **-1.4 bps** (±5.8) | `+17.6 bps` | `-0.013 / -0.195` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.39 | ⚪ **CASH** | **-11.3 bps** (±11.0) | `+2.7 bps` | `-0.007 / -0.236` | `0.52%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 07:32:31 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,270.34 | ⚪ **CASH** | **-11.3 bps** (±3.9) | `+12.3 bps` | `-0.102 / -0.262` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,427.45 | ⚪ **CASH** | **-1.4 bps** (±5.8) | `+17.6 bps` | `-0.013 / -0.195` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.37 | ⚪ **CASH** | **-11.3 bps** (±11.0) | `+2.7 bps` | `-0.007 / -0.236` | `0.52%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 07:17:12 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,340.99 | ⚪ **CASH** | **-11.3 bps** (±3.9) | `+12.3 bps` | `-0.102 / -0.262` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,429.37 | ⚪ **CASH** | **-1.4 bps** (±5.8) | `+17.6 bps` | `-0.013 / -0.195` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.42 | ⚪ **CASH** | **-11.3 bps** (±11.0) | `+2.7 bps` | `-0.007 / -0.236` | `0.52%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 07:02:13 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,516.87 | ⚪ **CASH** | **-11.3 bps** (±3.9) | `+12.3 bps` | `-0.102 / -0.262` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,434.45 | ⚪ **CASH** | **-1.4 bps** (±5.8) | `+17.6 bps` | `-0.013 / -0.195` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.63 | ⚪ **CASH** | **-11.3 bps** (±11.0) | `+2.7 bps` | `-0.007 / -0.236` | `0.52%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 06:47:29 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,508.31 | ⚪ **CASH** | **-15.9 bps** (±5.1) | `+5.7 bps` | `-0.099 / -0.293` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,429.99 | ⚪ **CASH** | **+0.8 bps** (±5.8) | `+20.3 bps` | `-0.015 / -0.177` | `0.48%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.49 | ⚪ **CASH** | **-2.2 bps** (±9.6) | `+13.9 bps` | `+0.007 / -0.183` | `0.52%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-22 06:32:00 UTC` | Patrimônio: **$994.32 USDT** (Caixa: `$994.32`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $82,590.00 | ⚪ **CASH** | **-15.9 bps** (±5.1) | `+5.7 bps` | `-0.099 / -0.293` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,433.46 | ⚪ **CASH** | **+0.8 bps** (±5.8) | `+20.3 bps` | `-0.015 / -0.177` | `0.48%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $104.64 | ⚪ **CASH** | **-2.2 bps** (±9.6) | `+13.9 bps` | `+0.007 / -0.183` | `0.52%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
