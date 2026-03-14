import sqlite3
import pandas as pd

DB_PATH = r"c:\Users\sameer\OneDrive\Desktop\mock\database\interview.db"

def find_intro_question():
    conn = sqlite3.connect(DB_PATH)
    try:
        print("--- Searching for 'Introduce' ---")
        df = pd.read_sql_query("SELECT id, question_text, difficulty, topic FROM questions WHERE question_text LIKE '%introduce%' OR question_text LIKE '%tell me about yourself%'", conn)
        print(df)
        
    except Exception as e:
        print(e)
    finally:
        conn.close()

if __name__ == "__main__":
    find_intro_question()
