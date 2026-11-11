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
  AlertCircle
} from '../icons';
import { api, setStoredAuth } from '../api';

export default function LoginModal({ isOpen, onClose, onLoginSuccess }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('password123');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  if (!isOpen) return null;

  async function handleLogin(e) {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      const res = await api.login(email, password);
      setStoredAuth(res.access_token, res);
      onLoginSuccess(res);
      onClose();
    } catch (err) {
      setError(err.message || 'Invalid email or password');
    } finally {
      setLoading(false);
    }
  }

  async function handleQuickDemo(role) {
    setError('');
    setLoading(true);
    try {
      const res = await api.demoLogin(role);
      setStoredAuth(res.access_token, res);
      onLoginSuccess(res);
      onClose();
    } catch (err) {
      setError(err.message || 'Demo login failed');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="modal-overlay">
      <div className="modal-content" style={{ maxWidth: '480px' }}>
        <div className="modal-header">
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <LogIn size={22} color="#10b981" />
            <h3>Sign In to ECMS Healthcare Suite</h3>
          </div>
          <button className="modal-close-btn" onClick={onClose} aria-label="Close login dialog">&times;</button>
        </div>

        {error && (
          <div style={{ 
            padding: '0.75rem 1rem', 
            background: 'rgba(239, 68, 68, 0.15)', 
            border: '1px solid #ef4444', 
            borderRadius: 'var(--radius-md)', 
            color: '#f87171', 
            fontSize: '0.85rem',
            marginBottom: '1rem',
            display: 'flex',
            alignItems: 'center',
            gap: '0.5rem'
          }}>
            <AlertCircle size={16} />
            <span>{error}</span>
          </div>
        )}

        <form onSubmit={handleLogin}>
          <div className="form-group">
            <label htmlFor="login-modal-email">Email Address</label>
            <div style={{ position: 'relative' }}>
              <Mail size={16} style={{ position: 'absolute', left: '0.85rem', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
              <input
                id="login-modal-email"
                type="email"
                placeholder="name@ecms.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                style={{ paddingLeft: '2.5rem', width: '100%' }}
                autoComplete="email"
                required
              />
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="login-modal-password">Password</label>
            <div style={{ position: 'relative' }}>
              <Key size={16} style={{ position: 'absolute', left: '0.85rem', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
              <input
                id="login-modal-password"
                type="password"
                placeholder="Enter password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                style={{ paddingLeft: '2.5rem', width: '100%' }}
                autoComplete="current-password"
                required
              />
            </div>
            <small style={{ color: 'var(--text-muted)', marginTop: '0.25rem', display: 'block' }}>
              Default demo password for all accounts: <code>password123</code>
            </small>
          </div>

          <button 
            type="submit" 
            className="btn btn-primary" 
            style={{ width: '100%', padding: '0.75rem', marginTop: '0.5rem' }}
            disabled={loading}
          >
            {loading ? 'Authenticating...' : 'Sign In'}
          </button>
        </form>

        {/* 1-Click Fast Demo Personas */}
        <div style={{ marginTop: '1.75rem', paddingTop: '1.25rem', borderTop: '1px solid var(--border-subtle)' }}>
          <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: '700', marginBottom: '0.75rem' }}>
            1-Click Instant Persona Sign-In:
          </p>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.5rem' }}>
            <button 
              type="button" 
              className="btn btn-secondary" 
              style={{ fontSize: '0.8rem', padding: '0.5rem' }}
              onClick={() => handleQuickDemo('CAREGIVER')}
            >
              <HeartHandshake size={14} color="#10b981" />
              <span>Caregiver (Sarah)</span>
            </button>

            <button 
              type="button" 
              className="btn btn-secondary" 
              style={{ fontSize: '0.8rem', padding: '0.5rem' }}
              onClick={() => handleQuickDemo('DOCTOR')}
            >
              <Stethoscope size={14} color="#38bdf8" />
              <span>Doctor (Marcus)</span>
            </button>

            <button 
              type="button" 
              className="btn btn-secondary" 
              style={{ fontSize: '0.8rem', padding: '0.5rem' }}
              onClick={() => handleQuickDemo('SENIOR')}
            >
              <UserCheck size={14} color="#f59e0b" />
              <span>Senior (Robert)</span>
            </button>

            <button 
              type="button" 
              className="btn btn-secondary" 
              style={{ fontSize: '0.8rem', padding: '0.5rem' }}
              onClick={() => handleQuickDemo('GUARDIAN')}
            >
              <Users size={14} color="#a855f7" />
              <span>Guardian (Emma)</span>
            </button>
          </div>

          <button 
            type="button" 
            className="btn btn-secondary" 
            style={{ width: '100%', fontSize: '0.8rem', padding: '0.5rem', marginTop: '0.5rem' }}
            onClick={() => handleQuickDemo('ADMIN')}
          >
            <ShieldCheck size={14} color="#94a3b8" />
            <span>Administrator (Alistair Vance)</span>
          </button>
        </div>
      </div>
    </div>
  );
}
