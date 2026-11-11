import { handleDemoRequest, createDemoEmergencyWebSocket } from './demoData';

// ECMS Centralized API & Real-time WebSocket Client
const BASE_URL = 'http://localhost:8000/api/v1';
const WS_URL = 'ws://localhost:8000/ws/emergency';

function isLocalHost() {
  if (typeof window === 'undefined') return false;
  const host = window.location.hostname;
  return host === 'localhost' || host === '127.0.0.1';
}

let useDemoFallback = !isLocalHost();

function getStoredToken() {
  return localStorage.getItem('ecms_token') || '';
}

export function setStoredAuth(token, user) {
  if (token) {
    localStorage.setItem('ecms_token', token);
  } else {
    localStorage.removeItem('ecms_token');
  }
  if (user) {
    localStorage.setItem('ecms_user', JSON.stringify(user));
  } else {
    localStorage.removeItem('ecms_user');
  }
}

export function getStoredUser() {
  try {
    const raw = localStorage.getItem('ecms_user');
    return raw ? JSON.parse(raw) : null;
  } catch (e) {
    return null;
  }
}

async function request(endpoint, options = {}) {
  if (useDemoFallback) {
    return handleDemoRequest(endpoint, options);
  }

  const token = getStoredToken();
  const headers = {
    'Content-Type': 'application/json',
    ...(options.headers || {}),
  };

  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  let response;
  try {
    response = await fetch(`${BASE_URL}${endpoint}`, {
      ...options,
      headers,
    });
  } catch (networkErr) {
    // Backend server is offline locally -> seamlessly fall back to built-in demo store
    useDemoFallback = true;
    return handleDemoRequest(endpoint, options);
  }

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    const message = errorData.detail || `Request failed with status ${response.status}`;
    throw new Error(message);
  }

  return response.json();
}

export const api = {
  // Authentication
  login: (email, password) =>
    request('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    }),

  demoLogin: (role) =>
    request('/auth/demo-login', {
      method: 'POST',
      body: JSON.stringify({ role }),
    }),

  getMe: () => request('/auth/me'),
  getUsers: () => request('/auth/users'),
  createUser: (data) =>
    request('/auth/users', {
      method: 'POST',
      body: JSON.stringify(data),
    }),
  updateUserStatus: (userId, status) =>
    request(`/auth/users/${userId}/status`, {
      method: 'PATCH',
      body: JSON.stringify({ status }),
    }),
  deleteUser: (userId) =>
    request(`/auth/users/${userId}`, {
      method: 'DELETE',
    }),

  // Seniors
  getSeniors: (search = '') =>
    request(`/seniors/${search ? `?search=${encodeURIComponent(search)}` : ''}`),
  getSenior: (id) => request(`/seniors/${id}`),
  createSenior: (data) =>
    request('/seniors/', {
      method: 'POST',
      body: JSON.stringify(data),
    }),
  updateSenior: (id, data) =>
    request(`/seniors/${id}`, {
      method: 'PUT',
      body: JSON.stringify(data),
    }),

  // Vitals
  getVitals: (seniorId = null) =>
    request(`/vitals/${seniorId ? `?senior_id=${seniorId}` : ''}`),
  recordVitals: (data) =>
    request('/vitals/', {
      method: 'POST',
      body: JSON.stringify(data),
    }),

  // Medications
  getMedications: (seniorId = null) =>
    request(`/medications/${seniorId ? `?senior_id=${seniorId}` : ''}`),
  prescribeMedication: (data) =>
    request('/medications/', {
      method: 'POST',
      body: JSON.stringify(data),
    }),
  getMedicationLogs: (seniorId = null) =>
    request(`/medications/logs${seniorId ? `?senior_id=${seniorId}` : ''}`),
  recordDose: (data) =>
    request('/medications/logs', {
      method: 'POST',
      body: JSON.stringify(data),
    }),

  // Appointments
  getAppointments: (seniorId = null) =>
    request(`/appointments/${seniorId ? `?senior_id=${seniorId}` : ''}`),
  bookAppointment: (data) =>
    request('/appointments/', {
      method: 'POST',
      body: JSON.stringify(data),
    }),
  updateAppointmentStatus: (id, status) =>
    request(`/appointments/${id}/status`, {
      method: 'PUT',
      body: JSON.stringify({ status }),
    }),

  // Emergency SOS
  getEmergencyAlerts: (statusFilter = null) =>
    request(`/emergency/alerts${statusFilter ? `?status_filter=${statusFilter}` : ''}`),
  triggerSos: (data) =>
    request('/emergency/sos', {
      method: 'POST',
      body: JSON.stringify(data),
    }),
  resolveAlert: (id, notes, status = 'RESOLVED') =>
    request(`/emergency/alerts/${id}/resolve`, {
      method: 'POST',
      body: JSON.stringify({ notes, status }),
    }),

  // Shift Handoff
  getShiftNotes: () => request('/handoff/notes'),
  submitShiftNote: (data) =>
    request('/handoff/notes', {
      method: 'POST',
      body: JSON.stringify(data),
    }),

  // Analytics & Admin
  getDashboardAnalytics: () => request('/analytics/dashboard'),
  getAuditLogs: () => request('/analytics/audit-logs'),
};

// WebSocket Service with Auto-Reconnect + Static Demo Fallback
export function createEmergencyWebSocket(onMessage, onStatusChange) {
  if (useDemoFallback) {
    return createDemoEmergencyWebSocket(onMessage, onStatusChange);
  }

  let socket = null;
  let reconnectTimer = null;
  let isClosedManually = false;
  let demoBridge = null;

  function connect() {
    if (useDemoFallback) {
      if (!demoBridge) {
        demoBridge = createDemoEmergencyWebSocket(onMessage, onStatusChange);
      }
      return;
    }

    try {
      socket = new WebSocket(WS_URL);

      socket.onopen = () => {
        if (onStatusChange) onStatusChange('connected');
        // send keepalive every 30s
        socket.pingInterval = setInterval(() => {
          if (socket && socket.readyState === WebSocket.OPEN) {
            socket.send(JSON.stringify({ type: 'PING' }));
          }
        }, 30000);
      };

      socket.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          if (onMessage) onMessage(data);
        } catch (e) {
          console.warn('Malformed WS message', e);
        }
      };

      socket.onclose = () => {
        if (socket && socket.pingInterval) clearInterval(socket.pingInterval);
        if (useDemoFallback) {
          if (!demoBridge) {
            demoBridge = createDemoEmergencyWebSocket(onMessage, onStatusChange);
          }
          return;
        }
        if (onStatusChange) onStatusChange('disconnected');
        if (!isClosedManually) {
          reconnectTimer = setTimeout(connect, 3000);
        }
      };

      socket.onerror = () => {
        if (onStatusChange) onStatusChange('error');
      };
    } catch (err) {
      if (!isClosedManually) {
        reconnectTimer = setTimeout(connect, 4000);
      }
    }
  }

  connect();

  return {
    send: (msg) => {
      if (demoBridge) return demoBridge.send(msg);
      if (socket && socket.readyState === WebSocket.OPEN) {
        socket.send(typeof msg === 'string' ? msg : JSON.stringify(msg));
      }
    },
    disconnect: () => {
      isClosedManually = true;
      if (reconnectTimer) clearTimeout(reconnectTimer);
      if (demoBridge) demoBridge.disconnect();
      if (socket) {
        if (socket.pingInterval) clearInterval(socket.pingInterval);
        socket.close();
      }
    },
  };
}
