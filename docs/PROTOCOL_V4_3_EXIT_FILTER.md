# Protocolo V4.3 — saída por previsão não positiva

V4.2 foi um refinamento exploratório: a seleção de hiperparâmetros usou os
primeiros folds e a avaliação final compartilhou parte dessas janelas. Seus
resultados não são promoção nem holdout. V4.3 corrige esse ponto e testa apenas
uma mudança de política de risco/frequência.

## Hipótese única

Uma posição horária não deve permanecer aberta enquanto a previsão líquida
ficou não positiva. A política V4.3 sai no primeiro evento entre previsão
`<= 0`, previsão abaixo do custo, seis horas de permanência, candle inválido ou
limite de risco. O horizonte do alvo permanece 1h e não há short.

## Seleção sem leakage

- Oito hiperparâmetros XGBoost continuam fixos em `v4/search.py`.
- A busca é feita nos três primeiros folds, mas avalia somente as previsões
  fora da amostra do período de calibração; os testes desses folds não entram
  na pontuação.
- A pontuação é `0,5 × retorno de calibração a 24 bps + 0,5 × retorno a 48 bps −
  drawdown`, com piso de cinco trades.
- Após congelar um JSON por ativo, executam-se os 12 testes mensais completos,
  cinco seeds, sem reescolher parâmetros. O holdout permanece fechado.

## Critério de interpretação

O objetivo não é fabricar 20 trades/mês. Frequência só conta se vier com
retorno líquido e risco aceitável. Um ativo com drawdown acima de 8%, custo
dobrado negativo ou menos de 10 trades em algum mês continua em caixa.

## Comandos

```powershell
python -m bottrade v4 tune --v4-config config/v4_refined_fast.yaml --search-folds 3
python -m bottrade v4 run --asset BTCUSDT --max-folds 12 `
  --v4-config config/v4_refined_fast.yaml `
  --params artifacts/v4/tuning/<run_id>/BTCUSDT_best_params.json
```

