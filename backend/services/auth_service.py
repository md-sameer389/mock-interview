import jwt
import datetime
import bcrypt
from functools import wraps
from flask import request, jsonify
from config import SECRET_KEY
from database import get_db_connection

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(" ")[1]
        
        if not token:
            return jsonify({'error': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            current_user_id = data['user_id']
        except Exception as e:
            return jsonify({'error': 'Token is invalid!', 'details': str(e)}), 401
            
        return f(current_user_id, *args, **kwargs)
    
    return decorated
    
    return decorated

def register_user(full_name, email, password):
    # Validate inputs
    if not full_name or not email or not password:
        return {'error': 'Full name, email, and password are required'}, 400
    
    if len(password) < 6:
        return {'error': 'Password must be at least 6 characters'}, 400
    
    if not isinstance(email, str) or '@' not in email:
        return {'error': 'Invalid email format'}, 400
    
    conn = get_db_connection()
    try:
        # Check if user exists
        existing = conn.execute('SELECT id FROM users WHERE email = ?', (email,)).fetchone()
        if existing:
            return {'error': 'Email already registered'}, 409
            
        hashed = hash_password(password)
        cursor = conn.execute(
            'INSERT INTO users (full_name, email, password_hash, role) VALUES (?, ?, ?, ?)',
            (full_name, email, hashed, 'student')
        )
        conn.commit()
        
        user_id = cursor.lastrowid
        token = generate_token(user_id)
        
        return {
            'message': 'Registered successfully',
            'token': token,
            'user': {'id': user_id, 'name': full_name, 'email': email, 'role': 'student'}
        }, 201
    except Exception as e:
        return {'error': 'Registration failed. Please try again.'}, 500
    finally:
        conn.close()

def login_user(email, password):
    # Validate inputs
    if not email or not password:
        return {'error': 'Email and password are required'}, 400
    
    conn = get_db_connection()
    try:
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        
        if not user or not check_password(password, user['password_hash']):
            return {'error': 'Invalid email or password'}, 401
            
        token = generate_token(user['id'])
        
        # Determine role (default to student if null)
        role = user['role'] if 'role' in user.keys() and user['role'] else 'student'
        
        return {
            'message': 'Login successful',
            'token': token,
            'user': {'id': user['id'], 'name': user['full_name'], 'email': user['email'], 'role': role}
        }, 200
    except Exception as e:
        return {'error': 'Login failed. Please try again.'}, 500
    finally:
        conn.close()
