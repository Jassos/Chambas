@echo off
setlocal

:: Abrir PowerShell y ejecutar comandos
set "SCRIPTDIR=%~dp0"

powershell -NoExit -Command ^
    "cd '%SCRIPTDIR%';" ^
    "Write-Host 'Carpeta actual: ' (Get-Location);" ^
    "py -m venv venv;" ^
    "Set-ExecutionPolicy Bypass -Scope Process -Force;" ^
    ".\venv\Scripts\Activate;" ^
    "Write-Host 'Entorno virtual activado';" ^
    "Write-Host 'Instalando pip...';" ^
    "pip install --upgrade pip;" ^
    "Write-Host 'Instalando dependencias...';" ^
    "pip install -r requirements.txt;" ^
    "pause"
