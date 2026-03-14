import sys
import os

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from utils.evaluator import evaluate_answer

question_keywords = "encapsulation, abstraction, inheritance"

# Test 1: Textbook answer
textbook_ans = "Encapsulation is data hiding. Abstraction hides implementation details. Inheritance is when a child class extends a parent class for example when Dog extends Animal. Because it is important for OOP."
res1 = evaluate_answer(textbook_ans, question_keywords, 'text')

print("=== TEST 1: Textbook Answer ===")
print("Dict Keys:", res1.keys())
print("Tech Score:", res1.get('technical_score'))
print("Prob Score:", res1.get('problem_solving_score'))
print("Comm Score:", res1.get('communication_score'))
print("Final Score:", res1.get('score'))
print("Feedback:\n", res1.get('feedback'))

# Test 2: Natural "Own Words" answer with some hesitations and depth
own_words = "I think it is about making things private, like data hiding. Then there's an abstraction which is like an interface to hide things under the hood to preserve memory. And derived class inherits things. Step 1 is to create a base class."
res2 = evaluate_answer(own_words, question_keywords, 'text')

print("\n=== TEST 2: Own Words with Depth ===")
print("Tech Score:", res2.get('technical_score'))
print("Prob Score:", res2.get('problem_solving_score'))
print("Comm Score:", res2.get('communication_score'))
print("Final Score:", res2.get('score'))
print("Feedback:\n", res2.get('feedback'))

