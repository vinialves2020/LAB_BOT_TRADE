# 🧠 Cerne do Projeto, Estratégias e Modelos de Machine Learning

Este documento detalha os fundamentos quantitativos, a matemática dos modelos preditivos e os filtros de microestrutura de mercado implementados no **BOT_TRADE V5.1**.

---

## 1. O Confronto de Arquiteturas: RF × Transformer × XGBoost

O laboratório colocou em confronto três grandes famílias de aprendizado de máquina para modelagem temporal de ativos cripto (`BTCUSDT`, `ETHUSDT`, `SOLUSDT`):

| Arquitetura | Características Técnicas | Comportamento Empírico no Mercado | Veredito |
|---|---|---|:---:|
| **Random Forest (`RFEnsemble`)** | 100 árvores com *subbagging* de 50%, feature subsampling (0.4) e paralelização multi-core. | Alta estabilidade ($IC > 0{,}04$), porém a média simples das árvores (*bagging*) atenua as caudas da distribuição (*shrinkage* excessivo), raramente superando a barreira de custo de 24 bps em spot. | 🥈 Modelo secundário (bom para filtros conservadores) |
| **PatchTransformer (`PatchTST`)** | Encoder de Transformers com patching temporal (janela 6, stride 3), RevIN (Normalização Reversível de Instâncias) acelerado via **CUDA 12.8**. | Aprende padrões temporais complexos, mas a perda MSE/Huber penaliza previsões extremas, convergindo para previsões médias próximas de zero após custos. | 🥉 Requer horizontes mais longos ou derivativos de alta alavancagem |
| **XGBoost Institucional (`XGBoostEnsemble`)** | Gradient Tree Boosting com árvores rasas (depth 4), subsample (0.8), shrinkage e regularização L2. | **O Grande Vencedor**: Ajusta diretamente os resíduos das caudas, disparando apenas quando a assimetria esperada supera o limiar de custo com margem estatística favorável. | 🏆 **Campeão Oficial de Produção** |

---

## 2. Estratégias Quantitativas Institucionais Implementadas

### A. Cumulative Volume Delta (CVD) e Divergências de Fluxo
Em mercados centralizados como a Binance, a movimentação de preço muitas vezes é induzida por pavios de baixa liquidez. O CVD mede o saldo líquido entre compras a mercado (*taker buy*) e vendas a mercado (*taker sell*):
- **CVD Multi-Horizonte**: Medido em janelas de 3h, 6h e 24h (`cvd_ratio_3h`, `cvd_ratio_6h`, `cvd_ratio_24h`).
- **Divergência Preço × CVD**: Identifica quando o preço faz novas mínimas, mas o delta de agressão vendedora é absorvido por ordens passivas (divergência compradora de reversão).

### B. Features Cíclicas de Sessões e Liquidez
O mercado cripto opera 24/7, mas os fluxos institucionais concentram-se na sobreposição dos mercados de Londres e Nova York:
- **Janela de Alta Liquidez (Londres/NY)**: Flag ativada entre 12:00 e 20:00 UTC.
- **Flag de Fins de Semana**: Períodos de livro fino e ruído lateral.
- **Decomposição Trigonométrica**: $\sin/\cos$ de hora do dia e dia da semana para capturar sazonalidade sem descontinuidades abruptas.

### C. Gestão de Risco e Saída Adaptativa por Volatilidade
Em vez de stops percentuais estáticos (que são frequentemente caçados em dias de alta volatilidade e muito largos em dias calmos), os stops são parametrizados pela **volatilidade EWMA horária ($\sigma_{1h}$)**:
- **Trailing Stop Dinâmico**: Ativa quando o lucro atinge $+2{,}0 \times \sigma_{1h}$. Trava $50\%$ do pico de lucro obtido se o preço recuar.
- **Hard Stop Loss Dinâmico**: Saída imediata de emergência se o ativo cair $-3{,}0 \times \sigma_{1h}$.

---

## 3. Blindagem de Regimes e Proteção Macro de Altcoins

A auditoria quantitativa inicial de 6 meses revelou que comprar altcoins (ETH e SOL) durante tendências de baixa macro gerava falsos rompimentos. Implementamos três filtros estruturais:

1. **Trava Macro do Bitcoin (`btc_dumping`)**:
   - Se o Bitcoin estiver em queda abrupta nas últimas 24h ($< -1{,}8\%$), **nenhuma nova compra é autorizada em ETH ou SOL**.
2. **Filtro de Tendência Estrutural (`own_in_downtrend`)**:
   - Se a altcoin estiver mais de $2{,}0\%$ abaixo da sua EMA semanal de 168h e o Bitcoin estiver em terreno negativo, o robô não tenta adivinhar fundo.
3. **Filtro de Range Lateral da Solana (`sol_sideways_filter`)**:
   - A Solana é um ativo de forte *momentum*. Se ela estiver oscilando lateralmente dentro de $\pm 2{,}5\%$ da EMA de 72h, novas compras são bloqueadas, evitando pavios e armadilhas de liquidez.

---

## 4. Bateria Anti-Overfitting

Para assegurar que o modelo não sofre de ajuste à curva (*curve fitting*):
- **Deflated Sharpe Ratio (DSR)**: Corrige o índice de Sharpe inflando a incerteza com base na assimetria (skewness), curtose e número de testes realizados.
- **Probability of Backtest Overfitting (PBO via CSCV)**: Utiliza Validação Cruzada Combinatória Simetricamente Purgada. O modelo obteve **PBO = 0.0%** (zero indício estatístico de overfitting).
- **Resiliência a Taxas e Slippage**: O portfólio permanece lucrativo mesmo sob um teste de estresse de **72 bps por operação** (3x o custo taker normal da Binance).
