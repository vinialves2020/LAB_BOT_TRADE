# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-12 23:00:57 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-12 23:00:57 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,340.68 | ⚪ **CASH** | **+0.0 bps** (±4.3) | `+6.6 bps` | `-0.019 / -0.046` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,012.48 | ⚪ **CASH** | **+28.3 bps** (±7.9) | `+45.3 bps` | `-0.010 / +0.145` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.39 | ⚪ **CASH** | **-0.1 bps** (±9.1) | `-10.5 bps` | `+0.020 / +0.166` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 22:45:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,423.69 | ⚪ **CASH** | **+2.2 bps** (±7.7) | `+9.7 bps` | `-0.019 / -0.023` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,012.57 | ⚪ **CASH** | **+28.5 bps** (±9.1) | `+48.2 bps` | `-0.013 / +0.114` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.37 | ⚪ **CASH** | **-0.3 bps** (±6.9) | `-10.2 bps` | `+0.011 / +0.165` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 22:30:48 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,503.76 | ⚪ **CASH** | **+2.2 bps** (±7.7) | `+9.7 bps` | `-0.019 / -0.023` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,014.62 | ⚪ **CASH** | **+28.5 bps** (±9.1) | `+48.2 bps` | `-0.013 / +0.114` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.49 | ⚪ **CASH** | **-0.3 bps** (±6.9) | `-10.2 bps` | `+0.011 / +0.165` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 22:15:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,408.00 | ⚪ **CASH** | **+2.2 bps** (±7.7) | `+9.7 bps` | `-0.019 / -0.023` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,012.46 | ⚪ **CASH** | **+28.5 bps** (±9.1) | `+48.2 bps` | `-0.013 / +0.114` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.36 | ⚪ **CASH** | **-0.3 bps** (±6.9) | `-10.2 bps` | `+0.011 / +0.165` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 22:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,504.00 | ⚪ **CASH** | **+2.2 bps** (±7.7) | `+9.7 bps` | `-0.019 / -0.023` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,015.53 | ⚪ **CASH** | **+28.5 bps** (±9.1) | `+48.2 bps` | `-0.013 / +0.114` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.33 | ⚪ **CASH** | **-0.3 bps** (±6.9) | `-10.2 bps` | `+0.011 / +0.165` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 21:45:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,555.76 | ⚪ **CASH** | **+2.7 bps** (±5.5) | `+7.5 bps` | `-0.015 / +0.008` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,019.53 | ⚪ **CASH** | **+33.4 bps** (±8.8) | `+58.3 bps` | `-0.013 / +0.094` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.50 | ⚪ **CASH** | **-1.1 bps** (±9.1) | `-10.3 bps` | `+0.001 / +0.161` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 21:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,610.06 | ⚪ **CASH** | **+2.7 bps** (±5.5) | `+7.5 bps` | `-0.015 / +0.008` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,021.36 | ⚪ **CASH** | **+33.4 bps** (±8.8) | `+58.3 bps` | `-0.013 / +0.094` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.60 | ⚪ **CASH** | **-1.1 bps** (±9.1) | `-10.3 bps` | `+0.001 / +0.161` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 21:15:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,547.60 | ⚪ **CASH** | **+2.7 bps** (±5.5) | `+7.5 bps` | `-0.015 / +0.008` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,018.02 | ⚪ **CASH** | **+33.4 bps** (±8.8) | `+58.3 bps` | `-0.013 / +0.094` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.55 | ⚪ **CASH** | **-1.1 bps** (±9.1) | `-10.3 bps` | `+0.001 / +0.161` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 21:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,499.98 | ⚪ **CASH** | **+2.7 bps** (±5.5) | `+7.5 bps` | `-0.015 / +0.008` | `0.38%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,017.40 | ⚪ **CASH** | **+33.4 bps** (±8.8) | `+58.3 bps` | `-0.013 / +0.094` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.42 | ⚪ **CASH** | **-1.1 bps** (±9.1) | `-10.3 bps` | `+0.001 / +0.161` | `0.51%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 20:45:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,506.61 | ⚪ **CASH** | **-1.2 bps** (±6.7) | `+5.8 bps` | `-0.026 / -0.045` | `0.38%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.5 bps) |
| **ETHUSDT** | $2,019.87 | ⚪ **CASH** | **+23.2 bps** (±6.3) | `+46.2 bps` | `-0.025 / +0.014` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.55 | ⚪ **CASH** | **-7.3 bps** (±6.5) | `-17.3 bps` | `-0.005 / +0.107` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 20:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,486.56 | ⚪ **CASH** | **-1.2 bps** (±6.7) | `+5.8 bps` | `-0.026 / -0.045` | `0.38%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.5 bps) |
| **ETHUSDT** | $2,018.78 | ⚪ **CASH** | **+23.2 bps** (±6.3) | `+46.2 bps` | `-0.025 / +0.014` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.50 | ⚪ **CASH** | **-7.3 bps** (±6.5) | `-17.3 bps` | `-0.005 / +0.107` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 20:15:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,571.74 | ⚪ **CASH** | **-1.2 bps** (±6.7) | `+5.8 bps` | `-0.026 / -0.045` | `0.38%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.5 bps) |
| **ETHUSDT** | $2,018.84 | ⚪ **CASH** | **+23.2 bps** (±6.3) | `+46.2 bps` | `-0.025 / +0.014` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.50 | ⚪ **CASH** | **-7.3 bps** (±6.5) | `-17.3 bps` | `-0.005 / +0.107` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 20:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,675.52 | ⚪ **CASH** | **-1.2 bps** (±6.7) | `+5.8 bps` | `-0.026 / -0.045` | `0.38%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.5 bps) |
| **ETHUSDT** | $2,017.09 | ⚪ **CASH** | **+23.2 bps** (±6.3) | `+46.2 bps` | `-0.025 / +0.014` | `0.47%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.61 | ⚪ **CASH** | **-7.3 bps** (±6.5) | `-17.3 bps` | `-0.005 / +0.107` | `0.52%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 19:45:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,604.01 | ⚪ **CASH** | **+1.6 bps** (±6.6) | `+8.8 bps` | `-0.014 / -0.040` | `0.39%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.0 bps) |
| **ETHUSDT** | $2,012.57 | ⚪ **CASH** | **+25.4 bps** (±4.8) | `+53.8 bps` | `-0.030 / -0.048` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.58 | ⚪ **CASH** | **-14.5 bps** (±5.4) | `-25.6 bps` | `-0.018 / +0.039` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.2 bps) |

---

### 🕒 Ciclo `2026-11-12 19:30:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,552.01 | ⚪ **CASH** | **+1.6 bps** (±6.6) | `+8.8 bps` | `-0.014 / -0.040` | `0.39%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.0 bps) |
| **ETHUSDT** | $2,011.14 | ⚪ **CASH** | **+25.4 bps** (±4.8) | `+53.8 bps` | `-0.030 / -0.048` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.60 | ⚪ **CASH** | **-14.5 bps** (±5.4) | `-25.6 bps` | `-0.018 / +0.039` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.2 bps) |

---

### 🕒 Ciclo `2026-11-12 19:15:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,649.24 | ⚪ **CASH** | **+1.6 bps** (±6.6) | `+8.8 bps` | `-0.014 / -0.040` | `0.39%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.0 bps) |
| **ETHUSDT** | $2,014.11 | ⚪ **CASH** | **+25.4 bps** (±4.8) | `+53.8 bps` | `-0.030 / -0.048` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.55 | ⚪ **CASH** | **-14.5 bps** (±5.4) | `-25.6 bps` | `-0.018 / +0.039` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.2 bps) |

---

### 🕒 Ciclo `2026-11-12 19:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,690.01 | ⚪ **CASH** | **+1.6 bps** (±6.6) | `+8.8 bps` | `-0.014 / -0.040` | `0.39%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.0 bps) |
| **ETHUSDT** | $2,014.89 | ⚪ **CASH** | **+25.4 bps** (±4.8) | `+53.8 bps` | `-0.030 / -0.048` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.53 | ⚪ **CASH** | **-14.5 bps** (±5.4) | `-25.6 bps` | `-0.018 / +0.039` | `0.52%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.2 bps) |

---

### 🕒 Ciclo `2026-11-12 18:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,752.61 | ⚪ **CASH** | **-0.9 bps** (±7.5) | `+3.1 bps` | `-0.007 / -0.035` | `0.39%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.9 bps) |
| **ETHUSDT** | $2,015.41 | ⚪ **CASH** | **+20.5 bps** (±9.9) | `+45.5 bps` | `-0.031 / -0.046` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.60 | ⚪ **CASH** | **-14.2 bps** (±13.5) | `-22.5 bps` | `-0.019 / +0.021` | `0.53%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.1 bps) |

---

### 🕒 Ciclo `2026-11-12 18:30:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $72,000.32 | ⚪ **CASH** | **-0.9 bps** (±7.5) | `+3.1 bps` | `-0.007 / -0.035` | `0.39%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.9 bps) |
| **ETHUSDT** | $2,020.89 | ⚪ **CASH** | **+20.5 bps** (±9.9) | `+45.5 bps` | `-0.031 / -0.046` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.74 | ⚪ **CASH** | **-14.2 bps** (±13.5) | `-22.5 bps` | `-0.019 / +0.021` | `0.53%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.1 bps) |

---

### 🕒 Ciclo `2026-11-12 18:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,935.23 | ⚪ **CASH** | **-0.9 bps** (±7.5) | `+3.1 bps` | `-0.007 / -0.035` | `0.39%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.9 bps) |
| **ETHUSDT** | $2,019.12 | ⚪ **CASH** | **+20.5 bps** (±9.9) | `+45.5 bps` | `-0.031 / -0.046` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.76 | ⚪ **CASH** | **-14.2 bps** (±13.5) | `-22.5 bps` | `-0.019 / +0.021` | `0.53%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.1 bps) |

---

### 🕒 Ciclo `2026-11-12 18:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,940.55 | ⚪ **CASH** | **-0.9 bps** (±7.5) | `+3.1 bps` | `-0.007 / -0.035` | `0.39%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.9 bps) |
| **ETHUSDT** | $2,018.50 | ⚪ **CASH** | **+20.5 bps** (±9.9) | `+45.5 bps` | `-0.031 / -0.046` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.74 | ⚪ **CASH** | **-14.2 bps** (±13.5) | `-22.5 bps` | `-0.019 / +0.021` | `0.53%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.1 bps) |

---

### 🕒 Ciclo `2026-11-12 17:45:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,748.01 | ⚪ **CASH** | **+6.2 bps** (±6.1) | `+16.5 bps` | `-0.004 / -0.054` | `0.39%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.7 bps) |
| **ETHUSDT** | $2,010.47 | ⚪ **CASH** | **-4.0 bps** (±16.1) | `+2.0 bps` | `-0.021 / -0.060` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.35 | ⚪ **CASH** | **-16.1 bps** (±11.2) | `-27.2 bps` | `-0.004 / +0.008` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 17:30:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,995.93 | ⚪ **CASH** | **+6.2 bps** (±6.1) | `+16.5 bps` | `-0.004 / -0.054` | `0.39%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.7 bps) |
| **ETHUSDT** | $2,012.93 | ⚪ **CASH** | **-4.0 bps** (±16.1) | `+2.0 bps` | `-0.021 / -0.060` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.55 | ⚪ **CASH** | **-16.1 bps** (±11.2) | `-27.2 bps` | `-0.004 / +0.008` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 17:15:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,674.01 | ⚪ **CASH** | **+6.2 bps** (±6.1) | `+16.5 bps` | `-0.004 / -0.054` | `0.39%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.7 bps) |
| **ETHUSDT** | $2,005.47 | ⚪ **CASH** | **-4.0 bps** (±16.1) | `+2.0 bps` | `-0.021 / -0.060` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.18 | ⚪ **CASH** | **-16.1 bps** (±11.2) | `-27.2 bps` | `-0.004 / +0.008` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 17:12:20 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,698.02 | ⚪ **CASH** | **+6.2 bps** (±6.1) | `+16.5 bps` | `-0.004 / -0.054` | `0.39%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.7 bps) |
| **ETHUSDT** | $2,005.58 | ⚪ **CASH** | **-4.0 bps** (±16.1) | `+2.0 bps` | `-0.021 / -0.060` | `0.48%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.17 | ⚪ **CASH** | **-16.1 bps** (±11.2) | `-27.2 bps` | `-0.004 / +0.008` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 17:00:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,792.01 | ⚪ **CASH** | **+6.2 bps** (±6.1) | `+16.5 bps` | `-0.004 / -0.054` | `0.39%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,008.70 | ⚪ **CASH** | **-4.0 bps** (±16.1) | `+2.0 bps` | `-0.021 / -0.060` | `0.48%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.49 | ⚪ **CASH** | **-16.1 bps** (±11.2) | `-27.2 bps` | `-0.004 / +0.008` | `0.54%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 16:45:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,550.01 | ⚪ **CASH** | **+6.0 bps** (±6.5) | `+16.1 bps` | `-0.002 / -0.056` | `0.40%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,000.36 | ⚪ **CASH** | **-11.0 bps** (±12.8) | `-11.1 bps` | `-0.019 / -0.070` | `0.49%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.15 | ⚪ **CASH** | **-16.2 bps** (±9.8) | `-26.8 bps` | `-0.008 / -0.000` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 16:30:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,880.79 | ⚪ **CASH** | **+6.0 bps** (±6.5) | `+16.1 bps` | `-0.002 / -0.056` | `0.40%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,014.31 | ⚪ **CASH** | **-11.0 bps** (±12.8) | `-11.1 bps` | `-0.019 / -0.070` | `0.49%/h` | `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.72 | ⚪ **CASH** | **-16.2 bps** (±9.8) | `-26.8 bps` | `-0.008 / -0.000` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

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
