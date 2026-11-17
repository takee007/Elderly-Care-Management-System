// seed.js  –  Populate MySQL database in phpMyAdmin with initial ECMS data
const bcrypt = require('bcryptjs');
const pool = require('./db/connection');

async function seed() {
  try {
    console.log('🌱 Checking ecms_db users...');
    const [existing] = await pool.execute('SELECT COUNT(*) AS count FROM users');
    if (existing[0].count > 0) {
      console.log(`ℹ️  ecms_db already has ${existing[0].count} users. Skipping initial seed.`);
      process.exit(0);
    }

    const hash = await bcrypt.hash('password123', 10);

    // 1. Seed Users
    const users = [
      ['admin@probin.gov.bd', hash, 'Engr. Md. Tariqul Islam', 'ADMIN', '+880 1711-098765', 'ACTIVE'],
      ['dr.hasan@probin.org.bd', hash, 'Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS', 'DOCTOR', '+880 1819-234567', 'ACTIVE'],
      ['nurse.fatema@probin.org.bd', hash, 'Fatema Begum, BSc Nursing (RN)', 'CAREGIVER', '+880 1912-345678', 'ACTIVE'],
      ['haji.abdul@gmail.com', hash, 'Haji Md. Abdul Mannan', 'SENIOR', '+880 1715-112233', 'ACTIVE'],
      ['tariq.mannan@gmail.com', hash, 'Tariq Mannan', 'GUARDIAN', '+880 1718-445566', 'ACTIVE'],
    ];

    for (const u of users) {
      await pool.execute(
        `INSERT INTO users (email, hashed_password, full_name, role, phone, status) VALUES (?,?,?,?,?,?)`,
        u
      );
    }
    console.log('✅ Seeded 5 initial users');

    // 2. Seed Seniors
    const seniors = [
      [
        'MRN-2026-001', 'Haji Md. Abdul Mannan', '1948-03-15', 'MALE', 'B+',
        'Room 204 (East Wing)', '+880 1715-112233', 'Plot 12, Road 4, Sector 7, Uttara, Dhaka',
        'Tariq Mannan (Son)', '+880 1718-445566', 'Prof. Dr. Syed Rafiqul Hasan',
        'Type 2 Diabetes, Stage 2 Hypertension, Mild Osteoarthritis',
        'Penicillin, Aspirin', 5, 4
      ],
      [
        'MRN-2026-002', 'Begum Rokeya Chowdhury', '1951-08-22', 'FEMALE', 'O+',
        'Room 108 (Ground Floor)', '+880 1817-654321', 'House 45, Road 9/A, Dhanmondi, Dhaka',
        'Zafar Chowdhury (Son)', '+880 1913-778899', 'Prof. Dr. Syed Rafiqul Hasan',
        'Parkinsonism (early stage), Chronic Kidney Disease (Stage 2)',
        'Sulfa drugs', null, null
      ]
    ];

    for (const s of seniors) {
      await pool.execute(
        `INSERT INTO seniors (mrn, full_name, date_of_birth, gender, blood_group, room_number, phone, address, emergency_name, emergency_phone, primary_doctor, chronic_ailments, drug_allergies, guardian_id, user_id)
         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)`,
        s
      );
    }
    console.log('✅ Seeded 2 seniors');

    console.log('🎉 Database seed complete! Check phpMyAdmin: http://localhost/phpmyadmin/index.php?route=/sql&pos=0&db=ecms_db&table=users');
    process.exit(0);
  } catch (err) {
    console.error('❌ Seed error:', err);
    process.exit(1);
  }
}

seed();

