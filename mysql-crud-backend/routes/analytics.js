// routes/analytics.js  –  MySQL (mysql2) version
const router = require('express').Router();
const pool   = require('../db/connection');
const { authenticate, authorize } = require('../middleware/auth');

router.get('/dashboard', authenticate, async (_req, res) => {
  const [[seniors], [users], [vitals], [alerts], [meds], [appts]] = await Promise.all([
    pool.execute('SELECT COUNT(*) AS count FROM seniors'),
    pool.execute('SELECT COUNT(*) AS count FROM users'),
    pool.execute('SELECT COUNT(*) AS count FROM vitals WHERE is_anomaly=1'),
    pool.execute("SELECT COUNT(*) AS count FROM emergency_alerts WHERE status != 'RESOLVED'"),
    pool.execute("SELECT COUNT(*) AS count FROM medications WHERE prescription_status='ACTIVE'"),
    pool.execute("SELECT COUNT(*) AS count FROM appointments WHERE status='SCHEDULED'"),
  ]);
  return res.json({
    total_seniors:          seniors[0].count,
    total_users:            users[0].count,
    anomaly_vitals:         vitals[0].count,
    active_alerts:          alerts[0].count,
    active_medications:     meds[0].count,
    scheduled_appointments: appts[0].count,
  });
});

router.get('/audit-logs', authenticate, authorize('ADMIN'), async (_req, res) => {
  const [rows] = await pool.execute('SELECT * FROM audit_logs ORDER BY timestamp DESC LIMIT 100');
  return res.json(rows);
});

module.exports = router;

