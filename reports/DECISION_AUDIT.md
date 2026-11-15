# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-15 22:00:52 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-15 22:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,940.01 | ⚪ **CASH** | **+1.8 bps** (±8.2) | `+34.3 bps` | `-0.068 / -0.299` | `0.82%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,818.05 | ⚪ **CASH** | **-4.9 bps** (±14.2) | `+14.2 bps` | `-0.062 / -0.168` | `1.06%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.87 | ⚪ **CASH** | **-20.6 bps** (±20.2) | `-23.9 bps` | `-0.070 / +0.005` | `1.16%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (20.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 21:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,086.49 | ⚪ **CASH** | **+1.6 bps** (±14.7) | `+30.9 bps` | `-0.061 / -0.248` | `0.83%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,822.48 | ⚪ **CASH** | **+44.7 bps** (±15.8) | `+105.4 bps` | `-0.063 / -0.183` | `1.07%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $72.05 | ⚪ **CASH** | **-25.7 bps** (±17.7) | `-31.7 bps` | `-0.076 / -0.019` | `1.17%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-15 21:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,966.01 | ⚪ **CASH** | **+1.6 bps** (±14.7) | `+30.9 bps` | `-0.061 / -0.248` | `0.83%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,816.79 | ⚪ **CASH** | **+44.7 bps** (±15.8) | `+105.4 bps` | `-0.063 / -0.183` | `1.07%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $71.78 | ⚪ **CASH** | **-25.7 bps** (±17.7) | `-31.7 bps` | `-0.076 / -0.019` | `1.17%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-15 21:15:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,008.01 | ⚪ **CASH** | **+1.6 bps** (±14.7) | `+30.9 bps` | `-0.061 / -0.248` | `0.83%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,821.11 | ⚪ **CASH** | **+44.7 bps** (±15.8) | `+105.4 bps` | `-0.063 / -0.183` | `1.07%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $71.80 | ⚪ **CASH** | **-25.7 bps** (±17.7) | `-31.7 bps` | `-0.076 / -0.019` | `1.17%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-15 21:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,068.29 | ⚪ **CASH** | **+1.6 bps** (±14.7) | `+30.9 bps` | `-0.061 / -0.248` | `0.83%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,823.57 | ⚪ **CASH** | **+44.7 bps** (±15.8) | `+105.4 bps` | `-0.063 / -0.183` | `1.07%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $71.80 | ⚪ **CASH** | **-25.7 bps** (±17.7) | `-31.7 bps` | `-0.076 / -0.019` | `1.17%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-15 20:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,988.01 | ⚪ **CASH** | **+0.9 bps** (±22.1) | `+31.2 bps` | `-0.068 / -0.238` | `0.84%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,826.92 | ⚪ **CASH** | **+22.0 bps** (±33.6) | `+70.9 bps` | `-0.077 / -0.212` | `1.09%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.6 bps > 19.5) |
| **SOLUSDT** | $71.88 | ⚪ **CASH** | **-17.3 bps** (±49.9) | `-7.1 bps` | `-0.080 / -0.063` | `1.19%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (49.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 20:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,918.01 | ⚪ **CASH** | **+0.9 bps** (±22.1) | `+31.2 bps` | `-0.068 / -0.238` | `0.84%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,825.57 | ⚪ **CASH** | **+22.0 bps** (±33.6) | `+70.9 bps` | `-0.077 / -0.212` | `1.09%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.6 bps > 19.5) |
| **SOLUSDT** | $71.67 | ⚪ **CASH** | **-17.3 bps** (±49.9) | `-7.1 bps` | `-0.080 / -0.063` | `1.19%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (49.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 20:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,720.01 | ⚪ **CASH** | **+0.9 bps** (±22.1) | `+31.2 bps` | `-0.068 / -0.238` | `0.84%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,817.68 | ⚪ **CASH** | **+22.0 bps** (±33.6) | `+70.9 bps` | `-0.077 / -0.212` | `1.09%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.6 bps > 19.5) |
| **SOLUSDT** | $71.25 | ⚪ **CASH** | **-17.3 bps** (±49.9) | `-7.1 bps` | `-0.080 / -0.063` | `1.19%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (49.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 20:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,896.01 | ⚪ **CASH** | **+0.9 bps** (±22.1) | `+31.2 bps` | `-0.068 / -0.238` | `0.84%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,822.11 | ⚪ **CASH** | **+22.0 bps** (±33.6) | `+70.9 bps` | `-0.077 / -0.212` | `1.09%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.6 bps > 19.5) |
| **SOLUSDT** | $71.59 | ⚪ **CASH** | **-17.3 bps** (±49.9) | `-7.1 bps` | `-0.080 / -0.063` | `1.19%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (49.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 19:45:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,980.86 | ⚪ **CASH** | **+9.0 bps** (±23.3) | `+43.3 bps` | `-0.064 / -0.203` | `0.85%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.3 bps > 19.5) |
| **ETHUSDT** | $1,825.76 | ⚪ **CASH** | **+12.9 bps** (±35.2) | `+55.2 bps` | `-0.077 / -0.223` | `1.10%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (35.2 bps > 19.5) |
| **SOLUSDT** | $71.82 | ⚪ **CASH** | **-37.3 bps** (±28.9) | `-44.7 bps` | `-0.087 / -0.095` | `1.19%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 19:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,980.00 | ⚪ **CASH** | **+9.0 bps** (±23.3) | `+43.3 bps` | `-0.064 / -0.203` | `0.85%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.3 bps > 19.5) |
| **ETHUSDT** | $1,826.51 | ⚪ **CASH** | **+12.9 bps** (±35.2) | `+55.2 bps` | `-0.077 / -0.223` | `1.10%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (35.2 bps > 19.5) |
| **SOLUSDT** | $71.68 | ⚪ **CASH** | **-37.3 bps** (±28.9) | `-44.7 bps` | `-0.087 / -0.095` | `1.19%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 19:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,019.16 | ⚪ **CASH** | **+9.0 bps** (±23.3) | `+43.3 bps` | `-0.064 / -0.203` | `0.85%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.3 bps > 19.5) |
| **ETHUSDT** | $1,823.92 | ⚪ **CASH** | **+12.9 bps** (±35.2) | `+55.2 bps` | `-0.077 / -0.223` | `1.10%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (35.2 bps > 19.5) |
| **SOLUSDT** | $71.59 | ⚪ **CASH** | **-37.3 bps** (±28.9) | `-44.7 bps` | `-0.087 / -0.095` | `1.19%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 19:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,756.03 | ⚪ **CASH** | **+9.0 bps** (±23.3) | `+43.3 bps` | `-0.064 / -0.203` | `0.85%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.3 bps > 19.5) |
| **ETHUSDT** | $1,817.13 | ⚪ **CASH** | **+12.9 bps** (±35.2) | `+55.2 bps` | `-0.077 / -0.223` | `1.10%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (35.2 bps > 19.5) |
| **SOLUSDT** | $71.21 | ⚪ **CASH** | **-37.3 bps** (±28.9) | `-44.7 bps` | `-0.087 / -0.095` | `1.19%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.9 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 18:45:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,612.25 | ⚪ **CASH** | **+14.7 bps** (±19.1) | `+52.1 bps` | `-0.062 / -0.196` | `0.86%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,813.54 | ⚪ **CASH** | **+12.2 bps** (±28.7) | `+50.1 bps` | `-0.074 / -0.188` | `1.11%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.7 bps > 19.5) |
| **SOLUSDT** | $70.98 | ⚪ **CASH** | **-30.7 bps** (±34.8) | `-31.6 bps` | `-0.086 / -0.097` | `1.21%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (34.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 18:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,570.94 | ⚪ **CASH** | **+14.7 bps** (±19.1) | `+52.1 bps` | `-0.062 / -0.196` | `0.86%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,812.93 | ⚪ **CASH** | **+12.2 bps** (±28.7) | `+50.1 bps` | `-0.074 / -0.188` | `1.11%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.7 bps > 19.5) |
| **SOLUSDT** | $70.84 | ⚪ **CASH** | **-30.7 bps** (±34.8) | `-31.6 bps` | `-0.086 / -0.097` | `1.21%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (34.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 18:15:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,573.99 | ⚪ **CASH** | **+14.7 bps** (±19.1) | `+52.1 bps` | `-0.062 / -0.196` | `0.86%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,814.44 | ⚪ **CASH** | **+12.2 bps** (±28.7) | `+50.1 bps` | `-0.074 / -0.188` | `1.11%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.7 bps > 19.5) |
| **SOLUSDT** | $71.28 | ⚪ **CASH** | **-30.7 bps** (±34.8) | `-31.6 bps` | `-0.086 / -0.097` | `1.21%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (34.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 18:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,497.59 | ⚪ **CASH** | **+14.7 bps** (±19.1) | `+52.1 bps` | `-0.062 / -0.196` | `0.86%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,811.94 | ⚪ **CASH** | **+12.2 bps** (±28.7) | `+50.1 bps` | `-0.074 / -0.188` | `1.11%/h` | `vol_compressed` `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.7 bps > 19.5) |
| **SOLUSDT** | $71.36 | ⚪ **CASH** | **-30.7 bps** (±34.8) | `-31.6 bps` | `-0.086 / -0.097` | `1.21%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (34.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 17:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,596.35 | ⚪ **CASH** | **+17.1 bps** (±23.4) | `+47.9 bps` | `-0.046 / -0.087` | `0.87%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (23.4 bps > 19.5) |
| **ETHUSDT** | $1,808.79 | ⚪ **CASH** | **+55.7 bps** (±9.7) | `+118.9 bps` | `-0.057 / -0.121` | `1.13%/h` | `vol_compressed` `weak_order_flow` | Filtro: compressão de volatilidade (< 0.75) |
| **SOLUSDT** | $71.31 | ⚪ **CASH** | **-18.4 bps** (±31.5) | `-12.4 bps` | `-0.083 / -0.073` | `1.22%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (31.5 bps > 19.5) |

---

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
