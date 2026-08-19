# Protocolo V2 — RF × Transformer × Gradient Boosting

Este documento congela a segunda rodada antes de qualquer novo resultado. A
V1 permanece preservada como resultado negativo/inconclusivo em
`docs/RESULTS_FIRST_RUN.md`.

## Objetivo

Estudar, dentro de cada ativo e braço de dados, Random Forest, HistGradientBoosting
e um Transformer temporal compacto em patches para um bot spot `long/flat` de
BTCUSDT, ETHUSDT e SOLUSDT. Não há short, alavancagem ou função de envio de
ordens reais. O ativo que não passar os gates permanece em caixa.

As decisões seguem horárias. Os candles de 15 minutos são somente contexto
agregado: quatro barras já encerradas produzem retorno, caminho intrahorário,
volatilidade, range, drawup/drawdown, concentração de volume, negócios,
agressão compradora e completude. Nenhuma barra posterior a `as_of` é usada.

## Correções em relação à V1

- Folds mensais gap-aware, com segmentos de continuidade e purge/embargo de
  12 horas. Menos de 12 folds pré-holdout classifica a rodada como piloto;
  piloto não pode abrir o holdout.
- Alvos de 3h, 6h e 12h: regressão do retorno normalizado e classificação de
  retorno bruto acima de 24 bps. A probabilidade é calibrada com previsões
  cronológicas fora da amostra.
- A política testa somente a grade pré-registrada de probabilidades
  `{0,50; 0,55; 0,60}` e margens `{0, 5, 10, 20, 30}` bps. O horizonte elegível
  com maior retorno líquido previsto vence; empate usa o menor horizonte.
- Random Forest e HistGradientBoosting têm cabeças por horizonte; o Transformer
  usa encoder em patches e cabeças simultâneas de regressão/classificação na
  arquitetura `TemporalTransformer`.
- Cinco seeds finais (`11, 23, 37, 53, 71`) são avaliadas. Para modelos
  tabulares V2 o `model.onnx` é um `VotingRegressor` que calcula a média das
  cinco seeds; cada artefato ONNX é verificado antes do registro.
- A seleção exige frequência sem forçar entradas: média de pelo menos 20
  trades/mês, piso de 10 em cada mês completo e no mínimo 60 trades na
  calibração, além do limite de duas entradas/saídas completas por dia.
- DSR e PBO são registrados para penalizar múltiplas tentativas. A escolha é
  feita por Sortino mediano com custo dobrado, depois drawdown e latência ONNX.

## Dados e braços

O arquivo de entrada é `config/v2.yaml`. O intervalo principal é `1h` e o
`data sync` também solicita `15m`. Candles Binance são aceitos em
milissegundos ou microssegundos e cada arquivo é guardado com URL, checksum,
schema e data de coleta no manifesto.

Os braços V2 são composíveis por `DataArmSpec`:

| Braço | Componentes |
| --- | --- |
| `market` | mercado 1h |
| `market_1h_15m` | mercado 1h + contexto 15m |
| `market_1h_15m_derivatives` | core + derivativos históricos read-only |
| sufixo `_onchain` | core + métrica on-chain/ecossistema com atraso de 24h |
| sufixo `_sentiment` | core + Fear & Greed geral com atraso de 24h |
| sufixo `_all` | core + on-chain + sentimento |

Ausência, idade e frescor são features explícitas. Dados alternativos com mais
de 72h acionam o fallback market-only. Gap de mercado não é interpolado e
impede novas posições.

## Ordem de execução

```text
bottrade data sync --config config/v2.yaml
bottrade dataset build --config config/v2.yaml
bottrade train --config config/v2.yaml --asset BTCUSDT --family random_forest --arm market
bottrade train --config config/v2.yaml --asset BTCUSDT --family hist_gradient_boosting --arm market
bottrade train --config config/v2.yaml --asset BTCUSDT --family transformer --arm market
```

O mesmo conjunto de comandos é repetido por ativo. Primeiro congela-se o
melhor core de mercado; depois executam-se as ablações, sem reabrir busca de
hiperparâmetros. `bottrade models select` cria o lock pré-holdout. O holdout
`2025-08-01` a `2026-07-31` só pode ser aberto uma vez por candidato congelado.

Após holdout aprovado: canário operacional de 14 dias, reset dos ledgers e
paper oficial de 183 dias. Qualquer falha de dado, modelo, banco, relógio ou
idempotência bloqueia novas posições. Nenhum gate autoriza capital real.

## Artefatos e auditoria

Cada experimento registra commit, seeds, parâmetros, folds, métricas normais e
com custo dobrado, regimes, latência, memória, explicabilidade, DSR/PBO e
model card. Para braços V2 tabulares, `multihorizon.json` aponta para os seis
artefatos (regressão/classificação de 3h, 6h e 12h); o Registry inclui todos os
checksums. O runtime escolhe o horizonte somente quando classificação e
regressão superam custo e margem.

## Critérios de aprovação

No holdout, cada ativo precisa de pelo menos 240 trades fechados, média de 20
e piso de 10 por mês, Sharpe diário anualizado ≥ 1,0, profit factor ≥ 1,2,
drawdown ≤ 8%, resultado positivo com 48 bps por round trip, superioridade aos
controles, estabilidade entre seeds e ausência de incidente crítico nos
últimos 90 dias. No paper de seis meses o mínimo é 120 trades por ativo. Falhar
qualquer condição mantém o ativo em caixa.

## Limites atuais

O conversor ONNX e os sidecars multi-horizonte são testados localmente; dados
de derivativos disponíveis somente por endpoint recente continuam em shadow e
não entram no treino retrospectivo. Os free tiers de nuvem não oferecem SLA.
O estudo é acadêmico e não constitui recomendação financeira.
