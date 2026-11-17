# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-17 00:00:52 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-17 00:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,922.97 | ⚪ **CASH** | **+25.9 bps** (±13.7) | `+41.2 bps` | `+0.027 / +0.065` | `0.70%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,821.99 | ⚪ **CASH** | **+30.2 bps** (±7.0) | `+59.4 bps` | `-0.020 / -0.039` | `0.90%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.61 | ⚪ **CASH** | **+4.1 bps** (±6.8) | `+29.9 bps` | `-0.151 / -0.120` | `0.94%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 23:45:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,854.48 | ⚪ **CASH** | **+22.4 bps** (±26.1) | `+34.0 bps` | `+0.027 / +0.114` | `0.70%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |
| **ETHUSDT** | $1,818.67 | ⚪ **CASH** | **+33.5 bps** (±10.4) | `+66.4 bps` | `-0.021 / -0.045` | `0.91%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.21 | ⚪ **CASH** | **-3.7 bps** (±12.5) | `+15.2 bps` | `-0.139 / -0.112` | `0.96%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 23:30:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,227.38 | ⚪ **CASH** | **+22.4 bps** (±26.1) | `+34.0 bps` | `+0.027 / +0.114` | `0.70%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |
| **ETHUSDT** | $1,822.80 | ⚪ **CASH** | **+33.5 bps** (±10.4) | `+66.4 bps` | `-0.021 / -0.045` | `0.91%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.55 | ⚪ **CASH** | **-3.7 bps** (±12.5) | `+15.2 bps` | `-0.139 / -0.112` | `0.96%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 23:15:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,315.57 | ⚪ **CASH** | **+22.4 bps** (±26.1) | `+34.0 bps` | `+0.027 / +0.114` | `0.70%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |
| **ETHUSDT** | $1,830.12 | ⚪ **CASH** | **+33.5 bps** (±10.4) | `+66.4 bps` | `-0.021 / -0.045` | `0.91%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.83 | ⚪ **CASH** | **-3.7 bps** (±12.5) | `+15.2 bps` | `-0.139 / -0.112` | `0.96%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 23:00:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,262.69 | ⚪ **CASH** | **+22.4 bps** (±26.1) | `+34.0 bps` | `+0.027 / +0.114` | `0.70%/h` | `vol_compressed` `high_uncertainty` `weak_order_flow` `stretched_top` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |
| **ETHUSDT** | $1,825.72 | ⚪ **CASH** | **+33.5 bps** (±10.4) | `+66.4 bps` | `-0.021 / -0.045` | `0.91%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.59 | ⚪ **CASH** | **-3.7 bps** (±12.5) | `+15.2 bps` | `-0.139 / -0.112` | `0.96%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 22:45:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,489.23 | ⚪ **CASH** | **+33.8 bps** (±19.4) | `+50.6 bps` | `+0.029 / +0.155` | `0.71%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,833.10 | ⚪ **CASH** | **+35.9 bps** (±14.8) | `+70.7 bps` | `-0.017 / -0.037` | `0.92%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.02 | ⚪ **CASH** | **-0.7 bps** (±15.5) | `+20.4 bps` | `-0.134 / -0.109` | `0.97%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 22:31:04 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,358.82 | ⚪ **CASH** | **+33.8 bps** (±19.4) | `+50.6 bps` | `+0.029 / +0.155` | `0.71%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,833.81 | ⚪ **CASH** | **+35.9 bps** (±14.8) | `+70.7 bps` | `-0.017 / -0.037` | `0.92%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.94 | ⚪ **CASH** | **-0.7 bps** (±15.5) | `+20.4 bps` | `-0.134 / -0.109` | `0.97%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 22:15:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,471.48 | ⚪ **CASH** | **+33.8 bps** (±19.4) | `+50.6 bps` | `+0.029 / +0.155` | `0.71%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,836.72 | ⚪ **CASH** | **+35.9 bps** (±14.8) | `+70.7 bps` | `-0.017 / -0.037` | `0.92%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.12 | ⚪ **CASH** | **-0.7 bps** (±15.5) | `+20.4 bps` | `-0.134 / -0.109` | `0.97%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 22:01:05 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,351.52 | ⚪ **CASH** | **+33.8 bps** (±19.4) | `+50.6 bps` | `+0.029 / +0.155` | `0.71%/h` | `vol_compressed` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,831.50 | ⚪ **CASH** | **+35.9 bps** (±14.8) | `+70.7 bps` | `-0.017 / -0.037` | `0.92%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.98 | ⚪ **CASH** | **-0.7 bps** (±15.5) | `+20.4 bps` | `-0.134 / -0.109` | `0.97%/h` | `vol_compressed` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-16 21:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,310.41 | ⚪ **CASH** | **+12.3 bps** (±22.8) | `+16.1 bps` | `+0.008 / +0.141` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.8 bps > 19.5) |
| **ETHUSDT** | $1,827.65 | ⚪ **CASH** | **+40.4 bps** (±12.7) | `+78.5 bps` | `-0.017 / -0.021` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $71.93 | ⚪ **CASH** | **-5.2 bps** (±16.2) | `+14.7 bps` | `-0.133 / -0.130` | `0.98%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-16 21:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,256.34 | ⚪ **CASH** | **+12.3 bps** (±22.8) | `+16.1 bps` | `+0.008 / +0.141` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.8 bps > 19.5) |
| **ETHUSDT** | $1,825.83 | ⚪ **CASH** | **+40.4 bps** (±12.7) | `+78.5 bps` | `-0.017 / -0.021` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $71.82 | ⚪ **CASH** | **-5.2 bps** (±16.2) | `+14.7 bps` | `-0.133 / -0.130` | `0.98%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-16 21:16:23 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,010.01 | ⚪ **CASH** | **+12.3 bps** (±22.8) | `+16.1 bps` | `+0.008 / +0.141` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.8 bps > 19.5) |
| **ETHUSDT** | $1,819.68 | ⚪ **CASH** | **+40.4 bps** (±12.7) | `+78.5 bps` | `-0.017 / -0.021` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $71.46 | ⚪ **CASH** | **-5.2 bps** (±16.2) | `+14.7 bps` | `-0.133 / -0.130` | `0.98%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-16 21:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,042.00 | ⚪ **CASH** | **+12.3 bps** (±22.8) | `+16.1 bps` | `+0.008 / +0.141` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.8 bps > 19.5) |
| **ETHUSDT** | $1,819.74 | ⚪ **CASH** | **+40.4 bps** (±12.7) | `+78.5 bps` | `-0.017 / -0.021` | `0.93%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $71.34 | ⚪ **CASH** | **-5.2 bps** (±16.2) | `+14.7 bps` | `-0.133 / -0.130` | `0.98%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 35.7 bps) |

---

### 🕒 Ciclo `2026-11-16 20:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,996.01 | ⚪ **CASH** | **+6.3 bps** (±22.5) | `+7.9 bps` | `-0.009 / +0.137` | `0.73%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.5 bps > 19.5) |
| **ETHUSDT** | $1,819.62 | ⚪ **CASH** | **+44.3 bps** (±19.8) | `+85.4 bps` | `-0.020 / +0.017` | `0.95%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (19.8 bps > 19.5) |
| **SOLUSDT** | $71.43 | ⚪ **CASH** | **-11.1 bps** (±14.1) | `+3.5 bps` | `-0.130 / -0.122` | `1.00%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.2 bps) |

---

### 🕒 Ciclo `2026-11-16 20:31:00 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,175.72 | ⚪ **CASH** | **+6.3 bps** (±22.5) | `+7.9 bps` | `-0.009 / +0.137` | `0.73%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.5 bps > 19.5) |
| **ETHUSDT** | $1,821.96 | ⚪ **CASH** | **+44.3 bps** (±19.8) | `+85.4 bps` | `-0.020 / +0.017` | `0.95%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (19.8 bps > 19.5) |
| **SOLUSDT** | $71.50 | ⚪ **CASH** | **-11.1 bps** (±14.1) | `+3.5 bps` | `-0.130 / -0.122` | `1.00%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.2 bps) |

---

### 🕒 Ciclo `2026-11-16 20:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,009.65 | ⚪ **CASH** | **+6.3 bps** (±22.5) | `+7.9 bps` | `-0.009 / +0.137` | `0.73%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.5 bps > 19.5) |
| **ETHUSDT** | $1,819.84 | ⚪ **CASH** | **+44.3 bps** (±19.8) | `+85.4 bps` | `-0.020 / +0.017` | `0.95%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (19.8 bps > 19.5) |
| **SOLUSDT** | $71.41 | ⚪ **CASH** | **-11.1 bps** (±14.1) | `+3.5 bps` | `-0.130 / -0.122` | `1.00%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.2 bps) |

---

### 🕒 Ciclo `2026-11-16 20:01:02 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,058.01 | ⚪ **CASH** | **+6.3 bps** (±22.5) | `+7.9 bps` | `-0.009 / +0.137` | `0.73%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.5 bps > 19.5) |
| **ETHUSDT** | $1,822.97 | ⚪ **CASH** | **+44.3 bps** (±19.8) | `+85.4 bps` | `-0.020 / +0.017` | `0.95%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (19.8 bps > 19.5) |
| **SOLUSDT** | $71.56 | ⚪ **CASH** | **-11.1 bps** (±14.1) | `+3.5 bps` | `-0.130 / -0.122` | `1.00%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.2 bps) |

---

### 🕒 Ciclo `2026-11-16 19:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,772.01 | ⚪ **CASH** | **+11.2 bps** (±18.6) | `+15.1 bps` | `-0.013 / +0.161` | `0.74%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 30.2 bps) |
| **ETHUSDT** | $1,813.93 | ⚪ **CASH** | **+45.6 bps** (±22.2) | `+89.3 bps` | `-0.022 / +0.007` | `0.96%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.2 bps > 19.5) |
| **SOLUSDT** | $71.02 | ⚪ **CASH** | **-10.0 bps** (±16.6) | `+4.5 bps` | `-0.111 / -0.124` | `1.01%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.2 bps) |

---

### 🕒 Ciclo `2026-11-16 19:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,980.99 | ⚪ **CASH** | **+11.2 bps** (±18.6) | `+15.1 bps` | `-0.013 / +0.161` | `0.74%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 30.2 bps) |
| **ETHUSDT** | $1,819.83 | ⚪ **CASH** | **+45.6 bps** (±22.2) | `+89.3 bps` | `-0.022 / +0.007` | `0.96%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.2 bps > 19.5) |
| **SOLUSDT** | $71.26 | ⚪ **CASH** | **-10.0 bps** (±16.6) | `+4.5 bps` | `-0.111 / -0.124` | `1.01%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.2 bps) |

---

### 🕒 Ciclo `2026-11-16 19:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,842.01 | ⚪ **CASH** | **+11.2 bps** (±18.6) | `+15.1 bps` | `-0.013 / +0.161` | `0.74%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 30.2 bps) |
| **ETHUSDT** | $1,814.46 | ⚪ **CASH** | **+45.6 bps** (±22.2) | `+89.3 bps` | `-0.022 / +0.007` | `0.96%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.2 bps > 19.5) |
| **SOLUSDT** | $71.09 | ⚪ **CASH** | **-10.0 bps** (±16.6) | `+4.5 bps` | `-0.111 / -0.124` | `1.01%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.2 bps) |

---

### 🕒 Ciclo `2026-11-16 19:00:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,998.01 | ⚪ **CASH** | **+11.2 bps** (±18.6) | `+15.1 bps` | `-0.013 / +0.161` | `0.74%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 30.2 bps) |
| **ETHUSDT** | $1,819.58 | ⚪ **CASH** | **+45.6 bps** (±22.2) | `+89.3 bps` | `-0.022 / +0.007` | `0.96%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.2 bps > 19.5) |
| **SOLUSDT** | $71.35 | ⚪ **CASH** | **-10.0 bps** (±16.6) | `+4.5 bps` | `-0.111 / -0.124` | `1.01%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 33.2 bps) |

---

### 🕒 Ciclo `2026-11-16 18:45:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,003.52 | ⚪ **CASH** | **+7.2 bps** (±26.1) | `+12.3 bps` | `-0.024 / +0.140` | `0.75%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |
| **ETHUSDT** | $1,820.51 | ⚪ **CASH** | **+41.4 bps** (±18.8) | `+81.3 bps` | `-0.026 / +0.017` | `0.98%/h` | `weak_order_flow` | Filtro: confluência Dual-Setup (A/B) e absorção CVD insuficiente |
| **SOLUSDT** | $71.26 | ⚪ **CASH** | **-11.0 bps** (±10.8) | `+1.2 bps` | `-0.107 / -0.116` | `1.02%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.9 bps) |

---

### 🕒 Ciclo `2026-11-16 18:31:06 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,797.48 | ⚪ **CASH** | **+7.2 bps** (±26.1) | `+12.3 bps` | `-0.024 / +0.140` | `0.75%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |
| **ETHUSDT** | $1,814.12 | ⚪ **CASH** | **+41.4 bps** (±18.8) | `+81.3 bps` | `-0.026 / +0.017` | `0.98%/h` | `weak_order_flow` | Filtro: confluência Dual-Setup (A/B) e absorção CVD insuficiente |
| **SOLUSDT** | $71.19 | ⚪ **CASH** | **-11.0 bps** (±10.8) | `+1.2 bps` | `-0.107 / -0.116` | `1.02%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.9 bps) |

---

### 🕒 Ciclo `2026-11-16 18:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,977.00 | ⚪ **CASH** | **+7.2 bps** (±26.1) | `+12.3 bps` | `-0.024 / +0.140` | `0.75%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |
| **ETHUSDT** | $1,820.50 | ⚪ **CASH** | **+41.4 bps** (±18.8) | `+81.3 bps` | `-0.026 / +0.017` | `0.98%/h` | `weak_order_flow` | Filtro: confluência Dual-Setup (A/B) e absorção CVD insuficiente |
| **SOLUSDT** | $71.41 | ⚪ **CASH** | **-11.0 bps** (±10.8) | `+1.2 bps` | `-0.107 / -0.116` | `1.02%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.9 bps) |

---

### 🕒 Ciclo `2026-11-16 18:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,825.72 | ⚪ **CASH** | **+7.2 bps** (±26.1) | `+12.3 bps` | `-0.024 / +0.140` | `0.75%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |
| **ETHUSDT** | $1,818.25 | ⚪ **CASH** | **+41.4 bps** (±18.8) | `+81.3 bps` | `-0.026 / +0.017` | `0.98%/h` | `weak_order_flow` | Filtro: confluência Dual-Setup (A/B) e absorção CVD insuficiente |
| **SOLUSDT** | $71.09 | ⚪ **CASH** | **-11.0 bps** (±10.8) | `+1.2 bps` | `-0.107 / -0.116` | `1.02%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.9 bps) |

---

### 🕒 Ciclo `2026-11-16 17:53:18 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,999.99 | ⚪ **CASH** | **+4.0 bps** (±27.8) | `+17.7 bps` | `-0.063 / +0.060` | `0.76%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (27.8 bps > 19.5) |
| **ETHUSDT** | $1,824.59 | ⚪ **CASH** | **+40.0 bps** (±16.1) | `+80.1 bps` | `-0.046 / +0.047` | `0.99%/h` | `weak_order_flow` | Filtro: confluência Dual-Setup (A/B) e absorção CVD insuficiente |
| **SOLUSDT** | $71.43 | ⚪ **CASH** | **-4.4 bps** (±18.5) | `+14.7 bps` | `-0.104 / -0.094` | `1.04%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.8 bps) |

---

### 🕒 Ciclo `2026-11-16 16:31:06 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,708.06 | ⚪ **CASH** | **+2.2 bps** (±28.3) | `+19.4 bps` | `-0.077 / +0.017` | `0.76%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.3 bps > 19.5) |
| **ETHUSDT** | $1,825.34 | ⚪ **CASH** | **+37.0 bps** (±17.0) | `+75.0 bps` | `-0.050 / +0.062` | `1.00%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $71.04 | ⚪ **CASH** | **-14.6 bps** (±6.6) | `-6.2 bps` | `-0.100 / -0.084` | `1.04%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.1 bps) |

---

### 🕒 Ciclo `2026-11-16 16:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,427.18 | ⚪ **CASH** | **+2.2 bps** (±28.3) | `+19.4 bps` | `-0.077 / +0.017` | `0.76%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.3 bps > 19.5) |
| **ETHUSDT** | $1,818.08 | ⚪ **CASH** | **+37.0 bps** (±17.0) | `+75.0 bps` | `-0.050 / +0.062` | `1.00%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $70.53 | ⚪ **CASH** | **-14.6 bps** (±6.6) | `-6.2 bps` | `-0.100 / -0.084` | `1.04%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.1 bps) |

---

### 🕒 Ciclo `2026-11-16 16:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,432.45 | ⚪ **CASH** | **+2.2 bps** (±28.3) | `+19.4 bps` | `-0.077 / +0.017` | `0.76%/h` | `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.3 bps > 19.5) |
| **ETHUSDT** | $1,818.77 | ⚪ **CASH** | **+37.0 bps** (±17.0) | `+75.0 bps` | `-0.050 / +0.062` | `1.00%/h` | `btc_dumping` `weak_order_flow` | Filtro: Bitcoin sem tração para o regime atual |
| **SOLUSDT** | $70.73 | ⚪ **CASH** | **-14.6 bps** (±6.6) | `-6.2 bps` | `-0.100 / -0.084` | `1.04%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 31.1 bps) |

---

### 🕒 Ciclo `2026-11-16 15:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,561.50 | ⚪ **CASH** | **+4.3 bps** (±12.3) | `+23.9 bps` | `-0.090 / -0.008` | `0.75%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 32.8 bps) |
| **ETHUSDT** | $1,819.59 | ⚪ **CASH** | **+11.8 bps** (±15.3) | `+30.2 bps` | `-0.060 / +0.068` | `0.98%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 31.3 bps) |
| **SOLUSDT** | $70.71 | ⚪ **CASH** | **-21.8 bps** (±12.1) | `-19.4 bps` | `-0.099 / -0.060` | `1.03%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.1 bps) |

---

### 🕒 Ciclo `2026-11-16 15:30:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,414.73 | ⚪ **CASH** | **+4.3 bps** (±12.3) | `+23.9 bps` | `-0.090 / -0.008` | `0.75%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 32.8 bps) |
| **ETHUSDT** | $1,813.72 | ⚪ **CASH** | **+11.8 bps** (±15.3) | `+30.2 bps` | `-0.060 / +0.068` | `0.98%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 31.3 bps) |
| **SOLUSDT** | $70.49 | ⚪ **CASH** | **-21.8 bps** (±12.1) | `-19.4 bps` | `-0.099 / -0.060` | `1.03%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.1 bps) |

---

### 🕒 Ciclo `2026-11-16 15:15:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,358.14 | ⚪ **CASH** | **+4.3 bps** (±12.3) | `+23.9 bps` | `-0.090 / -0.008` | `0.75%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 32.8 bps) |
| **ETHUSDT** | $1,813.20 | ⚪ **CASH** | **+11.8 bps** (±15.3) | `+30.2 bps` | `-0.060 / +0.068` | `0.98%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 31.3 bps) |
| **SOLUSDT** | $70.43 | ⚪ **CASH** | **-21.8 bps** (±12.1) | `-19.4 bps` | `-0.099 / -0.060` | `1.03%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.1 bps) |

---

### 🕒 Ciclo `2026-11-16 15:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,000.00 | ⚪ **CASH** | **+4.3 bps** (±12.3) | `+23.9 bps` | `-0.090 / -0.008` | `0.75%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 32.8 bps) |
| **ETHUSDT** | $1,836.67 | ⚪ **CASH** | **+11.8 bps** (±15.3) | `+30.2 bps` | `-0.060 / +0.068` | `0.98%/h` | `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 31.3 bps) |
| **SOLUSDT** | $71.40 | ⚪ **CASH** | **-21.8 bps** (±12.1) | `-19.4 bps` | `-0.099 / -0.060` | `1.03%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 34.1 bps) |

---

### 🕒 Ciclo `2026-11-16 14:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,168.38 | ⚪ **CASH** | **+17.3 bps** (±18.7) | `+57.1 bps` | `-0.117 / -0.078` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,849.59 | ⚪ **CASH** | **-47.6 bps** (±14.6) | `-67.4 bps` | `-0.101 / -0.015` | `0.89%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $72.23 | ⚪ **CASH** | **-18.0 bps** (±24.2) | `-6.8 bps` | `-0.110 / -0.076` | `1.01%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 14:31:04 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,466.27 | ⚪ **CASH** | **+17.3 bps** (±18.7) | `+57.1 bps` | `-0.117 / -0.078` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,822.19 | ⚪ **CASH** | **-47.6 bps** (±14.6) | `-67.4 bps` | `-0.101 / -0.015` | `0.89%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.24 | ⚪ **CASH** | **-18.0 bps** (±24.2) | `-6.8 bps` | `-0.110 / -0.076` | `1.01%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-16 14:15:59 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,578.44 | ⚪ **CASH** | **+17.3 bps** (±18.7) | `+57.1 bps` | `-0.117 / -0.078` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,824.47 | ⚪ **CASH** | **-47.6 bps** (±14.6) | `-67.4 bps` | `-0.101 / -0.015` | `0.89%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $71.40 | ⚪ **CASH** | **-18.0 bps** (±24.2) | `-6.8 bps` | `-0.110 / -0.076` | `1.01%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.2 bps > 19.5) |
