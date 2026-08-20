# Resultados V4.5 — alvo normalizado por volatilidade

Execução: `2026-08-20`. BTC foi o único ativo de desenvolvimento; o holdout
permaneceu fechado.

| Família | Trades | Trades/mês | Retorno 24 bps | Retorno 48 bps | Sharpe | Drawdown |
|---|---:|---:|---:|---:|---:|---:|
| XGBoost conjunto | 1 | 1,00 | +0,62% | 0,00% | 0,00 | 0,00% |
| HistGradientBoosting conjunto | 0 | 0,00 | 0,00% | 0,00% | 0,00 | 0,00% |

O alvo de regressão foi `log-return / EWMA_volatility_168h(t)` e voltou a
retorno bruto antes do gate. Amostras sem volatilidade causal disponível foram
excluídas; candles de volatilidade zero receberam apenas piso numérico de
`1e-6`, sem interpolação.

## Decisão

A normalização não resolveu o gargalo observado na V4.4: a concordância entre
classificação cost-aware e regressão continua esparsa demais. Os números não
formam amostra estatística e nenhum candidato passa frequência ou gates.

Não serão feitos novos ajustes de limiar, piso de trades ou custo nesta linha.
O próximo trabalho deve ser uma revisão de hipótese mais ampla — por exemplo,
retorno ordinal/ranking com calibragem temporal — ou uma pausa para coletar
mais dados prospectivos. V4.3 permanece apenas como benchmark de pesquisa; não
há promoção para paper/capital.

## Artefatos

- XGBoost: `artifacts/v4/joint/20260820T163732Z/xgboost/BTCUSDT/result.json`.
- HistGradientBoosting:
  `artifacts/v4/joint/20260820T163907Z/hist_gradient_boosting/BTCUSDT/result.json`.

