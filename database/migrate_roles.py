import sqlite3
import os

DATABASE_PATH = 'database/interview.db'
if not os.path.exists(DATABASE_PATH):
    DATABASE_PATH = '../database/interview.db'

def migrate_roles():
    print("Connecting to database...")
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    try:
        # Check if role column exists
        cursor.execute("PRAGMA table_info(users)")
        columns = [info[1] for info in cursor.fetchall()]
        
        if 'role' not in columns:
            print("Adding 'role' column to users table...")
            cursor.execute("ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'student'")
            print("Column added.")
            
            # Update existing users to 'student' (handled by default, but nice to be explicit if needed)
            # cursor.execute("UPDATE users SET role = 'student' WHERE role IS NULL")
            
            # OPTIONAL: Set a specific user as admin if you know their email
            # cursor.execute("UPDATE users SET role = 'admin' WHERE email = 'admin@college.edu'")
        else:
            print("'role' column already exists.")

    except Exception as e:
        print(f"Error: {e}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    migrate_roles()
