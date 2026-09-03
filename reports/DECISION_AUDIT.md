# 📋 BOT_TRADE V5 — Livro de Auditoria de Decisões e Análise de Mercado

Este documento registra o histórico contínuo das decisões tomadas pelo algoritmo a cada ciclo em tempo real na Binance.
Ele permite auditar o consenso dos 5 modelos XGBoost, o comportamento do CVD (Cumulative Volume Delta) e o disparo de travas de risco.

**Última Atualização**: `2026-09-03 14:45:47 UTC` | **Ledger**: `paper_1000`

<!-- AUDIT_START -->
### 🕒 Ciclo `2026-09-03 14:45:47 UTC` | Patrimônio: **$1,000.00 USDT** (Caixa: `$1,000.00`)

| Ativo | Preço | Sinal | Previsão Líquida | Consenso 5x XGBoost | Order Flow (CVD 6h) | Volatilidade | Filtros de Risco | Racional Quantitativo |
|:---|---:|:---:|---:|:---|:---:|:---:|:---|:---|
| **BTCUSDT** | $79,820.00 | ⚪ **CASH** | **+0.4 bps** (±0.3) | `[+0.4, +0.4, +0.6, +0.2, +1.0]` | `+0.076` | `0.33%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **ETHUSDT** | $2,458.11 | ⚪ **CASH** | **-0.2 bps** (±0.2) | `[+0.2, +0.1, -0.1, -0.1, -0.5]` | `+0.244` | `0.40%/h` | Liberado ✅ | Aguardando sinal com assimetria |
| **SOLUSDT** | $102.82 | ⚪ **CASH** | **-0.0 bps** (±0.4) | `[+0.2, -0.4, -0.1, +0.7, +0.4]` | `+0.144` | `0.53%/h` | `sol_sideways` | Aguardando sinal com assimetria |
