
import sqlite3
import os

DB_PATH = 'backend/interview.db'

def check_schema():
    if not os.path.exists(DB_PATH):
        print(f"Database not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get info about answers table
    cursor.execute("PRAGMA table_info(answers)")
    columns = cursor.fetchall()
    
    print("Columns in 'answers' table:")
    found_tech = False
    found_comm = False
    
    for col in columns:
        name = col[1]
        print(f"- {name} ({col[2]})")
        if name == 'technical_score': found_tech = True
        if name == 'communication_score': found_comm = True
        
    conn.close()
    
    if not found_tech or not found_comm:
        print("\nMISSING COLUMNS: technical_score, communication_score")
        exit(1)
    else:
        print("\nAll columns present.")
        exit(0)

if __name__ == "__main__":
    check_schema()
