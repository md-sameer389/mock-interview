import sqlite3
DB_PATH = r"c:\Users\sameer\OneDrive\Desktop\mock\database\interview.db"

def update_intro():
    conn = sqlite3.connect(DB_PATH)
    
    # Update 'Tell me about yourself' (and similar) to General Skill (ID 11)
    # Finding General ID first just to be safe
    gen_id = conn.execute("SELECT id FROM skills WHERE skill_name = 'General'").fetchone()[0]
    print(f"General Skill ID: {gen_id}")
    
    # Update questions
    cursor = conn.execute("UPDATE questions SET skill_id = ? WHERE question_text LIKE '%yourself%'", (gen_id,))
    print(f"Updated {cursor.rowcount} questions to General Skill.")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    update_intro()
