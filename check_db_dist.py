import sqlite3
import pandas as pd

def check_distribution():
    conn = sqlite3.connect('interview.db')
    try:
        # Count by Difficulty
        print("--- Difficulty Distribution ---")
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
        print(e)
    finally:
        conn.close()

if __name__ == "__main__":
    check_distribution()
