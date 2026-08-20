# Resultados V4.4 — classificação + regressão (BTC)

Execução: `2026-08-20`. O holdout não foi aberto.

## Resumo

| Família | Trades | Trades/mês | Retorno 24 bps | Retorno 48 bps | Sharpe | Drawdown | PF |
|---|---:|---:|---:|---:|---:|---:|---:|
| XGBoost conjunto | 3 | 1,50 | +0,50% | +2,03% | 9,19 | 0,30% | 2,68 |
| HistGradientBoosting conjunto | 0 | 0,00 | 0,00% | 0,00% | 0,00 | 0,00% | — |

Os números de Sharpe/PF do XGBoost não são interpretáveis com apenas três
trades. O HistGradientBoosting não produziu uma entrada elegível em nenhum
fold.

## Diagnóstico

- A classificação foi treinada para `gross_return > 24 bps`.
- A entrada exigiu probabilidade calibrada acima de 0,50/0,55/0,60 **e**
  regressão acima do custo mais margem.
- Quando a calibração não atingiu 20 trades, a política caiu para 0,60 + 30
  bps, preservando o gate de frequência em vez de forçar operações.
- O resultado mostra que a confirmação binária, nesta representação e neste
  período, é esparsa demais. Reduzir o gate só para fabricar trades seria
  overfitting e não foi feito.

## Decisão

V4.4 é rejeitada como candidata de produção/paper. A V4.3 continua sendo o
benchmark congelado, sem promoção. A próxima hipótese deve mudar o alvo ou a
calibração (por exemplo, classificação ordinal/quantílica ou label de excesso
de retorno por volatilidade), mantendo o mesmo gate econômico e sem reabrir o
holdout.

## Artefatos

- XGBoost: `artifacts/v4/joint/20260820T162535Z/xgboost/BTCUSDT/result.json`.
- HistGradientBoosting:
  `artifacts/v4/joint/20260820T162707Z/hist_gradient_boosting/BTCUSDT/result.json`.

