import sys
sys.path.insert(0, '.')
from utils.evaluator import evaluate_answer

tests = [
    ("Q3 Set output (was 1.8)", "{3} {1, 2, 3, 4, 5} {1, 2}", "set,2},intersection,1,2,3,4,5", "output", 1.8),
    ("Q5 2nd highest salary (was 1.6)", "SELECT MAX(salary) FROM Employee WHERE salary < ( SELECT MAX(salary) FROM Employee )", "row_number,limit,subquery", "logic", 1.6),
    ("Q4 Polymorphism (was 3.5)", "Polymorphism is an OOP concept where the same method can have different behaviors. Compile-time polymorphism uses method overloading. Run-time polymorphism uses method overriding.", "multiple forms,compile time,runtime", "text", 3.5),
    ("Q1 Myself BTech (was 4.2)", "My name is Mohammed Samir, third-year BTech student. Experience in Python, HTML, CSS. Projects include e-commerce sales analysis, house price prediction using machine learning, Voice-Based AI Mock Interview Platform.", "education,background,skills,experience,interest,project,goal,brief,summary,introduce", "text", 4.2),
    ("Q12 Overfitting (was 1.6)", "The model is overfitting; fix by reducing complexity, applying regularization, more training data, and validating with cross validation on a separate test set.", "test,cross-validation,simple", "text", 1.6),
    ("Q13 Hash index (was 4.2)", "A hash index is optimised for fast equality lookups using hashing, offering O(1) average lookup. B-tree preferred for range queries.", "exact match,collision,o(1)", "text", 4.2),
    ("Q6 TCP vs UDP (was 6.4)", "TCP is connection-oriented, reliable, used for HTTP, email, FTP. UDP is connectionless, faster, used for streaming, gaming, DNS.", "speed,reliability,use case", "text", 6.4),
]

with open("eval_results.txt", "w", encoding="utf-8") as f:
    f.write(f"{'Question':<40} {'OLD':>5} {'NEW':>5} {'T':>5} {'C':>5}  Result\n")
    f.write("=" * 80 + "\n")
    for label, ans, kw, qtype, old in tests:
        try:
            r = evaluate_answer(ans, kw, qtype)
            flag = "IMPROVED" if r['score'] > old + 0.5 else ("SAME" if abs(r['score'] - old) <= 0.5 else "WORSE")
            f.write(f"{label:<40} {old:>5.1f} {r['score']:>5.1f} {r['technical_score']:>5.1f} {r['communication_score']:>5.1f}  {flag}\n")
        except Exception as e:
            f.write(f"{label:<40} ERROR: {e}\n")

print("Done. Results in eval_results.txt")
