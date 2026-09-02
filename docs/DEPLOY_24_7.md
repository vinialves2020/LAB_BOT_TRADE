# Guia de Deploy 24/7 (Custo R$ 0,00)

Este guia explica como colocar o **BOT_TRADE V5** rodando 24 horas por dia, 7 dias por semana, sem gastar nada, aproveitando sua **Conta de Estudante do GitHub (Student Pack)** e sua conta **Google**.

---

## Comparativo de Opções Disponíveis

| Método | Onde Roda | Como Funciona | Custo | Dificuldade | Recomendação |
|---|---|---|:---:|:---:|:---:|
| **Opção 1: GitHub Actions (Cron)** | Nuvem do GitHub | Dispara a cada 1 hora no fechamento da vela de 1h (`0 * * * *`), roda o ciclo e salva o ledger | **R$ 0,00** (Incluído no GitHub) | ⭐ Muito Fácil (Já configurado!) | 🥇 **Ideal para começar agora** |
| **Opção 2: DigitalOcean VPS (Student Pack)** | Servidor Linux (Ubuntu) | Droplet de $4-$6/mês rodando o bot contínuo (`bottrade.service`) ou Docker | **R$ 0,00** ($200 em créditos por 1 ano) | ⭐⭐ Médio | 🥈 **Melhor para servidor dedicado** |
| **Opção 3: Microsoft Azure for Students** | VM Linux na Azure | Máquina B1s rodando 24/7 com créditos de estudante | **R$ 0,00** ($100 em créditos sem cartão) | ⭐⭐ Médio | 🥉 Alternativa à DigitalOcean |
| **Opção 4: Google Cloud (GCP Always Free)** | Cloud Run / e2-micro | Cloud Run Jobs com Cloud Scheduler (já temos Terraform no projeto) ou VM e2-micro | **R$ 0,00** (Always Free Tier) | ⭐⭐⭐ Avançado | Excelente para arquitetura serverless |

---

## Opção 1: GitHub Actions (Iniciar em 2 minutos, zero infraestrutura)

Como o bot de trading opera em velas de 1 hora, ele só precisa acordar a cada 60 minutos para processar o sinal e registrar ordens.

Já criamos o arquivo [`.github/workflows/paper_trade_cron.yml`](file:///.github/workflows/paper_trade_cron.yml).

### Como ativar:
1. Faça `git add .`, `git commit -m "feat: adicionar workflow paper trading"` e `git push origin main`.
2. Acesse seu repositório no GitHub: `https://github.com/vinialves2020/LAB_BOT_TRADE/actions`.
3. Você verá o workflow **"Paper Trading V5 (24/7 Hourly Engine)"**.
4. (Opcional) Para receber notificações instantâneas no celular, adicione as secrets `TELEGRAM_BOT_TOKEN` e `TELEGRAM_CHAT_ID` nas configurações do repositório (`Settings > Secrets and variables > Actions`).
5. Pronto! Ele executará automaticamente a cada hora, de graça, na nuvem do GitHub.

---

## Opção 2: DigitalOcean VPS com $200 do GitHub Student Pack

O GitHub Student Developer Pack dá **$200 de crédito na DigitalOcean** válidos por 1 ano.

### Passo a passo:
1. Acesse o portal do [GitHub Student Developer Pack](https://education.github.com/pack).
2. Resgate o benefício da **DigitalOcean** (ele gerará um cupom ou link de ativação).
3. Na DigitalOcean, crie um **Droplet**:
   - Imagem: **Ubuntu 24.04 LTS**
   - Plano: **Basic (Regular)** -> $4/mês ou $6/mês (1 vCPU, 1 GB RAM, 25 GB SSD).
   - Região: New York ou Frankfurt.
   - Autenticação: Chave SSH ou Senha root.
4. Conecte no terminal da VPS:
   ```bash
   ssh root@SEU_IP
   ```
5. Clone e instale o bot:
   ```bash
   git clone https://github.com/vinialves2020/LAB_BOT_TRADE.git
   cd LAB_BOT_TRADE
   sudo apt update && sudo apt install -y python3-pip python3-venv git
   python3 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install ".[ml]"
   ```
6. Inicialize o banco SQLite:
   ```bash
   bottrade paper init
   ```
7. Ative o serviço 24/7 com systemd:
   ```bash
   sudo cp infra/bottrade.service /etc/systemd/system/bottrade.service
   # Ajuste o usuário no arquivo se necessário
   sudo systemctl daemon-reload
   sudo systemctl enable --now bottrade
   ```
8. Para acompanhar os logs em tempo real na VPS:
   ```bash
   sudo journalctl -u bottrade -f
   # ou
   tail -f /var/log/bottrade.log
   ```

---

## Opção 3: Google Cloud (GCP) com o Terraform Existente

Se você preferir usar sua conta Google:
- O Google Cloud possui a camada **Always Free**, que disponibiliza:
  - 1 instância de VM `e2-micro` gratuita por mês (em `us-central1`, `us-east1` ou `us-west1`).
  - 2 milhões de requisições gratuitas no Cloud Run + 3 jobs no Cloud Scheduler.
- O projeto já possui a pasta [`infra/terraform`](file:///infra/terraform) pronta para provisionar essa infraestrutura serverless caso deseje seguir o padrão de nuvem corporativa (conforme documentado em [`docs/CLOUD.md`](file:///docs/CLOUD.md)).
