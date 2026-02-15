import sqlite3
import os
import json

DB_PATH = 'interview.db'

def migrate():
    print("Connecting to database...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Add test_cases column
    try:
        print("Checking for test_cases column...")
        cursor.execute("ALTER TABLE questions ADD COLUMN test_cases TEXT")
        print("Added 'test_cases' column.")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("'test_cases' column already exists.")
        else:
            print(f"Error adding column: {e}")

    # 2. Add Seed Data with Test Cases
    print("Seeding coding questions with test cases...")
    
    # Test Cases (JSON strings)
    fib_tests = json.dumps([
        {"input": [0], "output": 0},
        {"input": [1], "output": 1},
        {"input": [5], "output": 5}, 
        {"input": [10], "output": 55} # 12th is 144, 10th is 55: 0,1,1,2,3,5,8,13,21,34,55
    ])
    
    palindrome_tests = json.dumps([
        {"input": ["racecar"], "output": True},
        {"input": ["hello"], "output": False},
        {"input": ["A man, a plan, a canal: Panama"], "output": True}
    ])
    
    # We'll use a parameterized query with subselect for skill_id
    # Note: We need to DELETE existing coding questions to update them easily without complex UPSERT logic for this script
    # OR we can just insert new ones. Let's delete old 'coding' ones to be clean.
    cursor.execute("DELETE FROM questions WHERE question_type = 'coding'")
    
    seed_queries = [
        (
            "Python", 
            'Write a Python function `fibonacci(n)` that returns the Nth Fibonacci number.', 
            'Medium', 
            'recursion,loop,fibonacci', 
            'coding',
            fib_tests
        ),
        (
            "Python", 
            'Write a function `is_palindrome(s)` to validate if a string is a valid palindrome (ignoring non-alphanumeric).', 
            'Easy', 
            'palindrome,filter,reverse', 
            'coding',
            palindrome_tests
        )
    ]

    for skill, text, diff, keys, qtype, tests in seed_queries:
        try:
            # Get Skill ID
            cursor.execute("SELECT id FROM skills WHERE skill_name = ?", (skill,))
            res = cursor.fetchone()
            if not res:
                print(f"Skill {skill} not found, skipping.")
                continue
            skill_id = res[0]
            
            cursor.execute("""
                INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords, question_type, test_cases)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (skill_id, text, diff, keys, qtype, tests))
            print(f"Inserted question: {text[:30]}...")
        except Exception as e:
            print(f"Error inserting question: {e}")
            
    conn.commit()
    print("Migration and seeding complete.")
    conn.close()

if __name__ == "__main__":
    if not os.path.exists(DB_PATH):
        # Fallback if running from a different dir
        if os.path.exists(os.path.join('database', 'interview.db')):
            DB_PATH = os.path.join('database', 'interview.db')
        elif os.path.exists(os.path.join('..', 'database', 'interview.db')):
             DB_PATH = os.path.join('..', 'database', 'interview.db')
    
    migrate()
