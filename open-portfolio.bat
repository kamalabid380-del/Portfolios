@echo off
cd /d "%~dp0"
wscript //nologo "%~dp0start-hidden.vbs"
start "" "http://abidkamal.com/"
