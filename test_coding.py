import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
from utils.evaluator import evaluate_coding_answer

# Fibonacci without function
user_code = """
n = 10
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
"""

# The expected output string from standard logic
# e.g., "0 1 1 2 3 5 8 13 21 34 "
test_cases = json.dumps([
    {"input": 10, "output": "0 1 1 2 3 5 8 13 21 34"}
])

result = evaluate_coding_answer(user_code, test_cases)
print("Score:", result['score'])
print("Tech Score:", result['technical_score'])
print("Comm Score:", result['communication_score'])
print("Feedback:\n", result['feedback'])
