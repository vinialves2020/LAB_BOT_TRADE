# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-02 04:17:20 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-02 04:17:20 UTC` | Patrimônio: **$970.14 USDT** (Caixa: `$649.82`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,720.00 | ⚪ **CASH** | **+36.3 bps** (±8.9) | `+42.7 bps` | `+0.080 / +0.202` | `0.23%/h` | `stretched_top` | Filtro: preço esticado próximo ao topo de 24h |
| **ETHUSDT** | $2,311.00 | ⚪ **CASH** | **+25.5 bps** (±11.7) | `+17.2 bps` | `+0.128 / +0.224` | `0.29%/h` | `stretched_top` | Filtro: preço esticado próximo ao topo de 24h |
| **SOLUSDT** | $95.65 | 🟡 **HOLD** | **+24.6 bps** (±8.9) | `+31.7 bps` | `+0.025 / +0.127` | `0.41%/h` | Liberado ✅ | Posição ativa há 0.2h (PnL: +0.02% | Pico: +0.02%) |

---

### 🕒 Ciclo `2026-11-02 04:02:36 UTC` | Patrimônio: **$970.07 USDT** (Caixa: `$649.82`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,636.00 | ⚪ **CASH** | **+36.3 bps** (±8.9) | `+42.7 bps` | `+0.080 / +0.202` | `0.23%/h` | `stretched_top` | Filtro: preço esticado próximo ao topo de 24h |
| **ETHUSDT** | $2,310.04 | ⚪ **CASH** | **+25.5 bps** (±11.7) | `+17.2 bps` | `+0.128 / +0.224` | `0.29%/h` | `stretched_top` | Filtro: preço esticado próximo ao topo de 24h |
| **SOLUSDT** | $95.63 | 🟢 **BUY** | **+24.6 bps** (±8.9) | `+31.7 bps` | `+0.025 / +0.127` | `0.41%/h` | Liberado ✅ | Entrada Swing 12h aprovada (Alpha +24.6 bps > 24.0 bps | CVD 24h +0.025) |

---

### 🕒 Ciclo `2026-11-02 03:47:23 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,824.00 | ⚪ **CASH** | **+19.8 bps** (±7.3) | `+20.6 bps` | `+0.054 / +0.135` | `0.24%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,313.84 | ⚪ **CASH** | **+33.2 bps** (±7.1) | `+29.1 bps` | `+0.132 / +0.257` | `0.29%/h` | `stretched_top` | Filtro: preço esticado próximo ao topo de 24h |
| **SOLUSDT** | $95.87 | ⚪ **CASH** | **+21.1 bps** (±13.6) | `+35.4 bps` | `-0.010 / +0.057` | `0.42%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 03:32:53 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,668.01 | ⚪ **CASH** | **+19.8 bps** (±7.3) | `+20.6 bps` | `+0.054 / +0.135` | `0.24%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,310.33 | ⚪ **CASH** | **+33.2 bps** (±7.1) | `+29.1 bps` | `+0.132 / +0.257` | `0.29%/h` | `stretched_top` | Filtro: preço esticado próximo ao topo de 24h |
| **SOLUSDT** | $95.68 | ⚪ **CASH** | **+21.1 bps** (±13.6) | `+35.4 bps` | `-0.010 / +0.057` | `0.42%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 03:17:30 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,530.00 | ⚪ **CASH** | **+19.8 bps** (±7.3) | `+20.6 bps` | `+0.054 / +0.135` | `0.24%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,295.46 | ⚪ **CASH** | **+33.2 bps** (±7.1) | `+29.1 bps` | `+0.132 / +0.257` | `0.29%/h` | `stretched_top` | Filtro: preço esticado próximo ao topo de 24h |
| **SOLUSDT** | $95.00 | ⚪ **CASH** | **+21.1 bps** (±13.6) | `+35.4 bps` | `-0.010 / +0.057` | `0.42%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 03:02:51 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,450.00 | ⚪ **CASH** | **+19.8 bps** (±7.3) | `+20.6 bps` | `+0.054 / +0.135` | `0.24%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,295.43 | ⚪ **CASH** | **+33.2 bps** (±7.1) | `+29.1 bps` | `+0.132 / +0.257` | `0.29%/h` | `stretched_top` | Filtro: preço esticado próximo ao topo de 24h |
| **SOLUSDT** | $94.99 | ⚪ **CASH** | **+21.1 bps** (±13.6) | `+35.4 bps` | `-0.010 / +0.057` | `0.42%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 02:47:35 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,486.33 | ⚪ **CASH** | **+21.3 bps** (±2.3) | `+24.2 bps` | `+0.050 / +0.115` | `0.25%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,294.94 | ⚪ **CASH** | **+32.9 bps** (±8.9) | `+34.6 bps` | `+0.099 / +0.224` | `0.29%/h` | `stretched_top` | Filtro: preço esticado próximo ao topo de 24h |
| **SOLUSDT** | $95.03 | ⚪ **CASH** | **+18.5 bps** (±10.9) | `+28.9 bps` | `-0.013 / +0.083` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 02:32:20 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,522.01 | ⚪ **CASH** | **+21.3 bps** (±2.3) | `+24.2 bps` | `+0.050 / +0.115` | `0.25%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,296.12 | ⚪ **CASH** | **+32.9 bps** (±8.9) | `+34.6 bps` | `+0.099 / +0.224` | `0.29%/h` | `stretched_top` | Filtro: preço esticado próximo ao topo de 24h |
| **SOLUSDT** | $95.15 | ⚪ **CASH** | **+18.5 bps** (±10.9) | `+28.9 bps` | `-0.013 / +0.083` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 02:17:26 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,480.01 | ⚪ **CASH** | **+21.3 bps** (±2.3) | `+24.2 bps` | `+0.050 / +0.115` | `0.25%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,295.88 | ⚪ **CASH** | **+32.9 bps** (±8.9) | `+34.6 bps` | `+0.099 / +0.224` | `0.29%/h` | `stretched_top` | Filtro: preço esticado próximo ao topo de 24h |
| **SOLUSDT** | $95.09 | ⚪ **CASH** | **+18.5 bps** (±10.9) | `+28.9 bps` | `-0.013 / +0.083` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 02:02:31 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,404.01 | ⚪ **CASH** | **+21.3 bps** (±2.3) | `+24.2 bps` | `+0.050 / +0.115` | `0.25%/h` | `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,291.22 | ⚪ **CASH** | **+32.9 bps** (±8.9) | `+34.6 bps` | `+0.099 / +0.224` | `0.29%/h` | `stretched_top` | Filtro: preço esticado próximo ao topo de 24h |
| **SOLUSDT** | $94.97 | ⚪ **CASH** | **+18.5 bps** (±10.9) | `+28.9 bps` | `-0.013 / +0.083` | `0.44%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 01:47:29 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,566.00 | ⚪ **CASH** | **+11.9 bps** (±4.0) | `+16.2 bps` | `+0.032 / +0.023` | `0.25%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,295.82 | ⚪ **CASH** | **+12.4 bps** (±3.7) | `+5.5 bps` | `+0.066 / +0.147` | `0.28%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.17 | ⚪ **CASH** | **+13.0 bps** (±6.5) | `+20.7 bps` | `-0.018 / +0.068` | `0.42%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 01:32:33 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,596.00 | ⚪ **CASH** | **+11.9 bps** (±4.0) | `+16.2 bps` | `+0.032 / +0.023` | `0.25%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,293.19 | ⚪ **CASH** | **+12.4 bps** (±3.7) | `+5.5 bps` | `+0.066 / +0.147` | `0.28%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $95.25 | ⚪ **CASH** | **+13.0 bps** (±6.5) | `+20.7 bps` | `-0.018 / +0.068` | `0.42%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 01:18:01 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,373.97 | ⚪ **CASH** | **+11.9 bps** (±4.0) | `+16.2 bps` | `+0.032 / +0.023` | `0.25%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,287.11 | ⚪ **CASH** | **+12.4 bps** (±3.7) | `+5.5 bps` | `+0.066 / +0.147` | `0.28%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.95 | ⚪ **CASH** | **+13.0 bps** (±6.5) | `+20.7 bps` | `-0.018 / +0.068` | `0.42%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 01:02:24 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,165.43 | ⚪ **CASH** | **+11.9 bps** (±4.0) | `+16.2 bps` | `+0.032 / +0.023` | `0.25%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,273.77 | ⚪ **CASH** | **+12.4 bps** (±3.7) | `+5.5 bps` | `+0.066 / +0.147` | `0.28%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.13 | ⚪ **CASH** | **+13.0 bps** (±6.5) | `+20.7 bps` | `-0.018 / +0.068` | `0.42%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 00:47:40 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,133.88 | ⚪ **CASH** | **+13.0 bps** (±6.4) | `+18.1 bps` | `+0.039 / +0.014` | `0.25%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,271.80 | ⚪ **CASH** | **+22.8 bps** (±1.9) | `+32.5 bps` | `+0.039 / +0.053` | `0.30%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.13 | ⚪ **CASH** | **+14.6 bps** (±12.2) | `+22.9 bps` | `-0.007 / +0.071` | `0.42%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 00:32:51 UTC` | Patrimônio: **$970.45 USDT** (Caixa: `$970.45`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,122.00 | ⚪ **CASH** | **+13.0 bps** (±6.4) | `+18.1 bps` | `+0.039 / +0.014` | `0.25%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **ETHUSDT** | $2,273.21 | ⚪ **CASH** | **+22.8 bps** (±1.9) | `+32.5 bps` | `+0.039 / +0.053` | `0.30%/h` | `vol_compressed` `stretched_top` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $94.21 | ⚪ **CASH** | **+14.6 bps** (±12.2) | `+22.9 bps` | `-0.007 / +0.071` | `0.42%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

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
