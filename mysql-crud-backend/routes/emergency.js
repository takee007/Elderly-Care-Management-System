// routes/emergency.js
// CRUD for emergency alerts
const router = require('express').Router();
const pool   = require('../db/connection');
const { authenticate, authorize } = require('../middleware/auth');

/* ── POST /api/emergency/sos ──────────────────────────────── CREATE ───────── */
router.post('/sos', authenticate, async (req, res) => {
  const { senior_id, trigger_type = 'SOS_BUTTON', latitude, longitude } = req.body;
  if (!senior_id) return res.status(400).json({ error: 'senior_id is required' });

  const [result] = await pool.execute(
    `INSERT INTO emergency_alerts (senior_id, trigger_type, latitude, longitude)
     VALUES (?, ?, ?, ?)`,
    [senior_id, trigger_type, latitude || null, longitude || null]
  );
  return res.status(201).json({ id: result.insertId, status: 'TRIGGERED' });
});

/* ── GET /api/emergency/alerts?status_filter=TRIGGERED ────── READ ─────────── */
router.get('/alerts', authenticate, async (req, res) => {
  const { status_filter } = req.query;
  let sql = `SELECT ea.*, s.full_name AS senior_name, s.room_number
             FROM emergency_alerts ea
             JOIN seniors s ON ea.senior_id = s.id`;
  const params = [];
  if (status_filter) { sql += ' WHERE ea.status=?'; params.push(status_filter); }
  sql += ' ORDER BY ea.triggered_at DESC';
  const [rows] = await pool.execute(sql, params);
  return res.json(rows);
});

/* ── GET /api/emergency/alerts/:id ───────────────────────── READ SINGLE ───── */
router.get('/alerts/:id', authenticate, async (req, res) => {
  const [rows] = await pool.execute(
    'SELECT * FROM emergency_alerts WHERE id=?', [req.params.id]
  );
  if (!rows[0]) return res.status(404).json({ error: 'Alert not found' });
  return res.json(rows[0]);
});

/* ── POST /api/emergency/alerts/:id/resolve ──────────────── UPDATE ───────── */
router.post('/alerts/:id/resolve', authenticate, async (req, res) => {
  const { notes, status = 'RESOLVED', resolved_by } = req.body;
  const [result] = await pool.execute(
    `UPDATE emergency_alerts
     SET status=?, notes=?, resolved_at=NOW(), resolved_by=?
     WHERE id=?`,
    [status, notes || null, resolved_by || req.user?.email, req.params.id]
  );
  if (result.affectedRows === 0) return res.status(404).json({ error: 'Alert not found' });
  return res.json({ message: 'Alert resolved' });
});

/* ── DELETE /api/emergency/alerts/:id ────────────────────── DELETE ───────── */
router.delete('/alerts/:id', authenticate, authorize('ADMIN'), async (req, res) => {
  const [result] = await pool.execute(
    'DELETE FROM emergency_alerts WHERE id=?', [req.params.id]
  );
  if (result.affectedRows === 0) return res.status(404).json({ error: 'Alert not found' });
  return res.json({ message: 'Alert deleted' });
});

module.exports = router;

