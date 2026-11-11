from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from .config import settings
from .database import engine, Base, SessionLocal
from .websocket_manager import manager
from .seed_data import seed_database

# Import routers
from .routes import (
    auth_routes,
    seniors_routes,
    vitals_routes,
    medications_routes,
    appointments_routes,
    emergency_routes,
    handoff_routes,
    analytics_routes,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create tables and seed demo data if needed
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_database(db)
    except Exception as e:
        print(f"Seed notice: {e}")
    finally:
        db.close()
    yield
    # Shutdown

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Comprehensive Healthcare API for Elderly Care Management System (ECMS). Includes real-time WebSockets for SOS alerts, telemetry ingestion, automated anomaly detection, medication management, and role-based access control.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS configuration allowing cross-origin requests from frontend (port 5173 or any port)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount API Routers under /api/v1
app.include_router(auth_routes.router, prefix=settings.API_V1_STR)
app.include_router(seniors_routes.router, prefix=settings.API_V1_STR)
app.include_router(vitals_routes.router, prefix=settings.API_V1_STR)
app.include_router(medications_routes.router, prefix=settings.API_V1_STR)
app.include_router(appointments_routes.router, prefix=settings.API_V1_STR)
app.include_router(emergency_routes.router, prefix=settings.API_V1_STR)
app.include_router(handoff_routes.router, prefix=settings.API_V1_STR)
app.include_router(analytics_routes.router, prefix=settings.API_V1_STR)

@app.websocket("/ws/emergency")
async def websocket_emergency_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Keep connection open and receive client pings/messages
            data = await websocket.receive_text()
            # Echo or acknowledge if client sends heartbeat
            await websocket.send_text(f'{{"type":"HEARTBEAT_ACK","received":"{data}"}}')
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception as e:
        manager.disconnect(websocket)

@app.get("/")
def root():
    return {
        "service": "Elderly Care Management System (ECMS) API",
        "status": "online",
        "documentation": "/docs",
        "redoc": "/redoc",
        "api_v1": "/api/v1",
        "websocket": "/ws/emergency"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "database": "connected",
        "timestamp": "active"
    }
