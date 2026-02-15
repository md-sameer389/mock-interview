import os
import logging
from flask import jsonify
from werkzeug.utils import secure_filename
from models.resume_model import save_resume, get_resume_by_user
from utils.pdf_parser import extract_text_from_pdf
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS, MAX_FILE_SIZE

logger = logging.getLogger(__name__)

def allowed_file(filename):
    """
    Check if file extension is allowed
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_and_parse_resume(user_id, file):
    """
    Handle resume upload, extract text, and save to database
    
    Steps:
    1. Validate file type and size
    2. Save file to upload folder
    3. Extract text from PDF
    4. Save resume data to database
    5. Return resume ID and extracted text
    
    Args:
        user_id: ID of the user uploading resume
        file: File object from request
        
    Returns:
        JSON response with resume_id and extracted_text
    """
    try:
        # Validate file
        if not file or file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Only PDF files are allowed'}), 400
        
        # Check file size
        file.seek(0, 2)  # Seek to end
        file_size = file.tell()
        file.seek(0)  # Reset to start
        
        if file_size > MAX_FILE_SIZE:
            return jsonify({'error': f'File size exceeds {MAX_FILE_SIZE / (1024*1024):.1f}MB limit'}), 413
        
        if file_size == 0:
            return jsonify({'error': 'File is empty'}), 400
        
        # Secure filename and save file
        filename = secure_filename(file.filename)
        if not filename:
            return jsonify({'error': 'Invalid filename'}), 400
        
        filepath = os.path.join(UPLOAD_FOLDER, f"{user_id}_{filename}")
        file.save(filepath)
        
        # Extract text from PDF
        try:
            extracted_text = extract_text_from_pdf(filepath)
        except Exception as e:
            logger.error(f"PDF extraction failed for user {user_id}: {str(e)}")
            return jsonify({'error': 'Failed to extract text from PDF. Please ensure it is a valid PDF.'}), 400
        
        if not extracted_text or len(extracted_text.strip()) == 0:
            return jsonify({'error': 'PDF appears to be empty or unreadable'}), 400
        
        # Save to database
        try:
            resume_id = save_resume(user_id, filename, extracted_text)
        except Exception as e:
            logger.error(f"Failed to save resume for user {user_id}: {str(e)}")
            return jsonify({'error': 'Failed to save resume. Please try again.'}), 500
        
        # Extract and Save Skills
        try:
            from utils.skill_extractor import extract_skills_from_text
            from models.resume_model import save_candidate_skills
            
            skills = extract_skills_from_text(extracted_text)
            if skills:
                save_candidate_skills(user_id, skills)
        except Exception as e:
            logger.warning(f"Failed to extract skills for user {user_id}: {str(e)}")
            # Don't fail the upload if skill extraction fails
        
        logger.info(f"Resume uploaded successfully for user {user_id}, resume_id: {resume_id}")
        
        return jsonify({
            'message': 'Resume uploaded successfully',
            'resume_id': resume_id,
            'skills_found': skills if 'skills' in locals() else [],
            'extracted_text': extracted_text[:500] + '...' if len(extracted_text) > 500 else extracted_text
        }), 200
    
    except Exception as e:
        logger.error(f"Unexpected error uploading resume for user {user_id}: {str(e)}")
        return jsonify({'error': 'Error processing resume. Please try again.'}), 500
