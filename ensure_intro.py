import sqlite3

DB_PATH = r"c:\Users\sameer\OneDrive\Desktop\mock\database\interview.db"

def ensure_intro_question():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    Q_TEXT = "Tell me about yourself."
    
    # Check if exists
    cursor.execute("SELECT id FROM questions WHERE question_text = ?", (Q_TEXT,))
    row = cursor.fetchone()
    
    if row:
        print(f"Found existing: {row[0]}")
    else:
        print("Inserting new question...")
        cursor.execute("INSERT INTO questions (skill_id, question_text, difficulty, topic, expected_keywords) VALUES (1, ?, 'Easy', 'Behavioral', 'experience, background, role, project')", (Q_TEXT,))
        conn.commit()
        print(f"Inserted. New ID: {cursor.lastrowid}")
        
    conn.close()

if __name__ == "__main__":
    ensure_intro_question()
