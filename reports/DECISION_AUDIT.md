# 📋 BOT_TRADE V5.3 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-11-13 02:15:50 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-13 02:15:50 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $70,565.98 | ⚪ **CASH** | **-5.3 bps** (±7.0) | `+1.4 bps` | `-0.028 / -0.086` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $1,998.70 | ⚪ **CASH** | **+21.9 bps** (±11.8) | `+39.6 bps` | `-0.018 / +0.082` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $80.76 | ⚪ **CASH** | **-10.3 bps** (±9.5) | `-28.7 bps` | `+0.058 / +0.112` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 02:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $70,937.27 | ⚪ **CASH** | **-5.3 bps** (±7.0) | `+1.4 bps` | `-0.028 / -0.086` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,011.02 | ⚪ **CASH** | **+21.9 bps** (±11.8) | `+39.6 bps` | `-0.018 / +0.082` | `0.44%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.26 | ⚪ **CASH** | **-10.3 bps** (±9.5) | `-28.7 bps` | `+0.058 / +0.112` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 01:45:41 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $70,988.00 | ⚪ **CASH** | **-5.6 bps** (±5.3) | `+3.9 bps` | `-0.036 / -0.120` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,011.66 | ⚪ **CASH** | **+32.3 bps** (±8.7) | `+56.7 bps` | `-0.018 / +0.109` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.42 | ⚪ **CASH** | **-0.7 bps** (±4.3) | `-14.6 bps` | `+0.048 / +0.170` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 01:30:53 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,167.73 | ⚪ **CASH** | **-5.6 bps** (±5.3) | `+3.9 bps` | `-0.036 / -0.120` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,015.90 | ⚪ **CASH** | **+32.3 bps** (±8.7) | `+56.7 bps` | `-0.018 / +0.109` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.58 | ⚪ **CASH** | **-0.7 bps** (±4.3) | `-14.6 bps` | `+0.048 / +0.170` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 01:15:38 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $70,905.44 | ⚪ **CASH** | **-5.6 bps** (±5.3) | `+3.9 bps` | `-0.036 / -0.120` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,009.31 | ⚪ **CASH** | **+32.3 bps** (±8.7) | `+56.7 bps` | `-0.018 / +0.109` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.41 | ⚪ **CASH** | **-0.7 bps** (±4.3) | `-14.6 bps` | `+0.048 / +0.170` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 01:00:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,074.01 | ⚪ **CASH** | **-5.6 bps** (±5.3) | `+3.9 bps` | `-0.036 / -0.120` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,009.53 | ⚪ **CASH** | **+32.3 bps** (±8.7) | `+56.7 bps` | `-0.018 / +0.109` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.51 | ⚪ **CASH** | **-0.7 bps** (±4.3) | `-14.6 bps` | `+0.048 / +0.170` | `0.49%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 00:45:43 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $70,930.01 | ⚪ **CASH** | **-2.5 bps** (±2.6) | `+3.8 bps` | `-0.020 / -0.078` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,004.86 | ⚪ **CASH** | **+22.4 bps** (±4.3) | `+33.0 bps` | `-0.008 / +0.157` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.16 | ⚪ **CASH** | **+0.5 bps** (±4.7) | `-15.2 bps` | `+0.044 / +0.206` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 00:30:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,238.95 | ⚪ **CASH** | **-2.5 bps** (±2.6) | `+3.8 bps` | `-0.020 / -0.078` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,013.55 | ⚪ **CASH** | **+22.4 bps** (±4.3) | `+33.0 bps` | `-0.008 / +0.157` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.59 | ⚪ **CASH** | **+0.5 bps** (±4.7) | `-15.2 bps` | `+0.044 / +0.206` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 00:15:52 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,340.94 | ⚪ **CASH** | **-2.5 bps** (±2.6) | `+3.8 bps` | `-0.020 / -0.078` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,016.15 | ⚪ **CASH** | **+22.4 bps** (±4.3) | `+33.0 bps` | `-0.008 / +0.157` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.66 | ⚪ **CASH** | **+0.5 bps** (±4.7) | `-15.2 bps` | `+0.044 / +0.206` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-13 00:00:55 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,471.03 | ⚪ **CASH** | **-2.5 bps** (±2.6) | `+3.8 bps` | `-0.020 / -0.078` | `0.36%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,020.17 | ⚪ **CASH** | **+22.4 bps** (±4.3) | `+33.0 bps` | `-0.008 / +0.157` | `0.45%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.79 | ⚪ **CASH** | **+0.5 bps** (±4.7) | `-15.2 bps` | `+0.044 / +0.206` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 23:45:40 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,306.71 | ⚪ **CASH** | **+0.0 bps** (±4.3) | `+6.6 bps` | `-0.019 / -0.046` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,017.65 | ⚪ **CASH** | **+28.3 bps** (±7.9) | `+45.3 bps` | `-0.010 / +0.145` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.69 | ⚪ **CASH** | **-0.1 bps** (±9.1) | `-10.5 bps` | `+0.020 / +0.166` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 23:30:39 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,397.16 | ⚪ **CASH** | **+0.0 bps** (±4.3) | `+6.6 bps` | `-0.019 / -0.046` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,017.61 | ⚪ **CASH** | **+28.3 bps** (±7.9) | `+45.3 bps` | `-0.010 / +0.145` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.68 | ⚪ **CASH** | **-0.1 bps** (±9.1) | `-10.5 bps` | `+0.020 / +0.166` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

### 🕒 Ciclo `2026-11-12 23:15:42 UTC` | Patrimônio: **$960.36 USDT** (Caixa: `$960.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $71,468.30 | ⚪ **CASH** | **+0.0 bps** (±4.3) | `+6.6 bps` | `-0.019 / -0.046` | `0.37%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **ETHUSDT** | $2,017.85 | ⚪ **CASH** | **+28.3 bps** (±7.9) | `+45.3 bps` | `-0.010 / +0.145` | `0.46%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |
| **SOLUSDT** | $81.69 | ⚪ **CASH** | **-0.1 bps** (±9.1) | `-10.5 bps` | `+0.020 / +0.166` | `0.50%/h` | `vol_compressed` `btc_dumping` `weak_order_flow` | Aguardando setup com assimetria (> 36.0 bps) |

---

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
