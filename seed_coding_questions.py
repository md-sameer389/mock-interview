import sqlite3
import os
import json

DB_PATH = os.path.join(os.path.dirname(__file__), 'database/interview.db')

def seed_coding():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("Seeding coding questions...")
    
    questions = [
        # OUTPUT GUESSING
        {
            'skill_id': 1, # Python
            'question_text': "What is the output of the following code?",
            'question_type': 'output_guess',
            'difficulty': 'Easy',
            'code_snippet': "x = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)",
            'expected_keywords': "[1, 2, 3, 4]", # Used as correct output
            'correct_output': "[1, 2, 3, 4]",
            'test_cases': None
        },
        {
            'skill_id': 1, # Python
            'question_text': "What does this code print?",
            'question_type': 'output_guess',
            'difficulty': 'Medium',
            'code_snippet': "print(type(lambda x: x+1))",
            'expected_keywords': "<class 'function'>",
            'correct_output': "<class 'function'>",
            'test_cases': None
        },
        # CODING CHALLENGES
        {
            'skill_id': 1, # Python
            'question_text': "Write a function 'is_palindrome(s)' that checks if a string is a palindrome.",
            'question_type': 'coding',
            'difficulty': 'medium',
            'expected_keywords': 'def,return,==,reverse',
            'code_snippet': "def is_palindrome(s):\n    # Write your code here\n    pass",
            'test_cases': json.dumps([
                {"input": ["racecar"], "output": True},
                {"input": ["hello"], "output": False},
                {"input": ["madam"], "output": True},
                {"input": ["step on no pets"], "output": True}
            ]),
            'correct_output': None
        },
        {
            'skill_id': 3, # Data Structures
            'question_text': "Implement a function 'factorial(n)' that returns the factorial of a number.",
            'question_type': 'coding',
            'difficulty': 'Easy',
            'expected_keywords': 'def,return,if,else,*',
            'code_snippet': "def factorial(n):\n    # Write your code here\n    pass",
            'test_cases': json.dumps([
                {"input": [5], "output": 120},
                {"input": [0], "output": 1},
                {"input": [3], "output": 6}
            ]),
            'correct_output': None
        }
    ]

    for q in questions:
        # Check if exists to avoid duplicates
        exists = cursor.execute("SELECT id FROM questions WHERE question_text = ?", (q['question_text'],)).fetchone()
        if not exists:
            # Capitalize difficulty to match CHECK constraint if any (Easy, Medium, Hard)
            diff = q['difficulty'].capitalize()
            cursor.execute("""
                INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords, question_type, code_snippet, test_cases, correct_output)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (q['skill_id'], q['question_text'], diff, q['expected_keywords'], q['question_type'], q['code_snippet'], q['test_cases'], q['correct_output']))
            print(f"Added: {q['question_text'][:30]}...")
        else:
            print(f"Skipped (exists): {q['question_text'][:30]}...")
            
    conn.commit()
    conn.close()
    print("Seeding complete.")

if __name__ == "__main__":
    seed_coding()
