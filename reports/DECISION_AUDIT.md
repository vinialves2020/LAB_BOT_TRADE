# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-02 00:17:45 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-02 00:17:45 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,114.01 | ⚪ **CASH** | **+13.0 bps** (±6.4) | `+18.1 bps` | `+0.039 / +0.014` | `0.25%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,270.15 | ⚪ **CASH** | **+22.8 bps** (±1.9) | `+32.5 bps` | `+0.039 / +0.053` | `0.30%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.13 | ⚪ **CASH** | **+14.6 bps** (±12.2) | `+22.9 bps` | `-0.007 / +0.071` | `0.42%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 00:03:02 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,400.25 | ⚪ **CASH** | **+13.0 bps** (±6.4) | `+18.1 bps` | `+0.039 / +0.014` | `0.25%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,281.25 | ⚪ **CASH** | **+22.8 bps** (±1.9) | `+32.5 bps` | `+0.039 / +0.053` | `0.30%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.76 | ⚪ **CASH** | **+14.6 bps** (±12.2) | `+22.9 bps` | `-0.007 / +0.071` | `0.42%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 23:47:26 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,292.01 | ⚪ **CASH** | **-2.2 bps** (±3.9) | `-1.2 bps` | `+0.024 / -0.084` | `0.24%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,274.51 | ⚪ **CASH** | **-1.5 bps** (±5.8) | `-4.5 bps` | `+0.020 / -0.006` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.51 | ⚪ **CASH** | **-67.3 bps** (±11.6) | `-118.1 bps` | `-0.036 / +0.003` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 23:32:43 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,145.46 | ⚪ **CASH** | **-2.2 bps** (±3.9) | `-1.2 bps` | `+0.024 / -0.084` | `0.24%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,268.62 | ⚪ **CASH** | **-1.5 bps** (±5.8) | `-4.5 bps` | `+0.020 / -0.006` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.08 | ⚪ **CASH** | **-67.3 bps** (±11.6) | `-118.1 bps` | `-0.036 / +0.003` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 23:17:38 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,110.01 | ⚪ **CASH** | **-2.2 bps** (±3.9) | `-1.2 bps` | `+0.024 / -0.084` | `0.24%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,269.85 | ⚪ **CASH** | **-1.5 bps** (±5.8) | `-4.5 bps` | `+0.020 / -0.006` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.19 | ⚪ **CASH** | **-67.3 bps** (±11.6) | `-118.1 bps` | `-0.036 / +0.003` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 23:02:37 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,832.01 | ⚪ **CASH** | **-2.2 bps** (±3.9) | `-1.2 bps` | `+0.024 / -0.084` | `0.24%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,261.44 | ⚪ **CASH** | **-1.5 bps** (±5.8) | `-4.5 bps` | `+0.020 / -0.006` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $93.75 | ⚪ **CASH** | **-67.3 bps** (±11.6) | `-118.1 bps` | `-0.036 / +0.003` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 22:47:42 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,812.00 | ⚪ **CASH** | **+3.1 bps** (±5.5) | `+7.7 bps` | `+0.028 / -0.080` | `0.24%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,258.70 | ⚪ **CASH** | **+5.4 bps** (±1.9) | `-0.7 bps` | `+0.035 / +0.091` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $93.84 | ⚪ **CASH** | **-62.9 bps** (±13.0) | `-108.9 bps` | `-0.044 / +0.000` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 22:32:49 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,724.16 | ⚪ **CASH** | **+3.1 bps** (±5.5) | `+7.7 bps` | `+0.028 / -0.080` | `0.24%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,257.58 | ⚪ **CASH** | **+5.4 bps** (±1.9) | `-0.7 bps` | `+0.035 / +0.091` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $93.67 | ⚪ **CASH** | **-62.9 bps** (±13.0) | `-108.9 bps` | `-0.044 / +0.000` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 22:17:26 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,750.00 | ⚪ **CASH** | **+3.1 bps** (±5.5) | `+7.7 bps` | `+0.028 / -0.080` | `0.24%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,258.43 | ⚪ **CASH** | **+5.4 bps** (±1.9) | `-0.7 bps` | `+0.035 / +0.091` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $93.73 | ⚪ **CASH** | **-62.9 bps** (±13.0) | `-108.9 bps` | `-0.044 / +0.000` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 22:02:39 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,894.00 | ⚪ **CASH** | **+3.1 bps** (±5.5) | `+7.7 bps` | `+0.028 / -0.080` | `0.24%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,263.79 | ⚪ **CASH** | **+5.4 bps** (±1.9) | `-0.7 bps` | `+0.035 / +0.091` | `0.29%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.40 | ⚪ **CASH** | **-62.9 bps** (±13.0) | `-108.9 bps` | `-0.044 / +0.000` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 21:47:52 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,959.52 | ⚪ **CASH** | **+2.8 bps** (±4.6) | `+6.9 bps` | `+0.029 / -0.080` | `0.25%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,266.37 | ⚪ **CASH** | **+0.4 bps** (±2.6) | `-5.7 bps` | `+0.038 / +0.028` | `0.30%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.52 | ⚪ **CASH** | **-65.5 bps** (±16.2) | `-112.8 bps` | `-0.050 / +0.001` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 21:32:33 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,930.41 | ⚪ **CASH** | **+2.8 bps** (±4.6) | `+6.9 bps` | `+0.029 / -0.080` | `0.25%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,265.14 | ⚪ **CASH** | **+0.4 bps** (±2.6) | `-5.7 bps` | `+0.038 / +0.028` | `0.30%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.41 | ⚪ **CASH** | **-65.5 bps** (±16.2) | `-112.8 bps` | `-0.050 / +0.001` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 21:17:33 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,874.02 | ⚪ **CASH** | **+2.8 bps** (±4.6) | `+6.9 bps` | `+0.029 / -0.080` | `0.25%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,264.38 | ⚪ **CASH** | **+0.4 bps** (±2.6) | `-5.7 bps` | `+0.038 / +0.028` | `0.30%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.35 | ⚪ **CASH** | **-65.5 bps** (±16.2) | `-112.8 bps` | `-0.050 / +0.001` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 21:02:48 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,926.01 | ⚪ **CASH** | **+2.8 bps** (±4.6) | `+6.9 bps` | `+0.029 / -0.080` | `0.25%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,264.88 | ⚪ **CASH** | **+0.4 bps** (±2.6) | `-5.7 bps` | `+0.038 / +0.028` | `0.30%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.35 | ⚪ **CASH** | **-65.5 bps** (±16.2) | `-112.8 bps` | `-0.050 / +0.001` | `0.41%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 20:47:32 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,881.97 | ⚪ **CASH** | **+5.7 bps** (±4.0) | `+9.5 bps` | `+0.026 / -0.036` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,262.97 | ⚪ **CASH** | **+0.4 bps** (±7.2) | `-4.7 bps` | `+0.034 / +0.033` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.30 | ⚪ **CASH** | **-63.0 bps** (±9.4) | `-105.7 bps` | `-0.060 / -0.039` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 20:32:47 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,811.05 | ⚪ **CASH** | **+5.7 bps** (±4.0) | `+9.5 bps` | `+0.026 / -0.036` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,260.49 | ⚪ **CASH** | **+0.4 bps** (±7.2) | `-4.7 bps` | `+0.034 / +0.033` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.13 | ⚪ **CASH** | **-63.0 bps** (±9.4) | `-105.7 bps` | `-0.060 / -0.039` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 20:17:21 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,744.08 | ⚪ **CASH** | **+5.7 bps** (±4.0) | `+9.5 bps` | `+0.026 / -0.036` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,257.18 | ⚪ **CASH** | **+0.4 bps** (±7.2) | `-4.7 bps` | `+0.034 / +0.033` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $93.86 | ⚪ **CASH** | **-63.0 bps** (±9.4) | `-105.7 bps` | `-0.060 / -0.039` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 20:02:31 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,831.07 | ⚪ **CASH** | **+5.7 bps** (±4.0) | `+9.5 bps` | `+0.026 / -0.036` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,259.66 | ⚪ **CASH** | **+0.4 bps** (±7.2) | `-4.7 bps` | `+0.034 / +0.033` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.05 | ⚪ **CASH** | **-63.0 bps** (±9.4) | `-105.7 bps` | `-0.060 / -0.039` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 19:47:38 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,741.03 | ⚪ **CASH** | **+10.5 bps** (±3.1) | `+11.7 bps` | `+0.043 / +0.026` | `0.30%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,257.72 | ⚪ **CASH** | **+4.8 bps** (±5.4) | `-0.8 bps` | `+0.040 / +0.068` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $93.84 | ⚪ **CASH** | **-69.7 bps** (±20.4) | `-115.8 bps` | `-0.063 / -0.048` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 19:32:21 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,800.13 | ⚪ **CASH** | **+10.5 bps** (±3.1) | `+11.7 bps` | `+0.043 / +0.026` | `0.30%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,259.50 | ⚪ **CASH** | **+4.8 bps** (±5.4) | `-0.8 bps` | `+0.040 / +0.068` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $93.95 | ⚪ **CASH** | **-69.7 bps** (±20.4) | `-115.8 bps` | `-0.063 / -0.048` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 19:17:51 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,739.45 | ⚪ **CASH** | **+10.5 bps** (±3.1) | `+11.7 bps` | `+0.043 / +0.026` | `0.30%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,257.52 | ⚪ **CASH** | **+4.8 bps** (±5.4) | `-0.8 bps` | `+0.040 / +0.068` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $93.82 | ⚪ **CASH** | **-69.7 bps** (±20.4) | `-115.8 bps` | `-0.063 / -0.048` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 19:02:46 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,870.27 | ⚪ **CASH** | **+10.5 bps** (±3.1) | `+11.7 bps` | `+0.043 / +0.026` | `0.30%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,262.87 | ⚪ **CASH** | **+4.8 bps** (±5.4) | `-0.8 bps` | `+0.040 / +0.068` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.32 | ⚪ **CASH** | **-69.7 bps** (±20.4) | `-115.8 bps` | `-0.063 / -0.048` | `0.48%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 18:47:30 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,972.01 | ⚪ **CASH** | **+10.2 bps** (±3.7) | `+8.7 bps` | `+0.071 / +0.001` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,266.74 | ⚪ **CASH** | **-0.2 bps** (±5.2) | `-3.6 bps` | `+0.031 / -0.037` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.61 | ⚪ **CASH** | **-71.9 bps** (±21.7) | `-120.8 bps` | `-0.056 / -0.060` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 18:32:22 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,956.32 | ⚪ **CASH** | **+10.2 bps** (±3.7) | `+8.7 bps` | `+0.071 / +0.001` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,265.59 | ⚪ **CASH** | **-0.2 bps** (±5.2) | `-3.6 bps` | `+0.031 / -0.037` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.50 | ⚪ **CASH** | **-71.9 bps** (±21.7) | `-120.8 bps` | `-0.056 / -0.060` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 18:17:22 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,982.01 | ⚪ **CASH** | **+10.2 bps** (±3.7) | `+8.7 bps` | `+0.071 / +0.001` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,264.64 | ⚪ **CASH** | **-0.2 bps** (±5.2) | `-3.6 bps` | `+0.031 / -0.037` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.59 | ⚪ **CASH** | **-71.9 bps** (±21.7) | `-120.8 bps` | `-0.056 / -0.060` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 18:02:37 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,964.13 | ⚪ **CASH** | **+10.2 bps** (±3.7) | `+8.7 bps` | `+0.071 / +0.001` | `0.31%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,263.38 | ⚪ **CASH** | **-0.2 bps** (±5.2) | `-3.6 bps` | `+0.031 / -0.037` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.64 | ⚪ **CASH** | **-71.9 bps** (±21.7) | `-120.8 bps` | `-0.056 / -0.060` | `0.49%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 17:47:22 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,080.00 | ⚪ **CASH** | **+9.5 bps** (±5.6) | `+2.5 bps` | `+0.103 / +0.009` | `0.31%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,268.16 | ⚪ **CASH** | **+2.4 bps** (±4.2) | `-3.8 bps` | `+0.031 / +0.013` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.74 | ⚪ **CASH** | **-72.2 bps** (±22.2) | `-122.8 bps` | `-0.054 / -0.063` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 17:32:37 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,142.00 | ⚪ **CASH** | **+9.5 bps** (±5.6) | `+2.5 bps` | `+0.103 / +0.009` | `0.31%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,270.26 | ⚪ **CASH** | **+2.4 bps** (±4.2) | `-3.8 bps` | `+0.031 / +0.013` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.88 | ⚪ **CASH** | **-72.2 bps** (±22.2) | `-122.8 bps` | `-0.054 / -0.063` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 17:02:31 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,147.25 | ⚪ **CASH** | **+9.5 bps** (±5.6) | `+2.5 bps` | `+0.103 / +0.009` | `0.31%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,269.58 | ⚪ **CASH** | **+2.4 bps** (±4.2) | `-3.8 bps` | `+0.031 / +0.013` | `0.39%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.71 | ⚪ **CASH** | **-72.2 bps** (±22.2) | `-122.8 bps` | `-0.054 / -0.063` | `0.50%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 16:47:18 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,092.47 | ⚪ **CASH** | **+6.9 bps** (±4.5) | `-5.5 bps` | `+0.133 / -0.009` | `0.32%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,269.07 | ⚪ **CASH** | **+0.9 bps** (±4.4) | `-4.5 bps` | `+0.025 / -0.031` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.72 | ⚪ **CASH** | **-74.6 bps** (±19.5) | `-126.1 bps` | `-0.060 / -0.101` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 16:32:26 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,078.35 | ⚪ **CASH** | **+6.9 bps** (±4.5) | `-5.5 bps` | `+0.133 / -0.009` | `0.32%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,269.64 | ⚪ **CASH** | **+0.9 bps** (±4.4) | `-4.5 bps` | `+0.025 / -0.031` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.75 | ⚪ **CASH** | **-74.6 bps** (±19.5) | `-126.1 bps` | `-0.060 / -0.101` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 16:17:45 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,071.89 | ⚪ **CASH** | **+6.9 bps** (±4.5) | `-5.5 bps` | `+0.133 / -0.009` | `0.32%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,270.26 | ⚪ **CASH** | **+0.9 bps** (±4.4) | `-4.5 bps` | `+0.025 / -0.031` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.83 | ⚪ **CASH** | **-74.6 bps** (±19.5) | `-126.1 bps` | `-0.060 / -0.101` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 16:02:35 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,999.97 | ⚪ **CASH** | **+6.9 bps** (±4.5) | `-5.5 bps` | `+0.133 / -0.009` | `0.32%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,266.92 | ⚪ **CASH** | **+0.9 bps** (±4.4) | `-4.5 bps` | `+0.025 / -0.031` | `0.40%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.78 | ⚪ **CASH** | **-74.6 bps** (±19.5) | `-126.1 bps` | `-0.060 / -0.101` | `0.51%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 15:47:41 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,066.66 | ⚪ **CASH** | **+8.5 bps** (±7.7) | `-5.3 bps` | `+0.154 / -0.008` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,269.45 | ⚪ **CASH** | **+1.3 bps** (±4.3) | `-4.6 bps` | `+0.032 / -0.045` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.95 | ⚪ **CASH** | **-78.3 bps** (±18.9) | `-130.9 bps` | `-0.066 / -0.138` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 15:32:24 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,043.02 | ⚪ **CASH** | **+8.5 bps** (±7.7) | `-5.3 bps` | `+0.154 / -0.008` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,269.22 | ⚪ **CASH** | **+1.3 bps** (±4.3) | `-4.6 bps` | `+0.032 / -0.045` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.86 | ⚪ **CASH** | **-78.3 bps** (±18.9) | `-130.9 bps` | `-0.066 / -0.138` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-01 15:17:24 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,064.00 | ⚪ **CASH** | **+8.5 bps** (±7.7) | `-5.3 bps` | `+0.154 / -0.008` | `0.32%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,270.32 | ⚪ **CASH** | **+1.3 bps** (±4.3) | `-4.6 bps` | `+0.032 / -0.045` | `0.41%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.99 | ⚪ **CASH** | **-78.3 bps** (±18.9) | `-130.9 bps` | `-0.066 / -0.138` | `0.52%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
