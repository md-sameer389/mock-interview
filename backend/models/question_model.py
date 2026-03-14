from database import get_db_connection

def get_questions_by_skills(skill_names, limit=15):
    """
    Fetch 15 questions in a B.Tech placement pattern:
    1. Intro/Behavioral (2 questions) - Easy
    2. Core Skills (8 questions) - Medium (mix of skills)
    3. Advanced/Challenge (5 questions) - Hard (Coding, System Design)
    """
    conn = get_db_connection()
    unique_skills = list(set(skill_names))
    placeholders = ','.join('?' * len(unique_skills))
    
    questions = []
    
    # 1. INTRO / BEHAVIORAL (2 Questions)
    # Fetch specifically 'Behavioral' topic or just Easy General questions
    intro_query = """
        SELECT DISTINCT q.id, q.question_text, q.difficulty, q.question_type, s.skill_name, q.code_snippet 
        FROM questions q
        JOIN skills s ON q.skill_id = s.id
        WHERE (q.topic = 'Behavioral' OR q.difficulty = 'Easy')
        ORDER BY RANDOM() LIMIT 2
    """
    intro_questions = conn.execute(intro_query).fetchall()
    questions.extend(intro_questions)
    
    # 2. CORE SKILLS (8 Questions)
    # Medium difficulty from user's skills
    core_query = f"""
        SELECT DISTINCT q.id, q.question_text, q.difficulty, q.question_type, s.skill_name, q.code_snippet
        FROM questions q
        JOIN skills s ON q.skill_id = s.id
        WHERE s.skill_name IN ({placeholders})
        AND q.difficulty = 'Medium'
        ORDER BY RANDOM() LIMIT 8
    """
    core_questions = conn.execute(core_query, unique_skills).fetchall()
    questions.extend(core_questions)
    
    # Check if we have enough Core questions. If not, fill with any Medium questions
    if len(core_questions) < 8:
        needed = 8 - len(core_questions)
        backup_core = conn.execute(f"""
            SELECT DISTINCT q.id, q.question_text, q.difficulty, q.question_type, s.skill_name, q.code_snippet
            FROM questions q
            JOIN skills s ON q.skill_id = s.id
            WHERE q.difficulty = 'Medium' 
            AND q.id NOT IN ({','.join(str(q[0]) for q in questions) or '0'})
            ORDER BY RANDOM() LIMIT ?
        """, (needed,)).fetchall()
        questions.extend(backup_core)

    # 3. ADVANCED / CHALLENGE (5 Questions)
    # Hard difficulty (Coding, System Design)
    adv_query = f"""
        SELECT DISTINCT q.id, q.question_text, q.difficulty, q.question_type, s.skill_name, q.code_snippet
        FROM questions q
        JOIN skills s ON q.skill_id = s.id
        WHERE s.skill_name IN ({placeholders})
        AND q.difficulty = 'Hard'
        ORDER BY RANDOM() LIMIT 5
    """
    adv_questions = conn.execute(adv_query, unique_skills).fetchall()
    questions.extend(adv_questions)
    
    # Check if we have enough Advanced questions. If not, fill with any Hard questions
    if len(adv_questions) < 5:
        needed = 5 - len(adv_questions)
        backup_adv = conn.execute(f"""
            SELECT DISTINCT q.id, q.question_text, q.difficulty, q.question_type, s.skill_name, q.code_snippet
            FROM questions q
            JOIN skills s ON q.skill_id = s.id
            WHERE q.difficulty = 'Hard'
            AND q.id NOT IN ({','.join(str(q[0]) for q in questions) or '0'})
            ORDER BY RANDOM() LIMIT ?
        """, (needed,)).fetchall()
        questions.extend(backup_adv)
        
    conn.close()
    return questions

def update_question_stats(question_id, score):
    """
    Update usage stats: times_asked and avg_score
    """
    conn = get_db_connection()
    try:
        # Get current stats
        row = conn.execute("SELECT times_asked, avg_score FROM questions WHERE id = ?", (question_id,)).fetchone()
        if row:
            times = row[0] if row[0] else 0
            avg = row[1] if row[1] else 0.0
            
            new_times = times + 1
            # Running average update: new_avg = ((old_avg * old_times) + new_score) / new_times
            new_avg = ((avg * times) + score) / new_times
            
            conn.execute("UPDATE questions SET times_asked = ?, avg_score = ? WHERE id = ?", 
                         (new_times, new_avg, question_id))
            conn.commit()
    except Exception as e:
        print(f"Error updating stats: {e}")
    finally:
        conn.close()

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
        # Simplified: Removed topic, companies, hints, explanation insertion
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
