# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-15 02:00:55 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-15 02:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,819.18 | ⚪ **CASH** | **-2.5 bps** (±40.2) | `+18.3 bps` | `-0.080 / -0.057` | `0.66%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (40.2 bps > 19.5) |
| **ETHUSDT** | $1,734.40 | ⚪ **CASH** | **+11.1 bps** (±35.5) | `+50.4 bps` | `-0.114 / -0.134` | `0.90%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (35.5 bps > 19.5) |
| **SOLUSDT** | $68.08 | ⚪ **CASH** | **+1.1 bps** (±46.4) | `+25.9 bps` | `-0.066 / -0.078` | `0.97%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 01:45:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,098.35 | ⚪ **CASH** | **+6.4 bps** (±22.5) | `+26.7 bps` | `-0.070 / -0.012` | `0.64%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.5 bps > 19.5) |
| **ETHUSDT** | $1,714.87 | ⚪ **CASH** | **+8.8 bps** (±36.6) | `+45.9 bps` | `-0.113 / -0.134` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |
| **SOLUSDT** | $67.53 | ⚪ **CASH** | **-21.5 bps** (±48.4) | `-15.5 bps` | `-0.064 / -0.079` | `0.92%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (48.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 01:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,536.43 | ⚪ **CASH** | **+6.4 bps** (±22.5) | `+26.7 bps` | `-0.070 / -0.012` | `0.64%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.5 bps > 19.5) |
| **ETHUSDT** | $1,724.35 | ⚪ **CASH** | **+8.8 bps** (±36.6) | `+45.9 bps` | `-0.113 / -0.134` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |
| **SOLUSDT** | $68.44 | ⚪ **CASH** | **-21.5 bps** (±48.4) | `-15.5 bps` | `-0.064 / -0.079` | `0.92%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (48.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 01:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $62,781.00 | ⚪ **CASH** | **+6.4 bps** (±22.5) | `+26.7 bps` | `-0.070 / -0.012` | `0.64%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.5 bps > 19.5) |
| **ETHUSDT** | $1,729.44 | ⚪ **CASH** | **+8.8 bps** (±36.6) | `+45.9 bps` | `-0.113 / -0.134` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |
| **SOLUSDT** | $69.03 | ⚪ **CASH** | **-21.5 bps** (±48.4) | `-15.5 bps` | `-0.064 / -0.079` | `0.92%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (48.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 01:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,420.97 | ⚪ **CASH** | **+6.4 bps** (±22.5) | `+26.7 bps` | `-0.070 / -0.012` | `0.64%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.5 bps > 19.5) |
| **ETHUSDT** | $1,740.37 | ⚪ **CASH** | **+8.8 bps** (±36.6) | `+45.9 bps` | `-0.113 / -0.134` | `0.91%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |
| **SOLUSDT** | $69.38 | ⚪ **CASH** | **-21.5 bps** (±48.4) | `-15.5 bps` | `-0.064 / -0.079` | `0.92%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (48.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 00:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,899.82 | ⚪ **CASH** | **-8.4 bps** (±15.8) | `-0.8 bps` | `-0.072 / -0.014` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,758.86 | ⚪ **CASH** | **+26.9 bps** (±40.4) | `+76.7 bps` | `-0.102 / -0.107` | `0.89%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (40.4 bps > 19.5) |
| **SOLUSDT** | $70.11 | ⚪ **CASH** | **-16.3 bps** (±43.2) | `-9.2 bps` | `-0.055 / -0.057` | `0.92%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (43.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 00:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,747.57 | ⚪ **CASH** | **-8.4 bps** (±15.8) | `-0.8 bps` | `-0.072 / -0.014` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,752.75 | ⚪ **CASH** | **+26.9 bps** (±40.4) | `+76.7 bps` | `-0.102 / -0.107` | `0.89%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (40.4 bps > 19.5) |
| **SOLUSDT** | $69.77 | ⚪ **CASH** | **-16.3 bps** (±43.2) | `-9.2 bps` | `-0.055 / -0.057` | `0.92%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (43.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 00:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,323.07 | ⚪ **CASH** | **-8.4 bps** (±15.8) | `-0.8 bps` | `-0.072 / -0.014` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,769.38 | ⚪ **CASH** | **+26.9 bps** (±40.4) | `+76.7 bps` | `-0.102 / -0.107` | `0.89%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (40.4 bps > 19.5) |
| **SOLUSDT** | $70.37 | ⚪ **CASH** | **-16.3 bps** (±43.2) | `-9.2 bps` | `-0.055 / -0.057` | `0.92%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (43.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-15 00:00:58 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,120.01 | ⚪ **CASH** | **-8.4 bps** (±15.8) | `-0.8 bps` | `-0.072 / -0.014` | `0.63%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,767.44 | ⚪ **CASH** | **+26.9 bps** (±40.4) | `+76.7 bps` | `-0.102 / -0.107` | `0.89%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (40.4 bps > 19.5) |
| **SOLUSDT** | $70.23 | ⚪ **CASH** | **-16.3 bps** (±43.2) | `-9.2 bps` | `-0.055 / -0.057` | `0.92%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (43.2 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 23:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,897.90 | ⚪ **CASH** | **+5.7 bps** (±22.1) | `+33.2 bps` | `-0.093 / -0.078` | `0.60%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,759.75 | ⚪ **CASH** | **+54.3 bps** (±24.4) | `+124.8 bps` | `-0.106 / -0.103` | `0.85%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.4 bps > 19.5) |
| **SOLUSDT** | $69.91 | ⚪ **CASH** | **-4.0 bps** (±46.4) | `+15.6 bps` | `-0.053 / -0.071` | `0.86%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 23:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,656.14 | ⚪ **CASH** | **+5.7 bps** (±22.1) | `+33.2 bps` | `-0.093 / -0.078` | `0.60%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,745.12 | ⚪ **CASH** | **+54.3 bps** (±24.4) | `+124.8 bps` | `-0.106 / -0.103` | `0.85%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.4 bps > 19.5) |
| **SOLUSDT** | $69.21 | ⚪ **CASH** | **-4.0 bps** (±46.4) | `+15.6 bps` | `-0.053 / -0.071` | `0.86%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 23:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,725.13 | ⚪ **CASH** | **+5.7 bps** (±22.1) | `+33.2 bps` | `-0.093 / -0.078` | `0.60%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,746.27 | ⚪ **CASH** | **+54.3 bps** (±24.4) | `+124.8 bps` | `-0.106 / -0.103` | `0.85%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.4 bps > 19.5) |
| **SOLUSDT** | $69.41 | ⚪ **CASH** | **-4.0 bps** (±46.4) | `+15.6 bps` | `-0.053 / -0.071` | `0.86%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 23:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,703.69 | ⚪ **CASH** | **+5.7 bps** (±22.1) | `+33.2 bps` | `-0.093 / -0.078` | `0.60%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |
| **ETHUSDT** | $1,751.09 | ⚪ **CASH** | **+54.3 bps** (±24.4) | `+124.8 bps` | `-0.106 / -0.103` | `0.85%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (24.4 bps > 19.5) |
| **SOLUSDT** | $69.43 | ⚪ **CASH** | **-4.0 bps** (±46.4) | `+15.6 bps` | `-0.053 / -0.071` | `0.86%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.4 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 22:45:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,884.29 | ⚪ **CASH** | **-25.3 bps** (±33.5) | `-17.4 bps` | `-0.105 / -0.108` | `0.57%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.5 bps > 19.5) |
| **ETHUSDT** | $1,760.83 | ⚪ **CASH** | **+48.2 bps** (±21.5) | `+112.5 bps` | `-0.105 / -0.083` | `0.83%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.5 bps > 19.5) |
| **SOLUSDT** | $69.59 | ⚪ **CASH** | **+10.6 bps** (±46.1) | `+42.7 bps` | `-0.055 / -0.070` | `0.86%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 22:30:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,036.02 | ⚪ **CASH** | **-25.3 bps** (±33.5) | `-17.4 bps` | `-0.105 / -0.108` | `0.57%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.5 bps > 19.5) |
| **ETHUSDT** | $1,762.97 | ⚪ **CASH** | **+48.2 bps** (±21.5) | `+112.5 bps` | `-0.105 / -0.083` | `0.83%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.5 bps > 19.5) |
| **SOLUSDT** | $69.53 | ⚪ **CASH** | **+10.6 bps** (±46.1) | `+42.7 bps` | `-0.055 / -0.070` | `0.86%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 22:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $63,727.56 | ⚪ **CASH** | **-25.3 bps** (±33.5) | `-17.4 bps` | `-0.105 / -0.108` | `0.57%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.5 bps > 19.5) |
| **ETHUSDT** | $1,751.95 | ⚪ **CASH** | **+48.2 bps** (±21.5) | `+112.5 bps` | `-0.105 / -0.083` | `0.83%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.5 bps > 19.5) |
| **SOLUSDT** | $69.27 | ⚪ **CASH** | **+10.6 bps** (±46.1) | `+42.7 bps` | `-0.055 / -0.070` | `0.86%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 22:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,421.03 | ⚪ **CASH** | **-25.3 bps** (±33.5) | `-17.4 bps` | `-0.105 / -0.108` | `0.57%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (33.5 bps > 19.5) |
| **ETHUSDT** | $1,771.51 | ⚪ **CASH** | **+48.2 bps** (±21.5) | `+112.5 bps` | `-0.105 / -0.083` | `0.83%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.5 bps > 19.5) |
| **SOLUSDT** | $69.82 | ⚪ **CASH** | **+10.6 bps** (±46.1) | `+42.7 bps` | `-0.055 / -0.070` | `0.86%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 21:45:35 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,777.11 | ⚪ **CASH** | **-38.3 bps** (±32.5) | `-41.4 bps` | `-0.105 / -0.104` | `0.58%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (32.5 bps > 19.5) |
| **ETHUSDT** | $1,785.14 | ⚪ **CASH** | **+56.9 bps** (±26.8) | `+130.2 bps` | `-0.109 / -0.091` | `0.84%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.8 bps > 19.5) |
| **SOLUSDT** | $70.45 | ⚪ **CASH** | **-21.0 bps** (±50.7) | `-15.9 bps` | `-0.057 / -0.036` | `0.87%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (50.7 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 21:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,519.82 | ⚪ **CASH** | **-38.3 bps** (±32.5) | `-41.4 bps` | `-0.105 / -0.104` | `0.58%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (32.5 bps > 19.5) |
| **ETHUSDT** | $1,779.66 | ⚪ **CASH** | **+56.9 bps** (±26.8) | `+130.2 bps` | `-0.109 / -0.091` | `0.84%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.8 bps > 19.5) |
| **SOLUSDT** | $70.03 | ⚪ **CASH** | **-21.0 bps** (±50.7) | `-15.9 bps` | `-0.057 / -0.036` | `0.87%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (50.7 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 21:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,308.98 | ⚪ **CASH** | **-38.3 bps** (±32.5) | `-41.4 bps` | `-0.105 / -0.104` | `0.58%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (32.5 bps > 19.5) |
| **ETHUSDT** | $1,765.66 | ⚪ **CASH** | **+56.9 bps** (±26.8) | `+130.2 bps` | `-0.109 / -0.091` | `0.84%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.8 bps > 19.5) |
| **SOLUSDT** | $69.65 | ⚪ **CASH** | **-21.0 bps** (±50.7) | `-15.9 bps` | `-0.057 / -0.036` | `0.87%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (50.7 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 21:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $64,876.01 | ⚪ **CASH** | **-38.3 bps** (±32.5) | `-41.4 bps` | `-0.105 / -0.104` | `0.58%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (32.5 bps > 19.5) |
| **ETHUSDT** | $1,789.14 | ⚪ **CASH** | **+56.9 bps** (±26.8) | `+130.2 bps` | `-0.109 / -0.091` | `0.84%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.8 bps > 19.5) |
| **SOLUSDT** | $70.81 | ⚪ **CASH** | **-21.0 bps** (±50.7) | `-15.9 bps` | `-0.057 / -0.036` | `0.87%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (50.7 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 20:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,482.49 | ⚪ **CASH** | **-68.2 bps** (±46.1) | `-95.8 bps` | `-0.095 / -0.091` | `0.54%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.1 bps > 19.5) |
| **ETHUSDT** | $1,823.11 | ⚪ **CASH** | **+7.1 bps** (±25.5) | `+35.4 bps` | `-0.092 / -0.063` | `0.71%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.5 bps > 19.5) |
| **SOLUSDT** | $71.67 | ⚪ **CASH** | **-46.9 bps** (±26.0) | `-66.1 bps` | `-0.050 / -0.075` | `0.80%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.0 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 20:30:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,534.46 | ⚪ **CASH** | **-68.2 bps** (±46.1) | `-95.8 bps` | `-0.095 / -0.091` | `0.54%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.1 bps > 19.5) |
| **ETHUSDT** | $1,826.79 | ⚪ **CASH** | **+7.1 bps** (±25.5) | `+35.4 bps` | `-0.092 / -0.063` | `0.71%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.5 bps > 19.5) |
| **SOLUSDT** | $71.94 | ⚪ **CASH** | **-46.9 bps** (±26.0) | `-66.1 bps` | `-0.050 / -0.075` | `0.80%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.0 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 20:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,500.00 | ⚪ **CASH** | **-68.2 bps** (±46.1) | `-95.8 bps` | `-0.095 / -0.091` | `0.54%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.1 bps > 19.5) |
| **ETHUSDT** | $1,825.60 | ⚪ **CASH** | **+7.1 bps** (±25.5) | `+35.4 bps` | `-0.092 / -0.063` | `0.71%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.5 bps > 19.5) |
| **SOLUSDT** | $71.74 | ⚪ **CASH** | **-46.9 bps** (±26.0) | `-66.1 bps` | `-0.050 / -0.075` | `0.80%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.0 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 20:00:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,844.01 | ⚪ **CASH** | **-68.2 bps** (±46.1) | `-95.8 bps` | `-0.095 / -0.091` | `0.54%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (46.1 bps > 19.5) |
| **ETHUSDT** | $1,838.70 | ⚪ **CASH** | **+7.1 bps** (±25.5) | `+35.4 bps` | `-0.092 / -0.063` | `0.71%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.5 bps > 19.5) |
| **SOLUSDT** | $72.49 | ⚪ **CASH** | **-46.9 bps** (±26.0) | `-66.1 bps` | `-0.050 / -0.075` | `0.80%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.0 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 19:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,789.56 | ⚪ **CASH** | **-39.0 bps** (±38.8) | `-43.5 bps` | `-0.095 / -0.098` | `0.54%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (38.8 bps > 19.5) |
| **ETHUSDT** | $1,838.03 | ⚪ **CASH** | **+18.9 bps** (±29.8) | `+58.2 bps` | `-0.092 / -0.072` | `0.71%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (29.8 bps > 19.5) |
| **SOLUSDT** | $72.48 | ⚪ **CASH** | **-26.1 bps** (±34.8) | `-26.7 bps` | `-0.048 / -0.078` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (34.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 19:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,557.23 | ⚪ **CASH** | **-39.0 bps** (±38.8) | `-43.5 bps` | `-0.095 / -0.098` | `0.54%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (38.8 bps > 19.5) |
| **ETHUSDT** | $1,829.63 | ⚪ **CASH** | **+18.9 bps** (±29.8) | `+58.2 bps` | `-0.092 / -0.072` | `0.71%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (29.8 bps > 19.5) |
| **SOLUSDT** | $72.07 | ⚪ **CASH** | **-26.1 bps** (±34.8) | `-26.7 bps` | `-0.048 / -0.078` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (34.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 19:15:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,562.13 | ⚪ **CASH** | **-39.0 bps** (±38.8) | `-43.5 bps` | `-0.095 / -0.098` | `0.54%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (38.8 bps > 19.5) |
| **ETHUSDT** | $1,831.11 | ⚪ **CASH** | **+18.9 bps** (±29.8) | `+58.2 bps` | `-0.092 / -0.072` | `0.71%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (29.8 bps > 19.5) |
| **SOLUSDT** | $72.20 | ⚪ **CASH** | **-26.1 bps** (±34.8) | `-26.7 bps` | `-0.048 / -0.078` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (34.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 19:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,650.01 | ⚪ **CASH** | **-39.0 bps** (±38.8) | `-43.5 bps` | `-0.095 / -0.098` | `0.54%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (38.8 bps > 19.5) |
| **ETHUSDT** | $1,834.24 | ⚪ **CASH** | **+18.9 bps** (±29.8) | `+58.2 bps` | `-0.092 / -0.072` | `0.71%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (29.8 bps > 19.5) |
| **SOLUSDT** | $72.43 | ⚪ **CASH** | **-26.1 bps** (±34.8) | `-26.7 bps` | `-0.048 / -0.078` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (34.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 18:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,800.02 | ⚪ **CASH** | **-65.8 bps** (±42.1) | `-91.1 bps` | `-0.095 / -0.105` | `0.55%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (42.1 bps > 19.5) |
| **ETHUSDT** | $1,837.83 | ⚪ **CASH** | **+11.9 bps** (±26.8) | `+45.5 bps` | `-0.093 / -0.077` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.8 bps > 19.5) |
| **SOLUSDT** | $72.49 | ⚪ **CASH** | **-28.1 bps** (±37.5) | `-29.7 bps` | `-0.047 / -0.081` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (37.5 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 18:30:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,932.01 | ⚪ **CASH** | **-65.8 bps** (±42.1) | `-91.1 bps` | `-0.095 / -0.105` | `0.55%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (42.1 bps > 19.5) |
| **ETHUSDT** | $1,843.68 | ⚪ **CASH** | **+11.9 bps** (±26.8) | `+45.5 bps` | `-0.093 / -0.077` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.8 bps > 19.5) |
| **SOLUSDT** | $72.77 | ⚪ **CASH** | **-28.1 bps** (±37.5) | `-29.7 bps` | `-0.047 / -0.081` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (37.5 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 18:15:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,913.10 | ⚪ **CASH** | **-65.8 bps** (±42.1) | `-91.1 bps` | `-0.095 / -0.105` | `0.55%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (42.1 bps > 19.5) |
| **ETHUSDT** | $1,837.65 | ⚪ **CASH** | **+11.9 bps** (±26.8) | `+45.5 bps` | `-0.093 / -0.077` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.8 bps > 19.5) |
| **SOLUSDT** | $72.67 | ⚪ **CASH** | **-28.1 bps** (±37.5) | `-29.7 bps` | `-0.047 / -0.081` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (37.5 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 18:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $66,013.57 | ⚪ **CASH** | **-65.8 bps** (±42.1) | `-91.1 bps` | `-0.095 / -0.105` | `0.55%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (42.1 bps > 19.5) |
| **ETHUSDT** | $1,846.83 | ⚪ **CASH** | **+11.9 bps** (±26.8) | `+45.5 bps` | `-0.093 / -0.077` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.8 bps > 19.5) |
| **SOLUSDT** | $73.04 | ⚪ **CASH** | **-28.1 bps** (±37.5) | `-29.7 bps` | `-0.047 / -0.081` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (37.5 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 17:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,918.05 | ⚪ **CASH** | **-29.9 bps** (±31.8) | `-27.5 bps` | `-0.096 / -0.106` | `0.52%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (31.8 bps > 19.5) |
| **ETHUSDT** | $1,849.28 | ⚪ **CASH** | **+5.6 bps** (±25.3) | `+35.5 bps` | `-0.099 / -0.096` | `0.70%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.3 bps > 19.5) |
| **SOLUSDT** | $73.09 | ⚪ **CASH** | **-37.1 bps** (±21.8) | `-49.5 bps` | `-0.045 / -0.073` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 17:30:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,637.26 | ⚪ **CASH** | **-29.9 bps** (±31.8) | `-27.5 bps` | `-0.096 / -0.106` | `0.52%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (31.8 bps > 19.5) |
| **ETHUSDT** | $1,845.04 | ⚪ **CASH** | **+5.6 bps** (±25.3) | `+35.5 bps` | `-0.099 / -0.096` | `0.70%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.3 bps > 19.5) |
| **SOLUSDT** | $73.06 | ⚪ **CASH** | **-37.1 bps** (±21.8) | `-49.5 bps` | `-0.045 / -0.073` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.8 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-14 17:15:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $65,250.01 | ⚪ **CASH** | **-29.9 bps** (±31.8) | `-27.5 bps` | `-0.096 / -0.106` | `0.52%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (31.8 bps > 19.5) |
| **ETHUSDT** | $1,820.17 | ⚪ **CASH** | **+5.6 bps** (±25.3) | `+35.5 bps` | `-0.099 / -0.096` | `0.70%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.3 bps > 19.5) |
| **SOLUSDT** | $72.42 | ⚪ **CASH** | **-37.1 bps** (±21.8) | `-49.5 bps` | `-0.045 / -0.073` | `0.81%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (21.8 bps > 19.5) |
