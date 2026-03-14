import sqlite3
import pandas as pd
import os

DB_PATH = r"c:\Users\sameer\OneDrive\Desktop\mock\database\interview.db"

def check_distribution():
    if not os.path.exists(DB_PATH):
        print(f"Error: DB not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    try:
        # List Tables
        print("\n--- Tables ---")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(tables)
        
        # Count by Difficulty
        print("\n--- Difficulty Distribution ---")
        df_diff = pd.read_sql_query("SELECT difficulty, COUNT(*) as count FROM questions GROUP BY difficulty", conn)
        print(df_diff)
        
        # Count by Topic (for Behavioral)
        print("\n--- Topic Distribution (Top 10) ---")
        df_topic = pd.read_sql_query("SELECT topic, COUNT(*) as count FROM questions GROUP BY topic ORDER BY count DESC LIMIT 10", conn)
        print(df_topic)
        
        # Check specific "Warm-up" candidates
        print("\n--- Warm-up Candidates (Difficulty='Easy' OR Topic='Behavioral') ---")
        warmup_count = pd.read_sql_query("SELECT COUNT(*) as count FROM questions WHERE difficulty='Easy' OR topic='Behavioral'", conn).iloc[0]['count']
        print(f"Total Warm-up Questions: {warmup_count}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    check_distribution()
