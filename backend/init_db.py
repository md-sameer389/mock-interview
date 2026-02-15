import sqlite3
import os
from config import DATABASE_PATH

# Adjust path to schema based on execution directory
SCHEMA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database', 'schema.sql')

def init_db():
    print(f"Initializing database at {DATABASE_PATH}...")
    
    # Remove existing DB to ensure clean state
    if os.path.exists(DATABASE_PATH):
        try:
            os.remove(DATABASE_PATH)
            print("Removed existing database.")
        except Exception as e:
            print(f"Error removing DB: {e}")

    conn = sqlite3.connect(DATABASE_PATH)
    
    try:
        with open(SCHEMA_PATH, 'r') as f:
            schema = f.read()
            conn.executescript(schema)
        print("Schema applied successfully.")

        # Seed data
        SEED_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database', 'seed_questions.sql')
        if os.path.exists(SEED_PATH):
            with open(SEED_PATH, 'r') as f:
                seed = f.read()
                conn.executescript(seed)
            print("Database seeded successfully.")
        else:
            print("Warning: Seed file not found.")
    except Exception as e:
        print(f"Error applying schema: {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    init_db()
