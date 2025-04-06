# Read config file
$configFile = ".\edit_me.conf"
$configTable = @{}
Get-Content -Path $configFile | ForEach-Object {
  if ($_ -match '=') {
    $key, $value = $_ -split '='
    $configTable[$key.Trim()] = $value.Trim('"')
  }
}

# Retrieve values from the config hashtable
if (-not $configTable.ContainsKey("ARC_DPS_LOGS_DIR")) {
  Write-Error "ARC_DPS_LOGS_DIR not found. Please check your edit_me.conf file."
  Read-Host
  exit 1
}
$arcDpslogsDir = $configTable["ARC_DPS_LOGS_DIR"]
$resolvedPath = Resolve-Path -Path $arcDpslogsDir -ErrorAction SilentlyContinue
if (-not $resolvedPath) {
  Write-Error "Cannot resolve the ARC_DPS_LOGS_DIR path. Please provide in edit_me.conf file a correct path (e.g. `C:\Program Files (x86)\Guild Wars 2\addons\arcdps\arcdps.cbtlogs\WvW (1)\Player`)."
  Read-Host
  exit 1
}
$extractDate = ""
if ($configTable.ContainsKey("EXTRACT_DATE")) {
  $extractDate = $configTable["EXTRACT_DATE"]
  if ($extractDate -ne "" -and $extractDate -notmatch '^\d{8}$') {
    Write-Error "Invalid EXTRACT_DATE format. Please use YYYYMMDD format."
    Read-Host
    exit 1
  }
}

# Specific script paths
$eliteInsightsDir = "..\GW2EICLI"
$topStatsParserDir = "..\arcdps_top_stats_parser"
$customConfigPath = ".\custom-config"
$dataPath = ".\data"
$logsPath = ".\data\logs"
$jsonPath = ".\data\json"
$tidPath = ".\data\tid"

# Display correctly the EXTRACT_DATE if it's empty
if ($extractDate -eq "") {
  $displayExtractDate = "now"
  $extractDate = (Get-Date).ToString("yyyyMMdd")
}
else {
  $displayExtractDate = $extractDate
}



# Prepare the environment
Write-Output "##############################################################################"
Write-Output "### 1. Prepare the environment ###############################################"
Write-Output "###### Configuration #########################################################"
Write-Output "###### In-game logs path:     $arcDpslogsDir"
Write-Output "###### Extract date:          $displayExtractDate"

Write-Output "######## Fetch arcdps_top_stats_parser @latest version #######################"
$topStatsParserRepoUrl = "https://api.github.com/repos/Drevarr/arcdps_top_stats_parser/releases/latest"
$topStatsParserRepoUrlResponse = Invoke-RestMethod -Uri $topStatsParserRepoUrl
$topStatsParserLatestVersion = $topStatsParserRepoUrlResponse.tag_name
$topStatsParserCurrentVersion = "v3.5.20-TW5"
if ($topStatsParserCurrentVersion -ne $topStatsParserLatestVersion) {
  Write-Output "Downloading & updating arcdps_top_stats_parser @latest $topStatsParserLatestVersion..."
  # Fetch the zip file
  $topStatsParserAssetName = "arcdps_top_stats_parser.zip"
  $topStatsParserLatestReleaseUrl = $topStatsParserRepoUrlResponse.zipball_url
  Invoke-WebRequest -Uri $topStatsParserLatestReleaseUrl -OutFile $topStatsParserAssetName

  # Unzip the downloaded file
  Write-Output "Unzipping the latest arcdps_top_stats_parser.zip..."
  $topStatsParserTempDir = "..\tmp"
  Expand-Archive -Path $topStatsParserAssetName -DestinationPath $topStatsParserTempDir -Force

  # Move the contents from the nested temporary directory to the desired directory while preserving the structure
  $topStatsParserNestedDir = Get-ChildItem -Path $topStatsParserTempDir | Where-Object { $_.PSIsContainer } | Select-Object -ExpandProperty FullName
  Get-ChildItem -Path "$topStatsParserNestedDir\*" -Recurse | ForEach-Object {
    $destinationPath = $_.FullName.Replace($topStatsParserNestedDir, $topStatsParserDir)
    if ($_.PSIsContainer) {
      New-Item -ItemType Directory -Path $destinationPath -Force > $null
    }
    else {
      Copy-Item -Path $_.FullName -Destination $destinationPath -Force
    }
  }
  
  # Remove the temporary directory and the zip file
  Remove-Item -Path $topStatsParserTempDir -Recurse
  Remove-Item -Path $topStatsParserAssetName
}
else {
  Write-Output "arcdps_top_stats_parser already @latest $topStatsParserLatestVersion"
}

Write-Output "######## Update GW2-Elite-Insights-Parser CLI @latest version ################"
$eliteInsightsRepoUrl = "https://api.github.com/repos/baaron4/GW2-Elite-Insights-Parser/releases/latest"
$eliteInsightsLatestVersion = (Invoke-RestMethod -Uri $eliteInsightsRepoUrl).tag_name
$eliteInsightsCurrentVersion = "v3.5.0.0"
if ($eliteInsightsCurrentVersion -ne $eliteInsightsLatestVersion) {
  Write-Output "Downloading & updating GW2EICLI @latest $eliteInsightsLatestVersion..."
  # Fetch the zip file
  $eliteInsightsAssetName = "GW2EICLI.zip"
  $eliteInsightsLatestReleaseUrl = (Invoke-RestMethod -Uri $eliteInsightsRepoUrl).assets | Where-Object { $_.name -eq $eliteInsightsAssetName } | Select-Object -ExpandProperty browser_download_url
  Invoke-WebRequest -Uri $eliteInsightsLatestReleaseUrl -OutFile $eliteInsightsAssetName

  # Unzip the downloaded file
  Write-Output "Unzipping the latest GW2EICLI.zip..."
  Expand-Archive -Path $eliteInsightsAssetName -DestinationPath $eliteInsightsDir -Force

  # Remove the zip file
  Remove-Item -Path $eliteInsightsAssetName
}
else {
  Write-Output "GW2EICLI already @latest $eliteInsightsLatestVersion"
}

## Check if python3 is installed to continue, and install required Python packages
Write-Output "######## Install required Python packages ####################################"
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
  Write-Error "Python3 is not installed. Please install it from https://www.python.org/downloads/."
  Read-Host
  exit 1
}
python.exe -m pip install --upgrade pip -q
$pipPackages = @("xlrd", "xlutils", "xlwt", "jsons", "requests", "xlsxwriter")
function Test-PythonPackage {
  param (
    [string]$PackageName
  )
  $result = python -c "import $PackageName" 2>&1
  return ($result -match "ModuleNotFoundError")
}
$pipPackages | ForEach-Object {
  if ((Test-PythonPackage -PackageName $_)) {
    Write-Output "Installing package: $_..."
    python.exe -m pip install $_ -q
    if (-not $?) {
      Write-Error "Failed to install package: $_. Please install it manually."
      Read-Host
      exit 1
    }
  }
  else {
    Write-Output "Package already installed: $_"
  }
}

## Remove old data files
Write-Output "######## Removing old data files #############################################"
if ((Test-Path -Path $dataPath)) {
  Remove-Item -Path $dataPath -Recurse -Force
}

## Copy specific .zevtc files from arcdps.cbtlogs folder
Write-Output "######## Copying specific .zevtc files from ArcDps folder ####################"
if (-not (Test-Path -Path $logsPath)) {
  New-Item -ItemType Directory -Path $logsPath > $null
}
Copy-Item -Path "$arcDpslogsDir\$extractDate*.zevtc" -Destination $logsPath

Write-Output "##############################################################################"
Write-Output "### 2. Parse files & generate stats ##########################################"
# Convert .zevtc to .json files, using GW2-Elite-Insights-Parser
Write-Output "######## Converting .zevtc to .json, using GW2-Elite-Insights-Parser #########"
## Check if there are .zevtc files to convert
$zevtcFiles = Get-ChildItem -Path "$logsPath\*.zevtc"
if ($zevtcFiles.Count -eq 0) {
  Write-Output "No .zevtc files found to process."
  Read-Host
  exit 1
}
if (-not (Test-Path -Path $jsonPath)) {
  New-Item -ItemType Directory -Path $jsonPath > $null
}
foreach ($file in Get-ChildItem -Path "$logsPath\*.zevtc") {
  # TODO: add verbose option
  & "$eliteInsightsDir\GuildWars2EliteInsights-CLI.exe" -c "$customConfigPath\EI_detailed_json_combat_replay_custom.conf" "$file" > $null
}
Get-ChildItem -Path "$logsPath\*.json" | ForEach-Object {
  Move-Item -Path $_.FullName -Destination $jsonPath -Force
}

# Generate .tid file from .json, using arcdps_top_stats_parser
Write-Output "######## Generating .tid file from .json, using arcdps_top_stats_parser ######"
## Patch Python to add argument to adjust date with extract date
$patch = "addExtractDateInArgumentPythonScript.patch"
$topStatsParserDir = "..\arcdps_top_stats_parser"
Copy-Item -Path ".\$patch" -Destination $topStatsParserDir -Force
Set-Location $topStatsParserDir
git apply $patch -q
Set-Location "..\script"
## Running script with extractDate
if ($displayExtractDate -eq "now") {
  python "$topStatsParserDir\TW5_parse_top_stats_detailed.py" $jsonPath > $null
}
else {
  $dateTime = [datetime]::ParseExact($extractDate, 'yyyyMMdd', $null).AddHours(22).ToString("yyyy-MM-ddTHH:mm:ss")
  python "$topStatsParserDir\TW5_parse_top_stats_detailed.py" $jsonPath -d "$dateTime" > $null
}
if (-not (Test-Path -Path $tidPath)) {
  New-Item -ItemType Directory -Path $tidPath > $null
}
## Extract .tid file in a folder
Get-ChildItem -Path "$jsonPath\*.tid" | ForEach-Object {
  Copy-Item -Path $_.FullName -Destination $tidPath -Force
}

Write-Output "##############################################################################"
Write-Output "### 3. Upload .tid to show in web page #######################################"
Write-Output "##############################################################################"
Write-Output ""
Write-Output "==> Please import .tid files to your hosted TW5_Top_Stat_Parse.html, then press red top-right Save button to get the .html file. <=="
Write-Output ""

# Success! \o/
Write-Output "Script execution completed. Press Enter to exit."
Read-Host
exit 0
