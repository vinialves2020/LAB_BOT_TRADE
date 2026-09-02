# 🧪 Como Testar Você Mesmo (Guia Rápido)

Este guia prático ensina como clonar o repositório, configurar o ambiente em 2 minutos e executar tanto os testes quantitativos quanto o **Paper Trading em tempo real**.

---

## 1. Pré-requisitos e Instalação

### Passo 1: Clonar o Repositório
```bash
git clone https://github.com/vinialves2020/LAB_BOT_TRADE.git
cd LAB_BOT_TRADE
```

### Passo 2: Criar Ambiente Virtual e Instalar Dependências
```bash
# No Windows (PowerShell):
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[ml]"

# No Linux / macOS:
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e ".[ml]"
```

---

## 2. Como Executar os Testes

### A. Executar um Ciclo de Paper Trading ao Vivo (Binance)
Conecta diretamente na API pública da Binance, baixa os candles da última hora, roda os modelos quantitativos institucionais e exibe a telemetria com PnL e sinais:
```bash
bottrade v5 paper-run --live
```

### B. Executar o Paper Trading em Monitoramento Contínuo 24/7
Deixa o bot rodando no terminal, atualizando a cada 60 segundos com candles e preços ao vivo:
```bash
bottrade v5 paper-run --live --loop --interval-seconds 60
```

### C. Executar a Bateria de Auditoria de Estresse e Anti-Overfitting
Roda o teste de estresse de 6 meses (walk-forward contínuo), decompondo por cenários de mercado (pânico, alta, lateralidade) e calculando a resiliência a taxas (até 72 bps de slippage):
```bash
# Auditar todos os ativos (BTC, ETH, SOL) em 6 folds:
bottrade v5 stress-test --asset all --folds 6 --models xgboost

# Auditar apenas o Bitcoin:
bottrade v5 stress-test --asset BTCUSDT --folds 6 --models xgboost
```

### D. Executar o Benchmark Comparativo (RF × Transformer × XGBoost)
Compara as três famílias de inteligência artificial nos mesmos dados e horizonte temporal:
```bash
bottrade v5 benchmark --asset BTCUSDT --folds 3 --models all
```

---

## 3. Testes Unitários e Validação do Código
Para garantir que todos os módulos matemáticos e de inferência estão íntegros:
```bash
pytest -q tests/v5
```
