# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-02 16:02:25 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-02 16:02:25 UTC` | Patrimônio: **$961.33 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,574.97 | 🟡 **HOLD** | **+26.3 bps** (±10.2) | `+32.7 bps` | `+0.078 / +0.082` | `0.22%/h` | `vol_compressed` | Posição ativa há 11.0h (PnL: -1.09% | Pico: +0.00%) |
| **ETHUSDT** | $2,275.95 | 🟡 **HOLD** | **+45.5 bps** (±9.6) | `+96.8 bps` | `-0.057 / -0.162` | `0.32%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 11.0h (PnL: -0.76% | Pico: +0.31%) |
| **SOLUSDT** | $93.58 | ⚪ **CASH** | **+18.3 bps** (±14.9) | `+17.4 bps` | `+0.089 / +0.091` | `0.38%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 15:47:18 UTC` | Patrimônio: **$963.38 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,983.85 | 🟡 **HOLD** | **+27.0 bps** (±7.0) | `+32.0 bps` | `+0.089 / +0.081` | `0.21%/h` | `vol_compressed` | Posição ativa há 10.7h (PnL: -0.57% | Pico: +0.00%) |
| **ETHUSDT** | $2,290.83 | 🟡 **HOLD** | **+43.9 bps** (±11.7) | `+95.2 bps` | `-0.046 / -0.200` | `0.28%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 10.7h (PnL: -0.11% | Pico: +0.31%) |
| **SOLUSDT** | $94.26 | ⚪ **CASH** | **+24.5 bps** (±20.0) | `+23.9 bps` | `+0.104 / +0.147` | `0.36%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-02 15:32:29 UTC` | Patrimônio: **$962.96 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,855.10 | 🟡 **HOLD** | **+27.0 bps** (±7.0) | `+32.0 bps` | `+0.089 / +0.081` | `0.21%/h` | `vol_compressed` | Posição ativa há 10.5h (PnL: -0.74% | Pico: +0.00%) |
| **ETHUSDT** | $2,289.80 | 🟡 **HOLD** | **+43.9 bps** (±11.7) | `+95.2 bps` | `-0.046 / -0.200` | `0.28%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 10.5h (PnL: -0.16% | Pico: +0.31%) |
| **SOLUSDT** | $94.13 | ⚪ **CASH** | **+24.5 bps** (±20.0) | `+23.9 bps` | `+0.104 / +0.147` | `0.36%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-02 15:17:19 UTC` | Patrimônio: **$963.58 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,978.00 | 🟡 **HOLD** | **+27.0 bps** (±7.0) | `+32.0 bps` | `+0.089 / +0.081` | `0.21%/h` | `vol_compressed` | Posição ativa há 10.2h (PnL: -0.58% | Pico: +0.00%) |
| **ETHUSDT** | $2,294.26 | 🟡 **HOLD** | **+43.9 bps** (±11.7) | `+95.2 bps` | `-0.046 / -0.200` | `0.28%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 10.2h (PnL: +0.04% | Pico: +0.31%) |
| **SOLUSDT** | $94.47 | ⚪ **CASH** | **+24.5 bps** (±20.0) | `+23.9 bps` | `+0.104 / +0.147` | `0.36%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-02 15:02:24 UTC` | Patrimônio: **$962.64 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,805.65 | 🟡 **HOLD** | **+27.0 bps** (±7.0) | `+32.0 bps` | `+0.089 / +0.081` | `0.21%/h` | `vol_compressed` | Posição ativa há 10.0h (PnL: -0.80% | Pico: +0.00%) |
| **ETHUSDT** | $2,286.81 | 🟡 **HOLD** | **+43.9 bps** (±11.7) | `+95.2 bps` | `-0.046 / -0.200` | `0.28%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 10.0h (PnL: -0.29% | Pico: +0.31%) |
| **SOLUSDT** | $94.22 | ⚪ **CASH** | **+24.5 bps** (±20.0) | `+23.9 bps` | `+0.104 / +0.147` | `0.36%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-02 14:47:28 UTC` | Patrimônio: **$963.38 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,934.00 | 🟡 **HOLD** | **+27.5 bps** (±12.0) | `+39.3 bps` | `+0.066 / +0.048` | `0.21%/h` | `vol_compressed` | Posição ativa há 9.7h (PnL: -0.64% | Pico: +0.00%) |
| **ETHUSDT** | $2,292.94 | 🟡 **HOLD** | **+59.4 bps** (±9.1) | `+124.3 bps` | `-0.049 / -0.201` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 9.7h (PnL: -0.02% | Pico: +0.31%) |
| **SOLUSDT** | $94.49 | ⚪ **CASH** | **+18.8 bps** (±18.3) | `+14.8 bps` | `+0.097 / +0.153` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 14:32:34 UTC` | Patrimônio: **$963.60 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,017.13 | 🟡 **HOLD** | **+27.5 bps** (±12.0) | `+39.3 bps` | `+0.066 / +0.048` | `0.21%/h` | `vol_compressed` | Posição ativa há 9.5h (PnL: -0.53% | Pico: +0.00%) |
| **ETHUSDT** | $2,292.97 | 🟡 **HOLD** | **+59.4 bps** (±9.1) | `+124.3 bps` | `-0.049 / -0.201` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 9.5h (PnL: -0.02% | Pico: +0.31%) |
| **SOLUSDT** | $94.43 | ⚪ **CASH** | **+18.8 bps** (±18.3) | `+14.8 bps` | `+0.097 / +0.153` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 14:17:37 UTC` | Patrimônio: **$963.37 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,955.29 | 🟡 **HOLD** | **+27.5 bps** (±12.0) | `+39.3 bps` | `+0.066 / +0.048` | `0.21%/h` | `vol_compressed` | Posição ativa há 9.3h (PnL: -0.61% | Pico: +0.00%) |
| **ETHUSDT** | $2,291.85 | 🟡 **HOLD** | **+59.4 bps** (±9.1) | `+124.3 bps` | `-0.049 / -0.201` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 9.3h (PnL: -0.07% | Pico: +0.31%) |
| **SOLUSDT** | $94.22 | ⚪ **CASH** | **+18.8 bps** (±18.3) | `+14.8 bps` | `+0.097 / +0.153` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 14:02:37 UTC` | Patrimônio: **$963.34 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,988.00 | 🟡 **HOLD** | **+27.5 bps** (±12.0) | `+39.3 bps` | `+0.066 / +0.048` | `0.21%/h` | `vol_compressed` | Posição ativa há 9.0h (PnL: -0.57% | Pico: +0.00%) |
| **ETHUSDT** | $2,290.05 | 🟡 **HOLD** | **+59.4 bps** (±9.1) | `+124.3 bps` | `-0.049 / -0.201` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 9.0h (PnL: -0.15% | Pico: +0.31%) |
| **SOLUSDT** | $94.45 | ⚪ **CASH** | **+18.8 bps** (±18.3) | `+14.8 bps` | `+0.097 / +0.153` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 13:47:24 UTC` | Patrimônio: **$964.21 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,143.40 | 🟡 **HOLD** | **+29.7 bps** (±13.9) | `+44.9 bps` | `+0.064 / +0.033` | `0.21%/h` | `vol_compressed` | Posição ativa há 8.7h (PnL: -0.37% | Pico: +0.00%) |
| **ETHUSDT** | $2,297.08 | 🟡 **HOLD** | **+28.9 bps** (±9.8) | `+79.1 bps` | `-0.064 / -0.328` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 8.7h (PnL: +0.16% | Pico: +0.31%) |
| **SOLUSDT** | $94.85 | ⚪ **CASH** | **+29.4 bps** (±14.1) | `+34.9 bps` | `+0.086 / +0.145` | `0.38%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-02 13:32:33 UTC` | Patrimônio: **$961.74 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,653.85 | 🟡 **HOLD** | **+29.7 bps** (±13.9) | `+44.9 bps` | `+0.064 / +0.033` | `0.21%/h` | `vol_compressed` | Posição ativa há 8.5h (PnL: -0.99% | Pico: +0.00%) |
| **ETHUSDT** | $2,279.02 | 🟡 **HOLD** | **+28.9 bps** (±9.8) | `+79.1 bps` | `-0.064 / -0.328` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 8.5h (PnL: -0.63% | Pico: +0.31%) |
| **SOLUSDT** | $93.80 | ⚪ **CASH** | **+29.4 bps** (±14.1) | `+34.9 bps` | `+0.086 / +0.145` | `0.38%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-02 13:17:12 UTC` | Patrimônio: **$962.02 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,692.00 | 🟡 **HOLD** | **+29.7 bps** (±13.9) | `+44.9 bps` | `+0.064 / +0.033` | `0.21%/h` | `vol_compressed` | Posição ativa há 8.2h (PnL: -0.94% | Pico: +0.00%) |
| **ETHUSDT** | $2,281.88 | 🟡 **HOLD** | **+28.9 bps** (±9.8) | `+79.1 bps` | `-0.064 / -0.328` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 8.2h (PnL: -0.50% | Pico: +0.31%) |
| **SOLUSDT** | $93.87 | ⚪ **CASH** | **+29.4 bps** (±14.1) | `+34.9 bps` | `+0.086 / +0.145` | `0.38%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-02 13:02:44 UTC` | Patrimônio: **$962.21 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,730.83 | 🟡 **HOLD** | **+29.7 bps** (±13.9) | `+44.9 bps` | `+0.064 / +0.033` | `0.21%/h` | `vol_compressed` | Posição ativa há 8.0h (PnL: -0.89% | Pico: +0.00%) |
| **ETHUSDT** | $2,283.12 | 🟡 **HOLD** | **+28.9 bps** (±9.8) | `+79.1 bps` | `-0.064 / -0.328` | `0.29%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 8.0h (PnL: -0.45% | Pico: +0.31%) |
| **SOLUSDT** | $94.02 | ⚪ **CASH** | **+29.4 bps** (±14.1) | `+34.9 bps` | `+0.086 / +0.145` | `0.38%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-02 12:47:44 UTC` | Patrimônio: **$962.83 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,874.00 | 🟡 **HOLD** | **+29.4 bps** (±11.6) | `+49.8 bps` | `+0.046 / -0.014` | `0.21%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 7.8h (PnL: -0.71% | Pico: +0.00%) |
| **ETHUSDT** | $2,286.91 | 🟡 **HOLD** | **+21.5 bps** (±9.2) | `+73.7 bps` | `-0.088 / -0.405` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 7.8h (PnL: -0.28% | Pico: +0.31%) |
| **SOLUSDT** | $94.22 | ⚪ **CASH** | **+25.1 bps** (±11.3) | `+30.6 bps` | `+0.069 / +0.122` | `0.39%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-02 12:32:27 UTC` | Patrimônio: **$963.32 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,956.31 | 🟡 **HOLD** | **+29.4 bps** (±11.6) | `+49.8 bps` | `+0.046 / -0.014` | `0.21%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 7.5h (PnL: -0.61% | Pico: +0.00%) |
| **ETHUSDT** | $2,291.12 | 🟡 **HOLD** | **+21.5 bps** (±9.2) | `+73.7 bps` | `-0.088 / -0.405` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 7.5h (PnL: -0.10% | Pico: +0.31%) |
| **SOLUSDT** | $94.30 | ⚪ **CASH** | **+25.1 bps** (±11.3) | `+30.6 bps` | `+0.069 / +0.122` | `0.39%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-02 12:17:26 UTC` | Patrimônio: **$963.70 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,040.01 | 🟡 **HOLD** | **+29.4 bps** (±11.6) | `+49.8 bps` | `+0.046 / -0.014` | `0.21%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 7.2h (PnL: -0.50% | Pico: +0.00%) |
| **ETHUSDT** | $2,293.42 | 🟡 **HOLD** | **+21.5 bps** (±9.2) | `+73.7 bps` | `-0.088 / -0.405` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 7.2h (PnL: +0.00% | Pico: +0.31%) |
| **SOLUSDT** | $94.53 | ⚪ **CASH** | **+25.1 bps** (±11.3) | `+30.6 bps` | `+0.069 / +0.122` | `0.39%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-02 12:02:25 UTC` | Patrimônio: **$962.91 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,901.72 | 🟡 **HOLD** | **+29.4 bps** (±11.6) | `+49.8 bps` | `+0.046 / -0.014` | `0.21%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 7.0h (PnL: -0.68% | Pico: +0.00%) |
| **ETHUSDT** | $2,286.96 | 🟡 **HOLD** | **+21.5 bps** (±9.2) | `+73.7 bps` | `-0.088 / -0.405` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 7.0h (PnL: -0.28% | Pico: +0.31%) |
| **SOLUSDT** | $94.15 | ⚪ **CASH** | **+25.1 bps** (±11.3) | `+30.6 bps` | `+0.069 / +0.122` | `0.39%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-02 11:47:42 UTC` | Patrimônio: **$962.36 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,794.64 | 🟡 **HOLD** | **+28.5 bps** (±8.5) | `+45.6 bps` | `+0.051 / +0.005` | `0.22%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 6.8h (PnL: -0.81% | Pico: +0.00%) |
| **ETHUSDT** | $2,282.86 | 🟡 **HOLD** | **+24.8 bps** (±10.0) | `+77.4 bps` | `-0.070 / -0.398` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 6.8h (PnL: -0.46% | Pico: +0.31%) |
| **SOLUSDT** | $93.79 | ⚪ **CASH** | **+23.7 bps** (±8.2) | `+30.4 bps` | `+0.059 / +0.091` | `0.39%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 11:32:31 UTC` | Patrimônio: **$962.63 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,850.01 | 🟡 **HOLD** | **+28.5 bps** (±8.5) | `+45.6 bps` | `+0.051 / +0.005` | `0.22%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 6.5h (PnL: -0.74% | Pico: +0.00%) |
| **ETHUSDT** | $2,284.71 | 🟡 **HOLD** | **+24.8 bps** (±10.0) | `+77.4 bps` | `-0.070 / -0.398` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 6.5h (PnL: -0.38% | Pico: +0.31%) |
| **SOLUSDT** | $93.93 | ⚪ **CASH** | **+23.7 bps** (±8.2) | `+30.4 bps` | `+0.059 / +0.091` | `0.39%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 11:17:37 UTC` | Patrimônio: **$962.86 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,910.01 | 🟡 **HOLD** | **+28.5 bps** (±8.5) | `+45.6 bps` | `+0.051 / +0.005` | `0.22%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 6.3h (PnL: -0.67% | Pico: +0.00%) |
| **ETHUSDT** | $2,285.78 | 🟡 **HOLD** | **+24.8 bps** (±10.0) | `+77.4 bps` | `-0.070 / -0.398` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 6.3h (PnL: -0.33% | Pico: +0.31%) |
| **SOLUSDT** | $93.90 | ⚪ **CASH** | **+23.7 bps** (±8.2) | `+30.4 bps` | `+0.059 / +0.091` | `0.39%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 11:02:29 UTC` | Patrimônio: **$963.22 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,996.00 | 🟡 **HOLD** | **+28.5 bps** (±8.5) | `+45.6 bps` | `+0.051 / +0.005` | `0.22%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 6.0h (PnL: -0.56% | Pico: +0.00%) |
| **ETHUSDT** | $2,287.77 | 🟡 **HOLD** | **+24.8 bps** (±10.0) | `+77.4 bps` | `-0.070 / -0.398` | `0.30%/h` | `vol_compressed` `weak_order_flow` | Posição ativa há 6.0h (PnL: -0.25% | Pico: +0.31%) |
| **SOLUSDT** | $94.23 | ⚪ **CASH** | **+23.7 bps** (±8.2) | `+30.4 bps` | `+0.059 / +0.091` | `0.39%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-11-02 10:47:41 UTC` | Patrimônio: **$963.21 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,025.78 | 🟡 **HOLD** | **+29.8 bps** (±8.0) | `+45.3 bps` | `+0.058 / +0.028` | `0.22%/h` | `vol_compressed` | Posição ativa há 5.8h (PnL: -0.52% | Pico: +0.00%) |
| **ETHUSDT** | $2,286.30 | 🟡 **HOLD** | **-0.3 bps** (±9.0) | `+19.6 bps` | `-0.012 / -0.308` | `0.31%/h` | `weak_order_flow` | Posição ativa há 5.8h (PnL: -0.31% | Pico: +0.31%) |
| **SOLUSDT** | $94.14 | ⚪ **CASH** | **+24.6 bps** (±10.3) | `+33.2 bps` | `+0.049 / +0.086` | `0.40%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |

---

### 🕒 Ciclo `2026-11-02 10:32:29 UTC` | Patrimônio: **$963.22 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,003.90 | 🟡 **HOLD** | **+29.8 bps** (±8.0) | `+45.3 bps` | `+0.058 / +0.028` | `0.22%/h` | `vol_compressed` | Posição ativa há 5.5h (PnL: -0.55% | Pico: +0.00%) |
| **ETHUSDT** | $2,287.42 | 🟡 **HOLD** | **-0.3 bps** (±9.0) | `+19.6 bps` | `-0.012 / -0.308` | `0.31%/h` | `weak_order_flow` | Posição ativa há 5.5h (PnL: -0.26% | Pico: +0.31%) |
| **SOLUSDT** | $94.15 | ⚪ **CASH** | **+24.6 bps** (±10.3) | `+33.2 bps` | `+0.049 / +0.086` | `0.40%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-11-02 10:17:30 UTC` | Patrimônio: **$963.15 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $77,983.86 | 🟡 **HOLD** | **+29.8 bps** (±8.0) | `+45.3 bps` | `+0.058 / +0.028` | `0.22%/h` | `vol_compressed` | Posição ativa há 5.2h (PnL: -0.57% | Pico: +0.00%) |
| **ETHUSDT** | $2,287.12 | 🟡 **HOLD** | **-0.3 bps** (±9.0) | `+19.6 bps` | `-0.012 / -0.308` | `0.31%/h` | `weak_order_flow` | Posição ativa há 5.2h (PnL: -0.27% | Pico: +0.31%) |
| **SOLUSDT** | $94.14 | ⚪ **CASH** | **+24.6 bps** (±10.3) | `+33.2 bps` | `+0.049 / +0.086` | `0.40%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-11-02 10:02:54 UTC` | Patrimônio: **$963.21 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,004.32 | 🟡 **HOLD** | **+29.8 bps** (±8.0) | `+45.3 bps` | `+0.058 / +0.028` | `0.22%/h` | `vol_compressed` | Posição ativa há 5.0h (PnL: -0.55% | Pico: +0.00%) |
| **ETHUSDT** | $2,287.20 | 🟡 **HOLD** | **-0.3 bps** (±9.0) | `+19.6 bps` | `-0.012 / -0.308` | `0.31%/h` | `weak_order_flow` | Posição ativa há 5.0h (PnL: -0.27% | Pico: +0.31%) |
| **SOLUSDT** | $94.12 | ⚪ **CASH** | **+24.6 bps** (±10.3) | `+33.2 bps` | `+0.049 / +0.086` | `0.40%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-11-02 09:47:53 UTC` | Patrimônio: **$963.99 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,161.71 | 🟡 **HOLD** | **+31.3 bps** (±4.1) | `+38.0 bps` | `+0.069 / +0.145` | `0.22%/h` | `vol_compressed` | Posição ativa há 4.8h (PnL: -0.35% | Pico: +0.00%) |
| **ETHUSDT** | $2,292.75 | 🟡 **HOLD** | **+28.6 bps** (±9.8) | `+59.7 bps` | `+0.023 / -0.176` | `0.31%/h` | `weak_order_flow` | Posição ativa há 4.8h (PnL: -0.03% | Pico: +0.31%) |
| **SOLUSDT** | $94.53 | ⚪ **CASH** | **+30.9 bps** (±18.0) | `+43.0 bps` | `+0.034 / +0.149` | `0.40%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-11-02 09:32:24 UTC` | Patrimônio: **$963.71 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,126.25 | 🟡 **HOLD** | **+31.3 bps** (±4.1) | `+38.0 bps` | `+0.069 / +0.145` | `0.22%/h` | `vol_compressed` | Posição ativa há 4.5h (PnL: -0.39% | Pico: +0.00%) |
| **ETHUSDT** | $2,289.87 | 🟡 **HOLD** | **+28.6 bps** (±9.8) | `+59.7 bps` | `+0.023 / -0.176` | `0.31%/h` | `weak_order_flow` | Posição ativa há 4.5h (PnL: -0.15% | Pico: +0.31%) |
| **SOLUSDT** | $94.45 | ⚪ **CASH** | **+30.9 bps** (±18.0) | `+43.0 bps` | `+0.034 / +0.149` | `0.40%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-11-02 09:17:20 UTC` | Patrimônio: **$964.61 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,270.15 | 🟡 **HOLD** | **+31.3 bps** (±4.1) | `+38.0 bps` | `+0.069 / +0.145` | `0.22%/h` | `vol_compressed` | Posição ativa há 4.2h (PnL: -0.21% | Pico: +0.00%) |
| **ETHUSDT** | $2,298.01 | 🟡 **HOLD** | **+28.6 bps** (±9.8) | `+59.7 bps` | `+0.023 / -0.176` | `0.31%/h` | `weak_order_flow` | Posição ativa há 4.2h (PnL: +0.20% | Pico: +0.31%) |
| **SOLUSDT** | $94.76 | ⚪ **CASH** | **+30.9 bps** (±18.0) | `+43.0 bps` | `+0.034 / +0.149` | `0.40%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-11-02 09:02:30 UTC` | Patrimônio: **$964.86 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,305.29 | 🟡 **HOLD** | **+31.3 bps** (±4.1) | `+38.0 bps` | `+0.069 / +0.145` | `0.22%/h` | `vol_compressed` | Posição ativa há 4.0h (PnL: -0.16% | Pico: +0.00%) |
| **ETHUSDT** | $2,300.45 | 🟡 **HOLD** | **+28.6 bps** (±9.8) | `+59.7 bps` | `+0.023 / -0.176` | `0.31%/h` | `weak_order_flow` | Posição ativa há 4.0h (PnL: +0.31% | Pico: +0.31%) |
| **SOLUSDT** | $94.78 | ⚪ **CASH** | **+30.9 bps** (±18.0) | `+43.0 bps` | `+0.034 / +0.149` | `0.40%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-11-02 08:47:35 UTC` | Patrimônio: **$964.88 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,333.70 | 🟡 **HOLD** | **+30.2 bps** (±6.3) | `+41.6 bps` | `+0.047 / +0.113` | `0.22%/h` | `vol_compressed` | Posição ativa há 3.8h (PnL: -0.13% | Pico: +0.00%) |
| **ETHUSDT** | $2,299.48 | 🟡 **HOLD** | **+21.8 bps** (±11.9) | `+44.2 bps` | `+0.026 / -0.111` | `0.30%/h` | `weak_order_flow` | Posição ativa há 3.8h (PnL: +0.27% | Pico: +0.27%) |
| **SOLUSDT** | $94.78 | ⚪ **CASH** | **+30.7 bps** (±14.7) | `+44.7 bps` | `+0.033 / +0.125` | `0.40%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-11-02 08:32:19 UTC` | Patrimônio: **$964.22 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,206.01 | 🟡 **HOLD** | **+30.2 bps** (±6.3) | `+41.6 bps` | `+0.047 / +0.113` | `0.22%/h` | `vol_compressed` | Posição ativa há 3.5h (PnL: -0.29% | Pico: +0.00%) |
| **ETHUSDT** | $2,294.56 | 🟡 **HOLD** | **+21.8 bps** (±11.9) | `+44.2 bps` | `+0.026 / -0.111` | `0.30%/h` | `weak_order_flow` | Posição ativa há 3.5h (PnL: +0.05% | Pico: +0.05%) |
| **SOLUSDT** | $94.52 | ⚪ **CASH** | **+30.7 bps** (±14.7) | `+44.7 bps` | `+0.033 / +0.125` | `0.40%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-11-02 08:17:33 UTC` | Patrimônio: **$963.85 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,169.99 | 🟡 **HOLD** | **+30.2 bps** (±6.3) | `+41.6 bps` | `+0.047 / +0.113` | `0.22%/h` | `vol_compressed` | Posição ativa há 3.2h (PnL: -0.34% | Pico: +0.00%) |
| **ETHUSDT** | $2,290.29 | 🟡 **HOLD** | **+21.8 bps** (±11.9) | `+44.2 bps` | `+0.026 / -0.111` | `0.30%/h` | `weak_order_flow` | Posição ativa há 3.2h (PnL: -0.14% | Pico: +0.04%) |
| **SOLUSDT** | $94.37 | ⚪ **CASH** | **+30.7 bps** (±14.7) | `+44.7 bps` | `+0.033 / +0.125` | `0.40%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-11-02 08:02:28 UTC` | Patrimônio: **$963.86 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,173.27 | 🟡 **HOLD** | **+30.2 bps** (±6.3) | `+41.6 bps` | `+0.047 / +0.113` | `0.22%/h` | `vol_compressed` | Posição ativa há 3.0h (PnL: -0.33% | Pico: +0.00%) |
| **ETHUSDT** | $2,290.22 | 🟡 **HOLD** | **+21.8 bps** (±11.9) | `+44.2 bps` | `+0.026 / -0.111` | `0.30%/h` | `weak_order_flow` | Posição ativa há 3.0h (PnL: -0.14% | Pico: +0.04%) |
| **SOLUSDT** | $94.41 | ⚪ **CASH** | **+30.7 bps** (±14.7) | `+44.7 bps` | `+0.033 / +0.125` | `0.40%/h` | `vol_compressed` `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-11-02 07:47:22 UTC` | Patrimônio: **$962.73 USDT** (Caixa: `$606.74`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,004.20 | 🟡 **HOLD** | **+33.7 bps** (±5.0) | `+44.1 bps` | `+0.055 / +0.151` | `0.23%/h` | `vol_compressed` | Posição ativa há 2.7h (PnL: -0.55% | Pico: +0.00%) |
| **ETHUSDT** | $2,279.52 | 🟡 **HOLD** | **+17.1 bps** (±7.2) | `+16.5 bps` | `+0.078 / +0.087` | `0.31%/h` | Liberado ✅ | Posição ativa há 2.7h (PnL: -0.60% | Pico: +0.04%) |
| **SOLUSDT** | $94.29 | 🔴 **SELL** | **+22.2 bps** (±4.4) | `+28.5 bps` | `+0.028 / +0.109` | `0.41%/h` | Liberado ✅ | Stop Loss técnico acionado (-1.40%) |

---

### 🕒 Ciclo `2026-11-02 07:32:31 UTC` | Patrimônio: **$964.03 USDT** (Caixa: `$291.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,108.00 | 🟡 **HOLD** | **+33.7 bps** (±5.0) | `+44.1 bps` | `+0.055 / +0.151` | `0.23%/h` | `vol_compressed` | Posição ativa há 2.5h (PnL: -0.41% | Pico: +0.00%) |
| **ETHUSDT** | $2,282.82 | 🟡 **HOLD** | **+17.1 bps** (±7.2) | `+16.5 bps` | `+0.078 / +0.087` | `0.31%/h` | Liberado ✅ | Posição ativa há 2.5h (PnL: -0.46% | Pico: +0.04%) |
| **SOLUSDT** | $94.42 | 🟡 **HOLD** | **+22.2 bps** (±4.4) | `+28.5 bps` | `+0.028 / +0.109` | `0.41%/h` | Liberado ✅ | Posição ativa há 3.5h (PnL: -1.27% | Pico: +0.02%) |

---

### 🕒 Ciclo `2026-11-02 07:17:14 UTC` | Patrimônio: **$964.01 USDT** (Caixa: `$291.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $78,161.13 | 🟡 **HOLD** | **+33.7 bps** (±5.0) | `+44.1 bps` | `+0.055 / +0.151` | `0.23%/h` | `vol_compressed` | Posição ativa há 2.2h (PnL: -0.35% | Pico: +0.00%) |
| **ETHUSDT** | $2,284.91 | 🟡 **HOLD** | **+17.1 bps** (±7.2) | `+16.5 bps` | `+0.078 / +0.087` | `0.31%/h` | Liberado ✅ | Posição ativa há 2.2h (PnL: -0.37% | Pico: +0.04%) |
| **SOLUSDT** | $94.33 | 🟡 **HOLD** | **+22.2 bps** (±4.4) | `+28.5 bps` | `+0.028 / +0.109` | `0.41%/h` | Liberado ✅ | Posição ativa há 3.2h (PnL: -1.36% | Pico: +0.02%) |
