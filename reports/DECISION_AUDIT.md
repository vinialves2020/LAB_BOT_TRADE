# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-18 18:30:44 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-18 18:30:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,179.81 | ⚪ **CASH** | **+33.9 bps** (±16.7) | `+59.1 bps` | `+0.034 / +0.008` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,769.12 | ⚪ **CASH** | **+59.6 bps** (±14.0) | `+112.9 bps` | `-0.031 / -0.008` | `0.64%/h` | `weak_order_flow` | Filtro: confluência Dual-Setup (A/B) e absorção CVD insuficiente |
| **SOLUSDT** | $73.75 | ⚪ **CASH** | **+28.9 bps** (±13.2) | `+54.6 bps` | `-0.017 / +0.006` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 18:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,248.03 | ⚪ **CASH** | **+33.9 bps** (±16.7) | `+59.1 bps` | `+0.034 / +0.008` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,770.58 | ⚪ **CASH** | **+59.6 bps** (±14.0) | `+112.9 bps` | `-0.031 / -0.008` | `0.64%/h` | `weak_order_flow` | Filtro: confluência Dual-Setup (A/B) e absorção CVD insuficiente |
| **SOLUSDT** | $73.77 | ⚪ **CASH** | **+28.9 bps** (±13.2) | `+54.6 bps` | `-0.017 / +0.006` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 18:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,104.00 | ⚪ **CASH** | **+33.9 bps** (±16.7) | `+59.1 bps` | `+0.034 / +0.008` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,768.21 | ⚪ **CASH** | **+59.6 bps** (±14.0) | `+112.9 bps` | `-0.031 / -0.008` | `0.64%/h` | `weak_order_flow` | Filtro: confluência Dual-Setup (A/B) e absorção CVD insuficiente |
| **SOLUSDT** | $73.62 | ⚪ **CASH** | **+28.9 bps** (±13.2) | `+54.6 bps` | `-0.017 / +0.006` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 17:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,183.86 | ⚪ **CASH** | **+34.3 bps** (±13.0) | `+64.0 bps` | `+0.024 / -0.042` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,772.52 | ⚪ **CASH** | **+47.5 bps** (±7.1) | `+94.8 bps` | `-0.043 / -0.062` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $73.68 | ⚪ **CASH** | **+19.4 bps** (±18.9) | `+41.4 bps` | `-0.026 / -0.020` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 17:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,257.29 | ⚪ **CASH** | **+34.3 bps** (±13.0) | `+64.0 bps` | `+0.024 / -0.042` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,772.78 | ⚪ **CASH** | **+47.5 bps** (±7.1) | `+94.8 bps` | `-0.043 / -0.062` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $73.83 | ⚪ **CASH** | **+19.4 bps** (±18.9) | `+41.4 bps` | `-0.026 / -0.020` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 17:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,723.20 | ⚪ **CASH** | **+34.3 bps** (±13.0) | `+64.0 bps` | `+0.024 / -0.042` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,753.28 | ⚪ **CASH** | **+47.5 bps** (±7.1) | `+94.8 bps` | `-0.043 / -0.062` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $72.91 | ⚪ **CASH** | **+19.4 bps** (±18.9) | `+41.4 bps` | `-0.026 / -0.020` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 17:01:01 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,762.41 | ⚪ **CASH** | **+34.3 bps** (±13.0) | `+64.0 bps` | `+0.024 / -0.042` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,750.19 | ⚪ **CASH** | **+47.5 bps** (±7.1) | `+94.8 bps` | `-0.043 / -0.062` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $72.99 | ⚪ **CASH** | **+19.4 bps** (±18.9) | `+41.4 bps` | `-0.026 / -0.020` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 16:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,492.81 | ⚪ **CASH** | **+30.0 bps** (±20.5) | `+50.9 bps` | `+0.051 / -0.001` | `0.49%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.5 bps > 19.5) |
| **ETHUSDT** | $1,740.15 | ⚪ **CASH** | **+58.4 bps** (±6.5) | `+114.5 bps` | `-0.048 / -0.075` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $72.61 | ⚪ **CASH** | **+10.0 bps** (±12.6) | `+25.2 bps` | `-0.030 / -0.066` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 16:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,476.01 | ⚪ **CASH** | **+30.0 bps** (±20.5) | `+50.9 bps` | `+0.051 / -0.001` | `0.49%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.5 bps > 19.5) |
| **ETHUSDT** | $1,752.20 | ⚪ **CASH** | **+58.4 bps** (±6.5) | `+114.5 bps` | `-0.048 / -0.075` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $72.74 | ⚪ **CASH** | **+10.0 bps** (±12.6) | `+25.2 bps` | `-0.030 / -0.066` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 16:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,832.01 | ⚪ **CASH** | **+30.0 bps** (±20.5) | `+50.9 bps` | `+0.051 / -0.001` | `0.49%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.5 bps > 19.5) |
| **ETHUSDT** | $1,763.90 | ⚪ **CASH** | **+58.4 bps** (±6.5) | `+114.5 bps` | `-0.048 / -0.075` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $73.20 | ⚪ **CASH** | **+10.0 bps** (±12.6) | `+25.2 bps` | `-0.030 / -0.066` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 16:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,097.91 | ⚪ **CASH** | **+30.0 bps** (±20.5) | `+50.9 bps` | `+0.051 / -0.001` | `0.49%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.5 bps > 19.5) |
| **ETHUSDT** | $1,768.33 | ⚪ **CASH** | **+58.4 bps** (±6.5) | `+114.5 bps` | `-0.048 / -0.075` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $73.37 | ⚪ **CASH** | **+10.0 bps** (±12.6) | `+25.2 bps` | `-0.030 / -0.066` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-18 15:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,200.01 | ⚪ **CASH** | **+30.8 bps** (±14.6) | `+47.5 bps` | `+0.051 / +0.056` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,765.58 | ⚪ **CASH** | **+55.2 bps** (±10.6) | `+111.5 bps` | `-0.063 / -0.085` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $73.30 | ⚪ **CASH** | **+10.6 bps** (±6.1) | `+26.2 bps` | `-0.055 / -0.044` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 15:31:01 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,577.87 | ⚪ **CASH** | **+30.8 bps** (±14.6) | `+47.5 bps` | `+0.051 / +0.056` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,771.64 | ⚪ **CASH** | **+55.2 bps** (±10.6) | `+111.5 bps` | `-0.063 / -0.085` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $73.94 | ⚪ **CASH** | **+10.6 bps** (±6.1) | `+26.2 bps` | `-0.055 / -0.044` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 15:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,648.42 | ⚪ **CASH** | **+30.8 bps** (±14.6) | `+47.5 bps` | `+0.051 / +0.056` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,775.80 | ⚪ **CASH** | **+55.2 bps** (±10.6) | `+111.5 bps` | `-0.063 / -0.085` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $74.12 | ⚪ **CASH** | **+10.6 bps** (±6.1) | `+26.2 bps` | `-0.055 / -0.044` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 15:00:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,829.99 | ⚪ **CASH** | **+30.8 bps** (±14.6) | `+47.5 bps` | `+0.051 / +0.056` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,779.43 | ⚪ **CASH** | **+55.2 bps** (±10.6) | `+111.5 bps` | `-0.063 / -0.085` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $74.27 | ⚪ **CASH** | **+10.6 bps** (±6.1) | `+26.2 bps` | `-0.055 / -0.044` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 14:45:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,249.59 | ⚪ **CASH** | **+27.6 bps** (±16.1) | `+43.7 bps` | `+0.061 / +0.007` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,760.79 | ⚪ **CASH** | **+25.1 bps** (±17.0) | `+56.4 bps` | `-0.058 / -0.076` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $73.67 | ⚪ **CASH** | **+15.9 bps** (±5.6) | `+33.4 bps` | `-0.044 / -0.033` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 14:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,001.33 | ⚪ **CASH** | **+27.6 bps** (±16.1) | `+43.7 bps` | `+0.061 / +0.007` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,794.31 | ⚪ **CASH** | **+25.1 bps** (±17.0) | `+56.4 bps` | `-0.058 / -0.076` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.78 | ⚪ **CASH** | **+15.9 bps** (±5.6) | `+33.4 bps` | `-0.044 / -0.033` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 14:15:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,963.08 | ⚪ **CASH** | **+27.6 bps** (±16.1) | `+43.7 bps` | `+0.061 / +0.007` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,791.56 | ⚪ **CASH** | **+25.1 bps** (±17.0) | `+56.4 bps` | `-0.058 / -0.076` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.29 | ⚪ **CASH** | **+15.9 bps** (±5.6) | `+33.4 bps` | `-0.044 / -0.033` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 14:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,957.39 | ⚪ **CASH** | **+27.6 bps** (±16.1) | `+43.7 bps` | `+0.061 / +0.007` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,790.89 | ⚪ **CASH** | **+25.1 bps** (±17.0) | `+56.4 bps` | `-0.058 / -0.076` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.25 | ⚪ **CASH** | **+15.9 bps** (±5.6) | `+33.4 bps` | `-0.044 / -0.033` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 13:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,989.19 | ⚪ **CASH** | **+24.1 bps** (±16.5) | `+40.4 bps` | `+0.048 / -0.010` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,792.34 | ⚪ **CASH** | **+16.9 bps** (±10.2) | `+38.0 bps` | `-0.059 / -0.032` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.22 | ⚪ **CASH** | **+19.8 bps** (±6.7) | `+38.0 bps` | `-0.049 / +0.024` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 13:30:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,101.70 | ⚪ **CASH** | **+24.1 bps** (±16.5) | `+40.4 bps` | `+0.048 / -0.010` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,795.83 | ⚪ **CASH** | **+16.9 bps** (±10.2) | `+38.0 bps` | `-0.059 / -0.032` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.25 | ⚪ **CASH** | **+19.8 bps** (±6.7) | `+38.0 bps` | `-0.049 / +0.024` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 13:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,041.36 | ⚪ **CASH** | **+24.1 bps** (±16.5) | `+40.4 bps` | `+0.048 / -0.010` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,796.92 | ⚪ **CASH** | **+16.9 bps** (±10.2) | `+38.0 bps` | `-0.059 / -0.032` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.35 | ⚪ **CASH** | **+19.8 bps** (±6.7) | `+38.0 bps` | `-0.049 / +0.024` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 13:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,060.10 | ⚪ **CASH** | **+24.1 bps** (±16.5) | `+40.4 bps` | `+0.048 / -0.010` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,795.11 | ⚪ **CASH** | **+16.9 bps** (±10.2) | `+38.0 bps` | `-0.059 / -0.032` | `0.61%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.29 | ⚪ **CASH** | **+19.8 bps** (±6.7) | `+38.0 bps` | `-0.049 / +0.024` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 12:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,066.62 | ⚪ **CASH** | **+25.7 bps** (±17.6) | `+46.3 bps` | `+0.046 / -0.048` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,793.54 | ⚪ **CASH** | **+10.3 bps** (±11.3) | `+31.6 bps` | `-0.061 / -0.109` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.25 | ⚪ **CASH** | **+17.8 bps** (±4.7) | `+30.9 bps` | `-0.044 / +0.067` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 12:31:00 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,239.60 | ⚪ **CASH** | **+25.7 bps** (±17.6) | `+46.3 bps` | `+0.046 / -0.048` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,799.99 | ⚪ **CASH** | **+10.3 bps** (±11.3) | `+31.6 bps` | `-0.061 / -0.109` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.40 | ⚪ **CASH** | **+17.8 bps** (±4.7) | `+30.9 bps` | `-0.044 / +0.067` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 12:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,255.32 | ⚪ **CASH** | **+25.7 bps** (±17.6) | `+46.3 bps` | `+0.046 / -0.048` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,801.98 | ⚪ **CASH** | **+10.3 bps** (±11.3) | `+31.6 bps` | `-0.061 / -0.109` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.60 | ⚪ **CASH** | **+17.8 bps** (±4.7) | `+30.9 bps` | `-0.044 / +0.067` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 12:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,171.21 | ⚪ **CASH** | **+25.7 bps** (±17.6) | `+46.3 bps` | `+0.046 / -0.048` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,798.72 | ⚪ **CASH** | **+10.3 bps** (±11.3) | `+31.6 bps` | `-0.061 / -0.109` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.36 | ⚪ **CASH** | **+17.8 bps** (±4.7) | `+30.9 bps` | `-0.044 / +0.067` | `0.71%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 11:45:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,174.87 | ⚪ **CASH** | **+33.2 bps** (±14.4) | `+52.7 bps` | `+0.062 / +0.019` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,799.00 | ⚪ **CASH** | **+17.0 bps** (±8.1) | `+37.0 bps` | `-0.052 / -0.040` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.45 | ⚪ **CASH** | **+8.7 bps** (±5.8) | `+12.1 bps` | `-0.043 / +0.092` | `0.71%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 11:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,185.92 | ⚪ **CASH** | **+33.2 bps** (±14.4) | `+52.7 bps` | `+0.062 / +0.019` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,797.89 | ⚪ **CASH** | **+17.0 bps** (±8.1) | `+37.0 bps` | `-0.052 / -0.040` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.54 | ⚪ **CASH** | **+8.7 bps** (±5.8) | `+12.1 bps` | `-0.043 / +0.092` | `0.71%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 11:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,212.49 | ⚪ **CASH** | **+33.2 bps** (±14.4) | `+52.7 bps` | `+0.062 / +0.019` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,799.47 | ⚪ **CASH** | **+17.0 bps** (±8.1) | `+37.0 bps` | `-0.052 / -0.040` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.45 | ⚪ **CASH** | **+8.7 bps** (±5.8) | `+12.1 bps` | `-0.043 / +0.092` | `0.71%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 11:01:00 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,325.67 | ⚪ **CASH** | **+33.2 bps** (±14.4) | `+52.7 bps` | `+0.062 / +0.019` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,805.05 | ⚪ **CASH** | **+17.0 bps** (±8.1) | `+37.0 bps` | `-0.052 / -0.040` | `0.62%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.64 | ⚪ **CASH** | **+8.7 bps** (±5.8) | `+12.1 bps` | `-0.043 / +0.092` | `0.71%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 10:45:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,290.30 | ⚪ **CASH** | **+35.6 bps** (±18.3) | `+56.4 bps` | `+0.061 / +0.040` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,802.97 | ⚪ **CASH** | **+11.3 bps** (±10.2) | `+30.3 bps` | `-0.070 / -0.063` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.64 | ⚪ **CASH** | **+6.8 bps** (±8.9) | `+10.2 bps` | `-0.044 / +0.078` | `0.71%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 10:31:03 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,302.13 | ⚪ **CASH** | **+35.6 bps** (±18.3) | `+56.4 bps` | `+0.061 / +0.040` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,802.60 | ⚪ **CASH** | **+11.3 bps** (±10.2) | `+30.3 bps` | `-0.070 / -0.063` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.50 | ⚪ **CASH** | **+6.8 bps** (±8.9) | `+10.2 bps` | `-0.044 / +0.078` | `0.71%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 10:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,598.97 | ⚪ **CASH** | **+35.6 bps** (±18.3) | `+56.4 bps` | `+0.061 / +0.040` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,811.74 | ⚪ **CASH** | **+11.3 bps** (±10.2) | `+30.3 bps` | `-0.070 / -0.063` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.07 | ⚪ **CASH** | **+6.8 bps** (±8.9) | `+10.2 bps` | `-0.044 / +0.078` | `0.71%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 10:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,630.90 | ⚪ **CASH** | **+35.6 bps** (±18.3) | `+56.4 bps` | `+0.061 / +0.040` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,813.45 | ⚪ **CASH** | **+11.3 bps** (±10.2) | `+30.3 bps` | `-0.070 / -0.063` | `0.63%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $75.22 | ⚪ **CASH** | **+6.8 bps** (±8.9) | `+10.2 bps` | `-0.044 / +0.078` | `0.71%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |

---

### 🕒 Ciclo `2026-11-18 09:45:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,638.53 | ⚪ **CASH** | **+15.6 bps** (±13.9) | `+16.2 bps` | `+0.086 / +0.033` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,813.01 | ⚪ **CASH** | **+2.3 bps** (±15.9) | `+16.5 bps` | `-0.077 / -0.093` | `0.64%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $74.97 | ⚪ **CASH** | **+6.5 bps** (±6.6) | `+13.1 bps` | `-0.049 / +0.010` | `0.72%/h` | `vol_compressed` `weak_order_flow` `macro_downtrend` `stretched_top` | Filtro: armadilha de repique contra EMA semanal (168h) |
