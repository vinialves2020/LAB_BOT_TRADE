# Protocolo V4.5 — alvo de retorno normalizado por volatilidade

V4.5 muda uma única hipótese da V4.4. O BTC continua sendo o único ativo de
desenvolvimento, com XGBoost conjunto e HistGradientBoosting como challenger.
O holdout `2025-08-01` a `2026-07-31` permanece fechado.

## Alvo

O regressor treina:

`log(closet+1 / opent+1) / EWMA_volatility_168h(t)`.

A volatilidade é calculada apenas com o passado e já está no schema causal como
`ewma_volatility_1h`. Na inferência, a previsão volta para retorno logarítmico
multiplicando pela volatilidade conhecida no instante `t`. A classificação
continua sendo `gross_return > 24 bps`, portanto a entrada ainda precisa pagar
o custo nominal e a margem.

Não há novo grid de hiperparâmetros, alteração de custo, redução de gate ou
abertura de holdout nesta rodada.

## Validação

12 folds mensais, purge de 12h, cinco seeds, probabilidade calibrada somente
com previsões fora da amostra e estresse de 48 bps. O benchmark é a V4.3 e o
resultado só é considerado útil se mantiver frequência e gates econômicos.

```powershell
python -m bottrade v4 joint --asset BTCUSDT --family xgboost --max-folds 12 --v4-config config/v4_normalized.yaml
python -m bottrade v4 joint --asset BTCUSDT --family hist_gradient_boosting --max-folds 12 --v4-config config/v4_normalized.yaml
```

