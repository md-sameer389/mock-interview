from flask import Blueprint, jsonify, request
import logging
from services.student_service import get_student_stats, get_eligible_drives, get_student_history
from services.auth_service import token_required

logger = logging.getLogger(__name__)
student_bp = Blueprint("student", __name__, url_prefix="/student")

@student_bp.route("/dashboard-stats", methods=["GET"])
@token_required
def dashboard_stats(current_user_id):
    """
    Get stats for student dashboard
    """
    try:
        data = get_student_stats(current_user_id)
        return jsonify(data), 200
    except Exception as e:
        logger.error(f"Error getting dashboard stats for user {current_user_id}: {str(e)}")
        return jsonify({'error': 'Error loading dashboard statistics'}), 500

@student_bp.route("/drives", methods=["GET"])
@token_required
def drives(current_user_id):
    """
    Get eligible placement drives
    """
    try:
        data = get_eligible_drives(current_user_id)
        return jsonify(data), 200
    except Exception as e:
        logger.error(f"Error getting drives for user {current_user_id}: {str(e)}")
        return jsonify({'error': 'Error loading placement drives'}), 500

@student_bp.route("/history", methods=["GET"])
@token_required
def history(current_user_id):
    """
    Get own interview history
    """
    try:
        data = get_student_history(current_user_id)
        return jsonify(data), 200
    except Exception as e:
        logger.error(f"Error getting history for user {current_user_id}: {str(e)}")
        return jsonify({'error': 'Error loading interview history'}), 500
