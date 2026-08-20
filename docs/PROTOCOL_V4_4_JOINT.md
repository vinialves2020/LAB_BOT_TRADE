# Protocolo V4.4 — classificação cost-aware + regressão

## Escopo

V4.4 é um challenger restrito ao BTC. A V4.3 permanece como benchmark
congelado; ETH e SOL não entram na busca de desenvolvimento. O holdout
`2025-08-01` a `2026-07-31` continua fechado.

## Hipótese

O regressor sozinho pode produzir muitos sinais pequenos que não pagam custos.
V4.4 exige concordância de dois modelos:

1. Classificador: `gross_return > 24 bps`, com probabilidade calibrada por
   sigmoid usando previsões fora da amostra do período de calibração.
2. Regressor: retorno logarítmico previsto acima de 24 bps + margem.

A entrada só ocorre quando ambos concordam. A política testa, na calibração,
as combinações fixas de probabilidade `{0,50; 0,55; 0,60}` e margem `{0, 5, 10,
20, 30}` bps. Saída ocorre quando a classificação deixa de ser elegível, a
regressão fica não positiva, há seis horas de permanência, candle inválido ou
regra de risco.

## Famílias

- `xgboost`: regressão e classificação com os mesmos hiperparâmetros tabulares
  congelados da V4.3.
- `hist_gradient_boosting`: regressão e classificação HistGradientBoosting,
  com parâmetros fixos e cinco seeds.

Não há busca de hiperparâmetros nesta rodada. O objetivo é comparar a hipótese
de dois sinais e a família challenger, não procurar o melhor número após ver
os resultados.

## Validação

- 12 folds mensais pré-holdout, 24 meses de treino, 3 de calibração, 1 de
  teste e purge de 12h.
- Cinco seeds `11, 23, 37, 53, 71`; nenhum membro vencedor é escolhido.
- Custos de 24 bps e estresse de 48 bps por round trip.
- Gates econômicos e de frequência da V4 continuam obrigatórios.

## Comandos

```powershell
python -m bottrade v4 joint --asset BTCUSDT --family xgboost --max-folds 12
python -m bottrade v4 joint --asset BTCUSDT --family hist_gradient_boosting --max-folds 12
```

Nenhum resultado desta rodada promove modelo, abre holdout ou ativa paper.

