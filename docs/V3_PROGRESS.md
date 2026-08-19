# V3 — estado de implementação

## Concluído

- V2 congelada em `aaa2b28` como resultado negativo/inconclusivo;
- branch de implementação `codex/v3-meta-strategies`;
- protocolo e configuração V3 pré-registrados;
- geradores de candidatos de tendência, reversão e breakout;
- features 1h, intrahora 15m e contexto cruzado BTC/ETH/SOL;
- labels next-open com TP/SL/timeout, stop-first, gaps e custos 1×/2×/3×;
- folds walk-forward purgados, calibração cronológica, DSR e PBO;
- Random Forest, HistGradientBoosting e Transformer em patches;
- validação ONNX com tolerância `1e-4` para RF, HGB e Transformer;
- dois ledgers de portfólio e limites de risco;
- CLI `bottrade v3` e manifestos Parquet com hash/schema;
- braços composíveis com `available_at`, idade, missing/stale e filtro de
  derivativos sem colunas de alvo;
- gates mensais de frequência e comando `v3 gates`;
- holdout fechado por padrão;
- 11 testes V3 passando.

## Replay pré-holdout executado

Para BTCUSDT, o pipeline gerou 69.612 features, 68.785 candidatos e 68.483
rótulos válidos. O signal ceiling determinístico teve 4.746 trades, retorno
total negativo e PF 0,67 a custo-base; não há evidência de edge sem filtragem.

Um smoke-test HGB com 40 iterações produziu apenas um trade após o filtro
cost-aware. Ele serve para verificar o encadeamento, não é candidato de
promoção. A primeira execução de 300 iterações foi descartada após a auditoria
encontrar campos de resultado vazando para a matriz; nenhum desses números será
usado em seleção.

## Próximo passo seguro

1. Regerar features/candidatos/labels para ETHUSDT e SOLUSDT.
2. Executar as ablações sequenciais com hiperparâmetros congelados.
3. Rodar as cinco seeds finais por família/ativo e registrar o ledger de trials.
4. Consolidar gates por mês/regime e gerar o selection lock.
5. Somente depois de revisão humana abrir o holdout uma única vez.

Canário, paper oficial e qualquer discussão de capital real continuam bloqueados
até os gates acima e uma revisão operacional separada.
