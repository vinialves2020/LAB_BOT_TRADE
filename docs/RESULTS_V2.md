# Resultado formal da V2

Data da execução: 18/08/2026 UTC.

## Decisão

A V2 foi encerrada como resultado negativo/inconclusivo. Nenhum modelo foi
promovido, o holdout de `2025-08-01` a `2026-07-31` não foi aberto, nenhum
canário foi iniciado e nenhum ledger paper recebeu sinais oficiais.

O resultado é válido para a configuração V2 testada. Ele não prova que não
existe nenhuma estratégia possível para BTC, ETH ou SOL.

## O que foi executado

- Dados oficiais Binance spot em 1h e 15m para BTCUSDT, ETHUSDT e SOLUSDT.
- Checksums, manifests, segmentos de continuidade e purge/embargo de 12h.
- Labels cost-aware em 3h, 6h e 12h.
- Braços de mercado, intrahora, derivativos, on-chain e sentimento.
- Random Forest, HistGradientBoosting e Transformer temporal.
- Calibração cronológica, seleção de horizonte, custos base e dobrados.
- Auditorias OOS em até 31 folds de desenvolvimento.
- DSR/PBO, ONNX, falhas operacionais e testes de reprodutibilidade.

## Resultados principais

- O lote diagnóstico executou 37 avaliações e todas foram rejeitadas por
  política de calibração/frequência.
- A auditoria HGB completa permaneceu negativa fora da amostra:
  - BTC: retorno de teste `-7,09%`, Sharpe `-1,75`, profit factor `0,64`.
  - ETH: retorno de teste `-3,25%`, Sharpe `-0,42`, profit factor `0,91`.
  - SOL: retorno de teste `-19,11%`, Sharpe `-1,64`, profit factor `0,78`.
- O Transformer apresentou pequena vantagem diagnóstica em BTC e SOL, mas
  continuou negativo, instável e abaixo dos gates.
- AUCs ficaram próximas de 0,50–0,58, sem evidência de discriminação forte.
- Relaxar a frequência aumentou trades, mas não produziu resultado líquido
  positivo ou profit factor acima de 1.

## Causas prováveis

1. O modelo tentava prever diretamente retornos horários muito ruidosos.
2. O custo de 24–54 bps filtrava grande parte dos movimentos curtos.
3. A exigência de 20 trades por mês por ativo e piso mensal era excessiva.
4. O modelo precisava descobrir simultaneamente entrada, regime, tamanho e
   horizonte.
5. O alvo de fechamento futuro não representava bem a trajetória até uma
   saída com stop, alvo e custo.
6. Derivativos sem histórico verificável não forneceram sinal retrospectivo.

## Consequência metodológica

A próxima rodada deverá gerar oportunidades com estratégias determinísticas
de tendência, reversão e breakout. RF, HistGradientBoosting e Transformer
serão meta-modelos para filtrar essas oportunidades e estimar retorno líquido,
em vez de descobrirem toda a estratégia diretamente dos candles.

A frequência será avaliada no portfólio, sem obrigar cada ativo a operar todos
os meses. O holdout continuará fechado até que o novo protocolo esteja
pré-registrado e o lock de seleção seja criado.

## Reprodução

O relatório detalhado permanece em
`reports/generated/V2_BATCH_ANALYSIS.md`. A configuração está em
`config/v2.yaml`, e os testes V2 devem continuar passando com:

```powershell
python -m pytest -q
```

Nenhuma função de envio de ordens reais foi criada ou executada.
