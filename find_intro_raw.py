import sqlite3

DB_PATH = r"c:\Users\sameer\OneDrive\Desktop\mock\database\interview.db"

def find_intro():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("--- Question Search ---")
    cursor.execute("SELECT id, question_text, difficulty FROM questions WHERE question_text LIKE '%yourself%' OR question_text LIKE '%intro%'")
    rows = cursor.fetchall()
    
    if rows:
        for r in rows:
            print(f"ID: {r[0]} | Text: {r[1]} | Diff: {r[2]}")
    else:
        print("No intro questions found.")
        
    conn.close()

if __name__ == "__main__":
    find_intro()
