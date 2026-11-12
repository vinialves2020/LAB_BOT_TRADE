# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-12 16:15:46 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-12 16:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,914.60 | ⚪ **CASH** | **+6.0 bps** (±6.5) | `+16.1 bps` | `-0.002 / -0.056` | `0.40%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,012.49 | ⚪ **CASH** | **-11.0 bps** (±12.8) | `-11.1 bps` | `-0.019 / -0.070` | `0.49%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.84 | ⚪ **CASH** | **-16.2 bps** (±9.8) | `-26.8 bps` | `-0.008 / -0.000` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 16:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,645.24 | ⚪ **CASH** | **+6.0 bps** (±6.5) | `+16.1 bps` | `-0.002 / -0.056` | `0.40%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,007.91 | ⚪ **CASH** | **-11.0 bps** (±12.8) | `-11.1 bps` | `-0.019 / -0.070` | `0.49%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.62 | ⚪ **CASH** | **-16.2 bps** (±9.8) | `-26.8 bps` | `-0.008 / -0.000` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 15:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,405.25 | ⚪ **CASH** | **+10.5 bps** (±11.8) | `+24.8 bps` | `+0.005 / -0.063` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,000.66 | ⚪ **CASH** | **+29.3 bps** (±20.5) | `+62.5 bps` | `-0.004 / -0.082` | `0.50%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.15 | ⚪ **CASH** | **-7.1 bps** (±15.3) | `-10.6 bps` | `-0.005 / +0.009` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 15:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,501.49 | ⚪ **CASH** | **+10.5 bps** (±11.8) | `+24.8 bps` | `+0.005 / -0.063` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,005.64 | ⚪ **CASH** | **+29.3 bps** (±20.5) | `+62.5 bps` | `-0.004 / -0.082` | `0.50%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.14 | ⚪ **CASH** | **-7.1 bps** (±15.3) | `-10.6 bps` | `-0.005 / +0.009` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 15:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,369.99 | ⚪ **CASH** | **+10.5 bps** (±11.8) | `+24.8 bps` | `+0.005 / -0.063` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,998.63 | ⚪ **CASH** | **+29.3 bps** (±20.5) | `+62.5 bps` | `-0.004 / -0.082` | `0.50%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $80.72 | ⚪ **CASH** | **-7.1 bps** (±15.3) | `-10.6 bps` | `-0.005 / +0.009` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 15:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,546.94 | ⚪ **CASH** | **+10.5 bps** (±11.8) | `+24.8 bps` | `+0.005 / -0.063` | `0.41%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,000.16 | ⚪ **CASH** | **+29.3 bps** (±20.5) | `+62.5 bps` | `-0.004 / -0.082` | `0.50%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.04 | ⚪ **CASH** | **-7.1 bps** (±15.3) | `-10.6 bps` | `-0.005 / +0.009` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 14:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,752.79 | ⚪ **CASH** | **+7.1 bps** (±5.8) | `+12.4 bps` | `+0.017 / -0.015` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,002.16 | ⚪ **CASH** | **+33.4 bps** (±14.8) | `+68.2 bps` | `+0.003 / -0.090` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.14 | ⚪ **CASH** | **-16.2 bps** (±19.1) | `-28.3 bps` | `-0.002 / +0.026` | `0.55%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 14:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,970.61 | ⚪ **CASH** | **+7.1 bps** (±5.8) | `+12.4 bps` | `+0.017 / -0.015` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,994.41 | ⚪ **CASH** | **+33.4 bps** (±14.8) | `+68.2 bps` | `+0.003 / -0.090` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $80.92 | ⚪ **CASH** | **-16.2 bps** (±19.1) | `-28.3 bps` | `-0.002 / +0.026` | `0.55%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 14:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $72,393.55 | ⚪ **CASH** | **+7.1 bps** (±5.8) | `+12.4 bps` | `+0.017 / -0.015` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,008.29 | ⚪ **CASH** | **+33.4 bps** (±14.8) | `+68.2 bps` | `+0.003 / -0.090` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.16 | ⚪ **CASH** | **-16.2 bps** (±19.1) | `-28.3 bps` | `-0.002 / +0.026` | `0.55%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 14:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $72,564.86 | ⚪ **CASH** | **+7.1 bps** (±5.8) | `+12.4 bps` | `+0.017 / -0.015` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,014.43 | ⚪ **CASH** | **+33.4 bps** (±14.8) | `+68.2 bps` | `+0.003 / -0.090` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.49 | ⚪ **CASH** | **-16.2 bps** (±19.1) | `-28.3 bps` | `-0.002 / +0.026` | `0.55%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 13:45:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $72,581.74 | ⚪ **CASH** | **+7.7 bps** (±5.4) | `+10.2 bps` | `+0.016 / +0.039` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,011.19 | ⚪ **CASH** | **+55.6 bps** (±7.7) | `+98.2 bps` | `+0.044 / -0.012` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $81.53 | ⚪ **CASH** | **-3.8 bps** (±12.6) | `-10.7 bps` | `+0.003 / +0.075` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 13:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $72,729.41 | ⚪ **CASH** | **+7.7 bps** (±5.4) | `+10.2 bps` | `+0.016 / +0.039` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,016.80 | ⚪ **CASH** | **+55.6 bps** (±7.7) | `+98.2 bps` | `+0.044 / -0.012` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $81.68 | ⚪ **CASH** | **-3.8 bps** (±12.6) | `-10.7 bps` | `+0.003 / +0.075` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 13:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $72,528.28 | ⚪ **CASH** | **+7.7 bps** (±5.4) | `+10.2 bps` | `+0.016 / +0.039` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,005.21 | ⚪ **CASH** | **+55.6 bps** (±7.7) | `+98.2 bps` | `+0.044 / -0.012` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $81.42 | ⚪ **CASH** | **-3.8 bps** (±12.6) | `-10.7 bps` | `+0.003 / +0.075` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 13:00:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $72,882.98 | ⚪ **CASH** | **+7.7 bps** (±5.4) | `+10.2 bps` | `+0.016 / +0.039` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,020.81 | ⚪ **CASH** | **+55.6 bps** (±7.7) | `+98.2 bps` | `+0.044 / -0.012` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.16 | ⚪ **CASH** | **-3.8 bps** (±12.6) | `-10.7 bps` | `+0.003 / +0.075` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 12:45:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $72,905.35 | ⚪ **CASH** | **+7.5 bps** (±4.5) | `+8.1 bps` | `+0.015 / +0.062` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,022.25 | ⚪ **CASH** | **+51.8 bps** (±12.8) | `+95.9 bps` | `+0.038 / -0.060` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.25 | ⚪ **CASH** | **-0.4 bps** (±13.4) | `-6.0 bps` | `+0.007 / +0.098` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 12:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $72,865.08 | ⚪ **CASH** | **+7.5 bps** (±4.5) | `+8.1 bps` | `+0.015 / +0.062` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,021.94 | ⚪ **CASH** | **+51.8 bps** (±12.8) | `+95.9 bps` | `+0.038 / -0.060` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.19 | ⚪ **CASH** | **-0.4 bps** (±13.4) | `-6.0 bps` | `+0.007 / +0.098` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 12:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,065.49 | ⚪ **CASH** | **+7.5 bps** (±4.5) | `+8.1 bps` | `+0.015 / +0.062` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,027.28 | ⚪ **CASH** | **+51.8 bps** (±12.8) | `+95.9 bps` | `+0.038 / -0.060` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.59 | ⚪ **CASH** | **-0.4 bps** (±13.4) | `-6.0 bps` | `+0.007 / +0.098` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 12:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $72,908.60 | ⚪ **CASH** | **+7.5 bps** (±4.5) | `+8.1 bps` | `+0.015 / +0.062` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,021.54 | ⚪ **CASH** | **+51.8 bps** (±12.8) | `+95.9 bps` | `+0.038 / -0.060` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.44 | ⚪ **CASH** | **-0.4 bps** (±13.4) | `-6.0 bps` | `+0.007 / +0.098` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 11:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $72,982.30 | ⚪ **CASH** | **+7.6 bps** (±3.4) | `+1.2 bps` | `+0.027 / +0.142` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,029.09 | ⚪ **CASH** | **+42.3 bps** (±18.8) | `+76.4 bps` | `+0.047 / -0.029` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.57 | ⚪ **CASH** | **-4.0 bps** (±15.9) | `-18.0 bps` | `+0.017 / +0.161` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 11:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,170.40 | ⚪ **CASH** | **+7.6 bps** (±3.4) | `+1.2 bps` | `+0.027 / +0.142` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,031.55 | ⚪ **CASH** | **+42.3 bps** (±18.8) | `+76.4 bps` | `+0.047 / -0.029` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.51 | ⚪ **CASH** | **-4.0 bps** (±15.9) | `-18.0 bps` | `+0.017 / +0.161` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 11:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,384.00 | ⚪ **CASH** | **+7.6 bps** (±3.4) | `+1.2 bps` | `+0.027 / +0.142` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,042.95 | ⚪ **CASH** | **+42.3 bps** (±18.8) | `+76.4 bps` | `+0.047 / -0.029` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.91 | ⚪ **CASH** | **-4.0 bps** (±15.9) | `-18.0 bps` | `+0.017 / +0.161` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 11:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,477.29 | ⚪ **CASH** | **+7.6 bps** (±3.4) | `+1.2 bps` | `+0.027 / +0.142` | `0.35%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,045.22 | ⚪ **CASH** | **+42.3 bps** (±18.8) | `+76.4 bps` | `+0.047 / -0.029` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.96 | ⚪ **CASH** | **-4.0 bps** (±15.9) | `-18.0 bps` | `+0.017 / +0.161` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 10:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,510.00 | ⚪ **CASH** | **+4.9 bps** (±6.5) | `-2.0 bps` | `+0.025 / +0.127` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,047.95 | ⚪ **CASH** | **+42.5 bps** (±16.9) | `+79.7 bps` | `+0.042 / -0.072` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.18 | ⚪ **CASH** | **-7.2 bps** (±16.9) | `-23.1 bps` | `+0.034 / +0.129` | `0.55%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 10:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,545.29 | ⚪ **CASH** | **+4.9 bps** (±6.5) | `-2.0 bps` | `+0.025 / +0.127` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,048.97 | ⚪ **CASH** | **+42.5 bps** (±16.9) | `+79.7 bps` | `+0.042 / -0.072` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.32 | ⚪ **CASH** | **-7.2 bps** (±16.9) | `-23.1 bps` | `+0.034 / +0.129` | `0.55%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 10:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,419.38 | ⚪ **CASH** | **+4.9 bps** (±6.5) | `-2.0 bps` | `+0.025 / +0.127` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,044.09 | ⚪ **CASH** | **+42.5 bps** (±16.9) | `+79.7 bps` | `+0.042 / -0.072` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.04 | ⚪ **CASH** | **-7.2 bps** (±16.9) | `-23.1 bps` | `+0.034 / +0.129` | `0.55%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 10:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,486.01 | ⚪ **CASH** | **+4.9 bps** (±6.5) | `-2.0 bps` | `+0.025 / +0.127` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,046.39 | ⚪ **CASH** | **+42.5 bps** (±16.9) | `+79.7 bps` | `+0.042 / -0.072` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.18 | ⚪ **CASH** | **-7.2 bps** (±16.9) | `-23.1 bps` | `+0.034 / +0.129` | `0.55%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 09:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,407.53 | ⚪ **CASH** | **+4.9 bps** (±7.7) | `-1.6 bps` | `+0.018 / +0.142` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,045.13 | ⚪ **CASH** | **+41.4 bps** (±18.3) | `+77.7 bps` | `+0.037 / -0.057` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.06 | ⚪ **CASH** | **-11.1 bps** (±13.5) | `-21.1 bps` | `+0.030 / -0.007` | `0.56%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 09:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,472.01 | ⚪ **CASH** | **+4.9 bps** (±7.7) | `-1.6 bps` | `+0.018 / +0.142` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,046.82 | ⚪ **CASH** | **+41.4 bps** (±18.3) | `+77.7 bps` | `+0.037 / -0.057` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.98 | ⚪ **CASH** | **-11.1 bps** (±13.5) | `-21.1 bps` | `+0.030 / -0.007` | `0.56%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 09:15:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,362.35 | ⚪ **CASH** | **+4.9 bps** (±7.7) | `-1.6 bps` | `+0.018 / +0.142` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,042.46 | ⚪ **CASH** | **+41.4 bps** (±18.3) | `+77.7 bps` | `+0.037 / -0.057` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.74 | ⚪ **CASH** | **-11.1 bps** (±13.5) | `-21.1 bps` | `+0.030 / -0.007` | `0.56%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 09:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,509.98 | ⚪ **CASH** | **+4.9 bps** (±7.7) | `-1.6 bps` | `+0.018 / +0.142` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,047.57 | ⚪ **CASH** | **+41.4 bps** (±18.3) | `+77.7 bps` | `+0.037 / -0.057` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.90 | ⚪ **CASH** | **-11.1 bps** (±13.5) | `-21.1 bps` | `+0.030 / -0.007` | `0.56%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 08:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,520.64 | ⚪ **CASH** | **+10.2 bps** (±7.4) | `+9.3 bps` | `+0.019 / +0.119` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,048.78 | ⚪ **CASH** | **+37.9 bps** (±16.2) | `+69.9 bps` | `+0.036 / -0.038` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.91 | ⚪ **CASH** | **-18.0 bps** (±3.3) | `-31.3 bps` | `+0.029 / -0.069` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 08:30:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,521.54 | ⚪ **CASH** | **+10.2 bps** (±7.4) | `+9.3 bps` | `+0.019 / +0.119` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,047.58 | ⚪ **CASH** | **+37.9 bps** (±16.2) | `+69.9 bps` | `+0.036 / -0.038` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.87 | ⚪ **CASH** | **-18.0 bps** (±3.3) | `-31.3 bps` | `+0.029 / -0.069` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 08:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,584.13 | ⚪ **CASH** | **+10.2 bps** (±7.4) | `+9.3 bps` | `+0.019 / +0.119` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,048.94 | ⚪ **CASH** | **+37.9 bps** (±16.2) | `+69.9 bps` | `+0.036 / -0.038` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.88 | ⚪ **CASH** | **-18.0 bps** (±3.3) | `-31.3 bps` | `+0.029 / -0.069` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 08:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,644.17 | ⚪ **CASH** | **+10.2 bps** (±7.4) | `+9.3 bps` | `+0.019 / +0.119` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,051.30 | ⚪ **CASH** | **+37.9 bps** (±16.2) | `+69.9 bps` | `+0.036 / -0.038` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.00 | ⚪ **CASH** | **-18.0 bps** (±3.3) | `-31.3 bps` | `+0.029 / -0.069` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 07:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,579.00 | ⚪ **CASH** | **+4.6 bps** (±6.0) | `+6.5 bps` | `+0.020 / +0.000` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,048.24 | ⚪ **CASH** | **+34.3 bps** (±16.0) | `+65.7 bps` | `+0.038 / -0.078` | `0.53%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.85 | ⚪ **CASH** | **-20.4 bps** (±4.6) | `-31.3 bps` | `+0.022 / -0.123` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 07:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,570.22 | ⚪ **CASH** | **+4.6 bps** (±6.0) | `+6.5 bps` | `+0.020 / +0.000` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,049.44 | ⚪ **CASH** | **+34.3 bps** (±16.0) | `+65.7 bps` | `+0.038 / -0.078` | `0.53%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.88 | ⚪ **CASH** | **-20.4 bps** (±4.6) | `-31.3 bps` | `+0.022 / -0.123` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
