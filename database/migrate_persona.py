import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))
from database import get_db_connection

def migrate():
    conn = get_db_connection()
    try:
        print("Checking for persona column in interview_sessions...")
        cursor = conn.execute("PRAGMA table_info(interview_sessions)")
        columns = [row['name'] for row in cursor.fetchall()]
        
        if 'persona' not in columns:
            print("Adding persona column...")
            conn.execute("ALTER TABLE interview_sessions ADD COLUMN persona TEXT DEFAULT 'standard'")
            print("Migration successful: Added 'persona' column.")
        else:
            print("Column 'persona' already exists.")
            
        conn.commit()
    except Exception as e:
        print(f"Migration failed: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    migrate()
