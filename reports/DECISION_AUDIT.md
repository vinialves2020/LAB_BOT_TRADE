# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-15 17:30:51 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-15 17:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,850.01 | ⚪ **CASH** | **+17.1 bps** (±23.4) | `+47.9 bps` | `-0.046 / -0.087` | `0.87%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.4 bps > 19.5) |
| **ETHUSDT** | $1,815.60 | ⚪ **CASH** | **+55.7 bps** (±9.7) | `+118.9 bps` | `-0.057 / -0.121` | `1.13%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $71.39 | ⚪ **CASH** | **-18.4 bps** (±31.5) | `-12.4 bps` | `-0.083 / -0.073` | `1.22%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (31.5 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 17:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,789.72 | ⚪ **CASH** | **+17.1 bps** (±23.4) | `+47.9 bps` | `-0.046 / -0.087` | `0.87%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.4 bps > 19.5) |
| **ETHUSDT** | $1,815.72 | ⚪ **CASH** | **+55.7 bps** (±9.7) | `+118.9 bps` | `-0.057 / -0.121` | `1.13%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $71.22 | ⚪ **CASH** | **-18.4 bps** (±31.5) | `-12.4 bps` | `-0.083 / -0.073` | `1.22%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (31.5 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 17:00:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,750.00 | ⚪ **CASH** | **+17.1 bps** (±23.4) | `+47.9 bps` | `-0.046 / -0.087` | `0.87%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.4 bps > 19.5) |
| **ETHUSDT** | $1,816.30 | ⚪ **CASH** | **+55.7 bps** (±9.7) | `+118.9 bps` | `-0.057 / -0.121` | `1.13%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $71.50 | ⚪ **CASH** | **-18.4 bps** (±31.5) | `-12.4 bps` | `-0.083 / -0.073` | `1.22%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (31.5 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 16:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,689.24 | ⚪ **CASH** | **+17.9 bps** (±17.9) | `+47.3 bps` | `-0.047 / -0.068` | `0.88%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,815.45 | ⚪ **CASH** | **+61.2 bps** (±7.9) | `+126.7 bps` | `-0.054 / -0.099` | `1.14%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $71.47 | ⚪ **CASH** | **-46.4 bps** (±46.3) | `-61.9 bps` | `-0.082 / -0.056` | `1.24%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.3 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 16:30:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,952.02 | ⚪ **CASH** | **+17.9 bps** (±17.9) | `+47.3 bps` | `-0.047 / -0.068` | `0.88%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,828.35 | ⚪ **CASH** | **+61.2 bps** (±7.9) | `+126.7 bps` | `-0.054 / -0.099` | `1.14%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $71.90 | ⚪ **CASH** | **-46.4 bps** (±46.3) | `-61.9 bps` | `-0.082 / -0.056` | `1.24%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.3 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 16:15:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,622.33 | ⚪ **CASH** | **+17.9 bps** (±17.9) | `+47.3 bps` | `-0.047 / -0.068` | `0.88%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,807.96 | ⚪ **CASH** | **+61.2 bps** (±7.9) | `+126.7 bps` | `-0.054 / -0.099` | `1.14%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $71.20 | ⚪ **CASH** | **-46.4 bps** (±46.3) | `-61.9 bps` | `-0.082 / -0.056` | `1.24%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.3 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 16:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,732.87 | ⚪ **CASH** | **+17.9 bps** (±17.9) | `+47.3 bps` | `-0.047 / -0.068` | `0.88%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,809.51 | ⚪ **CASH** | **+61.2 bps** (±7.9) | `+126.7 bps` | `-0.054 / -0.099` | `1.14%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $71.18 | ⚪ **CASH** | **-46.4 bps** (±46.3) | `-61.9 bps` | `-0.082 / -0.056` | `1.24%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.3 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 15:45:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,661.82 | ⚪ **CASH** | **+24.5 bps** (±11.4) | `+54.8 bps` | `-0.050 / -0.014` | `0.89%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,807.56 | ⚪ **CASH** | **+120.9 bps** (±23.4) | `+233.5 bps` | `-0.055 / -0.026` | `1.16%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.4 bps > 19.5) |
| **SOLUSDT** | $71.07 | ⚪ **CASH** | **-26.7 bps** (±36.2) | `-30.4 bps` | `-0.076 / -0.026` | `1.26%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 15:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,666.08 | ⚪ **CASH** | **+24.5 bps** (±11.4) | `+54.8 bps` | `-0.050 / -0.014` | `0.89%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,810.04 | ⚪ **CASH** | **+120.9 bps** (±23.4) | `+233.5 bps` | `-0.055 / -0.026` | `1.16%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.4 bps > 19.5) |
| **SOLUSDT** | $71.25 | ⚪ **CASH** | **-26.7 bps** (±36.2) | `-30.4 bps` | `-0.076 / -0.026` | `1.26%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 15:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,607.01 | ⚪ **CASH** | **+24.5 bps** (±11.4) | `+54.8 bps` | `-0.050 / -0.014` | `0.89%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,806.46 | ⚪ **CASH** | **+120.9 bps** (±23.4) | `+233.5 bps` | `-0.055 / -0.026` | `1.16%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.4 bps > 19.5) |
| **SOLUSDT** | $71.10 | ⚪ **CASH** | **-26.7 bps** (±36.2) | `-30.4 bps` | `-0.076 / -0.026` | `1.26%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 15:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,743.16 | ⚪ **CASH** | **+24.5 bps** (±11.4) | `+54.8 bps` | `-0.050 / -0.014` | `0.89%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,807.33 | ⚪ **CASH** | **+120.9 bps** (±23.4) | `+233.5 bps` | `-0.055 / -0.026` | `1.16%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.4 bps > 19.5) |
| **SOLUSDT** | $71.31 | ⚪ **CASH** | **-26.7 bps** (±36.2) | `-30.4 bps` | `-0.076 / -0.026` | `1.26%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 14:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,728.06 | ⚪ **CASH** | **+18.2 bps** (±18.9) | `+44.7 bps` | `-0.053 / -0.005` | `0.89%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |
| **ETHUSDT** | $1,803.17 | ⚪ **CASH** | **+81.8 bps** (±21.8) | `+157.6 bps` | `-0.053 / +0.045` | `1.15%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.8 bps > 19.5) |
| **SOLUSDT** | $71.36 | ⚪ **CASH** | **+28.8 bps** (±13.8) | `+63.9 bps` | `-0.082 / +0.024` | `1.24%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-15 14:30:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,998.69 | ⚪ **CASH** | **+18.2 bps** (±18.9) | `+44.7 bps` | `-0.053 / -0.005` | `0.89%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |
| **ETHUSDT** | $1,813.72 | ⚪ **CASH** | **+81.8 bps** (±21.8) | `+157.6 bps` | `-0.053 / +0.045` | `1.15%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.8 bps > 19.5) |
| **SOLUSDT** | $71.82 | ⚪ **CASH** | **+28.8 bps** (±13.8) | `+63.9 bps` | `-0.082 / +0.024` | `1.24%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-15 14:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,323.02 | ⚪ **CASH** | **+18.2 bps** (±18.9) | `+44.7 bps` | `-0.053 / -0.005` | `0.89%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |
| **ETHUSDT** | $1,821.92 | ⚪ **CASH** | **+81.8 bps** (±21.8) | `+157.6 bps` | `-0.053 / +0.045` | `1.15%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.8 bps > 19.5) |
| **SOLUSDT** | $72.32 | ⚪ **CASH** | **+28.8 bps** (±13.8) | `+63.9 bps` | `-0.082 / +0.024` | `1.24%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-15 14:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,328.01 | ⚪ **CASH** | **+18.2 bps** (±18.9) | `+44.7 bps` | `-0.053 / -0.005` | `0.89%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |
| **ETHUSDT** | $1,827.17 | ⚪ **CASH** | **+81.8 bps** (±21.8) | `+157.6 bps` | `-0.053 / +0.045` | `1.15%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.8 bps > 19.5) |
| **SOLUSDT** | $72.44 | ⚪ **CASH** | **+28.8 bps** (±13.8) | `+63.9 bps` | `-0.082 / +0.024` | `1.24%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-15 13:45:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,464.00 | ⚪ **CASH** | **+19.4 bps** (±19.4) | `+51.8 bps` | `-0.057 / -0.071` | `0.91%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.8 bps) |
| **ETHUSDT** | $1,831.76 | ⚪ **CASH** | **+83.0 bps** (±17.2) | `+159.3 bps` | `-0.054 / +0.045` | `1.17%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.68 | ⚪ **CASH** | **+23.1 bps** (±17.9) | `+56.7 bps` | `-0.084 / -0.008` | `1.26%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 35.8 bps) |

---

### 🕒 Ciclo `2026-11-15 13:30:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,500.01 | ⚪ **CASH** | **+19.4 bps** (±19.4) | `+51.8 bps` | `-0.057 / -0.071` | `0.91%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.8 bps) |
| **ETHUSDT** | $1,833.90 | ⚪ **CASH** | **+83.0 bps** (±17.2) | `+159.3 bps` | `-0.054 / +0.045` | `1.17%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.86 | ⚪ **CASH** | **+23.1 bps** (±17.9) | `+56.7 bps` | `-0.084 / -0.008` | `1.26%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 35.8 bps) |

---

### 🕒 Ciclo `2026-11-15 13:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,572.00 | ⚪ **CASH** | **+19.4 bps** (±19.4) | `+51.8 bps` | `-0.057 / -0.071` | `0.91%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.8 bps) |
| **ETHUSDT** | $1,834.44 | ⚪ **CASH** | **+83.0 bps** (±17.2) | `+159.3 bps` | `-0.054 / +0.045` | `1.17%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $72.98 | ⚪ **CASH** | **+23.1 bps** (±17.9) | `+56.7 bps` | `-0.084 / -0.008` | `1.26%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 35.8 bps) |

---

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
