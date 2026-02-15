from database import get_db_connection

def get_questions_by_skills(skill_names, limit=10):
    """
    Fetch questions matching the given skills
    Returns a mix of Easy, Medium, and Hard questions
    """
    conn = get_db_connection()
    
    # Deduplicate skill names to prevent potential query issues
    unique_skills = list(set(skill_names))
    
    # Create placeholders for SQL IN clause
    placeholders = ','.join('?' * len(unique_skills))
    
    # Query questions for matching skills, ordered by difficulty
    # Use DISTINCT to be absolutely sure we don't get duplicates
    query = f"""
        SELECT DISTINCT q.*, s.skill_name 
        FROM questions q
        JOIN skills s ON q.skill_id = s.id
        WHERE s.skill_name IN ({placeholders})
        -- SAFETY NET: Only show coding questions if they have valid test cases
        AND (q.question_type != 'coding' OR (q.test_cases IS NOT NULL AND length(q.test_cases) > 5))
        ORDER BY 
            CASE q.difficulty
                WHEN 'Easy' THEN 1
                WHEN 'Medium' THEN 2
                WHEN 'Hard' THEN 3
            END,
            RANDOM()
        LIMIT ?
    """
    
    questions = conn.execute(query, (*unique_skills, limit)).fetchall()
    conn.close()
    return questions

def get_question_by_id(question_id):
    """
    Get specific question details by ID
    """
    conn = get_db_connection()
    question = conn.execute(
        "SELECT * FROM questions WHERE id = ?",
        (question_id,)
    ).fetchone()
    conn.close()
    return question

def get_all_skills():
    """
    Get all skills from database
    """
    conn = get_db_connection()
    skills = conn.execute("SELECT * FROM skills").fetchall()
    conn.close()
    return skills

def create_dynamic_question(text, skill_name, difficulty, expected_keywords, q_type='text'):
    """
    Create a new question if it doesn't exist, returning its ID.
    Handles skill lookup/creation too.
    """
    conn = get_db_connection()
    try:
        # 1. Get/Create Skill ID
        skill = conn.execute("SELECT id FROM skills WHERE skill_name = ?", (skill_name,)).fetchone()
        if skill:
            skill_id = skill[0]
        else:
            # Fallback to 'General' or create
            general = conn.execute("SELECT id FROM skills WHERE skill_name = 'General'").fetchone()
            if general:
                skill_id = general[0]
            else:
                # Create default General skill
                cursor = conn.execute("INSERT INTO skills (skill_name, keywords) VALUES (?, ?)", ('General', 'general'))
                skill_id = cursor.lastrowid
        
        # 2. Check if question exists
        existing = conn.execute("SELECT id FROM questions WHERE question_text = ?", (text,)).fetchone()
        if existing:
            return existing[0]
            
        # 3. Insert Question
        cursor = conn.execute("""
            INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords, question_type)
            VALUES (?, ?, ?, ?, ?)
        """, (skill_id, text, difficulty, expected_keywords, q_type))
        
        conn.commit()
        return cursor.lastrowid
    except Exception as e:
        print(f"Error creating dynamic question: {e}")
        return None
    finally:
        conn.close()
