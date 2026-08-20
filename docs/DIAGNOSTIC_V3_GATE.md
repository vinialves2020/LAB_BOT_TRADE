# Diagnóstico V3 — sinal, labels e gate

Data: 2026-08-20. Esta análise usa somente os artefatos BTCUSDT anteriores ao
holdout (`as_of < 2025-08-01T00:00:00Z`). Nenhum resultado desta página abre o
holdout.

## Evidências dos dados

- `features.parquet`: 69.612 candles, 77 colunas, UTC, até 2025-07-31.
- `candidates.parquet`: 68.785 candidatos em 31.696 horários distintos.
- `labels.parquet`: 68.483 labels válidos e 302 inválidos.
- Retorno líquido 1× positivo em 44,16% dos labels válidos; mediana −21,13
  bps e média −17,95 bps.
- Resultados dos eventos: 31.971 timeouts, 21.412 take-profits e 15.100
  stop-losses.

Os labels não são simplesmente todos negativos, mas a distribuição líquida é
desfavorável depois dos custos. O conjunto também é muito concentrado:

| Família | Candidatos | Participação |
|---|---:|---:|
| Tendência | 64.864 | 94,30% |
| Reversão | 2.073 | 3,01% |
| Breakout | 1.848 | 2,69% |

Entre as variantes, apenas `breakout_72h_h12` apresentou média líquida
positiva (+8,75 bps); as três variantes de tendência tiveram médias entre
−13,64 e −23,22 bps.

## Evidências dos modelos

Nos bundles completos disponíveis, avaliados sobre a matriz de desenvolvimento
para diagnóstico (não como métrica OOS):

- HGB: probabilidade calibrada máxima aproximadamente 0,437.
- RF: probabilidade calibrada máxima entre 0,469 e 0,478 nas seeds 11, 23 e
  37.
- As execuções anteriores usavam thresholds `[0,55; 0,60]`, embora o protocolo
  previsse `[0,50; 0,55; 0,60]`. Assim, o gate antigo era impossível para esses
  modelos e explica os zero trades observados.
- A configuração foi corrigida para margens `[0; 5; 10; 20; 30]` bps. Mesmo
  com `p≥0,50`, os bundles existentes continuam sem exemplos aprovados; isso
  aponta para baixa separação preditiva, não apenas para um typo de configuração.

## Decisão

O braço `market_1h + intrahour_15m` não deve avançar para holdout, canário ou
paper. A falha econômica do signal ceiling e a probabilidade calibrada baixa
justificam congelar o treino até uma nova rodada pré-holdout, com protocolo e
configuração corrigidos.

## Próxima rodada, se autorizada

1. Separar e avaliar tendência, reversão e breakout antes de misturar candidatos;
2. limitar a sobreposição por horário/candidato para não deixar tendência dominar;
3. calcular Brier, AUC, calibração e precisão nos thresholds antes do backtest;
4. executar um piloto barato com a grade corrigida e orçamento RF explícito;
5. somente se houver sinal preditivo e frequência aceitável, repetir o ensemble
   completo e ONNX.

Nenhuma dessas ações autoriza relaxar custos, risco ou critérios de promoção.
