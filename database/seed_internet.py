import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))
from database import get_db_connection

INTERNET_QUESTIONS = [
    # --- MACHINE LEARNING (Source: Medium, 2025 Trend) ---
    ("Explain the architecture of Transformer models. How does the 'Attention Mechanism' solve the vanishing gradient problem in RNNs?", "Machine Learning", "Hard", "attention,encoder,decoder,parallelization,long-range dependencies", "text"),
    ("What is the 'Bias-Variance Tradeoff'? How does it relate to Overfitting and Underfitting in Deep Learning?", "Machine Learning", "Medium", "bias,variance,regularization,complexity,generalization", "text"),
    ("Explain the difference between Batch Normalization and Layer Normalization. When would you use one over the other?", "Machine Learning", "Hard", "normalization,batch size,rnn,training stability,covariate shift", "text"),
    ("Define 'Data Drift' and 'Concept Drift'. How do you monitor for these in a production MLOps pipeline?", "Machine Learning", "Hard", "distribution change,monitoring,model performance,training-serving skew", "text"),
    
    # --- PYTHON ---
    ("How does the 'Global Interpreter Lock' (GIL) in Python affect multi-threaded applications? How do you bypass it?", "Python", "Hard", "gil,multiprocessing,concurrency,cpu-bound,io-bound", "text"),
    ("Explain the difference between @staticmethod and @classmethod in Python. usage examples?", "Python", "Medium", "static,class,instance,decorator,inheritance", "text"),
    ("What are Python generators and how do they differ from iterators regarding memory usage?", "Python", "Medium", "yield,memory efficiency,lazy evaluation,iterator protocol", "text"),
    
    # --- SYSTEM DESIGN (Source: Toptal, Eduactive) ---
    ("Design a scalable Rate Limiter (like in an API Gateway). What algorithms would you use?", "System Design", "Hard", "token bucket,leaky bucket,redis,distributed,concurrency", "text"),
    ("How would you design a distributed Key-Value store like DynamoDB? Discuss Consistency vs Availability (CAP Theorem).", "System Design", "Hard", "hashing,replication,cap theorem,partitions,quorum", "text"),
    ("We need to design a Notification Service that sends 1M+ emails/sms per hour. How do you handle failures and retries?", "System Design", "Hard", "queue,dead letter queue,idempotency,worker,async", "text"),
    ("Design a URL Shortener like Bit.ly. How do you generate unique IDs at scale?", "System Design", "Hard", "base62,hashing,database,collisions,zookeeper", "text"),
    ("How do you handle 'Hot Partitions' in a distributed database system?", "System Design", "Hard", "sharding,consistent hashing,salt,load balancing", "text"),

    # --- BEHAVIORAL (Source: Amazon STAR Method) ---
    ("Tell me about a time you had to make a decision without having all the data. What was the outcome?", "Behavioral", "Medium", "risk,ambiguity,decision making,intuition,outcome", "text"),
    ("Describe a situation where you had to push back against a manager's or senior engineer's request. How did you handle it?", "Behavioral", "Medium", "disagreement,respect,data-driven,compromise,backbone", "text"),
    ("Tell me about a time you failed to meet a deadline. How did you communicate this to stakeholders?", "Behavioral", "Medium", "communication,proactive,ownership,mitigation,trust", "text"),
    ("Describe a complex problem you solved with a simple solution. Why was simplicity important there?", "Behavioral", "Medium", "simplicity,maintainability,complexity,cost,efficiency", "text"),
    ("Give me an example of a time you received constructive criticism. How did you react?", "Behavioral", "Medium", "feedback,growth,listening,improvement,maturity", "text"),
    
    # --- FRONTEND (React/JS) ---
    ("Explain the concept of 'Hoisting' in JavaScript. How does let/const differ from var?", "JavaScript", "Medium", "scope,declaration,initialization,temporal dead zone", "text"),
    ("What is the Virtual DOM in React and how does it improve performance?", "React", "Medium", "diffing,reconciliation,batching,memory,render", "text"),
    ("Explain 'Prop Drilling' in React. How can you avoid it?", "React", "Medium", "context api,redux,state management,component composition", "text"),
    ("What is the difference between 'Event Bubbling' and 'Event Capturing' in the DOM?", "JavaScript", "Hard", "propagation,listeners,target,capture,bubble", "text"),

    # --- BACKEND / DEVOPS ---
    ("What is the difference between SQL and NoSQL databases? When would you choose one over the other?", "SQL", "Medium", "schema,scaling,acid,join,flexibility", "text"),
    ("Explain the concept of 'Containerization' (Docker). How does it differ from Virtualization?", "DevOps", "Medium", "os kernel,lightweight,isolation,images,portability", "text"),
    ("What happens when you type a URL into a browser and hit Enter? Walk through the DNS to Render process.", "General", "Hard", "dns,tcp,handshake,http,parsing,rendering", "text"),
    
    # --- REQUIRED ---
    ("Tell me about yourself. Walk me through your background and your relevant experience.", "Behavioral", "Easy", "experience,background,projects,skills,education", "text")
]

def seed_internet_questions():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    print("Seeding INTERNET trending questions...")
    
    # helper to get or create skill
    def get_skill_id(skill_name):
        res = cursor.execute("SELECT id FROM skills WHERE skill_name = ?", (skill_name,)).fetchone()
        if res:
            return res[0]
        # create if not exists
        cursor.execute("INSERT INTO skills (skill_name, keywords) VALUES (?, ?)", (skill_name, skill_name.lower()))
        return cursor.lastrowid

    count = 0
    for q_text, skill, diff, keys, q_type in INTERNET_QUESTIONS:
        # Check if exists
        exists = cursor.execute("SELECT id FROM questions WHERE question_text = ?", (q_text,)).fetchone()
        if exists:
            # OPTIONAL: Update keywords if existing is weak?
            continue
            
        skill_id = get_skill_id(skill)
        cursor.execute("""
            INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords, question_type)
            VALUES (?, ?, ?, ?, ?)
        """, (skill_id, q_text, diff, keys, q_type))
        count += 1
        
    conn.commit()
    conn.close()
    print(f"Successfully injected {count} TRENDING interview questions.")

if __name__ == "__main__":
    seed_internet_questions()
