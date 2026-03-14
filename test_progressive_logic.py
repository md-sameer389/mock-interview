import sys
import os

# Add root directory to path
sys.path.append(os.getcwd())

from backend.models.question_model import get_questions_by_skills

print("Simulating Question Fetch for Skills: ['Python', 'SQL']")
questions = get_questions_by_skills(['Python', 'SQL'], limit=15)

print(f"\nTotal Questions Fetched: {len(questions)}")
print("-" * 60)
print(f"{'ID':<5} {'Diff':<10} {'Type':<10} {'Text (Truncated)'}")
print("-" * 60)

difficulty_counts = {"Easy": 0, "Medium": 0, "Hard": 0}

for q in questions:
    # q is a Row object, access by index or key if configured
    # Based on query: id, text, diff, type, skill, code
    q_id = q[0]
    text = q[1]
    diff = q[2]
    q_type = q[3]
    
    difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1
    
    print(f"{q_id:<5} {diff:<10} {q_type:<10} {text[:40]}...")

print("-" * 60)
print("Distribution:")
for d, c in difficulty_counts.items():
    print(f"{d}: {c}")

expected = {"Easy": 2, "Medium": 8, "Hard": 5}
print(f"\nExpected approx: {expected}")
