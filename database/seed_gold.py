import sqlite3
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'interview.db')

def seed_gold():
    print("Seeding Gold Content...")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # helper to get skill id
    def get_skill_id(name):
        res = cur.execute("SELECT id FROM skills WHERE skill_name LIKE ?", (f'%{name}%',)).fetchone()
        return res[0] if res else 1 # Default to 1 (General/Python usually)

    py_id = get_skill_id('Python')
    dsa_id = get_skill_id('Data Structures')
    beh_id = get_skill_id('Behavioral')
    
    # 1. PYTHON GOLD QUESTIONS
    # ---------------------------------------------------------
    questions = [
        # Q1: GIL
        {
            "skill_id": py_id,
            "text": "Explain the Global Interpreter Lock (GIL) in Python and its impact on multi-threading.",
            "diff": "Hard",
            "keywords": "mutex, thread, lock, cpython, cpu-bound, io-bound, single thread",
            "type": "text",
            "variants": [
                {"variant_name": "Mechanism", "keywords": "mutex, reference counting, memory safety, thread-safe, bytecode, serialization"},
                {"variant_name": "Impact", "keywords": "cpu-bound, performance bottleneck, io-bound, concurrency, multiprocessing, parallelism"}
            ]
        },
        # Q2: Decorators
        {
            "skill_id": py_id,
            "text": "What is a Python decorator and how does it work under the hood?",
            "diff": "Medium",
            "keywords": "higher-order function, wrapper, closure, @ symbol, syntactic sugar, meta-programming",
            "type": "text",
            "variants": [
                {"variant_name": "Functional", "keywords": "function as argument, return function, closure, inner function, wrapper"},
                {"variant_name": "Implementation", "keywords": "__call__, dunder, class decorator, functools.wraps, introspection"}
            ]
        },
        # Q3: List vs Tuple
        {
            "skill_id": py_id,
            "text": "What are the key differences between a List and a Tuple in Python?",
            "diff": "Easy",
            "keywords": "mutable, immutable, syntax, performance, memory, hashing, dictionary key",
            "type": "text",
            "variants": [
                {"variant_name": "Properties", "keywords": "mutable, immutable, changed, static, dynamic, brackets, parentheses"},
                {"variant_name": "Usage", "keywords": "dictionary key, hashing, memory footprint, iteration speed, semantic difference"}
            ]
        },
        # Q4: Memory Management
        {
            "skill_id": py_id,
            "text": "How does Python manage memory?",
            "diff": "Hard",
            "keywords": "heap, garbage collection, reference counting, cycle, cyclic garbage collector, generations",
            "type": "text",
            "variants": [
                {"variant_name": "Core Mechanism", "keywords": "reference counting, ob_refcnt, deallocation, zero reference"},
                {"variant_name": "Garbage Collector", "keywords": "cyclic gc, generations, threshold, collect(), memory leak, weakref"}
            ]
        }
    ]
    
    # 2. DSA GOLD QUESTIONS (Mixed Text & Coding)
    # ---------------------------------------------------------
    questions.extend([
        # Q5: Valid Parentheses (Coding)
        {
            "skill_id": dsa_id,
            "text": "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
            "diff": "Medium",
            "keywords": "stack, push, pop, match, unbalanced, lifo",
            "type": "coding",
            "test_cases": '[{"input": "()", "output": true}, {"input": "()[]{}", "output": true}, {"input": "(]", "output": false}, {"input": "([)]", "output": false}]',
            "variants": []
        },
        # Q6: Two Sum (Coding)
        {
            "skill_id": dsa_id,
            "text": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
            "diff": "Medium",
            "keywords": "hash map, dictionary, complement, linear time, brute force",
            "type": "coding",
            "test_cases": '[{"input": [[2,7,11,15], 9], "output": [0,1]}, {"input": [[3,2,4], 6], "output": [1,2]}, {"input": [[3,3], 6], "output": [0,1]}]',
            "variants": []
        },
        # Q7: Array vs Linked List (Text)
        {
            "skill_id": dsa_id,
            "text": "Compare Array and Linked List data structures.",
            "diff": "Easy",
            "keywords": "contiguous, memory, cache, insertion, deletion, random access, pointer, overhead",
            "type": "text",
            "variants": [
                {"variant_name": "Performance", "keywords": "O(1) access, O(n) search, cache locality, insertion O(1), random access"},
                {"variant_name": "Structure", "keywords": "contiguous memory, dynamic size, node, pointer, reference, memory overhead"}
            ]
        }
    ])
    
    # 3. BEHAVIORAL GOLD QUESTIONS
    # ---------------------------------------------------------
    questions.extend([
        # Q8: Conflict
        {
            "skill_id": beh_id,
            "text": "Tell me about a time you had a conflict with a team member. How did you handle it?",
            "diff": "Medium",
            "keywords": "star method, communication, listen, perspective, compromise, resolution, professional",
            "type": "text",
            "variants": [
                {"variant_name": "Resolution Focus", "keywords": "calm, private discussion, root cause, common goal, data-driven"},
                {"variant_name": "Learning Focus", "keywords": "empathy, active listening, feedback, improvement, retrospective, team dynamic"}
            ]
        },
        # Q9: Weakness
        {
            "skill_id": beh_id,
            "text": "What is your greatest weakness?",
            "diff": "Easy",
            "keywords": "self-awareness, improvement, actionable, honest, skill, learning",
            "type": "text",
            "variants": [
                {"variant_name": "Growth Mindset", "keywords": "public speaking, delegation, perfectionism, detail-oriented, time management, active improvement"},
                {"variant_name": "Strategy", "keywords": "steps taken, progress, mentorship, tools used, ongoing effort"}
            ]
        }
    ])

    print(f"Prepared {len(questions)} Gold Questions.")
    
    count = 0
    for q in questions:
        # Check duplicate
        exists = cur.execute("SELECT id FROM questions WHERE question_text = ?", (q['text'],)).fetchone()
        if exists:
            continue
            
        variants_json = json.dumps(q['variants']) if q['variants'] else None
        
        cur.execute("""
            INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords, question_type, test_cases, answer_variants)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (q['skill_id'], q['text'], q['diff'], q['keywords'], q['type'], q.get('test_cases'), variants_json))
        count += 1
        
    conn.commit()
    conn.close()
    print(f"Successfully inserted {count} new Gold questions.")

if __name__ == "__main__":
    seed_gold()
