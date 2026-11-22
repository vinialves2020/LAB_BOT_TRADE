# 📋 BOT_TRADE V6.0 — Livro de Auditoria Institucional (CTA Long/Short 1x)

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo **V6.0 Institutional Regime-Weighted CTA** na Binance.
Opera comprado (`LONG 1x`) e vendido (`SHORT 1x`) guiado por Momentum Multi-Dias (`EMA 48h/168h/720h`), dimensionamento inverso à volatilidade (`30% Vol Target`), Chandelier ATR Stop (`5.5x`) e ajuste de convicção via Ensemble 5x XGBoost.

**Última Atualização**: `2026-11-22 23:45:52 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-11-22 23:45:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,262.41 | ⚪ **CASH** | **-3.34%** | `MACRO_BEAR` | `72%` | `+5.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,721.28 | ⚪ **CASH** | **-3.40%** | `MACRO_BEAR` | `81%` | `+17.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.61 | ⚪ **CASH** | **-2.83%** | `MACRO_BEAR` | `83%` | `+26.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 23:30:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,184.32 | ⚪ **CASH** | **-3.34%** | `MACRO_BEAR` | `72%` | `+5.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,725.35 | ⚪ **CASH** | **-3.39%** | `MACRO_BEAR` | `81%` | `+17.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.70 | ⚪ **CASH** | **-2.82%** | `MACRO_BEAR` | `83%` | `+26.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 23:15:42 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,042.01 | ⚪ **CASH** | **-3.35%** | `MACRO_BEAR` | `72%` | `+5.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,721.54 | ⚪ **CASH** | **-3.40%** | `MACRO_BEAR` | `81%` | `+17.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.49 | ⚪ **CASH** | **-2.83%** | `MACRO_BEAR` | `83%` | `+26.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 23:00:57 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,196.01 | ⚪ **CASH** | **-3.34%** | `MACRO_BEAR` | `72%` | `+5.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,724.30 | ⚪ **CASH** | **-3.39%** | `MACRO_BEAR` | `81%` | `+17.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.62 | ⚪ **CASH** | **-2.83%** | `MACRO_BEAR` | `83%` | `+26.8 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 22:45:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,838.02 | ⚪ **CASH** | **-3.43%** | `MACRO_BEAR` | `72%` | `+10.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,712.87 | ⚪ **CASH** | **-3.49%** | `MACRO_BEAR` | `81%` | `+26.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.11 | ⚪ **CASH** | **-2.89%** | `MACRO_BEAR` | `83%` | `+36.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 22:30:50 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,807.28 | ⚪ **CASH** | **-3.43%** | `MACRO_BEAR` | `72%` | `+10.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,713.20 | ⚪ **CASH** | **-3.49%** | `MACRO_BEAR` | `81%` | `+26.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.06 | ⚪ **CASH** | **-2.89%** | `MACRO_BEAR` | `83%` | `+36.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 22:15:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,942.73 | ⚪ **CASH** | **-3.43%** | `MACRO_BEAR` | `72%` | `+10.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,717.80 | ⚪ **CASH** | **-3.48%** | `MACRO_BEAR` | `81%` | `+26.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.35 | ⚪ **CASH** | **-2.88%** | `MACRO_BEAR` | `83%` | `+36.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 22:00:47 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,964.00 | ⚪ **CASH** | **-3.42%** | `MACRO_BEAR` | `72%` | `+10.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,719.44 | ⚪ **CASH** | **-3.48%** | `MACRO_BEAR` | `81%` | `+26.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.45 | ⚪ **CASH** | **-2.87%** | `MACRO_BEAR` | `83%` | `+36.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 21:45:46 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,043.11 | ⚪ **CASH** | **-3.49%** | `MACRO_BEAR` | `72%` | `+2.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,724.84 | ⚪ **CASH** | **-3.56%** | `MACRO_BEAR` | `81%` | `+22.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.49 | ⚪ **CASH** | **-2.92%** | `MACRO_BEAR` | `83%` | `+22.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 21:30:53 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,990.97 | ⚪ **CASH** | **-3.49%** | `MACRO_BEAR` | `72%` | `+2.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,725.64 | ⚪ **CASH** | **-3.55%** | `MACRO_BEAR` | `81%` | `+22.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.39 | ⚪ **CASH** | **-2.92%** | `MACRO_BEAR` | `83%` | `+22.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 21:15:37 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,988.01 | ⚪ **CASH** | **-3.49%** | `MACRO_BEAR` | `72%` | `+2.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,724.57 | ⚪ **CASH** | **-3.56%** | `MACRO_BEAR` | `81%` | `+22.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.29 | ⚪ **CASH** | **-2.92%** | `MACRO_BEAR` | `83%` | `+22.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 21:00:59 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,918.00 | ⚪ **CASH** | **-3.50%** | `MACRO_BEAR` | `72%` | `+2.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,720.38 | ⚪ **CASH** | **-3.56%** | `MACRO_BEAR` | `81%` | `+22.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.16 | ⚪ **CASH** | **-2.93%** | `MACRO_BEAR` | `83%` | `+22.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 20:45:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,631.99 | ⚪ **CASH** | **-3.58%** | `MACRO_BEAR` | `72%` | `+9.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,715.53 | ⚪ **CASH** | **-3.66%** | `MACRO_BEAR` | `81%` | `+26.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.06 | ⚪ **CASH** | **-2.97%** | `MACRO_BEAR` | `83%` | `+18.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 20:30:39 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,631.47 | ⚪ **CASH** | **-3.58%** | `MACRO_BEAR` | `72%` | `+9.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,713.14 | ⚪ **CASH** | **-3.66%** | `MACRO_BEAR` | `81%` | `+26.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $69.99 | ⚪ **CASH** | **-2.97%** | `MACRO_BEAR` | `83%` | `+18.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 20:15:41 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,707.96 | ⚪ **CASH** | **-3.58%** | `MACRO_BEAR` | `72%` | `+9.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,713.73 | ⚪ **CASH** | **-3.66%** | `MACRO_BEAR` | `81%` | `+26.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.04 | ⚪ **CASH** | **-2.97%** | `MACRO_BEAR` | `83%` | `+18.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 20:00:58 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,740.78 | ⚪ **CASH** | **-3.57%** | `MACRO_BEAR` | `72%` | `+9.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,715.39 | ⚪ **CASH** | **-3.66%** | `MACRO_BEAR` | `81%` | `+26.3 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.33 | ⚪ **CASH** | **-2.96%** | `MACRO_BEAR` | `83%` | `+18.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 19:45:42 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,745.35 | ⚪ **CASH** | **-3.64%** | `MACRO_BEAR` | `72%` | `+8.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,715.84 | ⚪ **CASH** | **-3.74%** | `MACRO_BEAR` | `81%` | `+22.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.31 | ⚪ **CASH** | **-3.00%** | `MACRO_BEAR` | `83%` | `+23.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 19:30:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,776.31 | ⚪ **CASH** | **-3.64%** | `MACRO_BEAR` | `72%` | `+8.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,715.81 | ⚪ **CASH** | **-3.74%** | `MACRO_BEAR` | `81%` | `+22.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.33 | ⚪ **CASH** | **-3.00%** | `MACRO_BEAR` | `83%` | `+23.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 19:15:50 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,754.41 | ⚪ **CASH** | **-3.64%** | `MACRO_BEAR` | `72%` | `+8.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,715.62 | ⚪ **CASH** | **-3.74%** | `MACRO_BEAR` | `81%` | `+22.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.45 | ⚪ **CASH** | **-2.99%** | `MACRO_BEAR` | `83%` | `+23.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 19:00:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,779.99 | ⚪ **CASH** | **-3.64%** | `MACRO_BEAR` | `72%` | `+8.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,715.09 | ⚪ **CASH** | **-3.74%** | `MACRO_BEAR` | `81%` | `+22.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.43 | ⚪ **CASH** | **-2.99%** | `MACRO_BEAR` | `83%` | `+23.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 18:45:46 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,716.17 | ⚪ **CASH** | **-3.71%** | `MACRO_BEAR` | `72%` | `+6.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,714.65 | ⚪ **CASH** | **-3.83%** | `MACRO_BEAR` | `82%` | `+23.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.36 | ⚪ **CASH** | **-3.04%** | `MACRO_BEAR` | `83%` | `+33.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 18:30:52 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,696.06 | ⚪ **CASH** | **-3.71%** | `MACRO_BEAR` | `72%` | `+6.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,714.34 | ⚪ **CASH** | **-3.83%** | `MACRO_BEAR` | `82%` | `+23.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.32 | ⚪ **CASH** | **-3.04%** | `MACRO_BEAR` | `83%` | `+33.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 18:15:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,812.00 | ⚪ **CASH** | **-3.70%** | `MACRO_BEAR` | `72%` | `+6.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,716.93 | ⚪ **CASH** | **-3.82%** | `MACRO_BEAR` | `82%` | `+23.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.49 | ⚪ **CASH** | **-3.03%** | `MACRO_BEAR` | `83%` | `+33.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 18:00:55 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,824.20 | ⚪ **CASH** | **-3.70%** | `MACRO_BEAR` | `72%` | `+6.5 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,714.23 | ⚪ **CASH** | **-3.83%** | `MACRO_BEAR` | `82%` | `+23.1 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.35 | ⚪ **CASH** | **-3.04%** | `MACRO_BEAR` | `83%` | `+33.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 17:45:43 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,925.50 | ⚪ **CASH** | **-3.77%** | `MACRO_BEAR` | `72%` | `-3.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,716.38 | ⚪ **CASH** | **-3.91%** | `MACRO_BEAR` | `81%` | `+10.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.47 | ⚪ **CASH** | **-3.08%** | `MACRO_BEAR` | `83%` | `+3.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 17:30:41 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,874.58 | ⚪ **CASH** | **-3.77%** | `MACRO_BEAR` | `72%` | `-3.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,715.88 | ⚪ **CASH** | **-3.91%** | `MACRO_BEAR` | `81%` | `+10.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.45 | ⚪ **CASH** | **-3.08%** | `MACRO_BEAR` | `83%` | `+3.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 17:15:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,823.79 | ⚪ **CASH** | **-3.77%** | `MACRO_BEAR` | `72%` | `-3.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,714.35 | ⚪ **CASH** | **-3.91%** | `MACRO_BEAR` | `82%` | `+10.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.40 | ⚪ **CASH** | **-3.08%** | `MACRO_BEAR` | `83%` | `+3.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 17:00:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,221.07 | ⚪ **CASH** | **-3.75%** | `MACRO_BEAR` | `72%` | `-3.6 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,722.79 | ⚪ **CASH** | **-3.90%** | `MACRO_BEAR` | `81%` | `+10.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.62 | ⚪ **CASH** | **-3.07%** | `MACRO_BEAR` | `83%` | `+3.7 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 16:45:43 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,317.32 | ⚪ **CASH** | **-3.84%** | `MACRO_BEAR` | `72%` | `-3.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,723.57 | ⚪ **CASH** | **-4.00%** | `MACRO_BEAR` | `81%` | `+5.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.70 | ⚪ **CASH** | **-3.13%** | `MACRO_BEAR` | `83%` | `+3.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 16:30:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,258.14 | ⚪ **CASH** | **-3.84%** | `MACRO_BEAR` | `72%` | `-3.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,722.36 | ⚪ **CASH** | **-4.00%** | `MACRO_BEAR` | `81%` | `+5.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.58 | ⚪ **CASH** | **-3.13%** | `MACRO_BEAR` | `83%` | `+3.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 16:15:48 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $61,051.06 | ⚪ **CASH** | **-3.85%** | `MACRO_BEAR` | `72%` | `-3.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,718.38 | ⚪ **CASH** | **-4.01%** | `MACRO_BEAR` | `81%` | `+5.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.36 | ⚪ **CASH** | **-3.14%** | `MACRO_BEAR` | `83%` | `+3.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 16:00:55 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,912.19 | ⚪ **CASH** | **-3.86%** | `MACRO_BEAR` | `72%` | `-3.2 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,718.98 | ⚪ **CASH** | **-4.01%** | `MACRO_BEAR` | `81%` | `+5.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.34 | ⚪ **CASH** | **-3.14%** | `MACRO_BEAR` | `83%` | `+3.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 15:45:44 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,799.99 | ⚪ **CASH** | **-3.95%** | `MACRO_BEAR` | `72%` | `-5.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,718.65 | ⚪ **CASH** | **-4.11%** | `MACRO_BEAR` | `81%` | `+11.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.43 | ⚪ **CASH** | **-3.18%** | `MACRO_BEAR` | `83%` | `+4.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 15:30:51 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,900.85 | ⚪ **CASH** | **-3.94%** | `MACRO_BEAR` | `72%` | `-5.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,717.87 | ⚪ **CASH** | **-4.11%** | `MACRO_BEAR` | `81%` | `+11.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.32 | ⚪ **CASH** | **-3.19%** | `MACRO_BEAR` | `83%` | `+4.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 15:15:49 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,917.70 | ⚪ **CASH** | **-3.94%** | `MACRO_BEAR` | `72%` | `-5.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,714.01 | ⚪ **CASH** | **-4.11%** | `MACRO_BEAR` | `81%` | `+11.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.28 | ⚪ **CASH** | **-3.19%** | `MACRO_BEAR` | `83%` | `+4.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |

---

### 🕒 Ciclo `2026-11-22 15:00:56 UTC` | Patrimônio: **$974.54 USDT** (Caixa: `$974.54`)

| Ativo | Preço | Sinal | Spread EMA48/168 | Regime Macro | Vol Anual | ML 12h | Racional Quantitativo |
|:---|---:|:---:|---:|:---:|---:|---:|:---|
| **BTCUSDT** | $60,909.36 | ⚪ **CASH** | **-3.94%** | `MACRO_BEAR` | `72%` | `-5.9 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **ETHUSDT** | $1,711.92 | ⚪ **CASH** | **-4.12%** | `MACRO_BEAR` | `81%` | `+11.0 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
| **SOLUSDT** | $70.30 | ⚪ **CASH** | **-3.19%** | `MACRO_BEAR` | `83%` | `+4.4 bps` | Bloqueio anti-whipsaw pós-Stop (SHORT); aguardando reset de tendência |
