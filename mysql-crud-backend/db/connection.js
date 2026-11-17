// db/connection.js  –  Local MySQL via XAMPP / phpMyAdmin
const mysql = require('mysql2/promise');
require('dotenv').config();

const pool = mysql.createPool({
  host:               process.env.DB_HOST     || 'localhost',
  port:               parseInt(process.env.DB_PORT) || 3306,
  user:               process.env.DB_USER     || 'root',
  password:           process.env.DB_PASSWORD || '',   // XAMPP default: empty
  database:           process.env.DB_NAME     || 'ecms_db',
  waitForConnections: true,
  connectionLimit:    10,
  queueLimit:         0,
  timezone:           '+00:00',
});

// Test connection on startup
pool.getConnection()
  .then(conn => {
    console.log('✅  MySQL (phpMyAdmin) connected successfully');
    conn.release();
  })
  .catch(err => {
    console.error('❌  MySQL connection failed:', err.message);
    console.error('👉  Make sure XAMPP MySQL is running and ecms_db exists in phpMyAdmin');
    process.exit(1);
  });

module.exports = pool;
