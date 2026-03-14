import re
import json
import logging
import traceback
import random

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# SYNONYM MAP — expanded significantly for better semantic coverage
# ---------------------------------------------------------------------------
SYNONYMS = {
    # Data structures / general
    'hash map':       ['dictionary', 'hash table', 'key-value pair', 'map', 'dict', 'hashmap'],
    'dictionary':     ['hash map', 'hash table', 'key-value pair', 'map', 'dict'],
    'array':          ['list', 'vector', 'collection', 'arr'],
    'list':           ['array', 'vector', 'collection'],
    'loop':           ['iteration', 'iterate', 'cycle'],
    'recursion':      ['recursive', 'self-calling', 'recurse'],

    # OOP
    'polymorphism':   ['many forms', 'multiple forms', 'overloading', 'overriding'],
    'inheritance':    ['parent class', 'child class', 'extends', 'subclass', 'base class', 'derived'],
    'encapsulation':  ['data hiding', 'private', 'protected', 'access control'],
    'abstraction':    ['abstract class', 'interface', 'hide implementation'],
    'compile time':   ['compile-time', 'static', 'method overloading'],
    'runtime':        ['run-time', 'run time', 'dynamic', 'method overriding', 'at runtime'],
    'multiple forms': ['polymorphism', 'overloading', 'overriding'],

    # Algorithms
    'big o':          ['time complexity', 'space complexity', 'efficiency'],
    'time complexity':['big o', 'o(n)', 'o(log n)', 'o(1)', 'o(n^2)'],
    'memoization':    ['memo', 'cache', 'top-down', 'store and reuse'],
    'tabulation':     ['bottom-up', 'dp table', 'iterative dp'],

    # Systems    # DB / SQL
    'cross-validation': ['cross validation', 'k-fold', 'validation set', 'validating', 'cv'],
    'subquery':       ['nested query', 'inner query', 'sub-query', 'select inside', 'nested select',
                       'where salary', 'select max', 'inner select', 'select within'],
    'limit':          ['top 1', 'top 2', 'fetch first', 'rownum', 'row_num', 'select top',
                       'offset', 'fetch next'],
    'row_number':     ['rank', 'dense_rank', 'ntile', 'window function', 'over(', 'over (', 'partition by'],
    'exact match':    ['equality', 'equality lookup', '=', 'equality check'],
    'o(1)':           ['constant time', 'constant lookup', 'hash lookup', 'o(1)', 'average o'],
    'cascade':        ['on delete', 'on update', 'cascading'],

    # Networking / OS
    'diagnose':       ['diagnostic', 'troubleshoot', 'ping', 'traceroute', 'detect'],
    'stateful':       ['connection tracking', 'track state', 'connection state'],
    'packet filter':  ['firewall', 'filter packets', 'acl', 'rules'],

    # Networking
    'api':            ['endpoint', 'service', 'rest', 'interface', 'route'],
    'frontend':       ['client-side', 'ui', 'user interface', 'browser'],
    'backend':        ['server-side', 'server', 'api', 'endpoint', 'flask', 'express'],
    'database':       ['db', 'sql', 'storage', 'data store', 'mysql', 'postgres', 'sqlite'],
    'use case':       ['use cases', 'used for', 'commonly used', 'applications of', 'scenario'],
    'use cases':      ['use case', 'used for', 'commonly used', 'applications of'],
    'speed':          ['faster', 'low latency', 'quick', 'performance', 'efficient', 'throughput'],
    'reliability':    ['reliable', 'guaranteed', 'consistent', 'accurate', 'error-free'],

    # Education / intro
    'education':      ['btech', 'b.tech', 'degree', 'student', 'college', 'university', 'course', 'year', 'engineering'],
    'background':     ['experience', 'journey', 'history', 'studied', 'worked on', 'my name'],
    'proficiency':    ['experience', 'comfortable', 'skilled', 'expert', 'level', 'worked with'],
    'level':          ['experience', 'comfortable', 'proficiency', 'intermediate', 'beginner', 'advanced'],
    'framework':      ['library', 'flask', 'django', 'react', 'express', 'spring', 'rails', 'tool'],

    # Networking
    'api':            ['endpoint', 'service', 'rest', 'interface', 'route'],
    'frontend':       ['client-side', 'ui', 'user interface', 'browser'],
    'backend':        ['server-side', 'server', 'api', 'endpoint', 'flask', 'express'],
    'database':       ['db', 'sql', 'storage', 'data store', 'mysql', 'postgres', 'sqlite'],
}

# ---------------------------------------------------------------------------
# OUTPUT QUESTION: exact answer comparison
# ---------------------------------------------------------------------------
def _normalize_output(text: str) -> str:
    """Normalise whitespace and punctuation for output comparison."""
    # Lowercase, strip, collapse spaces
    text = text.lower().strip()
    # Remove all whitespace inside set/tuple literals for fair comparison
    text = re.sub(r'\s+', ' ', text)
    # Remove spaces around commas and brackets so {1, 2} == {1,2}
    text = re.sub(r'\s*,\s*', ',', text)
    text = re.sub(r'\s*{\s*', '{', text)
    text = re.sub(r'\s*}\s*', '}', text)
    text = re.sub(r'\s*\(\s*', '(', text)
    text = re.sub(r'\s*\)\s*', ')', text)
    text = re.sub(r'\s*\[\s*', '[', text)
    text = re.sub(r'\s*\]\s*', ']', text)
    return text.strip()


def evaluate_output_answer(user_answer: str, expected_keywords: str) -> dict:
    """
    For 'output' question type: compare user answer against expected output.
    expected_keywords field stores the correct output (comma-separated parts or full string).
    We try both exact normalised match and keyword presence.
    """
    user_norm = _normalize_output(user_answer)

    # The expected_keywords for output questions contains the correct output tokens
    # e.g. "{3},{1,2,3,4,5},{1,2}"  or free text like "3 True None"
    correct_parts = [_normalize_output(k) for k in str(expected_keywords).split(',') if k.strip()]
    correct_full  = _normalize_output(expected_keywords.replace(',', ' '))

    # Check how many expected output tokens appear in normalised user answer
    matched = [p for p in correct_parts if p and p in user_norm]
    match_ratio = len(matched) / len(correct_parts) if correct_parts else 0

    # Also try full-string match (great for multi-value outputs like sets)
    full_match = (user_norm == correct_full) or (correct_full in user_norm)

    if full_match or match_ratio >= 0.85:
        tech_score = 10.0
        verdict = "Yes"
    elif match_ratio >= 0.6:
        tech_score = 7.0
        verdict = "Leaning Yes"
    elif match_ratio >= 0.3:
        tech_score = 4.0
        verdict = "Borderline"
    else:
        tech_score = 1.0
        verdict = "No"

    # Communication for output questions: was the answer clear and concise?
    words = len(user_answer.split())
    comm_score = 8.0 if 1 <= words <= 30 else (5.0 if words <= 60 else 3.0)

    final_score = round(tech_score * 0.8 + comm_score * 0.2, 1)

    missing = [p for p in correct_parts if p not in user_norm]
    feedback = (
        f"Overall Verdict: {verdict}\n\n"
        f"Why this answer works:\n"
        f"- {'Correct output!' if tech_score >= 9 else 'Partial match on expected output.'}\n\n"
        f"Areas to refine:\n"
        f"{'- Expected: ' + expected_keywords if tech_score < 9 else '- None.'}\n\n"
        f"Pro Tip:\n"
        f"- {'Great job — output matches perfectly!' if tech_score >= 9 else 'Double-check the output values.'}"
        f"\n\n**Score Breakdown:**\n- Technical Accuracy: {tech_score}/10\n- Communication: {comm_score}/10"
    )

    return {
        'score': final_score,
        'feedback': feedback,
        'matched_keywords': matched,
        'total_keywords': len(correct_parts),
        'technical_score': tech_score,
        'communication_score': comm_score,
    }


# ---------------------------------------------------------------------------
# MAIN ENTRY POINT
# ---------------------------------------------------------------------------
def evaluate_answer(user_answer, expected_keywords, question_type='text',
                    test_cases_json=None, answer_variants_json=None):
    """
    Evaluate user's answer using Strict Technical Interview Standards.
    Routes to specialised evaluators by question_type.
    """
    if not user_answer or not user_answer.strip():
        return {
            'score': 0,
            'feedback': "No answer provided.",
            'matched_keywords': [],
            'total_keywords': 0,
            'technical_score': 0,
            'communication_score': 0
        }

    if question_type == 'coding':
        return evaluate_coding_answer(user_answer, test_cases_json)

    if question_type == 'output':
        return evaluate_output_answer(user_answer, expected_keywords or '')

    # === TEXT / LOGIC QUESTIONS ===
    variants = []
    if answer_variants_json:
        try:
            parsed = json.loads(answer_variants_json)
            if isinstance(parsed, list):
                variants = parsed
        except json.JSONDecodeError:
            pass

    if not variants:
        variants = [{"variant_name": "Standard", "keywords": expected_keywords}]

    best_result = None
    for variant in variants:
        v_keywords = variant.get('keywords', '')
        v_name = variant.get('variant_name', 'Standard')
        result = _evaluate_text_variant(user_answer, v_keywords)
        result['variant_name'] = v_name
        if best_result is None or result['score'] > best_result['score']:
            best_result = result

    return best_result


# ---------------------------------------------------------------------------
# CORE TEXT / LOGIC EVALUATOR — Semantic Matching & Pillar Scoring
# ---------------------------------------------------------------------------
def _evaluate_text_variant(user_answer, expected_keywords):
    answer_lower = user_answer.lower()

    # Parse keywords
    if expected_keywords:
        if isinstance(expected_keywords, list):
            db_keywords = [str(k).strip().lower() for k in expected_keywords]
        else:
            db_keywords = [kw.strip().lower() for kw in str(expected_keywords).split(',') if kw.strip()]
    else:
        db_keywords = []

    # Expand keywords with synonyms
    expanded = set(db_keywords)
    for kw in db_keywords:
        if kw in SYNONYMS:
            expanded.update(SYNONYMS[kw])
    critical_keywords = list(expanded)

    # -----------------------------------------------------------------------
    # MATCHING — Concept-Based Semantic Checking
    # -----------------------------------------------------------------------
    def _norm(text):
        return re.sub(r'[-_]', ' ', text.lower())

    answer_norm = _norm(answer_lower)

    def has_term(text_norm, term):
        term_norm = _norm(term)
        if len(term_norm) < 4:
            return bool(re.search(r'\b' + re.escape(term_norm) + r'\b', text_norm))
        return term_norm in text_norm

    matched_critical = [kw for kw in critical_keywords if has_term(answer_norm, kw)]

    # -----------------------------------------------------------------------
    # PILLAR 1: TECHNICAL SCORE (Accuracy + Depth)
    # -----------------------------------------------------------------------
    target_count = max(len(db_keywords), 1)
    covered_original = []
    
    for orig_kw in db_keywords:
        synonyms_for_kw = SYNONYMS.get(orig_kw, [])
        all_forms = [orig_kw] + synonyms_for_kw
        if any(has_term(answer_norm, f) for f in all_forms):
            covered_original.append(orig_kw)

    match_ratio = min(len(covered_original) / target_count, 1.2)
    accuracy_score = min(match_ratio * 7.0, 7.0)

    depth_markers = ['complexity', 'resource', 'internal', 'memory', 'under the hood', 'performance', 'trade-off', 'trade off', 'edge case', 'limitations', 'bottleneck', 'optimized']
    found_depth = [m for m in depth_markers if m in answer_lower]
    depth_score = min(len(found_depth) * 1.5, 3.0)

    technical_score = round(accuracy_score + depth_score, 1)

    # -----------------------------------------------------------------------
    # PILLAR 2: PROBLEM SOLVING SCORE (Logic + Approach)
    # -----------------------------------------------------------------------
    logic_markers = ['because', 'therefore', 'however', 'specifically', 'firstly', 'finally', 'difference', 'advantage', 'disadvantage', 'important', 'scenario', 'situation', 'task', 'action', 'result']
    found_logic = sum(1 for m in logic_markers if m in answer_lower)
    logic_score = min(found_logic * 1.0, 5.0)

    approach_markers = ['initially', 'then i', 'i would', 'looking at', 'my approach', 'let me', 'step 1', 'first step', 'compare', 'we can', 'what if']
    found_approach = sum(1 for m in approach_markers if m in answer_lower)
    approach_score = min(found_approach * 1.5, 5.0)

    problem_solving_score = round(logic_score + approach_score, 1)

    # -----------------------------------------------------------------------
    # PILLAR 3: COMMUNICATION SCORE (Clarity + Confidence + Examples)
    # -----------------------------------------------------------------------
    word_count = len(answer_lower.split())
    
    if word_count >= 60: clarity_score = 4.0
    elif word_count >= 30: clarity_score = 3.0
    elif word_count >= 15: clarity_score = 2.0
    else: clarity_score = 0.5

    hesitation_markers = ['maybe', 'i guess', 'i think', 'probably', 'not sure', 'i believe', 'i suppose']
    found_hesitations = [m for m in hesitation_markers if m in answer_lower]
    confidence_penalty = min(len(found_hesitations) * 0.5, 2.0)

    example_markers = ['for example', 'e.g.', 'like when', 'in a scenario', 'instance', 'suppose', 'imagine', 'such as', 'for instance', 'consider', 'in practice', 'in real', 'project', 'in our', 'i used', 'i have used', 'i built', 'i worked']
    has_example = any(m in answer_lower for m in example_markers)
    example_score = 3.0 if has_example else 0.0

    communication_score = round(min(clarity_score + example_score + 3.0, 10.0) - confidence_penalty, 1)
    communication_score = max(communication_score, 0.0)

    # -----------------------------------------------------------------------
    # FINAL SCORE & HIRING DECISION
    # -----------------------------------------------------------------------
    final_score = round((technical_score * 0.40) + (problem_solving_score * 0.35) + (communication_score * 0.25), 1)
    if word_count < 5:
        final_score = max(final_score, 0.5)

    # Feedback
    missing_keywords = [kw for kw in db_keywords if kw not in covered_original]
    
    feedback = _generate_recruiter_scorecard(
        final_score, technical_score, problem_solving_score, communication_score,
        covered_original, missing_keywords, found_depth, found_approach, found_hesitations, has_example
    )

    return {
        'score': final_score,
        'feedback': feedback,
        'matched_keywords': matched_critical,
        'total_keywords': len(db_keywords),
        'technical_score': technical_score,
        'communication_score': communication_score,
        'problem_solving_score': problem_solving_score,
    }


# ---------------------------------------------------------------------------
# CODING EVALUATOR (unchanged logic, improved feedback)
# ---------------------------------------------------------------------------
def evaluate_coding_answer(user_answer, test_cases_json):
    syntax_score = 0
    execution_score = 0
    feedback_lines = []

    try:
        compile(user_answer, '<string>', 'exec')
        syntax_score = 10
    except SyntaxError as e:
        return {
            'score': 0,
            'feedback': f"**Verdict: No**\n\n**Critical Failure:** Syntax Error\nLine {e.lineno}: {e.msg}\n\nCode must compile to be evaluated.",
            'matched_keywords': [],
            'total_keywords': 0,
            'technical_score': 0,
            'communication_score': 0
        }

    passed_tests = 0
    total_tests = 0
    local_scope = {}
    
    import sys
    from io import StringIO

    try:
        # Capture stdout for script-style answers
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        
        exec(user_answer, {}, local_scope)
        
        sys.stdout = old_stdout
        script_output = redirected_output.getvalue().strip()
        
        defined_callables = [
            (name, func) for name, func in local_scope.items()
            if callable(func) and func.__module__ is None
        ]

        if not defined_callables:
            # Fallback for script-style answers (no function defined)
            if test_cases_json:
                try:
                    test_cases = json.loads(test_cases_json)
                    total_tests = len(test_cases)
                    
                    # For script style, we can only reasonably test the first case's output 
                    # since we can't pass different inputs to a raw script easily
                    if total_tests > 0:
                        exp = test_cases[0]['output']
                        # Check if the script's printed output contains or matches the expected output
                        if str(exp) in script_output or script_output == str(exp):
                            passed_tests = total_tests # Award full if the logic printed the right thing
                        else:
                            feedback_lines.append(f"Script Output Failed: Got '{script_output}', Expected '{exp}'")
                except json.JSONDecodeError:
                    feedback_lines.append("System Error: Invalid test case format.")
            else:
                 feedback_lines.append("No automated tests. Syntax passed.")
                 execution_score = 10
                 
            # Note: We continue to scoring below, we don't return early anymore
            target_func = None
        else:
            target_func = defined_callables[-1][1]

        if target_func and test_cases_json:
            try:
                test_cases = json.loads(test_cases_json)
                total_tests = len(test_cases)

                for i, case in enumerate(test_cases):
                    inp = case['input']
                    exp = case['output']
                    try:
                        if isinstance(inp, list):
                            res = target_func(*inp)
                        else:
                            res = target_func(inp)

                        if str(res) == str(exp):
                            passed_tests += 1
                        else:
                            feedback_lines.append(f"Test {i+1} Failed: Got {res}, Expected {exp}")
                    except Exception as e:
                        feedback_lines.append(f"Test {i+1} Runtime Error: {str(e)}")

            except json.JSONDecodeError:
                feedback_lines.append("System Error: Invalid test case format.")
        elif target_func:
            feedback_lines.append("No automated tests. Syntax passed.")
            execution_score = 10
            
        if total_tests > 0:
            execution_score = (passed_tests / total_tests) * 10

    except Exception as e:
        return {
            'score': 0,
            'feedback': f"**Verdict: No**\n\n**Runtime Error:** {str(e)}",
            'matched_keywords': [],
            'total_keywords': 0,
            'technical_score': 0,
            'communication_score': 0
        }

    if total_tests > 0:
        final_score = (syntax_score * 0.3) + (execution_score * 0.7)
    else:
        final_score = syntax_score

    final_score = round(final_score, 1)
    technical_score = round(execution_score, 1)
    communication_score = round(syntax_score, 1)

    verdict = "No"
    if final_score >= 9: verdict = "Strong Yes"
    elif final_score >= 7: verdict = "Leaning Yes"
    elif final_score >= 5: verdict = "Borderline"

    formatted_feedback = (
        f"Overall Verdict: {verdict}\n\n"
        f"Code Output:\n"
        f"{chr(10).join(['- ' + line for line in feedback_lines]) if feedback_lines else '- All tests passed.'}\n\n"
        f"**Score Breakdown:**\n"
        f"- Technical (Correctness): {technical_score}/10\n"
        f"- Communication (Syntax/Style): {communication_score}/10"
    )

    return {
        'score': final_score,
        'feedback': formatted_feedback,
        'matched_keywords': [],
        'total_keywords': 0,
        'technical_score': technical_score,
        'communication_score': communication_score
    }


# ---------------------------------------------------------------------------
# RECRUITER's SCORECARD GENERATOR
# ---------------------------------------------------------------------------
def _generate_recruiter_scorecard(score, tech, prob, comm, matched_kw, missing_kw, depth, approach, hesitations, has_example):
    # Hiring Decision Logic
    if score >= 8.5 and tech >= 8.0:
        verdict = "STRONG HIRE"
    elif score >= 7.0 and tech >= 6.0:
        verdict = "HIRE"
    elif score >= 5.0:
        verdict = "LEANING NO (Borderline)"
    else:
        verdict = "NO HIRE"

    # Evidence Generation
    positive_evidence = []
    if matched_kw:
        positive_evidence.append(f"Candidate accurately communicated core concepts ({', '.join(matched_kw[:3])}).")
    if depth:
        positive_evidence.append("Candidate demonstrated technical depth by mentioning constraints/complexities.")
    if approach:
        positive_evidence.append("Good 'think-aloud' approach observed.")
    if has_example:
        positive_evidence.append("Candidate proactively anchored answer with a real-world example/scenario.")
    
    if not positive_evidence:
        positive_evidence.append("The response was minimal or lacking substance.")

    gaps_identified = []
    if missing_kw:
        gaps_identified.append(f"Significant knowledge gap on: {', '.join(missing_kw[:3])}.")
    if hesitations:
        gaps_identified.append("Candidate exhibited low confidence / hesitation during the answer.")
    if not approach and not depth and tech < 8.0:
        gaps_identified.append("Response lacked structural depth and problem-solving framework.")

    if not gaps_identified:
        gaps_identified.append("No major gaps identified in this response.")

    return (
        f"**Hiring Decision: {verdict}**\n\n"
        f"**Positive Evidence Found:**\n"
        f"{chr(10).join(['- ' + p for p in positive_evidence])}\n\n"
        f"**Development Areas / Gaps:**\n"
        f"{chr(10).join(['- ' + p for p in gaps_identified])}\n\n"
        f"**Pillar Breakdown:**\n"
        f"- Technical Depth: {tech}/10\n"
        f"- Problem Solving: {prob}/10\n"
        f"- Communication:   {comm}/10"
    )

# Keep old name for backwards compatibility
def generate_encouraging_feedback(score, matched, missing, hesitations, structure):
    return _generate_recruiter_scorecard(score, score, score, score, matched, missing, [], [], hesitations, structure)
