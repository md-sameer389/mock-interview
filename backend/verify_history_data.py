from services.student_service import get_student_history
from database import get_db_connection

def verify_active():
    conn = get_db_connection()
    # Find a user who HAS sessions
    # Query: users joined with interview_sessions
    query = """
        SELECT DISTINCT u.id, u.full_name 
        FROM users u
        JOIN interview_sessions s ON u.id = s.user_id
        LIMIT 1
    """
    user = conn.execute(query).fetchone()
    
    if not user:
        print("No users with history found.")
        return

    print(f"Testing for user with history: {user['full_name']} (ID: {user['id']})")
    
    history = get_student_history(user['id'])
    print(f"Found {len(history)} history items")
    
    if history:
        print("First item keys:", history[0].keys())
        print("First item session_id:", history[0].get('session_id'))
    
    conn.close()

if __name__ == "__main__":
    verify_active()
