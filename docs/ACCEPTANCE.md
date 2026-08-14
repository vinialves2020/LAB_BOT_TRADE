# Critérios de aceite

## Gates técnicos antes de experimento

- Lint e testes unitários/integrados locais passam.
- Manifests têm URL, período, schema e SHA-256 válidos.
- Nenhum candle futuro/incompleto e nenhum gap tratado como preço verdadeiro.
- Joins alternativos respeitam `available_at`; teste temporal prova ausência de forward fill futuro.
- Split walk-forward confirma purge/embargo e scalers treinados somente no passado.
- Mesma seed reproduz previsões dentro da tolerância numérica.

## Gates de candidato

- Oito candidatos oficiais por ativo: duas famílias × quatro braços.
- Braço `market` com 30 trials e ablações com parâmetros herdados.
- Cinco seeds independentes, métricas medianas e dispersão registradas.
- Custos, thresholds, giro e trades mínimos aplicados na calibração.
- Permutation importance para ambos; SHAP ou IG/ablação conforme família.
- `experiment.json`, model card e hashes completos.
- ONNX com erro absoluto máximo `1e-4` contra o modelo nativo.
- Seleção imutável criada antes de abrir o holdout.

## Golden replay e falhas

O replay automatizado cobre tendência de alta, queda, lateralização e alta volatilidade. Os testes de dataset cobrem gaps de mercado e fontes alternativas ausentes; antes do canário, repetir esses cenários contra a infraestrutura de staging e guardar a evidência no relatório.

Executar injeções controladas em staging:

- Binance indisponível, livro sem profundidade e relógio divergente: nenhuma nova compra.
- Banco falhando no segundo ledger: rollback atômico dos dois e reconciliação íntegra.
- Bundle ausente, checksum/schema inválido ou inferência não finita: caixa/fallback conforme regra, nunca exposição insegura.
- Telegram indisponível: ledger preservado e falha observável.
- Reinício após fill: IDs determinísticos não duplicam ordem; caixa, posição e equity reconciliam.

Guardar logs, horário, versão da imagem e evidência de cada cenário. Testes não substituem o ensaio contra Neon/Cloud Run de staging.

## Gates do canário

- 14 dias completos em fase `canary`.
- Três agendas executadas e monitoradas; retries não duplicam fills.
- Nenhum incidente crítico não resolvido.
- Ambos os ledgers reconciliam após reinício.
- Correções limitadas a defeitos operacionais; qualquer mudança de estratégia reinicia o protocolo.
- Relatório do canário exportado antes do reset.

## Gate final por ativo

O avaliador exige simultaneamente no holdout e nos dois ledgers do paper oficial:

- Sharpe diário anualizado ≥ 1,0.
- Drawdown máximo ≤ 8%.
- Profit factor ≥ 1,2.
- Pelo menos 100 trades fechados.
- Resultado líquido positivo sob o replay de custos dobrados.
- Desempenho ajustado a risco superior aos controles.
- Nenhum ledger atingiu daily stop, position stop ou circuit breaker.
- Últimos 90 dias sem incidente crítico.
- Fase oficial encerrada após pelo menos 183 dias.

`bottrade paper evaluate` retorna motivos por ativo e por ledger; `bottrade report` incorpora o mesmo resultado. Falha ou evidência insuficiente mantém o ativo em caixa.

## Entrega acadêmica

- Dashboard operacional e relatório técnico em português.
- Matriz RF × Transformer × braço × ativo.
- Model cards e versões ONNX.
- Métricas preditivas, P&L, custos, regimes, seeds, explicabilidade, latência e memória.
- Catálogo objetivo de forças/fraquezas e falhas observadas.
- Limitações e decisões posteriores explicitamente separadas dos resultados pré-registrados.

Aprovação não habilita capital real. Essa decisão requer nova infraestrutura paga, custódia/rotação de chaves, controles independentes, revisão legal/tributária e autorização humana explícita.
