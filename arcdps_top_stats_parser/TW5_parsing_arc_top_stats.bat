@echo off
setlocal EnableDelayedExpansion

rem Check which executable exists
if exist "%~2\GuildWars2EliteInsights.exe" (
    set "EI_EXEC=%~2\GuildWars2EliteInsights.exe"
) else if exist "%~2\GuildWars2EliteInsights-CLI.exe" (
    set "EI_EXEC=%~2\GuildWars2EliteInsights-CLI.exe"
) else (
    echo No valid Guild Wars 2 Elite Insights executable found in %2
    exit /b 1
)

rem Process .zevtc files
for %%i in ("%~1\*.zevtc") do (
    "!EI_EXEC!" -c "%~3\EI_config\EI_detailed_json_combat_replay.conf" "%%i"
)

rem Run the Python script
python "%~3/TW5_parse_top_stats_detailed.py" "%~1"

endlocal
