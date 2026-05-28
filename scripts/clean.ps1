Get-ChildItem -Path . -Filter "__pycache__" -Recurse | Remove-Item -Force -Recurse
Get-ChildItem -Path . -Filter "*.pyc" -Recurse | Remove-Item -Force
Remove-Item -Path .coverage, htmlcov -Force -Recurse -ErrorAction SilentlyContinue
