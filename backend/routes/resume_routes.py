from flask import Blueprint, request, jsonify
from services.resume_service import upload_and_parse_resume
from services.auth_service import token_required

resume_bp = Blueprint("resume", __name__, url_prefix="/resume")

@resume_bp.route("/upload", methods=["POST"])
@token_required
def upload(current_user_id):
    """
    Upload and parse resume
    Expects: user_id (implicitly attributes to token owner), file (multipart/form-data)
    """
    try:
        # User ID comes from token now
        user_id = current_user_id
        
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        return upload_and_parse_resume(user_id, file)
    
    except Exception as e:
        return jsonify({'error': f'Error uploading resume: {str(e)}'}), 500
