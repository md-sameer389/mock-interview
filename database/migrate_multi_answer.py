import sqlite3
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'interview.db')

def migrate():
    print("Beginning migration for Multi-Answer Support...")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # 1. Add Column if not exists
    try:
        cur.execute("ALTER TABLE questions ADD COLUMN answer_variants TEXT")
        print("Added 'answer_variants' column.")
    except sqlite3.OperationalError:
        print("'answer_variants' column likely already exists. Skipping add.")
        
    # 2. Seed Example Data: SQL vs NoSQL (The user's complaint)
    # Variant A: Structure Emphasis (Schema, Relational)
    # Variant B: Scaling Emphasis (Vertical vs Horizontal, CAP Theorem)
    
    variants_sql = [
        {
            "variant_name": "Structure Focus",
            "keywords": "relational, schema, table, row, column, structured query language, fixed schema, predefined"
        },
        {
            "variant_name": "Scalability Focus",
            "keywords": "vertical scaling, horizontal scaling, acid, cap theorem, consistency, availability, partition tolerance, distributed"
        },
        {
            "variant_name": "Use-Case Focus",
            "keywords": "transaction, complex query, analytics, hierarchical data, key-value, document store, graph, flexible"
        }
    ]
    
    variants_json = json.dumps(variants_sql)
    
    # Find the SQL vs NoSQL question (id might vary, so use LIKE)
    cur.execute("UPDATE questions SET answer_variants = ? WHERE question_text LIKE '%SQL%' AND question_text LIKE '%NoSQL%'", (variants_json,))
    
    if cur.rowcount > 0:
        print(f"Updated {cur.rowcount} question(s) with SQL variants.")
    else:
        print("Warning: Could not find 'SQL vs NoSQL' question to update.")
        
    conn.commit()
    conn.close()
    print("Migration Complete.")

if __name__ == "__main__":
    migrate()
