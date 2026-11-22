@echo off
setlocal
cd /d "%~dp0"
set PYTHONUTF8=1

echo Refreshing the Vercel content seed from the local database...
py -3 manage.py dumpdata core.Profile core.Skill core.Project core.Post core.HeaderNav --indent 2 -o core\fixtures\seed.json
if errorlevel 1 (
  echo.
  echo FAILED: could not export the database.
  pause
  exit /b 1
)

git add core\fixtures\seed.json
git diff --cached --quiet
if errorlevel 1 (
  git commit -m "Refresh seed fixture"
  if errorlevel 1 (
    echo.
    echo FAILED: git commit did not work.
    pause
    exit /b 1
  )
  git push origin main
  if errorlevel 1 (
    echo.
    echo FAILED: git push did not work.
    pause
    exit /b 1
  )
  echo.
  echo Done. Vercel is redeploying with the new content.
) else (
  echo.
  echo No content changes - nothing to push.
)

pause
exit /b 0
