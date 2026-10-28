# 📋 BOT_TRADE V5.1 — Livro de Auditoria de Decisões e Análise de Mercado (Swing 12h + CVD)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o Alpha Composto de 12h (Ensemble 5x XGBoost + Order Flow CVD) e o disparo de travas de proteção.

**Última Atualização**: `2026-10-28 21:32:47 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-10-28 21:32:47 UTC` | Patrimônio: **$996.97 USDT** (Caixa: `$448.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,160.00 | 🟡 **HOLD** | **+21.7 bps** (±8.8) | `-3.1 bps` | `+0.165 / +0.303` | `0.30%/h` | Liberado ✅ | Posição ativa há 11.5h (PnL: -0.49% | Pico: +0.25%) |
| **ETHUSDT** | $2,356.20 | 🟡 **HOLD** | **+27.3 bps** (±15.3) | `+32.1 bps` | `+0.045 / +0.118` | `0.37%/h` | Liberado ✅ | Posição ativa há 0.5h (PnL: -0.18% | Pico: +0.21%) |
| **SOLUSDT** | $102.23 | ⚪ **CASH** | **+29.9 bps** (±11.0) | `+20.8 bps` | `+0.126 / +0.230` | `0.43%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-10-28 21:17:27 UTC` | Patrimônio: **$998.94 USDT** (Caixa: `$448.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,432.07 | 🟡 **HOLD** | **+21.7 bps** (±8.8) | `-3.1 bps` | `+0.165 / +0.303` | `0.30%/h` | Liberado ✅ | Posição ativa há 11.3h (PnL: -0.16% | Pico: +0.25%) |
| **ETHUSDT** | $2,365.49 | 🟡 **HOLD** | **+27.3 bps** (±15.3) | `+32.1 bps` | `+0.045 / +0.118` | `0.37%/h` | Liberado ✅ | Posição ativa há 0.2h (PnL: +0.21% | Pico: +0.21%) |
| **SOLUSDT** | $102.83 | ⚪ **CASH** | **+29.9 bps** (±11.0) | `+20.8 bps` | `+0.126 / +0.230` | `0.43%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-10-28 21:02:38 UTC` | Patrimônio: **$997.98 USDT** (Caixa: `$448.36`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,308.00 | 🟡 **HOLD** | **+21.7 bps** (±8.8) | `-3.1 bps` | `+0.165 / +0.303` | `0.30%/h` | Liberado ✅ | Posição ativa há 11.0h (PnL: -0.31% | Pico: +0.25%) |
| **ETHUSDT** | $2,360.55 | 🟢 **BUY** | **+27.3 bps** (±15.3) | `+32.1 bps` | `+0.045 / +0.118` | `0.37%/h` | Liberado ✅ | Entrada Swing 12h aprovada (Alpha +27.3 bps > 24.0 bps | CVD 24h +0.045) |
| **SOLUSDT** | $102.49 | ⚪ **CASH** | **+29.9 bps** (±11.0) | `+20.8 bps` | `+0.126 / +0.230` | `0.43%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-10-28 20:47:31 UTC` | Patrimônio: **$997.14 USDT** (Caixa: `$669.59`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,036.00 | 🟡 **HOLD** | **+37.9 bps** (±12.8) | `+26.1 bps` | `+0.166 / +0.315` | `0.29%/h` | `stretched_top` | Posição ativa há 10.8h (PnL: -0.64% | Pico: +0.25%) |
| **ETHUSDT** | $2,351.58 | ⚪ **CASH** | **+30.0 bps** (±18.0) | `+36.6 bps` | `+0.047 / +0.130` | `0.37%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $102.08 | ⚪ **CASH** | **+33.8 bps** (±6.1) | `+21.3 bps` | `+0.143 / +0.292` | `0.42%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-10-28 20:32:39 UTC` | Patrimônio: **$997.99 USDT** (Caixa: `$669.59`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,245.99 | 🟡 **HOLD** | **+37.9 bps** (±12.8) | `+26.1 bps` | `+0.166 / +0.315` | `0.29%/h` | `stretched_top` | Posição ativa há 10.5h (PnL: -0.38% | Pico: +0.25%) |
| **ETHUSDT** | $2,357.21 | ⚪ **CASH** | **+30.0 bps** (±18.0) | `+36.6 bps` | `+0.047 / +0.130` | `0.37%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $102.23 | ⚪ **CASH** | **+33.8 bps** (±6.1) | `+21.3 bps` | `+0.143 / +0.292` | `0.42%/h` | `cooldown_active` | Filtro: aguardando cooldown pós-trade (3h) |

---

### 🕒 Ciclo `2026-10-28 20:17:27 UTC` | Patrimônio: **$998.13 USDT** (Caixa: `$669.59`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,280.00 | 🟡 **HOLD** | **+37.9 bps** (±12.8) | `+26.1 bps` | `+0.166 / +0.315` | `0.29%/h` | `stretched_top` | Posição ativa há 10.3h (PnL: -0.34% | Pico: +0.25%) |
| **ETHUSDT** | $2,364.97 | ⚪ **CASH** | **+30.0 bps** (±18.0) | `+36.6 bps` | `+0.047 / +0.130` | `0.37%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $102.67 | 🔴 **SELL** | **+33.8 bps** (±6.1) | `+21.3 bps` | `+0.143 / +0.292` | `0.42%/h` | Liberado ✅ | Trailing Stop acionado (pico +1.59%, realizou +0.54%) |

---

### 🕒 Ciclo `2026-10-28 20:02:32 UTC` | Patrimônio: **$1,002.66 USDT** (Caixa: `$447.92`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,763.88 | 🟡 **HOLD** | **+37.9 bps** (±12.8) | `+26.1 bps` | `+0.166 / +0.315` | `0.29%/h` | `stretched_top` | Posição ativa há 10.0h (PnL: +0.25% | Pico: +0.25%) |
| **ETHUSDT** | $2,386.54 | ⚪ **CASH** | **+30.0 bps** (±18.0) | `+36.6 bps` | `+0.047 / +0.130` | `0.37%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $103.74 | 🟡 **HOLD** | **+33.8 bps** (±6.1) | `+21.3 bps` | `+0.143 / +0.292` | `0.42%/h` | Liberado ✅ | Posição ativa há 1.0h (PnL: +1.59% | Pico: +1.59%) |

---

### 🕒 Ciclo `2026-10-28 19:47:27 UTC` | Patrimônio: **$998.49 USDT** (Caixa: `$447.92`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,373.14 | 🟡 **HOLD** | **+29.0 bps** (±8.5) | `+16.8 bps` | `+0.150 / +0.236` | `0.27%/h` | `vol_compressed` | Posição ativa há 9.8h (PnL: -0.23% | Pico: +0.05%) |
| **ETHUSDT** | $2,364.96 | ⚪ **CASH** | **+28.1 bps** (±10.6) | `+39.3 bps` | `+0.032 / +0.050` | `0.36%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $102.54 | 🟡 **HOLD** | **+41.8 bps** (±19.3) | `+43.4 bps` | `+0.127 / +0.249` | `0.40%/h` | Liberado ✅ | Posição ativa há 0.7h (PnL: +0.41% | Pico: +0.41%) |

---

### 🕒 Ciclo `2026-10-28 19:32:25 UTC` | Patrimônio: **$997.27 USDT** (Caixa: `$447.92`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,215.02 | 🟡 **HOLD** | **+29.0 bps** (±8.5) | `+16.8 bps` | `+0.150 / +0.236` | `0.27%/h` | `vol_compressed` | Posição ativa há 9.5h (PnL: -0.42% | Pico: +0.05%) |
| **ETHUSDT** | $2,360.34 | ⚪ **CASH** | **+28.1 bps** (±10.6) | `+39.3 bps` | `+0.032 / +0.050` | `0.36%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $102.27 | 🟡 **HOLD** | **+41.8 bps** (±19.3) | `+43.4 bps` | `+0.127 / +0.249` | `0.40%/h` | Liberado ✅ | Posição ativa há 0.5h (PnL: +0.15% | Pico: +0.15%) |

---

### 🕒 Ciclo `2026-10-28 19:17:21 UTC` | Patrimônio: **$996.35 USDT** (Caixa: `$447.92`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,080.00 | 🟡 **HOLD** | **+29.0 bps** (±8.5) | `+16.8 bps` | `+0.150 / +0.236` | `0.27%/h` | `vol_compressed` | Posição ativa há 9.3h (PnL: -0.59% | Pico: +0.05%) |
| **ETHUSDT** | $2,355.32 | ⚪ **CASH** | **+28.1 bps** (±10.6) | `+39.3 bps` | `+0.032 / +0.050` | `0.36%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $102.10 | 🟡 **HOLD** | **+41.8 bps** (±19.3) | `+43.4 bps` | `+0.127 / +0.249` | `0.40%/h` | Liberado ✅ | Posição ativa há 0.2h (PnL: -0.02% | Pico: +0.00%) |

---

### 🕒 Ciclo `2026-10-28 19:02:47 UTC` | Patrimônio: **$996.26 USDT** (Caixa: `$447.92`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,046.19 | 🟡 **HOLD** | **+29.0 bps** (±8.5) | `+16.8 bps` | `+0.150 / +0.236` | `0.27%/h` | `vol_compressed` | Posição ativa há 9.0h (PnL: -0.63% | Pico: +0.05%) |
| **ETHUSDT** | $2,355.20 | ⚪ **CASH** | **+28.1 bps** (±10.6) | `+39.3 bps` | `+0.032 / +0.050` | `0.36%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $102.12 | 🟢 **BUY** | **+41.8 bps** (±19.3) | `+43.4 bps` | `+0.127 / +0.249` | `0.40%/h` | Liberado ✅ | Entrada Swing 12h aprovada (Alpha +41.8 bps > 24.0 bps | CVD 24h +0.127) |

---

### 🕒 Ciclo `2026-10-28 18:47:40 UTC` | Patrimônio: **$996.58 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $81,059.39 | 🟡 **HOLD** | **+25.9 bps** (±5.1) | `+13.9 bps` | `+0.153 / +0.179` | `0.27%/h` | Liberado ✅ | Posição ativa há 8.8h (PnL: -0.61% | Pico: +0.05%) |
| **ETHUSDT** | $2,355.50 | ⚪ **CASH** | **-1.6 bps** (±11.1) | `-10.7 bps` | `+0.032 / -0.014` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $102.16 | ⚪ **CASH** | **+10.0 bps** (±11.6) | `-3.1 bps` | `+0.086 / +0.113` | `0.40%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 18:32:33 UTC` | Patrimônio: **$995.61 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,820.01 | 🟡 **HOLD** | **+25.9 bps** (±5.1) | `+13.9 bps` | `+0.153 / +0.179` | `0.27%/h` | Liberado ✅ | Posição ativa há 8.5h (PnL: -0.91% | Pico: +0.05%) |
| **ETHUSDT** | $2,342.46 | ⚪ **CASH** | **-1.6 bps** (±11.1) | `-10.7 bps` | `+0.032 / -0.014` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.33 | ⚪ **CASH** | **+10.0 bps** (±11.6) | `-3.1 bps` | `+0.086 / +0.113` | `0.40%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 18:19:30 UTC` | Patrimônio: **$995.61 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,819.56 | 🟡 **HOLD** | **+25.9 bps** (±5.1) | `+13.9 bps` | `+0.153 / +0.179` | `0.27%/h` | Liberado ✅ | Posição ativa há 8.3h (PnL: -0.91% | Pico: +0.05%) |
| **ETHUSDT** | $2,344.52 | ⚪ **CASH** | **-1.6 bps** (±11.1) | `-10.7 bps` | `+0.032 / -0.014` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.50 | ⚪ **CASH** | **+10.0 bps** (±11.6) | `-3.1 bps` | `+0.086 / +0.113` | `0.40%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 18:02:31 UTC` | Patrimônio: **$996.15 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,953.88 | 🟡 **HOLD** | **+25.9 bps** (±5.1) | `+13.9 bps` | `+0.153 / +0.179` | `0.27%/h` | Liberado ✅ | Posição ativa há 8.0h (PnL: -0.74% | Pico: +0.05%) |
| **ETHUSDT** | $2,347.83 | ⚪ **CASH** | **-1.6 bps** (±11.1) | `-10.7 bps` | `+0.032 / -0.014` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.73 | ⚪ **CASH** | **+10.0 bps** (±11.6) | `-3.1 bps` | `+0.086 / +0.113` | `0.40%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 17:47:30 UTC` | Patrimônio: **$995.25 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,729.70 | 🟡 **HOLD** | **+23.3 bps** (±6.2) | `+14.8 bps` | `+0.147 / +0.108` | `0.27%/h` | Liberado ✅ | Posição ativa há 7.8h (PnL: -1.02% | Pico: +0.05%) |
| **ETHUSDT** | $2,340.93 | ⚪ **CASH** | **-5.4 bps** (±8.3) | `-15.5 bps` | `+0.030 / -0.046` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.48 | ⚪ **CASH** | **+6.8 bps** (±8.1) | `-2.1 bps` | `+0.068 / +0.032` | `0.40%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 17:32:27 UTC` | Patrimônio: **$994.73 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,602.01 | 🟡 **HOLD** | **+23.3 bps** (±6.2) | `+14.8 bps` | `+0.147 / +0.108` | `0.27%/h` | Liberado ✅ | Posição ativa há 7.5h (PnL: -1.17% | Pico: +0.05%) |
| **ETHUSDT** | $2,334.55 | ⚪ **CASH** | **-5.4 bps** (±8.3) | `-15.5 bps` | `+0.030 / -0.046` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.05 | ⚪ **CASH** | **+6.8 bps** (±8.1) | `-2.1 bps` | `+0.068 / +0.032` | `0.40%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 17:17:35 UTC` | Patrimônio: **$994.39 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,517.50 | 🟡 **HOLD** | **+23.3 bps** (±6.2) | `+14.8 bps` | `+0.147 / +0.108` | `0.27%/h` | Liberado ✅ | Posição ativa há 7.3h (PnL: -1.28% | Pico: +0.05%) |
| **ETHUSDT** | $2,332.94 | ⚪ **CASH** | **-5.4 bps** (±8.3) | `-15.5 bps` | `+0.030 / -0.046` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.08 | ⚪ **CASH** | **+6.8 bps** (±8.1) | `-2.1 bps` | `+0.068 / +0.032` | `0.40%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 17:02:28 UTC` | Patrimônio: **$994.62 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,574.01 | 🟡 **HOLD** | **+23.3 bps** (±6.2) | `+14.8 bps` | `+0.147 / +0.108` | `0.27%/h` | Liberado ✅ | Posição ativa há 7.0h (PnL: -1.21% | Pico: +0.05%) |
| **ETHUSDT** | $2,335.52 | ⚪ **CASH** | **-5.4 bps** (±8.3) | `-15.5 bps` | `+0.030 / -0.046` | `0.35%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.22 | ⚪ **CASH** | **+6.8 bps** (±8.1) | `-2.1 bps` | `+0.068 / +0.032` | `0.40%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 16:47:25 UTC` | Patrimônio: **$994.19 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,468.85 | 🟡 **HOLD** | **+21.0 bps** (±8.7) | `+11.7 bps` | `+0.156 / +0.077` | `0.27%/h` | Liberado ✅ | Posição ativa há 6.8h (PnL: -1.34% | Pico: +0.05%) |
| **ETHUSDT** | $2,329.76 | ⚪ **CASH** | **+7.4 bps** (±7.1) | `+3.7 bps` | `+0.048 / -0.021` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.86 | ⚪ **CASH** | **+4.2 bps** (±9.3) | `-2.6 bps` | `+0.054 / -0.016` | `0.40%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 16:32:50 UTC` | Patrimônio: **$994.50 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,545.45 | 🟡 **HOLD** | **+21.0 bps** (±8.7) | `+11.7 bps` | `+0.156 / +0.077` | `0.27%/h` | Liberado ✅ | Posição ativa há 6.5h (PnL: -1.24% | Pico: +0.05%) |
| **ETHUSDT** | $2,333.60 | ⚪ **CASH** | **+7.4 bps** (±7.1) | `+3.7 bps` | `+0.048 / -0.021` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.08 | ⚪ **CASH** | **+4.2 bps** (±9.3) | `-2.6 bps` | `+0.054 / -0.016` | `0.40%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 16:17:40 UTC` | Patrimônio: **$994.51 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,547.04 | 🟡 **HOLD** | **+21.0 bps** (±8.7) | `+11.7 bps` | `+0.156 / +0.077` | `0.27%/h` | Liberado ✅ | Posição ativa há 6.3h (PnL: -1.24% | Pico: +0.05%) |
| **ETHUSDT** | $2,332.87 | ⚪ **CASH** | **+7.4 bps** (±7.1) | `+3.7 bps` | `+0.048 / -0.021` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.96 | ⚪ **CASH** | **+4.2 bps** (±9.3) | `-2.6 bps` | `+0.054 / -0.016` | `0.40%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 16:02:50 UTC` | Patrimônio: **$994.55 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,558.01 | 🟡 **HOLD** | **+21.0 bps** (±8.7) | `+11.7 bps` | `+0.156 / +0.077` | `0.27%/h` | Liberado ✅ | Posição ativa há 6.0h (PnL: -1.23% | Pico: +0.05%) |
| **ETHUSDT** | $2,333.68 | ⚪ **CASH** | **+7.4 bps** (±7.1) | `+3.7 bps` | `+0.048 / -0.021` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.01 | ⚪ **CASH** | **+4.2 bps** (±9.3) | `-2.6 bps` | `+0.054 / -0.016` | `0.40%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 15:47:23 UTC` | Patrimônio: **$994.78 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,614.02 | 🟡 **HOLD** | **+22.9 bps** (±7.6) | `+12.6 bps` | `+0.170 / +0.080` | `0.28%/h` | Liberado ✅ | Posição ativa há 5.8h (PnL: -1.16% | Pico: +0.05%) |
| **ETHUSDT** | $2,335.03 | ⚪ **CASH** | **-1.1 bps** (±10.1) | `-12.0 bps` | `+0.074 / -0.059` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.06 | ⚪ **CASH** | **+5.2 bps** (±9.3) | `-4.1 bps` | `+0.066 / +0.006` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 15:32:27 UTC` | Patrimônio: **$994.63 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,578.00 | 🟡 **HOLD** | **+22.9 bps** (±7.6) | `+12.6 bps` | `+0.170 / +0.080` | `0.28%/h` | Liberado ✅ | Posição ativa há 5.5h (PnL: -1.20% | Pico: +0.05%) |
| **ETHUSDT** | $2,332.42 | ⚪ **CASH** | **-1.1 bps** (±10.1) | `-12.0 bps` | `+0.074 / -0.059` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.95 | ⚪ **CASH** | **+5.2 bps** (±9.3) | `-4.1 bps` | `+0.066 / +0.006` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 15:17:19 UTC` | Patrimônio: **$995.10 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,693.60 | 🟡 **HOLD** | **+22.9 bps** (±7.6) | `+12.6 bps` | `+0.170 / +0.080` | `0.28%/h` | Liberado ✅ | Posição ativa há 5.3h (PnL: -1.06% | Pico: +0.05%) |
| **ETHUSDT** | $2,336.63 | ⚪ **CASH** | **-1.1 bps** (±10.1) | `-12.0 bps` | `+0.074 / -0.059` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.09 | ⚪ **CASH** | **+5.2 bps** (±9.3) | `-4.1 bps` | `+0.066 / +0.006` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 15:02:09 UTC` | Patrimônio: **$995.03 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,677.13 | 🟡 **HOLD** | **+22.9 bps** (±7.6) | `+12.6 bps` | `+0.170 / +0.080` | `0.28%/h` | Liberado ✅ | Posição ativa há 5.0h (PnL: -1.08% | Pico: +0.05%) |
| **ETHUSDT** | $2,336.56 | ⚪ **CASH** | **-1.1 bps** (±10.1) | `-12.0 bps` | `+0.074 / -0.059` | `0.36%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.10 | ⚪ **CASH** | **+5.2 bps** (±9.3) | `-4.1 bps` | `+0.066 / +0.006` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 14:47:06 UTC` | Patrimônio: **$994.71 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,596.01 | 🟡 **HOLD** | **+22.3 bps** (±9.3) | `+11.5 bps` | `+0.170 / +0.087` | `0.28%/h` | Liberado ✅ | Posição ativa há 4.7h (PnL: -1.18% | Pico: +0.05%) |
| **ETHUSDT** | $2,333.32 | ⚪ **CASH** | **+17.7 bps** (±2.8) | `+18.4 bps` | `+0.075 / -0.023` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.95 | ⚪ **CASH** | **+5.5 bps** (±15.8) | `-4.0 bps` | `+0.078 / +0.014` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 14:32:08 UTC` | Patrimônio: **$994.52 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,550.01 | 🟡 **HOLD** | **+22.3 bps** (±9.3) | `+11.5 bps` | `+0.170 / +0.087` | `0.28%/h` | Liberado ✅ | Posição ativa há 4.5h (PnL: -1.24% | Pico: +0.05%) |
| **ETHUSDT** | $2,330.36 | ⚪ **CASH** | **+17.7 bps** (±2.8) | `+18.4 bps` | `+0.075 / -0.023` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.63 | ⚪ **CASH** | **+5.5 bps** (±15.8) | `-4.0 bps` | `+0.078 / +0.014` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 14:17:03 UTC` | Patrimônio: **$994.49 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,542.40 | 🟡 **HOLD** | **+22.3 bps** (±9.3) | `+11.5 bps` | `+0.170 / +0.087` | `0.28%/h` | Liberado ✅ | Posição ativa há 4.2h (PnL: -1.25% | Pico: +0.05%) |
| **ETHUSDT** | $2,327.86 | ⚪ **CASH** | **+17.7 bps** (±2.8) | `+18.4 bps` | `+0.075 / -0.023` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $100.65 | ⚪ **CASH** | **+5.5 bps** (±15.8) | `-4.0 bps` | `+0.078 / +0.014` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 14:02:10 UTC` | Patrimônio: **$995.15 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,705.98 | 🟡 **HOLD** | **+22.3 bps** (±9.3) | `+11.5 bps` | `+0.170 / +0.087` | `0.28%/h` | Liberado ✅ | Posição ativa há 4.0h (PnL: -1.05% | Pico: +0.05%) |
| **ETHUSDT** | $2,334.96 | ⚪ **CASH** | **+17.7 bps** (±2.8) | `+18.4 bps` | `+0.075 / -0.023` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.01 | ⚪ **CASH** | **+5.5 bps** (±15.8) | `-4.0 bps` | `+0.078 / +0.014` | `0.41%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 13:47:03 UTC` | Patrimônio: **$994.71 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,595.83 | 🟡 **HOLD** | **+21.3 bps** (±10.2) | `+8.2 bps` | `+0.175 / +0.100` | `0.29%/h` | Liberado ✅ | Posição ativa há 3.7h (PnL: -1.18% | Pico: +0.05%) |
| **ETHUSDT** | $2,330.73 | ⚪ **CASH** | **+19.9 bps** (±12.4) | `+21.4 bps` | `+0.081 / +0.008` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.27 | ⚪ **CASH** | **+1.5 bps** (±16.3) | `-12.9 bps` | `+0.085 / +0.026` | `0.41%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 13:32:28 UTC` | Patrimônio: **$995.34 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,753.38 | 🟡 **HOLD** | **+21.3 bps** (±10.2) | `+8.2 bps` | `+0.175 / +0.100` | `0.29%/h` | Liberado ✅ | Posição ativa há 3.5h (PnL: -0.99% | Pico: +0.05%) |
| **ETHUSDT** | $2,341.88 | ⚪ **CASH** | **+19.9 bps** (±12.4) | `+21.4 bps` | `+0.081 / +0.008` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.49 | ⚪ **CASH** | **+1.5 bps** (±16.3) | `-12.9 bps` | `+0.085 / +0.026` | `0.41%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 13:17:13 UTC` | Patrimônio: **$995.30 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,742.76 | 🟡 **HOLD** | **+21.3 bps** (±10.2) | `+8.2 bps` | `+0.175 / +0.100` | `0.29%/h` | Liberado ✅ | Posição ativa há 3.3h (PnL: -1.00% | Pico: +0.05%) |
| **ETHUSDT** | $2,339.43 | ⚪ **CASH** | **+19.9 bps** (±12.4) | `+21.4 bps` | `+0.081 / +0.008` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.46 | ⚪ **CASH** | **+1.5 bps** (±16.3) | `-12.9 bps` | `+0.085 / +0.026` | `0.41%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 13:02:02 UTC` | Patrimônio: **$995.35 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,755.93 | 🟡 **HOLD** | **+21.3 bps** (±10.2) | `+8.2 bps` | `+0.175 / +0.100` | `0.29%/h` | Liberado ✅ | Posição ativa há 3.0h (PnL: -0.99% | Pico: +0.05%) |
| **ETHUSDT** | $2,340.89 | ⚪ **CASH** | **+19.9 bps** (±12.4) | `+21.4 bps` | `+0.081 / +0.008` | `0.37%/h` | `weak_order_flow` | Aguardando setup com assimetria (> 24.0 bps) |
| **SOLUSDT** | $101.62 | ⚪ **CASH** | **+1.5 bps** (±16.3) | `-12.9 bps` | `+0.085 / +0.026` | `0.41%/h` | Liberado ✅ | Aguardando setup com assimetria (> 24.0 bps) |

---

### 🕒 Ciclo `2026-10-28 12:47:00 UTC` | Patrimônio: **$995.41 USDT** (Caixa: `$668.94`)

| Ativo | Preço | Sinal | Alpha 12h Efetivo | ML 12h | Order Flow (CVD 24h/6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|---:|:---:|:---:|:---|:---|
| **BTCUSDT** | $80,770.00 | 🟡 **HOLD** | **+30.8 bps** (±10.8) | `+21.9 bps` | `+0.192 / +0.118` | `0.26%/h` | Liberado ✅ | Posição ativa há 2.7h (PnL: -0.97% | Pico: +0.05%) |
| **ETHUSDT** | $2,340.04 | ⚪ **CASH** | **+24.6 bps** (±10.9) | `+26.0 bps` | `+0.096 / +0.030` | `0.33%/h` | `vol_compressed` | Filtro: compressão de volatilidade (< 0.70) |
| **SOLUSDT** | $101.59 | ⚪ **CASH** | **+11.5 bps** (±24.3) | `-1.5 bps` | `+0.117 / +0.090` | `0.36%/h` | `vol_compressed` | Aguardando setup com assimetria (> 24.0 bps) |
