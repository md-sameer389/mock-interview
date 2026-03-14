import sqlite3
import os

db_path = r"c:\Users\sameer\OneDrive\Desktop\mock\interview.db"

if not os.path.exists(db_path):
    print(f"Database file not found at: {db_path}")
else:
    print(f"Database file found at: {db_path}")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # List tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("Tables:", tables)
        
        if ('questions',) in tables:
            cursor.execute("SELECT count(*) FROM questions WHERE question_type='coding'")
            count = cursor.fetchone()[0]
            print(f"Coding questions count: {count}")
            
            cursor.execute("SELECT id, question_text, difficulty FROM questions WHERE question_type='coding'")
            coding_qs = cursor.fetchall()
            for q in coding_qs:
                print(q)
        else:
            print("Table 'questions' does not exist.")
            
        conn.close()
    except Exception as e:
        print(f"Error: {e}")
