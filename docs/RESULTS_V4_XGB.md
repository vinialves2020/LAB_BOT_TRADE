# Resultados V4 — XGBoost cost-aware

Data de execução: 20/08/2026. Todas as rodadas abaixo são pré-holdout. O
período `2025-08-01`–`2026-07-31` não foi usado como teste de seleção nem como
fonte de labels de treino.

## V4-base: alvo de 12h

Configuração: Pseudo-Huber, cinco seeds, entradas independentes, saída fixa em
12h, mercado 1h + estatísticas 15m, 12 folds mensais de agosto/2024 a
julho/2025.

| Ativo | Trades | Média trades/mês | Retorno líquido | Sharpe | Drawdown | PF | Retorno com 48 bps |
|---|---:|---:|---:|---:|---:|---:|---:|
| BTCUSDT | 158 | 14,36 | -7,43% | -0,10 | 27,27% | 0,98 | -37,14% |
| ETHUSDT | 301 | 25,08 | -29,08% | -0,50 | 56,42% | 0,94 | -64,09% |
| SOLUSDT | 267 | 22,25 | -5,19% | 0,40 | 34,15% | 1,04 | -26,62% |

Conclusão: reprovada nos três ativos. O modelo superestimava retornos: nos
trades selecionados de BTC a previsão média ficou perto de 78 bps, enquanto o
retorno bruto realizado ficou perto de 23 bps, insuficiente para pagar 24 bps.

## V4.1: alvo de uma hora

Configuração: MSE, cinco seeds, posição persistente long/flat, filtro de custo
na mudança de posição, saída por previsão negativa ou 12h. A revisão foi
registrada em `PROTOCOL_V4_1_XGB_HOURLY.md` antes da execução.

| Ativo | Trades | Média trades/mês | Retorno líquido | Sharpe | Drawdown | PF | Retorno com 48 bps |
|---|---:|---:|---:|---:|---:|---:|---:|
| BTCUSDT | 47 | 5,88 | +26,44% | 4,83 | 9,37% | 1,73 | +8,46% |
| ETHUSDT | 109 | 9,08 | -19,23% | -0,79 | 45,71% | 0,91 | -16,58% |
| SOLUSDT | 59 | 4,92 | +25,86% | 2,45 | 16,58% | 1,38 | -22,13% |

Conclusão: há sinal aparente em BTC e SOL com custo-base, mas nenhum ativo
passa todos os gates. BTC ainda excede o drawdown de 8% e tem baixa frequência;
SOL perde com custos dobrados; ETH falha em retorno, risco e estabilidade.

## Decisão

- Nenhum artefato V4/V4.1 foi promovido.
- O holdout não foi aberto.
- Nenhum canário ou paper foi iniciado.
- XGBoost não pode ser declarado “pronto” para dinheiro real.
- A diferença entre V4-base e V4.1 confirma que o alvo e a política de execução
  são tão importantes quanto a família do modelo.

O próximo estudo, se mantido, deve ser explicitamente um novo protocolo. Não é
permitido escolher outra janela, objetivo ou custo depois de olhar esses
resultados e ainda chamar a comparação de pré-registrada.
