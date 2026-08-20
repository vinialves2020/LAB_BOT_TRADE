# Resultados V4.6 — classificador ordinal (BTC)

Execução: `2026-08-20`. O holdout permaneceu fechado.

| Família | Trades | Trades/mês | Retorno 24 bps | Retorno 48 bps | Sharpe | Drawdown |
|---|---:|---:|---:|---:|---:|---:|
| XGBoost ordinal + regressão | 6 | 3,00 | +3,89% | +2,03% | 20,24 | 0,00% |
| HistGradientBoosting ordinal + regressão | 0 | 0,00 | 0,00% | 0,00% | 0,00 | 0,00% |

O XGBoost teve seis trades, concentrados em um único mês. Os números de Sharpe
e drawdown não têm validade estatística com essa amostra. O challenger não
produziu operações elegíveis.

## Diagnóstico e decisão

O rótulo ordinal reduziu a esparsidade em relação à V4.4/V4.5, mas ainda fica
muito abaixo de 20 trades/mês e não atende o piso mensal de 10 trades. A maior
parte dos folds caiu no fallback de calibração, que preserva o gate em vez de
forçar operações. Não houve alteração pós-resultado de thresholds ou custos.

V4.6 é rejeitada como candidata de paper. A linha de XGBoost conjunto,
normalizado e ordinal está encerrada até que exista uma hipótese estrutural
nova ou mais dados prospectivos. V4.3 continua apenas como benchmark de
pesquisa; nenhum ativo pode seguir para capital real.

## Artefatos

- XGBoost: `artifacts/v4/joint/20260820T182801Z/xgboost/BTCUSDT/result.json`.
- HistGradientBoosting:
  `artifacts/v4/joint/20260820T182956Z/hist_gradient_boosting/BTCUSDT/result.json`.

