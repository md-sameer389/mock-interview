import logging
from flask import jsonify
from database import get_db_connection
from models.resume_model import get_resume_by_id
from models.question_model import get_questions_by_skills, get_question_by_id, create_dynamic_question
from models.session_model import (
    create_session, save_answer, update_session_score, 
    complete_session, get_session_results, get_user_history,
    get_answered_questions
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
        # For HR, we might focus on soft skills even if resume has technical skills
        dynamic_qs = generate_heuristic_questions(skills, count=3, persona=persona)
        created_dynamic_ids = []
        
        for dq in dynamic_qs:
            q_id = create_dynamic_question(
                dq['question_text'], 
                dq['skill_name'], 
                dq['difficulty'], 
                dq['expected_keywords'],
                dq['question_type']
            )
            if q_id:
                created_dynamic_ids.append(q_id)
                
        # 2. Get Standard Questions based on skills & persona
        # Reduce limit since we have dynamic ones now
        standard_limit = 7
        
        # PERSONA LOGIC FOR STANDARD QUESTIONS:
        # We need to filter standard questions.
        # Currently get_questions_by_skills returns ANY difficulty.
        # We could filter them here or update the model.
        # For simplicity, let's fetch more and filter in python.
        
        raw_standard_questions = get_questions_by_skills(skills, limit=15)
        
        filtered_standard_questions = []
        if persona == 'technical':
            # Prefer Hard/Medium (Exclude coding for now)
            filtered_standard_questions = [
                q for q in raw_standard_questions 
                if (q['difficulty'] in ['Hard', 'Medium']) and q['question_type'] != 'coding'
            ]
        elif persona == 'hr':
            # Prefer Behavioral if possible
            # STRICTLY EXCLUDE CODING
            filtered_standard_questions = [
                q for q in raw_standard_questions 
                if (q['difficulty'] == 'Easy' or q['skill_id'] == 1) and q['question_type'] != 'coding'
            ]
        else:
            # exclude coding
            filtered_standard_questions = [q for q in raw_standard_questions if q['question_type'] != 'coding'] 
 
        # Fallback if filtering removed too many
        # STRICTLY EXCLUDE CODING IN FALLBACK TOO
        if len(filtered_standard_questions) < 3:
             filtered_standard_questions = [q for q in raw_standard_questions if q['question_type'] != 'coding']

        # Cap it
        standard_questions = filtered_standard_questions[:standard_limit]
        
        if not standard_questions and not created_dynamic_ids:
             return jsonify({'error': 'No questions found for your skills'}), 404

        # Combine Questions
        final_questions_pool = []

        # 0. ALWAYS START WITH: Introduce Yourself
        # Check if it exists in DB, otherwise create dynamic/temporary one
        # Ideally, we create a dynamic one to ensure it has an ID for tracking answers.
        
        intro_q_id = create_dynamic_question(
            "Tell me about yourself. Walk me through your background and your relevant experience.",
            "Behavioral",
            "Easy",
            "experience,background,projects,skills,education",
            "text"
        )
        if intro_q_id:
            intro_q = get_question_by_id(intro_q_id)
            if intro_q:
                final_questions_pool.append(intro_q)

        # Add dynamic ones (high priority)
        for qid in created_dynamic_ids:
            q_obj = get_question_by_id(qid)
            if q_obj:
                final_questions_pool.append(q_obj)
        
        # Add standard ones
        final_questions_pool.extend(standard_questions)
        
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
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'Error starting interview: {str(e)}'}), 500

    except Exception as e:
        import traceback
        with open('traceback.txt', 'w') as f:
            traceback.print_exc(file=f)
        # Close connection if open? (Handled by context usually but good practice)
        if 'conn' in locals():
            conn.close()
        logger.error(f"Error in dynamic fetch: {str(e)}")
        return None

def get_next_question(session_id, current_skills=None):
    """
    Get the next unanswered question dynamically based on performance (Adaptive Difficulty)
    """
    try:
        # 1. Check Session Status
        conn = get_db_connection()
        session = conn.execute("SELECT * FROM interview_sessions WHERE id = ?", (session_id,)).fetchone()
        
        if not session:
            conn.close()
            return None
            
        # 2. Get Answered Question IDs
        answered_ids = get_answered_questions(session_id)
        
        # 3. Check if we've reached the limit
        if len(answered_ids) >= session['total_questions']:
            conn.close()
            return None # Interview Complete

        # --- FORCE FIRST QUESTION: INTRODUCE YOURSELF ---
        if len(answered_ids) == 0:
            # Try to find the specific "Introduce Yourself" question
            # We look for the text pattern or specific text we seeded
            intro_q = conn.execute(
                "SELECT * FROM questions WHERE question_text LIKE 'Tell me about yourself%' LIMIT 1"
            ).fetchone()
            
            if intro_q:
                # If found and not answered (obviously not answered if len is 0), return it
                logger.info(f"Forcing first question: {intro_q['id']}")
                conn.close()
                return dict(intro_q)
            else:
                 logger.warning("Introduce Yourself question not found in DB. Falling back to random.")

        # 4. Determine Current Performance (Adaptive Logic)
        # Calculate average score of answered questions
        avg_score_row = conn.execute(
            "SELECT AVG(score) as val FROM answers WHERE session_id = ?", 
            (session_id,)
        ).fetchone()
        current_avg = avg_score_row['val'] if avg_score_row['val'] is not None else 6.0 # Default to Medium start
        
        # 5. Select Target Difficulty
        target_difficulty = 'Medium'
        if current_avg >= 7.5:
            target_difficulty = 'Hard'
        elif current_avg <= 4.0:
            target_difficulty = 'Easy'
            
        # 6. Fetch a Random Unanswered Question matching Difficulty & Skills
        # Get resume to filter by skills (crucial fix)
        resume = get_resume_by_id(session['resume_id'])
        extracted_text = resume['extracted_text']
        skills = extract_skills_from_text(extracted_text)
        
        # Filter questions by these skills
        if not skills:
            skills = ['General'] # Fallback
            
        skill_placeholders = ','.join('?' * len(skills))
        
        # Prepare Answered IDs placeholder
        placeholders = ','.join('?' * len(answered_ids)) if answered_ids else '0'
        
        # Prioritize Coding questions if not yet asked? 
        # NO - User requested removal. Explicitly EXCLUDE coding.
        query = f"""
            SELECT DISTINCT q.*, s.skill_name
            FROM questions q
            JOIN skills s ON q.skill_id = s.id
            WHERE q.id NOT IN ({placeholders})
            AND s.skill_name IN ({skill_placeholders})
            AND q.difficulty = ?
            AND q.question_type != 'coding' -- Explicitly removed
            ORDER BY RANDOM()
            LIMIT 1
        """
        
        params = list(answered_ids) + list(skills) + [target_difficulty]
        
        logger.debug(f"Fetching question. Skills: {skills}, Difficulty: {target_difficulty}, Answered questions: {len(answered_ids)}")
        question = conn.execute(query, params).fetchone()
        
        if question:
            logger.debug(f"Found question: {question['id']} Type: {question['question_type']}")
        else:
            logger.debug("No question found with strict criteria. Trying fallback.")
 
        # Fallback 1: If no question of target difficulty, try Medium (but still filter by skills)
        if not question and target_difficulty != 'Medium':
            query_fallback = f"""
                SELECT DISTINCT q.*, s.skill_name
                FROM questions q
                JOIN skills s ON q.skill_id = s.id
                WHERE q.id NOT IN ({placeholders})
                AND s.skill_name IN ({skill_placeholders})
                AND q.question_type != 'coding' -- Explicitly removed
                ORDER BY RANDOM()
                LIMIT 1
            """
            params_fallback = list(answered_ids) + list(skills)
            question = conn.execute(query_fallback, params_fallback).fetchone()
            
        # Fallback 2: Any unanswered question (REMOVED)
        # We no longer fall back to random questions to ensure relevance to the resume.
        # If no question is found for the extracted skills, the interview naturally ends.
        
        conn.close()
        
        if question:
             return dict(question)
        return None
    
    except Exception as e:
        import traceback
        with open('traceback.txt', 'w') as f:
            traceback.print_exc(file=f)
        # Close connection if open? (Handled by context usually but good practice)
        if 'conn' in locals():
            conn.close()
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
            evaluation['feedback']
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
