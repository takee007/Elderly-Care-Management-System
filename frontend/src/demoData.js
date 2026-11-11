// Client-side Demo Store & Offline API Router for Static Deployments (e.g. GitHub Pages)
// Mirrors backend/app/seed_data.py and FastAPI route contracts 1:1.

const DEMO_STORE_KEY = 'ecms_demo_store_v1';
const DEMO_WS_EVENT = 'ecms-demo-ws-message';

function hoursAgo(h) {
  return new Date(Date.now() - h * 3600 * 1000).toISOString();
}

function minutesAgo(m) {
  return new Date(Date.now() - m * 60 * 1000).toISOString();
}

function daysFromNow(d, h = 0) {
  return new Date(Date.now() + (d * 24 + h) * 3600 * 1000).toISOString();
}

function createInitialStore() {
  const today = new Date().toISOString().split('T')[0];
  return {
    nextIds: {
      users: 6,
      seniors: 5,
      medications: 7,
      medicationLogs: 6,
      vitals: 6,
      appointments: 3,
      emergencyAlerts: 1,
      shiftNotes: 2,
      auditLogs: 3,
    },
    users: [
      {
        id: 1,
        email: 'admin@probin.gov.bd',
        password: 'password123',
        full_name: 'Engr. Md. Tariqul Islam',
        role: 'ADMIN',
        phone: '+880 1711-098765',
        status: 'ACTIVE',
        created_at: hoursAgo(72),
      },
      {
        id: 2,
        email: 'dr.hasan@probin.org.bd',
        password: 'password123',
        full_name: 'Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS',
        role: 'DOCTOR',
        phone: '+880 1819-234567',
        status: 'ACTIVE',
        created_at: hoursAgo(72),
      },
      {
        id: 3,
        email: 'nurse.fatema@probin.org.bd',
        password: 'password123',
        full_name: 'Fatema Begum, BSc Nursing (RN)',
        role: 'CAREGIVER',
        phone: '+880 1912-345678',
        status: 'ACTIVE',
        created_at: hoursAgo(72),
      },
      {
        id: 4,
        email: 'tanvir.ahmed@gmail.com',
        password: 'password123',
        full_name: 'Tanvir Ahmed',
        role: 'GUARDIAN',
        phone: '+880 1712-889900',
        status: 'ACTIVE',
        created_at: hoursAgo(72),
      },
      {
        id: 5,
        email: 'shamsuddin@probin.org.bd',
        password: 'password123',
        full_name: 'Alhaj Mohammad Shamsuddin Ahmed',
        role: 'SENIOR',
        phone: '+880 1715-443322',
        status: 'ACTIVE',
        created_at: hoursAgo(72),
      },
    ],
    seniors: [
      {
        id: 1,
        mrn: 'BD-MRN-90210',
        full_name: 'Alhaj Mohammad Shamsuddin Ahmed',
        date_of_birth: '1948-02-15',
        gender: 'Male',
        blood_group: 'B+',
        room_number: 'Suite 204 (Padma Wing)',
        phone: '+880 1715-443322',
        address: 'Probin Nibash Assisted Living, Dhanmondi Road 8/A, Dhaka-1209',
        emergency_name: 'Tanvir Ahmed (Son)',
        emergency_phone: '+880 1712-889900',
        primary_doctor: 'Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS',
        chronic_ailments: 'Type 2 Diabetes Mellitus, Stage 1 Hypertension, Chronic Kidney Disease (Stage 2)',
        drug_allergies: 'Penicillin, Sulfa drugs',
        guardian_id: 4,
        user_id: 5,
        created_at: hoursAgo(72),
      },
      {
        id: 2,
        mrn: 'BD-MRN-90211',
        full_name: 'Begum Rokeya Chowdhury',
        date_of_birth: '1944-11-20',
        gender: 'Female',
        blood_group: 'O+',
        room_number: 'Suite 108 (Meghna Wing)',
        phone: '+880 1814-776655',
        address: 'Probin Nibash Assisted Living, Dhanmondi Road 8/A, Dhaka-1209',
        emergency_name: 'Nusrat Chowdhury (Daughter)',
        emergency_phone: '+880 1819-987654',
        primary_doctor: 'Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS',
        chronic_ailments: 'Severe Knee Osteoarthritis, Post-Cataract Glaucoma',
        drug_allergies: 'None known (NKDA)',
        guardian_id: null,
        user_id: null,
        created_at: hoursAgo(72),
      },
      {
        id: 3,
        mrn: 'BD-MRN-90212',
        full_name: 'Kazi Nurul Huda',
        date_of_birth: '1942-08-10',
        gender: 'Male',
        blood_group: 'A+',
        room_number: 'Suite 312 (Jamuna Pavilion)',
        phone: '+880 1911-332211',
        address: 'Probin Nibash Assisted Living, Dhanmondi Road 8/A, Dhaka-1209',
        emergency_name: 'Nasreen Huda (Wife)',
        emergency_phone: '+880 1915-554433',
        primary_doctor: 'Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS',
        chronic_ailments: "Early-Stage Alzheimer's Disease / Memory Care, Atrial Fibrillation",
        drug_allergies: 'Aspirin (Gastric Ulceration)',
        guardian_id: null,
        user_id: null,
        created_at: hoursAgo(72),
      },
      {
        id: 4,
        mrn: 'BD-MRN-90213',
        full_name: 'Sultana Razia Begum',
        date_of_birth: '1952-04-05',
        gender: 'Female',
        blood_group: 'AB+',
        room_number: 'Suite 102 (Surma Wing)',
        phone: '+880 1718-990011',
        address: 'Probin Nibash Assisted Living, Dhanmondi Road 8/A, Dhaka-1209',
        emergency_name: 'Farhan Razia (Son)',
        emergency_phone: '+880 1716-223344',
        primary_doctor: 'Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS',
        chronic_ailments: 'Coronary Artery Disease (Post-Stent), Bronchial Asthma',
        drug_allergies: 'Ibuprofen, NSAIDs',
        guardian_id: null,
        user_id: null,
        created_at: hoursAgo(72),
      },
    ],
    medications: [
      {
        id: 1,
        senior_id: 1,
        name: 'Tab. Comet 500mg (Metformin HCl)',
        dosage: '500 mg',
        frequency: 'Twice daily post-meal',
        scheduled_times: '08:30, 20:30',
        instructions: 'Take immediately after meals with a glass of water (Square Pharmaceuticals)',
        prescription_status: 'ACTIVE',
        prescribed_by: 'Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS',
        start_date: '2026-01-10',
        end_date: null,
      },
      {
        id: 2,
        senior_id: 1,
        name: 'Tab. Camlosart 5/20 (Amlodipine + Olmesartan)',
        dosage: '5/20 mg',
        frequency: 'Once daily morning post-breakfast',
        scheduled_times: '08:30',
        instructions: 'Monitor blood pressure prior to administration (Incepta Pharmaceuticals)',
        prescription_status: 'ACTIVE',
        prescribed_by: 'Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS',
        start_date: '2026-02-01',
        end_date: null,
      },
      {
        id: 3,
        senior_id: 1,
        name: 'Tab. Rosuva 10mg (Rosuvastatin)',
        dosage: '10 mg',
        frequency: 'Once daily at bedtime',
        scheduled_times: '22:00',
        instructions: 'Take at night before sleep with water (Renata Limited)',
        prescription_status: 'ACTIVE',
        prescribed_by: 'Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS',
        start_date: '2026-01-15',
        end_date: null,
      },
      {
        id: 4,
        senior_id: 1,
        name: 'Cap. Bicozin (Vitamin B Complex + Zinc)',
        dosage: '1 Capsule',
        frequency: 'Once daily at noon after lunch',
        scheduled_times: '13:30',
        instructions: 'General geriatric nutrition and nerve support supplement (Square Pharmaceuticals)',
        prescription_status: 'ACTIVE',
        prescribed_by: 'Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS',
        start_date: '2026-03-01',
        end_date: null,
      },
      {
        id: 5,
        senior_id: 2,
        name: 'Tab. Seclo 20mg (Omeprazole)',
        dosage: '20 mg',
        frequency: 'Once daily morning before breakfast',
        scheduled_times: '07:30',
        instructions: 'Take on an empty stomach 30 minutes before morning breakfast (Square Pharmaceuticals)',
        prescription_status: 'ACTIVE',
        prescribed_by: 'Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS',
        start_date: '2026-02-15',
        end_date: null,
      },
      {
        id: 6,
        senior_id: 3,
        name: 'Tab. Alzepil 5mg (Donepezil HCl)',
        dosage: '5 mg',
        frequency: 'Once daily at bedtime',
        scheduled_times: '21:30',
        instructions: 'Cognitive support - administer with light evening snack (Beximco Pharma)',
        prescription_status: 'ACTIVE',
        prescribed_by: 'Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS',
        start_date: '2026-04-12',
        end_date: null,
      },
    ],
    medicationLogs: [
      {
        id: 1,
        medication_id: 1,
        senior_id: 1,
        scheduled_time: '08:30',
        administered_at: hoursAgo(5),
        status: 'GIVEN',
        administered_by: 'Fatema Begum, RN',
        notes: 'Administered with morning breakfast. Resident in stable condition.',
      },
      {
        id: 2,
        medication_id: 2,
        senior_id: 1,
        scheduled_time: '08:30',
        administered_at: hoursAgo(5),
        status: 'GIVEN',
        administered_by: 'Fatema Begum, RN',
        notes: 'Blood pressure verified at 125/80 mmHg before successful administration.',
      },
      {
        id: 3,
        medication_id: 4,
        senior_id: 1,
        scheduled_time: '13:30',
        administered_at: hoursAgo(1),
        status: 'GIVEN',
        administered_by: 'Fatema Begum, RN',
        notes: 'Administered 1 capsule with post-lunch water.',
      },
      {
        id: 4,
        medication_id: 1,
        senior_id: 1,
        scheduled_time: '20:30',
        administered_at: null,
        status: 'PENDING',
        administered_by: null,
        notes: 'Scheduled for post-dinner dose.',
      },
      {
        id: 5,
        medication_id: 3,
        senior_id: 1,
        scheduled_time: '22:00',
        administered_at: null,
        status: 'PENDING',
        administered_by: null,
        notes: 'Scheduled bedtime dose.',
      },
    ],
    vitals: [
      {
        id: 1,
        senior_id: 1,
        recorded_at: hoursAgo(18),
        systolic_bp: 122,
        diastolic_bp: 80,
        pulse_rate: 72,
        spo2: 98,
        temperature: 98.4,
        blood_glucose: 112,
        is_anomaly: false,
        anomaly_notes: 'Normal baseline blood pressure and blood glucose',
        recorded_by: 'Fatema Begum, RN',
      },
      {
        id: 2,
        senior_id: 1,
        recorded_at: hoursAgo(5),
        systolic_bp: 125,
        diastolic_bp: 82,
        pulse_rate: 74,
        spo2: 97,
        temperature: 98.6,
        blood_glucose: 126,
        is_anomaly: false,
        anomaly_notes: 'Stable post-prandial glucose reading',
        recorded_by: 'Fatema Begum, RN',
      },
      {
        id: 3,
        senior_id: 1,
        recorded_at: minutesAgo(40),
        systolic_bp: 144,
        diastolic_bp: 92,
        pulse_rate: 86,
        spo2: 95,
        temperature: 98.6,
        blood_glucose: 148,
        is_anomaly: true,
        anomaly_notes: 'Elevated Blood Pressure Alert (144/92 mmHg) - Resident resting comfortably under observation',
        recorded_by: 'Fatema Begum, RN',
      },
      {
        id: 4,
        senior_id: 2,
        recorded_at: hoursAgo(4),
        systolic_bp: 118,
        diastolic_bp: 76,
        pulse_rate: 70,
        spo2: 99,
        temperature: 98.2,
        blood_glucose: 95,
        is_anomaly: false,
        anomaly_notes: 'Blood pressure and SpO2 in optimal range',
        recorded_by: 'Fatema Begum, RN',
      },
      {
        id: 5,
        senior_id: 3,
        recorded_at: hoursAgo(2),
        systolic_bp: 130,
        diastolic_bp: 82,
        pulse_rate: 80,
        spo2: 96,
        temperature: 98.4,
        blood_glucose: 105,
        is_anomaly: false,
        anomaly_notes: 'Jamuna Pavilion memory care routine observation',
        recorded_by: 'Fatema Begum, RN',
      },
    ],
    appointments: [
      {
        id: 1,
        senior_id: 1,
        doctor_id: 2,
        doctor_name: 'Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS',
        specialty: 'Geriatric Medicine & Cardiology (BSMMU/BIRDEM)',
        scheduled_at: daysFromNow(2, 4),
        consultation_type: 'TELECONSULT',
        status: 'SCHEDULED',
        notes: 'Glycemic control, kidney profile (serum creatinine) and hypertension teleconsultation review.',
        teleconsult_link: 'https://meet.jit.si/ECMS-BD-Shamsuddin-1',
      },
      {
        id: 2,
        senior_id: 3,
        doctor_id: 2,
        doctor_name: 'Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS',
        specialty: 'Neurology & Memory Care',
        scheduled_at: daysFromNow(4, 2),
        consultation_type: 'IN_PERSON',
        status: 'SCHEDULED',
        notes: 'Mini-Mental State Exam (MMSE) longitudinal cognitive progression assessment.',
        teleconsult_link: null,
      },
    ],
    emergencyAlerts: [],
    shiftNotes: [
      {
        id: 1,
        caregiver_id: 3,
        caregiver_name: 'Fatema Begum, BSc Nursing (RN)',
        shift_date: today,
        shift_type: 'MORNING',
        handover_to: 'Shirin Akhter, Diploma Nurse (Evening Shift Lead)',
        notes:
          'All morning oral medications (Comet, Camlosart) administered on schedule. Mr. Shamsuddin exhibited mild BP elevation (144/92) at 12:15 PM; resting comfortably in lounge chair, hydration encouraged. Mrs. Begum Rokeya Chowdhury completed 20 minutes assisted walking with physiotherapist. National Emergency 999 and DGHS 16263 channels active.',
        flagged_seniors:
          'Alhaj Mohammad Shamsuddin Ahmed (Suite 204 - Padma Wing) - Re-check blood pressure before dinner dose.',
        signed_at: hoursAgo(1),
      },
    ],
    auditLogs: [
      {
        id: 1,
        user_id: 1,
        user_email: 'admin@probin.gov.bd',
        action: 'SYSTEM_INITIALIZATION_BD',
        details:
          'Bangladesh Elderly Care Management System (Probin Sheba Kendro) initialized with national healthcare compliance standards.',
        ip_address: '127.0.0.1',
        timestamp: hoursAgo(24),
      },
      {
        id: 2,
        user_id: 3,
        user_email: 'nurse.fatema@probin.org.bd',
        action: 'VITALS_TELEMETRY_LOGGED',
        details:
          'Recorded routine telemetry for Padma and Meghna ward residents. Dhaka Timezone UTC+6.',
        ip_address: '127.0.0.1',
        timestamp: hoursAgo(1),
      },
    ],
  };
}

function loadStore() {
  try {
    const raw = localStorage.getItem(DEMO_STORE_KEY);
    if (raw) {
      const parsed = JSON.parse(raw);
      if (parsed && Array.isArray(parsed.users) && Array.isArray(parsed.seniors)) {
        return parsed;
      }
    }
  } catch (e) {
    // ignore corrupt localStorage
  }
  const initial = createInitialStore();
  saveStore(initial);
  return initial;
}

function saveStore(store) {
  try {
    localStorage.setItem(DEMO_STORE_KEY, JSON.stringify(store));
  } catch (e) {
    // ignore quota errors
  }
}

function getCurrentDemoUser(store) {
  try {
    const raw = localStorage.getItem('ecms_user');
    if (raw) {
      const parsed = JSON.parse(raw);
      const found = store.users.find((u) => u.id === parsed.user_id || u.email === parsed.email);
      if (found) return found;
      return parsed;
    }
  } catch (e) {}
  return store.users[2]; // Caregiver fallback
}

function emitDemoWs(payload) {
  window.dispatchEvent(new CustomEvent(DEMO_WS_EVENT, { detail: payload }));
}

function addAudit(store, user, action, details) {
  store.auditLogs.unshift({
    id: store.nextIds.auditLogs++,
    user_id: user?.id || null,
    user_email: user?.email || 'system@probin.org.bd',
    action,
    details,
    ip_address: 'demo-client',
    timestamp: new Date().toISOString(),
  });
}

function detectVitalsAnomalies(v) {
  const anomalies = [];
  if (v.systolic_bp > 140 || v.diastolic_bp > 90) {
    anomalies.push(`Hypertensive Crisis / High BP (${v.systolic_bp}/${v.diastolic_bp} mmHg)`);
  } else if (v.systolic_bp < 90 || v.diastolic_bp < 60) {
    anomalies.push(`Hypotension Warning (${v.systolic_bp}/${v.diastolic_bp} mmHg)`);
  }
  if (v.spo2 < 93) {
    anomalies.push(`Hypoxemia / Critical Low SpO2 (${v.spo2}%)`);
  }
  if (v.pulse_rate > 105) {
    anomalies.push(`Tachycardia / Elevated Pulse (${v.pulse_rate} bpm)`);
  } else if (v.pulse_rate < 50) {
    anomalies.push(`Bradycardia / Low Pulse (${v.pulse_rate} bpm)`);
  }
  if (v.blood_glucose > 180) {
    anomalies.push(`Hyperglycemia (${v.blood_glucose} mg/dL)`);
  } else if (v.blood_glucose < 70) {
    anomalies.push(`Hypoglycemia Warning (${v.blood_glucose} mg/dL)`);
  }
  if (v.temperature > 100.4) {
    anomalies.push(`Pyrexia / Fever (${v.temperature}°F)`);
  } else if (v.temperature < 96.0) {
    anomalies.push(`Hypothermia (${v.temperature}°F)`);
  }
  return anomalies.length > 0
    ? { isAnomaly: true, notes: anomalies.join(' | ') }
    : { isAnomaly: false, notes: 'Normal physiologic parameters' };
}

function sanitizeUser(u) {
  const { password, ...rest } = u;
  return rest;
}

export function createDemoEmergencyWebSocket(onMessage, onStatusChange) {
  if (onStatusChange) {
    setTimeout(() => onStatusChange('connected'), 50);
  }
  const handler = (event) => {
    if (onMessage && event.detail) {
      onMessage(event.detail);
    }
  };
  window.addEventListener(DEMO_WS_EVENT, handler);
  return {
    send: () => {},
    disconnect: () => {
      window.removeEventListener(DEMO_WS_EVENT, handler);
      if (onStatusChange) onStatusChange('disconnected');
    },
  };
}

export async function handleDemoRequest(endpoint, options = {}) {
  const method = (options.method || 'GET').toUpperCase();
  const body = options.body ? JSON.parse(options.body) : null;
  const [path, queryString] = endpoint.split('?');
  const params = new URLSearchParams(queryString || '');
  const store = loadStore();
  const currentUser = getCurrentDemoUser(store);

  // --- AUTH ---
  if (path === '/auth/login' && method === 'POST') {
    const email = (body?.email || '').trim().toLowerCase();
    const password = body?.password || '';
    const user = store.users.find((u) => u.email.toLowerCase() === email);
    if (!user || (user.password || 'password123') !== password) {
      throw new Error('Incorrect email or password');
    }
    if (user.status !== 'ACTIVE') {
      throw new Error('Account is deactivated. Contact System Administrator.');
    }
    addAudit(store, user, 'USER_LOGIN_SUCCESS', `User ${user.email} authenticated successfully with role ${user.role}`);
    saveStore(store);
    return {
      access_token: `demo-token-${user.role}-${user.id}`,
      token_type: 'bearer',
      user_id: user.id,
      email: user.email,
      full_name: user.full_name,
      role: user.role,
    };
  }

  if (path === '/auth/demo-login' && method === 'POST') {
    const targetRole = (body?.role || '').toUpperCase();
    const user = store.users.find((u) => u.role === targetRole);
    if (!user) throw new Error(`No demo user found for role ${targetRole}`);
    if (user.status !== 'ACTIVE') {
      throw new Error(`The account for role ${targetRole} is currently ${user.status.toLowerCase()}. Contact administrator.`);
    }
    return {
      access_token: `demo-token-${user.role}-${user.id}`,
      token_type: 'bearer',
      user_id: user.id,
      email: user.email,
      full_name: user.full_name,
      role: user.role,
    };
  }

  if (path === '/auth/me' && method === 'GET') {
    return sanitizeUser(currentUser);
  }

  if (path === '/auth/users' && method === 'GET') {
    return store.users.slice().sort((a, b) => a.id - b.id).map(sanitizeUser);
  }

  if (path === '/auth/users' && method === 'POST') {
    const email = (body?.email || '').trim().toLowerCase();
    if (store.users.some((u) => u.email.toLowerCase() === email)) {
      throw new Error(`Email '${email}' is already registered in ECMS.`);
    }
    const cleanRole = (body?.role || 'CAREGIVER').toUpperCase().trim();
    const newUser = {
      id: store.nextIds.users++,
      email,
      password: body?.password || 'password123',
      full_name: (body?.full_name || '').trim(),
      role: cleanRole,
      phone: body?.phone ? body.phone.trim() : null,
      status: 'ACTIVE',
      created_at: new Date().toISOString(),
    };
    store.users.push(newUser);
    addAudit(
      store,
      currentUser,
      'USER_PROVISIONED',
      `Admin ${currentUser.email} provisioned new ${cleanRole} user: ${newUser.full_name} (${newUser.email})`
    );
    saveStore(store);
    return sanitizeUser(newUser);
  }

  const userStatusMatch = path.match(/^\/auth\/users\/(\d+)\/status$/);
  if (userStatusMatch && method === 'PATCH') {
    const userId = parseInt(userStatusMatch[1], 10);
    const target = store.users.find((u) => u.id === userId);
    if (!target) throw new Error('User not found');
    const newStatus = (body?.status || '').toUpperCase().trim();
    if (target.id === currentUser.id && newStatus !== 'ACTIVE') {
      throw new Error('Security violation: System Administrator cannot terminate or suspend their own account.');
    }
    const prev = target.status;
    target.status = newStatus;
    const actionLabel =
      newStatus === 'TERMINATED'
        ? 'USER_TERMINATED'
        : newStatus === 'ACTIVE'
        ? 'USER_REACTIVATED'
        : 'USER_SUSPENDED';
    addAudit(
      store,
      currentUser,
      actionLabel,
      `Admin ${currentUser.email} set user ${target.email} status from ${prev} to ${newStatus}`
    );
    saveStore(store);
    return sanitizeUser(target);
  }

  const userDeleteMatch = path.match(/^\/auth\/users\/(\d+)$/);
  if (userDeleteMatch && method === 'DELETE') {
    const userId = parseInt(userDeleteMatch[1], 10);
    const idx = store.users.findIndex((u) => u.id === userId);
    if (idx === -1) throw new Error('User not found');
    const target = store.users[idx];
    if (target.id === currentUser.id) {
      throw new Error('Security violation: Cannot delete your own administrator account.');
    }
    const hasLinks = store.seniors.some((s) => s.user_id === userId || s.guardian_id === userId);
    let msg;
    if (hasLinks) {
      target.status = 'TERMINATED';
      msg = `User ${target.email} has linked resident records. Account was set to TERMINATED to preserve audit history.`;
    } else {
      store.users.splice(idx, 1);
      msg = `User ${target.email} was permanently deleted.`;
    }
    addAudit(store, currentUser, 'USER_TERMINATED', `Admin ${currentUser.email} removed/terminated user ${target.email} (${target.role})`);
    saveStore(store);
    return { message: msg, user_id: userId };
  }

  // --- SENIORS ---
  if (path === '/seniors/' && method === 'GET') {
    const search = (params.get('search') || '').trim().toLowerCase();
    let list = store.seniors.slice();
    if (currentUser?.role === 'GUARDIAN') {
      const assigned = list.filter((s) => s.guardian_id === currentUser.id);
      list = assigned.length > 0 ? assigned : [list[0]];
    } else if (currentUser?.role === 'SENIOR') {
      const self = list.filter((s) => s.user_id === currentUser.id);
      list = self.length > 0 ? self : [list[0]];
    }
    if (search) {
      list = list.filter(
        (s) =>
          s.full_name.toLowerCase().includes(search) ||
          s.room_number.toLowerCase().includes(search) ||
          s.mrn.toLowerCase().includes(search)
      );
    }
    list.sort((a, b) => a.room_number.localeCompare(b.room_number));

    return list.map((s) => {
      const seniorVitals = store.vitals
        .filter((v) => v.senior_id === s.id)
        .sort((a, b) => new Date(b.recorded_at) - new Date(a.recorded_at));
      const latestVital = seniorVitals[0] || null;
      const activeAlerts = store.emergencyAlerts.filter(
        (a) => a.senior_id === s.id && ['TRIGGERED', 'DISPATCHED', 'RESPONDING'].includes(a.status)
      ).length;
      const logs = store.medicationLogs.filter((l) => l.senior_id === s.id);
      const given = logs.filter((l) => l.status === 'GIVEN').length;
      const adherenceRate = logs.length > 0 ? Math.round((given / logs.length) * 1000) / 10 : 100.0;
      const guardian = store.users.find((u) => u.id === s.guardian_id);

      return {
        ...s,
        guardian_name: guardian ? guardian.full_name : null,
        active_alerts_count: activeAlerts,
        adherence_rate: adherenceRate,
        latest_vital: latestVital
          ? {
              systolic_bp: latestVital.systolic_bp,
              diastolic_bp: latestVital.diastolic_bp,
              pulse_rate: latestVital.pulse_rate,
              spo2: latestVital.spo2,
              temperature: latestVital.temperature,
              blood_glucose: latestVital.blood_glucose,
              is_anomaly: latestVital.is_anomaly,
              recorded_at: latestVital.recorded_at,
            }
          : null,
      };
    });
  }

  const seniorDetailMatch = path.match(/^\/seniors\/(\d+)$/);
  if (seniorDetailMatch && method === 'GET') {
    const seniorId = parseInt(seniorDetailMatch[1], 10);
    const s = store.seniors.find((item) => item.id === seniorId);
    if (!s) throw new Error('Senior record not found');
    const guardian = store.users.find((u) => u.id === s.guardian_id);
    const recentVitals = store.vitals
      .filter((v) => v.senior_id === seniorId)
      .sort((a, b) => new Date(b.recorded_at) - new Date(a.recorded_at))
      .slice(0, 10);
    const medications = store.medications.filter((m) => m.senior_id === seniorId);
    const alerts = store.emergencyAlerts
      .filter((a) => a.senior_id === seniorId)
      .sort((a, b) => new Date(b.triggered_at) - new Date(a.triggered_at));
    return {
      senior: {
        ...s,
        guardian_name: guardian ? guardian.full_name : null,
      },
      recent_vitals: recentVitals,
      medications,
      emergency_alerts: alerts,
    };
  }

  if (path === '/seniors/' && method === 'POST') {
    if (store.seniors.some((s) => s.mrn === body?.mrn)) {
      throw new Error('Senior with this MRN already exists');
    }
    const created = {
      ...body,
      id: store.nextIds.seniors++,
      created_at: new Date().toISOString(),
    };
    store.seniors.push(created);
    addAudit(store, currentUser, 'SENIOR_PROFILE_CREATED', `Created record for ${created.full_name} (MRN: ${created.mrn}, Room: ${created.room_number})`);
    saveStore(store);
    return created;
  }

  if (seniorDetailMatch && method === 'PUT') {
    const seniorId = parseInt(seniorDetailMatch[1], 10);
    const idx = store.seniors.findIndex((s) => s.id === seniorId);
    if (idx === -1) throw new Error('Senior record not found');
    store.seniors[idx] = { ...store.seniors[idx], ...body, id: seniorId };
    addAudit(store, currentUser, 'SENIOR_PROFILE_UPDATED', `Updated record for ${store.seniors[idx].full_name} (Room: ${store.seniors[idx].room_number})`);
    saveStore(store);
    return store.seniors[idx];
  }

  // --- VITALS ---
  if (path === '/vitals/' && method === 'GET') {
    const seniorId = params.get('senior_id') ? parseInt(params.get('senior_id'), 10) : null;
    let list = store.vitals.slice();
    if (seniorId) list = list.filter((v) => v.senior_id === seniorId);
    return list.sort((a, b) => new Date(b.recorded_at) - new Date(a.recorded_at)).slice(0, 50);
  }

  if (path === '/vitals/' && method === 'POST') {
    const senior = store.seniors.find((s) => s.id === body?.senior_id);
    if (!senior) throw new Error('Senior record not found');
    const { isAnomaly, notes: anomalyNotes } = detectVitalsAnomalies(body);
    const newVital = {
      id: store.nextIds.vitals++,
      senior_id: body.senior_id,
      recorded_at: new Date().toISOString(),
      systolic_bp: body.systolic_bp,
      diastolic_bp: body.diastolic_bp,
      pulse_rate: body.pulse_rate,
      spo2: body.spo2,
      temperature: body.temperature,
      blood_glucose: body.blood_glucose,
      is_anomaly: isAnomaly,
      anomaly_notes: isAnomaly ? anomalyNotes : null,
      recorded_by: currentUser?.full_name || body.recorded_by || 'Fatema Begum, RN',
    };
    store.vitals.push(newVital);

    if (isAnomaly) {
      const alert = {
        id: store.nextIds.emergencyAlerts++,
        senior_id: senior.id,
        triggered_at: new Date().toISOString(),
        trigger_type: 'VITALS_ANOMALY',
        latitude: 23.8151,
        longitude: 90.4255,
        status: 'TRIGGERED',
        resolved_at: null,
        resolved_by: null,
        notes: `Clinical Vital Anomaly Detected: ${anomalyNotes}`,
      };
      store.emergencyAlerts.push(alert);
      emitDemoWs({
        type: 'VITALS_ANOMALY_ALERT',
        alert_id: alert.id,
        senior_id: senior.id,
        senior_name: senior.full_name,
        room_number: senior.room_number,
        emergency_phone: senior.emergency_phone,
        trigger_type: alert.trigger_type,
        notes: anomalyNotes,
        timestamp: newVital.recorded_at,
      });
    }

    addAudit(
      store,
      currentUser,
      'VITALS_RECORDED',
      `Recorded telemetry for ${senior.full_name}. Anomaly: ${isAnomaly} (${anomalyNotes})`
    );
    saveStore(store);
    return newVital;
  }

  // --- MEDICATIONS ---
  if (path === '/medications/' && method === 'GET') {
    const seniorId = params.get('senior_id') ? parseInt(params.get('senior_id'), 10) : null;
    return seniorId
      ? store.medications.filter((m) => m.senior_id === seniorId)
      : store.medications.slice();
  }

  if (path === '/medications/' && method === 'POST') {
    const senior = store.seniors.find((s) => s.id === body?.senior_id);
    if (!senior) throw new Error('Senior record not found');
    const newMed = {
      id: store.nextIds.medications++,
      senior_id: body.senior_id,
      name: body.name,
      dosage: body.dosage,
      frequency: body.frequency,
      scheduled_times: body.scheduled_times,
      instructions: body.instructions || null,
      prescription_status: 'ACTIVE',
      prescribed_by: currentUser?.full_name || 'Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS',
      start_date: body.start_date,
      end_date: body.end_date || null,
    };
    store.medications.push(newMed);

    const times = (newMed.scheduled_times || '')
      .split(',')
      .map((t) => t.trim())
      .filter(Boolean);
    for (const t of times) {
      store.medicationLogs.push({
        id: store.nextIds.medicationLogs++,
        medication_id: newMed.id,
        senior_id: senior.id,
        scheduled_time: t,
        administered_at: null,
        status: 'PENDING',
        notes: null,
        administered_by: null,
      });
    }
    addAudit(store, currentUser, 'MEDICATION_PRESCRIBED', `Prescribed ${newMed.name} ${newMed.dosage} for ${senior.full_name}`);
    saveStore(store);
    return newMed;
  }

  if (path === '/medications/logs' && method === 'GET') {
    const seniorId = params.get('senior_id') ? parseInt(params.get('senior_id'), 10) : null;
    let logs = store.medicationLogs.slice();
    if (seniorId) logs = logs.filter((l) => l.senior_id === seniorId);
    return logs.sort((a, b) => b.id - a.id).slice(0, 100);
  }

  if (path === '/medications/logs' && method === 'POST') {
    const med = store.medications.find((m) => m.id === body?.medication_id);
    if (!med) throw new Error('Medication not found');
    const existing = store.medicationLogs.find(
      (l) =>
        l.medication_id === body.medication_id &&
        l.scheduled_time === body.scheduled_time &&
        l.status === 'PENDING'
    );
    let resultLog;
    if (existing) {
      existing.status = body.status;
      existing.administered_at = new Date().toISOString();
      existing.administered_by = currentUser?.full_name || body.administered_by || 'Fatema Begum, RN';
      existing.notes = body.notes || null;
      resultLog = existing;
    } else {
      resultLog = {
        id: store.nextIds.medicationLogs++,
        medication_id: body.medication_id,
        senior_id: body.senior_id,
        scheduled_time: body.scheduled_time,
        administered_at: new Date().toISOString(),
        status: body.status,
        notes: body.notes || null,
        administered_by: currentUser?.full_name || body.administered_by || 'Fatema Begum, RN',
      };
      store.medicationLogs.push(resultLog);
    }
    addAudit(
      store,
      currentUser,
      'MEDICATION_DOSE_LOGGED',
      `Dose of ${med.name} recorded as ${body.status} by ${currentUser?.full_name || body.administered_by}`
    );
    saveStore(store);
    return resultLog;
  }

  // --- APPOINTMENTS ---
  if (path === '/appointments/' && method === 'GET') {
    const seniorId = params.get('senior_id') ? parseInt(params.get('senior_id'), 10) : null;
    let list = store.appointments.slice();
    if (seniorId) {
      list = list.filter((a) => a.senior_id === seniorId);
    }
    list.sort((a, b) => new Date(a.scheduled_at) - new Date(b.scheduled_at));
    return list.map((appt) => {
      const senior = store.seniors.find((s) => s.id === appt.senior_id);
      return {
        ...appt,
        senior_name: senior ? senior.full_name : 'Unknown Resident',
        room_number: senior ? senior.room_number : 'N/A',
      };
    });
  }

  if (path === '/appointments/' && method === 'POST') {
    const senior = store.seniors.find((s) => s.id === body?.senior_id);
    if (!senior) throw new Error('Senior not found');
    const ts = Math.floor(new Date(body.scheduled_at).getTime() / 1000);
    const newAppt = {
      id: store.nextIds.appointments++,
      senior_id: body.senior_id,
      doctor_id: body.doctor_id || 2,
      doctor_name: body.doctor_name,
      specialty: body.specialty,
      scheduled_at: body.scheduled_at,
      consultation_type: body.consultation_type || 'IN_PERSON',
      status: 'SCHEDULED',
      notes: body.notes || null,
      teleconsult_link:
        body.teleconsult_link ||
        (body.consultation_type === 'TELECONSULT'
          ? `https://meet.jit.si/ECMS-CareConsult-${body.senior_id}-${ts}`
          : null),
    };
    store.appointments.push(newAppt);
    addAudit(
      store,
      currentUser,
      'APPOINTMENT_SCHEDULED',
      `Booked ${newAppt.consultation_type} consultation with ${newAppt.doctor_name} for ${senior.full_name}`
    );
    saveStore(store);
    return newAppt;
  }

  const apptStatusMatch = path.match(/^\/appointments\/(\d+)\/status$/);
  if (apptStatusMatch && method === 'PUT') {
    const apptId = parseInt(apptStatusMatch[1], 10);
    const appt = store.appointments.find((a) => a.id === apptId);
    if (!appt) throw new Error('Appointment not found');
    appt.status = (body?.status || '').toUpperCase();
    addAudit(store, currentUser, 'APPOINTMENT_STATUS_UPDATED', `Appointment #${apptId} updated to ${appt.status}`);
    saveStore(store);
    return { message: 'Appointment status updated successfully', status: appt.status };
  }

  // --- EMERGENCY SOS ---
  if (path === '/emergency/alerts' && method === 'GET') {
    const statusFilter = params.get('status_filter');
    let list = store.emergencyAlerts.slice();
    if (statusFilter) list = list.filter((a) => a.status === statusFilter);
    list.sort((a, b) => new Date(b.triggered_at) - new Date(a.triggered_at));
    return list.slice(0, 50).map((a) => {
      const senior = store.seniors.find((s) => s.id === a.senior_id);
      return {
        ...a,
        senior_name: senior ? senior.full_name : 'Unknown Senior',
        room_number: senior ? senior.room_number : 'N/A',
        emergency_phone: senior ? senior.emergency_phone : 'N/A',
      };
    });
  }

  if (path === '/emergency/sos' && method === 'POST') {
    const senior = store.seniors.find((s) => s.id === body?.senior_id);
    if (!senior) throw new Error('Senior record not found');
    const newAlert = {
      id: store.nextIds.emergencyAlerts++,
      senior_id: senior.id,
      triggered_at: new Date().toISOString(),
      trigger_type: body.trigger_type || 'SOS_BUTTON',
      latitude: body.latitude || 23.8151,
      longitude: body.longitude || 90.4255,
      status: 'TRIGGERED',
      resolved_at: null,
      resolved_by: null,
      notes: body.notes || 'Immediate Senior SOS distress initiated via Emergency Button',
    };
    store.emergencyAlerts.push(newAlert);
    emitDemoWs({
      type: 'EMERGENCY_SOS_ACTIVE',
      alert_id: newAlert.id,
      senior_id: senior.id,
      senior_name: senior.full_name,
      room_number: senior.room_number,
      emergency_phone: senior.emergency_phone,
      trigger_type: newAlert.trigger_type,
      latitude: newAlert.latitude,
      longitude: newAlert.longitude,
      triggered_at: newAlert.triggered_at,
      notes: newAlert.notes,
    });
    addAudit(
      store,
      currentUser,
      'EMERGENCY_SOS_TRIGGERED',
      `EMERGENCY SOS triggered for ${senior.full_name} in Room ${senior.room_number}`
    );
    saveStore(store);
    return {
      status: 'EMERGENCY_DISPATCHED',
      alert_id: newAlert.id,
      senior_name: senior.full_name,
      room_number: senior.room_number,
      message: 'Emergency dispatch notification broadcasted to all active clinical personnel and guardians.',
    };
  }

  const resolveMatch = path.match(/^\/emergency\/alerts\/(\d+)\/resolve$/);
  if (resolveMatch && method === 'POST') {
    const alertId = parseInt(resolveMatch[1], 10);
    const alert = store.emergencyAlerts.find((a) => a.id === alertId);
    if (!alert) throw new Error('Alert not found');
    const newStatus = body?.status || 'RESOLVED';
    alert.status = newStatus;
    if (newStatus === 'RESOLVED') {
      alert.resolved_at = new Date().toISOString();
    }
    alert.resolved_by = currentUser?.full_name || 'Clinical Staff';
    alert.notes = `${alert.notes || ''} | Response Update by ${alert.resolved_by}: ${body?.notes || ''}`;
    const senior = store.seniors.find((s) => s.id === alert.senior_id);
    emitDemoWs({
      type: 'EMERGENCY_SOS_RESOLVED',
      alert_id: alert.id,
      senior_name: senior ? senior.full_name : 'Resident',
      status: alert.status,
      resolved_by: alert.resolved_by,
      notes: body?.notes || '',
    });
    addAudit(
      store,
      currentUser,
      'EMERGENCY_ALERT_RESOLVED',
      `Alert #${alertId} for senior ${alert.senior_id} marked as ${newStatus} by ${alert.resolved_by}`
    );
    saveStore(store);
    return { message: 'Emergency alert status updated', alert_id: alert.id, status: alert.status };
  }

  // --- HANDOFF ---
  if (path === '/handoff/notes' && method === 'GET') {
    return store.shiftNotes
      .slice()
      .sort((a, b) => new Date(b.signed_at) - new Date(a.signed_at))
      .slice(0, 20);
  }

  if (path === '/handoff/notes' && method === 'POST') {
    const newNote = {
      id: store.nextIds.shiftNotes++,
      caregiver_id: currentUser?.id || body?.caregiver_id || 3,
      caregiver_name: currentUser?.full_name || body?.caregiver_name || 'Fatema Begum, RN',
      shift_date: body.shift_date,
      shift_type: (body.shift_type || 'MORNING').toUpperCase(),
      handover_to: body.handover_to,
      notes: body.notes,
      flagged_seniors: body.flagged_seniors || null,
      signed_at: new Date().toISOString(),
    };
    store.shiftNotes.push(newNote);
    addAudit(
      store,
      currentUser,
      'SHIFT_HANDOVER_SUBMITTED',
      `Caregiver ${newNote.caregiver_name} submitted ${newNote.shift_type} shift handover to ${newNote.handover_to}`
    );
    saveStore(store);
    return newNote;
  }

  // --- ANALYTICS ---
  if (path === '/analytics/dashboard' && method === 'GET') {
    const totalMedLogs = store.medicationLogs.length;
    const givenLogs = store.medicationLogs.filter((l) => l.status === 'GIVEN').length;
    const pendingLogs = store.medicationLogs.filter((l) => l.status === 'PENDING').length;
    const missedLogs = store.medicationLogs.filter((l) => ['MISSED', 'REFUSED'].includes(l.status)).length;
    const adherencePct = totalMedLogs > 0 ? Math.round((givenLogs / totalMedLogs) * 1000) / 10 : 96.4;

    return {
      total_seniors: store.seniors.length,
      active_emergency_alerts: store.emergencyAlerts.filter((a) =>
        ['TRIGGERED', 'DISPATCHED', 'RESPONDING'].includes(a.status)
      ).length,
      resolved_emergency_alerts: store.emergencyAlerts.filter((a) => a.status === 'RESOLVED').length,
      total_vitals_telemetry: store.vitals.length,
      vital_anomalies_flagged: store.vitals.filter((v) => v.is_anomaly).length,
      medication_adherence_rate: adherencePct,
      total_medication_logs: totalMedLogs,
      pending_doses_today: pendingLogs,
      missed_doses: missedLogs,
      care_staff: {
        caregivers: store.users.filter((u) => u.role === 'CAREGIVER').length,
        doctors: store.users.filter((u) => u.role === 'DOCTOR').length,
      },
    };
  }

  if (path === '/analytics/audit-logs' && method === 'GET') {
    return store.auditLogs
      .slice()
      .sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp))
      .slice(0, 50);
  }

  throw new Error(`Unsupported demo endpoint: ${method} ${path}`);
}

