import sqlite3

conn = sqlite3.connect('database/interview.db')
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(questions)")
columns = cursor.fetchall()
with open('db_schema_utf8.txt', 'w', encoding='utf-8') as f:
    f.write(f"{'CID':<5} {'Name':<20} {'Type':<10} {'NotNull':<10} {'DfltVal':<10} {'PK':<5}\n")
    f.write("-" * 65 + "\n")
    for col in columns:
        f.write(f"{col[0]:<5} {col[1]:<20} {col[2]:<10} {col[3]:<10} {col[4]!s:<10} {col[5]:<5}\n")

print("Schema written to db_schema_utf8.txt")
conn.close()
