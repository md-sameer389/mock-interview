import sys
sys.path.insert(0, '.')
from utils.evaluator import _evaluate_text_variant, _norm
import re

ans = "TCP is connection-oriented, reliable, used for HTTP, email, FTP. UDP is connectionless, faster, used for streaming, gaming, DNS."
kw = "speed,reliability,use case"

answer_lower = ans.lower()
answer_norm = re.sub(r'[-_]', ' ', answer_lower)

db_keywords = [k.strip().lower() for k in kw.split(',')]
print("DB keywords:", db_keywords)
print("Answer norm snippet:", answer_norm[:80])

def _norm(text):
    return re.sub(r'[-_]', ' ', text.lower())

def has_term(text_norm, term):
    term_norm = _norm(term)
    if len(term_norm) < 4:
        return bool(re.search(r'\b' + re.escape(term_norm) + r'\b', text_norm))
    return term_norm in text_norm

for kw in db_keywords:
    print(f"  '{kw}' in answer_norm: {has_term(answer_norm, kw)}")

r = _evaluate_text_variant(ans, "speed,reliability,use case")
print(f"\nFinal: score={r['score']} tech={r['technical_score']} comm={r['communication_score']}")
