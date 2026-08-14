# Primeira leva de treinamento — resultado negativo

**Status:** encerrada como experimento negativo; nenhum modelo foi promovido.

**Data da execução:** 14 de agosto de 2026 UTC  
**Protocolo:** v1  
**Braço executado:** `market`  
**Holdout:** não aberto  
**Capital real:** não utilizado

## Resumo executivo

A primeira leva cumpriu o objetivo científico de testar o pipeline RF × Transformer em
BTC, ETH e SOL sob custos, purge/embargo, cinco seeds, explicabilidade e exportação ONNX.
O resultado econômico foi insuficiente. O Transformer foi mais capaz que o Random Forest
de produzir sinais que ultrapassassem o custo mínimo, mas os poucos trades e a variação
entre seeds impedem concluir que exista uma vantagem persistente.

Isso não foi uma falha operacional. Dados, alinhamento temporal, execução dos modelos,
GPU, determinismo, ONNX e testes funcionaram. A falha foi de adequação estatística e
econômica: o sinal encontrado não foi suficientemente forte, frequente e estável.

## O que foi executado

- Dados spot de 1h da Binance, com contexto dos três ativos.
- 12 datasets point-in-time foram construídos: quatro braços para cada ativo.
- O braço `market` foi treinado para as duas famílias em cada ativo.
- Busca de até 30 configurações no braço de mercado.
- Cinco seeds finais: 11, 23, 37, 53 e 71.
- Custos-base de 24 bps por round trip e estresse de 48 bps.
- Walk-forward, purge/embargo, controles e verificação ONNX.
- O holdout `2025-08-01` a `2026-07-31` permaneceu fechado.

Os braços `market_onchain`, `market_sentiment` e `market_all` ainda não foram usados
para uma conclusão. Eles dependem de parâmetros de mercado congelados e serão tratados
em uma nova etapa, após a decisão metodológica descrita neste documento.

## Resultados observados

As métricas abaixo são do único teste walk-forward pré-holdout disponível, não do
holdout. Percentuais são retornos líquidos; “estresse” usa custos dobrados.

| Ativo | Família | Busca/calibração | Retorno | Sharpe | Sortino | Drawdown | Profit factor | Trades | Estresse |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| BTC | Random Forest | 30/30 rejeitados | — | — | — | — | — | — | — |
| BTC | Transformer | melhor candidato rejeitado na seed 23 | — | — | — | — | — | — |
| ETH | Random Forest | 30/30 rejeitados | — | — | — | — | — | — | — |
| ETH | Transformer | 30 elegíveis; 5 seeds passaram a calibração | 1,03% | 5,05 | 16,55 | 0,24% | 14,07 | 5 | 0,79% |
| SOL | Random Forest | 3 trials rejeitados; candidato concluído | −0,40% | −1,54 | −0,47 | 1,07% | 0,68 | 7 | −0,73% |
| SOL | Transformer | 1 trial rejeitado; 5 seeds concluídas | 0,64% | 3,83 | 0,88 | 0,64% | 2,35 | 6 | 0,49% |

### BTC

O Random Forest não encontrou uma única configuração que gerasse atividade suficiente
na calibração. O Transformer encontrou configurações elegíveis na busca, mas o melhor
candidato falhou quando a arquitetura foi repetida na seed 23. BTC não tem candidato
robusto nesta leva.

### ETH

O Transformer foi o resultado mais forte em retorno ajustado a risco, mas o teste teve
somente cinco trades. Nas cinco seeds, o comportamento variou de zero trades a 16 trades;
uma seed teve o menor erro de validação em um diagnóstico anterior, mas não o melhor
resultado econômico. Isso mostra por que loss preditivo não pode ser o único critério.

### SOL

O Random Forest perdeu dinheiro e também perdeu para o buy-and-hold escalado ao risco.
O Transformer fez 0,64% no teste e superou modestamente o buy-and-hold escalado, que fez
0,37%, mas teve apenas seis trades. Uma das cinco seeds teve retorno negativo de 0,49% e
o desvio do Sortino entre seeds foi alto. É um candidato de pesquisa, não um modelo pronto.

## Limitações e causas prováveis

### 1. Histórico contínuo curto demais

Foram identificados gaps reais de mercado compartilhados pelos três pares. A política
conservadora removeu o trecho até `2023-03-24 14:00 UTC`. Com janela de 24 meses de treino,
3 meses de calibração e 1 mês de teste antes do holdout, restou somente um fold de
desenvolvimento. Um único mês não mede estabilidade por regime.

### 2. Barreira econômica e baixa frequência

O custo mínimo é 24 bps por round trip. O RF frequentemente produziu previsões menores
que essa barreira, então 30 configurações foram corretamente rejeitadas. Quando o
Transformer negociou, a exposição foi muito pequena e o número de trades ficou entre
2 e 16 no mês de teste.

### 3. Sinal preditivo fraco

Os resultados de Spearman e acerto direcional ficaram próximos do acaso em vários casos.
Uma regressão de retorno normalizado pode estar tentando estimar uma grandeza ruidosa
demais para virar uma decisão long/flat depois de custos.

### 4. Instabilidade entre seeds

ETH e SOL mostraram grandes diferenças de trades, retorno e Sortino entre seeds. O modelo
aprende políticas diferentes a partir de pequenas alterações de inicialização, sinal de
que a vantagem não está bem identificada.

### 5. Seleção em amostra pequena

Sharpe e Sortino altos com cinco ou seis trades são estatisticamente frágeis. Não houve
evidência suficiente para justificar a abertura do holdout ou um campeão econômico.

### 6. Complexidade computacional

Alguns trials de Random Forest levaram vários minutos, enquanto Transformers usaram a
GPU de forma estável. O custo não causou a perda financeira, mas limita o orçamento de
busca e o número de refits possíveis.

### O que não foi causa

- Não foi detectado leakage temporal.
- O purge/embargo foi aplicado.
- A GPU e o treinamento determinístico funcionaram.
- ONNX coincidiu dentro da tolerância.
- Os testes automatizados permaneceram verdes.
- Nenhuma ordem real foi enviada.

## Proposta para o próximo protocolo

Esta seção é uma proposta para discussão. Ela não altera retroativamente o protocolo v1.
Antes de qualquer novo holdout, deve ser registrada como v2 e commitada.

### Meta de frequência

O primeiro objetivo realista será **aproximadamente um trade fechado por dia no
portfólio BTC/ETH/SOL**, ou cerca de 20–25 trades por mês. Isso não significa forçar uma
operação diária: se nenhum sinal líquido superar o custo e o risco, o sistema permanece
em caixa. A frequência será uma métrica explícita, não um motivo para reduzir
artificialmente o threshold abaixo dos custos.

Gates sugeridos para v2:

- registrar trades/dia, horas qualificadas, exposição e turnover por ativo e portfólio;
- exigir pelo menos 60 trades no portfólio durante os 3 meses de calibração;
- exigir pelo menos 20 trades no portfólio em cada mês de teste, quando o fold tiver um
  mês completo;
- manter o gate final de 100 trades no paper oficial;
- exigir resultado positivo com custos dobrados e desempenho superior aos controles.

### Dados e validação

1. Criar folds gap-aware, mantendo somente segmentos contínuos e buscando pelo menos
   três folds pré-holdout. Se isso não for possível, classificar a próxima rodada como
   piloto e não abrir o holdout.
2. Medir estabilidade por regime e por seed antes de comparar famílias.
3. Não escolher threshold, feature, arquitetura ou frequência usando o holdout.
4. Reavaliar o valor incremental de on-chain e sentimento somente depois que o braço
   `market` tiver uma arquitetura congelada.

### Modelagem e sinal

1. Testar um modelo em dois estágios: probabilidade de direção e magnitude/retorno
   condicional, com calibração purgada.
2. Testar ranking dos três ativos por retorno líquido esperado, selecionando apenas o
   melhor sinal horário quando houver edge suficiente. Isso pode aumentar a frequência
   do portfólio sem obrigar cada ativo a operar todos os dias.
3. Testar horizontes alternativos, como 6h e 12h, em protocolo separado; o alvo de 3h
   não deve ser trocado depois de observar resultados.
4. Para o Transformer, pré-registrar regularização e eventual ensemble de seeds somente
   se o custo computacional for aceitável.
5. Para o RF, reduzir busca improdutiva e registrar limites de tempo/memória sem
   transformar timeout em um falso resultado positivo.

### Ordem de execução recomendada

1. Commitar a emenda v2 e o diagnóstico de folds/frequência.
2. Reconstruir datasets/folds sem abrir o holdout.
3. Repetir primeiro o braço `market` com os novos gates de atividade.
4. Executar ablações somente com parâmetros de mercado congelados.
5. Comparar contra cash, buy-and-hold ajustado ao risco, médias móveis e Ridge.
6. Só se houver estabilidade, frequência e custos aprovados, criar o lock de seleção e
   abrir o holdout.
7. Depois do holdout: canário de 14 dias, paper oficial de 183 dias e nova avaliação.

## Decisão

Esta primeira leva fica oficialmente classificada como **resultado negativo/inconclusivo**.
Ela não justifica capital real, canário ou paper oficial. O resultado útil foi identificar
que a representação atual não produz sinais frequentes e estáveis, além de revelar que a
validação precisa de mais folds contínuos. O próximo treinamento deve atacar essas causas
com uma emenda explícita, preservando este registro como referência e sem reescrever os
resultados observados.

## Rastreabilidade local

Os artefatos gerados são mantidos fora do Git por política de tamanho e dados derivados.
Os registros principais desta rodada são:

- ETH/Transformer: `artifacts/experiments/ETHUSDT/market/transformer/146c32882c006976/experiment.json`;
- SOL/Random Forest: `artifacts/experiments/SOLUSDT/market/random_forest/150bd7c87c797794/experiment.json`;
- SOL/Transformer: `artifacts/experiments/SOLUSDT/market/transformer/296e7643ae3e9f9a/experiment.json`;
- rejeição de seed do BTC/Transformer: `artifacts/experiments/BTCUSDT/market/transformer/rejections/f05bf655288bd324.json`.

As execuções oficiais foram feitas com árvore Git limpa. A implementação de registro
formal de buscas inteiramente rejeitadas foi adicionada posteriormente e vale para novas
execuções; os resultados legados de BTC/ETH permanecem descritos aqui exatamente como
observados nos logs da rodada original.
