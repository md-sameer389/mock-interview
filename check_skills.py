
import sqlite3
import os

db_path = os.path.join('database', 'interview.db')
conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row
rows = conn.execute("SELECT * FROM skills").fetchall()
for row in rows:
    print(f"ID: {row['id']} | Name: {row['skill_name']} | Keywords: {row['keywords']}")
conn.close()
