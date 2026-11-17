// routes/seniors.js
// Full CRUD – Create, Read (list + single), Update, Delete seniors
const router = require('express').Router();
const pool   = require('../db/connection');
const { authenticate, authorize } = require('../middleware/auth');

/* ── POST /api/seniors ────────────────────────────────────── CREATE ───────── */
router.post('/', authenticate, authorize('ADMIN', 'DOCTOR', 'CAREGIVER'), async (req, res) => {
  const {
    mrn, full_name, date_of_birth, gender, blood_group,
    room_number, phone, address, emergency_name, emergency_phone,
    primary_doctor, chronic_ailments, drug_allergies, guardian_id, user_id,
  } = req.body;

  if (!mrn || !full_name || !date_of_birth || !gender || !room_number || !emergency_name || !emergency_phone)
    return res.status(400).json({ error: 'Required fields missing' });

  try {
    const [result] = await pool.execute(
      `INSERT INTO seniors
         (mrn, full_name, date_of_birth, gender, blood_group, room_number,
          phone, address, emergency_name, emergency_phone,
          primary_doctor, chronic_ailments, drug_allergies, guardian_id, user_id)
       VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)`,
      [mrn, full_name, date_of_birth, gender, blood_group || null,
       room_number, phone || null, address || null,
       emergency_name, emergency_phone,
       primary_doctor || null, chronic_ailments || null,
       drug_allergies || null, guardian_id || null, user_id || null]
    );
    return res.status(201).json({ id: result.insertId, mrn, full_name });
  } catch (err) {
    if (err.code === 'ER_DUP_ENTRY')
      return res.status(409).json({ error: 'MRN already exists' });
    console.error(err);
    return res.status(500).json({ error: 'Server error' });
  }
});

/* ── GET /api/seniors?search=xyz ─────────────────────────── READ LIST ─────── */
router.get('/', authenticate, async (req, res) => {
  const search = req.query.search || '';
  let sql = 'SELECT * FROM seniors';
  const params = [];
  if (search) {
    sql += ' WHERE full_name LIKE ? OR mrn LIKE ? OR room_number LIKE ?';
    params.push(`%${search}%`, `%${search}%`, `%${search}%`);
  }
  sql += ' ORDER BY created_at DESC';
  const [rows] = await pool.execute(sql, params);
  return res.json(rows);
});

/* ── GET /api/seniors/:id ────────────────────────────────── READ SINGLE ───── */
router.get('/:id', authenticate, async (req, res) => {
  const [rows] = await pool.execute('SELECT * FROM seniors WHERE id=?', [req.params.id]);
  if (!rows[0]) return res.status(404).json({ error: 'Senior not found' });
  return res.json(rows[0]);
});

/* ── PUT /api/seniors/:id ────────────────────────────────── UPDATE ───────── */
router.put('/:id', authenticate, authorize('ADMIN', 'DOCTOR', 'CAREGIVER'), async (req, res) => {
  const {
    full_name, date_of_birth, gender, blood_group, room_number,
    phone, address, emergency_name, emergency_phone,
    primary_doctor, chronic_ailments, drug_allergies,
  } = req.body;

  const [result] = await pool.execute(
    `UPDATE seniors SET
       full_name=?, date_of_birth=?, gender=?, blood_group=?,
       room_number=?, phone=?, address=?, emergency_name=?,
       emergency_phone=?, primary_doctor=?, chronic_ailments=?, drug_allergies=?
     WHERE id=?`,
    [full_name, date_of_birth, gender, blood_group || null,
     room_number, phone || null, address || null,
     emergency_name, emergency_phone,
     primary_doctor || null, chronic_ailments || null,
     drug_allergies || null, req.params.id]
  );
  if (result.affectedRows === 0) return res.status(404).json({ error: 'Senior not found' });
  return res.json({ message: 'Senior updated' });
});

/* ── DELETE /api/seniors/:id ─────────────────────────────── DELETE ───────── */
router.delete('/:id', authenticate, authorize('ADMIN'), async (req, res) => {
  const [result] = await pool.execute('DELETE FROM seniors WHERE id=?', [req.params.id]);
  if (result.affectedRows === 0) return res.status(404).json({ error: 'Senior not found' });
  return res.json({ message: 'Senior deleted' });
});

module.exports = router;

