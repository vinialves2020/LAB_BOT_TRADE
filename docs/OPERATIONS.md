# Runbook operacional

## Estados permitidos

`development` é pesquisa anterior ao holdout. `holdout` é avaliação offline congelada. `canary` é paper operacional por pelo menos 14 dias. `paper` é o período oficial por pelo menos 183 dias. Não existe estado, credencial ou comando de real-money.

## Checklist antes do canário

1. Sincronizar dados, construir datasets e concluir os oito candidatos por ativo.
2. Criar a seleção imutável antes do holdout; revisar checksums, model cards, cinco seeds, explicabilidade e ONNX.
3. Executar uma vez cada candidato congelado distinto no holdout.
4. Promover `champion` e `market_fallback` aprovados dos três ativos para `canary`; promover `challenger` se houver.
5. Inicializar Neon/Postgres e executar `bottrade paper reconcile` nos dois ledgers.
6. Validar Telegram, relógio Binance, regras de símbolo, bucket de modelos e dashboard com `bottrade doctor`.
7. Executar `bottrade paper canary-start`; os jobs de mutação recusam rodar sem fase ativa.
8. Executar manualmente `risk`, depois `signal`, e repetir `signal` para comprovar idempotência; somente então habilitar schedulers.

## Frequências UTC

- `signal`: minuto 02 de toda hora, após fechamento do candle.
- `risk`: a cada 15 minutos.
- `daily`: 00:15.

`signal` reconcilia o banco, valida relógio/continuidade, hidrata os bundles ONNX, grava champion e shadow forecasts, marca patrimônio, calcula targets e simula fills. `risk` não abre posições; apenas reconcilia, marca e executa saídas obrigatórias. `daily` gera relatório e resumo Telegram.

## Atomicidade e idempotência

O `client_order_id` deriva de ledger, ativo, candle e intenção. Rodar o mesmo ciclo duas vezes não cria outra ordem. As alterações dos dois ledgers de um lote são confirmadas numa única transação; falha de banco desfaz o lote todo.

Uma lease global no banco serializa as seções mutáveis de `signal` e `risk`, inclusive se duas execuções Cloud Run se sobrepuserem. A lease expira em cinco minutos após morte abrupta; disputa ativa falha fechada e é tentada novamente pelo scheduler.

Cada fill registra bid, ask, quantidade/notional visíveis, spread e impacto estimado. Antes de cada job, `cash + valor das posições` precisa reconciliar com o patrimônio persistido. Divergência coloca os ledgers em `manual_pause`, registra evento crítico e impede novas exposições.

## Falha segura

Não abrir posição em caso de candle incompleto/stale ou com gap, relógio divergente, schema/hash inválido, modelo ausente, ONNX inválido, banco indisponível, livro insuficiente, regras Binance inválidas ou ciclo duplicado.

Fonte alternativa ausente ou com idade superior a 72h seleciona somente o `market_fallback` pré-congelado. Candle de mercado ausente não tem fallback e bloqueia entradas. Falha de Telegram não altera o ledger; fica registrada para investigação.

## Circuit breakers

- Perda máxima por posição: 0,5% do patrimônio.
- Perda diária: 1%; liquida e bloqueia novas entradas até a próxima data UTC.
- Drawdown: 8%; liquida, entra em `circuit_breaker` e exige retomada manual.
- Holding máximo: 12h.
- Limites de alocação: 20% por ativo e 50% de exposição total.

Retomada manual:

    bottrade paper reconcile
    bottrade paper resume --ledger paper_500 --confirmation RESUME-PAPER

Repetir para o outro ledger somente depois de identificar e corrigir a causa. `resume` não apaga eventos nem altera modelos.
O comando aceita apenas `circuit_breaker` ou `manual_pause`; um `daily_stop` é liberado automaticamente somente na primeira marcação de patrimônio do dia UTC seguinte.

## Encerramento do canário e reset

Após 14 dias completos e sem incidente crítico:

    bottrade paper canary-complete
    bottrade report
    bottrade paper reset-after-canary --confirmation RESET-PAPER-AFTER-CANARY --bucket PROJECT-bottrade-models

O reset zera caixa/posições para 500 e 1.000 USDT e inicia automaticamente o paper oficial. Ordens, fills, forecasts, snapshots, eventos, ciclos e a fase do canário permanecem append-only; métricas oficiais são filtradas pelo início da nova fase.

O conjunto de ativos habilitados é congelado no início do canário. Ativar ou remover um ativo durante os 14 dias impede a conclusão; se nenhum ativo passar o holdout, o canário nem é iniciado.

Durante o canário só se corrigem falhas operacionais sem mudar a estratégia. Mudança de feature, modelo, threshold, gate ou sizing exige novo protocolo e novo canário.

## Refit mensal

O refit ocorre localmente, idealmente na RTX 2060, e herda o artefato ativo:

    bottrade models refit --asset BTCUSDT --slot champion

Revisar dataset/schema, lineage, model card, threshold recalibrado e paridade ONNX. Para uma versão aprovada:

    bottrade models refit --asset BTCUSDT --slot champion --activate
    bottrade models publish --asset BTCUSDT --slot champion --bucket PROJECT-bottrade-models

Fazer também para `market_fallback` e, se usado, `challenger`. Falha em qualquer verificação mantém o ponteiro anterior. O refit não pode mudar família, braço ou hiperparâmetros.

## Recuperação após interrupção

1. Pausar os três Cloud Schedulers.
2. Verificar Neon e o último `ProcessedCycle`.
3. Rodar `bottrade doctor` e `bottrade paper reconcile`.
4. Conferir o último candle fechado, ponteiros e checksums no bucket.
5. Reexecutar primeiro `risk` e depois `signal`; IDs determinísticos evitam reaplicação.
6. Confirmar `cash + posições = equity` nos dois ledgers.
7. Reativar os schedulers somente após consistência.

## Fechamento oficial

Depois de 183 dias completos:

    bottrade paper official-complete
    bottrade paper evaluate
    bottrade report

`official-complete` exige que as posições já tenham sido zeradas pelas regras normais e que a reconciliação esteja íntegra. Se houver posição, manter `risk` ativo até a saída de no máximo 12h; não é criado um fill artificial retrospectivo. Pausar os schedulers antes do comando final.

O avaliador cruza holdout e paper por ativo/ledger, reconstrói trades, aplica custo incremental para o cenário dobrado, compara controles e verifica incidentes. `passed=true` não habilita ordens reais; apenas permite iniciar uma revisão independente de infraestrutura paga, segurança, jurídico/tributário e autorização explícita.
