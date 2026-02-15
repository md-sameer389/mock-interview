from flask import Blueprint, request, jsonify
from services.interview_service import (
    start_interview, get_next_question, submit_answer,
    get_interview_results, get_history
)

interview_bp = Blueprint("interview", __name__, url_prefix="/interview")

from services.auth_service import token_required

@interview_bp.route("/start", methods=["POST"])
@token_required
def start(current_user_id):
    """
    Start a new interview session
    Expects JSON: { resume_id } (user_id from token)
    """
    try:
        data = request.json
        if not data or 'resume_id' not in data:
            return jsonify({'error': 'Resume ID is required'}), 400
        
        user_id = current_user_id
        resume_id = data.get('resume_id')
        persona = data.get('persona', 'standard')
        
        # Validate persona
        valid_personas = ['standard', 'technical', 'hr']
        if persona not in valid_personas:
            return jsonify({'error': f'Invalid persona. Choose from: {", ".join(valid_personas)}'}), 400
        
        return start_interview(user_id, resume_id, persona)
    
    except Exception as e:
        return jsonify({'error': 'Error starting interview. Please try again.'}), 500

@interview_bp.route("/next-question", methods=["POST"])
@token_required
def next_question(current_user_id):
    """
    Get next unanswered question dynamically
    Expects JSON: { session_id }
    """
    try:
        data = request.json
        if not data or 'session_id' not in data:
            return jsonify({'error': 'Session ID is required'}), 400
        
        session_id = data.get('session_id')
        
        # Verify session belongs to current_user_id for security
        from models.session_model import get_session_by_id
        session = get_session_by_id(session_id)
        if not session or session['user_id'] != current_user_id:
            return jsonify({'error': 'Unauthorized access to this session'}), 403
        
        question = get_next_question(session_id)
        
        if question:
            return jsonify({
                'message': 'Next question retrieved',
                'question': question
            }), 200
        else:
            return jsonify({
                'message': 'All questions answered',
                'question': None
            }), 200
    
    except Exception as e:
        import traceback
        logger.error(f"Error getting next question: {traceback.format_exc()}")
        return jsonify({'error': 'Error getting next question. Please try again.'}), 500

@interview_bp.route("/submit-answer", methods=["POST"])
@token_required
def submit(current_user_id):
    """
    Submit answer for evaluation
    Expects JSON: { session_id, question_id, user_answer }
    """
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Request body is required'}), 400
        
        session_id = data.get('session_id')
        question_id = data.get('question_id')
        user_answer = data.get('user_answer')
        
        if not session_id or not question_id or not user_answer:
            return jsonify({'error': 'Session ID, Question ID, and Answer are required'}), 400
        
        if not isinstance(user_answer, str) or len(user_answer.strip()) == 0:
            return jsonify({'error': 'Answer cannot be empty'}), 400
        
        # Verify session belongs to current_user_id for security
        from models.session_model import get_session_by_id
        session = get_session_by_id(session_id)
        if not session or session['user_id'] != current_user_id:
            return jsonify({'error': 'Unauthorized access to this session'}), 403
        
        return submit_answer(session_id, question_id, user_answer)
    
    except Exception as e:
        return jsonify({'error': 'Error submitting answer. Please try again.'}), 500

@interview_bp.route("/results/<int:session_id>", methods=["GET"])
@interview_bp.route("/results/<int:session_id>", methods=["GET"])
def results(session_id):
    """
    Get interview results
    """
    try:
        return get_interview_results(session_id)
    
    except Exception as e:
        return jsonify({'error': f'Error getting results: {str(e)}'}), 500

@interview_bp.route("/history", methods=["GET"])
@token_required
def history(current_user_id):
    """
    Get current user's interview history
    """
    try:
        return get_history(current_user_id)
    
    except Exception as e:
        return jsonify({'error': f'Error getting history: {str(e)}'}), 500
