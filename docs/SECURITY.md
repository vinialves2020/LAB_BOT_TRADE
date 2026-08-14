# Segurança

## Limite estrutural

Não há método para criar ordem real, endpoint autenticado de exchange ou campo de API key Binance. As integrações Binance são somente leitura pública.

## Segredos

- DATABASE_URL, token/chat Telegram e senha do dashboard ficam em Secret Manager ou variáveis locais ignoradas pelo Git.
- Nunca incluir segredo em YAML versionado, imagem, log, model metadata ou Terraform state.
- Alertas Telegram de exceção enviam somente a classe da falha; mensagens arbitrárias de bibliotecas não são encaminhadas ao chat.
- Identidades são separadas: runtime lê modelos e segredos operacionais; dashboard lê banco/senha; scheduler apenas invoca jobs; publisher apenas grava no bucket.
- Publicação local deve usar impersonation/ADC; não criar ou baixar chave JSON de service account.
- Bucket bloqueia acesso público.

## Artefatos

- Modelo implantado precisa ser ONNX verificado.
- Ponteiro referencia versão imutável; o runtime revalida checksum SHA-256 após hidratar o bundle.
- Schema/lista ordenada de features acompanha o modelo.
- Pickle/joblib e state_dict existem apenas no laboratório local; runtime não os carrega.

## Banco

- Neon deve exigir TLS (`sslmode=require`).
- O dashboard é read-only no código de interface.
- O serviço Cloud Run exige IAM e a interface exige uma segunda senha; acesso por navegador deve passar por proxy autenticado.
- Rotacionar credenciais após suspeita ou exposição.
- Backups/exportações do ledger não devem conter segredos.

## Nuvem gratuita

`max-instances=1`, `task_count=1` e `parallelism=1` limitam fan-out. Budget de USD 1 é alerta, não hard cap. Revisar faturamento, duração e quotas semanalmente durante o canário.

## Futuro dinheiro real

Fica explicitamente fora do escopo. Exigiria outro repositório/adaptador, infraestrutura paga com SLA, subconta, chave sem saque, allowlist de IP, revisão legal/tributária, threat model e autorização humana independente.
