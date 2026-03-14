import sqlite3
import json
import os

DATABASE_PATH = 'database/interview.db'
if not os.path.exists(DATABASE_PATH):
    if os.path.exists('interview.db'):
        DATABASE_PATH = 'interview.db'
    elif os.path.exists('../database/interview.db'):
        DATABASE_PATH = '../database/interview.db'

def seed_advanced_content():
    print(f"Seeding advanced content to {DATABASE_PATH}...")
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # 1. Update Existing Questions with Topics
    print("Updating existing questions with topics...")
    topic_map = {
        "array": "Arrays",
        "linked list": "Linked Lists",
        "tree": "Trees",
        "graph": "Graphs",
        "sort": "Sorting",
        "search": "Searching",
        "sql": "SQL",
        "nosql": "NoSQL",
        "thread": "Concurrency",
        "process": "OS Concepts",
        "http": "Protocols",
        "tcp": "Protocols",
        "inheritance": "OOP Concepts",
        "polymorphism": "OOP Concepts",
        "react": "Frontend Frameworks",
        "api": "API Design"
    }

    cursor.execute("SELECT id, question_text FROM questions")
    questions = cursor.fetchall()
    
    for q_id, text in questions:
        text_lower = text.lower()
        topic = "General"
        for key, val in topic_map.items():
            if key in text_lower:
                topic = val
                break
        
        # Also assign difficulty_numeric based on text difficulty
        # (This is a rough heuristic since we can't easily read the difficulty column without another query or join, 
        # but we can rely on existing default which is 1. Let's try to be smarter if we can)
        
        cursor.execute("UPDATE questions SET topic = ? WHERE id = ?", (topic, q_id))

    # Update numeric difficulty based on string difficulty
    cursor.execute("UPDATE questions SET difficulty_numeric = 3 WHERE difficulty = 'Easy'")
    cursor.execute("UPDATE questions SET difficulty_numeric = 6 WHERE difficulty = 'Medium'")
    cursor.execute("UPDATE questions SET difficulty_numeric = 9 WHERE difficulty = 'Hard'")

    # 2. Add Premium Questions (with hints, companies, etc)
    print("Adding Premium questions...")
    
    premium_questions = [
        {
            "skill_id": 3, # Data Structures
            "question_text": "Two Sum: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
            "difficulty": "Easy",
            "expected_keywords": "hash map, dictionary, complement, o(n), index, key value",
            "question_type": "coding",
            "topic": "Arrays",
            "companies": json.dumps(["Google", "Amazon", "Facebook", "Apple"]),
            "hints": json.dumps(["Brute force is O(n^2).", "Can you use a hash map to check for the complement in O(1)?"]),
            "explanation": "Use a hash map to store values and their indices. Iterate through the array, check if (target - num) exists in the map.",
            "difficulty_numeric": 3,
            "test_cases": json.dumps([{"input": "[2,7,11,15], 9", "output": "[0, 1]"}, {"input": "[3,2,4], 6", "output": "[1, 2]"}]),
            "code_snippet": "def two_sum(nums, target):\n    # Your code here\n    pass"
        },
        {
            "skill_id": 8, # OOP
            "question_text": "Design a Parking Lot system.",
            "difficulty": "Hard",
            "expected_keywords": "class, object, inheritance, vehicle, spot, ticket, payment, strategy pattern",
            "question_type": "text", # System Design is often text/draw based
            "topic": "System Design",
            "companies": json.dumps(["Amazon", "Microsoft", "Uber"]),
            "hints": json.dumps(["Identify core entities: Vehicle, Spot, Level, Ticket.", "Consider different vehicle types.", "How do you handle entry and exit?"]),
            "explanation": "Core classes: ParkingSpot (abstract), CompactSpot, LargeSpot. Vehicle (abstract), Car, Truck. ParkingLot (singleton).",
            "difficulty_numeric": 8
        },
        {
            "skill_id": 1, # Python
            "question_text": "Tell me about a time you failed. How did you handle it?",
            "difficulty": "Medium",
            "expected_keywords": "star method, situation, task, action, result, learning, growth, responsibility",
            "question_type": "behavioral",
            "topic": "Behavioral",
            "companies": json.dumps(["All"]),
            "hints": json.dumps(["Use the STAR method.", "Focus on what you learned.", "Don't blame others."]),
            "explanation": "Structure: S (Situation), T (Task), A (Action), R (Result). Emphasize the 'Action' and 'Result' and the lesson learned.",
            "difficulty_numeric": 5
        }
    ]

    for q in premium_questions:
        # Check if exists
        exists = cursor.execute("SELECT id FROM questions WHERE question_text = ?", (q["question_text"],)).fetchone()
        if not exists:
            cursor.execute("""
                INSERT INTO questions (
                    skill_id, question_text, difficulty, expected_keywords, question_type, 
                    topic, companies, hints, explanation, difficulty_numeric, test_cases, code_snippet
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                q["skill_id"], q["question_text"], q["difficulty"], q["expected_keywords"], q["question_type"],
                q["topic"], q["companies"], q["hints"], q["explanation"], q["difficulty_numeric"], 
                q.get("test_cases"), q.get("code_snippet")
            ))
            print(f"Added premium question: {q['question_text'][:30]}...")

    conn.commit()
    conn.close()
    print("Seeding completed.")

if __name__ == "__main__":
    seed_advanced_content()
