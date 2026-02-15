import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))

# Generate a secure secret key from environment or use a strong default
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production-12345')
DATABASE_PATH = os.path.join(BASE_DIR, '../database/interview.db')

# Upload configuration
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
ALLOWED_EXTENSIONS = {'pdf'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
