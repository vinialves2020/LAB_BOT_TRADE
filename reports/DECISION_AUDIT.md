# 📋 BOT_TRADE V5.2 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-12 11:15:50 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
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

---

### 🕒 Ciclo `2026-11-12 07:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,473.59 | ⚪ **CASH** | **+4.6 bps** (±6.0) | `+6.5 bps` | `+0.020 / +0.000` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,046.91 | ⚪ **CASH** | **+34.3 bps** (±16.0) | `+65.7 bps` | `+0.038 / -0.078` | `0.53%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.78 | ⚪ **CASH** | **-20.4 bps** (±4.6) | `-31.3 bps` | `+0.022 / -0.123` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 07:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,566.84 | ⚪ **CASH** | **+4.6 bps** (±6.0) | `+6.5 bps` | `+0.020 / +0.000` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,046.40 | ⚪ **CASH** | **+34.3 bps** (±16.0) | `+65.7 bps` | `+0.038 / -0.078` | `0.53%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.77 | ⚪ **CASH** | **-20.4 bps** (±4.6) | `-31.3 bps` | `+0.022 / -0.123` | `0.58%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 06:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,584.48 | ⚪ **CASH** | **+3.2 bps** (±5.4) | `+3.0 bps` | `+0.017 / +0.019` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,045.51 | ⚪ **CASH** | **+35.7 bps** (±11.2) | `+62.3 bps` | `+0.041 / -0.002` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.78 | ⚪ **CASH** | **-19.1 bps** (±7.0) | `-27.9 bps` | `+0.021 / -0.130` | `0.59%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 06:30:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,652.64 | ⚪ **CASH** | **+3.2 bps** (±5.4) | `+3.0 bps` | `+0.017 / +0.019` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,050.70 | ⚪ **CASH** | **+35.7 bps** (±11.2) | `+62.3 bps` | `+0.041 / -0.002` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.05 | ⚪ **CASH** | **-19.1 bps** (±7.0) | `-27.9 bps` | `+0.021 / -0.130` | `0.59%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 06:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,670.00 | ⚪ **CASH** | **+3.2 bps** (±5.4) | `+3.0 bps` | `+0.017 / +0.019` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,051.15 | ⚪ **CASH** | **+35.7 bps** (±11.2) | `+62.3 bps` | `+0.041 / -0.002` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $83.06 | ⚪ **CASH** | **-19.1 bps** (±7.0) | `-27.9 bps` | `+0.021 / -0.130` | `0.59%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 06:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,623.91 | ⚪ **CASH** | **+3.2 bps** (±5.4) | `+3.0 bps` | `+0.017 / +0.019` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,047.69 | ⚪ **CASH** | **+35.7 bps** (±11.2) | `+62.3 bps` | `+0.041 / -0.002` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.95 | ⚪ **CASH** | **-19.1 bps** (±7.0) | `-27.9 bps` | `+0.021 / -0.130` | `0.59%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 05:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,609.82 | ⚪ **CASH** | **+3.6 bps** (±5.0) | `+3.6 bps` | `+0.021 / +0.011` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,046.65 | ⚪ **CASH** | **+38.0 bps** (±14.4) | `+65.5 bps` | `+0.045 / +0.010` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.00 | ⚪ **CASH** | **-20.6 bps** (±3.9) | `-30.3 bps` | `+0.024 / -0.150` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 05:30:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,623.38 | ⚪ **CASH** | **+3.6 bps** (±5.0) | `+3.6 bps` | `+0.021 / +0.011` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,044.36 | ⚪ **CASH** | **+38.0 bps** (±14.4) | `+65.5 bps` | `+0.045 / +0.010` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.94 | ⚪ **CASH** | **-20.6 bps** (±3.9) | `-30.3 bps` | `+0.024 / -0.150` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 05:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,583.46 | ⚪ **CASH** | **+3.6 bps** (±5.0) | `+3.6 bps` | `+0.021 / +0.011` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,044.01 | ⚪ **CASH** | **+38.0 bps** (±14.4) | `+65.5 bps` | `+0.045 / +0.010` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $82.82 | ⚪ **CASH** | **-20.6 bps** (±3.9) | `-30.3 bps` | `+0.024 / -0.150` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 05:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,700.01 | ⚪ **CASH** | **+3.6 bps** (±5.0) | `+3.6 bps` | `+0.021 / +0.011` | `0.39%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,049.37 | ⚪ **CASH** | **+38.0 bps** (±14.4) | `+65.5 bps` | `+0.045 / +0.010` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.03 | ⚪ **CASH** | **-20.6 bps** (±3.9) | `-30.3 bps` | `+0.024 / -0.150` | `0.60%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 04:45:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,739.60 | ⚪ **CASH** | **+4.8 bps** (±4.4) | `+6.4 bps` | `+0.023 / -0.004` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,050.99 | ⚪ **CASH** | **+40.3 bps** (±12.6) | `+68.9 bps` | `+0.039 / +0.026` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.12 | ⚪ **CASH** | **-15.8 bps** (±7.4) | `-19.6 bps` | `+0.020 / -0.167` | `0.61%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 04:30:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,733.01 | ⚪ **CASH** | **+4.8 bps** (±4.4) | `+6.4 bps` | `+0.023 / -0.004` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,052.14 | ⚪ **CASH** | **+40.3 bps** (±12.6) | `+68.9 bps` | `+0.039 / +0.026` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.05 | ⚪ **CASH** | **-15.8 bps** (±7.4) | `-19.6 bps` | `+0.020 / -0.167` | `0.61%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 04:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,767.13 | ⚪ **CASH** | **+4.8 bps** (±4.4) | `+6.4 bps` | `+0.023 / -0.004` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,053.60 | ⚪ **CASH** | **+40.3 bps** (±12.6) | `+68.9 bps` | `+0.039 / +0.026` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.14 | ⚪ **CASH** | **-15.8 bps** (±7.4) | `-19.6 bps` | `+0.020 / -0.167` | `0.61%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 04:00:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,819.00 | ⚪ **CASH** | **+4.8 bps** (±4.4) | `+6.4 bps` | `+0.023 / -0.004` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,055.75 | ⚪ **CASH** | **+40.3 bps** (±12.6) | `+68.9 bps` | `+0.039 / +0.026` | `0.55%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.41 | ⚪ **CASH** | **-15.8 bps** (±7.4) | `-19.6 bps` | `+0.020 / -0.167` | `0.61%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 03:45:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,800.01 | ⚪ **CASH** | **+3.2 bps** (±5.1) | `+6.1 bps` | `+0.020 / -0.034` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,054.66 | ⚪ **CASH** | **+40.3 bps** (±9.7) | `+66.9 bps` | `+0.037 / +0.053` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.26 | ⚪ **CASH** | **-14.9 bps** (±5.8) | `-18.6 bps` | `+0.022 / -0.163` | `0.62%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 03:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,826.01 | ⚪ **CASH** | **+3.2 bps** (±5.1) | `+6.1 bps` | `+0.020 / -0.034` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,055.41 | ⚪ **CASH** | **+40.3 bps** (±9.7) | `+66.9 bps` | `+0.037 / +0.053` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.30 | ⚪ **CASH** | **-14.9 bps** (±5.8) | `-18.6 bps` | `+0.022 / -0.163` | `0.62%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 03:15:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,733.24 | ⚪ **CASH** | **+3.2 bps** (±5.1) | `+6.1 bps` | `+0.020 / -0.034` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,053.48 | ⚪ **CASH** | **+40.3 bps** (±9.7) | `+66.9 bps` | `+0.037 / +0.053` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.22 | ⚪ **CASH** | **-14.9 bps** (±5.8) | `-18.6 bps` | `+0.022 / -0.163` | `0.62%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 03:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,814.46 | ⚪ **CASH** | **+3.2 bps** (±5.1) | `+6.1 bps` | `+0.020 / -0.034` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,058.59 | ⚪ **CASH** | **+40.3 bps** (±9.7) | `+66.9 bps` | `+0.037 / +0.053` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.48 | ⚪ **CASH** | **-14.9 bps** (±5.8) | `-18.6 bps` | `+0.022 / -0.163` | `0.62%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 02:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,843.03 | ⚪ **CASH** | **+2.7 bps** (±4.7) | `+8.3 bps` | `+0.019 / -0.083` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,057.88 | ⚪ **CASH** | **+36.5 bps** (±10.5) | `+61.1 bps` | `+0.035 / +0.043` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.38 | ⚪ **CASH** | **-13.7 bps** (±8.1) | `-17.7 bps` | `+0.028 / -0.144` | `0.62%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 02:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $73,985.95 | ⚪ **CASH** | **+2.7 bps** (±4.7) | `+8.3 bps` | `+0.019 / -0.083` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,061.13 | ⚪ **CASH** | **+36.5 bps** (±10.5) | `+61.1 bps` | `+0.035 / +0.043` | `0.56%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $83.55 | ⚪ **CASH** | **-13.7 bps** (±8.1) | `-17.7 bps` | `+0.028 / -0.144` | `0.62%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
