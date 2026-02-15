import re
import json
import logging
import traceback
import random
from utils.technical_keywords import get_keywords_for_skill

logger = logging.getLogger(__name__)

def evaluate_answer(user_answer, expected_keywords, question_type='text', test_cases_json=None, answer_variants_json=None):
    """
    Evaluate user's answer using Strict Technical Interview Standards.
    Supports multiple valid answer variants (e.g., Iterative vs Recursive).
    Returns a score out of 10 and detailed structured feedback.
    """
    if not user_answer:
        return {
            'score': 0,
            'feedback': "No answer provided.",
            'matched_keywords': [],
            'total_keywords': 0
        }

    # === CODING QUESTIONS ===
    if question_type == 'coding':
        return evaluate_coding_answer(user_answer, test_cases_json)

    # === OUTPUT GUESSING QUESTIONS ===
    if question_type == 'output_guess':
        # Simple exact match or regex match
        # correct_output is passed via expected_keywords or a new param. 
        # For now, let's assume expected_keywords holds the correct output if correct_output is not explicitly passed, 
        # but the plan added a correct_output column. 
        # We need to fetch that value. Since evaluate_answer signature is fixed, we might need to rely on expected_keywords being the output.
        # WAIT: The caller (interview_routes) will pass correct_output as expected_keywords or similar.
        # Let's standardize: expected_keywords will hold the correct output for this type.
        
        normalized_user = user_answer.strip()
        normalized_expected = str(expected_keywords).strip()
        
        if normalized_user == normalized_expected:
             return {
                'score': 10,
                'feedback': "Correct! You identified the correct output.",
                'matched_keywords': [normalized_expected],
                'total_keywords': 1
            }
        else:
             return {
                'score': 0,
                'feedback': f"Incorrect. The correct output was: {normalized_expected}",
                'matched_keywords': [],
                'total_keywords': 1
            }

    # === TEXT QUESTIONS (MULTI-VARIANT SUPPORT) ===
    
    # Check for variants
    variants = []
    if answer_variants_json:
        try:
            parsed = json.loads(answer_variants_json)
            if isinstance(parsed, list):
                variants = parsed
        except json.JSONDecodeError:
            pass
            
    # If no variants, create a single default variant
    if not variants:
        variants = [{"variant_name": "Standard", "keywords": expected_keywords}]
        
    # Evaluate against ALL variants and pick the best one
    best_result = None
    
    for variant in variants:
        # Get keywords for this variant
        v_keywords = variant.get('keywords', '')
        v_name = variant.get('variant_name', 'Standard')
        
        # Run evaluation
        result = _evaluate_text_variant(user_answer, v_keywords)
        result['variant_name'] = v_name
        
        # Keep the best score
        if best_result is None or result['score'] > best_result['score']:
            best_result = result
            
    # Append variant info to feedback if helpful
    if len(variants) > 1 and best_result:
        # Parse existing feedback to insert the note cleanly
        # Or just append it? The strict format is formatted...
        # We'll prepend it to "What the candidate did well" or just leave it implicitly handled by the accurate keywords.
        # Actually, let's explicit mention the approach recognized.
        pass 

    return best_result

def _evaluate_text_variant(user_answer, expected_keywords):
    """
    Core strict text evaluation logic for a single set of keywords.
    """
    # 1. Parse Inputs
    # ---------------------------------------------------------
    answer_lower = user_answer.lower()
    
    # Parse expected keywords from DB
    db_keywords = []
    if expected_keywords:
        # Handle if expected_keywords is list or string
        if isinstance(expected_keywords, list):
             db_keywords = [str(k).strip().lower() for k in expected_keywords]
        else:
             db_keywords = [kw.strip().lower() for kw in str(expected_keywords).split(',') if kw.strip()]
        
    # Get broader skill context keywords (e.g., if expected has "python", get all python terms)
    skill_context_keywords = []
    if db_keywords:
        # Heuristic: First keyword implies skill context
        # Check against known skill keys
        for kw in db_keywords:
            related = get_keywords_for_skill(kw)
            if related:
                skill_context_keywords.extend(related)
                break
    
    # "Critical" keywords are those explicitly expected by the question
    critical_keywords = db_keywords 
    # "Bonus" keywords are relevant technical terms from the broader skill domain
    bonus_keywords = list(set(skill_context_keywords) - set(critical_keywords))
    
    # 2. Analyze Content (Match & Count)
    # ---------------------------------------------------------
    matched_critical = []
    matched_bonus = []
    
    # Helper for robust matching (word boundaries)
    def has_term(text, term):
        if len(term) < 4:
            return bool(re.search(r'\b' + re.escape(term) + r'\b', text))
        return term in text

    for kw in critical_keywords:
        if has_term(answer_lower, kw):
            matched_critical.append(kw)
            
    for kw in bonus_keywords:
        if has_term(answer_lower, kw):
            matched_bonus.append(kw)
            
    # Check for Hesitation / Weak Language
    hesitation_markers = ['maybe', 'i guess', 'i think', 'probably', 'not sure', 'umb', 'uh']
    found_hesitations = [m for m in hesitation_markers if m in answer_lower]
    
    # Check for Vague Fillers
    vague_markers = ['stuff', 'things', 'basically', 'sort of', 'kind of']
    found_vague = [m for m in vague_markers if m in answer_lower]

    # Check for Structure/Logic
    structure_markers = ['because', 'therefore', 'however', 'specifically', 'for example', 'firstly', 'finally', 'consequently']
    found_structure = [m for m in structure_markers if m in answer_lower]

    # 3. Calculate Strict Score
    # ---------------------------------------------------------
    # Base Confidence: Starts at 5.0 (Neutral)
    # Correctness is key.
    
    score = 0.0
    
    # A. Critical Coverage (Max 6.0)
    if critical_keywords:
        coverage = len(matched_critical) / len(critical_keywords)
        score += coverage * 6.0
    else:
        # If no strict expected keywords, rely on bonus technical terms
        score += min(len(matched_bonus) * 1.5, 6.0)

    # B. Technical Depth (Bonus Terms) (Max 3.0)
    # Showing knowledge beyond the bare minimum
    if matched_bonus:
        score += min(len(matched_bonus) * 0.5, 3.0)

    # C. Structure & Clarity (Max 1.0)
    if len(answer_lower.split()) > 20 and found_structure:
        score += 1.0
        
    # D. Penalties
    score -= len(found_hesitations) * 1.0  # Hesitation is fatal in interviews
    score -= len(found_vague) * 0.5        # Vagueness indicates lack of depth
    
    # E. Sanity Checks
    # If answer is very short (<10 words) but has keywords -> Buzzword dumping?
    if len(answer_lower.split()) < 10 and score > 4:
        score = 4.0 # Cap score for one-liners
        
    # Boundary Check
    score = max(0.0, min(score, 10.0))
    score = round(score, 1)

    # 4. Generate Structured Feedback
    # ---------------------------------------------------------
    feedback = generate_strict_feedback(
        score, 
        matched_critical, 
        list(set(critical_keywords) - set(matched_critical)), 
        found_hesitations,
        found_structure
    )

    return {
        'score': score,
        'feedback': feedback,
        'matched_keywords': matched_critical + matched_bonus,
        'total_keywords': len(critical_keywords)
    }

def evaluate_coding_answer(user_answer, test_cases_json):
    """
    Evaluates coding answers with execution and formats feedback strictly.
    """
    syntax_score = 0
    execution_score = 0
    feedback_lines = []
    
    # 1. Syntax Valid?
    try:
        compile(user_answer, '<string>', 'exec')
        syntax_score = 10
    except SyntaxError as e:
        return {
            'score': 0,
            'feedback': f"**Verdict: No**\n\n**Critical Failure:** Syntax Error\nLine {e.lineno}: {e.msg}\n\nCode must compile to be evaluated.",
            'matched_keywords': [],
            'total_keywords': 0
        }

    # 2. Execution Test (Mandatory)
    passed_tests = 0
    total_tests = 0
    local_scope = {}
    
    try:
        # A. execute the user's code to define functions/classes
        # This will catch NameErrors like 'dfvsdfv' if they are top-level expressions
        exec(user_answer, {}, local_scope)
        
        # B. Check for defined function/class
        # Filter out built-ins and verify callable
        defined_callables = [
            (name, func) for name, func in local_scope.items() 
            if callable(func) and func.__module__ is None # ensure it's defined in this scope
        ]
        
        if not defined_callables:
            return {
                'score': 0,
                'feedback': "**Verdict: No**\n\n**Critical Failure:** No Function Defined.\n\nYou must define a function (e.g., `def solution(): ...`) to solve the problem.",
                'matched_keywords': [],
                'total_keywords': 0
            }
            
        target_func = defined_callables[-1][1] # Use the last defined function
        
        # C. Run Test Cases
        if test_cases_json:
            try:
                test_cases = json.loads(test_cases_json)
                total_tests = len(test_cases)
                
                for i, case in enumerate(test_cases):
                    inp = case['input']
                    exp = case['output']
                    try:
                        # Handle varied input formats
                        if isinstance(inp, list):
                            res = target_func(*inp)
                        else:
                            res = target_func(inp)
                        
                        # Compare
                        # Convert to string to handle type mismatches gracefully in feedback
                        if str(res) == str(exp): 
                            passed_tests += 1
                        else:
                            feedback_lines.append(f"Test {i+1} Failed: Input {inp} -> Expected {exp}, Got {res}")
                    except Exception as e:
                        feedback_lines.append(f"Test {i+1} Runtime Error: {str(e)}")
                        
                if total_tests > 0:
                    execution_score = (passed_tests / total_tests) * 10
                else:
                    feedback_lines.append("System Error: No valid test cases found.")
                    execution_score = 0
                    
            except json.JSONDecodeError:
                 feedback_lines.append("System Error: Invalid test case format.")
                 execution_score = 0
        else:
            # Fallback: No test cases = Cannot Verify Correctness
            feedback_lines.append("System Error: No automated tests available for this question.")
            execution_score = 0 # STRICT: Do not give free points.
            
    except Exception as e:
         return {
            'score': 0,
            'feedback': f"**Verdict: No**\n\n**Runtime Error:** {str(e)}\n\nYour code crashed during definition/execution.",
            'matched_keywords': [],
            'total_keywords': 0
         }

    # Final logic
    if not test_cases_json or total_tests == 0:
        final_score = 0 # Force 0 if unable to test
        verdict = "System Error"
    else:
        final_score = (syntax_score * 0.4) + (execution_score * 0.6)
        final_score = round(final_score, 1)
        verdict = "No"
        if final_score >= 9: verdict = "Strong Yes"
        elif final_score >= 7: verdict = "Leaning Yes"
        elif final_score >= 5: verdict = "Borderline"

    formatted_feedback = f"""Overall Verdict: {verdict}

Conceptual Accuracy: {'High' if final_score > 8 else 'Moderate' if final_score > 5 else 'Low'}

What the candidate did well:
{'- Code executed without runtime errors.' if syntax_score==10 else '- Nothing.'}
{f'- Passed {passed_tests}/{total_tests} test cases.' if total_tests > 0 else ''}

What is incorrect or missing:
{chr(10).join(['- ' + line for line in feedback_lines]) if feedback_lines else '- Function logic seems correct for provided cases.'}

Interviewer’s concern:
{'- Partial failure.' if passed_tests < total_tests else '- No major concerns.'}

How to improve:
- Check edge cases.
- Verify algorithm time complexity."""

    return {
        'score': final_score,
        'feedback': formatted_feedback,
        'matched_keywords': [],
        'total_keywords': 0
    }

def generate_strict_feedback(score, matched, missing, hesitations, structure):
    """
    Generates the specific 'Interviewer Verdict' format.
    """
    # 1. Determine Verdict
    if score >= 8.5:
        verdict = "Strong Yes"
        impact = "Pass. Clearly hire-able."
    elif score >= 7.0:
        verdict = "Leaning Yes"
        impact = "Likely Pass, but would probe deeper in next round."
    elif score >= 5.0:
        verdict = "Borderline"
        impact = "Risky. Fundamentals are shaky."
    else:
        verdict = "No"
        impact = "Reject. Not ready for this level."

    # 2. Conceptual Accuracy Assessment
    if score > 8:
        accuracy = "High. Concepts are well-understood."
    elif score > 5:
        accuracy = "Moderate. Basic understanding present, but lacks depth/precision."
    else:
        accuracy = "Low. Significant gaps in understanding."

    # 3. What Went Well
    good_points = []
    if matched:
        good_points.append(f"Correctly identified key terms: {', '.join(matched[:3])}")
    if structure:
        good_points.append("Used logical connectors to structure the answer.")
    if not hesitations and len(matched) > 1:
        good_points.append("Confident delivery without fillers.")
    if not good_points:
        good_points.append("Attempted to answer relevant to the topic.")
        
    # 4. What is Wrong/Missing
    bad_points = []
    if missing:
        bad_points.append(f"Missed critical concepts: {', '.join(missing[:3])}")
    if hesitations:
        bad_points.append(f"Used low-confidence hesitation markers ('{hesitations[0]}').")
    if score < 4:
        bad_points.append("Explanation was too vague or surface-level.")
        
    # 5. Improvement
    improvement = []
    if missing:
        improvement.append(f"Study specifically about: {', '.join(missing)}")
    if hesitations:
        improvement.append("Avoid 'I think/maybe'. State facts clearly.")
    if not structure:
        improvement.append("Use the STAR method (Situation, Task, Action, Result) or 'What/Why/How' structure.")
        
    # Format String
    return f"""Overall Verdict: {verdict}

Conceptual Accuracy: {accuracy}

What the candidate did well:
{chr(10).join(['- ' + p for p in good_points])}

What is incorrect or missing:
{chr(10).join(['- ' + p for p in bad_points]) if bad_points else '- None identified.'}

Interviewer’s concern (if any):
{impact}

How the answer could be improved to be clearly hire-worthy:
{chr(10).join(['- ' + p for p in improvement])}"""

    """
    Evaluate user's answer using Simulated Hybrid Intelligence (Heuristics) OR Dynamic Execution
    """
    if not user_answer:
        return {
            'score': 0,
            'feedback': "No answer provided.",
            'matched_keywords': [],
            'total_keywords': 0
        }

    # 1. Keyword Score (Enhanced with Technical Dictionary)
    from utils.technical_keywords import get_keywords_for_skill
    
    answer_lower = user_answer.lower()
    if not expected_keywords:
        expected_keywords = ""
        
    # Parse explicit expected keywords (from DB)
    db_keywords = [kw.strip().lower() for kw in str(expected_keywords).split(',') if kw.strip()]
    
    # Identify Potential Skill Context (Assumes first keyword is skill name, e.g. "python")
    # OR check if any known skill is in the db_keywords
    skill_context_keywords = []
    if db_keywords:
        potential_skill = db_keywords[0] # heuristic: first tag is usually skill
        skill_context_keywords = get_keywords_for_skill(potential_skill)
        
    # Combine lists (DB keywords + Rich Technical keywords)
    # We prioritize specific technical terms over generic "challenge"
    all_possible_keywords = list(set(db_keywords + skill_context_keywords))
    
    matched_count = 0
    matched_keywords = []
    
    # Check for matches
    for keyword in all_possible_keywords:
        # Use simple substring match for now (robust enough for phrases)
        # Add word boundary check for short words to avoid false positives (e.g. "c")
        if len(keyword) < 4:
             if re.search(r'\b' + re.escape(keyword) + r'\b', answer_lower):
                 matched_count += 1
                 matched_keywords.append(keyword)
        else:
             if keyword in answer_lower:
                 matched_count += 1
                 matched_keywords.append(keyword)
            
    # SCORE CALCULATION
    # Density Scoring: 1 relevant term = 3.0, 2=6.0, 3=9.0, 4+=10.0
    
    if len(all_possible_keywords) == 0:
        keyword_score = 0
    else:
        # Soft cap at 4 keywords for full marks
        keyword_score = min(matched_count * 3.0, 10.0)
    
    logger.debug(f"Matched Technical Keywords: {matched_keywords}, Keyword Score: {keyword_score} (Count: {matched_count})")
        
    # BACKWARD COMPATIBILITY & FEEDBACK
    # The feedback generator expects 'keywords' and 'total_keywords'.
    # We use db_keywords for specific "missing" feedback, but the score is already high if they used technical terms.
    keywords = db_keywords
    total_keywords = len(db_keywords)

    # === CODING EVALUATION LOGIC (DYNAMIC) ===
    if question_type == 'coding':
        syntax_score = 0
        execution_score = 0
        feedback_lines = []
        
        # 1. Syntax Valid?
        try:
            compile(user_answer, '<string>', 'exec')
            syntax_score = 10
            feedback_lines.append("Syntax: Valid.")
        except SyntaxError as e:
            return {
                'score': 0,
                'feedback': f"Syntax Error on line {e.lineno}: {e.msg}",
                'matched_keywords': matched_keywords,
                'total_keywords': total_keywords
            }

        # 2. Execution Test
        passed_tests = 0
        total_tests = 0
        
        if test_cases_json:
            try:
                test_cases = json.loads(test_cases_json)
                total_tests = len(test_cases)
                
                # Create a safe-ish scope
                local_scope = {}
                try:
                    exec(user_answer, {}, local_scope)
                except Exception as e:
                    return {
                        'score': 2,
                        'feedback': f"Runtime Error during definition: {str(e)}",
                        'matched_keywords': matched_keywords
                    }
                
                # Find the target function (last defined function)
                target_func = None
                for key, val in local_scope.items():
                    if callable(val):
                        target_func = val
                
                if not target_func:
                    feedback_lines.append("Error: No function defined. Please define a function.")
                else:
                    # Run Tests
                    for i, case in enumerate(test_cases):
                        inp = case['input'] # List of args
                        exp = case['output']
                        
                        try:
                            # Handle single arg vs multi arg
                            if isinstance(inp, list):
                                res = target_func(*inp)
                            else:
                                res = target_func(inp)
                                
                            if res == exp:
                                passed_tests += 1
                            else:
                                feedback_lines.append(f"Test {i+1} Failed: Input {inp} -> Expected {exp}, Got {res}")
                        except Exception as e:
                            feedback_lines.append(f"Test {i+1} Error: {str(e)}")
                    
                    execution_score = (passed_tests / total_tests) * 10
                    feedback_lines.append(f"Tests Passed: {passed_tests}/{total_tests}")

            except json.JSONDecodeError:
                feedback_lines.append("System Error: Invalid test case format.")
            except Exception as e:
                 feedback_lines.append(f"System Error: {str(e)}")
        else:
             feedback_lines.append("No automated tests available for this question. syntax check only.")
             execution_score = 10 # Default pass if no tests
             
        final_score = (syntax_score * 0.4) + (execution_score * 0.6)
        final_score = round(final_score, 1)
        
        return {
            'score': final_score,
            'feedback': " ".join(feedback_lines),
            'matched_keywords': matched_keywords,
            'total_keywords': total_keywords,
            'details': {
                'syntax_score': syntax_score,
                'execution_score': execution_score,
                'passed_tests': passed_tests,
                'total_tests': total_tests
            }
        }

    # === TEXT/VERBAL EVALUATION LOGIC (Original) ===
    
    # 2. Depth Score (20%)
    word_count = len(user_answer.split())
    depth_score = min(max((word_count - 20) / 80 * 10, 0), 10)
    
    # 3. Structure Score (20%)
    # Check for analytical/connecting words
    structure_markers = ['because', 'therefore', 'however', 'for example', 'firstly', 'finally', 
                        'specifically', 'in contrast', 'basically', 'include', 'additionally', 
                        'also', 'plus', 'secondly', 'thirdly', 'conclusion', 'summary', 'overall']
    structure_hits = sum(1 for marker in structure_markers if marker in answer_lower)
    structure_score = min(structure_hits * 3.5, 10) 
    
    # 4. Confidence Score (10%)
    hesitation_markers = ['maybe', 'i think', 'i guess', 'probably', 'not sure', 'umb', 'uh']
    hesitation_hits = sum(1 for marker in hesitation_markers if marker in answer_lower)
    confidence_score = max(10 - (hesitation_hits * 2), 0)
    
    # Calculate Weighted Final Score
    final_score = (
        (keyword_score * 0.50) +
        (depth_score * 0.20) +
        (structure_score * 0.20) +
        (confidence_score * 0.10)
    )
    
    # Rounding
    final_score = round(final_score, 1)
    
    # Generate Advanced Feedback
    missing_keywords = [kw for kw in keywords if kw not in matched_keywords]
    feedback = generate_advanced_feedback(final_score, keyword_score, depth_score, structure_score, confidence_score, matched_keywords, missing_keywords)
    
    return {
        'score': final_score,
        'feedback': feedback,
        'matched_keywords': matched_keywords,
        'total_keywords': total_keywords,
        'details': {
            'keyword_score': round(keyword_score, 1),
            'depth_score': round(depth_score, 1),
            'structure_score': round(structure_score, 1),
            'confidence_score': round(confidence_score, 1)
        }
    }

def generate_advanced_feedback(final_score, k_score, d_score, s_score, c_score, matched, missing):
    """
    Generates context-aware feedback based on specific sub-scores.
    """
    
    # Determine the "Weakest Link"
    metrics = {
        'keywords': k_score, 
        'depth': d_score, 
        'structure': s_score, 
        'confidence': c_score
    }
    weakest_metric = min(metrics, key=metrics.get)
    
    # Opening Statement
    if final_score >= 7.5:
        opener = random.choice([
            "Outstanding answer. You demonstrated both breadth and depth.",
            "This is a senior-level response. Very well articulated.",
            "Excellent. You hit the key technical points with confidence."
        ])
    elif final_score >= 5:
        opener = random.choice([
            "Good effort. You're on the right track, but there's room for polish.",
            "A solid B-grade answer. You understand the basics.",
            "Acceptable, but to stand out, you need to be more precise."
        ])
    else:
        opener = random.choice([
            "This answer needs significant work.",
            "I'm not convinced you fully grasp this concept yet.",
            "A bit too vague for a technical interview."
        ])
        
    # Specific Advice based on Weakest Metric
    advice = ""
    if weakest_metric == 'keywords':
        missing_str = ", ".join(missing[:2])
        advice = f"You missed critical technical terms like '{missing_str}'. Precision matters."
    elif weakest_metric == 'depth':
        advice = "Your answer was too brief. Elaborate on the 'how' and 'why', not just the 'what'."
    elif weakest_metric == 'structure':
        advice = "Your explanation felt a bit unstructured. Try using phrases like 'First', 'However', or 'For example' to guide the listener."
    elif weakest_metric == 'confidence':
        advice = "You used too many hesitation words (like 'I think' or 'maybe'). State your answer with authority."
        
    # Closing
    closer = "Keep practicing!"
    if final_score >= 8:
        closer = "You're ready for the real thing."
        
    return f"{opener} {advice} {closer}"
