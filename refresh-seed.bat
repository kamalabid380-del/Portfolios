@echo off
setlocal
cd /d "%~dp0"

if /I "%~1"=="--quiet" (
  "%~f0" --logged >> "%~dp0refresh-seed.log" 2>&1
  exit /b %errorlevel%
)

set PYTHONUTF8=1
set GIT_TERMINAL_PROMPT=0

echo [%date% %time%] Refreshing the Vercel content seed from the local database...
py -3 manage.py dumpdata core.Profile core.Skill core.Project core.Post core.HeaderNav --indent 2 -o core\fixtures\seed.json
if errorlevel 1 (
  echo [%date% %time%] FAILED: could not export the database.
  if /I not "%~1"=="--logged" pause
  exit /b 1
)

git add core\fixtures\seed.json
git diff --cached --quiet
if errorlevel 1 (
  git commit -m "Refresh seed fixture"
  if errorlevel 1 (
    echo [%date% %time%] FAILED: git commit did not work.
    if /I not "%~1"=="--logged" pause
    exit /b 1
  )
  git push origin main
  if errorlevel 1 (
    echo [%date% %time%] FAILED: git push did not work.
    if /I not "%~1"=="--logged" pause
    exit /b 1
  )
  echo [%date% %time%] Done. Vercel is redeploying with the new content.
) else (
  echo [%date% %time%] No content changes - nothing to push.
)

if /I not "%~1"=="--logged" pause
exit /b 0
