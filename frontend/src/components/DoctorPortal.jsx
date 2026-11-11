import React, { useState, useEffect } from 'react';
import { 
  Stethoscope, 
  Video, 
  Calendar, 
  Pill, 
  Activity, 
  User, 
  Plus, 
  FileCheck, 
  Clock, 
  AlertTriangle,
  ExternalLink
} from '../icons';
import { api } from '../api';

export default function DoctorPortal({ currentUser }) {
  const [seniors, setSeniors] = useState([]);
  const [appointments, setAppointments] = useState([]);
  const [selectedSeniorId, setSelectedSeniorId] = useState(null);
  const [seniorDetails, setSeniorDetails] = useState(null);

  // Modals
  const [showPrescribeModal, setShowPrescribeModal] = useState(false);
  const [showAppointmentModal, setShowAppointmentModal] = useState(false);

  // Prescription Form
  const [prescribeForm, setPrescribeForm] = useState({
    name: '',
    dosage: '',
    frequency: 'Once daily morning',
    scheduled_times: '08:00',
    instructions: 'Take with full glass of water',
    start_date: new Date().toISOString().split('T')[0],
  });

  // Appointment Form
  const [appointmentForm, setAppointmentForm] = useState({
    senior_id: '',
    doctor_name: currentUser?.full_name || 'Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS',
    specialty: 'Geriatric Internal Medicine & Cardiology (BSMMU/BIRDEM)',
    scheduled_at: new Date(Date.now() + 86400000 * 2).toISOString().slice(0, 16),
    consultation_type: 'TELECONSULT',
    notes: 'Routine clinical follow-up, glycemic control and blood pressure review.',
  });

  useEffect(() => {
    loadDoctorData();
  }, []);

  useEffect(() => {
    if (selectedSeniorId) {
      loadSeniorDetail(selectedSeniorId);
    }
  }, [selectedSeniorId]);

  async function loadDoctorData() {
    try {
      const [seniorsRes, apptsRes] = await Promise.all([
        api.getSeniors(),
        api.getAppointments(),
      ]);
      setSeniors(seniorsRes);
      setAppointments(apptsRes);
      if (seniorsRes.length > 0 && !selectedSeniorId) {
        setSelectedSeniorId(seniorsRes[0].id);
      }
    } catch (err) {
      console.error('Failed to load doctor data:', err);
    }
  }

  async function loadSeniorDetail(id) {
    try {
      const res = await api.getSenior(id);
      setSeniorDetails(res);
    } catch (err) {
      console.error('Failed to load senior detail:', err);
    }
  }

  async function handlePrescribe(e) {
    e.preventDefault();
    if (!selectedSeniorId) return;

    try {
      await api.prescribeMedication({
        senior_id: selectedSeniorId,
        name: prescribeForm.name,
        dosage: prescribeForm.dosage,
        frequency: prescribeForm.frequency,
        scheduled_times: prescribeForm.scheduled_times,
        instructions: prescribeForm.instructions,
        start_date: prescribeForm.start_date,
      });
      setShowPrescribeModal(false);
      setPrescribeForm({
        name: '',
        dosage: '',
        frequency: 'Once daily morning',
        scheduled_times: '08:00',
        instructions: 'Take with full glass of water',
        start_date: new Date().toISOString().split('T')[0],
      });
      loadSeniorDetail(selectedSeniorId);
      alert('Prescription successfully signed and added to resident eMAR queue.');
    } catch (err) {
      alert(`Prescription error: ${err.message}`);
    }
  }

  async function handleBookAppointment(e) {
    e.preventDefault();
    try {
      await api.bookAppointment({
        senior_id: parseInt(appointmentForm.senior_id || selectedSeniorId),
        doctor_id: currentUser?.id || 2,
        doctor_name: appointmentForm.doctor_name,
        specialty: appointmentForm.specialty,
        scheduled_at: new Date(appointmentForm.scheduled_at).toISOString(),
        consultation_type: appointmentForm.consultation_type,
        notes: appointmentForm.notes,
      });
      setShowAppointmentModal(false);
      const apptsRes = await api.getAppointments();
      setAppointments(apptsRes);
      alert('Consultation scheduled successfully.');
    } catch (err) {
      alert(`Appointment error: ${err.message}`);
    }
  }

  const selectedSenior = seniors.find((s) => s.id === selectedSeniorId);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '1rem' }}>
        <div>
          <h1 style={{ fontSize: '1.8rem', fontWeight: '800', color: '#fff' }}>Geriatric Specialist Clinical Portal (Physician EHR)</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
            Senior Geriatric Consultant: <strong>{currentUser?.full_name || 'Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS'}</strong> &bull; BMDC Reg: A-48219 (BSMMU/BIRDEM)
          </p>
        </div>
        <div style={{ display: 'flex', gap: '0.75rem' }}>
          <button className="btn btn-secondary" onClick={() => setShowAppointmentModal(true)}>
            <Calendar size={16} />
            <span>Schedule Consult</span>
          </button>
          <button className="btn btn-primary" onClick={() => setShowPrescribeModal(true)} disabled={!selectedSeniorId} style={{ background: 'linear-gradient(135deg, #006a4e 0%, #059669 100%)' }}>
            <Pill size={16} />
            <span>Prescribe Medication</span>
          </button>
        </div>
      </div>

      {/* Telehealth & Appointments Section */}
      <div className="card">
        <div className="card-header">
          <div className="card-title-group">
            <Video size={20} color="#38bdf8" />
            <h3>Scheduled Telehealth &amp; Clinical Reviews</h3>
          </div>
          <span className="badge badge-info">{appointments.length} Consultations</span>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '1rem' }}>
          {appointments.map((appt) => (
            <div key={appt.id} style={{ 
              background: 'rgba(15, 23, 42, 0.6)', 
              border: '1px solid var(--border-subtle)', 
              borderRadius: 'var(--radius-md)', 
              padding: '1.25rem' 
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '0.5rem' }}>
                <div>
                  <h4 style={{ color: '#fff' }}>{appt.senior_name}</h4>
                  <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>
                    Room: {appt.room_number} &bull; {appt.specialty}
                  </span>
                </div>
                <span className={`badge ${appt.consultation_type === 'TELECONSULT' ? 'badge-info' : 'badge-success'}`}>
                  {appt.consultation_type}
                </span>
              </div>

              <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--text-secondary)', fontSize: '0.85rem', marginBottom: '0.75rem' }}>
                <Clock size={14} />
                <span>{new Date(appt.scheduled_at).toLocaleString()}</span>
              </div>

              <p style={{ fontSize: '0.85rem', color: 'var(--text-primary)', marginBottom: '1rem' }}>
                {appt.notes}
              </p>

              {appt.consultation_type === 'TELECONSULT' && appt.teleconsult_link && (
                <a
                  href={appt.teleconsult_link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn btn-primary"
                  style={{ width: '100%', textDecoration: 'none', fontSize: '0.82rem' }}
                >
                  <Video size={15} />
                  <span>Launch Secure Teleconsult</span>
                  <ExternalLink size={13} style={{ marginLeft: 'auto' }} />
                </a>
              )}
            </div>
          ))}
        </div>
      </div>

      {/* Two Column Layout: Resident Selector & EHR Details */}
      <div style={{ display: 'grid', gridTemplateColumns: '300px 1fr', gap: '1.5rem', alignItems: 'start' }}>
        {/* Resident Selector List */}
        <div className="card" style={{ padding: '1rem' }}>
          <h4 style={{ fontSize: '0.9rem', color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '0.75rem', paddingLeft: '0.5rem' }}>
            Select Patient
          </h4>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
            {seniors.map((s) => (
              <div
                key={s.id}
                onClick={() => setSelectedSeniorId(s.id)}
                style={{
                  padding: '0.75rem 1rem',
                  borderRadius: 'var(--radius-md)',
                  cursor: 'pointer',
                  background: s.id === selectedSeniorId ? 'rgba(56, 189, 248, 0.15)' : 'transparent',
                  border: `1px solid ${s.id === selectedSeniorId ? 'var(--secondary-light)' : 'transparent'}`,
                  transition: 'all 0.15s ease',
                }}
              >
                <div style={{ fontWeight: '700', color: s.id === selectedSeniorId ? '#38bdf8' : '#fff' }}>
                  {s.full_name}
                </div>
                <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                  {s.mrn} &bull; {s.room_number}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Selected Senior Clinical Record (EHR) */}
        {seniorDetails ? (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            {/* Senior Banner */}
            <div className="card" style={{ borderLeft: '4px solid var(--secondary-light)' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '1rem' }}>
                <div>
                  <h3 style={{ fontSize: '1.4rem' }}>{seniorDetails.senior.full_name}</h3>
                  <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem' }}>
                    MRN: <strong>{seniorDetails.senior.mrn}</strong> &bull; DOB: {seniorDetails.senior.date_of_birth} &bull; Gender: {seniorDetails.senior.gender} &bull; Blood: <strong>{seniorDetails.senior.blood_group}</strong>
                  </p>
                </div>
                <span className="badge badge-success">Assisted Living Ward</span>
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '1rem', marginTop: '1rem', paddingTop: '1rem', borderTop: '1px solid var(--border-subtle)' }}>
                <div>
                  <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>CHRONIC CONDITIONS</span>
                  <p style={{ fontSize: '0.9rem', fontWeight: '600' }}>{seniorDetails.senior.chronic_ailments || 'None'}</p>
                </div>
                <div>
                  <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>KNOWN DRUG ALLERGIES</span>
                  <p style={{ fontSize: '0.9rem', fontWeight: '600', color: '#f87171' }}>
                    {seniorDetails.senior.drug_allergies || 'No known drug allergies (NKDA)'}
                  </p>
                </div>
                <div>
                  <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>EMERGENCY CONTACT</span>
                  <p style={{ fontSize: '0.9rem' }}>
                    {seniorDetails.senior.emergency_name} ({seniorDetails.senior.emergency_phone})
                  </p>
                </div>
              </div>
            </div>

            {/* Longitudinal Vitals Telemetry History */}
            <div className="card">
              <div className="card-header">
                <div className="card-title-group">
                  <Activity size={20} color="#10b981" />
                  <h3>Physiological Vitals Telemetry Log</h3>
                </div>
              </div>

              <div className="table-container">
                <table>
                  <thead>
                    <tr>
                      <th>Timestamp</th>
                      <th>BP (mmHg)</th>
                      <th>Heart Rate</th>
                      <th>SpO2</th>
                      <th>Glucose</th>
                      <th>Temp</th>
                      <th>Clinical Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    {seniorDetails.recent_vitals.map((v) => (
                      <tr key={v.id} style={{ background: v.is_anomaly ? 'rgba(239, 68, 68, 0.08)' : 'transparent' }}>
                        <td style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                          {new Date(v.recorded_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', month: 'short', day: 'numeric' })}
                        </td>
                        <td style={{ fontWeight: '700', fontFamily: 'var(--font-mono)' }}>
                          {v.systolic_bp} / {v.diastolic_bp}
                        </td>
                        <td style={{ fontFamily: 'var(--font-mono)' }}>{v.pulse_rate} bpm</td>
                        <td style={{ fontFamily: 'var(--font-mono)', color: v.spo2 < 95 ? '#f87171' : 'inherit' }}>
                          {v.spo2}%
                        </td>
                        <td style={{ fontFamily: 'var(--font-mono)' }}>{v.blood_glucose} mg/dL</td>
                        <td style={{ fontFamily: 'var(--font-mono)' }}>{v.temperature}&deg;F</td>
                        <td>
                          {v.is_anomaly ? (
                            <span className="vital-anomaly-pill">
                              <AlertTriangle size={12} />
                              <span>{v.anomaly_notes}</span>
                            </span>
                          ) : (
                            <span className="badge badge-success">Optimal</span>
                          )}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

            {/* Active Prescriptions */}
            <div className="card">
              <div className="card-header">
                <div className="card-title-group">
                  <Pill size={20} color="#fbbf24" />
                  <h3>Active Medication Regimen (Doctor Orders)</h3>
                </div>
                <button className="btn btn-primary" style={{ padding: '0.4rem 0.8rem', fontSize: '0.78rem' }} onClick={() => setShowPrescribeModal(true)}>
                  <Plus size={14} />
                  <span>Add Prescription</span>
                </button>
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '1rem' }}>
                {seniorDetails.medications.map((m) => (
                  <div key={m.id} style={{ background: 'rgba(15, 23, 42, 0.6)', border: '1px solid var(--border-subtle)', borderRadius: 'var(--radius-md)', padding: '1rem' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '0.5rem' }}>
                      <h4 style={{ color: '#fff' }}>{m.name}</h4>
                      <span className="badge badge-success">{m.dosage}</span>
                    </div>
                    <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginBottom: '0.5rem' }}>
                      <p><strong>Frequency:</strong> {m.frequency}</p>
                      <p><strong>Schedule:</strong> {m.scheduled_times}</p>
                      <p><strong>Instructions:</strong> {m.instructions || 'Standard oral administration.'}</p>
                    </div>
                    <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', borderTop: '1px solid var(--border-subtle)', paddingTop: '0.5rem' }}>
                      Prescribed by {m.prescribed_by} &bull; Started {m.start_date}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        ) : (
          <div className="card" style={{ textAlign: 'center', padding: '3rem', color: 'var(--text-muted)' }}>
            Select a resident to inspect their clinical records.
          </div>
        )}
      </div>

      {/* Prescribe Modal */}
      {showPrescribeModal && selectedSenior && (
        <div className="modal-overlay">
          <div className="modal-content">
            <div className="modal-header">
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                <Pill size={22} color="#10b981" />
                <h3>Electronic Prescription: {selectedSenior.full_name}</h3>
              </div>
              <button className="modal-close-btn" onClick={() => setShowPrescribeModal(false)} aria-label="Close prescription dialog">&times;</button>
            </div>

            <form onSubmit={handlePrescribe}>
              <div className="form-group">
                <label htmlFor="prescribe-med-name">Medication Name &amp; Formulation</label>
                <input
                  id="prescribe-med-name"
                  type="text"
                  placeholder="e.g. Lisinopril or Atorvastatin Calcium"
                  value={prescribeForm.name}
                  onChange={(e) => setPrescribeForm({ ...prescribeForm, name: e.target.value })}
                  required
                />
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="prescribe-med-dosage">Dosage &amp; Strength</label>
                  <input
                    id="prescribe-med-dosage"
                    type="text"
                    placeholder="e.g. 10 mg or 500 mg"
                    value={prescribeForm.dosage}
                    onChange={(e) => setPrescribeForm({ ...prescribeForm, dosage: e.target.value })}
                    required
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="prescribe-med-frequency">Frequency</label>
                  <select
                    id="prescribe-med-frequency"
                    value={prescribeForm.frequency}
                    onChange={(e) => setPrescribeForm({ ...prescribeForm, frequency: e.target.value })}
                  >
                    <option value="Once daily morning">Once daily morning</option>
                    <option value="Twice daily with meals">Twice daily with meals</option>
                    <option value="Three times daily">Three times daily</option>
                    <option value="Once daily at bedtime">Once daily at bedtime</option>
                    <option value="PRN as needed">PRN as needed</option>
                  </select>
                </div>
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="prescribe-med-times">Scheduled Administration Times</label>
                  <input
                    id="prescribe-med-times"
                    type="text"
                    placeholder="e.g. 08:00 or 08:00, 20:00"
                    value={prescribeForm.scheduled_times}
                    onChange={(e) => setPrescribeForm({ ...prescribeForm, scheduled_times: e.target.value })}
                    required
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="prescribe-med-start">Start Date</label>
                  <input
                    id="prescribe-med-start"
                    type="date"
                    value={prescribeForm.start_date}
                    onChange={(e) => setPrescribeForm({ ...prescribeForm, start_date: e.target.value })}
                    required
                  />
                </div>
              </div>

              <div className="form-group">
                <label htmlFor="prescribe-med-instructions">Clinical Administration Instructions &amp; Warnings</label>
                <textarea
                  id="prescribe-med-instructions"
                  rows={3}
                  placeholder="e.g. Monitor blood pressure before giving. Take with 8oz water."
                  value={prescribeForm.instructions}
                  onChange={(e) => setPrescribeForm({ ...prescribeForm, instructions: e.target.value })}
                  style={{ width: '100%' }}
                />
              </div>

              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '0.75rem', marginTop: '1.25rem' }}>
                <button type="button" className="btn btn-secondary" onClick={() => setShowPrescribeModal(false)}>
                  Cancel
                </button>
                <button type="submit" className="btn btn-primary">
                  Sign &amp; Issue Prescription
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Appointment Modal */}
      {showAppointmentModal && (
        <div className="modal-overlay">
          <div className="modal-content">
            <div className="modal-header">
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                <Calendar size={22} color="#38bdf8" />
                <h3>Book Clinical / Telehealth Consultation</h3>
              </div>
              <button className="modal-close-btn" onClick={() => setShowAppointmentModal(false)} aria-label="Close consultation booking dialog">&times;</button>
            </div>

            <form onSubmit={handleBookAppointment}>
              <div className="form-group">
                <label htmlFor="appointment-senior-select">Select Resident</label>
                <select
                  id="appointment-senior-select"
                  value={appointmentForm.senior_id || selectedSeniorId}
                  onChange={(e) => setAppointmentForm({ ...appointmentForm, senior_id: e.target.value })}
                  required
                >
                  {seniors.map((s) => (
                    <option key={s.id} value={s.id}>
                      {s.full_name} ({s.mrn} - {s.room_number})
                    </option>
                  ))}
                </select>
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="appointment-consult-type">Consultation Type</label>
                  <select
                    id="appointment-consult-type"
                    value={appointmentForm.consultation_type}
                    onChange={(e) => setAppointmentForm({ ...appointmentForm, consultation_type: e.target.value })}
                  >
                    <option value="TELECONSULT">Video Teleconsultation (Virtual Link)</option>
                    <option value="IN_PERSON">In-Person Ward Examination</option>
                  </select>
                </div>
                <div className="form-group">
                  <label htmlFor="appointment-scheduled-at">Scheduled Date &amp; Time</label>
                  <input
                    id="appointment-scheduled-at"
                    type="datetime-local"
                    value={appointmentForm.scheduled_at}
                    onChange={(e) => setAppointmentForm({ ...appointmentForm, scheduled_at: e.target.value })}
                    required
                  />
                </div>
              </div>

              <div className="form-group">
                <label htmlFor="appointment-specialty">Specialty / Clinical Objective</label>
                <input
                  id="appointment-specialty"
                  type="text"
                  value={appointmentForm.specialty}
                  onChange={(e) => setAppointmentForm({ ...appointmentForm, specialty: e.target.value })}
                  required
                />
              </div>

              <div className="form-group">
                <label htmlFor="appointment-clinical-notes">Clinical Notes</label>
                <textarea
                  id="appointment-clinical-notes"
                  rows={3}
                  value={appointmentForm.notes}
                  onChange={(e) => setAppointmentForm({ ...appointmentForm, notes: e.target.value })}
                  style={{ width: '100%' }}
                />
              </div>

              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '0.75rem', marginTop: '1.25rem' }}>
                <button type="button" className="btn btn-secondary" onClick={() => setShowAppointmentModal(false)}>
                  Cancel
                </button>
                <button type="submit" className="btn btn-primary">
                  Confirm Consultation
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
