import sys
sys.path.insert(0, '.')
from utils.evaluator import evaluate_answer

tests = [
    (
        "Q3 Set output (was 1.8)",
        "{3} {1, 2, 3, 4, 5} {1, 2}",
        "set,2},intersection,1,2,3,4,5",
        "output",
        1.8,
    ),
    (
        "Q5 2nd highest salary (was 1.6)",
        "SELECT MAX(salary) FROM Employee WHERE salary < ( SELECT MAX(salary) FROM Employee )",
        "row_number,limit,subquery",
        "logic",
        1.6,
    ),
    (
        "Q4 Polymorphism (was 3.5)",
        "Polymorphism is an OOP concept where the same method can have different behaviors. Compile-time polymorphism uses method overloading. Run-time polymorphism uses method overriding, where a child class provides its own implementation.",
        "multiple forms,compile time,runtime",
        "text",
        3.5,
    ),
    (
        "Q1 Introduce myself (was 4.2)",
        "My name is Mohammed Samir, and I am currently a third-year BTech student with a strong interest in software development, data analysis, and AI-based systems. I have a solid foundation in programming, especially in Python, along with experience in HTML, CSS, and basic backend concepts. Over time, I have worked on several practical projects that helped me apply theoretical knowledge to real-world problems. Some of my key projects include an e-commerce sales analysis, Uber data analysis, house price prediction using machine learning, and a language detection system. One of my major ongoing projects is a Voice-Based AI Mock Interview Platform.",
        "education,background,skills,experience,interest,project,goal,brief,summary,introduce",
        "text",
        4.2,
    ),
    (
        "Q6 TCP vs UDP (was 6.4)",
        "TCP is used when reliability and accuracy are critical. It establishes a connection before data transfer, ensures data is delivered in order, and retransmits lost packets. Use cases: web browsing HTTP HTTPS, email SMTP, file transfer FTP, database connections where data integrity matters more than speed. UDP is used when low latency and speed are more important than guaranteed delivery. It does not establish a connection, does not guarantee order or delivery. Use cases: video audio streaming, online gaming, live broadcasts, VoIP, DNS where occasional packet loss is acceptable but delays are not.",
        "speed,reliability,use case",
        "text",
        6.4,
    ),
    (
        "Q12 Overfitting (was 1.6)",
        "The model is overfitting; it can be fixed by reducing model complexity, applying regularization, using more training data, and validating with cross validation on a separate test set.",
        "test,cross-validation,simple",
        "text",
        1.6,
    ),
    (
        "Q13 Hash index (was 4.2)",
        "A hash index is optimised for fast equality lookups using hashing, offering O(1) average lookup time. B-tree index is preferred for range queries, ordering, and general-purpose indexing. Use hash index when only equality comparisons are needed.",
        "exact match,collision,o(1)",
        "text",
        4.2,
    ),
]

with open("eval_results2.txt", "w", encoding="utf-8") as f:
    f.write(f"{'Question':<45} {'OLD':>5} {'NEW':>5} {'T':>5} {'C':>5}  Result\n")
    f.write("=" * 85 + "\n")
    for label, ans, kw, qtype, old in tests:
        try:
            r = evaluate_answer(ans, kw, qtype)
            if r['score'] > old + 0.5:
                flag = "IMPROVED"
            elif abs(r['score'] - old) <= 0.5:
                flag = "SAME"
            else:
                flag = "WORSE"
            f.write(f"{label:<45} {old:>5.1f} {r['score']:>5.1f} {r['technical_score']:>5.1f} {r['communication_score']:>5.1f}  {flag}\n")
        except Exception as e:
            import traceback
            f.write(f"{label:<45} ERROR: {e}\n")
            f.write(traceback.format_exc() + "\n")
    f.write("\nDone.\n")

print("Results written to eval_results2.txt")
