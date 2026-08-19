# Resultados V3 — replay pré-holdout

Data de coleta: 2026-08-19. Todos os números abaixo usam somente amostras com
`as_of < 2025-08-01T00:00:00Z`. O holdout original não foi aberto.

## Signal ceiling determinístico

| Ativo | Custo | Trades | Retorno total | Sharpe HAC | PF | Drawdown |
|---|---:|---:|---:|---:|---:|---:|
| BTCUSDT | 1× | 4.746 | −99,9995% | −4,372 | 0,670 | 100,00% |
| BTCUSDT | 2× | 4.746 | −100,0000% | −8,831 | 0,453 | 100,00% |
| BTCUSDT | 3× | 4.746 | −100,0000% | −13,188 | 0,303 | 100,00% |
| ETHUSDT | 1× | 4.764 | −99,9981% | −2,818 | 0,765 | 100,00% |
| ETHUSDT | 2× | 4.764 | −100,0000% | −6,303 | 0,561 | 100,00% |
| ETHUSDT | 3× | 4.764 | −100,0000% | −9,974 | 0,411 | 100,00% |
| SOLUSDT | 1× | 2.907 | −98,9294% | −0,956 | 0,907 | 99,28% |
| SOLUSDT | 2× | 2.907 | −99,9990% | −3,057 | 0,736 | 100,00% |
| SOLUSDT | 3× | 2.907 | −100,0000% | −5,255 | 0,595 | 100,00% |

Este replay intentionally does not claim that a production policy would take
every candidate; it measures the raw deterministic ceiling before the
meta-model. The negative result means the candidate rules, as currently
specified, do not provide enough evidence on their own.

## Smoke-test audit

Um HGB com 40 iterações e uma seed foi executado apenas para validar o caminho
walk-forward e o salvamento nativo. Depois da remoção dos campos de resultado
que vazavam para as features, ele teve 1 trade fechado e retorno −1,18%. Não é
resultado de seleção, não é ensemble e não pode ser promovido.

## Treino oficial HGB — BTCUSDT

Em 2026-08-19 foi executado o primeiro treino pré-holdout completo da V3 para
BTCUSDT com `hist_gradient_boosting`, no braço `market_1h + intrahour_15m`.
O conjunto final teve 42.514 linhas e 93 features após o join ponto-no-tempo,
com 32 folds mensais gap-aware. Foram treinadas as cinco seeds obrigatórias
`11, 23, 37, 53, 71`; nenhuma seed selecionou uma operação:

| Seed | Folds | Trades fechados | Retorno líquido | Sharpe HAC | Drawdown |
|---:|---:|---:|---:|---:|---:|
| 11 | 32 | 0 | 0,00% | 0,00 | 0,00% |
| 23 | 32 | 0 | 0,00% | 0,00 | 0,00% |
| 37 | 32 | 0 | 0,00% | 0,00 | 0,00% |
| 53 | 32 | 0 | 0,00% | 0,00 | 0,00% |
| 71 | 32 | 0 | 0,00% | 0,00 | 0,00% |

O resultado é inconclusivo do ponto de vista econômico, mas operacionalmente
reprodutível. O gate de frequência falha (mínimo de 20 trades/mês, piso de 10
por mês e 60 na calibração); por isso não há candidato, campeão ou seleção
lock. O holdout permanece fechado.

Todos os cinco bundles nativos foram exportados para ONNX. A maior diferença
absoluta entre execução nativa e ONNX foi `1,9172e-7`, abaixo da tolerância
protocolar `1e-4`, em cada seed. Essa verificação garante portabilidade, não
qualidade preditiva.

## RF oficial — execução interrompida por custo

O RF foi iniciado no mesmo braço e com a configuração oficial. Após 30,25
minutos de parede (aproximadamente 5,31 horas de CPU acumulada), nenhuma seed
terminou e nenhum artefato de modelo foi escrito. O processo foi encerrado por
limite operacional de computação, com `metrics_valid: false`; isso não é uma
falha econômica nem um resultado de backtest. O registro da interrupção está em
`reports/generated/v3/BTCUSDT/rf_official/INTERRUPTED.json`. Para retomar, será
necessário escolher explicitamente entre uma janela computacional maior ou um
orçamento RF congelado e pré-registrado; não se deve aproveitar qualquer saída
parcial.

## Decisão

BTC, ETH e SOL permanecem em caixa. O HGB de BTC não é promovido e não autoriza
holdout, canário, paper oficial ou capital real. O próximo experimento deve
continuar pelas ablações pré-holdout (RF com orçamento computacional decidido e
Transformer em patches) e tratar a frequência nula como diagnóstico de
sinal/gate, sem relaxar os limites de risco ou forçar operações.
