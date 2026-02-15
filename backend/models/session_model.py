from database import get_db_connection
from datetime import datetime

def create_session(user_id, resume_id, total_questions):
    """
    Create a new interview session
    """
    conn = get_db_connection()
    cursor = conn.execute(
        "INSERT INTO interview_sessions (user_id, resume_id, total_questions) VALUES (?, ?, ?)",
        (user_id, resume_id, total_questions)
    )
    session_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return session_id

def save_answer(session_id, question_id, user_answer, score, feedback):
    """
    Save user's answer with score and feedback
    """
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO answers (session_id, question_id, user_answer, score, feedback) VALUES (?, ?, ?, ?, ?)",
        (session_id, question_id, user_answer, score, feedback)
    )
    conn.commit()
    conn.close()

def update_session_score(session_id):
    """
    Calculate and update total score for a session
    """
    conn = get_db_connection()
    
    # Calculate average score from all answers
    result = conn.execute(
        "SELECT AVG(score) as avg_score FROM answers WHERE session_id = ?",
        (session_id,)
    ).fetchone()
    
    avg_score = result['avg_score'] if result['avg_score'] else 0
    
    # Update session with total score
    conn.execute(
        "UPDATE interview_sessions SET total_score = ? WHERE id = ?",
        (avg_score, session_id)
    )
    conn.commit()
    conn.close()
    return avg_score

def complete_session(session_id):
    """
    Mark session as completed
    """
    conn = get_db_connection()
    conn.execute(
        "UPDATE interview_sessions SET status = 'completed', completed_at = ? WHERE id = ?",
        (datetime.now(), session_id)
    )
    conn.commit()
    conn.close()

def get_session_results(session_id):
    """
    Get complete session data with all answers
    """
    conn = get_db_connection()
    
    # Get session info
    session = conn.execute(
        "SELECT * FROM interview_sessions WHERE id = ?",
        (session_id,)
    ).fetchone()
    
    # Get all answers with question details
    answers = conn.execute(
        """
        SELECT a.*, q.question_text, q.difficulty, s.skill_name
        FROM answers a
        JOIN questions q ON a.question_id = q.id
        JOIN skills s ON q.skill_id = s.id
        WHERE a.session_id = ?
        ORDER BY a.answered_at
        """,
        (session_id,)
    ).fetchall()
    
    conn.close()
    
    return {
        'session': dict(session) if session else None,
        'answers': [dict(answer) for answer in answers]
    }

def get_user_history(user_id):
    """
    Get all interview sessions for a user
    """
    conn = get_db_connection()
    sessions = conn.execute(
        """
        SELECT * FROM interview_sessions 
        WHERE user_id = ? 
        ORDER BY started_at DESC
        """,
        (user_id,)
    ).fetchall()
    conn.close()
    return [dict(session) for session in sessions]

def get_answered_questions(session_id):
    """
    Get list of question IDs already answered in this session
    """
    conn = get_db_connection()
    answered = conn.execute(
        "SELECT question_id FROM answers WHERE session_id = ?",
        (session_id,)
    ).fetchall()
    conn.close()
    return [row['question_id'] for row in answered]

def get_session_by_id(session_id):
    """
    Get session details by ID
    """
    conn = get_db_connection()
    session = conn.execute(
        "SELECT * FROM interview_sessions WHERE id = ?",
        (session_id,)
    ).fetchone()
    conn.close()
    return dict(session) if session else None
