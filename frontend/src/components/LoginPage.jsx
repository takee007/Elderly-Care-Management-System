import React, { useState } from 'react';
import { 
  LogIn, 
  Key, 
  Mail, 
  ShieldCheck, 
  Stethoscope, 
  HeartHandshake, 
  UserCheck, 
  Users, 
  Activity, 
  AlertTriangle, 
  Lock, 
  Terminal, 
  ExternalLink,
  ChevronRight,
  PhoneCall,
  Shield
} from '../icons';
import { api, setStoredAuth } from '../api';

export default function LoginPage({ onLoginSuccess }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('password123');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const demoAccounts = [
    {
      role: 'CAREGIVER',
      title: 'Caregiver Station',
      name: 'Fatema Begum, BSc Nursing (RN)',
      email: 'nurse.fatema@probin.org.bd',
      icon: HeartHandshake,
      color: '#10b981',
      badgeBg: 'rgba(16, 185, 129, 0.15)',
      desc: 'Vitals telemetry, eMAR dose queue, shift handovers'
    },
    {
      role: 'DOCTOR',
      title: 'Physician Portal',
      name: 'Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS',
      email: 'dr.hasan@probin.org.bd',
      icon: Stethoscope,
      color: '#38bdf8',
      badgeBg: 'rgba(56, 189, 248, 0.15)',
      desc: 'EHR patient reviews, e-prescriptions, teleconsult video links'
    },
    {
      role: 'SENIOR',
      title: 'Senior Resident UI',
      name: 'Alhaj Mohammad Shamsuddin (Suite 204 - Padma)',
      email: 'shamsuddin@probin.org.bd',
      icon: UserCheck,
      color: '#f59e0b',
      badgeBg: 'rgba(245, 158, 11, 0.15)',
      desc: 'Accessible large-card interface, Giant 999 SOS button, medication checkoff'
    },
    {
      role: 'GUARDIAN',
      title: 'Family Guardian Portal',
      name: 'Tanvir Ahmed (Son / Designated Guardian)',
      email: 'tanvir.ahmed@gmail.com',
      icon: Users,
      color: '#a855f7',
      badgeBg: 'rgba(168, 85, 247, 0.15)',
      desc: 'Father wellness tracking, medication adherence gauge, nurse messaging'
    },
    {
      role: 'ADMIN',
      title: 'System Administrator',
      name: 'Engr. Md. Tariqul Islam',
      email: 'admin@probin.gov.bd',
      icon: ShieldCheck,
      color: '#94a3b8',
      badgeBg: 'rgba(148, 163, 184, 0.15)',
      desc: 'National healthcare KPIs, RBAC user accounts, audit trail'
    }
  ];

  async function handleFormSubmit(e) {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      const res = await api.login(email, password);
      setStoredAuth(res.access_token, res);
      onLoginSuccess(res);
    } catch (err) {
      setError(err.message || 'Invalid email or password. Please verify your credentials.');
    } finally {
      setLoading(false);
    }
  }

  async function handleDemoPersonaClick(role, demoEmail) {
    setError('');
    setLoading(true);
    try {
      const res = await api.demoLogin(role);
      setStoredAuth(res.access_token, res);
      onLoginSuccess(res);
    } catch (err) {
      try {
        const res = await api.login(demoEmail, 'password123');
        setStoredAuth(res.access_token, res);
        onLoginSuccess(res);
      } catch (e) {
        setError(e.message || `Demo login failed for ${role}`);
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <main style={{
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      padding: '2.5rem 1.5rem',
      position: 'relative',
    }}>
      {/* Brand Header */}
      <div style={{ textAlign: 'center', marginBottom: '2.5rem', maxWidth: '780px' }}>
        <div style={{
          display: 'inline-flex',
          alignItems: 'center',
          gap: '0.75rem',
          background: 'rgba(15, 23, 42, 0.92)',
          border: '1px solid rgba(0, 106, 78, 0.4)',
          padding: '0.5rem 1.25rem',
          borderRadius: 'var(--radius-full)',
          marginBottom: '1rem',
          boxShadow: 'var(--shadow-md)'
        }}>
          <div style={{
            width: '1.75rem',
            height: '1.75rem',
            borderRadius: '6px',
            background: 'linear-gradient(135deg, #006a4e 0%, #f42a41 100%)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: '#fff'
          }}>
            <Activity size={18} />
          </div>
          <span style={{ fontSize: '0.9rem', fontWeight: '800', letterSpacing: '0.03em', color: '#fff' }}>
            ELDERLY CARE MANAGEMENT SYSTEM (ECMS)
          </span>
        </div>

        <h1 style={{ fontSize: '2.4rem', fontWeight: '800', color: '#fff', lineHeight: 1.25, textShadow: '0 2px 10px rgba(0,0,0,0.5)' }}>
          Healthcare Portal Sign-In
        </h1>
        <p style={{ color: 'var(--text-secondary)', fontSize: '1rem', marginTop: '0.5rem' }}>
          Smart Telemetry, eMAR Medication Management &amp; Emergency 999 SOS Platform &bull; Dhanmondi, Dhaka
        </p>
      </div>

      {/* Main Split Authentication Card */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(360px, 1fr))',
        gap: '2.5rem',
        maxWidth: '1100px',
        width: '100%',
        background: 'rgba(15, 23, 42, 0.94)',
        border: '1px solid rgba(255, 255, 255, 0.15)',
        borderRadius: 'var(--radius-xl)',
        padding: '2.5rem',
        boxShadow: '0 20px 40px rgba(0, 0, 0, 0.7)'
      }}>
        {/* Left Column: Standard Credentials Login Form */}
        <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1.25rem' }}>
              <Lock size={20} color="#10b981" />
              <h2 style={{ fontSize: '1.35rem', color: '#fff' }}>Account Authentication</h2>
            </div>
            <p style={{ fontSize: '0.88rem', color: 'var(--text-secondary)', marginBottom: '1.5rem' }}>
              Sign in with your institutional credentials or choose an instant persona below.
            </p>

            {error && (
              <div style={{
                padding: '0.85rem 1rem',
                background: 'rgba(239, 68, 68, 0.15)',
                border: '1px solid #ef4444',
                borderRadius: 'var(--radius-md)',
                color: '#f87171',
                fontSize: '0.85rem',
                marginBottom: '1.25rem',
                display: 'flex',
                alignItems: 'center',
                gap: '0.5rem'
              }}>
                <AlertTriangle size={16} flexShrink={0} />
                <span>{error}</span>
              </div>
            )}

            <form onSubmit={handleFormSubmit}>
              <div className="form-group">
                <label htmlFor="login-email">Institutional Email Address</label>
                <div style={{ position: 'relative' }}>
                  <Mail size={16} style={{ position: 'absolute', left: '0.85rem', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
                  <input
                    id="login-email"
                    type="email"
                    name="email"
                    autoComplete="email"
                    placeholder="e.g. nurse.fatema@probin.org.bd"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    style={{ paddingLeft: '2.5rem', width: '100%' }}
                    required
                  />
                </div>
              </div>

              <div className="form-group">
                <label htmlFor="login-password">Password</label>
                <div style={{ position: 'relative' }}>
                  <Key size={16} style={{ position: 'absolute', left: '0.85rem', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
                  <input
                    id="login-password"
                    type="password"
                    name="password"
                    autoComplete="current-password"
                    placeholder="Enter password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    style={{ paddingLeft: '2.5rem', width: '100%' }}
                    required
                  />
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '0.4rem', fontSize: '0.78rem', color: 'var(--text-muted)' }}>
                  <span>Default demo password for all accounts: <code>password123</code></span>
                </div>
              </div>

              <button
                type="submit"
                className="btn btn-primary"
                style={{
                  width: '100%',
                  padding: '0.85rem',
                  fontSize: '1rem',
                  fontWeight: '700',
                  marginTop: '0.75rem',
                  borderRadius: 'var(--radius-md)',
                  background: 'linear-gradient(135deg, #006a4e 0%, #059669 100%)'
                }}
                disabled={loading}
              >
                <LogIn size={18} />
                <span>{loading ? 'Verifying Credentials...' : 'Sign In to Portal'}</span>
              </button>
            </form>
          </div>

          {/* National helpline banner footer */}
          <div style={{
            marginTop: '2rem',
            paddingTop: '1.25rem',
            borderTop: '1px solid var(--border-subtle)',
            fontSize: '0.8rem',
            color: 'var(--text-muted)'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.35rem' }}>
              <Shield size={14} color="#10b981" />
              <strong style={{ color: 'var(--text-secondary)' }}>DGHS &bull; Ministry of Health &amp; Family Welfare Compliance</strong>
            </div>
            <p>
              National Emergency: <strong>999</strong> &bull; DGHS Healthline: <strong>16263</strong> &bull; API Documentation:{' '}
              <a href="http://127.0.0.1:8000/docs" target="_blank" rel="noopener noreferrer" style={{ color: '#38bdf8' }}>
                /docs <ExternalLink size={11} style={{ display: 'inline' }} />
              </a>
            </p>
          </div>
        </div>

        {/* Right Column: 1-Click Fast Persona Switcher */}
        <div style={{ borderLeft: '1px solid rgba(255, 255, 255, 0.08)', paddingLeft: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
            <h3 style={{ fontSize: '1.15rem', color: '#fff' }}>1-Click Instant Persona Sign-In</h3>
            <span className="badge badge-success" style={{ fontSize: '0.7rem' }}>Demo Ready</span>
          </div>
          <p style={{ fontSize: '0.82rem', color: 'var(--text-secondary)', marginBottom: '1.25rem' }}>
            Click any clinical or resident role below to log in directly:
          </p>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
            {demoAccounts.map((acc) => {
              const Icon = acc.icon;
              return (
                <div
                  key={acc.role}
                  onClick={() => handleDemoPersonaClick(acc.role, acc.email)}
                  style={{
                    background: 'rgba(15, 23, 42, 0.65)',
                    border: '1px solid rgba(255, 255, 255, 0.08)',
                    borderRadius: 'var(--radius-md)',
                    padding: '0.85rem 1rem',
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.85rem',
                    transition: 'all 0.2s ease',
                  }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.borderColor = acc.color;
                    e.currentTarget.style.transform = 'translateX(4px)';
                    e.currentTarget.style.background = 'rgba(30, 41, 59, 0.85)';
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.borderColor = 'rgba(255, 255, 255, 0.08)';
                    e.currentTarget.style.transform = 'translateX(0)';
                    e.currentTarget.style.background = 'rgba(15, 23, 42, 0.65)';
                  }}
                >
                  <div style={{
                    width: '2.5rem',
                    height: '2.5rem',
                    borderRadius: '8px',
                    background: acc.badgeBg,
                    color: acc.color,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    flexShrink: 0
                  }}>
                    <Icon size={20} />
                  </div>

                  <div style={{ flex: 1, minWidth: 0 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                      <span style={{ fontWeight: '700', color: '#fff', fontSize: '0.92rem' }}>
                        {acc.title}
                      </span>
                    </div>
                    <div style={{ fontSize: '0.8rem', color: acc.color, fontWeight: '600' }}>
                      {acc.name}
                    </div>
                    <div style={{ fontSize: '0.74rem', color: 'var(--text-muted)', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                      {acc.desc}
                    </div>
                  </div>

                  <ChevronRight size={16} color="var(--text-muted)" />
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </main>
  );
}
