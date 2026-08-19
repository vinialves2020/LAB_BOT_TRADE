$ErrorActionPreference = "Continue"

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot
New-Item -ItemType Directory -Force -Path "artifacts/logs" | Out-Null

# Diagnostic-only batch: it deliberately uses the minimum 12 pre-holdout folds,
# one registered seed and one search trial.  It is not eligible for promotion.
$assets = @("BTCUSDT", "ETHUSDT", "SOLUSDT")
$families = @("hist_gradient_boosting", "transformer")
$arms = @(
    "market",
    "market_1h_15m_derivatives",
    "market_1h_15m_derivatives_onchain",
    "market_1h_15m_derivatives_sentiment",
    "market_1h_15m_derivatives_all"
)
$summary = @()

foreach ($asset in $assets) {
    foreach ($family in $families) {
        foreach ($arm in $arms) {
            $tag = "${asset}_${family}_${arm}"
            $log = Join-Path "artifacts/logs" ("v2_ablation_pilot_{0}.log" -f $tag)
            $started = Get-Date
            $args = @(
                "-m", "bottrade", "train",
                "--asset", $asset,
                "--family", $family,
                "--arm", $arm,
                "--trials", "1",
                "--max-folds", "12",
                "--seeds", "11",
                "--config", "config/v2.yaml"
            )
            Write-Output ("START {0} {1} {2}" -f $asset, $family, $arm)
            & python @args *> $log
            $exitCode = $LASTEXITCODE
            $finished = Get-Date
            $summary += [PSCustomObject]@{
                asset = $asset
                family = $family
                arm = $arm
                exit_code = $exitCode
                started_at = $started.ToUniversalTime().ToString("o")
                finished_at = $finished.ToUniversalTime().ToString("o")
                log = $log
            }
            Write-Output ("DONE {0} exit={1} log={2}" -f $tag, $exitCode, $log)
        }
    }
}

$summary | ConvertTo-Json -Depth 4 | Set-Content -Encoding UTF8 "artifacts/logs/v2_ablation_pilot.summary.json"
Write-Output "SUMMARY artifacts/logs/v2_ablation_pilot.summary.json"
