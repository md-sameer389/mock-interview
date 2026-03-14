import sqlite3
DB_PATH = r"c:\Users\sameer\OneDrive\Desktop\mock\database\interview.db"

def check_intro():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    
    # 1. Find the question
    q = conn.execute("SELECT * FROM questions WHERE question_text LIKE '%yourself%'").fetchall()
    for row in q:
        print(f"ID: {row['id']}, Text: {row['question_text']}, Skill_ID: {row['skill_id']}, Difficulty: {row['difficulty']}")
        
    # 2. Find General Skill ID
    skills = conn.execute("SELECT * FROM skills WHERE skill_name IN ('General', 'Behavioral', 'Python')").fetchall()
    for s in skills:
        print(f"Skill: {s['skill_name']}, ID: {s['id']}")
        
    conn.close()

if __name__ == "__main__":
    check_intro()
