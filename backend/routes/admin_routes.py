from flask import Blueprint, jsonify, request
import logging
from database import get_db_connection
from services.auth_service import token_required
import sqlite3

logger = logging.getLogger(__name__)
admin_bp = Blueprint('admin', __name__)

# --- Quality Control (Student Facing) ---
@admin_bp.route('/api/flag_answer', methods=['POST'])
@token_required
def flag_answer(current_user_id):
    """
    Allow students to flag an answer as unfair/incorrect.
    Body: { "session_id": int, "question_id": int, "reason": str }
    """
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Request body is required'}), 400
        
        session_id = data.get('session_id')
        question_id = data.get('question_id')
        reason = data.get('reason', 'Unspecified')
        
        if not session_id or not question_id:
            return jsonify({'error': 'Missing session_id and question_id'}), 400
        
        if not isinstance(reason, str) or len(reason.strip()) == 0:
            return jsonify({'error': 'Reason must be a non-empty string'}), 400
        
        # Verify session belongs to current user
        from models.session_model import get_session_by_id
        session = get_session_by_id(session_id)
        if not session or session['user_id'] != current_user_id:
            return jsonify({'error': 'Unauthorized access to this session'}), 403
        
        try:
            conn = get_db_connection()
            # Check if columns exist, if not, this might fail unless migration run
            conn.execute("""
                UPDATE answers 
                SET flagged = 1, flag_reason = ? 
                WHERE session_id = ? AND question_id = ?
            """, (reason, session_id, question_id))
            conn.commit()
            conn.close()
            logger.info(f"Answer flagged by user {current_user_id}: session {session_id}, question {question_id}")
            return jsonify({'message': 'Issue reported successfully. Admin will review.'}), 200
        except sqlite3.OperationalError:
            logger.warning("Flag column not yet migrated in database")
            return jsonify({'error': 'Flagging not yet available'}), 501
    except Exception as e:
        logger.error(f"Error flagging answer: {str(e)}")
        return jsonify({'error': 'Error reporting issue. Please try again.'}), 500

# --- Admin Dashboard (Admin Facing) ---

@admin_bp.route('/api/admin/stats', methods=['GET'])
@token_required
def get_stats(current_user_id):
    """
    Returns aggregated statistics for the dashboard.
    Expected by frontend: total_candidates, total_interviews, avg_score, placement_readiness
    """
    try:
        # Verify admin role
        conn = get_db_connection()
        user = conn.execute("SELECT role FROM users WHERE id = ?", (current_user_id,)).fetchone()
        if not user or user['role'] != 'admin':
            return jsonify({'error': 'Admin access required'}), 403
        
        # 1. Total Candidates (All registered students)
        total_candidates = conn.execute("SELECT COUNT(*) FROM users WHERE role = 'student'").fetchone()[0]
        
        # 2. Total Interviews
        total_interviews = conn.execute("SELECT COUNT(*) FROM interview_sessions").fetchone()[0]
        
        # 3. Average Score
        avg_score = conn.execute("SELECT AVG(total_score) FROM interview_sessions WHERE status = 'completed'").fetchone()[0]
        avg_score = round(avg_score, 1) if avg_score else 0.0
        
        # 4. Placement Readiness (Custom Metric: % of sessions with score > 7)
        strong_sessions = conn.execute("SELECT COUNT(*) FROM interview_sessions WHERE status = 'completed' AND total_score >= 7.0").fetchone()[0]
        placement_readiness = round((strong_sessions / total_interviews * 100), 1) if total_interviews > 0 else 0
        
        conn.close()
        conn.close()
        
        return jsonify({
            'total_candidates': total_candidates,
            'total_interviews': total_interviews,
            'avg_score': avg_score,
            'placement_readiness': placement_readiness
        })
    except Exception as e:
        print(f"Stats Error: {e}")
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/api/admin/activity', methods=['GET'])
def get_activity():
    """
    Recent interview activity.
    Returns: list of { full_name, session_id, started_at, status, questions_answered, total_score }
    """
    try:
        conn = get_db_connection()
        query = """
            SELECT 
                u.full_name, 
                s.id as session_id, 
                s.started_at, 
                s.status, 
                s.total_questions as questions_answered, 
                s.total_score 
            FROM interview_sessions s
            JOIN users u ON s.user_id = u.id
            ORDER BY s.started_at DESC
            LIMIT 10
        """
        rows = conn.execute(query).fetchall()
        activity = [dict(row) for row in rows]
        conn.close()
        return jsonify(activity)
    except Exception as e:
        print(f"Activity Error: {e}")
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/api/admin/students', methods=['GET'])
def get_students():
    """
    List of all students with summary stats.
    """
    try:
        conn = get_db_connection()
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
            WHERE u.role = 'student' OR u.role IS NULL
            GROUP BY u.id
        """
        rows = conn.execute(query).fetchall()
        
        students = []
        for row in rows:
            s_dict = dict(row)
            s_dict['avg_score'] = round(s_dict['avg_score'], 1) if s_dict['avg_score'] else 0.0
            students.append(s_dict)
            
        conn.close()
        return jsonify(students)
    except Exception as e:
        print(f"Students Error: {e}")
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/api/admin/students/<int:user_id>', methods=['DELETE'])
def delete_student(user_id):
    """
    Delete a student and all their associated data (Cascading delete).
    """
    try:
        conn = get_db_connection()
        
        # 1. Check if user exists and is a student
        user = conn.execute("SELECT role FROM users WHERE id = ?", (user_id,)).fetchone()
        if not user:
            conn.close()
            return jsonify({'error': 'User not found'}), 404
        
        # Optional: Prevent deleting other admins if that was possible via this route
        # (Though route logic implies students list)
        if user['role'] == 'admin':
            conn.close()
            return jsonify({'error': 'Cannot delete admin accounts via this route'}), 403

        # 2. Delete related data manually (in case FK constraints aren't enabled)
        # Delete Answers
        conn.execute("""
            DELETE FROM answers 
            WHERE session_id IN (SELECT id FROM interview_sessions WHERE user_id = ?)
        """, (user_id,))
        
        # Delete Sessions
        conn.execute("DELETE FROM interview_sessions WHERE user_id = ?", (user_id,))
        
        # Delete Resumes
        conn.execute("DELETE FROM resumes WHERE user_id = ?", (user_id,))
        
        # 3. Delete User
        conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
        
        conn.commit()
        conn.close()
        
        logger.info(f"Student {user_id} deleted by admin.")
        return jsonify({'message': 'Student deleted successfully'}), 200

    except Exception as e:
        logger.error(f"Error deleting student {user_id}: {e}")
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/api/admin/students/<int:user_id>', methods=['GET'])
def get_student_details(user_id):
    """
    Details for a specific student.
    """
    try:
        conn = get_db_connection()
        
        user = conn.execute("SELECT id, full_name, email FROM users WHERE id = ?", (user_id,)).fetchone()
        if not user:
            return jsonify({'error': 'User not found'}), 404
            
        sessions_rows = conn.execute("""
            SELECT started_at, total_score, status 
            FROM interview_sessions 
            WHERE user_id = ? 
            ORDER BY started_at DESC
        """, (user_id,)).fetchall()
        
        sessions = [dict(row) for row in sessions_rows]
        
        conn.close()
        
        return jsonify({
            'user': dict(user),
            'sessions': sessions
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# --- Analytics ---

@admin_bp.route('/api/admin/analytics/skills', methods=['GET'])
def get_skill_analytics():
    """
    Average score per skill.
    """
    try:
        conn = get_db_connection()
        query = """
            SELECT 
                sk.skill_name, 
                AVG(a.score) as avg_score
            FROM answers a
            JOIN questions q ON a.question_id = q.id
            JOIN skills sk ON q.skill_id = sk.id
            GROUP BY sk.skill_name
        """
        rows = conn.execute(query).fetchall()
        analytics = [{'skill_name': row[0], 'avg_score': round(row[1], 1)} for row in rows]
        conn.close()
        return jsonify(analytics)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/api/admin/analytics/activity', methods=['GET'])
def get_activity_analytics():
    """
    Interviews conducted per day (last 7 data points).
    """
    try:
        conn = get_db_connection()
        query = """
            SELECT 
                date(started_at) as interview_date, 
                COUNT(*) as session_count
            FROM interview_sessions
            GROUP BY date(started_at)
            ORDER BY date(started_at) DESC
            LIMIT 7
        """
        rows = conn.execute(query).fetchall()
        # Reverse to show chronological order
        analytics = [{'interview_date': row[0], 'session_count': row[1]} for row in reversed(rows)]
        conn.close()
        return jsonify(analytics)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# --- Placement Drives ---

@admin_bp.route('/api/admin/drives', methods=['GET'])
def get_drives():
    try:
        conn = get_db_connection()
        rows = conn.execute("SELECT * FROM drives ORDER BY date DESC").fetchall()
        drives = [dict(row) for row in rows]
        conn.close()
        return jsonify(drives)
    except Exception as e:
        # Table might not exist if migration failed
        print(f"Drives Error: {e}")
        return jsonify([]), 200 # Return empty list gracefully

@admin_bp.route('/api/admin/drives', methods=['POST'])
def create_drive():
    data = request.json
    try:
        conn = get_db_connection()
        conn.execute("""
            INSERT INTO drives (company, role, date, description, status)
            VALUES (?, ?, ?, ?, 'Open')
        """, (data['company'], data['role'], data['date'], data['description']))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Drive created'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/api/admin/drives/<int:id>', methods=['DELETE'])
def delete_drive(id):
    try:
        conn = get_db_connection()
        conn.execute("DELETE FROM drives WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Drive deleted'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# --- Reports ---

@admin_bp.route('/api/admin/reports', methods=['GET'])
def get_reports():
    """
    Fetch all flagged answers/reports.
    """
    try:
        conn = get_db_connection()
        query = """
            SELECT 
                u.full_name as student_name,
                a.session_id,
                q.question_text,
                a.flag_reason,
                a.transcript as user_answer,
                a.feedback,
                a.score
            FROM answers a
            JOIN interview_sessions s ON a.session_id = s.id
            JOIN users u ON s.user_id = u.id
            JOIN questions q ON a.question_id = q.id
            WHERE a.flagged = 1
            ORDER BY s.started_at DESC
        """
        try:
            rows = conn.execute(query).fetchall()
            reports = [dict(row) for row in rows]
        except sqlite3.OperationalError as e:
            # Handle case where 'flagged' column might be missing if migration didn't run
            print(f"Reports Query Error (possible missing migration): {e}")
            reports = []

        conn.close()
        return jsonify(reports)
    except Exception as e:
        print(f"Reports Error: {e}")
        return jsonify({'error': str(e)}), 500

# --- System Reset ---

@admin_bp.route('/api/admin/reset', methods=['POST'])
def system_reset():
    """
    Dangerous: Wipes all interview data.
    """
    try:
        conn = get_db_connection()
        # Delete data but keep users/questions/drives
        conn.execute("DELETE FROM answers")
        conn.execute("DELETE FROM interview_sessions")
        conn.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'answers'")
        conn.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'interview_sessions'")
        conn.commit()
        conn.close()
        return jsonify({'message': 'System reset successful'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
# --- Question Management ---

@admin_bp.route('/api/admin/questions', methods=['GET'])
@token_required
def get_questions(current_user_id):
    """
    Get all questions for admin management.
    """
    try:
        # Verify admin
        conn = get_db_connection()
        user = conn.execute("SELECT role FROM users WHERE id = ?", (current_user_id,)).fetchone()
        if not user or user['role'] != 'admin':
            return jsonify({'error': 'Admin access required'}), 403
            
        query = """
            SELECT q.id, q.question_text, q.difficulty, q.topic, q.expected_keywords, s.skill_name 
            FROM questions q
            JOIN skills s ON q.skill_id = s.id
            ORDER BY q.id DESC
        """
        rows = conn.execute(query).fetchall()
        questions = [dict(row) for row in rows]
        
        # Also fetch skills for the dropdown
        skills_rows = conn.execute("SELECT id, skill_name FROM skills").fetchall()
        skills = [dict(row) for row in skills_rows]
        
        conn.close()
        return jsonify({'questions': questions, 'skills': skills})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/api/admin/questions', methods=['POST'])
@token_required
def create_question(current_user_id):
    """
    Create a new question.
    """
    try:
        data = request.json
        # Verify admin
        conn = get_db_connection()
        user = conn.execute("SELECT role FROM users WHERE id = ?", (current_user_id,)).fetchone()
        if not user or user['role'] != 'admin':
            return jsonify({'error': 'Admin access required'}), 403
            
        # Basic validation
        if not data.get('question_text') or not data.get('skill_id'):
            return jsonify({'error': 'Question text and skill are required'}), 400
            
        conn.execute("""
            INSERT INTO questions (skill_id, question_text, difficulty, topic, expected_keywords, question_type)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            data['skill_id'], 
            data['question_text'], 
            data.get('difficulty', 'Medium'),
            data.get('topic', 'General'),
            data.get('expected_keywords', ''),
            data.get('question_type', 'text')
        ))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Question created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/api/admin/questions/<int:id>', methods=['PUT'])
@token_required
def update_question(current_user_id, id):
    """
    Update an existing question.
    """
    try:
        data = request.json
        # Verify admin
        conn = get_db_connection()
        user = conn.execute("SELECT role FROM users WHERE id = ?", (current_user_id,)).fetchone()
        if not user or user['role'] != 'admin':
            return jsonify({'error': 'Admin access required'}), 403
            
        conn.execute("""
            UPDATE questions 
            SET skill_id = ?, question_text = ?, difficulty = ?, topic = ?, expected_keywords = ?
            WHERE id = ?
        """, (
            data['skill_id'], 
            data['question_text'], 
            data.get('difficulty', 'Medium'),
            data.get('topic', 'General'),
            data.get('expected_keywords', ''),
            id
        ))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Question updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/api/admin/questions/<int:id>', methods=['DELETE'])
@token_required
def delete_question(current_user_id, id):
    """
    Delete a question.
    """
    try:
        # Verify admin
        conn = get_db_connection()
        user = conn.execute("SELECT role FROM users WHERE id = ?", (current_user_id,)).fetchone()
        if not user or user['role'] != 'admin':
            return jsonify({'error': 'Admin access required'}), 403
            
        conn.execute("DELETE FROM questions WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Question deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
