# Protocolo V3 — estratégias determinísticas com meta-modelos

Este protocolo é aditivo à V1 e V2. A V2 continua congelada como resultado
negativo/inconclusivo em [RESULTS_V2.md](RESULTS_V2.md). O holdout
`2025-08-01`–`2026-07-31` permanece fechado até a criação de um lock de seleção.

## Mudança central

As estratégias de tendência, reversão e breakout geram candidatos long/flat.
Random Forest, HistGradientBoosting, Transformer e controles lineares filtram
os candidatos e estimam retorno líquido, em vez de descobrirem toda a política
diretamente de um retorno horário ruidoso.

## Frequência

A frequência é avaliada no portfólio. O alvo desejável é de 20–45 trades
fechados por mês, mas nenhum ativo é obrigado a operar em todos os meses.
Ativos sem evidência suficiente permanecem em caixa.

## Ordem de execução

```text
features → candidates → event labels → signal ceiling → meta-models
→ portfolio backtest → gates → selection lock → holdout → canary → paper
```

Todas as decisões usam 1h. Candles 15m servem para microestrutura, execução e
resolução de stop/alvo. Nenhum candle posterior a `as_of` entra nas features.

## Estratégias pré-registradas

- Tendência: EMA 6/24, 12/48 e 24/72 com confirmação de inclinação e retorno.
- Reversão: retorno extremo normalizado, drawdown intrahorário e recuperação no
  último candle de 15m.
- Breakout: rompimento da máxima anterior, volume acelerado, fechamento alto
  no range e compressão de volatilidade anterior.

As variantes e valores estão em `config/v3.yaml`. Não adicionar combinações
fora da configuração sem criar uma nova versão do protocolo.

## Labels

O evento começa no próximo open de 15m. O take-profit é custo de round trip
mais `0,75 × volatilidade × sqrt(h)`. O stop é `-1,0 × volatilidade × sqrt(h)`.
Se stop e alvo ocorrerem no mesmo candle, o stop vence. Gaps, horizontes
incompletos e amostras que cruzam o holdout são inválidos.

## Gates

O portfólio precisa ser líquido positivo com custos 1× e 2×, Sharpe HAC ≥ 1,
intervalo inferior do Sharpe positivo, profit factor ≥ 1,2, drawdown ≤ 8%,
DSR ≥ 0,95, PBO ≤ 0,20 e estabilidade em folds e seeds. Os mesmos sinais são
comparados com caixa, buy-and-hold ajustado ao risco, médias e Ridge.

Custos 3× são stress obrigatório para uma futura candidatura a capital, mas
nenhum gate autoriza capital real automaticamente.
