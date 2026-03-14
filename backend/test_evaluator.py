import sys
sys.path.insert(0, '.')
from utils.evaluator import evaluate_answer

tests = [
    # (label, user_answer, keywords, q_type, old_score, note)
    (
        "Q3 Set output",
        "{3} {1, 2, 3, 4, 5} {1, 2}",
        "set,2},intersection,1,2,3,4,5",
        "output",
        1.8,
        "CORRECT answer, must be near 10"
    ),
    (
        "Q5 2nd highest salary SQL",
        "SELECT MAX(salary) FROM Employee WHERE salary < ( SELECT MAX(salary) FROM Employee )",
        "row_number,limit,subquery",
        "logic",
        1.6,
        "Correct SQL approach using subquery"
    ),
    (
        "Q4 Polymorphism",
        "Polymorphism is an OOP concept where the same method can have different behaviors depending on context. Compile-time polymorphism uses method overloading. Run-time polymorphism uses method overriding, where a child class provides its own implementation.",
        "multiple forms,compile time,runtime",
        "text",
        3.5,
        "Correct answer, should be >6"
    ),
    (
        "Q1 Introduce yourself",
        "My name is Mohammed Samir, third-year BTech student with interest in software development and AI. I have experience in Python, HTML, CSS. Projects include e-commerce sales analysis, house price prediction using machine learning, and a Voice-Based AI Mock Interview Platform integrating RAG-based teaching assistants.",
        "education,background,skills,experience,interest,project,goal,brief,summary,introduce",
        "text",
        4.2,
        "Strong answer, education=BTech, background=experience"
    ),
    (
        "Q12 Overfitting",
        "The model is overfitting; it can be fixed by reducing model complexity, applying regularization, using more training data, and validating with cross validation on a separate test set.",
        "test,cross-validation,simple",
        "text",
        1.6,
        "Correct fix described, cross-validation mentioned"
    ),
    (
        "Q6 TCP vs UDP",
        "TCP is connection-oriented, reliable, used for HTTP, email, FTP. UDP is connectionless, faster, used for streaming, gaming, DNS — where speed matters more than reliability.",
        "speed,reliability,use case",
        "text",
        6.4,
        "Good answer, should stay similar or improve"
    ),
    (
        "Q13 Hash index",
        "A hash index is optimised for fast equality lookups using hashing, offering O(1) average lookup. B-tree is preferred for range queries. Use hash when only equality comparisons are needed.",
        "exact match,collision,o(1)",
        "text",
        4.2,
        "Correct — equality=exact match, O(1) mentioned"
    ),
]

print("=" * 70)
print(f"{'Question':<30} {'OLD':>5} {'NEW':>5} {'T':>5} {'C':>5}  Note")
print("=" * 70)
for label, ans, kw, qtype, old, note in tests:
    r = evaluate_answer(ans, kw, qtype)
    flag = "✅" if r['score'] > old else ("⚠️" if r['score'] >= old - 0.5 else "❌")
    print(f"{label:<30} {old:>5.1f} {r['score']:>5.1f} {r['technical_score']:>5.1f} {r['communication_score']:>5.1f}  {flag} {note}")
print("=" * 70)
