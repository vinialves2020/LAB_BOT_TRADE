# Protocolo V4.1 — XGBoost horário com filtro de custo persistente

Status: segunda tentativa pré-holdout, criada após a reprovação documentada do
alvo de 12h. O holdout `2025-08-01`–`2026-07-31` continua fechado.

## Mudanças pré-registradas

- alvo: retorno da próxima hora (`next open` até `next close`);
- objetivo: `reg:squarederror`;
- decisão: a cada hora, com uma posição persistente `long/flat`;
- entrada: previsão positiva acima de `24 bps + margem`;
- saída: previsão negativa abaixo do limiar, doze horas de permanência ou
  falha operacional;
- máximo de duas entradas/saídas completas por ativo/dia;
- margens permitidas: `0, 5, 10, 20 e 30 bps`;
- cinco seeds finais, agregadas por ensemble.

O filtro persistente evita contar uma nova operação a cada candle enquanto a
posição continua aberta. O custo dobrado usa 48 bps e não escolhe parâmetros.

## Motivo da revisão

O núcleo V4 de 12h, Pseudo-Huber e posições independentes foi executado em 12
folds pré-holdout e falhou nos três ativos. O estudo externo usado como
motivação trabalha com retorno horário, filtro cost-aware baseado na mudança de
posição e MSE; essa reprodução será testada uma única vez antes de considerar
XGBoost encerrado para este laboratório.

Não haverá novas alterações de horizonte, objetivo ou política depois de ver os
resultados V4.1 sem registrar outro protocolo.
