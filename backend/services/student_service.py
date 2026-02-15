from database import get_db_connection
import logging

logger = logging.getLogger(__name__)

def get_student_stats(user_id):
    """
    Get dashboard stats for a specific student
    """
    conn = get_db_connection()
    stats = {}
    
    try:
        # Total Interviews
        stats['total_interviews'] = conn.execute(
            "SELECT COUNT(*) FROM interview_sessions WHERE user_id = ?", 
            (user_id,)
        ).fetchone()[0]
        
        # Avg Score
        avg_score = conn.execute(
            "SELECT AVG(total_score) FROM interview_sessions WHERE user_id = ? AND status = 'completed'", 
            (user_id,)
        ).fetchone()[0]
        stats['avg_score'] = round(avg_score, 1) if avg_score else 0.0
        
        # Pending Interviews (In Progress)
        stats['pending_interviews'] = conn.execute(
            "SELECT COUNT(*) FROM interview_sessions WHERE user_id = ? AND status = 'in_progress'", 
            (user_id,)
        ).fetchone()[0]

        # Skill Performance Heatmap
        skill_query = """
            SELECT s.skill_name, AVG(a.score) as avg_score, COUNT(a.id) as answer_count
            FROM answers a
            JOIN interview_sessions ises ON a.session_id = ises.id
            JOIN questions q ON a.question_id = q.id
            JOIN skills s ON q.skill_id = s.id
            WHERE ises.user_id = ?
            GROUP BY s.skill_name
            ORDER BY avg_score DESC
        """
        skill_rows = conn.execute(skill_query, (user_id,)).fetchall()
        
        stats['skill_performance'] = [
            {'skill': row['skill_name'], 'avg_score': round(row['avg_score'], 1), 'count': row['answer_count']}
            for row in skill_rows
        ]

    except Exception as e:
        logger.error(f"Error fetching student stats: {e}")
        stats = {'error': str(e)}
    finally:
        conn.close()
        
    return stats

def get_eligible_drives(user_id=None):
    """
    Get all upcoming and open placement drives with skill matching
    """
    conn = get_db_connection()
    drives = []
    
    try:
        # 1. Fetch Student Skills if user_id is provided
        student_skills = set()
        if user_id:
            rows = conn.execute("SELECT skill_name FROM candidate_skills WHERE user_id = ?", (user_id,)).fetchall()
            student_skills = {row[0].lower() for row in rows}

        # 2. Fetch Drives
        query = "SELECT * FROM drives WHERE status IN ('Upcoming', 'Open') ORDER BY date ASC"
        rows = conn.execute(query).fetchall()
        
        for row in rows:
            drive = dict(row)
            
            # 3. Calculate Match Score
            required = drive.get('required_skills', '')
            match_score = 0
            
            if required:
                req_skills = [s.strip().lower() for s in required.split(',') if s.strip()]
                if req_skills:
                    matched_count = sum(1 for s in req_skills if s in student_skills)
                    match_score = int((matched_count / len(req_skills)) * 100)
            
            drive['match_score'] = match_score
            drive['student_skills_count'] = len(student_skills) # nice to start showing if they have 0 skills
            drives.append(drive)
            
    except Exception as e:
        logger.error(f"Error fetching drives: {e}")
    finally:
        conn.close()
        
    return drives

def get_student_history(user_id):
    """
    Get interview history for a student
    """
    conn = get_db_connection()
    history = []
    
    try:
        query = """
            SELECT id, total_score, status, started_at, total_questions 
            FROM interview_sessions 
            WHERE user_id = ? 
            ORDER BY started_at DESC
        """
        rows = conn.execute(query, (user_id,)).fetchall()
        
        for row in rows:
            history.append(dict(row))
            
    except Exception as e:
        logger.error(f"Error fetching history: {e}")
    finally:
        conn.close()
        
    return history
