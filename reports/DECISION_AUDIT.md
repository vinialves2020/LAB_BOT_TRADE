# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-13 14:45:39 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-13 14:45:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,083.16 | ⚪ **CASH** | **-12.8 bps** (±7.7) | `-16.2 bps` | `-0.040 / +0.005` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,961.69 | ⚪ **CASH** | **+11.7 bps** (±10.2) | `+24.4 bps` | `-0.033 / +0.062` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.13 | ⚪ **CASH** | **-4.0 bps** (±10.4) | `-1.8 bps` | `+0.010 / -0.040` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 14:30:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,304.01 | ⚪ **CASH** | **-12.8 bps** (±7.7) | `-16.2 bps` | `-0.040 / +0.005` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,966.41 | ⚪ **CASH** | **+11.7 bps** (±10.2) | `+24.4 bps` | `-0.033 / +0.062` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.51 | ⚪ **CASH** | **-4.0 bps** (±10.4) | `-1.8 bps` | `+0.010 / -0.040` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 14:15:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,320.21 | ⚪ **CASH** | **-12.8 bps** (±7.7) | `-16.2 bps` | `-0.040 / +0.005` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,966.63 | ⚪ **CASH** | **+11.7 bps** (±10.2) | `+24.4 bps` | `-0.033 / +0.062` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.31 | ⚪ **CASH** | **-4.0 bps** (±10.4) | `-1.8 bps` | `+0.010 / -0.040` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 14:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,485.18 | ⚪ **CASH** | **-12.8 bps** (±7.7) | `-16.2 bps` | `-0.040 / +0.005` | `0.54%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,966.13 | ⚪ **CASH** | **+11.7 bps** (±10.2) | `+24.4 bps` | `-0.033 / +0.062` | `0.67%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.44 | ⚪ **CASH** | **-4.0 bps** (±10.4) | `-1.8 bps` | `+0.010 / -0.040` | `0.70%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` `stretched_top` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 13:45:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,853.95 | ⚪ **CASH** | **-9.7 bps** (±4.9) | `-9.6 bps` | `-0.048 / -0.000` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.2 bps) |
| **ETHUSDT** | $1,978.69 | ⚪ **CASH** | **-27.9 bps** (±11.2) | `-43.3 bps` | `-0.055 / +0.037` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $82.11 | ⚪ **CASH** | **-13.6 bps** (±8.9) | `-14.0 bps` | `+0.002 / -0.107` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 13:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,458.01 | ⚪ **CASH** | **-9.7 bps** (±4.9) | `-9.6 bps` | `-0.048 / -0.000` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.2 bps) |
| **ETHUSDT** | $1,965.94 | ⚪ **CASH** | **-27.9 bps** (±11.2) | `-43.3 bps` | `-0.055 / +0.037` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.09 | ⚪ **CASH** | **-13.6 bps** (±8.9) | `-14.0 bps` | `+0.002 / -0.107` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 13:15:37 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,206.54 | ⚪ **CASH** | **-9.7 bps** (±4.9) | `-9.6 bps` | `-0.048 / -0.000` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.2 bps) |
| **ETHUSDT** | $1,955.79 | ⚪ **CASH** | **-27.9 bps** (±11.2) | `-43.3 bps` | `-0.055 / +0.037` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $80.72 | ⚪ **CASH** | **-13.6 bps** (±8.9) | `-14.0 bps` | `+0.002 / -0.107` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 13:00:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,140.01 | ⚪ **CASH** | **-9.7 bps** (±4.9) | `-9.6 bps` | `-0.048 / -0.000` | `0.54%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 34.2 bps) |
| **ETHUSDT** | $1,956.91 | ⚪ **CASH** | **-27.9 bps** (±11.2) | `-43.3 bps` | `-0.055 / +0.037` | `0.68%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $80.61 | ⚪ **CASH** | **-13.6 bps** (±8.9) | `-14.0 bps` | `+0.002 / -0.107` | `0.69%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 12:45:45 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,279.67 | ⚪ **CASH** | **-7.7 bps** (±7.1) | `-7.7 bps` | `-0.049 / +0.033` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,961.45 | ⚪ **CASH** | **-19.2 bps** (±16.1) | `-26.9 bps` | `-0.051 / +0.035` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |
| **SOLUSDT** | $80.76 | ⚪ **CASH** | **-16.2 bps** (±13.5) | `-19.5 bps` | `-0.001 / -0.078` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.8 bps) |

---

### 🕒 Ciclo `2026-11-13 12:31:00 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,341.00 | ⚪ **CASH** | **-7.7 bps** (±7.1) | `-7.7 bps` | `-0.049 / +0.033` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,960.96 | ⚪ **CASH** | **-19.2 bps** (±16.1) | `-26.9 bps` | `-0.051 / +0.035` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |
| **SOLUSDT** | $80.77 | ⚪ **CASH** | **-16.2 bps** (±13.5) | `-19.5 bps` | `-0.001 / -0.078` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.8 bps) |

---

### 🕒 Ciclo `2026-11-13 12:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,473.76 | ⚪ **CASH** | **-7.7 bps** (±7.1) | `-7.7 bps` | `-0.049 / +0.033` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,963.14 | ⚪ **CASH** | **-19.2 bps** (±16.1) | `-26.9 bps` | `-0.051 / +0.035` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |
| **SOLUSDT** | $80.82 | ⚪ **CASH** | **-16.2 bps** (±13.5) | `-19.5 bps` | `-0.001 / -0.078` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.8 bps) |

---

### 🕒 Ciclo `2026-11-13 12:00:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,363.83 | ⚪ **CASH** | **-7.7 bps** (±7.1) | `-7.7 bps` | `-0.049 / +0.033` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,960.86 | ⚪ **CASH** | **-19.2 bps** (±16.1) | `-26.9 bps` | `-0.051 / +0.035` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 35.0 bps) |
| **SOLUSDT** | $80.70 | ⚪ **CASH** | **-16.2 bps** (±13.5) | `-19.5 bps` | `-0.001 / -0.078` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 29.8 bps) |

---

### 🕒 Ciclo `2026-11-13 11:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,373.02 | ⚪ **CASH** | **-8.8 bps** (±5.0) | `-9.1 bps` | `-0.052 / +0.025` | `0.56%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,960.34 | ⚪ **CASH** | **-12.7 bps** (±12.1) | `-9.5 bps` | `-0.057 / -0.050` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.2 bps) |
| **SOLUSDT** | $80.73 | ⚪ **CASH** | **-3.0 bps** (±28.6) | `+9.5 bps` | `-0.006 / -0.100` | `0.70%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 11:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,283.21 | ⚪ **CASH** | **-8.8 bps** (±5.0) | `-9.1 bps` | `-0.052 / +0.025` | `0.56%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,956.51 | ⚪ **CASH** | **-12.7 bps** (±12.1) | `-9.5 bps` | `-0.057 / -0.050` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.2 bps) |
| **SOLUSDT** | $80.51 | ⚪ **CASH** | **-3.0 bps** (±28.6) | `+9.5 bps` | `-0.006 / -0.100` | `0.70%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 11:15:47 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,334.13 | ⚪ **CASH** | **-8.8 bps** (±5.0) | `-9.1 bps` | `-0.052 / +0.025` | `0.56%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,953.30 | ⚪ **CASH** | **-12.7 bps** (±12.1) | `-9.5 bps` | `-0.057 / -0.050` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.2 bps) |
| **SOLUSDT** | $80.53 | ⚪ **CASH** | **-3.0 bps** (±28.6) | `+9.5 bps` | `-0.006 / -0.100` | `0.70%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 11:00:56 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,302.36 | ⚪ **CASH** | **-8.8 bps** (±5.0) | `-9.1 bps` | `-0.052 / +0.025` | `0.56%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,950.75 | ⚪ **CASH** | **-12.7 bps** (±12.1) | `-9.5 bps` | `-0.057 / -0.050` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 32.2 bps) |
| **SOLUSDT** | $80.46 | ⚪ **CASH** | **-3.0 bps** (±28.6) | `+9.5 bps` | `-0.006 / -0.100` | `0.70%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (28.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 10:45:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,322.01 | ⚪ **CASH** | **-16.8 bps** (±6.6) | `-22.6 bps` | `-0.049 / +0.006` | `0.56%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,951.53 | ⚪ **CASH** | **-19.5 bps** (±13.6) | `-20.1 bps` | `-0.061 / -0.069` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |
| **SOLUSDT** | $80.41 | ⚪ **CASH** | **-6.7 bps** (±27.1) | `-0.0 bps` | `-0.004 / -0.067` | `0.71%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (27.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 10:30:51 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,253.24 | ⚪ **CASH** | **-16.8 bps** (±6.6) | `-22.6 bps` | `-0.049 / +0.006` | `0.56%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,949.92 | ⚪ **CASH** | **-19.5 bps** (±13.6) | `-20.1 bps` | `-0.061 / -0.069` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |
| **SOLUSDT** | $80.44 | ⚪ **CASH** | **-6.7 bps** (±27.1) | `-0.0 bps` | `-0.004 / -0.067` | `0.71%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (27.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 10:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,365.62 | ⚪ **CASH** | **-16.8 bps** (±6.6) | `-22.6 bps` | `-0.049 / +0.006` | `0.56%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,953.28 | ⚪ **CASH** | **-19.5 bps** (±13.6) | `-20.1 bps` | `-0.061 / -0.069` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |
| **SOLUSDT** | $80.41 | ⚪ **CASH** | **-6.7 bps** (±27.1) | `-0.0 bps` | `-0.004 / -0.067` | `0.71%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (27.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 10:00:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,111.90 | ⚪ **CASH** | **-16.8 bps** (±6.6) | `-22.6 bps` | `-0.049 / +0.006` | `0.56%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,944.42 | ⚪ **CASH** | **-19.5 bps** (±13.6) | `-20.1 bps` | `-0.061 / -0.069` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 31.6 bps) |
| **SOLUSDT** | $80.17 | ⚪ **CASH** | **-6.7 bps** (±27.1) | `-0.0 bps` | `-0.004 / -0.067` | `0.71%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (27.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 09:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,055.99 | ⚪ **CASH** | **-1.8 bps** (±10.3) | `+6.3 bps` | `-0.044 / -0.020` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,940.12 | ⚪ **CASH** | **-19.3 bps** (±11.1) | `-17.8 bps` | `-0.063 / -0.107` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $79.91 | ⚪ **CASH** | **-19.2 bps** (±22.1) | `-27.6 bps` | `+0.013 / -0.037` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 09:30:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,943.11 | ⚪ **CASH** | **-1.8 bps** (±10.3) | `+6.3 bps` | `-0.044 / -0.020` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,938.78 | ⚪ **CASH** | **-19.3 bps** (±11.1) | `-17.8 bps` | `-0.063 / -0.107` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $79.77 | ⚪ **CASH** | **-19.2 bps** (±22.1) | `-27.6 bps` | `+0.013 / -0.037` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 09:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,837.63 | ⚪ **CASH** | **-1.8 bps** (±10.3) | `+6.3 bps` | `-0.044 / -0.020` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,936.02 | ⚪ **CASH** | **-19.3 bps** (±11.1) | `-17.8 bps` | `-0.063 / -0.107` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $79.88 | ⚪ **CASH** | **-19.2 bps** (±22.1) | `-27.6 bps` | `+0.013 / -0.037` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 09:00:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,744.00 | ⚪ **CASH** | **-1.8 bps** (±10.3) | `+6.3 bps` | `-0.044 / -0.020` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,933.41 | ⚪ **CASH** | **-19.3 bps** (±11.1) | `-17.8 bps` | `-0.063 / -0.107` | `0.69%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $79.81 | ⚪ **CASH** | **-19.2 bps** (±22.1) | `-27.6 bps` | `+0.013 / -0.037` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (22.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 08:45:54 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,818.46 | ⚪ **CASH** | **+0.2 bps** (±7.0) | `+11.9 bps` | `-0.048 / -0.049` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,933.58 | ⚪ **CASH** | **-20.8 bps** (±6.2) | `-20.0 bps` | `-0.064 / -0.124` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $79.98 | ⚪ **CASH** | **-5.3 bps** (±26.1) | `-2.7 bps` | `+0.023 / -0.032` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 08:30:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,773.19 | ⚪ **CASH** | **+0.2 bps** (±7.0) | `+11.9 bps` | `-0.048 / -0.049` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,934.56 | ⚪ **CASH** | **-20.8 bps** (±6.2) | `-20.0 bps` | `-0.064 / -0.124` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $79.95 | ⚪ **CASH** | **-5.3 bps** (±26.1) | `-2.7 bps` | `+0.023 / -0.032` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 08:15:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,692.00 | ⚪ **CASH** | **+0.2 bps** (±7.0) | `+11.9 bps` | `-0.048 / -0.049` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,932.64 | ⚪ **CASH** | **-20.8 bps** (±6.2) | `-20.0 bps` | `-0.064 / -0.124` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $79.77 | ⚪ **CASH** | **-5.3 bps** (±26.1) | `-2.7 bps` | `+0.023 / -0.032` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 08:00:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,645.26 | ⚪ **CASH** | **+0.2 bps** (±7.0) | `+11.9 bps` | `-0.048 / -0.049` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,935.46 | ⚪ **CASH** | **-20.8 bps** (±6.2) | `-20.0 bps` | `-0.064 / -0.124` | `0.70%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $79.85 | ⚪ **CASH** | **-5.3 bps** (±26.1) | `-2.7 bps` | `+0.023 / -0.032` | `0.72%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (26.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 07:45:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,818.00 | ⚪ **CASH** | **-16.2 bps** (±11.3) | `-16.1 bps` | `-0.051 / -0.060` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,941.77 | ⚪ **CASH** | **-33.5 bps** (±11.8) | `-41.1 bps` | `-0.065 / -0.135` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $80.19 | ⚪ **CASH** | **-1.7 bps** (±36.6) | `+4.7 bps` | `+0.029 / -0.023` | `0.73%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 07:30:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,019.67 | ⚪ **CASH** | **-16.2 bps** (±11.3) | `-16.1 bps` | `-0.051 / -0.060` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,943.46 | ⚪ **CASH** | **-33.5 bps** (±11.8) | `-41.1 bps` | `-0.065 / -0.135` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $80.60 | ⚪ **CASH** | **-1.7 bps** (±36.6) | `+4.7 bps` | `+0.029 / -0.023` | `0.73%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 07:15:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,176.99 | ⚪ **CASH** | **-16.2 bps** (±11.3) | `-16.1 bps` | `-0.051 / -0.060` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,944.90 | ⚪ **CASH** | **-33.5 bps** (±11.8) | `-41.1 bps` | `-0.065 / -0.135` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $80.48 | ⚪ **CASH** | **-1.7 bps** (±36.6) | `+4.7 bps` | `+0.029 / -0.023` | `0.73%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 07:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $69,129.41 | ⚪ **CASH** | **-16.2 bps** (±11.3) | `-16.1 bps` | `-0.051 / -0.060` | `0.55%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **ETHUSDT** | $1,940.42 | ⚪ **CASH** | **-33.5 bps** (±11.8) | `-41.1 bps` | `-0.065 / -0.135` | `0.71%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 28.0 bps) |
| **SOLUSDT** | $80.23 | ⚪ **CASH** | **-1.7 bps** (±36.6) | `+4.7 bps` | `+0.029 / -0.023` | `0.73%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (36.6 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 06:45:46 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,948.00 | ⚪ **CASH** | **+4.3 bps** (±5.1) | `+24.3 bps` | `-0.062 / -0.099` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.1 bps) |
| **ETHUSDT** | $1,935.53 | ⚪ **CASH** | **-3.2 bps** (±25.5) | `+18.8 bps` | `-0.070 / -0.152` | `0.66%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.5 bps > 19.5) |
| **SOLUSDT** | $79.95 | ⚪ **CASH** | **-15.0 bps** (±34.1) | `-18.6 bps` | `+0.026 / -0.031` | `0.62%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (34.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 06:30:49 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,824.01 | ⚪ **CASH** | **+4.3 bps** (±5.1) | `+24.3 bps` | `-0.062 / -0.099` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.1 bps) |
| **ETHUSDT** | $1,935.63 | ⚪ **CASH** | **-3.2 bps** (±25.5) | `+18.8 bps` | `-0.070 / -0.152` | `0.66%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.5 bps > 19.5) |
| **SOLUSDT** | $79.79 | ⚪ **CASH** | **-15.0 bps** (±34.1) | `-18.6 bps` | `+0.026 / -0.031` | `0.62%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (34.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 06:15:36 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $68,374.46 | ⚪ **CASH** | **+4.3 bps** (±5.1) | `+24.3 bps` | `-0.062 / -0.099` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.1 bps) |
| **ETHUSDT** | $1,918.67 | ⚪ **CASH** | **-3.2 bps** (±25.5) | `+18.8 bps` | `-0.070 / -0.152` | `0.66%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.5 bps > 19.5) |
| **SOLUSDT** | $78.93 | ⚪ **CASH** | **-15.0 bps** (±34.1) | `-18.6 bps` | `+0.026 / -0.031` | `0.62%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (34.1 bps > 19.5) |

---

### 🕒 Ciclo `2026-11-13 06:00:44 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $67,962.51 | ⚪ **CASH** | **+4.3 bps** (±5.1) | `+24.3 bps` | `-0.062 / -0.099` | `0.48%/h` | `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 30.1 bps) |
| **ETHUSDT** | $1,905.51 | ⚪ **CASH** | **-3.2 bps** (±25.5) | `+18.8 bps` | `-0.070 / -0.152` | `0.66%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (25.5 bps > 19.5) |
| **SOLUSDT** | $78.29 | ⚪ **CASH** | **-15.0 bps** (±34.1) | `-18.6 bps` | `+0.026 / -0.031` | `0.62%/h` | `btc_dumping` `high_uncertainty` `weak_order_flow` | Filtro: divergência alta no ensemble (34.1 bps > 19.5) |
