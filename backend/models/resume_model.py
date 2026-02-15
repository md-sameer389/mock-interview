from database import get_db_connection

def save_resume(user_id, filename, extracted_text):
    """
    Save resume metadata and extracted text to database
    """
    conn = get_db_connection()
    cursor = conn.execute(
        "INSERT INTO resumes (user_id, filename, extracted_text) VALUES (?, ?, ?)",
        (user_id, filename, extracted_text)
    )
    resume_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return resume_id

def save_candidate_skills(user_id, skills):
    """
    Save extracted skills for a candidate
    """
    conn = get_db_connection()
    try:
        # First, clear previous skills for this user (assuming re-upload replaces skills)
        conn.execute("DELETE FROM candidate_skills WHERE user_id = ?", (user_id,))
        
        # Insert new skills
        for skill in skills:
            conn.execute(
                "INSERT INTO candidate_skills (user_id, skill_name) VALUES (?, ?)",
                (user_id, skill)
            )
        conn.commit()
    except Exception as e:
        print(f"Error saving skills: {e}")
    finally:
        conn.close()

def get_resume_by_user(user_id):
    """
    Fetch the most recent resume for a user
    """
    conn = get_db_connection()
    resume = conn.execute(
        "SELECT * FROM resumes WHERE user_id = ? ORDER BY uploaded_at DESC LIMIT 1",
        (user_id,)
    ).fetchone()
    conn.close()
    return resume

def get_resume_by_id(resume_id):
    """
    Fetch resume by ID
    """
    conn = get_db_connection()
    resume = conn.execute(
        "SELECT * FROM resumes WHERE id = ?",
        (resume_id,)
    ).fetchone()
    conn.close()
    return resume
