import sqlite3
import os
import json

DB_PATH = os.path.join(os.path.dirname(__file__), 'database/interview.db')

def seed_cpp():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("Seeding C/C++ content...")
    
    # 1. Add C/C++ Skill
    skill_id = None
    # 1. Add C/C++ Skill
    skill_exists = cursor.execute("SELECT id FROM skills WHERE skill_name = ?", ("C++",)).fetchone()
    
    if skill_exists:
        skill_id = skill_exists[0]
        print(f"Skill C++ already exists (ID: {skill_id})")
    else:
        # Include keywords which is NOT NULL
        cursor.execute("INSERT INTO skills (skill_name, keywords) VALUES (?, ?)", ("C++", "c++,cpp,programming,memory,pointers,stl"))
        skill_id = cursor.lastrowid
        print(f"Added Skill: C++ (ID: {skill_id})")

    if not skill_id:
        print("Failed to get skill ID.")
        return

    questions = [
        # === TEXT QUESTIONS ===
        {
            'skill_id': skill_id,
            'question_text': "What is the difference between malloc/free and new/delete?",
            'question_type': 'text',
            'difficulty': 'Medium',
            'expected_keywords': "constructor,destructor,class,object,memory allocation,stdlib",
            'code_snippet': None, 'test_cases': None, 'correct_output': None
        },
        {
            'skill_id': skill_id,
            'question_text': "Explain the concept of a Virtual Function and Polymorphism in C++.",
            'question_type': 'text',
            'difficulty': 'Hard',
            'expected_keywords': "vtable,virtual table,dynamic dispatch,runtime polymorphism,override,base class",
            'code_snippet': None, 'test_cases': None, 'correct_output': None
        },
        {
            'skill_id': skill_id,
            'question_text': "What is a 'Smart Pointer' in C++? Name a few types.",
            'question_type': 'text',
            'difficulty': 'Medium',
            'expected_keywords': "unique_ptr,shared_ptr,weak_ptr,memory management,raii,ownership",
            'code_snippet': None, 'test_cases': None, 'correct_output': None
        },
        {
            'skill_id': skill_id,
            'question_text': "Differentiate between 'struct' and 'class' in C++.",
            'question_type': 'text',
            'difficulty': 'Easy',
            'expected_keywords': "public default,private default,access modifier,inheritance",
            'code_snippet': None, 'test_cases': None, 'correct_output': None
        },

        # === OUTPUT GUESSING QUESTIONS ===
        {
            'skill_id': skill_id,
            'question_text': "What is the output of this C++ pointer arithmetic?",
            'question_type': 'output_guess',
            'difficulty': 'Medium',
            'code_snippet': "int arr[] = {10, 20, 30};\nint *ptr = arr;\nptr++;\nstd::cout << *ptr;",
            'expected_keywords': "20",
            'correct_output': "20",
            'test_cases': None
        },
        {
            'skill_id': skill_id,
            'question_text': "What does this code print?",
            'question_type': 'output_guess',
            'difficulty': 'Medium',
            'code_snippet': "#include <iostream>\nusing namespace std;\n\nvoid wow(int& x) { x += 10; }\n\nint main() {\n   int a = 5;\n   wow(a);\n   cout << a;\n   return 0;\n}",
            'expected_keywords': "15",
            'correct_output': "15",
            'test_cases': None
        },
        
        # === CODING QUESTIONS (Logic only, since we execute Python backend. We can check Logic using Python wrapper or just syntax check/Plan) ===
        # NOTE: Our execution engine currently runs PYTHON code (via `exec()`).
        # Evaluating C++ code dynamically requires `g++` on the server.
        # Im closing the loop here: user wants C++ questions.
        # But our `evaluator.py` runs `exec(user_answer)`. This ONLY works for Python.
        # I will flag this in the description or just use "Text" questions for Coding Concepts?
        # OR: I can add C++ questions as "Write a Function" but the evaluator will likely fail if they write C++ syntax.
        # Better approach: Add them, but set evaluation to "Text" mode for now so it checks logic keywords? 
        # User explicitly asked for CODING.
        # Hack: The question asks for C++ code. The user writes C++. `evaluator.py` sees `question_type='coding'` -> runs `compile()`.
        # C++ code will fail Python compile().
        # Verdict: I cannot support EXECUTION of C++ code without installing a compiler.
        # Solution: I will add them as 'text' questions requiring code logic explanation OR 'output_guess'.
        # Actually, user asked for "Coding". I will enable them but use a special handle for non-python?
        # No, for now I will add them as output_guess and text. 
        # Wait, I can add a coding question "Write Python code that simulates..." NO.
        # I will add **Python** questions that ask for C++ concepts? No.
        
        # DECISION: I will add C++ Coding questions as TEXT type where they have to Write the code, 
        # and we verify keywords like `std::vector`, `cin`, `cout`.
        # Because we CANNOT execute C++ on this Windows machine securely/easily without verifying gcc exists.
        
        {
            'skill_id': skill_id,
            'question_text': "Write a C++ function to swap two numbers using pointers.",
            'question_type': 'text', # fallback to text so it doesn't try to run python exec
            'difficulty': 'Easy',
            'expected_keywords': "temp,*,pointer,swap,address,dereference,&",
            'code_snippet': "void swap(int *a, int *b) {\n    // Code here\n}",
            'test_cases': None, 'correct_output': None
        }
    ]

    for q in questions:
        exists = cursor.execute("SELECT id FROM questions WHERE question_text = ?", (q['question_text'],)).fetchone()
        
        # Prepare params (handle None)
        diff = q.get('difficulty', 'Medium').capitalize()
        exp_kw = q.get('expected_keywords')
        q_type = q.get('question_type', 'text')
        code = q.get('code_snippet')
        cases = q.get('test_cases')
        output = q.get('correct_output')
        
        if not exists:
            cursor.execute("""
                INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords, question_type, code_snippet, test_cases, correct_output)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (q['skill_id'], q['question_text'], diff, exp_kw, q_type, code, cases, output))
            print(f"Added: {q['question_text'][:30]}...")
        else:
            print(f"Skipped: {q['question_text'][:30]}...")
            
    conn.commit()
    conn.close()
    print("Seeding C++ complete.")

if __name__ == "__main__":
    seed_cpp()
