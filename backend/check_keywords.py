import sqlite3
DB_PATH = r"c:\Users\sameer\OneDrive\Desktop\mock\database\interview.db"

def check_keywords():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    
    # Check "Tell me about yourself"
    q = conn.execute("SELECT * FROM questions WHERE question_text LIKE '%yourself%'").fetchone()
    if q:
        print(f"ID: {q['id']}")
        print(f"Text: {q['question_text']}")
        print(f"Keywords: '{q['expected_keywords']}'")
    else:
        print("Question not found.")
        
    conn.close()

if __name__ == "__main__":
    check_keywords()
