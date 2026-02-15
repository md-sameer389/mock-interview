import os
import logging
from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth_bp
from routes.resume_routes import resume_bp
from routes.interview_routes import interview_bp
from routes.admin_routes import admin_bp
from routes.student_routes import student_bp
from config import SECRET_KEY

app = Flask(__name__, static_folder='../frontend', static_url_path='')
app.secret_key = SECRET_KEY

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

@app.errorhandler(404)
def not_found(error):
    return {'error': 'Endpoint not found'}, 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f'Internal server error: {str(error)}')
    return {'error': 'Internal server error'}, 500

if __name__=='__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='127.0.0.1', port=5000)
