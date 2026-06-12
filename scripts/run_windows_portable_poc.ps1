<#
SolidPrivacy Scrub Windows portable proof-of-concept launcher.
Runs the existing Python localhost launcher from a local repository folder.
#>

[CmdletBinding()]
param(
    [string]$PythonCommand = "python",
    [string]$Address = "127.0.0.1",
    [string]$Port = "8501"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$ScriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepositoryRoot = Resolve-Path (Join-Path $ScriptDirectory "..")
Set-Location $RepositoryRoot

& $PythonCommand "scripts/run_local_streamlit.py" --address $Address --port $Port
exit $LASTEXITCODE
