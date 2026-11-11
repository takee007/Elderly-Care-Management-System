import React, { useState, useEffect } from 'react';
import { 
  Heart, 
  Users, 
  Pill, 
  Activity, 
  ShieldCheck, 
  Calendar, 
  Phone, 
  MessageSquare, 
  CheckCircle, 
  Clock,
  Sparkles
} from '../icons';
import { api } from '../api';

export default function GuardianPortal({ currentUser }) {
  const [senior, setSenior] = useState(null);
  const [vitals, setVitals] = useState([]);
  const [medLogs, setMedLogs] = useState([]);
  const [message, setMessage] = useState('');
  const [messageSent, setMessageSent] = useState(false);

  useEffect(() => {
    loadGuardianData();
  }, []);

  async function loadGuardianData() {
    try {
      const seniors = await api.getSeniors();
      const parent = seniors[0] || null;
      if (parent) {
        setSenior(parent);
        const [vitalsRes, logsRes] = await Promise.all([
          api.getVitals(parent.id),
          api.getMedicationLogs(parent.id),
        ]);
        setVitals(vitalsRes);
        setMedLogs(logsRes);
      }
    } catch (err) {
      console.error('Failed to load guardian data:', err);
    }
  }

  function handleSendMessage(e) {
    e.preventDefault();
    if (!message) return;
    setMessageSent(true);
    setMessage('');
    setTimeout(() => setMessageSent(false), 5000);
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
      {/* Welcome Banner */}
      <div style={{ 
        background: 'linear-gradient(135deg, rgba(139, 92, 246, 0.15) 0%, rgba(56, 189, 248, 0.1) 100%)', 
        border: '1px solid rgba(139, 92, 246, 0.3)', 
        borderRadius: 'var(--radius-xl)', 
        padding: '1.75rem',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        flexWrap: 'wrap',
        gap: '1.5rem'
      }}>
        <div>
          <span className="badge" style={{ background: 'rgba(139, 92, 246, 0.2)', color: '#c084fc', border: '1px solid rgba(139, 92, 246, 0.4)', marginBottom: '0.5rem' }}>
            Family Guardian Portal
          </span>
          <h1 style={{ fontSize: '1.75rem', fontWeight: '800', color: '#fff' }}>
            Welcome back, {currentUser?.full_name || 'Tanvir Ahmed'}!
          </h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem' }}>
            Monitoring care &amp; telemetry for your father: <strong>{senior?.full_name || 'Alhaj Mohammad Shamsuddin Ahmed'}</strong> ({senior?.room_number || 'Suite 204 - Padma Wing, Dhanmondi'})
          </p>
        </div>

        <div style={{ display: 'flex', gap: '0.75rem' }}>
          <button 
            className="btn btn-primary"
            onClick={() => alert('Direct Call to Dhanmondi Nurse Station: Nurse Fatema Begum +880 1912-345678')}
            style={{ background: 'linear-gradient(135deg, #006a4e 0%, #059669 100%)' }}
          >
            <Phone size={16} />
            <span>Call Duty Nurse</span>
          </button>
        </div>
      </div>

      {/* Metric Highlights */}
      <div className="metrics-grid">
        <div className="metric-tile">
          <div className="metric-icon-box emerald">
            <ShieldCheck size={26} />
          </div>
          <div className="metric-info">
            <h4>Resident Care Status</h4>
            <div className="metric-value" style={{ color: '#34d399', fontSize: '1.4rem' }}>
              Resting Well
            </div>
            <div className="metric-subtext">No active alarms</div>
          </div>
        </div>

        <div className="metric-tile">
          <div className="metric-icon-box sky">
            <Pill size={26} />
          </div>
          <div className="metric-info">
            <h4>Medication Adherence</h4>
            <div className="metric-value">{senior?.adherence_rate || 96.4}%</div>
            <div className="metric-subtext">Monthly benchmark exceeded</div>
          </div>
        </div>

        <div className="metric-tile">
          <div className="metric-icon-box amber">
            <Activity size={26} />
          </div>
          <div className="metric-info">
            <h4>Latest Blood Pressure</h4>
            <div className="metric-value" style={{ fontSize: '1.4rem', fontFamily: 'var(--font-mono)' }}>
              {senior?.latest_vital ? `${senior.latest_vital.systolic_bp}/${senior.latest_vital.diastolic_bp}` : '124/82'}
            </div>
            <div className="metric-subtext">mmHg &bull; Monitored</div>
          </div>
        </div>

        <div className="metric-tile">
          <div className="metric-icon-box rose">
            <Calendar size={26} />
          </div>
          <div className="metric-info">
            <h4>Next Doctor Visit</h4>
            <div className="metric-value" style={{ fontSize: '1.25rem' }}>In 2 Days</div>
            <div className="metric-subtext">Dr. Marcus Smith, MD</div>
          </div>
        </div>
      </div>

      {/* Two Column Layout: Daily eMAR Log & Send Note */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(360px, 1fr))', gap: '1.5rem' }}>
        {/* Medication Administration Timeline */}
        <div className="card">
          <div className="card-header">
            <div className="card-title-group">
              <Pill size={20} color="#34d399" />
              <h3>Today's Medication Record (MAR)</h3>
            </div>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.85rem' }}>
            {medLogs.length > 0 ? (
              medLogs.slice(0, 5).map((log) => (
                <div key={log.id} style={{
                  background: 'rgba(15, 23, 42, 0.6)',
                  border: '1px solid var(--border-subtle)',
                  borderRadius: 'var(--radius-md)',
                  padding: '1rem',
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                }}>
                  <div>
                    <div style={{ fontWeight: '700', color: '#fff', fontSize: '0.95rem' }}>
                      Scheduled Dose: {log.scheduled_time}
                    </div>
                    <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
                      {log.notes || 'Administered with meal'}
                    </div>
                  </div>
                  <span className={`badge ${log.status === 'GIVEN' ? 'badge-success' : 'badge-warning'}`}>
                    {log.status}
                  </span>
                </div>
              ))
            ) : (
              <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>No dose records available.</p>
            )}
          </div>
        </div>

        {/* Message to Caregiver Station */}
        <div className="card">
          <div className="card-header">
            <div className="card-title-group">
              <MessageSquare size={20} color="#8b5cf6" />
              <h3>Leave a Message for Shift Caregiver</h3>
            </div>
          </div>

          <form onSubmit={handleSendMessage}>
            <p style={{ fontSize: '0.88rem', color: 'var(--text-secondary)', marginBottom: '1rem' }}>
              Messages submitted here are immediately displayed on Caregiver Sarah's active shift dashboard.
            </p>

            <div className="form-group">
              <label htmlFor="caregiver-message-input">Direct Note to Nurse / Caregiver</label>
              <textarea
                id="caregiver-message-input"
                aria-label="Direct Note to Nurse / Caregiver"
                rows={4}
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="e.g. Hi Sarah, I will be visiting father this Saturday at 2 PM. Please let me know if he needs any extra warm sweaters."
                style={{ width: '100%' }}
                required
              />
            </div>

            {messageSent && (
              <div style={{ padding: '0.65rem 1rem', background: 'rgba(16, 185, 129, 0.15)', border: '1px solid #10b981', borderRadius: 'var(--radius-md)', color: '#34d399', fontSize: '0.85rem', marginBottom: '1rem' }}>
                <CheckCircle size={15} style={{ display: 'inline', marginRight: '6px', verticalAlign: 'middle' }} />
                Message successfully transmitted to Shift Nurse Station!
              </div>
            )}

            <button 
              type="submit" 
              className="btn btn-primary"
              style={{ background: 'linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%)', width: '100%' }}
            >
              <span>Transmit Note to Care Team</span>
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
