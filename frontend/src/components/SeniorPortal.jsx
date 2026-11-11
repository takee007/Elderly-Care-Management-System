import React, { useState, useEffect } from 'react';
import { 
  AlertTriangle, 
  Pill, 
  PhoneCall, 
  Calendar, 
  Heart, 
  CheckCircle2, 
  XCircle,
  Smile,
  Shield,
  Volume2
} from '../icons';
import { api } from '../api';

export default function SeniorPortal({ currentUser, onEmergencyTriggered }) {
  const [seniorData, setSeniorData] = useState(null);
  const [medications, setMedications] = useState([]);
  const [takenMeds, setTakenMeds] = useState({});
  const [isCountingDown, setIsCountingDown] = useState(false);
  const [countdown, setCountdown] = useState(5);
  const [sosSent, setSosSent] = useState(false);

  useEffect(() => {
    loadSeniorProfile();
  }, []);

  async function loadSeniorProfile() {
    try {
      const seniors = await api.getSeniors();
      const current = seniors[0] || null;
      if (current) {
        setSeniorData(current);
        const meds = await api.getMedications(current.id);
        setMedications(meds);
      }
    } catch (err) {
      console.error('Failed to load senior portal data:', err);
    }
  }

  // 5-Second SOS Countdown Timer with Sound
  useEffect(() => {
    let timer = null;
    let audioCtx = null;
    let osc = null;

    if (isCountingDown && countdown > 0) {
      try {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        audioCtx = new AudioContext();
        osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(440, audioCtx.currentTime);
        gain.gain.value = 0.1;
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        setTimeout(() => {
          try { osc.stop(); audioCtx.close(); } catch (e) {}
        }, 150);
      } catch (e) {}

      timer = setTimeout(() => {
        setCountdown((c) => c - 1);
      }, 1000);
    } else if (isCountingDown && countdown === 0) {
      sendEmergencySos();
    }

    return () => {
      if (timer) clearTimeout(timer);
    };
  }, [isCountingDown, countdown]);

  function handleStartSos() {
    setCountdown(5);
    setIsCountingDown(true);
    setSosSent(false);
  }

  function handleCancelSos() {
    setIsCountingDown(false);
    setCountdown(5);
  }

  async function sendEmergencySos() {
    setIsCountingDown(false);
    if (!seniorData) return;

    try {
      await api.triggerSos({
        senior_id: seniorData.id,
        trigger_type: 'SOS_BUTTON',
        notes: `Senior resident ${seniorData.full_name} initiated Emergency Call from Suite 204 (Padma Wing). Immediate nursing and ambulance response dispatched.`,
      });
      setSosSent(true);
      if (onEmergencyTriggered) onEmergencyTriggered();
    } catch (err) {
      alert(`Emergency transmission error: ${err.message}`);
    }
  }

  function toggleMedicine(medId) {
    setTakenMeds((prev) => ({
      ...prev,
      [medId]: !prev[medId],
    }));
  }

  return (
    <div className="senior-portal">
      {/* Friendly Accessible Welcome Header */}
      <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '2.5rem', fontWeight: '900', color: '#fff', letterSpacing: '-0.02em' }}>
          Hello, {seniorData?.full_name ? seniorData.full_name.split(' ')[0] : 'Shamsuddin'} Sahib!
        </h1>
        <p style={{ fontSize: '1.25rem', color: '#94a3b8', marginTop: '0.25rem' }}>
          Your Room: <strong style={{ color: '#38bdf8' }}>{seniorData?.room_number || 'Suite 204 (Padma Wing)'}</strong> &bull; Nurse on Duty: <strong style={{ color: '#34d399' }}>Fatema Begum (RN)</strong>
        </p>
      </div>

      {/* Giant WCAG Accessible SOS Emergency Button */}
      <div className="senior-sos-card">
        <h2 style={{ fontSize: '1.8rem', color: '#fca5a5', marginBottom: '1.25rem' }}>
          Need Immediate Medical Help or Emergency Assistance?
        </h2>
        
        <button 
          className="senior-sos-button"
          onClick={handleStartSos}
          aria-label="Emergency Help and Call Nurse Button"
        >
          <AlertTriangle size={60} strokeWidth={2.5} />
          <span className="senior-sos-text">HELP</span>
          <span className="senior-sos-sub">SOS 999 &bull; CALL NURSE</span>
        </button>

        {sosSent && (
          <div style={{ 
            background: 'rgba(239, 68, 68, 0.3)', 
            border: '2px solid #ef4444', 
            borderRadius: 'var(--radius-lg)', 
            padding: '1.25rem',
            color: '#fff',
            fontSize: '1.2rem',
            fontWeight: '700',
            maxWidth: '580px',
            margin: '0 auto'
          }}>
            🚨 HELP IS ON THE WAY! Nurse Fatema Begum and emergency response team have been dispatched to Suite 204. National Emergency 999 alerted. Please remain seated calmly.
          </div>
        )}

        <p style={{ fontSize: '1.2rem', color: '#fecaca', marginTop: '1rem' }}>
          Pressing this large button activates an alarm at the Nurse Station and notifies your son Tanvir Ahmed.
        </p>
      </div>

      {/* Large Touch Action Cards Grid */}
      <div className="senior-cards-grid">
        {/* Medicine Check-off */}
        <div className="senior-action-card medicine-card">
          <div>
            <div className="senior-card-top">
              <div className="senior-card-icon" style={{ background: 'rgba(16, 185, 129, 0.2)', color: '#34d399' }}>
                <Pill size={36} />
              </div>
              <div>
                <h3 className="senior-card-heading">My Medicines Today</h3>
                <p style={{ color: '#94a3b8', fontSize: '1.1875rem' }}>Tap checkbox when medicine is taken</p>
              </div>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem', marginTop: '1rem' }}>
              {medications.map((m) => {
                const isChecked = !!takenMeds[m.id];
                return (
                  <div
                    key={m.id}
                    onClick={() => toggleMedicine(m.id)}
                    style={{
                      background: isChecked ? 'rgba(16, 185, 129, 0.25)' : 'rgba(15, 23, 42, 0.7)',
                      border: `2px solid ${isChecked ? '#10b981' : 'var(--border-subtle)'}`,
                      borderRadius: 'var(--radius-md)',
                      padding: '1rem',
                      minHeight: '64px',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'space-between',
                      cursor: 'pointer',
                      transition: 'all 0.2s ease',
                    }}
                  >
                    <div>
                      <div style={{ fontSize: '1.3rem', fontWeight: '800', color: '#fff' }}>
                        {m.name}
                      </div>
                      <div style={{ fontSize: '1.1875rem', color: 'var(--text-secondary)' }}>
                        {m.dosage} &bull; {m.frequency} ({m.scheduled_times})
                      </div>
                    </div>
                    {isChecked ? (
                      <CheckCircle2 size={34} color="#10b981" />
                    ) : (
                      <div style={{ width: 30, height: 30, borderRadius: '50%', border: '2px solid #64748b' }} />
                    )}
                  </div>
                );
              })}
            </div>
          </div>
        </div>

        {/* Daily Schedule & Routine */}
        <div className="senior-action-card">
          <div>
            <div className="senior-card-top">
              <div className="senior-card-icon" style={{ background: 'rgba(56, 189, 248, 0.2)', color: '#38bdf8' }}>
                <Calendar size={36} />
              </div>
              <div>
                <h3 className="senior-card-heading">Today's Schedule</h3>
                <p style={{ color: '#94a3b8', fontSize: '1.1875rem' }}>Daily Routine</p>
              </div>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.85rem', marginTop: '1rem' }}>
              <div style={{ padding: '0.85rem 1rem', background: 'rgba(15, 23, 42, 0.6)', borderRadius: 'var(--radius-md)', borderLeft: '4px solid #10b981' }}>
                <strong style={{ fontSize: '1.25rem', color: '#fff' }}>08:30 AM &bull; Breakfast &amp; Vitals Telemetry</strong>
                <p style={{ fontSize: '1.1875rem', color: 'var(--text-secondary)' }}>Room tray served with morning medications</p>
              </div>
              <div style={{ padding: '0.85rem 1rem', background: 'rgba(15, 23, 42, 0.6)', borderRadius: 'var(--radius-md)', borderLeft: '4px solid #38bdf8' }}>
                <strong style={{ fontSize: '1.25rem', color: '#fff' }}>11:00 AM &bull; Garden Walk &amp; Relaxation</strong>
                <p style={{ fontSize: '1.1875rem', color: 'var(--text-secondary)' }}>Dhanmondi Care courtyard fresh air &amp; gentle stretch</p>
              </div>
              <div style={{ padding: '0.85rem 1rem', background: 'rgba(15, 23, 42, 0.6)', borderRadius: 'var(--radius-md)', borderLeft: '4px solid #a855f7' }}>
                <strong style={{ fontSize: '1.25rem', color: '#fff' }}>03:30 PM &bull; Video Call with Son Tanvir</strong>
                <p style={{ fontSize: '1.1875rem', color: 'var(--text-secondary)' }}>Tablet assistance provided by Nurse Fatema</p>
              </div>
            </div>
          </div>
        </div>

        {/* Direct Call Loved One or Nurse */}
        <div className="senior-action-card">
          <div>
            <div className="senior-card-top">
              <div className="senior-card-icon" style={{ background: 'rgba(168, 85, 247, 0.2)', color: '#c084fc' }}>
                <PhoneCall size={36} />
              </div>
              <div>
                <h3 className="senior-card-heading">Family &amp; Nurse Speed Dial</h3>
                <p style={{ color: '#94a3b8', fontSize: '1.1875rem' }}>1-Tap Direct Call</p>
              </div>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem', marginTop: '1rem' }}>
              <button 
                onClick={() => alert('Calling Son Tanvir Ahmed: +880 1712-889900...')}
                style={{
                  background: 'linear-gradient(135deg, #7c3aed 0%, #6d28d9 100%)',
                  color: '#fff',
                  padding: '1.25rem',
                  minHeight: '64px',
                  borderRadius: 'var(--radius-lg)',
                  fontSize: '1.3rem',
                  fontWeight: '800',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  gap: '0.75rem',
                  boxShadow: '0 4px 15px rgba(124, 58, 237, 0.4)',
                }}
              >
                <PhoneCall size={26} />
                <span>Call Son Tanvir</span>
              </button>

              <button 
                onClick={() => alert('Paging Nurse Fatema Begum at Dhanmondi Station...')}
                style={{
                  background: 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)',
                  color: '#fff',
                  padding: '1.25rem',
                  minHeight: '64px',
                  borderRadius: 'var(--radius-lg)',
                  fontSize: '1.3rem',
                  fontWeight: '800',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  gap: '0.75rem',
                  boxShadow: '0 4px 15px rgba(2, 132, 199, 0.4)',
                }}
              >
                <Heart size={26} />
                <span>Call Duty Nurse</span>
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* 5-Second SOS Cancellation Modal */}
      {isCountingDown && (
        <div className="modal-overlay">
          <div className="countdown-modal">
            <AlertTriangle size={64} color="#f87171" style={{ margin: '0 auto' }} />
            <h2 style={{ fontSize: '2rem', color: '#fff', marginTop: '1rem' }}>
              SENDING EMERGENCY SIGNAL...
            </h2>
            <div className="countdown-digits">{countdown}</div>
            <p style={{ fontSize: '1.25rem', color: '#fecaca', marginBottom: '1.5rem' }}>
              If touched by mistake, tap the button below immediately!
            </p>

            <button className="btn-cancel-sos" onClick={handleCancelSos}>
              ❌ CANCEL SOS (I AM SAFE)
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
