# Critérios de aceite V3

Este arquivo é o checklist operacional antes de qualquer abertura do holdout.
O estado atual é pré-holdout: nenhum comando de desenvolvimento pode ler ou
usar `2025-08-01` a `2026-07-31`.

## Gates econômicos

- [ ] pelo menos 240 trades no holdout por ativo e 120 no paper de seis meses;
- [ ] média de 20 trades/mês e piso de 10 em cada mês completo;
- [ ] retorno líquido positivo com custo-base e custo dobrado;
- [ ] Sharpe diário HAC anualizado ≥ 1,0 e limite inferior do bootstrap > 0;
- [ ] profit factor ≥ 1,2;
- [ ] drawdown máximo ≤ 8%;
- [ ] DSR ≥ 0,95 e PBO ≤ 0,20;
- [ ] quatro das cinco seeds com retorno não negativo e nenhuma com drawdown > 8%;
- [ ] superioridade ajustada ao risco contra caixa, buy-and-hold, médias e Ridge;
- [ ] ambos os ledgers sem violação de risco.

Um gate faltante reprova o ativo e mantém sua posição em caixa. A frequência
nunca é obtida forçando operações.

## Gates de dados e segurança

- [ ] fontes oficiais com checksum e manifesto de schema;
- [ ] timestamps UTC e parser de milissegundos/microssegundos validados;
- [ ] nenhum gap interpolado e nenhuma sequência atravessa segmento;
- [ ] purge/embargo de 12h em todos os folds;
- [ ] calibração cronológica fora da amostra;
- [ ] duplicidade, candle incompleto, banco/modelo inválido e relógio divergente
      bloqueiam novas posições;
- [ ] ONNX de cada membro coincide com o artefato nativo dentro de `1e-4`;
- [ ] seleção registrada em lock imutável antes do holdout.

## Comandos reproduzíveis

```powershell
bottrade v3 preflight --config config/v3.yaml
bottrade v3 features --asset BTCUSDT --output data/processed/v3/BTCUSDT/features.parquet
bottrade v3 candidates --asset BTCUSDT --features data/processed/v3/BTCUSDT/features.parquet --output data/processed/v3/BTCUSDT/candidates.parquet
bottrade v3 labels --candidates data/processed/v3/BTCUSDT/candidates.parquet --intrahour data/raw/market/BTCUSDT_15m.parquet --output data/processed/v3/BTCUSDT/labels.parquet
bottrade v3 deterministic --labels data/processed/v3/BTCUSDT/labels.parquet --output-dir reports/generated/v3/BTCUSDT/deterministic
bottrade v3 gates --metrics reports/generated/v3/BTCUSDT/deterministic/metrics.json --trades reports/generated/v3/BTCUSDT/deterministic/trades_1x.parquet
bottrade v3 meta-train --asset BTCUSDT --family hist_gradient_boosting --features data/processed/v3/BTCUSDT/features.parquet --candidates data/processed/v3/BTCUSDT/candidates.parquet --labels data/processed/v3/BTCUSDT/labels.parquet --output-dir reports/generated/v3/BTCUSDT/hgb
```

O smoke-test usa `--params-json` explicitamente e não é elegível para
promoção. A abertura do holdout só pode ocorrer com:

```powershell
bottrade v3 holdout --lock reports/generated/v3/selection-lock.json --confirm OPEN-V3-HOLDOUT
```

Sem a confirmação exata, o comando falha fechado.
