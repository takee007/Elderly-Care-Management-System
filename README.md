# Elderly Care Management System (ECMS)

Full-stack geriatric healthcare operations platform with role-based portals, real-time WebSocket emergency SOS broadcasting, vital-sign anomaly detection, electronic Medication Administration Record (eMAR) tracking, appointment/teleconsult scheduling, and complete IEEE 830 / ISO/IEC/IEEE 29148 requirements engineering deliverables.

---

## Live Design & Documentation (GitHub Pages)

- **Interactive Dual-Fidelity Design Viewer (Low-Fi & High-Fi):** https://takee007.github.io/Elderly-Care-Management-System/
- **Requirements & SRS Documentation Portal:** https://takee007.github.io/Elderly-Care-Management-System/requirements_specification_portal.html

---

## Key Capabilities

- **Role-Based Access Control (5 Portals):**
  - **Admin (`AdminPortal`)**: Healthcare KPI oversight, user provisioning/termination/reactivation, and audit trail review.
  - **Caregiver (`CaregiverDashboard`)**: Live resident telemetry, vitals logging with automated anomaly detection, eMAR administration queue, and shift handoff logs.
  - **Doctor (`DoctorPortal`)**: EHR patient reviews, electronic prescription management, and teleconsultation scheduling.
  - **Senior (`SeniorPortal`)**: Accessible large-type UI, giant 999 emergency SOS trigger with 5-second countdown, medication checklist, and daily schedule.
  - **Guardian (`GuardianPortal`)**: Parent wellness summary, medication adherence tracking, vitals history, and alerts.
- **Real-Time Emergency SOS (`ws://127.0.0.1:8000/ws/emergency`)**: Instant WebSocket broadcast banner across active sessions when an SOS alert or critical vital-sign anomaly is triggered.
- **Requirements & Design Artifacts**: Proposal, Low/High-Fidelity HTML & PDF prototypes, Requirements Elicitation Document, Requirements Analysis Document, IEEE-template SRS (`.md`, `.html`, `.docx`, `.pdf`), and architecture/UML/DFD/ER diagrams (`figures_png/`).

---

## Project Structure

```text
├── backend/                  # FastAPI + SQLAlchemy + WebSocket API
│   ├── app/
│   │   ├── routes/           # Auth, Seniors, Vitals, Medications, Appointments, Emergency, Handoff, Analytics
│   │   ├── auth.py           # JWT + bcrypt + role-checking dependencies
│   │   ├── models.py         # SQLAlchemy ORM models
│   │   ├── schemas.py        # Pydantic validation schemas
│   │   ├── seed_data.py      # Initial demo personas and clinical baseline records
│   │   └── main.py           # FastAPI entry point & WebSocket endpoint
│   └── run.py                # Uvicorn dev server launcher
├── frontend/                 # React 19 + Vite + Lucide Icons
│   └── src/
│       ├── components/       # Role portals, Navbar, EmergencyBanner, LoginPage/Modal
│       ├── api.js            # REST client & WebSocket helper
│       └── App.jsx           # Auth routing & lazy-loaded portal shell
├── figures_png/              # Context, ER, DFD, UML use-case, SDLC, and Gantt diagrams
├── start_system.bat          # Windows one-click launcher for backend + frontend
└── README_RUN.md             # Detailed quick-start guide & demo account credentials
```

---

## Quick Start

See [README_RUN.md](./README_RUN.md) for full setup details and demo login accounts.

### Windows One-Click Launch
```bat
start_system.bat
```

### Manual Launch

**1. Start the Backend (FastAPI on `http://127.0.0.1:8000`):**
```powershell
cd backend
python run.py
```

**2. Start the Frontend (React + Vite on `http://127.0.0.1:5173`):**
```powershell
cd frontend
npm install
npm run dev
```

- **Web UI**: `http://127.0.0.1:5173/`
- **Swagger Docs**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`
