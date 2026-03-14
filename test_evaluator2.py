import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
from utils.evaluator import evaluate_answer

question_keywords = "encapsulation, abstraction, inheritance"

ans1 = "Encapsulation is data hiding. Abstraction hides implementation details. Inheritance is when a child class extends a parent class for example when Dog extends Animal. Because it is important for OOP."
res1 = evaluate_answer(ans1, question_keywords, 'text')

ans2 = "I think it is about making things private, like data hiding. Then there's an abstraction which is like an interface to hide things under the hood to preserve memory. And derived class inherits things. Step 1 is to create a base class."
res2 = evaluate_answer(ans2, question_keywords, 'text')

with open('out.txt', 'w', encoding='utf-8') as f:
    f.write("=== TEST 1 ===\n")
    f.write(f"Tech: {res1['technical_score']}, Prob: {res1['problem_solving_score']}, Comm: {res1['communication_score']} -> {res1['score']}\n")
    f.write(res1['feedback'] + "\n\n")

    f.write("=== TEST 2 ===\n")
    f.write(f"Tech: {res2['technical_score']}, Prob: {res2['problem_solving_score']}, Comm: {res2['communication_score']} -> {res2['score']}\n")
    f.write(res2['feedback'] + "\n\n")
