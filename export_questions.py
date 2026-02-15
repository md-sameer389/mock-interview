import sqlite3
import os
import json

DB_PATH = os.path.join(os.path.dirname(__file__), 'database/interview.db')
OUTPUT_FILE = 'all_questions.md'

def export_questions():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Fetch all questions
    cursor.execute("""
        SELECT id, skill_id, question_text, difficulty, question_type, 
               expected_keywords, code_snippet, correct_output 
        FROM questions 
        ORDER BY skill_id, id
    """)
    questions = cursor.fetchall()
    
    # Fetch skill names
    cursor.execute("SELECT id, skill_name FROM skills")
    skills = {row[0]: row[1] for row in cursor.fetchall()}
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# Full Question Database\n\n")
        f.write(f"Total Questions: {len(questions)}\n\n")
        
        for q in questions:
            q_id, skill_id, text, diff, q_type, keywords, code, output = q
            skill = skills.get(skill_id, "Unknown")
            
            f.write(f"## {q_id}. [{skill}] {text}\n")
            f.write(f"- **Type:** {q_type.upper() if q_type else 'TEXT'}\n")
            f.write(f"- **Difficulty:** {diff}\n")
            
            if q_type == 'coding' or q_type == 'output_guess':
                if code:
                    f.write(f"- **Code Snippet:**\n```python\n{code}\n```\n")
                if output:
                    f.write(f"- **Correct Output:** `{output}`\n")
                if keywords and q_type == 'output_guess' and not output:
                     f.write(f"- **Correct Output (legacy):** `{keywords}`\n")
                if keywords and q_type == 'coding':
                     f.write(f"- **Required Keywords:** `{keywords}`\n")

            else:
                f.write(f"- **Expected Keywords (Answer Key):** {keywords}\n")
            
            f.write("\n---\n")
            
    conn.close()
    print(f"Exported {len(questions)} questions to {OUTPUT_FILE}")

if __name__ == "__main__":
    export_questions()
