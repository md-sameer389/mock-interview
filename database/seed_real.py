import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))
from database import get_db_connection

REAL_QUESTIONS = [
    # --- SYSTEM DESIGN / SCALABILITY ---
    ("Design a URL shortening service like Bit.ly. Focus on the database schema and unique ID generation.", "System Design", "Hard", "hashing,database,collision,scaling,key-value", "text"),
    ("How would you design a real-time chat application (like WhatsApp)? Discuss WebSocket vs HTTP polling.", "System Design", "Hard", "websocket,real-time,latency,pub-sub,message queue", "text"),
    ("We have a monolithic app that is too slow. How would you approach breaking it into microservices?", "System Design", "Hard", "microservices,decoupling,api gateway,latency,database per service", "text"),
    
    # --- PRACTICAL CODING / DEBUGGING ---
    ("You push code to production and it immediately spikes the CPU to 100%. What are your first 3 steps?", "DevOps", "Medium", "rollback,logs,monitor,profiling,revert", "text"),
    ("Explain the difference between vertical scaling and horizontal scaling. When would you use one over the other?", "System Design", "Medium", "load balancer,cost,database,complexity", "text"),
    ("Your database query is taking 10 seconds. How do you optimize it?", "Database", "Medium", "indexing,explain plan,caching,query optimization,normalization", "text"),
    
    # --- BEHAVIORAL ---
    ("Tell me about a time you had to deliver a feature with incomplete requirements. How did you proceed?", "Behavioral", "Medium", "communication,clarification,assumptions,feedback,agile", "text"),
    ("Describe a technical bug that was extremely hard to track down. What was the root cause?", "Behavioral", "Medium", "debugging,logs,reproducibility,root cause analysis", "text"),
    
    # --- PYTHON / DATA STRUCTURES (Practical) ---
    ("Implement a function to detect a cycle in a linked list.", "Python", "Medium", "fast slow pointers,hashing,visited set", "coding"),
    ("Explain how Python handles memory management. What is reference counting?", "Python", "Hard", "garbage collection,reference counting,memory leak,heap", "text")
]

def seed_real_questions():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    print("Seeding REAL world questions...")
    
    # helper to get or create skill
    def get_skill_id(skill_name):
        res = cursor.execute("SELECT id FROM skills WHERE skill_name = ?", (skill_name,)).fetchone()
        if res:
            return res[0]
        # create if not exists
        cursor.execute("INSERT INTO skills (skill_name, keywords) VALUES (?, ?)", (skill_name, skill_name.lower()))
        return cursor.lastrowid

    count = 0
    for q_text, skill, diff, keys, q_type in REAL_QUESTIONS:
        # Check if exists
        exists = cursor.execute("SELECT id FROM questions WHERE question_text = ?", (q_text,)).fetchone()
        if exists:
            continue
            
        skill_id = get_skill_id(skill)
        cursor.execute("""
            INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords, question_type)
            VALUES (?, ?, ?, ?, ?)
        """, (skill_id, q_text, diff, keys, q_type))
        count += 1
        
    conn.commit()
    conn.close()
    print(f"Successfully added {count} new high-quality questions.")

if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))
    from database import get_db_connection
    seed_real_questions()
