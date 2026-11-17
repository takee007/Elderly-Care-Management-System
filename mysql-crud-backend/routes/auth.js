// routes/auth.js
// CRUD: Create user (register), Read user (login / me), Update status, Delete
const router  = require('express').Router();
const bcrypt  = require('bcryptjs');
const jwt     = require('jsonwebtoken');
const pool    = require('../db/connection');
const { authenticate, authorize } = require('../middleware/auth');

/* ── helpers ──────────────────────────────────────────────────────────────── */
function signToken(user) {
  return jwt.sign(
    { id: user.id, email: user.email, role: user.role },
    process.env.JWT_SECRET,
    { expiresIn: process.env.JWT_EXPIRES_IN || '7d' }
  );
}

/* ── POST /api/auth/register ─────────────────────────────── CREATE ───────── */
router.post('/register', async (req, res) => {
  const { email, password, full_name, role = 'CAREGIVER', phone } = req.body;
  if (!email || !password || !full_name)
    return res.status(400).json({ error: 'email, password and full_name are required' });

  try {
    const hashed = await bcrypt.hash(password, 10);
    const [result] = await pool.execute(
      `INSERT INTO users (email, hashed_password, full_name, role, phone)
       VALUES (?, ?, ?, ?, ?)`,
      [email, hashed, full_name, role, phone || null]
    );
    return res.status(201).json({ id: result.insertId, email, full_name, role });
  } catch (err) {
    if (err.code === 'ER_DUP_ENTRY')
      return res.status(409).json({ error: 'Email already in use' });
    console.error(err);
    return res.status(500).json({ error: 'Server error' });
  }
});

/* ── POST /api/auth/login ────────────────────────────────── READ ─────────── */
router.post('/login', async (req, res) => {
  const { email, password } = req.body;
  if (!email || !password)
    return res.status(400).json({ error: 'email and password are required' });

  try {
    const [rows] = await pool.execute(
      'SELECT * FROM users WHERE email = ? AND status = "ACTIVE"', [email]
    );
    const user = rows[0];
    if (!user) return res.status(401).json({ error: 'Invalid credentials' });

    const ok = await bcrypt.compare(password, user.hashed_password);
    if (!ok) return res.status(401).json({ error: 'Invalid credentials' });

    const { hashed_password: _, ...safeUser } = user;
    return res.json({ access_token: signToken(user), user: safeUser });
  } catch (err) {
    console.error(err);
    return res.status(500).json({ error: 'Server error' });
  }
});

/* ── GET /api/auth/me ────────────────────────────────────── READ ─────────── */
router.get('/me', authenticate, async (req, res) => {
  const [rows] = await pool.execute(
    'SELECT id,email,full_name,role,phone,status,created_at FROM users WHERE id=?',
    [req.user.id]
  );
  if (!rows[0]) return res.status(404).json({ error: 'User not found' });
  return res.json(rows[0]);
});

/* ── GET /api/auth/users ─────────────────────────────────── READ ─────────── */
router.get('/users', authenticate, authorize('ADMIN'), async (_req, res) => {
  const [rows] = await pool.execute(
    'SELECT id,email,full_name,role,phone,status,created_at FROM users ORDER BY created_at DESC'
  );
  return res.json(rows);
});

/* ── PATCH /api/auth/users/:id/status ───────────────────── UPDATE ────────── */
router.patch('/users/:id/status', authenticate, authorize('ADMIN'), async (req, res) => {
  const { status } = req.body;
  if (!['ACTIVE', 'INACTIVE'].includes(status))
    return res.status(400).json({ error: 'status must be ACTIVE or INACTIVE' });

  await pool.execute('UPDATE users SET status=? WHERE id=?', [status, req.params.id]);
  return res.json({ message: 'Status updated' });
});

/* ── DELETE /api/auth/users/:id ──────────────────────────── DELETE ───────── */
router.delete('/users/:id', authenticate, authorize('ADMIN'), async (req, res) => {
  const [result] = await pool.execute('DELETE FROM users WHERE id=?', [req.params.id]);
  if (result.affectedRows === 0)
    return res.status(404).json({ error: 'User not found' });
  return res.json({ message: 'User deleted' });
});

module.exports = router;

