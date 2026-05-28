# scripts/build.ps1 — syntax-check Python sources
$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

Push-Location $Root
try {
    Write-Host "Building rosilda-mapas-de-calor..."
    uv run python -m compileall backend/src 2>$null
    Write-Host "Build check complete."
} finally {
    Pop-Location
}
