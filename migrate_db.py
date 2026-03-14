
import sqlite3

DB_PATH = 'database/interview.db'

def migrate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        # Add technical_score column
        try:
            cursor.execute("ALTER TABLE answers ADD COLUMN technical_score REAL DEFAULT 0.0")
            print("Added technical_score column.")
        except sqlite3.OperationalError as e:
            print(f"technical_score column might already exist: {e}")

        # Add communication_score column
        try:
            cursor.execute("ALTER TABLE answers ADD COLUMN communication_score REAL DEFAULT 0.0")
            print("Added communication_score column.")
        except sqlite3.OperationalError as e:
            print(f"communication_score column might already exist: {e}")
            
        conn.commit()
        print("Migration complete.")
        
    except Exception as e:
        print(f"Migration failed: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    migrate()
