import sqlite3
import os

DATABASE_PATH = 'database/interview.db'
if not os.path.exists(DATABASE_PATH):
    # Handle running from root or other dirs
    if os.path.exists('interview.db'):
        DATABASE_PATH = 'interview.db'
    elif os.path.exists('../database/interview.db'):
        DATABASE_PATH = '../database/interview.db'

def migrate_premium_features():
    print(f"Connecting to database at {DATABASE_PATH}...")
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    columns_to_add = [
        ("topic", "TEXT", "General"),
        ("companies", "TEXT", "[]"), # JSON list
        ("hints", "TEXT", "[]"),     # JSON list
        ("explanation", "TEXT", ""),
        ("difficulty_numeric", "INTEGER", 1),
        ("times_asked", "INTEGER", 0),
        ("avg_score", "REAL", 0.0)
    ]

    print("Checking for missing columns...")
    cursor.execute("PRAGMA table_info(questions)")
    existing_columns = [col[1] for col in cursor.fetchall()]

    for col_name, col_type, default_val in columns_to_add:
        if col_name not in existing_columns:
            try:
                print(f"Adding column '{col_name}'...")
                # SQLite doesn't support adding multiple columns in one statement reliably across versions
                # defaulting text fields to empty string or empty json list
                if col_type == "TEXT":
                    cursor.execute(f"ALTER TABLE questions ADD COLUMN {col_name} {col_type} DEFAULT '{default_val}'")
                else:
                    cursor.execute(f"ALTER TABLE questions ADD COLUMN {col_name} {col_type} DEFAULT {default_val}")
            except Exception as e:
                print(f"Error adding {col_name}: {e}")
        else:
            print(f"Column '{col_name}' already exists.")

    conn.commit()
    conn.close()
    print("Migration completed.")

if __name__ == "__main__":
    migrate_premium_features()
