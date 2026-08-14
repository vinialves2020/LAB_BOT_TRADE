# Deploy Cloud Run + Neon

## Arquitetura operacional

- Três Cloud Run Jobs em `us-central1`: `signal`, `risk` e `daily`.
- Um Cloud Run Service privado, scale-to-zero e `max-instances=1` para Streamlit.
- Três Cloud Scheduler jobs UTC chamando a API v2 `jobs:run` com OAuth.
- Bucket privado e versionado logicamente para bundles ONNX.
- Neon Postgres contém apenas ledger/auditoria operacional.
- Quatro segredos: URL do banco, token/chat Telegram e senha do dashboard.
- Quatro identidades separadas: runtime, dashboard, scheduler e publisher.

## Pré-requisitos

- Projeto Google Cloud com billing habilitado, `gcloud`, Docker e Terraform.
- Banco Neon e URL `postgresql+psycopg://...?sslmode=require`.
- Bot/chat Telegram.
- Champion e fallback aprovados no holdout dos três ativos.
- Identidade humana definida em `dashboard_invoker_email`, no formato `user:nome@dominio`.

## Ordem segura de implantação

1. Copiar `infra/terraform/terraform.tfvars.example` para `terraform.tfvars`; não colocar segredos no arquivo.
2. Inicializar e revisar:

       terraform -chdir=infra/terraform init
       terraform -chdir=infra/terraform validate
       terraform -chdir=infra/terraform plan

3. Criar inicialmente APIs, Artifact Registry, bucket e objetos Secret Manager. O script `infra/deploy.ps1` faz esse bootstrap de forma direcionada.
4. Adicionar versões por stdin, sem valor literal no histórico:

       $value | gcloud secrets versions add bottrade-database-url --data-file=-

   Repetir para `bottrade-telegram-bot-token`, `bottrade-telegram-chat-id` e `bottrade-dashboard-password`.
5. Construir/publicar uma tag imutável e aplicar Terraform completo:

       .\infra\deploy.ps1 -ProjectId PROJECT -DashboardInvokerEmail "user:nome@dominio" -ImageTag "runtime-YYYYMMDD-SHA"

6. Conceder à identidade de publicação local o direito de impersonar apenas `bottrade-publisher@PROJECT.iam.gserviceaccount.com`; não baixar chave JSON. Configurar ADC por impersonation e publicar champion/fallback/challenger:

       bottrade models publish --asset BTCUSDT --slot champion --bucket PROJECT-bottrade-models

7. Executar `bottrade paper canary-start`, chamar cada job manualmente e conferir Neon, Telegram e reconciliação. `schedulers_paused=true` é o default do Terraform.
8. Depois da assinatura, alterar `schedulers_paused=false`, revisar o plan e aplicar. Antes de encerrar o paper, voltar para `true` para impedir uma execução posterior à fase.

O deploy usa uma imagem comum, mas o import da CLI operacional não carrega PyTorch, scikit-learn, SHAP, Captum ou Optuna. Treino e refit permanecem locais.

## Menor privilégio

- `bottrade-runtime`: lê objetos do bucket e acessa somente banco + Telegram.
- `bottrade-dashboard`: acessa somente banco + senha do dashboard.
- `bottrade-scheduler`: possui `roles/run.invoker`; não lê banco, bucket ou segredos.
- `bottrade-publisher`: `roles/storage.objectAdmin` apenas no bucket de modelos.
- O bucket tem uniform access, prevenção de acesso público e não pode ser destruído à força.
- O dashboard não recebe `allUsers`; IAM do Cloud Run e senha de aplicativo são camadas independentes.

Para acesso local ao serviço privado, usar um proxy autenticado, por exemplo `gcloud run services proxy bottrade-dashboard --region us-central1`, e então abrir a porta local exibida. Uma URL privada do Cloud Run não envia automaticamente um ID token ao ser colada no navegador.

## Custo e free tier

O objetivo é custo zero, não uma garantia. Conforme a tabela atual do [Cloud Run](https://cloud.google.com/run/pricing), Jobs têm franquia mensal de 240.000 vCPU-segundos e 450.000 GiB-segundos, baseada nos preços de `us-central1`, e cada execução é faturada por no mínimo um minuto. Com as três agendas deste projeto, um mês de 31 dias gera até 3.751 execuções e um piso de 225.060 vCPU-segundos: sobra pouca margem para jobs com mais de um minuto, retries e uso do dashboard.

O [Cloud Scheduler](https://cloud.google.com/scheduler/pricing) oferece três jobs gratuitos por billing account; este desenho consome exatamente os três. O plano Free atual do [Neon](https://neon.com/pricing) informa 100 CU-hours por projeto/mês, 0,5 GB e scale-to-zero, sem SLA.

Medidas obrigatórias:

- Budget de USD 1 com alertas em 50%, 90% e 100% quando `billing_account_id` é informado.
- Quotas de invocação e `max-instances=1`.
- Dashboard fechado quando não estiver em uso.
- Revisão mensal de billing e duração p95 dos jobs.
- Alertas de orçamento não são hard caps e podem chegar depois do consumo.

## Schedules e execução manual

Os schedules são `2 * * * *`, `*/15 * * * *` e `15 0 * * *`, todos em UTC. A chamada oficial de um job usa:

    POST https://run.googleapis.com/v2/projects/PROJECT/locations/REGION/jobs/JOB:run

Essa forma segue a documentação de [execução de Cloud Run Jobs](https://cloud.google.com/run/docs/execute/jobs). O Scheduler usa a service account própria e escopo `cloud-platform`.

## Neon e migração

Na primeira conexão, `Storage.initialize` cria o schema e registra sua versão. Atualizações aditivas conhecidas são aplicadas de forma idempotente. Antes de atualizar imagem ou refit:

1. Fazer backup lógico/branch no Neon.
2. Executar a nova imagem contra um banco de staging.
3. Rodar `paper reconcile`.
4. Só então trocar a imagem dos jobs.

## Publicação, rollback e retenção

`models publish` envia o diretório versionado antes de atualizar o ponteiro do slot. Runtime baixa o ponteiro, os blobs e revalida SHA-256. Para rollback, promover/publicar uma versão ONNX anterior sem sobrescrever seu diretório. Se o schema mudou, usar também a imagem compatível.

O lifecycle do bucket remove objetos após 730 dias para conter custo; relatórios finais e bundles acadêmicos que precisem de retenção maior devem ser exportados antes desse prazo para arquivo controlado.
