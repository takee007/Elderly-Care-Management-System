// routes/appointments.js
// CRUD for appointments
const router = require('express').Router();
const pool   = require('../db/connection');
const { authenticate, authorize } = require('../middleware/auth');

/* ── POST /api/appointments ───────────────────────────────── CREATE ───────── */
router.post('/', authenticate, async (req, res) => {
  const { senior_id, doctor_id, doctor_name, specialty,
          scheduled_at, consultation_type, notes, teleconsult_link } = req.body;

  if (!senior_id || !doctor_name || !specialty || !scheduled_at)
    return res.status(400).json({ error: 'Required appointment fields missing' });

  const [result] = await pool.execute(
    `INSERT INTO appointments
       (senior_id,doctor_id,doctor_name,specialty,scheduled_at,
        consultation_type,notes,teleconsult_link)
     VALUES (?,?,?,?,?,?,?,?)`,
    [senior_id, doctor_id || null, doctor_name, specialty,
     scheduled_at, consultation_type || 'IN_PERSON',
     notes || null, teleconsult_link || null]
  );
  return res.status(201).json({ id: result.insertId });
});

/* ── GET /api/appointments?senior_id=1 ───────────────────── READ ─────────── */
router.get('/', authenticate, async (req, res) => {
  const { senior_id } = req.query;
  let sql = `SELECT a.*, s.full_name AS senior_name
             FROM appointments a
             JOIN seniors s ON a.senior_id = s.id`;
  const params = [];
  if (senior_id) { sql += ' WHERE a.senior_id=?'; params.push(senior_id); }
  sql += ' ORDER BY a.scheduled_at DESC';
  const [rows] = await pool.execute(sql, params);
  return res.json(rows);
});

/* ── GET /api/appointments/:id ────────────────────────────── READ SINGLE ──── */
router.get('/:id', authenticate, async (req, res) => {
  const [rows] = await pool.execute('SELECT * FROM appointments WHERE id=?', [req.params.id]);
  if (!rows[0]) return res.status(404).json({ error: 'Appointment not found' });
  return res.json(rows[0]);
});

/* ── PUT /api/appointments/:id/status ────────────────────── UPDATE ───────── */
router.put('/:id/status', authenticate, async (req, res) => {
  const { status } = req.body;
  if (!['SCHEDULED', 'COMPLETED', 'CANCELLED'].includes(status))
    return res.status(400).json({ error: 'Invalid status' });

  const [result] = await pool.execute(
    'UPDATE appointments SET status=? WHERE id=?', [status, req.params.id]
  );
  if (result.affectedRows === 0) return res.status(404).json({ error: 'Appointment not found' });
  return res.json({ message: 'Status updated' });
});

/* ── PUT /api/appointments/:id ────────────────────────────── UPDATE FULL ──── */
router.put('/:id', authenticate, authorize('ADMIN','DOCTOR'), async (req, res) => {
  const { doctor_name, specialty, scheduled_at,
          consultation_type, notes, teleconsult_link, status } = req.body;

  const [result] = await pool.execute(
    `UPDATE appointments SET
       doctor_name=?, specialty=?, scheduled_at=?,
       consultation_type=?, notes=?, teleconsult_link=?, status=?
     WHERE id=?`,
    [doctor_name, specialty, scheduled_at,
     consultation_type || 'IN_PERSON', notes || null,
     teleconsult_link || null, status || 'SCHEDULED', req.params.id]
  );
  if (result.affectedRows === 0) return res.status(404).json({ error: 'Appointment not found' });
  return res.json({ message: 'Appointment updated' });
});

/* ── DELETE /api/appointments/:id ────────────────────────── DELETE ───────── */
router.delete('/:id', authenticate, authorize('ADMIN','DOCTOR'), async (req, res) => {
  const [result] = await pool.execute('DELETE FROM appointments WHERE id=?', [req.params.id]);
  if (result.affectedRows === 0) return res.status(404).json({ error: 'Appointment not found' });
  return res.json({ message: 'Appointment deleted' });
});

module.exports = router;

