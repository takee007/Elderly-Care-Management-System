// routes/vitals.js
// CRUD for vital signs recordings
const router = require('express').Router();
const pool   = require('../db/connection');
const { authenticate, authorize } = require('../middleware/auth');

/* ── POST /api/vitals ─────────────────────────────────────── CREATE ───────── */
router.post('/', authenticate, authorize('ADMIN','DOCTOR','CAREGIVER'), async (req, res) => {
  const {
    senior_id, systolic_bp, diastolic_bp, pulse_rate,
    spo2, temperature, blood_glucose, recorded_by,
  } = req.body;

  if (!senior_id || systolic_bp == null || diastolic_bp == null || !recorded_by)
    return res.status(400).json({ error: 'Required vital fields missing' });

  // Simple anomaly detection (mirrors Python backend logic)
  const is_anomaly =
    systolic_bp > 140 || systolic_bp < 90 ||
    diastolic_bp > 90 || diastolic_bp < 60 ||
    pulse_rate   > 100 || pulse_rate   < 60 ||
    spo2         < 95 ||
    temperature  > 99.5 || temperature < 97 ||
    blood_glucose > 180 || blood_glucose < 70;

  const anomaly_notes = is_anomaly ? 'Auto-flagged: values outside normal range' : null;

  const [result] = await pool.execute(
    `INSERT INTO vitals
       (senior_id,systolic_bp,diastolic_bp,pulse_rate,spo2,temperature,
        blood_glucose,is_anomaly,anomaly_notes,recorded_by)
     VALUES (?,?,?,?,?,?,?,?,?,?)`,
    [senior_id, systolic_bp, diastolic_bp, pulse_rate, spo2,
     temperature, blood_glucose, is_anomaly ? 1 : 0, anomaly_notes, recorded_by]
  );
  return res.status(201).json({ id: result.insertId, is_anomaly });
});

/* ── GET /api/vitals?senior_id=1 ─────────────────────────── READ ─────────── */
router.get('/', authenticate, async (req, res) => {
  const { senior_id } = req.query;
  let sql = 'SELECT * FROM vitals';
  const params = [];
  if (senior_id) { sql += ' WHERE senior_id=?'; params.push(senior_id); }
  sql += ' ORDER BY recorded_at DESC LIMIT 100';
  const [rows] = await pool.execute(sql, params);
  return res.json(rows);
});

/* ── GET /api/vitals/:id ──────────────────────────────────── READ SINGLE ──── */
router.get('/:id', authenticate, async (req, res) => {
  const [rows] = await pool.execute('SELECT * FROM vitals WHERE id=?', [req.params.id]);
  if (!rows[0]) return res.status(404).json({ error: 'Vital record not found' });
  return res.json(rows[0]);
});

/* ── PUT /api/vitals/:id ──────────────────────────────────── UPDATE ───────── */
router.put('/:id', authenticate, authorize('ADMIN','DOCTOR'), async (req, res) => {
  const { anomaly_notes, is_anomaly } = req.body;
  const [result] = await pool.execute(
    'UPDATE vitals SET anomaly_notes=?, is_anomaly=? WHERE id=?',
    [anomaly_notes, is_anomaly ? 1 : 0, req.params.id]
  );
  if (result.affectedRows === 0) return res.status(404).json({ error: 'Vital not found' });
  return res.json({ message: 'Vital updated' });
});

/* ── DELETE /api/vitals/:id ───────────────────────────────── DELETE ───────── */
router.delete('/:id', authenticate, authorize('ADMIN'), async (req, res) => {
  const [result] = await pool.execute('DELETE FROM vitals WHERE id=?', [req.params.id]);
  if (result.affectedRows === 0) return res.status(404).json({ error: 'Vital not found' });
  return res.json({ message: 'Vital deleted' });
});

module.exports = router;

