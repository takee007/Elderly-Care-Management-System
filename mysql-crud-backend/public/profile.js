// profile.js  –  Client DOM Manipulation & REST API Integration
// Implements the Whiteboard Flow: Link -> Receive JSON -> Parse -> Extract -> DOM

const API_BASE_URL = 'http://localhost:5000/api/auth';
let currentUserId = 1;

// ── DOM Element References ──────────────────────────────────────────────────
const elAvatar       = document.getElementById('profile-avatar');
const elName         = document.getElementById('profile-name');
const elEmail        = document.getElementById('profile-email');
const elRole         = document.getElementById('profile-role');
const elId           = document.getElementById('profile-id');
const elPhone        = document.getElementById('profile-phone');
const elStatus       = document.getElementById('profile-status');
const elCreated      = document.getElementById('profile-created');

// Form Input Elements
const editForm       = document.getElementById('edit-profile-form');
const inputName      = document.getElementById('edit-name');
const inputPhone     = document.getElementById('edit-phone');
const validationMsg  = document.getElementById('validation-alert');
const userSelector   = document.getElementById('user-selector');

// ── 1. Fetch & DOM Populate Function ────────────────────────────────────────
async function loadUserProfile(userId) {
  try {
    // Stage 1: LINK (Initiate REST API request to Server)
    console.log(`[Client Link] Fetching REST API: ${API_BASE_URL}/profile/${userId}`);
    const response = await fetch(`${API_BASE_URL}/profile/${userId}`);

    if (!response.ok) {
      throw new Error(`Server returned HTTP ${response.status}`);
    }

    // Stage 2 & 3: RECEIVE JSON & PARSE
    const user = await response.json();
    console.log('[Receive & Parse JSON]', user);

    // Stage 4: EXTRACT fields from JSON
    const { id, full_name, email, role, phone, status, created_at } = user;

    // Stage 5: DOM MANIPULATION (Inject into HTML Interface)
    elName.textContent         = full_name || 'N/A';
    elEmail.textContent        = email || 'N/A';
    elRole.textContent         = role || 'USER';
    elId.textContent           = `#${id}`;
    elPhone.textContent        = phone || 'Not provided';
    elStatus.textContent       = status || 'ACTIVE';
    elAvatar.textContent       = full_name ? full_name.charAt(0).toUpperCase() : 'U';
    elCreated.textContent      = created_at ? new Date(created_at).toLocaleDateString() : 'N/A';

    // Populate the Edit Form inputs
    inputName.value  = full_name || '';
    inputPhone.value = phone || '';

    hideValidationMessage();
  } catch (err) {
    console.error('Failed to load profile via DOM:', err);
    showValidationMessage('error', `Could not connect to Server: ${err.message}`);
  }
}

// ── 2. Client-Side Validation ───────────────────────────────────────────────
function validateProfileInputs(name, phone) {
  // Rule 1: Full name cannot be empty and must be at least 3 characters
  if (!name || name.trim().length < 3) {
    return { valid: false, message: 'Full Name must be at least 3 characters long.' };
  }

  // Rule 2: Phone number validation (optional format check)
  if (phone && phone.trim().length > 0) {
    const phoneRegex = /^[+0-9\s\-()]{7,20}$/;
    if (!phoneRegex.test(phone.trim())) {
      return { valid: false, message: 'Please enter a valid phone number format.' };
    }
  }

  return { valid: true };
}

// ── 3. Handle Form Submit (Update Profile via REST API) ──────────────────────
editForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const newName  = inputName.value.trim();
  const newPhone = inputPhone.value.trim();

  // Step A: Client-Side Validation
  const validation = validateProfileInputs(newName, newPhone);
  if (!validation.valid) {
    showValidationMessage('error', `⚠️ Validation Error: ${validation.message}`);
    return;
  }

  try {
    showValidationMessage('info', 'Saving updates to MySQL database...');

    // Step B: REST API PUT Request (Client -> Server)
    const response = await fetch(`${API_BASE_URL}/profile/${currentUserId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        full_name: newName,
        phone: newPhone,
      }),
    });

    const result = await response.json();

    if (!response.ok) {
      throw new Error(result.error || 'Failed to update profile.');
    }

    // Step C: Update DOM with new data
    elName.textContent  = result.user.full_name;
    elPhone.textContent = result.user.phone || 'Not provided';
    elAvatar.textContent = result.user.full_name.charAt(0).toUpperCase();

    showValidationMessage('success', '✅ Profile updated successfully in MySQL!');
  } catch (err) {
    showValidationMessage('error', `❌ Error: ${err.message}`);
  }
});

// ── Helper UI Functions ─────────────────────────────────────────────────────
function showValidationMessage(type, message) {
  validationMsg.className = 'validation-msg ' + (type === 'error' ? 'msg-error' : 'msg-success');
  validationMsg.textContent = message;
  validationMsg.style.display = 'block';
}

function hideValidationMessage() {
  validationMsg.style.display = 'none';
}

// User switcher event
userSelector.addEventListener('change', (e) => {
  currentUserId = e.target.value;
  loadUserProfile(currentUserId);
});

// Initial Load on Page Startup
document.addEventListener('DOMContentLoaded', () => {
  loadUserProfile(currentUserId);
});
