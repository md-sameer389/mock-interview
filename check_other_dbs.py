import sqlite3
import pandas as pd
import os

DB_PATHS = [
    r"c:\Users\sameer\OneDrive\Desktop\mock\database\interview.db",
    r"c:\Users\sameer\OneDrive\Desktop\mock\interview.db"
]

def check_dbs():
    for path in DB_PATHS:
        print(f"\nChecking: {path}")
        if not os.path.exists(path):
            print("  Not found.")
            continue
            
        try:
            conn = sqlite3.connect(path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            print(f"  Tables: {[t[0] for t in tables]}")
            
            if ('questions',) in tables:
                count = pd.read_sql_query("SELECT COUNT(*) as count FROM questions", conn).iloc[0]['count']
                print(f"  Question Count: {count}")
                
            conn.close()
        except Exception as e:
            print(f"  Error: {e}")

if __name__ == "__main__":
    check_dbs()
