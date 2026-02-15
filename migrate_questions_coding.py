import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'database/interview.db')

def migrate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("Migrating questions table...")
    
    try:
        # Add question_type column
        try:
            cursor.execute("ALTER TABLE questions ADD COLUMN question_type TEXT DEFAULT 'text'")
            print("Added question_type column.")
        except sqlite3.OperationalError:
            print("question_type column already exists.")
            
        # Add code_snippet column
        try:
            cursor.execute("ALTER TABLE questions ADD COLUMN code_snippet TEXT")
            print("Added code_snippet column.")
        except sqlite3.OperationalError:
            print("code_snippet column already exists.")

        # Add test_cases column
        try:
            cursor.execute("ALTER TABLE questions ADD COLUMN test_cases TEXT")
            print("Added test_cases column.")
        except sqlite3.OperationalError:
            print("test_cases column already exists.")

        # Add correct_output column
        try:
            cursor.execute("ALTER TABLE questions ADD COLUMN correct_output TEXT")
            print("Added correct_output column.")
        except sqlite3.OperationalError:
            print("correct_output column already exists.")
            
        conn.commit()
        print("Migration complete.")
        
    except Exception as e:
        print(f"Migration failed: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    migrate()
