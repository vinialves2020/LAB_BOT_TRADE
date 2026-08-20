# Protocolo V4.2 — refinamento controlado do XGBoost horário

## Objetivo

Refinar o XGBoost horário que apresentou sinal positivo em BTC e SOL na V4.1,
sem reabrir o holdout `2025-08-01` a `2026-07-31` e sem iniciar uma busca
ilimitada. ETH permanece um diagnóstico negativo até que uma rodada completa,
pré-registrada, demonstre melhora.

## Mudanças permitidas

1. O horizonte continua em 1h, com posição long/flat persistente, saída por
   previsão negativa, 12 horas ou regra de risco.
2. O conjunto de dados continua sendo mercado 1h + agregados causais dos quatro
   candles 15m encerrados antes de `as_of`.
3. Volumes, negócios e volume agressor recebem `log1p`; razões agressoras viram
   desequilíbrios assinados; volatilidades de 6h/24h/72h recebem razão contra
   a volatilidade de 168h. Os campos absolutos correspondentes são removidos.
   Nenhum preço é interpolado e nenhum campo de continuidade que olha o futuro
   entra no modelo.
4. Oito configurações XGBoost fixas (`xgb_01` a `xgb_08`) são testadas. A lista
   está no código e não pode ser expandida depois de observar os resultados.

## Busca e congelamento

- A busca usa somente os três primeiros folds gap-aware disponíveis antes do
  holdout e apenas a seed 11.
- A pontuação, definida antes da busca, é:

  `0,5 × retorno líquido base + 0,5 × retorno líquido com custo dobrado − drawdown máximo`.

- Candidatos com menos de cinco trades nos folds de busca não podem vencer.
- O melhor JSON por ativo é congelado. Só depois dele são executados os 12
  folds finais com as cinco seeds `11, 23, 37, 53, 71`.
- A V4.2 não abre o holdout. O holdout só será tocado após revisão do relatório
  pré-holdout e lock criptográfico do candidato.

## Gates de decisão

Para ser candidato a canário, o ativo precisa manter retorno positivo com 24 e
48 bps, Sharpe diário anualizado ≥ 1,0, profit factor ≥ 1,2, drawdown ≤ 8%,
volume mínimo definido no protocolo V4.1 e estabilidade entre seeds. Caso não
atinja os gates, permanece em caixa; não se aumenta o risco para produzir mais
trades.

## Comandos reproduzíveis

```powershell
python -m bottrade v4 tune --v4-config config/v4_refined.yaml --search-folds 3
python -m bottrade v4 run --asset BTCUSDT --max-folds 12 `
  --v4-config config/v4_refined.yaml `
  --params artifacts/v4/tuning/<run_id>/BTCUSDT/best_params.json
```

O mesmo comando `run` é repetido para ETHUSDT e SOLUSDT com o JSON específico
de cada ativo. Artefatos de tuning e walk-forward ficam em `artifacts/v4/`
(ignorados pelo Git), enquanto este protocolo e o resultado resumido são
versionados.

