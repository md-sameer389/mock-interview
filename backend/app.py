import os
import sys
import logging
from flask import Flask
from flask_cors import CORS

# Fix for Render imports
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from routes.auth_routes import auth_bp
from routes.resume_routes import resume_bp
from routes.interview_routes import interview_bp
from routes.admin_routes import admin_bp
from routes.student_routes import student_bp
from config import SECRET_KEY

# Handle paths relative to the root folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

app = Flask(__name__, 
            static_folder=os.path.join(ROOT_DIR, 'frontend'), 
            static_url_path='')
app.secret_key = SECRET_KEY

# Auto-initialize database if it doesn't exist
def init_db_if_missing():
    from config import DATABASE_PATH
    db_dir = os.path.dirname(DATABASE_PATH)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
    
    if not os.path.exists(DATABASE_PATH):
        print("Database not found. Initializing...")
        try:
            import sqlite3
            schema_path = os.path.join(ROOT_DIR, 'database', 'schema.sql')
            seed_path = os.path.join(ROOT_DIR, 'database', 'seed_questions.sql')
            
            conn = sqlite3.connect(DATABASE_PATH)
            with open(schema_path, 'r') as f:
                conn.executescript(f.read())
            
            if os.path.exists(seed_path):
                with open(seed_path, 'r') as f:
                    conn.executescript(f.read())
            
            conn.close()
            print("Database initialized successfully.")
        except Exception as e:
            print(f"Error initializing database: {e}")

# Run init check
init_db_if_missing()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Enable CORS for all routes/origins for development
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(auth_bp)
app.register_blueprint(resume_bp)
app.register_blueprint(interview_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(student_bp)

@app.route('/')
def home():
    # Serve index.html if it exists, else default message
    try:
        return app.send_static_file('index.html')
    except:
        return 'Mock Interview Platform Backend Running. Access /admin for dashboard.'

@app.route('/admin')
def admin_dashboard():
    return app.send_static_file('admin.html')

@app.route('/health')
def health_check():
    return {'status': 'healthy'}, 200

@app.errorhandler(404)
def not_found(error):
    return {'error': 'Endpoint not found'}, 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f'Internal server error: {str(error)}')
    return {'error': 'Internal server error'}, 500

if __name__=='__main__':
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
