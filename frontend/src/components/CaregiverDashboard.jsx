import React, { useState, useEffect } from 'react';
import { 
  Heart, 
  Pill, 
  FileText, 
  Activity, 
  AlertCircle, 
  Check, 
  X, 
  Clock, 
  User, 
  Search, 
  Plus, 
  TrendingUp,
  AlertTriangle
} from '../icons';
import { api } from '../api';

export default function CaregiverDashboard({ currentUser, onEmergencyTriggered }) {
  const [seniors, setSeniors] = useState([]);
  const [medLogs, setMedLogs] = useState([]);
  const [shiftNotes, setShiftNotes] = useState([]);
  const [search, setSearch] = useState('');
  const [loading, setLoading] = useState(true);

  // Modals
  const [selectedSenior, setSelectedSenior] = useState(null);
  const [showVitalsModal, setShowVitalsModal] = useState(false);
  const [showShiftModal, setShowShiftModal] = useState(false);

  // Vitals Form State
  const [vitalsForm, setVitalsForm] = useState({
    systolic_bp: 120,
    diastolic_bp: 80,
    pulse_rate: 72,
    spo2: 98,
    temperature: 98.6,
    blood_glucose: 110,
    notes: '',
  });

  // Shift Form State
  const [shiftForm, setShiftForm] = useState({
    shift_date: new Date().toISOString().split('T')[0],
    shift_type: 'MORNING',
    handover_to: 'Shirin Akhter, Diploma Nurse',
    notes: '',
    flagged_seniors: '',
  });

  useEffect(() => {
    loadData();
  }, [search]);

  async function loadData() {
    try {
      setLoading(true);
      const [seniorsRes, logsRes, notesRes] = await Promise.all([
        api.getSeniors(search),
        api.getMedicationLogs(),
        api.getShiftNotes(),
      ]);
      setSeniors(seniorsRes);
      setMedLogs(logsRes);
      setShiftNotes(notesRes);
    } catch (err) {
      console.error('Failed to load caregiver data:', err);
    } finally {
      setLoading(false);
    }
  }

  function handleOpenVitals(senior) {
    setSelectedSenior(senior);
    setShowVitalsModal(true);
  }

  async function handleRecordVitals(e) {
    e.preventDefault();
    if (!selectedSenior) return;

    try {
      const res = await api.recordVitals({
        senior_id: selectedSenior.id,
        systolic_bp: parseInt(vitalsForm.systolic_bp),
        diastolic_bp: parseInt(vitalsForm.diastolic_bp),
        pulse_rate: parseInt(vitalsForm.pulse_rate),
        spo2: parseInt(vitalsForm.spo2),
        temperature: parseFloat(vitalsForm.temperature),
        blood_glucose: parseInt(vitalsForm.blood_glucose),
        recorded_by: currentUser?.full_name || 'Fatema Begum, RN',
        notes: vitalsForm.notes,
      });

      if (res.is_anomaly) {
        alert(`⚠️ CLINICAL ALERT: Anomaly Detected!\n${res.anomaly_notes}\nEmergency response team automatically dispatched.`);
      }

      setShowVitalsModal(false);
      loadData();
    } catch (err) {
      alert(`Failed to save vitals: ${err.message}`);
    }
  }

  async function handleRecordMedDose(medId, seniorId, time, status) {
    try {
      await api.recordDose({
        medication_id: medId,
        senior_id: seniorId,
        scheduled_time: time,
        status: status,
        notes: `Caregiver ${status.toLowerCase()} on schedule.`,
        administered_by: currentUser?.full_name || 'Fatema Begum, RN',
      });
      loadData();
    } catch (err) {
      alert(`Error logging dose: ${err.message}`);
    }
  }

  async function handleSaveShiftNote(e) {
    e.preventDefault();
    try {
      await api.submitShiftNote({
        caregiver_id: currentUser?.id || 1,
        caregiver_name: currentUser?.full_name || 'Fatema Begum, RN',
        shift_date: shiftForm.shift_date,
        shift_type: shiftForm.shift_type,
        handover_to: shiftForm.handover_to,
        notes: shiftForm.notes,
        flagged_seniors: shiftForm.flagged_seniors,
      });
      setShowShiftModal(false);
      setShiftForm({
        shift_date: new Date().toISOString().split('T')[0],
        shift_type: 'MORNING',
        handover_to: 'Shirin Akhter, Diploma Nurse',
        notes: '',
        flagged_seniors: '',
      });
      loadData();
    } catch (err) {
      alert(`Failed to submit shift handover: ${err.message}`);
    }
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
      {/* Top Banner / Actions */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '1rem' }}>
        <div>
          <h1 style={{ fontSize: '1.8rem', fontWeight: '800', color: '#fff' }}>Caregiver Clinical Operations &amp; Telemetry Station</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginTop: '0.25rem' }}>
            Shift Lead: <strong>{currentUser?.full_name || 'Fatema Begum, BSc Nursing (RN)'}</strong> &bull; Dhanmondi Care (Padma &amp; Meghna Wings)
          </p>
        </div>
        <div style={{ display: 'flex', gap: '0.75rem', alignItems: 'center' }}>
          <div style={{ position: 'relative' }}>
            <Search size={16} style={{ position: 'absolute', left: '0.75rem', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
            <input
              id="senior-search-input"
              type="text"
              aria-label="Search senior resident by name or room number"
              placeholder="Search senior or room..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              style={{ paddingLeft: '2.25rem', width: '230px' }}
            />
          </div>
          <button 
            className="btn btn-primary"
            onClick={() => setShowShiftModal(true)}
            style={{ background: 'linear-gradient(135deg, #006a4e 0%, #059669 100%)' }}
          >
            <FileText size={16} />
            <span>Sign Shift Handover</span>
          </button>
        </div>
      </div>

      {/* Senior Resident Cards Grid */}
      <div>
        <h3 style={{ marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <User size={18} color="#10b981" />
          <span>Assigned Senior Residents ({seniors.length})</span>
        </h3>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '1.25rem', minHeight: '340px' }}>
          {seniors.map((s) => (
            <div key={s.id} className="card" style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '0.75rem' }}>
                  <div>
                    <h4 style={{ fontSize: '1.15rem', color: '#fff' }}>{s.full_name}</h4>
                    <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', fontFamily: 'var(--font-mono)' }}>
                      {s.mrn} &bull; {s.room_number}
                    </span>
                  </div>
                  <span className={`badge ${s.active_alerts_count > 0 ? 'badge-danger' : 'badge-success'}`}>
                    {s.active_alerts_count > 0 ? 'SOS Active' : 'Normal'}
                  </span>
                </div>

                <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginBottom: '0.75rem' }}>
                  <p><strong>Ailments:</strong> {s.chronic_ailments || 'None'}</p>
                  <p><strong>Allergies:</strong> <span style={{ color: '#fca5a5' }}>{s.drug_allergies || 'NKDA'}</span></p>
                </div>

                {/* Latest Vitals Capsule */}
                {s.latest_vital ? (
                  <div style={{ 
                    background: s.latest_vital.is_anomaly ? 'rgba(239, 68, 68, 0.15)' : 'rgba(15, 23, 42, 0.6)', 
                    border: `1px solid ${s.latest_vital.is_anomaly ? 'rgba(239, 68, 68, 0.4)' : 'var(--border-subtle)'}`,
                    borderRadius: 'var(--radius-md)', 
                    padding: '0.75rem',
                    marginBottom: '1rem'
                  }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.75rem', color: 'var(--text-muted)', marginBottom: '0.35rem' }}>
                      <span>Latest Telemetry</span>
                      {s.latest_vital.is_anomaly && <span style={{ color: '#f87171', fontWeight: 'bold' }}>⚠️ ANOMALY</span>}
                    </div>
                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '0.5rem', textAlign: 'center' }}>
                      <div>
                        <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>BP (mmHg)</div>
                        <div style={{ fontWeight: '700', fontFamily: 'var(--font-mono)', fontSize: '0.9rem' }}>
                          {s.latest_vital.systolic_bp}/{s.latest_vital.diastolic_bp}
                        </div>
                      </div>
                      <div>
                        <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>Pulse</div>
                        <div style={{ fontWeight: '700', fontFamily: 'var(--font-mono)', fontSize: '0.9rem' }}>
                          {s.latest_vital.pulse_rate} bpm
                        </div>
                      </div>
                      <div>
                        <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>SpO2</div>
                        <div style={{ fontWeight: '700', fontFamily: 'var(--font-mono)', fontSize: '0.9rem', color: s.latest_vital.spo2 < 95 ? '#f87171' : '#34d399' }}>
                          {s.latest_vital.spo2}%
                        </div>
                      </div>
                    </div>
                  </div>
                ) : (
                  <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', fontStyle: 'italic', marginBottom: '1rem' }}>
                    No vitals recorded this shift.
                  </div>
                )}
              </div>

              {/* Card Actions */}
              <div style={{ display: 'flex', gap: '0.5rem', borderTop: '1px solid var(--border-subtle)', paddingTop: '0.75rem' }}>
                <button 
                  className="btn btn-primary" 
                  onClick={() => handleOpenVitals(s)}
                  style={{ flex: 1, padding: '0.5rem', fontSize: '0.82rem' }}
                >
                  <Activity size={15} />
                  <span>Log Vitals</span>
                </button>
                <button 
                  className="btn btn-outline-danger"
                  onClick={async () => {
                    if (confirm(`Trigger emergency distress alert for ${s.full_name}?`)) {
                      await api.triggerSos({ senior_id: s.id, trigger_type: 'CAREGIVER_MANUAL_SOS' });
                      loadData();
                    }
                  }}
                  style={{ padding: '0.5rem 0.75rem' }}
                  title="Manual Emergency SOS"
                  aria-label={`Manual Emergency SOS for ${s.full_name}`}
                >
                  <AlertTriangle size={15} />
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Medication MAR Administration Queue */}
      <div className="card">
        <div className="card-header">
          <div className="card-title-group">
            <Pill size={20} color="#38bdf8" />
            <h3>eMAR: Today's Medication Administration Queue</h3>
          </div>
          <span className="badge badge-info">{medLogs.length} Records</span>
        </div>

        <div className="table-container">
          <table>
            <thead>
              <tr>
                <th>Scheduled Time</th>
                <th>Resident</th>
                <th>Status</th>
                <th>Administered By</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {medLogs.length > 0 ? (
                medLogs.slice(0, 8).map((log) => (
                  <tr key={log.id}>
                    <td style={{ fontFamily: 'var(--font-mono)', fontWeight: '700' }}>
                      <Clock size={13} style={{ display: 'inline', marginRight: '4px', verticalAlign: 'middle' }} />
                      {log.scheduled_time}
                    </td>
                    <td>Resident #{log.senior_id}</td>
                    <td>
                      <span className={`badge ${
                        log.status === 'GIVEN' ? 'badge-success' : log.status === 'PENDING' ? 'badge-warning' : 'badge-danger'
                      }`}>
                        {log.status}
                      </span>
                    </td>
                    <td style={{ color: 'var(--text-secondary)' }}>
                      {log.administered_by || 'Awaiting Shift Nurse'}
                    </td>
                    <td>
                      {log.status === 'PENDING' ? (
                        <div style={{ display: 'flex', gap: '0.35rem' }}>
                          <button
                            className="btn btn-primary"
                            style={{ padding: '0.3rem 0.6rem', fontSize: '0.75rem' }}
                            onClick={() => handleRecordMedDose(log.medication_id, log.senior_id, log.scheduled_time, 'GIVEN')}
                          >
                            <Check size={13} />
                            <span>Given</span>
                          </button>
                          <button
                            className="btn btn-secondary"
                            style={{ padding: '0.3rem 0.6rem', fontSize: '0.75rem' }}
                            onClick={() => handleRecordMedDose(log.medication_id, log.senior_id, log.scheduled_time, 'MISSED')}
                          >
                            <span>Missed</span>
                          </button>
                          <button
                            className="btn btn-outline-danger"
                            style={{ padding: '0.3rem 0.6rem', fontSize: '0.75rem' }}
                            onClick={() => handleRecordMedDose(log.medication_id, log.senior_id, log.scheduled_time, 'REFUSED')}
                            aria-label="Mark dose refused by resident"
                            title="Refused"
                          >
                            <X size={13} />
                          </button>
                        </div>
                      ) : (
                        <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Recorded</span>
                      )}
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan={5} style={{ textAlign: 'center', padding: '1.5rem', color: 'var(--text-muted)' }}>
                    All scheduled medications up to date.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Shift Handover Logs */}
      <div className="card">
        <div className="card-header">
          <div className="card-title-group">
            <FileText size={20} color="#a855f7" />
            <h3>Recent Shift Handover Logs</h3>
          </div>
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          {shiftNotes.map((note) => (
            <div key={note.id} style={{ 
              background: 'rgba(15, 23, 42, 0.5)', 
              padding: '1.25rem', 
              borderRadius: 'var(--radius-md)', 
              borderLeft: '4px solid #a855f7' 
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem', flexWrap: 'wrap' }}>
                <div>
                  <strong style={{ color: '#fff' }}>{note.caregiver_name}</strong> &rarr; <span style={{ color: 'var(--text-secondary)' }}>{note.handover_to}</span>
                </div>
                <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                  {note.shift_type} SHIFT &bull; {note.shift_date}
                </div>
              </div>
              <p style={{ fontSize: '0.9rem', color: 'var(--text-primary)', marginBottom: '0.5rem' }}>
                {note.notes}
              </p>
              {note.flagged_seniors && (
                <div style={{ fontSize: '0.8rem', color: '#fca5a5', background: 'rgba(239, 68, 68, 0.1)', padding: '0.35rem 0.75rem', borderRadius: 'var(--radius-sm)' }}>
                  <strong>Flagged Residents to Watch:</strong> {note.flagged_seniors}
                </div>
              )}
            </div>
          ))}
        </div>
      </div>

      {/* Vitals Telemetry Logger Modal */}
      {showVitalsModal && selectedSenior && (
        <div className="modal-overlay">
          <div className="modal-content">
            <div className="modal-header">
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                <Activity size={22} color="#10b981" />
                <h3>Log Clinical Telemetry: {selectedSenior.full_name}</h3>
              </div>
              <button className="modal-close-btn" onClick={() => setShowVitalsModal(false)} aria-label="Close vitals entry dialog">&times;</button>
            </div>

            <form onSubmit={handleRecordVitals}>
              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="vitals-systolic">Systolic BP (mmHg)</label>
                  <input
                    id="vitals-systolic"
                    type="number"
                    min="60"
                    max="240"
                    value={vitalsForm.systolic_bp}
                    onChange={(e) => setVitalsForm({ ...vitalsForm, systolic_bp: e.target.value })}
                    required
                  />
                  <small style={{ color: 'var(--text-muted)' }}>Norm: 90 - 130</small>
                </div>
                <div className="form-group">
                  <label htmlFor="vitals-diastolic">Diastolic BP (mmHg)</label>
                  <input
                    id="vitals-diastolic"
                    type="number"
                    min="40"
                    max="140"
                    value={vitalsForm.diastolic_bp}
                    onChange={(e) => setVitalsForm({ ...vitalsForm, diastolic_bp: e.target.value })}
                    required
                  />
                  <small style={{ color: 'var(--text-muted)' }}>Norm: 60 - 85</small>
                </div>
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="vitals-pulse">Pulse / Heart Rate (bpm)</label>
                  <input
                    id="vitals-pulse"
                    type="number"
                    min="30"
                    max="220"
                    value={vitalsForm.pulse_rate}
                    onChange={(e) => setVitalsForm({ ...vitalsForm, pulse_rate: e.target.value })}
                    required
                  />
                  <small style={{ color: 'var(--text-muted)' }}>Norm: 60 - 100</small>
                </div>
                <div className="form-group">
                  <label htmlFor="vitals-spo2">Oxygen Saturation SpO2 (%)</label>
                  <input
                    id="vitals-spo2"
                    type="number"
                    min="70"
                    max="100"
                    value={vitalsForm.spo2}
                    onChange={(e) => setVitalsForm({ ...vitalsForm, spo2: e.target.value })}
                    required
                  />
                  <small style={{ color: 'var(--text-muted)' }}>Norm: 95 - 100%</small>
                </div>
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="vitals-glucose">Blood Glucose (mg/dL)</label>
                  <input
                    id="vitals-glucose"
                    type="number"
                    min="40"
                    max="450"
                    value={vitalsForm.blood_glucose}
                    onChange={(e) => setVitalsForm({ ...vitalsForm, blood_glucose: e.target.value })}
                    required
                  />
                  <small style={{ color: 'var(--text-muted)' }}>Norm: 70 - 140</small>
                </div>
                <div className="form-group">
                  <label htmlFor="vitals-temp">Temperature (&deg;F)</label>
                  <input
                    id="vitals-temp"
                    type="number"
                    step="0.1"
                    min="94"
                    max="108"
                    value={vitalsForm.temperature}
                    onChange={(e) => setVitalsForm({ ...vitalsForm, temperature: e.target.value })}
                    required
                  />
                  <small style={{ color: 'var(--text-muted)' }}>Norm: 97.5 - 99.0</small>
                </div>
              </div>

              <div className="form-group">
                <label htmlFor="vitals-notes">Clinical Observations / Notes</label>
                <textarea
                  id="vitals-notes"
                  rows={2}
                  value={vitalsForm.notes}
                  placeholder="e.g. Resident was resting comfortably, took medication with lukewarm water."
                  onChange={(e) => setVitalsForm({ ...vitalsForm, notes: e.target.value })}
                  style={{ width: '100%' }}
                />
              </div>

              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '0.75rem', marginTop: '1.25rem' }}>
                <button type="button" className="btn btn-secondary" onClick={() => setShowVitalsModal(false)}>
                  Cancel
                </button>
                <button type="submit" className="btn btn-primary">
                  Save Telemetry &amp; Check Anomalies
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Shift Handover Modal */}
      {showShiftModal && (
        <div className="modal-overlay">
          <div className="modal-content">
            <div className="modal-header">
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                <FileText size={22} color="#a855f7" />
                <h3>Caregiver Shift Handover Sign-off</h3>
              </div>
              <button className="modal-close-btn" onClick={() => setShowShiftModal(false)} aria-label="Close shift handover dialog">&times;</button>
            </div>

            <form onSubmit={handleSaveShiftNote}>
              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="shift-date">Shift Date</label>
                  <input
                    id="shift-date"
                    type="date"
                    value={shiftForm.shift_date}
                    onChange={(e) => setShiftForm({ ...shiftForm, shift_date: e.target.value })}
                    required
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="shift-type">Shift Type</label>
                  <select
                    id="shift-type"
                    value={shiftForm.shift_type}
                    onChange={(e) => setShiftForm({ ...shiftForm, shift_type: e.target.value })}
                  >
                    <option value="MORNING">Morning Shift (07:00 - 15:00)</option>
                    <option value="EVENING">Evening Shift (15:00 - 23:00)</option>
                    <option value="NIGHT">Night Shift (23:00 - 07:00)</option>
                  </select>
                </div>
              </div>

              <div className="form-group">
                <label htmlFor="shift-handover-to">Handover To (Next Caregiver / Charge Nurse)</label>
                <input
                  id="shift-handover-to"
                  type="text"
                  value={shiftForm.handover_to}
                  onChange={(e) => setShiftForm({ ...shiftForm, handover_to: e.target.value })}
                  placeholder="e.g. David Miller, LPN"
                  required
                />
              </div>

              <div className="form-group">
                <label htmlFor="shift-flagged">Flagged Residents Requiring Close Monitoring</label>
                <input
                  id="shift-flagged"
                  type="text"
                  value={shiftForm.flagged_seniors}
                  onChange={(e) => setShiftForm({ ...shiftForm, flagged_seniors: e.target.value })}
                  placeholder="e.g. Robert Chen (Suite 204) - Monitor evening BP"
                />
              </div>

              <div className="form-group">
                <label htmlFor="shift-notes">Clinical Shift Notes &amp; Handover Summary</label>
                <textarea
                  id="shift-notes"
                  rows={4}
                  value={shiftForm.notes}
                  onChange={(e) => setShiftForm({ ...shiftForm, notes: e.target.value })}
                  placeholder="Detail completed meal assistances, PRN medications given, doctor visits, and resident moods..."
                  style={{ width: '100%' }}
                  required
                />
              </div>

              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '0.75rem', marginTop: '1.25rem' }}>
                <button type="button" className="btn btn-secondary" onClick={() => setShowShiftModal(false)}>
                  Cancel
                </button>
                <button type="submit" className="btn btn-primary">
                  Submit &amp; Electronically Sign Handover
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
