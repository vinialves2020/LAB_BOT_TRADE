# Fontes e dicionário de dados

## Binance

Campos de candle: open_time, open, high, low, close, volume, close_time, quote_volume, trade_count, taker_buy_base_volume e taker_buy_quote_volume.

Arquivos mensais são verificados pelo checksum publicado. Arquivo ausente usa REST público. Timestamps em microssegundos após a mudança da fonte são detectados por magnitude e normalizados para UTC.

Um candle entra no pipeline somente depois de `as_of = open_time + 1h`. A continuidade dos três mercados é validada antes de inferência; um gap em qualquer contexto bloqueia novas entradas naquele ciclo.

Na V2, os arquivos `*_15m.parquet` são sincronizados pela mesma rotina. Somente
as quatro barras encerradas até o fechamento horário são agregadas; falta de uma
das quatro barras vira indicador de completude, nunca preço interpolado.

Derivativos são exclusivamente informacionais: funding, premium, mark/index,
basis, volume/agressão e open interest quando o arquivo histórico oficial é
verificável. Endpoints que só expõem histórico recente ficam em shadow e não
entram no treino retrospectivo.

## Coin Metrics comunitária

BTC e ETH usam, inicialmente:

- AdrActCnt: endereços ativos.
- TxCnt: quantidade de transações.
- SplyCur: oferta corrente.

São features diárias com available_at = event_time + 24h. Alterações metodológicas do provedor permanecem uma limitação documentada.

## DefiLlama / Solana

- TVL do ecossistema.
- Oferta de stablecoins.
- Volume DEX.
- Taxas do ecossistema.

Esses campos medem atividade DeFi/ecossistema e não são equivalentes a endereço ativo ou transação de BTC/ETH.

## Alternative.me

Fear & Greed de 0 a 100. É geral, diário, centrado em Bitcoin e parcialmente composto por mercado. O braço mede valor incremental, não trata o índice como sentimento independente puro.

## Regras point-in-time

- Join sempre por `available_at <= as_of`, por merge as-of voltado para trás.
- Alternativos recebem atraso mínimo de 24h.
- Cada linha inclui `event_time`, `available_at`, idade, `missing` e `stale`.
- Idade superior a 72h obriga fallback market-only no runtime.
- Mercado com mais de 75 minutos sem último candle fechado bloqueia o job signal.
- O dataset bruto nunca é preenchido com preço sintético. A V1 preserva o corte
  após a última lacuna; a V2 mantém os trechos e grava `continuity_segment_id`.
  Uma amostra V2 só é válida se lookback, próximo open e horizonte máximo
  estiverem no mesmo segmento; qualquer gap recente continua bloqueando novas
  entradas.
- Infinitos viram missing; imputadores são ajustados apenas no treino.
- Uma falha ao buscar fonte alternativa não contamina a construção market-only; o runtime usa o fallback previamente congelado. Não existe substituição automática de fonte que altere o schema.

## Features de mercado

- Retornos de 1, 3, 6, 12, 24, 72 e 168h.
- Volatilidade EWMA de 24, 72 e 168h.
- Z-score de volume, range e número de negócios.
- Corpo/range do candle e razão compradora agressora.
- Contexto dos três ativos.
- Na V2, caminho intrahorário 15m, volatilidade realizada, range,
  drawup/drawdown, concentração/aceleração de volume, negócios e agressão.
- Seno/cosseno e índices de hora UTC/dia da semana. O Transformer transforma os índices em embeddings aprendidos; o RF recebe sua representação tabular.

## Labels

Na V1, retorno logarítmico entre a abertura do próximo candle e o fechamento
três horas adiante, dividido pelo desvio EWMA dos retornos horários
estritamente conhecidos. Na V2, o mesmo cálculo existe para 3h, 6h e 12h e
também gera a classe `retorno bruto > 24 bps`. A volatilidade usa janela dura
de 168 observações (`alpha = 2 / 169`) e não carrega memória de períodos
anteriores. O backtest usa retornos horários seguintes e aplica custo a cada
mudança de posição.

## Versionamento

Cada fonte registra período solicitado, URL, caminho, SHA-256, número de linhas, limites temporais, schema de colunas e horário de coleta. Os datasets processados preservam `event_time` e `available_at` prefixados por fonte para auditoria point-in-time. Cada dataset processado recebe hash de conteúdo e manifest próprio. O hash, a lista ordenada de features e a versão de schema (`features-v3` V1 ou `features-v4` V2) entram no metadata e na trava de seleção.

Datasets e versões de modelo são append-only para fins de auditoria. Uma mudança de metodologia do provedor, schema ou disponibilidade cria nova versão; ela não reescreve silenciosamente um experimento concluído.
