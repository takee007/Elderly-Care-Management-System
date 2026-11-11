import React, { useState, useEffect, lazy, Suspense } from 'react';
import Navbar from './components/Navbar';
import EmergencyBanner from './components/EmergencyBanner';
import { api, getStoredUser, setStoredAuth, createEmergencyWebSocket } from './api';
import { ExternalLink, Shield, Terminal, LogIn } from './icons';

const CaregiverDashboard = lazy(() => import('./components/CaregiverDashboard'));
const DoctorPortal = lazy(() => import('./components/DoctorPortal'));
const SeniorPortal = lazy(() => import('./components/SeniorPortal'));
const GuardianPortal = lazy(() => import('./components/GuardianPortal'));
const AdminPortal = lazy(() => import('./components/AdminPortal'));
const LoginPage = lazy(() => import('./components/LoginPage'));

export default function App() {
  const [currentUser, setCurrentUser] = useState(() => getStoredUser());
  const [activeAlert, setActiveAlert] = useState(null);
  const [wsStatus, setWsStatus] = useState('disconnected');
  const [viewMode, setViewMode] = useState(() => (getStoredUser()?.role ? 'PORTAL' : 'LOGIN'));

  // Initialize Auth & Check Active Emergency Alerts
  useEffect(() => {
    if (currentUser?.role) {
      checkActiveAlerts();
    }
  }, [currentUser]);

  async function checkActiveAlerts() {
    try {
      const alerts = await api.getEmergencyAlerts();
      const active = alerts.find((a) => a.status === 'TRIGGERED' || a.status === 'RESPONDING');
      if (active) {
        setActiveAlert(active);
      } else {
        setActiveAlert(null);
      }
    } catch (e) {
      // Graceful fallback if backend not reached
    }
  }

  // Real-time WebSocket connection for SOS and telemetry broadcasting (active only when logged in)
  useEffect(() => {
    if (!currentUser) return;

    const ws = createEmergencyWebSocket(
      (data) => {
        if (data.type === 'EMERGENCY_SOS_ACTIVE' || data.type === 'VITALS_ANOMALY_ALERT') {
          setActiveAlert(data);
        } else if (data.type === 'EMERGENCY_SOS_RESOLVED') {
          checkActiveAlerts();
        }
      },
      (status) => setWsStatus(status)
    );

    return () => {
      ws.disconnect();
    };
  }, [currentUser]);

  function handleLogout() {
    setStoredAuth(null, null);
    setCurrentUser(null);
    setViewMode('LOGIN');
  }

  // If no user is authenticated or on Login view, render the dedicated LoginPage!
  if (!currentUser || viewMode === 'LOGIN') {
    return (
      <Suspense fallback={<div style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', background: '#0b1120', color: '#10b981' }}>Loading ECMS Portal...</div>}>
        <LoginPage
          onLoginSuccess={(user) => {
            setCurrentUser(user);
            setViewMode('PORTAL');
          }}
        />
      </Suspense>
    );
  }

  const role = currentUser.role || 'CAREGIVER';

  return (
    <div className="app-container">
      {/* Top Header - Enforces Strict RBAC with Active Role Display */}
      <Navbar
        currentUser={currentUser}
        onLogout={handleLogout}
        wsStatus={wsStatus}
      />

      {/* Flashing Emergency SOS Broadcast Banner */}
      <EmergencyBanner
        activeAlert={activeAlert}
        onAlertResolved={() => checkActiveAlerts()}
      />

      {/* Main Content Area: Render Strictly Authorized Portal for Logged-In User */}
      <main className="main-content">
        <Suspense fallback={<div style={{ padding: '2rem', textAlign: 'center', color: '#10b981' }}>Loading Healthcare Station...</div>}>
          {role === 'CAREGIVER' && (
            <CaregiverDashboard
              currentUser={currentUser}
              onEmergencyTriggered={() => checkActiveAlerts()}
            />
          )}

          {role === 'DOCTOR' && (
            <DoctorPortal currentUser={currentUser} />
          )}

          {role === 'SENIOR' && (
            <SeniorPortal
              currentUser={currentUser}
              onEmergencyTriggered={() => checkActiveAlerts()}
            />
          )}

          {role === 'GUARDIAN' && (
            <GuardianPortal currentUser={currentUser} />
          )}

          {role === 'ADMIN' && (
            <AdminPortal currentUser={currentUser} />
          )}
        </Suspense>
      </main>

      {/* Footer with Swagger API link and IEEE SRS compliance info */}
      <footer style={{ 
        borderTop: '1px solid var(--border-subtle)', 
        padding: '1.25rem 2rem', 
        background: 'rgba(11, 17, 32, 0.8)', 
        backdropFilter: 'blur(10px)',
        display: 'flex', 
        justifyContent: 'space-between', 
        alignItems: 'center', 
        flexWrap: 'wrap', 
        gap: '1rem',
        fontSize: '0.85rem',
        color: 'var(--text-muted)'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <Shield size={16} color="#10b981" />
          <span>Elderly Care Management System (ECMS) &bull; Role-Based Healthcare Architecture</span>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '1.25rem' }}>
          <button
            onClick={handleLogout}
            style={{
              background: 'transparent',
              border: 'none',
              color: '#34d399',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '0.35rem',
              fontSize: '0.85rem'
            }}
          >
            <LogIn size={14} />
            <span>Sign Out &amp; Switch User</span>
          </button>
          <span>&bull;</span>
          <a
            href="http://localhost:8000/docs"
            target="_blank"
            rel="noopener noreferrer"
            style={{ color: '#38bdf8', textDecoration: 'none', display: 'flex', alignItems: 'center', gap: '0.35rem' }}
          >
            <Terminal size={14} />
            <span>FastAPI Swagger /docs</span>
            <ExternalLink size={12} />
          </a>
          <span>&bull;</span>
          <a
            href="http://localhost:8000/redoc"
            target="_blank"
            rel="noopener noreferrer"
            style={{ color: '#a855f7', textDecoration: 'none', display: 'flex', alignItems: 'center', gap: '0.35rem' }}
          >
            <span>Interactive ReDoc</span>
            <ExternalLink size={12} />
          </a>
        </div>
      </footer>
    </div>
  );
}
