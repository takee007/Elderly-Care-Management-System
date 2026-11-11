import React from 'react';
import { 
  HeartHandshake, 
  ShieldCheck, 
  Stethoscope, 
  UserCheck, 
  Users, 
  Activity, 
  LogOut, 
  PhoneCall,
  Shield
} from '../icons';

export default function Navbar({ 
  currentUser, 
  onLogout, 
  wsStatus 
}) {
  const roleMetadata = {
    CAREGIVER: { label: 'Caregiver Station', icon: HeartHandshake, color: '#10b981', bg: 'rgba(16, 185, 129, 0.15)' },
    DOCTOR: { label: 'Physician Portal', icon: Stethoscope, color: '#38bdf8', bg: 'rgba(56, 189, 248, 0.15)' },
    SENIOR: { label: 'Senior Resident UI', icon: UserCheck, color: '#f59e0b', bg: 'rgba(245, 158, 11, 0.15)' },
    GUARDIAN: { label: 'Family Guardian Portal', icon: Users, color: '#a855f7', bg: 'rgba(168, 85, 247, 0.15)' },
    ADMIN: { label: 'System Administration', icon: ShieldCheck, color: '#94a3b8', bg: 'rgba(148, 163, 184, 0.15)' },
  };

  const currentRoleInfo = currentUser && roleMetadata[currentUser.role] 
    ? roleMetadata[currentUser.role] 
    : { label: 'Elderly Care Portal', icon: Activity, color: '#10b981', bg: 'rgba(16, 185, 129, 0.15)' };

  const RoleIcon = currentRoleInfo.icon;

  return (
    <nav className="navbar">
      {/* Brand Section */}
      <div className="brand-section">
        <div className="brand-logo-icon" style={{ background: 'linear-gradient(135deg, #059669 0%, #0284c7 100%)' }}>
          <Activity size={24} />
        </div>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <span className="brand-title">Elderly Care Management System</span>
            <span className="brand-badge">ECMS</span>
          </div>
          <p style={{ fontSize: '0.72rem', color: 'var(--text-muted)', margin: 0 }}>
            Geriatric Telemetry, eMAR &amp; Emergency SOS Platform
          </p>
        </div>
      </div>

      {/* Bangladesh National Helplines Quick Access */}
      <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', flexWrap: 'wrap' }}>
        <a 
          href="tel:999" 
          aria-label="Call National Emergency 999"
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '0.35rem',
            background: 'rgba(239, 68, 68, 0.15)',
            border: '1px solid rgba(239, 68, 68, 0.4)',
            padding: '0.25rem 0.65rem',
            borderRadius: 'var(--radius-full)',
            color: '#fca5a5',
            fontSize: '0.75rem',
            fontWeight: '700',
            textDecoration: 'none'
          }}
          title="Bangladesh National Emergency Hotline 999"
        >
          <PhoneCall size={12} color="#ef4444" />
          <span>Emergency 999</span>
        </a>

        <a 
          href="tel:16263" 
          aria-label="Call DGHS Health Helpline 16263"
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '0.35rem',
            background: 'rgba(16, 185, 129, 0.15)',
            border: '1px solid rgba(16, 185, 129, 0.4)',
            padding: '0.25rem 0.65rem',
            borderRadius: 'var(--radius-full)',
            color: '#6ee7b7',
            fontSize: '0.75rem',
            fontWeight: '700',
            textDecoration: 'none'
          }}
          title="DGHS National Healthline Shastho Batayon 16263"
        >
          <Shield size={12} color="#10b981" />
          <span>Health Helpline 16263</span>
        </a>

        {/* Authenticated Role Badge */}
        {currentUser && (
          <div style={{
            display: 'flex',
            alignItems: 'center',
            gap: '0.5rem',
            background: currentRoleInfo.bg,
            border: `1px solid ${currentRoleInfo.color}40`,
            padding: '0.35rem 0.85rem',
            borderRadius: 'var(--radius-full)'
          }}>
            <RoleIcon size={15} color={currentRoleInfo.color} />
            <span style={{ fontSize: '0.82rem', fontWeight: '700', color: '#fff' }}>
              {currentRoleInfo.label}
            </span>
            <span style={{ fontSize: '0.75rem', color: currentRoleInfo.color, fontWeight: '600' }}>
              &bull; Role-Authorized
            </span>
          </div>
        )}
      </div>

      {/* Live System Status & Auth */}
      <div className="header-actions">
        <div 
          className="connection-status-pill"
          title={wsStatus === 'connected' ? 'WebSocket Real-time SOS channel active (Dhaka BST)' : 'Connecting to Telemetry Socket...'}
        >
          <div className="status-dot" style={{ backgroundColor: wsStatus === 'connected' ? '#10b981' : '#f59e0b' }} />
          <span>{wsStatus === 'connected' ? 'Live Telemetry' : 'Connecting...'}</span>
        </div>

        {currentUser ? (
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <div style={{ textAlign: 'right' }}>
              <div style={{ fontSize: '0.85rem', fontWeight: '700', color: '#fff' }}>
                {currentUser.full_name}
              </div>
              <div style={{ fontSize: '0.7rem', color: 'var(--text-secondary)' }}>
                {currentUser.email}
              </div>
            </div>
            <button 
              className="btn btn-secondary" 
              onClick={onLogout}
              style={{ padding: '0.45rem 0.85rem', fontSize: '0.8rem', gap: '0.35rem' }}
              title="Sign Out & Return to Login Screen"
              aria-label="Sign Out & Return to Login Screen"
            >
              <LogOut size={13} />
              <span>Sign Out</span>
            </button>
          </div>
        ) : null}
      </div>
    </nav>
  );
}
