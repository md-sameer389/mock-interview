import sqlite3
import os

def get_question_counts():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, '../database/interview.db')
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    
    query = """
    SELECT s.skill_name, COUNT(q.id) as question_count
    FROM skills s
    LEFT JOIN questions q ON s.id = q.skill_id
    GROUP BY s.skill_name
    ORDER BY question_count DESC;
    """
    
    try:
        results = conn.execute(query).fetchall()
        with open('final_counts.txt', 'w', encoding='utf-8') as f:
            f.write(f"{'Skill':<30} | {'Count':<5}\n")
            f.write("-" * 38 + "\n")
            total = 0
            for row in results:
                f.write(f"{row['skill_name']:<30} | {row['question_count']:<5}\n")
                total += row['question_count']
            f.write("-" * 38 + "\n")
            f.write(f"{'Total':<30} | {total:<5}\n")
        print("Report generated in final_counts.txt")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    get_question_counts()
