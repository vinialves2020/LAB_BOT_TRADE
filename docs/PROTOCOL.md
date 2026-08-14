# Protocolo pré-registrado v1

## Pergunta e hipótese

Avaliar, dentro do mesmo ativo e braço informacional, se um Transformer temporal extrai dependências que melhoram retorno líquido ajustado a risco em relação a um Random Forest, e se eventual melhora compensa custo computacional, instabilidade e menor transparência.

Resultados entre ativos não são tratados como experimentos equivalentes. O estudo de 15 minutos será outro protocolo; não existe alternância dinâmica de timeframe nesta versão.

## Universo e política

- `BTCUSDT`, `ETHUSDT` e `SOLUSDT` spot.
- Long/flat, sem short, margem, alavancagem ou empréstimo.
- Features disponíveis no fechamento do candle de 1h.
- Sinal recalculado de hora em hora e execução simulada a partir do próximo preço executável.
- Horizonte do alvo de 3h e holding máximo de 12h.
- Dois patrimônios independentes recebem os mesmos sinais, sem compartilhar caixa.

## Braços e igualdade informacional

1. `market`
2. `market_onchain`
3. `market_sentiment`
4. `market_all`

RF e Transformer recebem o mesmo conteúdo informacional e o contexto de retorno/volatilidade dos outros dois ativos. O RF usa a linha tabular com lags e estatísticas; o Transformer usa sequências de 168 linhas e embeddings aprendidos de hora/dia. Comparações primárias são família contra família dentro do mesmo ativo e braço.

## Alvo

Após o fechamento em `t`, o retorno bruto é `log(close[t+3] / open[t+1])`. Ele é dividido por uma estimativa EWMA de desvio dos retornos horários que usa uma janela dura de exatamente 168 observações até `t`; pesos anteriores à janela não influenciam o alvo. Abertura, fechamento futuro e label nunca entram nas features.

## Congelamentos

- Holdout offline: `2025-08-01 00:00:00` a `2026-07-31 23:59:59` UTC.
- Máximo de 30 configurações por família/ativo, pesquisadas somente no braço `market`.
- Hiperparâmetros encontrados em `market` são reutilizados sem nova busca nas três ablações.
- Seeds finais independentes: 11, 23, 37, 53 e 71. Métricas oficiais são medianas; dispersão por seed também é registrada. Não há ensemble entre seeds.
- Thresholds: custo round trip de 24 bps mais `{0, 5, 10, 20, 30}` bps.
- Mínimo de 20 trades e máximo de turnover 2,0 por dia no período de calibração.
- Família, braço, campeão, fallback e challenger são congelados antes de qualquer leitura do holdout.
- No paper, somente refit mensal é permitido, conservando família, braço, hiperparâmetros e raiz de linhagem.

## Separação desenvolvimento/holdout

O comando `train` cria apenas folds com teste anterior ao início do holdout. Depois que existem os oito candidatos elegíveis de um ativo, `models select` grava um lock imutável contendo parâmetros, versões, caminhos e SHA-256. O comando `holdout` valida esse lock, permite uma única abertura por candidato congelado e grava a versão resultante. Um arquivo alterado após o lock invalida a execução.

Se duas funções congeladas apontarem para o mesmo `run_id`, uma avaliação satisfaz as duas. Uma falha operacional pode ser retomada com `--resume`, mas não é permitido trocar parâmetros. Uma nova hipótese ou ajuste motivado pelo holdout exige protocolo v2 e novo holdout futuro.

## Validação e ajuste

- Walk-forward mensal: 24 meses de treino, 3 meses de calibração e 1 mês de teste.
- Purge/embargo mínimo de 3h entre blocos.
- Imputadores, scalers, early stopping, seleção de features e threshold ajustam somente passado.
- Threshold escolhido pelo maior Sortino líquido; desempates: retorno, depois menor drawdown.
- Custo-base: 10 bps de taxa + 2 bps de fricção por perna, 24 bps por round trip.
- Estresse: todas as pernas com custo dobrado.
- Entrada apenas acima do threshold; saída por previsão não positiva, 12h ou regra de risco.
- Posição histórica por ativo limitada a 20%, compatível com a política paper.

## Modelos e controles

- `RandomForestRegressor` com lags/estatísticas de 1, 3, 6, 12, 24, 72 e 168h.
- Encoder Transformer compacto de 2–3 camadas, janela 168h, embeddings de calendário e regressão escalar.
- Controles: caixa, buy-and-hold, buy-and-hold escalado ao risco, cruzamento de médias e Ridge.
- Exportação ONNX obrigatória; promoção exige erro absoluto máximo de `1e-4` contra o modelo nativo.
- Permutation importance para ambos, SHAP para RF, integrated gradients e ablação temporal para Transformer. Atenção não é interpretada como explicação causal.

## Métricas

Preditivas: MAE, RMSE, correlação de Spearman e acerto direcional.

Trading: retorno líquido, Sharpe/Sortino diário anualizado, drawdown, Calmar, profit factor, turnover, exposição, hit rate, custos e trades fechados.

Robustez: regimes de tendência/queda/lateralização e volatilidade, cinco seeds, custo dobrado e controles.

Operacionais: tempo de treino/exportação/inferência, carga ONNX, memória de pico, tamanhos, staleness, divergência ONNX e incidentes.

## Seleção e promoção

Antes do holdout, reprovar apenas artefatos tecnicamente inválidos: matriz incompleta, parâmetros de ablação divergentes, explicabilidade ausente, métrica não finita ou ONNX fora da tolerância. Não aplicar retrospectivamente os gates econômicos finais nessa escolha. Entre os válidos, ordenar por Sortino mediano, menor drawdown e retorno sob estresse. O melhor `market` tecnicamente válido é congelado como fallback; sem fallback, um campeão com dados alternativos não pode ser escolhido. O segundo melhor distinto é o challenger shadow.

O mesmo conjunto de gates é reavaliado no holdout. Falha impede promoção para canário e mantém o ativo/slot em caixa. Durante os seis meses oficiais, o challenger não gera targets nem fills.

Os ativos aprovados são congelados explicitamente no registro da fase canário e copiados sem alteração para a fase oficial. Um ativo reprovado não bloqueia o estudo dos demais, mas não pode ser ativado no meio do período.

## Integridade acadêmica

Os artefatos guardam commit quando disponível, seeds, hashes, parâmetros, folds, versões de dependência, métricas, explicabilidade e model card. Execuções com `--max-folds`, seeds reduzidas ou `backtest` diagnóstico recebem `protocol_eligible=false`.

Uma execução oficial também exige `HEAD` disponível e nenhuma alteração não commitada em código, configuração, protocolo ou dependências. Mudanças esperadas em diretórios gerados de dados/artefatos não tornam o código dirty; a trava de seleção possui seu próprio hash de integridade.

Qualquer mudança de feature, arquitetura, threshold ou gate após observar holdout/paper cria uma nova versão de protocolo. O histórico original permanece preservado e nunca será reclassificado como teste intocado.
