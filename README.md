# BOT_TRADE — RF × Transformer × Gradient Boosting

Laboratório reproduzível e bot de paper trading spot `long/flat` para `BTCUSDT`, `ETHUSDT` e `SOLUSDT`. O repositório implementa o protocolo experimental, o registro imutável de modelos e o caminho operacional 24/7. A primeira leva de treinamento foi encerrada como resultado negativo/inconclusivo e está documentada em [docs/RESULTS_FIRST_RUN.md](docs/RESULTS_FIRST_RUN.md); nenhum holdout, canário ou capital real foi ativado.

> Segurança: não existe adaptador de ordens reais neste projeto. Aprovação nos gates apenas torna um ativo candidato a uma revisão futura e separada.

## Escopo implementado

- Candles públicos Binance 1h, Coin Metrics para BTC/ETH, DefiLlama para Solana e Fear & Greed geral.
- V2 adiciona candles 15m, segmentos gap-aware, labels cost-aware em 3h/6h/12h,
  HistGradientBoosting challenger e braços composíveis com derivativos históricos.
- `event_time`, `available_at`, atraso conservador de 24h, idade, ausência, staleness de 72h e fallback pré-selecionado `market`.
- V1 preserva quatro braços (`market`, `market_onchain`, `market_sentiment`,
  `market_all`); V2 usa `DataArmSpec` para compor core 1h/15m, derivativos,
  on-chain e sentimento.
- Label de retorno do próximo `open` até o fechamento três horas adiante, normalizado pela EWMA truncada às 168 horas estritamente anteriores.
- Random Forest, Transformer temporal com embeddings de calendário e controles cash, buy-and-hold com risco equivalente, médias móveis e Ridge.
- V2 congela cinco seeds, ensemble tabular ONNX, calibração de probabilidade,
  seleção de horizonte e diagnósticos DSR/PBO.
- O resultado negativo/inconclusivo da V2 está congelado em
  [docs/RESULTS_V2.md](docs/RESULTS_V2.md); a V3 será implementada em módulos
  aditivos, sem abrir o holdout.
- A V3 adiciona estratégias determinísticas com meta-modelos RF/HGB/Transformer,
  labels event-driven, persistência com hashes e a CLI `bottrade v3`; o estado
  executado fica em [docs/V3_PROGRESS.md](docs/V3_PROGRESS.md) e os gates em
  [docs/ACCEPTANCE_V3.md](docs/ACCEPTANCE_V3.md).
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

No Windows com GPU NVIDIA, o índice padrão pode instalar uma build CPU-only do
PyTorch. Confirme com `python -c "import torch; print(torch.cuda.is_available())"`.
Para a RTX 2060 usada neste estudo, preserve a versão e troque a wheel pela build
CUDA 12.8 oficial antes de treinar Transformers:

    python -m pip install --no-deps --force-reinstall torch==2.11.0+cu128 --index-url https://download.pytorch.org/whl/cu128

Antes de modelos promovidos, `doctor` pode retornar `model_not_ready`; essa falha segura é esperada.

Antes da primeira execução oficial, inicialize o controle de versão e faça um commit do protocolo/configuração. Cada experimento captura `HEAD` e o estado dirty; sem repositório ele registra `commit=unavailable` e não deve ser aceito como execução acadêmica final.

## Fluxo experimental oficial

Para a implementação V3, o caminho seguro começa pelo preflight e mantém o
holdout fechado por padrão:

    bottrade v3 preflight --config config/v3.yaml
    bottrade v3 features --asset BTCUSDT --output data/processed/v3/BTCUSDT/features.parquet
    bottrade v3 candidates --asset BTCUSDT --features data/processed/v3/BTCUSDT/features.parquet --output data/processed/v3/BTCUSDT/candidates.parquet
    bottrade v3 labels --candidates data/processed/v3/BTCUSDT/candidates.parquet --intrahour data/raw/market/BTCUSDT_15m.parquet --output data/processed/v3/BTCUSDT/labels.parquet
    bottrade v3 deterministic --labels data/processed/v3/BTCUSDT/labels.parquet --output-dir reports/generated/v3/BTCUSDT/deterministic

Os comandos `meta-train`, `portfolio`, `select`, `report` e `holdout` estão
descritos em [docs/ACCEPTANCE_V3.md](docs/ACCEPTANCE_V3.md). `--params-json`
marca um smoke-test; resultados assim não podem ser promovidos.

O fluxo V1 abaixo continua apenas para reprodução histórica. Toda nova rodada
deve apontar explicitamente para `config/v2.yaml`; o holdout permanece fixo e
intocável durante treino e ablações. A sequência detalhada está em
[docs/PROTOCOL_V2.md](docs/PROTOCOL_V2.md).

1. Coletar e construir os braços V2 (1h + 15m e, quando houver arquivo oficial,
   derivativos). O corte de desenvolvimento continua anterior a `2025-08-01`;
   o comando de treino nunca avalia o holdout.

       bottrade data sync --config config/v2.yaml --start 2017-08-17 --end 2026-07-31T23:59:59Z
       bottrade dataset build --config config/v2.yaml

2. Para cada ativo, executar no máximo 20 trials no core V2 de cada família.
   Depois de congelar o core em `training.frozen_core_arm`, as ablações carregam
   os mesmos hiperparâmetros e usam as cinco seeds configuradas.

       bottrade train --config config/v2.yaml --asset BTCUSDT --family random_forest --arm market_1h_15m --trials 20
       bottrade train --config config/v2.yaml --asset BTCUSDT --family hist_gradient_boosting --arm market_1h_15m --trials 20
       bottrade train --config config/v2.yaml --asset BTCUSDT --family transformer --arm market_1h_15m --trials 20
       bottrade train --config config/v2.yaml --asset BTCUSDT --family random_forest --arm market_1h_15m_derivatives

3. Somente quando a matriz V2 completa de famílias × braços existir, congelar
   campeão, fallback e challenger. O arquivo de seleção é imutável e guarda
   checksums.

       bottrade models select --config config/v2.yaml --asset BTCUSDT

4. Abrir o holdout uma única vez para cada `run_id` distinto indicado pela seleção. Se duas funções apontarem para o mesmo candidato, uma única avaliação satisfaz ambas. `--resume` só recupera a mesma execução após falha operacional.

       bottrade holdout --config config/v2.yaml --asset BTCUSDT --role champion
       bottrade holdout --config config/v2.yaml --asset BTCUSDT --role market_fallback
       bottrade holdout --config config/v2.yaml --asset BTCUSDT --role challenger

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
- [Protocolo V2](docs/PROTOCOL_V2.md)
- [Fontes e dicionário de dados](docs/DATA.md)
- [Operação, canário e recuperação](docs/OPERATIONS.md)
- [Segurança e limites](docs/SECURITY.md)
- [Deploy em Cloud Run](docs/CLOUD.md)
- [Critérios de aceite](docs/ACCEPTANCE.md)
- [Resultados da primeira leva e plano v2](docs/RESULTS_FIRST_RUN.md)
- [Protocolo V3](docs/PROTOCOL_V3.md)
- [Critérios de aceite V3](docs/ACCEPTANCE_V3.md)
- [Estado de implementação V3](docs/V3_PROGRESS.md)

## Limitações explícitas

- Métricas de Solana descrevem atividade do ecossistema e não são equivalentes às métricas de BTC/ETH.
- Fear & Greed é geral, centrado em Bitcoin e parcialmente derivado do mercado.
- Fills paper não reproduzem prioridade de fila, latência ou impacto real integral.
- Free tiers não têm SLA; orçamento é alerta, não hard cap, e custo zero não é garantido.
- Nenhuma conclusão de promoção ou uso real é válida antes de holdout e paper; resultados preliminares negativos/inconclusivos ficam documentados separadamente.
