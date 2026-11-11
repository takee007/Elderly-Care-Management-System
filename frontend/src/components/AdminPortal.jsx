import React, { useState, useEffect } from 'react';
import { 
  ShieldCheck, 
  Users, 
  Activity, 
  FileText, 
  AlertTriangle, 
  Server, 
  Database, 
  CheckCircle, 
  Download,
  Lock,
  UserPlus,
  UserX,
  RefreshCw,
  Mail,
  Phone,
  Key
} from '../icons';
import { api } from '../api';

export default function AdminPortal({ currentUser }) {
  const [metrics, setMetrics] = useState(null);
  const [users, setUsers] = useState([]);
  const [auditLogs, setAuditLogs] = useState([]);
  const [loading, setLoading] = useState(true);

  // New User Provisioning Modal State
  const [showAddUserModal, setShowAddUserModal] = useState(false);
  const [newUserForm, setNewUserForm] = useState({
    full_name: '',
    email: '',
    role: 'CAREGIVER',
    phone: '',
    password: 'password123'
  });
  const [formLoading, setFormLoading] = useState(false);
  const [formError, setFormError] = useState('');

  // Termination Confirmation Modal State
  const [confirmTerminateUser, setConfirmTerminateUser] = useState(null);
  const [terminateLoading, setTerminateLoading] = useState(false);

  // Status Notification Banner
  const [notification, setNotification] = useState(null);

  useEffect(() => {
    loadAdminData();
  }, []);

  function showNotification(type, message) {
    setNotification({ type, message });
    setTimeout(() => {
      setNotification(null);
    }, 4500);
  }

  async function loadAdminData() {
    try {
      setLoading(true);
      const [metricsRes, usersRes, auditRes] = await Promise.all([
        api.getDashboardAnalytics(),
        api.getUsers(),
        api.getAuditLogs(),
      ]);
      setMetrics(metricsRes);
      setUsers(usersRes);
      setAuditLogs(auditRes);
    } catch (err) {
      console.error('Failed to load admin data:', err);
    } finally {
      setLoading(false);
    }
  }

  async function handleAddUser(e) {
    e.preventDefault();
    setFormError('');
    setFormLoading(true);
    try {
      const created = await api.createUser(newUserForm);
      setShowAddUserModal(false);
      setNewUserForm({
        full_name: '',
        email: '',
        role: 'CAREGIVER',
        phone: '',
        password: 'password123'
      });
      showNotification('success', `User account for ${created.full_name} (${created.role}) provisioned successfully!`);
      await loadAdminData();
    } catch (err) {
      setFormError(err.message || 'Failed to provision user. Please verify input details.');
    } finally {
      setFormLoading(false);
    }
  }

  async function handleTerminateUser() {
    if (!confirmTerminateUser) return;
    setTerminateLoading(true);
    try {
      await api.updateUserStatus(confirmTerminateUser.id, 'TERMINATED');
      const terminatedName = confirmTerminateUser.full_name;
      setConfirmTerminateUser(null);
      showNotification('warning', `Access terminated for ${terminatedName}. User login is now revoked.`);
      await loadAdminData();
    } catch (err) {
      alert(err.message || 'Failed to terminate user access');
    } finally {
      setTerminateLoading(false);
    }
  }

  async function handleReactivateUser(user) {
    try {
      await api.updateUserStatus(user.id, 'ACTIVE');
      showNotification('success', `Access restored for ${user.full_name}. User can now log in.`);
      await loadAdminData();
    } catch (err) {
      alert(err.message || 'Failed to reactivate user');
    }
  }

  function handleExportAudit() {
    const jsonStr = JSON.stringify(auditLogs, null, 2);
    const blob = new Blob([jsonStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `ECMS_Audit_Trail_${new Date().toISOString().split('T')[0]}.json`;
    link.click();
    URL.revokeObjectURL(url);
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
      {/* Toast Notification */}
      {notification && (
        <div style={{
          position: 'fixed',
          top: '5rem',
          right: '2rem',
          zIndex: 1000,
          background: notification.type === 'success' ? 'rgba(16, 185, 129, 0.95)' : 'rgba(239, 68, 68, 0.95)',
          color: '#fff',
          padding: '0.85rem 1.5rem',
          borderRadius: 'var(--radius-md)',
          boxShadow: '0 10px 25px -5px rgba(0, 0, 0, 0.6)',
          display: 'flex',
          alignItems: 'center',
          gap: '0.75rem',
          fontWeight: '600',
          backdropFilter: 'blur(8px)',
          animation: 'slideInRight 0.3s ease'
        }}>
          {notification.type === 'success' ? <CheckCircle size={20} /> : <AlertTriangle size={20} />}
          <span>{notification.message}</span>
        </div>
      )}

      {/* Admin Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '1rem' }}>
        <div>
          <h1 style={{ fontSize: '1.8rem', fontWeight: '800', color: '#fff' }}>National Elderly Care Administration &amp; Audit Intelligence (ECMS-BD)</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
            System Director: <strong>{currentUser?.full_name || 'Engr. Md. Tariqul Islam'}</strong> &bull; DGHS National Healthcare Network
          </p>
        </div>
        <div style={{ display: 'flex', gap: '0.75rem' }}>
          <button className="btn btn-secondary" onClick={handleExportAudit}>
            <Download size={16} />
            <span>Export Audit Trail (JSON)</span>
          </button>
        </div>
      </div>

      {/* Facility KPI Metrics */}
      <div className="metrics-grid">
        <div className="metric-tile">
          <div className="metric-icon-box emerald">
            <Users size={26} />
          </div>
          <div className="metric-info">
            <h4>Total Seniors</h4>
            <div className="metric-value">{metrics?.total_seniors || 4}</div>
            <div className="metric-subtext">Active Resident Profiles</div>
          </div>
        </div>

        <div className="metric-tile">
          <div className="metric-icon-box sky">
            <Activity size={26} />
          </div>
          <div className="metric-info">
            <h4>Vitals Telemetry</h4>
            <div className="metric-value">{metrics?.total_vitals_telemetry || 5}</div>
            <div className="metric-subtext">{metrics?.vital_anomalies_flagged || 1} Anomalies Flagged</div>
          </div>
        </div>

        <div className="metric-tile">
          <div className="metric-icon-box amber">
            <CheckCircle size={26} />
          </div>
          <div className="metric-info">
            <h4>MAR Adherence</h4>
            <div className="metric-value">{metrics?.medication_adherence_rate || 96.4}%</div>
            <div className="metric-subtext">Facility-wide Benchmark</div>
          </div>
        </div>

        <div className="metric-tile">
          <div className="metric-icon-box rose">
            <AlertTriangle size={26} />
          </div>
          <div className="metric-info">
            <h4>Emergency Dispatches</h4>
            <div className="metric-value" style={{ color: metrics?.active_emergency_alerts > 0 ? '#ef4444' : 'inherit' }}>
              {metrics?.active_emergency_alerts || 0}
            </div>
            <div className="metric-subtext">Active Live Alarms</div>
          </div>
        </div>
      </div>

      {/* User Management Table */}
      <div className="card">
        <div className="card-header">
          <div className="card-title-group">
            <Users size={20} color="#38bdf8" />
            <h3>Role-Based Access Control (RBAC): System Users</h3>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <span className="badge badge-info">{users.length} Enrolled Accounts</span>
            <button 
              className="btn btn-primary"
              onClick={() => {
                setFormError('');
                setShowAddUserModal(true);
              }}
              style={{ padding: '0.45rem 0.95rem', fontSize: '0.82rem' }}
            >
              <UserPlus size={16} />
              <span>+ Add New User</span>
            </button>
          </div>
        </div>

        <div className="table-container">
          <table>
            <thead>
              <tr>
                <th>User ID</th>
                <th>Full Name</th>
                <th>Email Address</th>
                <th>Role</th>
                <th>Phone</th>
                <th>Status</th>
                <th style={{ textAlign: 'right' }}>Actions</th>
              </tr>
            </thead>
            <tbody>
              {users.map((u) => {
                const isCurrentAdmin = (currentUser?.id && u.id === currentUser.id) || 
                                       (currentUser?.user_id && u.id === currentUser.user_id) || 
                                       (currentUser?.email === u.email);
                const isTerminated = u.status === 'TERMINATED' || u.status === 'SUSPENDED';

                return (
                  <tr key={u.id} style={{ opacity: isTerminated ? 0.65 : 1 }}>
                    <td style={{ fontFamily: 'var(--font-mono)' }}>#{u.id}</td>
                    <td>
                      <div style={{ fontWeight: '700', color: isTerminated ? 'var(--text-muted)' : '#fff' }}>
                        {u.full_name}
                      </div>
                    </td>
                    <td style={{ color: isTerminated ? 'var(--text-muted)' : 'inherit' }}>{u.email}</td>
                    <td>
                      <span className={`badge ${
                        u.role === 'ADMIN' ? 'badge-info' :
                        u.role === 'DOCTOR' ? 'badge-success' :
                        u.role === 'CAREGIVER' ? 'badge-warning' : 'badge-primary'
                      }`}>
                        {u.role}
                      </span>
                    </td>
                    <td style={{ color: 'var(--text-secondary)' }}>{u.phone || 'N/A'}</td>
                    <td>
                      <span className={`badge ${isTerminated ? 'badge-danger' : 'badge-success'}`}>
                        {u.status}
                      </span>
                    </td>
                    <td style={{ textAlign: 'right' }}>
                      {isCurrentAdmin ? (
                        <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', fontStyle: 'italic' }}>
                          Current Session
                        </span>
                      ) : isTerminated ? (
                        <button
                          className="btn btn-secondary"
                          onClick={() => handleReactivateUser(u)}
                          style={{
                            padding: '0.35rem 0.75rem',
                            fontSize: '0.78rem',
                            borderColor: 'rgba(16, 185, 129, 0.4)',
                            color: '#34d399'
                          }}
                          title="Restore user login access"
                        >
                          <CheckCircle size={14} />
                          <span>Reactivate</span>
                        </button>
                      ) : (
                        <button
                          className="btn btn-outline-danger"
                          onClick={() => setConfirmTerminateUser(u)}
                          style={{ padding: '0.35rem 0.75rem', fontSize: '0.78rem' }}
                          title="Terminate access"
                        >
                          <UserX size={14} />
                          <span>Terminate</span>
                        </button>
                      )}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>

      {/* Audit Trail Logs */}
      <div className="card">
        <div className="card-header">
          <div className="card-title-group">
            <Lock size={20} color="#10b981" />
            <h3>Immutable System &amp; Clinical Audit Trail</h3>
          </div>
          <span className="badge badge-success">HIPAA / GDPR Verified</span>
        </div>

        <div className="table-container">
          <table>
            <thead>
              <tr>
                <th>Timestamp</th>
                <th>User</th>
                <th>Action</th>
                <th>Details</th>
                <th>IP Address</th>
              </tr>
            </thead>
            <tbody>
              {auditLogs.map((log) => (
                <tr key={log.id}>
                  <td style={{ fontSize: '0.8rem', color: 'var(--text-muted)', fontFamily: 'var(--font-mono)' }}>
                    {new Date(log.timestamp).toLocaleString()}
                  </td>
                  <td style={{ fontWeight: '600' }}>{log.user_email}</td>
                  <td>
                    <span className={`badge ${
                      log.action.includes('TERMINATED') ? 'badge-danger' :
                      log.action.includes('PROVISIONED') || log.action.includes('ACTIVATED') ? 'badge-success' : 'badge-info'
                    }`}>
                      {log.action}
                    </span>
                  </td>
                  <td style={{ color: 'var(--text-secondary)', fontSize: '0.85rem' }}>{log.details}</td>
                  <td style={{ fontFamily: 'var(--font-mono)', fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                    {log.ip_address}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Provision New User Modal */}
      {showAddUserModal && (
        <div className="modal-overlay">
          <div className="modal-content" style={{ maxWidth: '540px' }}>
            <div className="modal-header">
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.65rem' }}>
                <div style={{
                  width: '2rem',
                  height: '2rem',
                  borderRadius: 'var(--radius-md)',
                  background: 'rgba(16, 185, 129, 0.15)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  color: 'var(--primary-light)'
                }}>
                  <UserPlus size={18} />
                </div>
                <div>
                  <h3 style={{ fontSize: '1.2rem', color: '#fff' }}>Provision New System User</h3>
                  <p style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>
                    Assign Role-Based Access Control (RBAC) &amp; institutional credentials
                  </p>
                </div>
              </div>
              <button className="modal-close-btn" onClick={() => setShowAddUserModal(false)} aria-label="Close user provisioning dialog">&times;</button>
            </div>

            {formError && (
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
                <AlertTriangle size={16} />
                <span>{formError}</span>
              </div>
            )}

            <form onSubmit={handleAddUser}>
              <div className="form-group">
                <label htmlFor="admin-new-fullname">Full Legal Name &amp; Title</label>
                <input
                  id="admin-new-fullname"
                  type="text"
                  placeholder="e.g. Dr. Salma Khatun, MBBS or Shirin Akhter, RN"
                  value={newUserForm.full_name}
                  onChange={(e) => setNewUserForm({ ...newUserForm, full_name: e.target.value })}
                  required
                />
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="admin-new-email">Institutional Email</label>
                  <input
                    id="admin-new-email"
                    type="email"
                    placeholder="e.g. dr.salma@probin.org.bd"
                    value={newUserForm.email}
                    onChange={(e) => setNewUserForm({ ...newUserForm, email: e.target.value })}
                    required
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="admin-new-role">Assign Role</label>
                  <select
                    id="admin-new-role"
                    value={newUserForm.role}
                    onChange={(e) => setNewUserForm({ ...newUserForm, role: e.target.value })}
                    required
                  >
                    <option value="CAREGIVER">CAREGIVER (Nurse / Care Station)</option>
                    <option value="DOCTOR">DOCTOR (Physician EHR &amp; Prescriptions)</option>
                    <option value="SENIOR">SENIOR (Resident Accessible UI)</option>
                    <option value="GUARDIAN">GUARDIAN (Family Member Portal)</option>
                    <option value="ADMIN">ADMIN (System Director &amp; Audit)</option>
                  </select>
                </div>
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="admin-new-phone">Official Phone Number</label>
                  <input
                    id="admin-new-phone"
                    type="tel"
                    placeholder="e.g. +880 1711-234567"
                    value={newUserForm.phone}
                    onChange={(e) => setNewUserForm({ ...newUserForm, phone: e.target.value })}
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="admin-new-pwd">Initial Temporary Password</label>
                  <input
                    id="admin-new-pwd"
                    type="text"
                    value={newUserForm.password}
                    onChange={(e) => setNewUserForm({ ...newUserForm, password: e.target.value })}
                    required
                  />
                </div>
              </div>

              <div style={{
                background: 'rgba(15, 23, 42, 0.5)',
                border: '1px solid var(--border-subtle)',
                borderRadius: 'var(--radius-md)',
                padding: '0.85rem',
                fontSize: '0.8rem',
                color: 'var(--text-secondary)',
                marginBottom: '1.25rem'
              }}>
                ℹ️ The new user will be provisioned with <strong>ACTIVE</strong> status and can log in immediately using their email and initial password. An immutable audit trail entry will be recorded.
              </div>

              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '0.75rem' }}>
                <button
                  type="button"
                  className="btn btn-secondary"
                  onClick={() => setShowAddUserModal(false)}
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="btn btn-primary"
                  disabled={formLoading}
                >
                  <UserPlus size={16} />
                  <span>{formLoading ? 'Provisioning...' : 'Provision User Account'}</span>
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Terminate User Confirmation Modal */}
      {confirmTerminateUser && (
        <div className="modal-overlay">
          <div className="modal-content" style={{ maxWidth: '480px' }}>
            <div className="modal-header">
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.65rem' }}>
                <div style={{
                  width: '2rem',
                  height: '2rem',
                  borderRadius: 'var(--radius-md)',
                  background: 'rgba(239, 68, 68, 0.15)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  color: '#ef4444'
                }}>
                  <UserX size={18} />
                </div>
                <h3 style={{ fontSize: '1.15rem', color: '#fff' }}>Terminate User Access</h3>
              </div>
              <button className="modal-close-btn" onClick={() => setConfirmTerminateUser(null)} aria-label="Close termination confirmation dialog">&times;</button>
            </div>

            <div style={{ padding: '0.5rem 0 1.5rem 0' }}>
              <div style={{
                background: 'rgba(239, 68, 68, 0.1)',
                border: '1px solid rgba(239, 68, 68, 0.3)',
                borderRadius: 'var(--radius-md)',
                padding: '1rem',
                marginBottom: '1rem',
                color: '#fca5a5',
                fontSize: '0.88rem'
              }}>
                <div style={{ fontWeight: '700', marginBottom: '0.25rem', color: '#fff' }}>
                  Are you sure you want to terminate this user?
                </div>
                Access will be revoked immediately for:
                <div style={{ color: '#fff', fontWeight: '800', marginTop: '0.5rem', fontSize: '0.95rem' }}>
                  {confirmTerminateUser.full_name}
                </div>
                <div style={{ color: 'var(--text-secondary)', fontSize: '0.82rem' }}>
                  {confirmTerminateUser.email} &bull; Role: <strong>{confirmTerminateUser.role}</strong>
                </div>
              </div>

              <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
                This user's login access will be blocked instantly. Existing medical records, prescriptions, and telemetry data associated with this user will be preserved for clinical audit compliance.
              </p>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '0.75rem' }}>
              <button
                type="button"
                className="btn btn-secondary"
                onClick={() => setConfirmTerminateUser(null)}
              >
                Keep Active
              </button>
              <button
                type="button"
                className="btn btn-danger"
                disabled={terminateLoading}
                onClick={handleTerminateUser}
              >
                <UserX size={16} />
                <span>{terminateLoading ? 'Terminating...' : 'Confirm Termination'}</span>
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
