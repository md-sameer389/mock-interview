import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'interview.db')

def migrate_admin():
    print("Beginning migration for Admin Dashboard (Answers Table)...")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # Check if columns exist
    try:
        cur.execute("ALTER TABLE answers ADD COLUMN flagged BOOLEAN DEFAULT 0")
        print("Added 'flagged' column.")
    except sqlite3.OperationalError:
        print("'flagged' column likely already exists.")
        
    try:
        cur.execute("ALTER TABLE answers ADD COLUMN flag_reason TEXT")
        print("Added 'flag_reason' column.")
    except sqlite3.OperationalError:
        print("'flag_reason' column likely already exists.")
        
    conn.commit()
    conn.close()
    print("Migration Complete.")

if __name__ == "__main__":
    migrate_admin()
