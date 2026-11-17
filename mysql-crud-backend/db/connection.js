// db/connection.js
// ─────────────────────────────────────────────────────────────────────────────
// Creates a MySQL connection pool using the mysql2 library.
// Reference: https://medium.com/@navidunimsara/node-js-mysql-database-connection-and-perform-crud-operations-893db877dc8d
// ─────────────────────────────────────────────────────────────────────────────
const mysql = require('mysql2/promise');
require('dotenv').config();

const pool = mysql.createPool({
  host:               process.env.DB_HOST     || 'localhost',
  port:               parseInt(process.env.DB_PORT) || 3306,
  user:               process.env.DB_USER     || 'root',
  password:           process.env.DB_PASSWORD || '',
  database:           process.env.DB_NAME     || 'ecms_db',
  waitForConnections: true,
  connectionLimit:    10,
  queueLimit:         0,
  timezone:           '+00:00',       // store timestamps in UTC
});

// Test the pool immediately on startup
pool.getConnection()
  .then(conn => {
    console.log('✅  MySQL connected successfully');
    conn.release();
  })
  .catch(err => {
    console.error('❌  MySQL connection failed:', err.message);
    process.exit(1);
  });

module.exports = pool;

