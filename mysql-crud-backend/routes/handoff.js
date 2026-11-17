// routes/handoff.js  –  MySQL (mysql2) version
const router = require('express').Router();
const pool   = require('../db/connection');
const { authenticate, authorize } = require('../middleware/auth');

router.post('/notes', authenticate, authorize('ADMIN','CAREGIVER'), async (req, res) => {
  const { caregiver_name, shift_date, shift_type, handover_to, notes, flagged_seniors } = req.body;
  if (!shift_date||!shift_type||!handover_to||!notes) return res.status(400).json({ error: 'Required fields missing' });
  const [result] = await pool.execute(
    `INSERT INTO shift_notes (caregiver_id,caregiver_name,shift_date,shift_type,handover_to,notes,flagged_seniors) VALUES (?,?,?,?,?,?,?)`,
    [req.user.id,caregiver_name||req.user.email,shift_date,shift_type,handover_to,notes,flagged_seniors||null]
  );
  return res.status(201).json({ id: result.insertId });
});

router.get('/notes', authenticate, async (_req, res) => {
  const [rows] = await pool.execute('SELECT * FROM shift_notes ORDER BY signed_at DESC LIMIT 50');
  return res.json(rows);
});

router.get('/notes/:id', authenticate, async (req, res) => {
  const [rows] = await pool.execute('SELECT * FROM shift_notes WHERE id=?', [req.params.id]);
  if (!rows[0]) return res.status(404).json({ error: 'Note not found' }); return res.json(rows[0]);
});

router.put('/notes/:id', authenticate, authorize('ADMIN'), async (req, res) => {
  const { notes, flagged_seniors } = req.body;
  const [result] = await pool.execute('UPDATE shift_notes SET notes=?,flagged_seniors=? WHERE id=?', [notes,flagged_seniors||null,req.params.id]);
  if (result.affectedRows===0) return res.status(404).json({ error: 'Note not found' });
  return res.json({ message: 'Note updated' });
});

router.delete('/notes/:id', authenticate, authorize('ADMIN'), async (req, res) => {
  const [result] = await pool.execute('DELETE FROM shift_notes WHERE id=?', [req.params.id]);
  if (result.affectedRows===0) return res.status(404).json({ error: 'Note not found' });
  return res.json({ message: 'Note deleted' });
});

module.exports = router;
