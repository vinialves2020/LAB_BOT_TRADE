# BOT_TRADE — RF × Transformer

Laboratório reproduzível e bot de paper trading spot `long/flat` para `BTCUSDT`, `ETHUSDT` e `SOLUSDT`. O repositório implementa o protocolo experimental, o registro imutável de modelos e o caminho operacional 24/7; ainda não contém resultados acadêmicos, porque eles só podem existir depois dos experimentos e dos 183 dias oficiais.

> Segurança: não existe adaptador de ordens reais neste projeto. Aprovação nos gates apenas torna um ativo candidato a uma revisão futura e separada.

## Escopo implementado

- Candles públicos Binance 1h, Coin Metrics para BTC/ETH, DefiLlama para Solana e Fear & Greed geral.
- `event_time`, `available_at`, atraso conservador de 24h, idade, ausência, staleness de 72h e fallback pré-selecionado `market`.
- Quatro braços: `market`, `market_onchain`, `market_sentiment` e `market_all`.
- Label de retorno do próximo `open` até o fechamento três horas adiante, normalizado pela EWMA truncada às 168 horas estritamente anteriores.
- Random Forest, Transformer temporal com embeddings de calendário e controles cash, buy-and-hold com risco equivalente, médias móveis e Ridge.
- Walk-forward 24m/3m/1m, purge/embargo, cinco seeds independentes, custos-base/dobrados, análise por regime e explicabilidade.
- Trava de seleção anterior ao holdout, holdout inacessível pelo fluxo de desenvolvimento, linhagem de refit e verificação ONNX.
- Dois ledgers transacionais de 500/1.000 USDT, execução hipotética pelo livro, regras Binance, idempotência, reconciliação e circuit breakers.
- Jobs `signal`, `risk` e `daily`, challenger em shadow, dashboard, Telegram e Terraform para Cloud Run/Neon.

## Arquitetura

    fontes públicas -> manifests/checksums -> datasets point-in-time
                                                |
                                    RF / Transformer / controles
                                                |
                            walk-forward -> seleção imutável -> holdout
                                                |
                                  bundle ONNX + model card + lineage
                                                |
              sinal horário -> risco/targets -> fills paper atômicos
                                                |
                       Neon/Postgres -> dashboard privado + Telegram

O runtime aceita apenas bundles ONNX registrados. PyTorch, scikit-learn e explicadores ficam fora da imagem enxuta de produção.

## Instalação local

Python 3.11 a 3.13:

    python -m venv .venv
    .venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python -m pip install -e ".[ml,explain,dashboard,postgres,cloud,dev]"
    Copy-Item .env.example .env
    bottrade paper init
    bottrade doctor

Antes de modelos promovidos, `doctor` pode retornar `model_not_ready`; essa falha segura é esperada.

Antes da primeira execução oficial, inicialize o controle de versão e faça um commit do protocolo/configuração. Cada experimento captura `HEAD` e o estado dirty; sem repositório ele registra `commit=unavailable` e não deve ser aceito como execução acadêmica final.

## Fluxo experimental oficial

1. Coletar e construir os quatro braços. O corte de desenvolvimento continua anterior a `2025-08-01`; o comando de treino nunca avalia o holdout.

       bottrade data sync --start 2017-08-17 --end 2026-07-31T23:59:59Z
       bottrade dataset build

2. Para cada ativo, executar 30 trials no braço `market` de cada família. Em seguida, executar os outros três braços; eles carregam automaticamente os hiperparâmetros congelados de `market`. Toda execução oficial usa as cinco seeds configuradas.

       bottrade train --asset BTCUSDT --family random_forest --arm market --trials 30
       bottrade train --asset BTCUSDT --family transformer --arm market --trials 30
       bottrade train --asset BTCUSDT --family random_forest --arm market_onchain
       bottrade train --asset BTCUSDT --family random_forest --arm market_sentiment
       bottrade train --asset BTCUSDT --family random_forest --arm market_all
       bottrade train --asset BTCUSDT --family transformer --arm market_onchain
       bottrade train --asset BTCUSDT --family transformer --arm market_sentiment
       bottrade train --asset BTCUSDT --family transformer --arm market_all

3. Somente quando os oito candidatos elegíveis existirem, congelar campeão, fallback e challenger. O arquivo de seleção é imutável e guarda checksums.

       bottrade models select --asset BTCUSDT

4. Abrir o holdout uma única vez para cada `run_id` distinto indicado pela seleção. Se duas funções apontarem para o mesmo candidato, uma única avaliação satisfaz ambas. `--resume` só recupera a mesma execução após falha operacional.

       bottrade holdout --asset BTCUSDT --role champion
       bottrade holdout --asset BTCUSDT --role market_fallback
       bottrade holdout --asset BTCUSDT --role challenger

5. Repetir para ETH e SOL. Um candidato que falhar no holdout não pode ser promovido e o respectivo ativo/slot fica em caixa.

A lista de ativos realmente habilitados é gravada na fase do banco. Assim, um ativo reprovado fica em caixa sem impedir que os demais façam canário; a ausência posterior de um modelo que estava habilitado gera incidente crítico e target zero para ele.

`backtest` aceita parâmetros e folds reduzidos para diagnóstico, mas seus artefatos são marcados como não elegíveis para o protocolo.

## Canário e paper oficial

Promover as versões de holdout aprovadas. Se o challenger congelado também passar, ele é obrigatório no canário, mas roda somente em shadow; challenger reprovado é omitido.

    bottrade models promote --asset BTCUSDT --version VERSION --slot champion --stage canary
    bottrade models promote --asset BTCUSDT --version VERSION --slot market_fallback --stage canary
    bottrade models promote --asset BTCUSDT --version VERSION --slot challenger --stage canary
    bottrade models publish --asset BTCUSDT --slot champion --bucket PROJECT-bottrade-models
    bottrade paper canary-start

Os schedulers executam:

    bottrade paper run signal
    bottrade paper run risk
    bottrade paper run daily

Após no mínimo 14 dias sem incidente crítico:

    bottrade paper canary-complete
    bottrade paper reset-after-canary --confirmation RESET-PAPER-AFTER-CANARY --bucket PROJECT-bottrade-models

O reset preserva auditoria, zera os dois ledgers e inicia os 183 dias oficiais. O refit mensal conserva família, braço, hiperparâmetros e linhagem; `--activate` troca o ponteiro apenas após todas as validações.

    bottrade models refit --asset BTCUSDT --slot champion --activate
    bottrade paper reconcile
    bottrade paper official-complete
    bottrade paper evaluate
    bottrade report

## Validação e execução

    python -m ruff check src tests dashboard
    python -m pytest -q
    terraform -chdir=infra/terraform init -backend=false
    terraform -chdir=infra/terraform validate

Docker local:

    docker compose up --build postgres dashboard

O dashboard fica em `http://localhost:8501`. O compose não agenda jobs automaticamente para evitar mutações paper acidentais.

## Documentação

- [Protocolo pré-registrado](docs/PROTOCOL.md)
- [Fontes e dicionário de dados](docs/DATA.md)
- [Operação, canário e recuperação](docs/OPERATIONS.md)
- [Segurança e limites](docs/SECURITY.md)
- [Deploy em Cloud Run](docs/CLOUD.md)
- [Critérios de aceite](docs/ACCEPTANCE.md)

## Limitações explícitas

- Métricas de Solana descrevem atividade do ecossistema e não são equivalentes às métricas de BTC/ETH.
- Fear & Greed é geral, centrado em Bitcoin e parcialmente derivado do mercado.
- Fills paper não reproduzem prioridade de fila, latência ou impacto real integral.
- Free tiers não têm SLA; orçamento é alerta, não hard cap, e custo zero não é garantido.
- Nenhuma conclusão de desempenho é preenchida antes de dados reais de holdout e paper.
