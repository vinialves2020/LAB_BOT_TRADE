# Protocolo V4.6 — classificação ordinal de retorno

V4.6 é uma única mudança de rótulo sobre a V4.4. O BTC permanece como único
ativo de desenvolvimento, com XGBoost conjunto e HistGradientBoosting
challenger; ETH/SOL continuam controles e o holdout permanece fechado.

## Rótulo ordinal

Cada candle recebe uma das três classes, usando o custo-base de 24 bps:

- `0`: retorno bruto abaixo de `-24 bps`;
- `1`: retorno entre `-24` e `+24 bps` (neutro);
- `2`: retorno bruto acima de `+24 bps`.

O classificador produz `P(negativo)`, `P(neutro)` e `P(positivo)`. As
probabilidades positiva e negativa são calibradas separadamente com previsões
fora da amostra. A regressão continua sendo a magnitude do retorno. A entrada
exige `P(positivo) ≥ {0,50; 0,55; 0,60}`, `P(positivo) > P(negativo)` e retorno
previsto acima do custo + margem. A política, custos, seeds e folds não mudam.

## Critério

V4.6 só é útil se resolver a esparsidade sem perder o custo dobrado, o drawdown
e a estabilidade entre seeds. Se não houver pelo menos 10 trades em cada mês
e 20 trades/mês em média, o ativo continua em caixa. Não serão reduzidos gates
depois de ver os resultados.

```powershell
python -m bottrade v4 joint --asset BTCUSDT --family xgboost --max-folds 12 --v4-config config/v4_ordinal.yaml
python -m bottrade v4 joint --asset BTCUSDT --family hist_gradient_boosting --max-folds 12 --v4-config config/v4_ordinal.yaml
```

