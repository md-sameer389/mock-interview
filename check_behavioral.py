import sqlite3
import pandas as pd

DB_PATH = r"c:\Users\sameer\OneDrive\Desktop\mock\database\interview.db"

def check_behavioral_difficulty():
    conn = sqlite3.connect(DB_PATH)
    try:
        print("--- Behavioral Questions Difficulty ---")
        df = pd.read_sql_query("SELECT difficulty, COUNT(*) as count FROM questions WHERE topic='Behavioral' GROUP BY difficulty", conn)
        print(df)
        
        print("\n--- Sample Behavioral Questions ---")
        df_sample = pd.read_sql_query("SELECT question_text, difficulty FROM questions WHERE topic='Behavioral' LIMIT 5", conn)
        print(df_sample)
        
    except Exception as e:
        print(e)
    finally:
        conn.close()

if __name__ == "__main__":
    check_behavioral_difficulty()
