param(
    [ValidateSet("BTCUSDT", "ETHUSDT", "SOLUSDT")]
    [string]$Asset = "BTCUSDT",
    [ValidateSet("random_forest", "hist_gradient_boosting", "transformer")]
    [string]$Family = "hist_gradient_boosting",
    [string]$Config = "config/v3.yaml",
    [string]$Root = "data/processed/v3"
)

$ErrorActionPreference = "Stop"
$assetRoot = Join-Path $Root $Asset
New-Item -ItemType Directory -Force -Path $assetRoot | Out-Null

bottrade v3 preflight --config $Config
bottrade v3 features --asset $Asset --output (Join-Path $assetRoot "features.parquet") --config $Config
bottrade v3 candidates --asset $Asset --features (Join-Path $assetRoot "features.parquet") --output (Join-Path $assetRoot "candidates.parquet") --config $Config
bottrade v3 labels --candidates (Join-Path $assetRoot "candidates.parquet") --intrahour (Join-Path "data/raw/market" ("{0}_15m.parquet" -f $Asset)) --output (Join-Path $assetRoot "labels.parquet") --config $Config
bottrade v3 deterministic --labels (Join-Path $assetRoot "labels.parquet") --output-dir (Join-Path "reports/generated/v3" $Asset) --config $Config
bottrade v3 meta-train --asset $Asset --family $Family --features (Join-Path $assetRoot "features.parquet") --candidates (Join-Path $assetRoot "candidates.parquet") --labels (Join-Path $assetRoot "labels.parquet") --output-dir (Join-Path (Join-Path "reports/generated/v3" $Asset) $Family) --config $Config

Write-Host "Pré-holdout concluído para $Asset. O holdout não foi aberto."
