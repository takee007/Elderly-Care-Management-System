# Elderly Care Management System (ECMS) - Quick Run Guide

## System Requirements
- **Python 3.12+** (Installed)
- **Node.js 18+ & npm** (Installed)
- **OS**: Windows / Linux / macOS

---

## ⚡ Method 1: One-Click Launcher (Windows)
Double-click the launcher script in the project root:
```
start_system.bat
```
This automatically starts both the Python FastAPI backend and the React Vite frontend in separate terminal windows.

---

## 🖥️ Method 2: Manual Terminal Startup

### Terminal 1: Start Backend (FastAPI)
```powershell
# Navigate to the backend directory
cd "d:\Antigravity_Workspace\Elderly Care Management System\backend"

# Run the server
python run.py
```
- **Backend URL**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive Swagger API Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- **WebSocket Emergency Channel**: `ws://127.0.0.1:8000/ws/emergency`

*(Note: SQLite database `ecms.db` is automatically created and seeded on first run).*

---

### Terminal 2: Start Frontend (React + Vite)
```powershell
# Navigate to the frontend directory
cd "d:\Antigravity_Workspace\Elderly Care Management System\frontend"

# (Only needed if node_modules is missing)
npm install

# Start development dev server
npm run dev
```
- **Web Application URL**: [http://127.0.0.1:5173/](http://127.0.0.1:5173/)

---

## 🔑 Demo Login Accounts

All accounts share the default password: **`password123`**

| Role | Name | Email | Purpose & Features |
|---|---|---|---|
| **ADMIN** | Engr. Md. Tariqul Islam | `admin@probin.gov.bd` | National healthcare KPIs, user provisioning (+ Add User), termination/reactivation, HIPAA audit logs |
| **CAREGIVER** | Fatema Begum, BSc Nursing (RN) | `nurse.fatema@probin.org.bd` | Live senior telemetry, log vitals with anomaly detection, eMAR medication queue, shift handover logs |
| **DOCTOR** | Prof. Dr. Syed Rafiqul Hasan | `dr.hasan@probin.org.bd` | EHR patient reviews, electronic prescription manager, teleconsult video rooms |
| **SENIOR** | Alhaj Mohammad Shamsuddin | `shamsuddin@probin.org.bd` | Accessible large UI, Giant 999 SOS button with 5s countdown, medication checklist, daily timeline |
| **GUARDIAN** | Tanvir Ahmed | `tanvir.ahmed@gmail.com` | Parent wellness status, medication adherence ring (60%), vitals history, caregiver messaging |

*Note: You can also use the **1-Click Instant Persona Sign-In** cards directly on the login screen.*
