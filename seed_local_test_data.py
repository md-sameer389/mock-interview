
import sqlite3
import os
import bcrypt

DATABASE_PATH = os.path.join('database', 'interview.db')

def hash_pw(pw):
    return bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def seed_local_data():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    
    print("Seeding local test data...")
    
    # 1. Ensure Admin
    admin = conn.execute("SELECT id FROM users WHERE email = 'admin@mock.com'").fetchone()
    if not admin:
        print("Creating Admin...")
        conn.execute("INSERT INTO users (full_name, email, password_hash, role) VALUES (?, ?, ?, ?)",
                     ("Local Admin", "admin@mock.com", hash_pw('admin123'), "admin"))
    else:
        print("Admin already exists.")

    # 2. Ensure Student
    student = conn.execute("SELECT id FROM users WHERE email = 'student@mock.com'").fetchone()
    if not student:
        print("Creating Student...")
        conn.execute("INSERT INTO users (full_name, email, password_hash, role) VALUES (?, ?, ?, ?)",
                     ("Local Student", "student@mock.com", hash_pw('student123'), "student"))
        student_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
    else:
        print("Student already exists.")
        student_id = student['id']

    # 3. Add Dummy Resume if needed
    resume = conn.execute("SELECT id FROM resumes WHERE user_id = ?", (student_id,)).fetchone()
    if not resume:
        print("Adding dummy resume...")
        conn.execute("INSERT INTO resumes (user_id, filename, extracted_text) VALUES (?, ?, ?)",
                     (student_id, "test_resume.pdf", "Python, JavaScript, SQL"))
        resume_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
    else:
        resume_id = resume['id']

    # 4. Add a dummy completed interview session
    session = conn.execute("SELECT id FROM interview_sessions WHERE user_id = ? AND status='completed'", (student_id,)).fetchone()
    if not session:
        print("Adding dummy completed session...")
        conn.execute("""
            INSERT INTO interview_sessions 
            (user_id, resume_id, total_questions, total_score, status, started_at, completed_at, persona) 
            VALUES (?, ?, ?, ?, ?, datetime('now', '-1 day'), datetime('now', '-23 hours'), 'technical')
        """, (student_id, resume_id, 5, 8.5, 'completed'))
    
    conn.commit()
    conn.close()
    print("Local seeding complete!")

if __name__ == "__main__":
    seed_local_data()
