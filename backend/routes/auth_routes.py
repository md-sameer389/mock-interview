from flask import Blueprint, request, jsonify
from services.auth_service import register_user, login_user

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["POST"])
def register():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Request body is required'}), 400
        
        full_name = data.get('full_name')
        email = data.get('email')
        password = data.get('password')
        
        return register_user(full_name, email, password)
    except Exception as e:
        return jsonify({'error': 'Registration failed. Please try again.'}), 500

@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Request body is required'}), 400
        
        email = data.get('email')
        password = data.get('password')
        
        return login_user(email, password)
    except Exception as e:
        return jsonify({'error': 'Login failed. Please try again.'}), 500
