"""Add 5 intro question variants and tag existing intro question with topic='Introduction'."""
import sqlite3, os
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

INTRO_VARIANTS = [
    (11, "Walk me through your resume and highlight your key experiences.",
     'Easy', 'education,project,internship,skill,experience,role,highlight,achievement,background,journey', 'text', 'Introduction'),
    (11, "Can you give a brief introduction about yourself and what you are looking for?",
     'Easy', 'background,education,skills,goal,looking for,interest,role,apply,strength,career', 'text', 'Introduction'),
    (11, "Describe yourself in terms of your technical skills and career aspirations.",
     'Easy', 'technical,skill,language,framework,project,aspiration,goal,career,interest,strength', 'text', 'Introduction'),
    (11, "What is your background and what led you to apply for this position?",
     'Easy', 'background,education,project,skill,reason,apply,interest,led,journey,goal', 'text', 'Introduction'),
    (11, "Start by telling us a little about yourself — your education, skills, and what you enjoy working on.",
     'Easy', 'education,skill,enjoy,project,interest,background,passion,work,technology,career', 'text', 'Introduction'),
]

conn = sqlite3.connect(DB_PATH)
try:
    # Tag existing "Tell me about yourself" as Introduction topic
    updated = conn.execute("UPDATE questions SET topic='Introduction' WHERE question_text LIKE '%yourself%'").rowcount
    print(f"Tagged {updated} existing question(s) as Introduction topic")

    # Remove duplicates: don't insert if same question_text already exists
    existing = {row[0] for row in conn.execute("SELECT question_text FROM questions WHERE topic='Introduction'").fetchall()}

    inserted = 0
    for (sid, q, d, k, t, top) in INTRO_VARIANTS:
        if q not in existing:
            conn.execute(
                "INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords, question_type, topic) VALUES (?,?,?,?,?,?)",
                (sid, q, d, k, t, top)
            )
            inserted += 1
        else:
            print(f"  Skipped (already exists): {q[:60]}")
    conn.commit()
    print(f"Inserted {inserted} new intro variants")

    # Show final list
    rows = conn.execute("SELECT id, question_text FROM questions WHERE topic='Introduction' ORDER BY id").fetchall()
    print(f"\nAll {len(rows)} intro question(s) (topic=Introduction):")
    for r in rows:
        print(f"  [{r[0]}] {r[1][:80]}")
except Exception as e:
    conn.rollback()
    import traceback; traceback.print_exc()
finally:
    conn.close()
