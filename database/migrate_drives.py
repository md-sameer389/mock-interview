import sqlite3
import os

DATABASE_PATH = 'database/interview.db'
if not os.path.exists(DATABASE_PATH):
    DATABASE_PATH = '../database/interview.db'


def migrate_drives():
    print("Connecting to database...")
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Create Drives Table
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS drives (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company TEXT NOT NULL,
                role TEXT NOT NULL,
                description TEXT,
                date TEXT NOT NULL,
                status TEXT DEFAULT 'Upcoming' -- Upcoming, Open, Completed
            )
        """)
        print("Created drives table.")
        
        # Seed Data
        drives = [
            ("Google", "Software Engineer", "Early Career 2026 hiring for Bangalore/Hyderabad.", "2026-03-15", "Upcoming"),
            ("TCS", "System Engineer", "Pan-India NQT Exam for 2026 Batch.", "2026-02-20", "Open"),
            ("Infosys", "Specialist Programmer", "High package role for coding experts.", "2026-04-10", "Upcoming"),
            ("Amazon", "SDE Intern", "6-month internship with PPO opportunity.", "2026-01-10", "Completed")
        ]
        
        # Check if empty
        count = cursor.execute("SELECT COUNT(*) FROM drives").fetchone()[0]
        if count == 0:
            cursor.executemany("INSERT INTO drives (company, role, description, date, status) VALUES (?, ?, ?, ?, ?)", drives)
            print("Seeded placement drives.")
        else:
            print("Drives table already populated.")
            
    except Exception as e:
        print(f"Error: {e}")
        
    conn.commit()
    conn.close()

if __name__ == "__main__":
    migrate_drives()
