$ErrorActionPreference = "Stop"

Write-Host "== V3 compile =="
python -m compileall -q src/bottrade/v3
Write-Host "== V3 tests =="
python -m pytest tests/v3 -q
Write-Host "== CLI preflight =="
bottrade v3 preflight --config config/v3.yaml
