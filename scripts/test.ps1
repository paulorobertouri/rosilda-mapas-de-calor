$ErrorActionPreference = "Stop"

$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

Push-Location $Root
try {
    uv run python -m pytest backend/tests -v
} finally {
    Pop-Location
}
