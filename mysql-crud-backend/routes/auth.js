// routes/auth.js  –  MySQL (mysql2) version
const router  = require('express').Router();
const bcrypt  = require('bcryptjs');
const jwt     = require('jsonwebtoken');
const pool    = require('../db/connection');
const { authenticate, authorize } = require('../middleware/auth');

const JWT_SECRET = process.env.JWT_SECRET || 'ecms_super_secret_jwt_key_2026';

function signToken(user) {
  return jwt.sign(
    { id: user.id, email: user.email, role: user.role },
    JWT_SECRET,
    { expiresIn: process.env.JWT_EXPIRES_IN || '7d' }
  );
}

/* ── User Creation Handler (for both /register and /users) ── */
async function handleCreateUser(req, res) {
  const { email, password = 'Password@123', full_name, role = 'CAREGIVER', phone } = req.body;
  if (!email || !full_name) {
    return res.status(400).json({ error: 'email and full_name are required' });
  }

  try {
    const hashed = await bcrypt.hash(password || 'Password@123', 10);
    const [result] = await pool.execute(
      `INSERT INTO users (email, hashed_password, full_name, role, phone, status)
       VALUES (?, ?, ?, ?, ?, 'ACTIVE')`,
      [email, hashed, full_name, role, phone || null]
    );

    const newUser = {
      id: result.insertId,
      email,
      full_name,
      role,
      phone: phone || null,
      status: 'ACTIVE',
      created_at: new Date().toISOString(),
    };

    console.log(`✅ [MySQL phpMyAdmin] Created user: #${newUser.id} ${newUser.full_name} (${newUser.email})`);
    return res.status(201).json(newUser);
  } catch (err) {
    if (err.code === 'ER_DUP_ENTRY') {
      return res.status(409).json({ error: `User with email "${email}" already exists` });
    }
    console.error('Create user error:', err);
    return res.status(500).json({ error: 'Server error: ' + err.message });
  }
}

/* ── POST /api/auth/register & POST /api/auth/users ─── CREATE ── */
router.post('/register', handleCreateUser);
router.post('/users', handleCreateUser);

/* ── POST /api/auth/login ──────── READ ─── */
router.post('/login', async (req, res) => {
  const { email, password } = req.body;
  if (!email || !password) return res.status(400).json({ error: 'email and password required' });

  try {
    const [rows] = await pool.execute(
      'SELECT * FROM users WHERE email=? AND status="ACTIVE"', [email]
    );
    const user = rows[0];
    if (!user) return res.status(401).json({ error: 'Invalid credentials' });

    const ok = await bcrypt.compare(password, user.hashed_password);
    if (!ok) return res.status(401).json({ error: 'Invalid credentials' });

    const { hashed_password: _, ...safeUser } = user;
    return res.json({ access_token: signToken(user), user: safeUser });
  } catch (err) {
    console.error('Login error:', err);
    return res.status(500).json({ error: 'Server error: ' + err.message });
  }
});

/* ── POST /api/auth/demo-login ─── DEMO ─── */
router.post('/demo-login', async (req, res) => {
  const { role = 'ADMIN' } = req.body;
  
  // Find or create a matching user in DB so FK constraints work
  try {
    const [rows] = await pool.execute('SELECT * FROM users WHERE role=? LIMIT 1', [role]);
    if (rows.length > 0) {
      const user = rows[0];
      const { hashed_password: _, ...safeUser } = user;
      return res.json({ access_token: signToken(user), user: safeUser });
    }
  } catch (e) {
    console.warn('Demo login DB lookup fallback:', e.message);
  }

  const demoUser = {
    id: 1,
    email: `demo_${role.toLowerCase()}@ecms.demo`,
    full_name: `Demo ${role}`,
    role,
    status: 'ACTIVE',
  };
  return res.json({ access_token: signToken(demoUser), user: demoUser });
});

/* ── GET /api/auth/me ─────────── READ ─── */
router.get('/me', async (req, res) => {
  const authHeader = req.headers['authorization'] || '';
  const token = authHeader.startsWith('Bearer ') ? authHeader.slice(7) : null;
  if (!token) return res.status(401).json({ error: 'Not authenticated' });

  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    const [rows] = await pool.execute(
      'SELECT id, email, full_name, role, phone, status, created_at FROM users WHERE id=?',
      [decoded.id]
    );
    if (!rows[0]) return res.status(404).json({ error: 'User not found' });
    return res.json(rows[0]);
  } catch (err) {
    return res.status(401).json({ error: 'Invalid token' });
  }
});

/* ── GET /api/auth/users ───────── READ LIST ─── */
router.get('/users', async (_req, res) => {
  try {
    const [rows] = await pool.execute(
      'SELECT id, email, full_name, role, phone, status, created_at FROM users ORDER BY id ASC'
    );
    return res.json(rows);
  } catch (err) {
    console.error('Get users error:', err);
    return res.status(500).json({ error: 'Server error: ' + err.message });
  }
});

/* ── PATCH /api/auth/users/:id/status ─ UPDATE ─── */
router.patch('/users/:id/status', async (req, res) => {
  const { status } = req.body;
  if (!status) {
    return res.status(400).json({ error: 'status is required' });
  }

  try {
    const [result] = await pool.execute('UPDATE users SET status=? WHERE id=?', [status, req.params.id]);
    if (result.affectedRows === 0) return res.status(404).json({ error: 'User not found' });
    return res.json({ message: 'Status updated', id: req.params.id, status });
  } catch (err) {
    console.error('Update status error:', err);
    return res.status(500).json({ error: 'Server error: ' + err.message });
  }
});

/* ── GET /api/auth/profile/:id ─── READ PROFILE ─ */
router.get('/profile/:id', async (req, res) => {
  try {
    const [rows] = await pool.execute(
      'SELECT id, email, full_name, role, phone, status, created_at FROM users WHERE id=?',
      [req.params.id]
    );
    if (!rows[0]) return res.status(404).json({ error: 'User profile not found' });
    return res.json(rows[0]);
  } catch (err) {
    console.error('Get profile error:', err);
    return res.status(500).json({ error: 'Server error: ' + err.message });
  }
});

/* ── PUT /api/auth/profile/:id ─── UPDATE PROFILE ─ */
router.put('/profile/:id', async (req, res) => {
  const { full_name, phone } = req.body;
  if (!full_name || full_name.trim().length === 0) {
    return res.status(400).json({ error: 'Full name is required' });
  }

  try {
    const [result] = await pool.execute(
      'UPDATE users SET full_name=?, phone=? WHERE id=?',
      [full_name.trim(), phone || null, req.params.id]
    );
    if (result.affectedRows === 0) return res.status(404).json({ error: 'User not found' });

    const [rows] = await pool.execute(
      'SELECT id, email, full_name, role, phone, status, created_at FROM users WHERE id=?',
      [req.params.id]
    );
    return res.json({ message: 'Profile updated successfully', user: rows[0] });
  } catch (err) {
    console.error('Update profile error:', err);
    return res.status(500).json({ error: 'Server error: ' + err.message });
  }
});

/* ── DELETE /api/auth/users/:id ─── DELETE ─── */
router.delete('/users/:id', async (req, res) => {
  try {
    const [result] = await pool.execute('DELETE FROM users WHERE id=?', [req.params.id]);
    if (result.affectedRows === 0) return res.status(404).json({ error: 'User not found' });
    return res.json({ message: 'User deleted', id: req.params.id });
  } catch (err) {
    console.error('Delete user error:', err);
    return res.status(500).json({ error: 'Server error: ' + err.message });
  }
});

module.exports = router;
