import logging
from flask import jsonify
from database import get_db_connection
from models.resume_model import get_resume_by_id
from models.question_model import get_questions_by_skills, get_question_by_id, create_dynamic_question
from models.session_model import (
    create_session, save_answer, update_session_score, 
    complete_session, get_session_results, get_user_history,
    get_answered_questions, get_globally_seen_questions
)
from utils.skill_extractor import extract_skills_from_text
from utils.evaluator import evaluate_answer
from utils.question_generator import generate_heuristic_questions

logger = logging.getLogger(__name__)

def start_interview(user_id, resume_id, persona='standard'):
    """
    Start a new interview session with persona awareness
    """
    try:
        # Get resume
        resume = get_resume_by_id(resume_id)
        if not resume:
            return jsonify({'error': 'Resume not found'}), 404
        
        # Extract skills from resume text
        extracted_text = resume['extracted_text']
        skills = extract_skills_from_text(extracted_text)
        
        if not skills:
            # Fallback for MVP: Don't block user. Assume General engineering.
            logger.warning(f"No skills found in resume {resume_id}. Defaulting to General.")
            skills = ['General']
            
        # 1. Generate Dynamic Questions (Heuristic) based on Persona
        # DISABLING dynamic questions for now to ensure strict adherence to B.Tech pattern (Intro -> Core -> Hard)
        # dynamic_qs = generate_heuristic_questions(skills, count=3, persona=persona)
        created_dynamic_ids = []
        
        # 2. Get Standard Questions based on skills & persona
        # Fetch 15 to match the specific B.Tech pattern
        raw_standard_questions = get_questions_by_skills(skills, limit=15)
        
        filtered_standard_questions = []
        if persona == 'technical':
            # Prefer Hard/Medium
            filtered_standard_questions = [
                q for q in raw_standard_questions 
                if q['difficulty'] in ['Hard', 'Medium'] or q['question_type'] == 'coding'
            ]
        elif persona == 'hr':
            # Prefer Behavioral if possible (though we might not have many labeled as such linked to tech skills)
            # Or just Easy questions
            filtered_standard_questions = [
                q for q in raw_standard_questions 
                if q['difficulty'] == 'Easy' or q['skill_id'] == 1 # Assuming 1 is General/Behavioral - unsafe assumption but acceptable for mvp
            ]
        else:
            filtered_standard_questions = raw_standard_questions
            
        # Fallback if filtering removed too many
        if len(filtered_standard_questions) < 3:
             filtered_standard_questions = raw_standard_questions

        standard_questions = filtered_standard_questions

        # Cap it
        if not standard_questions and not created_dynamic_ids:
             return jsonify({'error': 'No questions found for your skills'}), 404

        # Combine Questions
        final_questions_pool = []
        
        # Add dynamic ones (high priority)
        # Note: We are disabling dynamic generation mostly, but keeping logic
        for qid in created_dynamic_ids:
            q_obj = get_question_by_id(qid)
            if q_obj:
                final_questions_pool.append(q_obj)
        
        # Add standard ones
        final_questions_pool.extend(standard_questions)
        
        # Ensure we have at least 15 for the session count
        # (Though get_next_question will enforce it dynamically)
        
        # Create session (save persona)
        # Note: create_session needs update to accept persona, or we do manual update
        session_id = create_session(user_id, resume_id, len(final_questions_pool))
        
        # Update persona column manually since create_session might not have it yet
        conn = get_db_connection()
        conn.execute("UPDATE interview_sessions SET persona = ? WHERE id = ?", (persona, session_id))
        conn.commit()
        conn.close()
        
        # Convert questions to list of dicts
        question_list = [dict(q) for q in final_questions_pool]
        
        return jsonify({
            'message': 'Interview started successfully',
            'session_id': session_id,
            'skills_found': skills,
            'total_questions': len(final_questions_pool),
            'questions': question_list
        }), 200
    
    except Exception as e:
        return jsonify({'error': f'Error starting interview: {str(e)}'}), 500

def get_next_question(session_id, current_skills=None):
    """
    Get the next unanswered question based on PROGRESSIVE STAGES:
    1. Warm-up (Q1-2): Easy / Intro
    2. Core (Q3-10): Medium
    3. Advanced (Q11-15): Hard
    """
    try:
        # 1. Check Session Status
        conn = get_db_connection()
        session = conn.execute("SELECT * FROM interview_sessions WHERE id = ?", (session_id,)).fetchone()
        
        if not session:
            conn.close()
            return None
            
        # 2. Get Answered Question IDs (current session)
        answered_ids = get_answered_questions(session_id)
        count_answered = len(answered_ids)

        # NO-REPEAT MODE: Exclude questions seen in ALL past sessions for this user
        globally_seen_ids = get_globally_seen_questions(session['user_id'])
        # Merge: union of current-session answered + all past sessions seen
        # Use a set to deduplicate, convert back to list for SQL
        excluded_ids = list(set(answered_ids) | set(globally_seen_ids))
        
        # HOTFIX: Force upgrade old sessions to 15 questions
        if session['total_questions'] < 15:
            logger.info(f"Upgrading session {session_id} from {session['total_questions']} to 15 questions.")
            conn.execute("UPDATE interview_sessions SET total_questions = 15 WHERE id = ?", (session_id,))
            conn.commit()
            # Update local dict to match
            # session is a Row, convert to dict to modify or just re-fetch?
            # Easiest is just to trust the new limit logic below
            session_limit = 15
        else:
            session_limit = session['total_questions']
        
        # 3. Check if we've reached the limit
        if count_answered >= session_limit:
            conn.close()
            return None # Interview Complete
            
        # 4. DETERMINE TARGET DIFFICULTY BASED ON STAGE
        curr_stage = "Core"
        target_difficulty = "Medium"
        
        if count_answered < 2:
            curr_stage = "Warm-up"
            target_difficulty = "Easy"
        elif count_answered < 10:
            curr_stage = "Core"
            target_difficulty = "Medium"
        else:
            # Last 5 questions (10-15)
            curr_stage = "Advanced"
            target_difficulty = "Hard"
            
        logger.info(f"Session {session_id}: Fetching Q{count_answered+1} ({curr_stage} - {target_difficulty})")

        # 5. Get User Skills
        resume = get_resume_by_id(session['resume_id'])
        extracted_text = resume['extracted_text']
        skills = extract_skills_from_text(extracted_text)
        if not skills: skills = ['General']
        
        # INJECT CORE SUBJECTS (Standard B.Tech Stack)
        # Even if not in resume, these are fair game and prevent running out of questions
        core_subjects = ['DBMS', 'Operating Systems', 'Computer Networks', 'SQL', 'Object Oriented Programming']
        for result in core_subjects:
            if result not in skills:
                skills.append(result)
            
        skill_placeholders = ','.join('?' * len(skills))
        # Use excluded_ids (global + current session) for no-repeat mode
        # Fallback: if all questions are exhausted globally, reset to session-only exclusion
        placeholders = ','.join('?' * len(excluded_ids)) if excluded_ids else '0'
        exclude_params = excluded_ids if excluded_ids else []
        
        # 6. Fetch Question
        # Prioritize 'Behavioral' for Warm-up if possible
        question = None
        
        if curr_stage == "Warm-up":
            # 1. ROTATING INTRO: Q1 always picks an unseen 'Introduction'-topic question
            if count_answered == 0:
                intro_placeholders = ','.join('?' * len(exclude_params)) if exclude_params else '0'
                query_intro = f"""
                    SELECT * FROM questions
                    WHERE topic = 'Introduction'
                    AND id NOT IN ({intro_placeholders})
                    ORDER BY RANDOM() LIMIT 1
                """
                question = conn.execute(query_intro, exclude_params).fetchone()

                if not question:
                    # All intro variants exhausted — pick any unseen Easy question as opener
                    logger.info("All intro variants seen. Using random Easy question as opener.")
                    query_intro_fallback = f"""
                        SELECT q.*, s.skill_name FROM questions q
                        JOIN skills s ON q.skill_id = s.id
                        WHERE q.id NOT IN ({intro_placeholders})
                        AND q.difficulty = 'Easy'
                        ORDER BY RANDOM() LIMIT 1
                    """
                    question = conn.execute(query_intro_fallback, exclude_params).fetchone()

            # 2. General Warm-up (Behavioral or Easy) — respects no-repeat pool
            if not question:
                query_warmup = f"""
                    SELECT DISTINCT q.*, s.skill_name
                    FROM questions q
                    JOIN skills s ON q.skill_id = s.id
                    WHERE q.id NOT IN ({placeholders})
                    AND (q.topic = 'Behavioral' OR q.difficulty = 'Easy')
                    ORDER BY RANDOM() LIMIT 1
                """
                question = conn.execute(query_warmup, exclude_params).fetchone()


        if not question:
            # Standard Fetch for Core/Advanced — uses global exclusion list
            query = f"""
                SELECT DISTINCT q.*, s.skill_name
                FROM questions q
                JOIN skills s ON q.skill_id = s.id
                WHERE q.id NOT IN ({placeholders})
                AND s.skill_name IN ({skill_placeholders})
                AND q.difficulty = ?
                -- SAFETY NET for Coding
                AND (q.question_type != 'coding' OR (q.test_cases IS NOT NULL AND length(q.test_cases) > 5))
                ORDER BY RANDOM() LIMIT 1
            """
            params = exclude_params + list(skills) + [target_difficulty]
            question = conn.execute(query, params).fetchone()

        # Fallback 1: Any Medium question if specific difficulty not found (global exclusion)
        if not question and target_difficulty != 'Medium':
            logger.warning(f"No {target_difficulty} question found. Falling back to Medium (Strict Skills).")
            query_fallback = f"""
               SELECT DISTINCT q.*, s.skill_name
               FROM questions q
               JOIN skills s ON q.skill_id = s.id
               WHERE q.id NOT IN ({placeholders})
               AND s.skill_name IN ({skill_placeholders})
               AND q.difficulty = 'Medium'
               ORDER BY RANDOM() LIMIT 1
            """
            params_kb = exclude_params + list(skills)
            question = conn.execute(query_fallback, params_kb).fetchone()

            if not question:
                logger.warning("No Medium question found. Falling back to Easy (Strict Skills).")
                query_fallback_easy = f"""
                   SELECT DISTINCT q.*, s.skill_name
                   FROM questions q
                   JOIN skills s ON q.skill_id = s.id
                   WHERE q.id NOT IN ({placeholders})
                   AND s.skill_name IN ({skill_placeholders})
                   AND q.difficulty = 'Easy'
                   ORDER BY RANDOM() LIMIT 1
                """
                question = conn.execute(query_fallback_easy, params_kb).fetchone()

        # Fallback 2: Pool exhausted globally — relax to session-only exclusion
        # This handles the rare case where a user has seen all questions for their skills
        if not question and len(excluded_ids) > len(answered_ids):
            logger.warning("Global question pool exhausted for user. Relaxing to session-only exclusion.")
            session_placeholders = ','.join('?' * len(answered_ids)) if answered_ids else '0'
            query_relaxed = f"""
               SELECT DISTINCT q.*, s.skill_name
               FROM questions q
               JOIN skills s ON q.skill_id = s.id
               WHERE q.id NOT IN ({session_placeholders})
               AND s.skill_name IN ({skill_placeholders})
               ORDER BY RANDOM() LIMIT 1
            """
            question = conn.execute(query_relaxed, list(answered_ids) + list(skills)).fetchone()

        # Fallback 3: ABSOLUTE EMERGENCY - General/Behavioral only
        if not question:
            logger.warning("Emergency Fallback: Fetching General/Behavioral question.")
            emg_placeholders = ','.join('?' * len(answered_ids)) if answered_ids else '0'
            query_any = f"""
               SELECT q.*, s.skill_name 
               FROM questions q
               JOIN skills s ON q.skill_id = s.id
               WHERE q.id NOT IN ({emg_placeholders}) 
               AND (s.skill_name = 'General' OR q.topic = 'Behavioral')
               LIMIT 1
            """
            question = conn.execute(query_any, list(answered_ids)).fetchone()
             
        conn.close()
        
        if question:
             # Override difficulty for display consistency in Warm-up
             q_dict = dict(question)
             if curr_stage == "Warm-up":
                 q_dict['difficulty'] = "Easy"
             
             return {
                 'question': q_dict,
                 'progress': {
                     'answered': count_answered,
                     'total': session_limit
                 }
             }
        return None
    
    except Exception as e:
        if 'conn' in locals(): conn.close()
        logger.error(f"Error in dynamic fetch: {str(e)}")
        return None

def submit_answer(session_id, question_id, user_answer):
    """
    Submit and evaluate user's answer
    
    Steps:
    1. Get question details
    2. Evaluate answer using keyword matching
    3. Save answer with score and feedback
    4. Update session total score
    5. Return evaluation results
    
    Args:
        session_id: ID of the interview session
        question_id: ID of the question being answered
        user_answer: User's text answer
        
    Returns:
        JSON response with score and feedback
    """
    try:
        # Get question
        question = get_question_by_id(question_id)
        if not question:
            return jsonify({'error': 'Question not found'}), 404
        
        # Evaluate answer
        expected_keywords = question['expected_keywords']
        # Fix: sqlite3.Row might not support .get(), convert to dict first
        q_dict = dict(question)
        question_type = q_dict.get('question_type', 'text')
        test_cases_json = q_dict.get('test_cases')
        answer_variants_json = q_dict.get('answer_variants')
        
        evaluation = evaluate_answer(
            user_answer, 
            expected_keywords, 
            question_type, 
            test_cases_json,
            answer_variants_json=answer_variants_json
        )
        
        # Save answer
        save_answer(
            session_id, 
            question_id, 
            user_answer, 
            evaluation['score'], 
            evaluation['feedback'],
            technical_score=evaluation.get('technical_score', evaluation.get('score', 0)),
            communication_score=evaluation.get('communication_score', evaluation.get('score', 0)),
            problem_solving_score=evaluation.get('problem_solving_score', evaluation.get('score', 0))
        )
        
        # Update session score
        update_session_score(session_id)

        # --- PERSONA FEEDBACK REMOVED ---
        # The new strict evaluator generates comprehensive feedback.
        final_feedback = evaluation.get('feedback', 'No feedback')

        return jsonify({
            'message': 'Answer submitted successfully',
            'score': evaluation.get('score', 0),
            'feedback': final_feedback,
            'matched_keywords': evaluation.get('matched_keywords', []),
            'total_keywords': evaluation.get('total_keywords', 0)
        }), 200
    
    except Exception as e:
        return jsonify({'error': f'Error submitting answer: {str(e)}'}), 500

def get_interview_results(session_id):
    """
    Get final interview results
    
    Steps:
    1. Mark session as completed
    2. Get all answers with scores
    3. Calculate final statistics
    4. Return comprehensive results
    
    Args:
        session_id: ID of the interview session
        
    Returns:
        JSON response with complete results
    """
    try:
        # Mark session as completed
        complete_session(session_id)
        
        # Get session results
        results = get_session_results(session_id)
        
        if not results['session']:
            return jsonify({'error': 'Session not found'}), 404
        
        # Calculate Skill Breakdown
        skill_map = {}
        for ans in results['answers']:
            skill = ans['skill_name']
            if skill not in skill_map:
                skill_map[skill] = {'total': 0, 'count': 0}
            skill_map[skill]['total'] += ans['score']
            skill_map[skill]['count'] += 1
            
        skill_breakdown = []
        for skill, data in skill_map.items():
            skill_breakdown.append({
                'skill': skill,
                'score': round(data['total'] / data['count'], 1)
            })
            
        return jsonify({
            'message': 'Interview completed',
            'session': results['session'],
            'answers': results['answers'],
            'total_score': results['session']['total_score'],
            'total_questions': results['session']['total_questions'],
            'skill_breakdown': skill_breakdown
        }), 200
    
    except Exception as e:
        return jsonify({'error': f'Error getting results: {str(e)}'}), 500

def get_history(user_id):
    """
    Get user's interview history
    
    Args:
        user_id: ID of the user
        
    Returns:
        JSON response with all past sessions
    """
    try:
        history = get_user_history(user_id)
        
        return jsonify({
            'message': 'History retrieved successfully',
            'sessions': history
        }), 200
    
    except Exception as e:
        return jsonify({'error': f'Error getting history: {str(e)}'}), 500
