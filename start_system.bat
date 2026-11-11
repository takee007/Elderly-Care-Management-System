@echo off
title Elderly Care Management System (ECMS) Launcher
echo =====================================================================
echo    Elderly Care Management System (ECMS) - Full Stack Launcher
echo =====================================================================
echo.
echo Starting FastAPI Python Backend on http://127.0.0.1:8000 ...
start "ECMS Backend (FastAPI)" cmd /k "cd /d "%~dp0backend" && python run.py"

echo Starting React Vite Frontend on http://127.0.0.1:5173 ...
start "ECMS Frontend (React)" cmd /k "cd /d "%~dp0frontend" && npm run dev"

echo.
echo Both servers are launching!
echo  - Frontend Web UI: http://127.0.0.1:5173/
echo  - Backend API Docs: http://127.0.0.1:8000/docs
echo.
pause
