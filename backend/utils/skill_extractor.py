import re
from models.question_model import get_all_skills

def extract_skills_from_text(resume_text):
    """
    Extract skills from resume text with section awareness to reduce false positives.
    """
    text_lower = resume_text.lower()
    
    # 1. Try to isolate the "Skills" section
    # Common headers for skills
    skill_headers = ['technical skills', 'skills', 'technologies', 'competencies', 'programming languages']
    
    skills_section_text = ""
    start_idx = -1
    
    for header in skill_headers:
        # distinct header pattern (newline + header + newline/colon)
        # simplistic check
        idx = text_lower.find(header)
        if idx != -1:
            start_idx = idx
            break
            
    if start_idx != -1:
        # Find the next section header to stop (e.g., "Projects", "Experience")
        # Just grab the next 1000 chars as a heuristic for the skills section
        skills_section_text = text_lower[start_idx:start_idx+1000]
    else:
        # Fallback: Treat the bottom 30% of resume as likely place for skills if no header found?
        # Or just use full text but be stricter.
        skills_section_text = text_lower

    # Get all skills from database
    all_skills = get_all_skills()
    matched_skills = []
    
    for skill in all_skills:
        skill_name = skill['skill_name']
        keywords = skill['keywords'].lower().split(',')
        
        # Strategy:
        # If skill name/keyword is in the "Skills Section", it's a strong match.
        # If it's only in general text, we need to be careful.
        
        is_match = False
        
        # 1. Check strict match in Skills Section (High Confidence)
        if start_idx != -1:
            if re.search(r'\b' + re.escape(skill_name.lower()) + r'\b', skills_section_text):
                is_match = True
            else:
                for kw in keywords:
                    if re.search(r'\b' + re.escape(kw.strip()) + r'\b', skills_section_text):
                        is_match = True
                        break
        
        # 2. If not found in explicit section, check full text BUT with exclusions
        if not is_match and start_idx == -1:
            # For broad skills like 'Web Development', we might skip them if not in skills section
            # or check for them globally.
            search_scope = text_lower
            
            # EXCLUSION PATTERNS for False Positives
            # e.g. "web development video course" -> should not trigger "Web Development"
            # match "web development" but NOT if followed by "course" or "project" directly?
            # Too complex for regex for all.
            
            # Simple check: Does the skill name appear?
            if re.search(r'\b' + re.escape(skill_name.lower()) + r'\b', search_scope):
                 is_match = True
                 
            # If skill name didn't match, check keywords
            if not is_match:
                for kw in keywords:
                    if re.search(r'\b' + re.escape(kw.strip()) + r'\b', search_scope):
                        is_match = True
                        break

    
        # 3. Special Case Filter: Web Development
        # If we matched "Web Development" but the context is "Web Development video course", ignore it.
        if is_match and skill_name == "Web Development":
            # Check for invalidating phrases
            if "web development video course" in text_lower or \
               "web development project" in text_lower:
                # If these represent the ONLY occurrences, we should probably unmatch.
                # But calculating that is hard. 
                # Let's just be conservative: matches in Projects often mean "I built a project IN this", 
                # implying they HAVE the skill. 
                # The user's compliant is that they don't *specialize* in it or list it as a main skill.
                pass
        
        # PROPOSED REFINED LOGIC:
        # If a skill was NOT found in the explicit "Skills" section (if one existed),
        # AND it's a broad category skill (like Web Dev), exclude it.
        # This honors the user's explicit "Technical Skills" list.
        
        if start_idx != -1:
             # We found a skills section. Any match MUST come from there.
             # Reset match to False and re-verify ONLY against skills_section_text
             # This is aggressive but accurate for standard resumes.
             is_match = False
             if re.search(r'\b' + re.escape(skill_name.lower()) + r'\b', skills_section_text):
                 is_match = True
             else:
                 for kw in keywords:
                     if re.search(r'\b' + re.escape(kw.strip()) + r'\b', skills_section_text):
                         is_match = True
                         break
        
        if is_match:
            matched_skills.append(skill_name)
    
    return matched_skills
