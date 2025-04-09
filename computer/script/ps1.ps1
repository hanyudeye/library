Get-ExecutionPolicy
$name="xiaoli"
Write-Host "Hello,$name"

Invoke-RestMethod https://get.scoop.sh
# Invoke-RestMethod https://get.scoop.sh | Invoke-Expression