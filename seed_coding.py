import sqlite3
import os

db_path = r"c:\Users\sameer\OneDrive\Desktop\mock\database\interview.db"
sql_file = r"c:\Users\sameer\OneDrive\Desktop\mock\database\add_coding_questions.sql"

def seed():
    if not os.path.exists(db_path):
        print("DB not found")
        return
        
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_content = f.read()
        
    # Split by semicolon to get individual statements roughly
    # This is a simple splitter, might break on semicolons in strings.
    # But my strings don't have semicolons (hopefully).
    # Better: read the whole file and execute script?
    try:
        cursor.executescript(sql_content)
        conn.commit()
        print("Allocated successfully.")
    except Exception as e:
        print(f"Error: {e}")
        
    # Check counts
    cursor.execute("SELECT skill_id, count(*) FROM questions WHERE question_type='coding' GROUP BY skill_id")
    print("Counts:", cursor.fetchall())
    
    conn.close()

if __name__ == "__main__":
    seed()
