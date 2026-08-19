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

## Decisão

BTC, ETH e SOL permanecem em caixa. O próximo experimento deve completar as
ablações e as cinco seeds finais; qualquer resultado precisa passar os gates de
frequência, custo dobrado, risco, DSR/PBO e estabilidade antes da criação do
selection lock. Nenhum número desta página autoriza holdout, canário, paper
oficial ou capital real.
