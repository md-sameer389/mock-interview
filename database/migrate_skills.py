import sqlite3
import os

DATABASE_PATH = 'database/interview.db'
if not os.path.exists(DATABASE_PATH):
    DATABASE_PATH = '../database/interview.db'

def migrate_skills():
    print("Connecting to database...")
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    try:
        # 1. Create candidate_skills table
        print("Creating candidate_skills table...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS candidate_skills (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                skill_name TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        
        # 2. Add required_skills to drives
        print("Checking drives table...")
        cursor.execute("PRAGMA table_info(drives)")
        columns = [info[1] for info in cursor.fetchall()]
        
        if 'required_skills' not in columns:
            print("Adding 'required_skills' column to drives...")
            cursor.execute("ALTER TABLE drives ADD COLUMN required_skills TEXT DEFAULT ''")
        
        # 3. Seed required skills for existing drives
        print("Updating existing drives with skills...")
        updates = [
            ("Google", "Python,Data Structures,Algorithms"),
            ("TCS", "Java,SQL,Aptitude"),
            ("Infosys", "Python,React,SQL"),
            ("Amazon", "Java,AWS,System Design")
        ]
        
        for company, skills in updates:
            cursor.execute("UPDATE drives SET required_skills = ? WHERE company = ?", (skills, company))

        print("Migration complete.")

    except Exception as e:
        print(f"Error: {e}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    migrate_skills()
