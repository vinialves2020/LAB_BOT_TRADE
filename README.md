# 🤖 BOT_TRADE — Laboratório Quantitativo Institucional V5.1

<p align="center">
  <img src="https://img.shields.io/badge/Status-🟢%20Paper%20Trading%2024%2F7-brightgreen?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/Modelo-XGBoost%20Ensemble%20(ONNX)-blue?style=for-the-badge" alt="Model" />
  <img src="https://img.shields.io/badge/Portfólio%20Sharpe-7.22-purple?style=for-the-badge" alt="Sharpe" />
  <img src="https://img.shields.io/badge/Retorno%20Líquido-+12.77%25-success?style=for-the-badge" alt="Return" />
  <img src="https://img.shields.io/badge/Overfitting%20PBO-0.0%25-darkgreen?style=for-the-badge" alt="PBO" />
  <img src="https://img.shields.io/badge/Execução-GitHub%20Actions%20Hourly-black?style=for-the-badge" alt="GitHub Actions" />
</p>

<p align="center">
  <b>Laboratório reproduzível de Machine Learning institucional e bot de Paper Trading autônomo 24/7 para <code>BTCUSDT</code>, <code>ETHUSDT</code> e <code>SOLUSDT</code>.</b>
</p>

<p align="center">
  <a href="#-painel-ao-vivo-paper-trading-247"><b>🟢 Live Dashboard</b></a> •
  <a href="#-cerne-do-projeto--estratégias"><b>🧠 Cerne & Estratégias</b></a> •
  <a href="#-como-testar-você-mesmo"><b>🧪 Como Testar</b></a> •
  <a href="#-auditoria-quantitativa-e-resultados"><b>📊 Auditoria & Resultados</b></a> •
  <a href="#-ferramentas--stack-tecnológico"><b>🛠️ Ferramentas & Stack</b></a>
</p>

---

## 🟢 Painel Ao Vivo (Paper Trading 24/7)

O robô está em execução autônoma contínua na nuvem via **GitHub Actions**, conectando-se diretamente à API da Binance no fechamento de cada vela horária (1h) e enviando telemetria em tempo real para o **Telegram**.

> 🔗 **Ver Painel Completo em Tempo Real**: [**`reports/LIVE_DASHBOARD.md`**](reports/LIVE_DASHBOARD.md) *(atualizado automaticamente a cada 60 minutos pelo robô)*

```
=================================================================
  [BOT] BOTTRADE V5 - PAPER TRADING ENGINE (ONLINE)
  Status: 🟢 ONLINE | Ledger: paper_1000 | Frequência: Horária (1h)
=================================================================
  Patrimônio Líquido Total: $1,000.00 USDT (+0.00%)
  Caixa Disponível:        $1,000.00 USDT
  Capital em Posições:     $0.00 USDT
-----------------------------------------------------------------
  SINAIS & MODELOS EM TEMPO REAL (XGBoost Institucional):
  [CAIXA]  BTCUSDT | Preço: $ 77,103.98 | Sinal: CASH | Pred:  +0.4 bps (Gate: 24.0)
  [CAIXA]  ETHUSDT | Preço: $  2,383.60 | Sinal: CASH | Pred:  +0.1 bps (Gate: 24.0)
  [CAIXA]  SOLUSDT | Preço: $     99.71 | Sinal: CASH | Pred:  -1.8 bps (Gate: 24.0)
-----------------------------------------------------------------
  POSIÇÕES ATIVAS: (Capital 100% preservado em caixa; aguardando assimetria favorável)
=================================================================
```

---

## 🧠 Cerne do Projeto & Estratégias

O projeto nasceu para investigar o limite empírico entre **Transformers Neurais**, **Random Forests** e **Gradient Boosting (XGBoost)** aplicados à previsão de retornos em criptoativos, incorporando regras quantitativas usadas por fundos de investimento.

> 📖 **Documentação Aprofundada**: [**`docs/ESTRATEGIAS_E_MODELOS.md`**](docs/ESTRATEGIAS_E_MODELOS.md)

### 1. O Confronto das Arquiteturas
- **Random Forest**: Alta estabilidade ($IC > 0{,}04$), mas a média simples de árvores (*bagging*) retrai as previsões para o centro (*mean shrinkage*), raramente superando a barreira de taxas de 24 bps.
- **PatchTransformer (PatchTST na GPU via CUDA 12.8)**: Aprende dinâmicas temporais complexas, mas o erro quadrático induz previsões moderadas demais para acionar operações em spot sem alavancagem.
- **XGBoost Institucional (O Campeão)**: O ajuste de resíduos (*boosting*) preserva as caudas da distribuição, disparando entradas cirúrgicas apenas quando a probabilidade condicional de lucro supera os custos com folga.

### 2. Microestrutura e Sinais Institucionais
- **Cumulative Volume Delta (CVD)**: Acúmulo de agressão compradora vs. vendedora (`cvd_ratio_3h`, `6h`, `24h`) e detecção de **divergências** (ex: absorção passiva institucional em fundos de pânico).
- **Features Cíclicas de Sessão**: Identificação da sobreposição de liquidez Londres/Nova York (12h às 20h UTC) e filtros para baixa liquidez de fins de semana.
- **Trailing Stop & Stop Loss Adaptativos**: Parametrizados pela volatilidade horária EWMA ($\sigma_{1h}$): lucros são travados dinamicamente ($+2\sigma$ ativa trailing) e quedas anormais são cortadas antes de virarem prejuízos graves.

### 3. Travas Macro de Regime
- **Filtro de Queda Macro do Bitcoin (`btc_dumping`)**: Se o BTC cair mais de $1{,}8\%$ em 24h, novas compras em altcoins (ETH e SOL) são bloqueadas, eliminando o risco de "pegar faca caindo".
- **Filtro Direcional da Solana (`sol_sideways_filter`)**: A Solana é um ativo de alto *momentum*. Quando oscila lateralmente dentro de $\pm 2{,}5\%$ da EMA de 72h, novas entradas são vetadas, blindando o capital contra pavios falsos.

---

## 🧪 Como Testar Você Mesmo

Você pode reproduzir facilmente os resultados ou rodar o bot na sua própria máquina.

> 🚀 **Guia Passo a Passo Completo**: [**`docs/COMO_TESTAR.md`**](docs/COMO_TESTAR.md)

### Instalação Rápida (1 Minuto):
```bash
git clone https://github.com/vinialves2020/LAB_BOT_TRADE.git
cd LAB_BOT_TRADE
python -m venv .venv
# Ativar no Windows: .venv\Scripts\Activate.ps1 | No Linux: source .venv/bin/activate
pip install -e ".[ml]"
```

### Comandos Principais:

```bash
# 1. Executar um ciclo de Paper Trading ao vivo (baixa candles da Binance e roda os modelos)
bottrade v5 paper-run --live

# 2. Executar o bot em loop contínuo 24/7 (ex: checando a cada 60 segundos)
bottrade v5 paper-run --live --loop --interval-seconds 60

# 3. Executar o teste de estresse de 6 meses em todos os ativos
bottrade v5 stress-test --asset all --folds 6 --models xgboost

# 4. Executar os testes unitários da suíte V5
pytest -q tests/v5
```

---

## 📊 Auditoria Quantitativa e Resultados

O modelo passou por uma rigorosa auditoria em **6 meses contínuos de walk-forward** (com purge e embargo de dados), cobrindo cenários de alta, consolidação e quedas de pânico:

### Desempenho Auditado por Ativo (Custo Base Taker: 24 bps)

| Ativo | Trades | Frequência | Retorno Líquido | Retorno sob Estresse (48 bps) | Índice Sharpe | Max Drawdown | PBO (Overfitting) |
|---|---:|---:|---:|---:|---:|---:|:---:|
| **SOLUSDT** | 5 | 1.67/mês | **+11.97%** | **+10.66%** | **11.23** | **2.95%** | **0.0%** |
| **BTCUSDT** | 14 | 7.00/mês | **+12.80%** | **+9.10%** | **5.50** | **5.61%** | **0.0%** |
| **ETHUSDT** | 23 | 5.75/mês | **+13.55%** | **+7.47%** | **4.94** | **9.41%** | **0.0%** |
| **PORTFÓLIO CONSOLIDADO** | **42** | **8.40/mês** | **+12.77%** | **+9.08%** | **7.22** | **9.41%** | **0.0%** |

### Curva de Degradação de Custos (Resiliência a Slippage Severo)

| Ativo | Maker VIP (12 bps) | Taker Base (24 bps) | Estresse Dobrado (48 bps) | Choque Extremo (72 bps) | Resiliência Operacional |
|---|---:|---:|---:|---:|:---:|
| **SOLUSDT** | **+12.63%** | **+11.97%** | **+10.66%** | **+9.37%** | 🏆 **LUCRA ATÉ A 72 BPS** |
| **BTCUSDT** | **+14.69%** | **+12.80%** | **+9.10%** | **+5.51%** | 🏆 **LUCRA ATÉ A 72 BPS** |
| **ETHUSDT** | **+16.71%** | **+13.55%** | **+7.47%** | **+1.71%** | 🏆 **LUCRA ATÉ A 72 BPS** |

> 🛡️ **Zero Overfitting**: A Probabilidade de Ajuste à Curva (**PBO via CSCV**) foi de **0.0%**, com resiliência positiva comprovada mesmo com taxas triplicadas a 72 bps.

---

## 🛠️ Ferramentas & Stack Tecnológico

| Camada | Ferramentas Utilizadas |
|---|---|
| **Linguagem & Core** | Python 3.12, Typer CLI, Pydantic, Pandas, NumPy |
| **Machine Learning** | XGBoost, LightGBM, Scikit-Learn, PyTorch (CUDA 12.8), ONNX Runtime |
| **Microestrutura & Dados** | Binance Public REST API (Klines/CVD), Order Flow Analytics |
| **Armazenamento & Ledgers** | SQLite (`bottrade.db`), SQLAlchemy ORM, Neon PostgreSQL |
| **Automação & Cloud 24/7** | GitHub Actions (Cron Horário), Telegram Bot API, Docker, Terraform |
| **Qualidade & Auditoria** | Pytest, Ruff Linter, DSR (Deflated Sharpe), PBO (Combinatorial Cross-Validation) |

---

## 📁 Estrutura de Documentação do Projeto

- 📘 [**`docs/ESTRATEGIAS_E_MODELOS.md`**](docs/ESTRATEGIAS_E_MODELOS.md): Fundamentos quantitativos, CVD, saídas adaptativas e matemática dos regimes.
- 🧪 [**`docs/COMO_TESTAR.md`**](docs/COMO_TESTAR.md): Instruções passo a passo para executar localmente.
- ☁️ [**`docs/DEPLOY_24_7.md`**](docs/DEPLOY_24_7.md): Guia de deploy em nuvem gratuita (GitHub Actions, DigitalOcean Student Pack, Google Cloud).
- 📈 [**`reports/LIVE_DASHBOARD.md`**](reports/LIVE_DASHBOARD.md): Painel ao vivo de operações de Paper Trading.

---

<p align="center">
  <sub>Desenvolvido para fins de pesquisa quantitativa e simulação em ambiente institucional reproduzível.</sub>
</p>
