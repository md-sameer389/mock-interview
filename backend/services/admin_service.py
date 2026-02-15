from database import get_db_connection
import logging

logger = logging.getLogger(__name__)

def get_overall_stats():
    """
    Get high-level statistics for the dashboard
    """
    conn = get_db_connection()
    stats = {}
    
    try:
        # 1. Total Users (Candidates)
        stats['total_candidates'] = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        
        # 2. Total Interviews Conducted
        stats['total_interviews'] = conn.execute("SELECT COUNT(*) FROM interview_sessions").fetchone()[0]
        
        # 3. Average Technical Score (normalized to 10 scale if needed, or raw)
        # Using avg score from sessions
        avg_score_row = conn.execute("SELECT AVG(total_score) FROM interview_sessions WHERE status = 'completed'").fetchone()
        stats['avg_score'] = round(avg_score_row[0], 1) if avg_score_row[0] else 0
        
        # 4. Placement Readiness (Mock metric: Ratio of high scores > 7)
        high_performers = conn.execute("SELECT COUNT(*) FROM interview_sessions WHERE total_score >= 7 AND status = 'completed'").fetchone()[0]
        completed_sessions = conn.execute("SELECT COUNT(*) FROM interview_sessions WHERE status = 'completed'").fetchone()[0]
        
        stats['placement_readiness'] = round((high_performers / completed_sessions * 100), 1) if completed_sessions > 0 else 0
        
    except Exception as e:
        logger.error(f"Error fetching stats: {e}")
        stats = {'error': str(e)}
    finally:
        conn.close()
        
    return stats

def get_recent_activity(limit=10):
    """
    Get recent interview sessions with user details
    """
    conn = get_db_connection()
    activity = []
    
    try:
        query = """
            SELECT 
                s.id as session_id,
                u.full_name,
                s.total_score,
                s.status,
                s.started_at,
                (SELECT COUNT(*) FROM answers WHERE session_id = s.id) as questions_answered
            FROM interview_sessions s
            JOIN users u ON s.user_id = u.id
            ORDER BY s.started_at DESC
            LIMIT ?
        """
        rows = conn.execute(query, (limit,)).fetchall()
        
        for row in rows:
            activity.append(dict(row))
            
    except Exception as e:
        logger.error(f"Error fetching activity: {e}")
    finally:
        conn.close()
        
    return activity

def get_all_students():
    """
    Get all students with their aggregate stats
    """
    conn = get_db_connection()
    students = []
    
    try:
        query = """
            SELECT 
                u.id, 
                u.full_name, 
                u.email,
                COUNT(s.id) as total_sessions,
                AVG(s.total_score) as avg_score,
                MAX(s.started_at) as last_active
            FROM users u
            LEFT JOIN interview_sessions s ON u.id = s.user_id
            GROUP BY u.id
            ORDER BY last_active DESC
        """
        rows = conn.execute(query).fetchall()
        for row in rows:
            r = dict(row)
            # Handle nulls
            if r['avg_score']: r['avg_score'] = round(r['avg_score'], 1)
            else: r['avg_score'] = 0.0
            students.append(r)
            
    except Exception as e:
        logger.error(f"Error fetching students: {e}")
    finally:
        conn.close()
        
    return students

def get_student_details(user_id):
    """
    Get detailed profile for a student
    """
    conn = get_db_connection()
    data = {}
    
    try:
        # User Info
        user = conn.execute("SELECT id, full_name, email FROM users WHERE id = ?", (user_id,)).fetchone()
        if not user:
            return None
        data['user'] = dict(user)
        
        # Session History
        sessions_query = """
            SELECT id, total_score, status, started_at, total_questions 
            FROM interview_sessions 
            WHERE user_id = ? 
            ORDER BY started_at DESC
        """
        sessions = conn.execute(sessions_query, (user_id,)).fetchall()
        data['sessions'] = [dict(s) for s in sessions]
        
    except Exception as e:
        logger.error(f"Error fetching detail: {e}")
    finally:
        conn.close()
        
    return data

def get_skill_performance():
    """
    Aggregate average scores by skill
    """
    conn = get_db_connection()
    skills_data = []
    
    try:
        # Join answers -> questions -> skills
        query = """
            SELECT s.skill_name, AVG(a.score) as avg_score, COUNT(a.id) as answer_count
            FROM answers a
            JOIN questions q ON a.question_id = q.id
            JOIN skills s ON q.skill_id = s.id
            GROUP BY s.id
            ORDER BY avg_score DESC
        """
        rows = conn.execute(query).fetchall()
        
        for row in rows:
            r = dict(row)
            if r['avg_score']: r['avg_score'] = round(r['avg_score'], 1)
            skills_data.append(r)
            
    except Exception as e:
        logger.error(f"Error fetching skill stats: {e}")
    finally:
        conn.close()
        
    return skills_data

def get_daily_activity(days=7):
    """
    Get session counts for the last N days
    """
    conn = get_db_connection()
    activity_data = []
    
    try:
        # SQLite: use strftime for dates
        query = """
            SELECT 
                date(started_at) as interview_date, 
                COUNT(*) as session_count
            FROM interview_sessions
            WHERE started_at >= date('now', ?)
            GROUP BY interview_date
            ORDER BY interview_date ASC
        """
        rows = conn.execute(query, (f'-{days} days',)).fetchall()
        
        for row in rows:
            activity_data.append(dict(row))
            
    except Exception as e:
        logger.error(f"Error fetching daily activity: {e}")
    finally:
        conn.close()
        
    return activity_data

def get_drives():
    """
    Get all placement drives
    """
    conn = get_db_connection()
    drives = []
    
    try:
        rows = conn.execute("SELECT * FROM drives ORDER BY date ASC").fetchall()
        for row in rows:
            drives.append(dict(row))
    except Exception as e:
        logger.error(f"Error fetching drives: {e}")
    finally:
        conn.close()
        
    return drives

def create_drive(data):
    """
    Create a new placement drive
    """
    conn = get_db_connection()
    try:
        conn.execute("""
            INSERT INTO drives (company, role, required_skills, description, date, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (data['company'], data['role'], data.get('required_skills', ''), data['description'], data['date'], 'Upcoming'))
        conn.commit()
        return True
    except Exception as e:
        logger.error(f"Error creating drive: {e}")
        return False
    finally:
        conn.close()

def delete_drive(drive_id):
    """
    Delete a placement drive
    """
    conn = get_db_connection()
    try:
        conn.execute("DELETE FROM drives WHERE id = ?", (drive_id,))
        conn.commit()
        return True
    except Exception as e:
        logger.error(f"Error deleting drive: {e}")
        return False
    finally:
        conn.close()

def reset_system():
    """
    Clear all interview data (Dangerous!)
    """
    conn = get_db_connection()
    try:
        # Clear sessions and answers
        conn.execute("DELETE FROM answers")
        conn.execute("DELETE FROM interview_sessions")
        # Optional: Clear users too? keeping users for now as they might be registered.
        # conn.execute("DELETE FROM users") 
        conn.commit()
        return True
    except Exception as e:
        logger.error(f"Error resetting system: {e}")
        return False
    finally:
        conn.close()
