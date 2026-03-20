param(
    [switch]$SkipVenv
)

$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ProjectRoot

$PyLauncher = Get-Command py -ErrorAction SilentlyContinue
if (-not $PyLauncher) {
    throw "Python launcher 'py' not found. Install Python 3.11 from python.org and ensure the launcher is installed."
}

$AvailablePythons = py -0p
if (($AvailablePythons -join "`n") -notmatch "(?m)-V:3\.11") {
    throw "Python 3.11 is required for this build. Install Python 3.11, then re-run ./build_windows.ps1."
}

if (-not $SkipVenv) {
    if (-not (Test-Path ".venv")) {
        Write-Host "[1/5] Creating .venv with Python 3.11..."
        py -3.11 -m venv .venv
    }
}

$PythonExe = Join-Path $ProjectRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $PythonExe)) {
    throw "Python virtual environment not found at .venv. Run with -SkipVenv only if .venv already exists."
}

Write-Host "[2/5] Upgrading pip..."
& $PythonExe -m pip install --upgrade pip

Write-Host "[3/5] Installing dependencies..."
& $PythonExe -m pip install -r requirements_windows.txt pyinstaller
if ($LASTEXITCODE -ne 0) {
    throw "Dependency installation failed."
}

Write-Host "[4/5] Building executable with PyInstaller..."
& $PythonExe -m PyInstaller --noconfirm --clean smart_gesture_hci.spec
if ($LASTEXITCODE -ne 0) {
    throw "PyInstaller build failed."
}

Write-Host "[5/5] Copying .env example into output..."
if (Test-Path ".env.example") {
    Copy-Item ".env.example" "dist\SmartGestureHCI\.env.example" -Force
}

Write-Host "Build complete. Output folder: dist\SmartGestureHCI"
