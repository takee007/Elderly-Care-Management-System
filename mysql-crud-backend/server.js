// server.js  –  Entry point
// ═════════════════════════════════════════════════════════════════════════════
// Node.js + MySQL CRUD backend for the Elderly Care Management System (ECMS)
// Reference: https://medium.com/@navidunimsara/node-js-mysql-database-connection-and-perform-crud-operations-893db877dc8d
// ═════════════════════════════════════════════════════════════════════════════
require('dotenv').config();
const express = require('express');
const cors    = require('cors');

const app = express();

/* ── Global middleware ────────────────────────────────────────────────────── */
app.use(cors({
  origin: true, // Allow any local development origin (localhost:5173, 127.0.0.1, etc.)
  credentials: true,
}));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

/* ── Request Logger ───────────────────────────────────────────────────────── */
app.use((req, res, next) => {
  console.log(`[${new Date().toLocaleTimeString()}] ${req.method} ${req.url}`);
  next();
});

/* ── Route mounting ───────────────────────────────────────────────────────── */
app.use('/api/auth',         require('./routes/auth'));
app.use('/api/seniors',      require('./routes/seniors'));
app.use('/api/vitals',       require('./routes/vitals'));
app.use('/api/medications',  require('./routes/medications'));
app.use('/api/appointments', require('./routes/appointments'));
app.use('/api/emergency',    require('./routes/emergency'));
app.use('/api/handoff',      require('./routes/handoff'));
app.use('/api/analytics',    require('./routes/analytics'));

/* ── Health check ─────────────────────────────────────────────────────────── */
app.get('/health', (_req, res) =>
  res.json({ status: 'ok', database: 'MySQL ecms_db', timestamp: new Date().toISOString() })
);
app.get('/api/health', (_req, res) =>
  res.json({ status: 'ok', database: 'MySQL ecms_db', timestamp: new Date().toISOString() })
);

/* ── 404 handler ──────────────────────────────────────────────────────────── */
app.use((req, res) =>
  res.status(404).json({ error: `Route ${req.method} ${req.path} not found` })
);

/* ── Global error handler ─────────────────────────────────────────────────── */
app.use((err, _req, res, _next) => {
  console.error('[ERROR]', err);
  res.status(err.status || 500).json({ error: err.message || 'Internal server error' });
});

/* ── Start ────────────────────────────────────────────────────────────────── */
const PORT = process.env.PORT || 5000;
app.listen(PORT, () =>
  console.log(`🚀  ECMS MySQL API running on http://localhost:${PORT}`)
);
