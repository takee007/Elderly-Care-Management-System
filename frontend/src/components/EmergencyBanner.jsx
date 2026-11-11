import React, { useState, useEffect } from 'react';
import { AlertTriangle, BellRing, CheckCircle, Volume2, VolumeX, ShieldAlert } from '../icons';
import { api } from '../api';

export default function EmergencyBanner({ activeAlert, onAlertResolved }) {
  const [soundEnabled, setSoundEnabled] = useState(false);
  const [showResolveModal, setShowResolveModal] = useState(false);
  const [resolveNotes, setResolveNotes] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);

  // Synthesizer Siren using Web Audio API
  useEffect(() => {
    let audioCtx = null;
    let osc = null;
    let gain = null;
    let interval = null;

    if (activeAlert && soundEnabled) {
      try {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        audioCtx = new AudioContext();
        osc = audioCtx.createOscillator();
        gain = audioCtx.createGain();

        osc.type = 'sawtooth';
        gain.gain.value = 0.15;
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();

        let high = false;
        interval = setInterval(() => {
          if (osc && audioCtx.state === 'running') {
            osc.frequency.setValueAtTime(high ? 880 : 587.33, audioCtx.currentTime);
            high = !high;
          }
        }, 350);
      } catch (err) {
        console.warn('Web Audio not allowed without user gesture', err);
      }
    }

    return () => {
      if (interval) clearInterval(interval);
      if (osc) {
        try { osc.stop(); } catch (e) {}
      }
      if (audioCtx) {
        try { audioCtx.close(); } catch (e) {}
      }
    };
  }, [activeAlert, soundEnabled]);

  if (!activeAlert) return null;

  async function handleResolve(status) {
    try {
      setIsSubmitting(true);
      await api.resolveAlert(activeAlert.id || activeAlert.alert_id, resolveNotes || 'Dispatched clinical assistance on site.', status);
      setShowResolveModal(false);
      setResolveNotes('');
      if (onAlertResolved) onAlertResolved();
    } catch (err) {
      alert(`Error updating emergency status: ${err.message}`);
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <>
      <div className="emergency-broadcast-banner">
        <div className="emergency-banner-info">
          <div className="sos-beacon">
            <AlertTriangle size={24} />
          </div>
          <div className="emergency-banner-text">
            <h3>🚨 EMERGENCY SOS DISTRESS ACTIVE &bull; NATIONAL EMERGENCY 999</h3>
            <p>
              Resident: <strong>{activeAlert.senior_name || 'Alhaj Shamsuddin Ahmed'}</strong> &bull; Location: <strong>{activeAlert.room_number || 'Suite 204 (Padma Wing)'}</strong> &bull; Emergency Mobile: <strong>{activeAlert.emergency_phone || '+880 1712-889900'}</strong> &bull; Event: <em>{activeAlert.trigger_type || 'SOS_BUTTON'}</em>
            </p>
          </div>
        </div>

        <div className="emergency-banner-actions">
          <button 
            className="btn btn-secondary"
            onClick={() => setSoundEnabled(!soundEnabled)}
            style={{ 
              background: soundEnabled ? 'rgba(255,255,255,0.25)' : 'rgba(0,0,0,0.3)',
              color: '#fff',
              padding: '0.45rem 0.8rem',
              fontSize: '0.8rem'
            }}
            title={soundEnabled ? 'Mute Siren Alarm' : 'Enable Siren Sound'}
          >
            {soundEnabled ? <Volume2 size={16} /> : <VolumeX size={16} />}
            <span>{soundEnabled ? 'Mute Siren' : 'Enable Siren'}</span>
          </button>

          <button 
            className="btn-emergency-respond"
            onClick={() => setShowResolveModal(true)}
          >
            <ShieldAlert size={18} />
            <span>Respond &amp; Triage Incident</span>
          </button>
        </div>
      </div>

      {/* Emergency Resolution Modal */}
      {showResolveModal && (
        <div className="modal-overlay">
          <div className="modal-content" style={{ borderColor: 'var(--danger)' }}>
            <div className="modal-header">
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.65rem' }}>
                <ShieldAlert size={24} color="#ef4444" />
                <h3 style={{ color: '#fff' }}>Emergency Incident Response Triage</h3>
              </div>
              <button className="modal-close-btn" onClick={() => setShowResolveModal(false)} aria-label="Close emergency resolution dialog">&times;</button>
            </div>

            <div style={{ marginBottom: '1.25rem', padding: '1rem', background: 'rgba(239, 68, 68, 0.1)', borderRadius: 'var(--radius-md)', border: '1px solid rgba(239, 68, 68, 0.3)' }}>
              <p style={{ fontSize: '0.95rem', marginBottom: '0.4rem' }}>
                <strong>Resident:</strong> {activeAlert.senior_name}
              </p>
              <p style={{ fontSize: '0.95rem', marginBottom: '0.4rem' }}>
                <strong>Room:</strong> {activeAlert.room_number}
              </p>
              <p style={{ fontSize: '0.95rem', marginBottom: '0.4rem' }}>
                <strong>Details:</strong> {activeAlert.notes || 'Emergency distress beacon active'}
              </p>
            </div>

            <div className="form-group">
              <label htmlFor="emergency-resolution-notes">Clinical Action / Resolution Log</label>
              <textarea
                id="emergency-resolution-notes"
                aria-label="Clinical action and resolution log"
                rows={3}
                placeholder="e.g. Caregiver Sarah arrived at room 204. Resident assisted. Vital signs stabilized."
                value={resolveNotes}
                onChange={(e) => setResolveNotes(e.target.value)}
                style={{ width: '100%' }}
              />
            </div>

            <div style={{ display: 'flex', gap: '0.75rem', justifyContent: 'flex-end', marginTop: '1.5rem' }}>
              <button 
                className="btn btn-secondary" 
                onClick={() => handleResolve('RESPONDING')}
                disabled={isSubmitting}
              >
                Mark as Caregiver En-Route
              </button>
              <button 
                className="btn btn-primary" 
                onClick={() => handleResolve('RESOLVED')}
                disabled={isSubmitting}
                style={{ background: 'linear-gradient(135deg, #10b981 0%, #059669 100%)' }}
              >
                <CheckCircle size={16} />
                <span>Resolve &amp; Close Emergency</span>
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
