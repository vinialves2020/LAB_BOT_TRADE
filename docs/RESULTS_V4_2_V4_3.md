# Resultados de refinamento V4.2/V4.3 (pré-holdout)

Data de execução: `2026-08-20`. Os testes abaixo usam somente o período
pré-holdout e não autorizam canário, holdout ou capital real.

## V4.2 — features estacionárias + tuning limitado

Busca: três folds iniciais, uma seed, oito candidatos fixos. O walk-forward
final usa 12 folds, cinco seeds. A busca de V4.2 compartilhou os três folds de
desenvolvimento com a avaliação final, portanto esta tabela é exploratória e
não é o resultado oficial de seleção.

| Ativo | Trades | Trades/mês | Retorno 24 bps | Retorno 48 bps | Sharpe | Drawdown | PF |
|---|---:|---:|---:|---:|---:|---:|---:|
| BTCUSDT | 50 | 6,25 | +23,69% | +6,37% | 3,85 | 7,55% | 1,58 |
| ETHUSDT | 117 | 10,64 | -15,25% | -9,80% | -0,47 | 41,44% | 0,94 |
| SOLUSDT | 68 | 6,18 | +3,82% | -2,26% | 0,80 | 25,11% | 1,10 |

BTC teve melhora de drawdown em relação à V4.1, mas ficou abaixo da frequência
de referência e não atingiu 10 trades em cada mês. ETH e SOL falharam nos gates;
SOL perdeu a robustez no custo dobrado.

## V4.3 — saída quando a previsão fica não positiva e permanência máxima de 6h

A busca de hiperparâmetros avalia somente previsões fora da amostra no período
de calibração. Os 12 testes mensais continuam separados da seleção.

| Ativo | Trades | Trades/mês | Retorno 24 bps | Retorno 48 bps | Sharpe | Drawdown | PF |
|---|---:|---:|---:|---:|---:|---:|---:|
| BTCUSDT | 48 | 6,86 | +17,05% | +3,61% | 5,58 | 4,20% | 1,68 |
| ETHUSDT | 116 | 10,55 | -40,36% | -12,45% | -4,39 | 43,72% | 0,51 |
| SOLUSDT | 72 | 6,00 | -7,30% | -21,11% | -0,36 | 27,48% | 0,95 |

A saída antecipada reduziu o drawdown do BTC, mas também reduziu retorno; para
ETH e SOL ela cristalizou perdas e não resolveu o problema de regime. A mudança
fica rejeitada como política global. Não há motivo estatístico para aumentar
frequência à força.

## Decisão

- Nenhum ativo passa os gates de promoção. BTC é o único sinal economicamente
  interessante, porém com apenas ~6–7 trades/mês e sem estabilidade mensal.
- ETH permanece em caixa; o modelo horário não demonstrou edge robusto.
- SOL permanece em caixa; o resultado positivo da V4.1 não resistiu a custos e
  a pequenas mudanças de política.
- A próxima pesquisa deve ser uma mudança de hipótese (label/regime ou um
  modelo challenger), com orçamento pré-registrado. Não serão feitos novos
  ajustes de limiar ou permanência no mesmo holdout para “fabricar” trades.

## Artefatos

- Tuning V4.2: `artifacts/v4/tuning/20260820T155520Z/tuning.json`.
- Walk-forward V4.2: `artifacts/v4/20260820T155859Z/run.json` (BTC),
  `20260820T160030Z/run.json` (ETH), `20260820T160210Z/run.json` (SOL).
- Tuning V4.3: `artifacts/v4/tuning/20260820T160604Z/tuning.json`.
- Walk-forward V4.3: `artifacts/v4/20260820T161011Z/run.json` (BTC),
  `20260820T161159Z/run.json` (ETH), `20260820T161337Z/run.json` (SOL).

