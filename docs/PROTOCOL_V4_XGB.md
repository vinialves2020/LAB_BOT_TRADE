# Protocolo V4 — XGBoost direto, cost-aware, horizonte de 12h

Status: pré-registro antes da primeira rodada V4. O holdout continua fechado.

## Decisão

A primeira família será XGBoost. Haverá um regressor por ativo (`BTCUSDT`,
`ETHUSDT`, `SOLUSDT`) e cinco membros com seeds `11, 23, 37, 53, 71`. O
ensemble será a média das previsões; nenhuma seed individual será promovida.

O modelo recebe observações horárias de mercado e estatísticas dos quatro
candles de 15 minutos já encerrados. Breakouts, tendência e reversão entram
como variáveis explicativas; não existe gerador de candidatos que force uma
operação.

## Label

Para uma decisão no fechamento de `t`, a entrada é o próximo `open` disponível.
O alvo é o retorno simples entre essa entrada e o `close` do candle de 12h.
Uma amostra é inválida quando falta candle, há gap, o lookback de 168h não é
contínuo ou o horizonte atravessa o holdout.

O custo-base é 24 bps por round trip. A política entra somente quando a
previsão do ensemble supera `24 bps + margem`, com margens pré-registradas de
`0, 5, 10, 20 e 30 bps`. O stress usa 48 bps.

A calibração affine de escala é implementada como diagnóstico opcional, mas
fica desligada no primeiro núcleo pré-registrado: o teste piloto mostrou que
um intercepto positivo na janela de calibração poderia transformar uma média
histórica em falso sinal para todas as horas. Ativar essa calibração exigiria
um novo protocolo antes de qualquer resultado ser comparado.

## Validação

Walk-forward mensal com 24 meses de treino, 3 meses de calibração, 1 mês de
teste e purge/embargo de 12h. No máximo 20 configurações são permitidas no
braço inicial. A calibração escolhe a margem por Sortino líquido, respeitando
20 trades mínimos na janela e dois round trips completos por ativo/dia.

Nenhuma escolha consulta o período `2025-08-01`–`2026-07-31`. Se o núcleo não
passar os gates, o resultado será registrado como falha; não haverá ajustes
ilimitados até produzir lucro.

## Gates econômicos

- Sharpe diário anualizado mínimo de 1,0.
- Profit factor mínimo de 1,2.
- Drawdown máximo de 8%.
- Resultado líquido positivo com custos-base e dobrados.
- Média alvo de 20 trades/mês no portfólio e pelo menos 60 trades na calibração.
- Superioridade aos controles e estabilidade entre as cinco seeds.

Passar esses gates não autoriza dinheiro real. O caminho posterior continua
sendo holdout único, canário de 14 dias e paper oficial.
