import sqlite3
from utils.skill_extractor import extract_skills_from_text

DB_PATH = r"c:\Users\sameer\OneDrive\Desktop\mock\database\interview.db"

def check_resume_skills():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    
    # Get latest resume
    # We don't have user_id easily, just grab the most recent resume
    try:
        resume = conn.execute("SELECT id, filename, extracted_text FROM resumes ORDER BY id DESC LIMIT 1").fetchone()
        if resume:
            print(f"Resume: {resume['filename']}")
            skills = extract_skills_from_text(resume['extracted_text'])
            print(f"Extracted Skills: {skills}")
        else:
            print("No resume found.")
    except Exception as e:
        print(e)
    finally:
        conn.close()

if __name__ == "__main__":
    check_resume_skills()
