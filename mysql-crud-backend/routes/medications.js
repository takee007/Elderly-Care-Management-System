// routes/medications.js
// CRUD for medications + medication logs
const router = require('express').Router();
const pool   = require('../db/connection');
const { authenticate, authorize } = require('../middleware/auth');

/* ══ MEDICATIONS ════════════════════════════════════════════════════════════ */

/* ── POST /api/medications ────────────────────────────────── CREATE ───────── */
router.post('/', authenticate, authorize('ADMIN','DOCTOR'), async (req, res) => {
  const { senior_id, name, dosage, frequency, scheduled_times,
          instructions, prescribed_by, start_date, end_date } = req.body;

  if (!senior_id || !name || !dosage || !frequency || !scheduled_times || !start_date)
    return res.status(400).json({ error: 'Required medication fields missing' });

  const [result] = await pool.execute(
    `INSERT INTO medications
       (senior_id,name,dosage,frequency,scheduled_times,instructions,prescribed_by,start_date,end_date)
     VALUES (?,?,?,?,?,?,?,?,?)`,
    [senior_id, name, dosage, frequency, scheduled_times,
     instructions || null, prescribed_by || null, start_date, end_date || null]
  );
  return res.status(201).json({ id: result.insertId });
});

/* ── GET /api/medications?senior_id=1 ────────────────────── READ ─────────── */
router.get('/', authenticate, async (req, res) => {
  const { senior_id } = req.query;
  let sql = 'SELECT * FROM medications';
  const params = [];
  if (senior_id) { sql += ' WHERE senior_id=?'; params.push(senior_id); }
  const [rows] = await pool.execute(sql, params);
  return res.json(rows);
});

/* ── GET /api/medications/:id ─────────────────────────────── READ SINGLE ──── */
router.get('/:id', authenticate, async (req, res) => {
  const [rows] = await pool.execute('SELECT * FROM medications WHERE id=?', [req.params.id]);
  if (!rows[0]) return res.status(404).json({ error: 'Medication not found' });
  return res.json(rows[0]);
});

/* ── PUT /api/medications/:id ─────────────────────────────── UPDATE ───────── */
router.put('/:id', authenticate, authorize('ADMIN','DOCTOR'), async (req, res) => {
  const { dosage, frequency, scheduled_times, instructions,
          prescription_status, end_date } = req.body;

  const [result] = await pool.execute(
    `UPDATE medications SET
       dosage=?, frequency=?, scheduled_times=?,
       instructions=?, prescription_status=?, end_date=?
     WHERE id=?`,
    [dosage, frequency, scheduled_times, instructions || null,
     prescription_status || 'ACTIVE', end_date || null, req.params.id]
  );
  if (result.affectedRows === 0) return res.status(404).json({ error: 'Medication not found' });
  return res.json({ message: 'Medication updated' });
});

/* ── DELETE /api/medications/:id ──────────────────────────── DELETE ───────── */
router.delete('/:id', authenticate, authorize('ADMIN','DOCTOR'), async (req, res) => {
  const [result] = await pool.execute('DELETE FROM medications WHERE id=?', [req.params.id]);
  if (result.affectedRows === 0) return res.status(404).json({ error: 'Medication not found' });
  return res.json({ message: 'Medication deleted' });
});

/* ══ MEDICATION LOGS ════════════════════════════════════════════════════════ */

/* ── GET /api/medications/logs?senior_id=1 ───────────────── READ ─────────── */
router.get('/logs', authenticate, async (req, res) => {
  const { senior_id } = req.query;
  let sql = `SELECT ml.*, m.name AS medication_name
             FROM medication_logs ml
             JOIN medications m ON ml.medication_id = m.id`;
  const params = [];
  if (senior_id) { sql += ' WHERE ml.senior_id=?'; params.push(senior_id); }
  sql += ' ORDER BY ml.id DESC';
  const [rows] = await pool.execute(sql, params);
  return res.json(rows);
});

/* ── POST /api/medications/logs ──────────────────────────── CREATE ───────── */
router.post('/logs', authenticate, authorize('ADMIN','CAREGIVER','DOCTOR'), async (req, res) => {
  const { medication_id, senior_id, scheduled_time, status, notes, administered_by } = req.body;
  if (!medication_id || !senior_id || !scheduled_time)
    return res.status(400).json({ error: 'medication_id, senior_id and scheduled_time are required' });

  const administered_at = ['GIVEN'].includes(status) ? new Date() : null;
  const [result] = await pool.execute(
    `INSERT INTO medication_logs
       (medication_id,senior_id,scheduled_time,administered_at,status,notes,administered_by)
     VALUES (?,?,?,?,?,?,?)`,
    [medication_id, senior_id, scheduled_time, administered_at,
     status || 'PENDING', notes || null, administered_by || null]
  );
  return res.status(201).json({ id: result.insertId });
});

module.exports = router;

