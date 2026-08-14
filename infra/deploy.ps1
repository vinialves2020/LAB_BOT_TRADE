param(
  [Parameter(Mandatory=$true)][string]$ProjectId,
  [Parameter(Mandatory=$true)][string]$DashboardInvokerEmail,
  [string]$Region = "us-central1",
  [string]$ImageTag = "runtime-v1",
  [string]$BillingAccountId = ""
)

$ErrorActionPreference = "Stop"
$Repository = "$Region-docker.pkg.dev/$ProjectId/bottrade"
$Image = "$Repository/runtime:$ImageTag"

Push-Location infra/terraform
terraform init
terraform apply `
  -target="google_project_service.required" `
  -target="google_artifact_registry_repository.images" `
  -target="google_storage_bucket.models" `
  -target="google_secret_manager_secret.runtime" `
  -var "project_id=$ProjectId" `
  -var "region=$Region" `
  -var "image=$Image" `
  -var "dashboard_invoker_email=$DashboardInvokerEmail" `
  -var "billing_account_id=$BillingAccountId"
Pop-Location

$RequiredSecrets = @(
  "bottrade-database-url",
  "bottrade-telegram-bot-token",
  "bottrade-telegram-chat-id",
  "bottrade-dashboard-password"
)
$MissingSecrets = @()
foreach ($SecretName in $RequiredSecrets) {
  $Versions = gcloud secrets versions list $SecretName --filter="state=ENABLED" --format="value(name)" 2>$null
  if (-not $Versions) { $MissingSecrets += $SecretName }
}
if ($MissingSecrets.Count -gt 0) {
  Write-Output "Secret versions missing: $($MissingSecrets -join ', ')"
  Write-Output "Add values through stdin as documented in docs/CLOUD.md, then rerun this script."
  exit 2
}

gcloud auth configure-docker "$Region-docker.pkg.dev" --quiet
docker build --pull --tag $Image .
docker push $Image
$Digest = gcloud artifacts docker images describe $Image --format="value(image_summary.digest)"
if (-not $Digest -or -not $Digest.StartsWith("sha256:")) {
  throw "Could not resolve the pushed Artifact Registry digest for $Image"
}
$PinnedImage = "$Repository/runtime@$Digest"

Push-Location infra/terraform
terraform apply `
  -var "project_id=$ProjectId" `
  -var "region=$Region" `
  -var "image=$PinnedImage" `
  -var "dashboard_invoker_email=$DashboardInvokerEmail" `
  -var "billing_account_id=$BillingAccountId"
Pop-Location

Write-Output "Image deployed: $PinnedImage"
Write-Output "Populate Secret Manager versions before allowing schedulers to run."
