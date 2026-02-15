import random

class SmartQuestionBuilder:
    """
    Generates dynamic, non-repetitive questions using a combinatorial approach.
    Simulates LLM variety by mixing:
    - Openers (How would you...)
    - Concepts (Memory Management...)
    - Contexts (in a high-load system...)
    """
    
    # KB: Concepts per Skill
    SKILL_CONCEPTS = {
        'Python': ['Global Interpreter Lock (GIL)', 'memory management', 'decorators', 'generators', 'list comprehensions vs loops', 'multi-threading', 'asyncio'],
        'Java': ['Garbage Collection', 'JVM tuning', 'multithreading', 'Stream API', 'Spring Boot dependency injection', 'memory leaks'],
        'JavaScript': ['Event Loop', 'Promises vs Async/Await', 'prototypal inheritance', 'DOM manipulation', 'closures', 'hoisting'],
        'React': ['Virtual DOM', 'useEffect hooks', 'state management (Redux/Context)', 'component lifecycle', 'prop drilling', 'rendering optimization'],
        'SQL': ['indexing strategies', 'JOIN optimization', 'ACID properties', 'normalization vs denormalization', 'stored procedures', 'query execution plans'],
        'Machine Learning': ['overfitting', 'bias-variance tradeoff', 'feature selection', 'model deployment', 'hyperparameter tuning', 'gradient descent'],
        'System Design': ['horizontal scaling', 'load balancing', 'caching strategies', 'database sharding', 'microservices communication', 'CAP theorem trade-offs'],
        'General': ['code maintainability', 'testing strategies', 'CI/CD pipelines', 'debugging complex issues', 'agile methodologies', 'technical debt']
    }

    # KB: Sentence Parts
    OPENERS_TECHNICAL = [
        "Can you explain how {concept} works in {skill}",
        "Walk me through how you would handle {concept} when working with {skill}",
        "What are the best practices for {concept} in {skill}",
        "How does {skill} handle {concept} internally",
        "If you encountered a problem with {concept} in {skill}, how would you debug it",
        "Why is {concept} considered important in the {skill} ecosystem"
    ]

    CONTEXTS = [
        "", # sometimes no context
        "in a high-traffic production environment?",
        "when dealing with legacy code?",
        "to ensure maximum performance?",
        "if you need to scale to millions of users?",
        "considering security implications?",
        "while maintaining code readability?"
    ]

    OPENERS_BEHAVIORAL = [
        "Tell me about a time you struggled with {concept}.",
        "Describe a situation where {concept} was critical to success.",
        "How do you approach {concept} when deadlines are tight?",
        "Give me an example of how you improved {concept} in a past project."
    ]
    
    CONCEPTS_BEHAVIORAL = [
        "team conflict resolution", "identifying requirements", "learning new tech", 
        "mentoring juniors", "managing technical debt", "communicating with stakeholders"
    ]

    @staticmethod
    def get_concept(skill):
        # Return random concept for skill, or generic if skill unknown
        pool = SmartQuestionBuilder.SKILL_CONCEPTS.get(skill, SmartQuestionBuilder.SKILL_CONCEPTS['General'])
        return random.choice(pool)

    @staticmethod
    def build(skill, persona='standard'):
        if persona == 'hr':
            opener = random.choice(SmartQuestionBuilder.OPENERS_BEHAVIORAL)
            concept = random.choice(SmartQuestionBuilder.CONCEPTS_BEHAVIORAL)
            return opener.format(concept=concept)
        
        # Technical / Standard
        concept = SmartQuestionBuilder.get_concept(skill)
        opener = random.choice(SmartQuestionBuilder.OPENERS_TECHNICAL)
        context = random.choice(SmartQuestionBuilder.CONTEXTS)
        
        # Construct
        question = opener.format(skill=skill, concept=concept)
        if context:
             # Fix punctuation if needed
             if question.endswith('?'):
                 question = question[:-1] 
             question += f" {context}"
             
        if not question.endswith('?'):
            question += "?"
            
        return question

def generate_heuristic_questions(skills, count=3, persona='standard'):
    """
    Generate specific questions based on user skills and SELECTED PERSONA.
    """
    questions = []
    
    selected_skills = []
    if skills:
        # De-duplicate and shuffle
        unique_skills = list(set(skills))
        random.shuffle(unique_skills)
        # If we have skills, try to use different ones for each question
        # If count > len(skills), we will cycle or pick random
        selected_skills = unique_skills
    
    generated_count = 0
    
    # Try to generate one question per skill first
    for skill in selected_skills:
        if generated_count >= count:
            break
            
        q_text = SmartQuestionBuilder.build(skill, persona)
        
        # Avoid exact duplicates in this batch
        if any(q['question_text'] == q_text for q in questions):
             # Try one more time
             q_text = SmartQuestionBuilder.build(skill, persona)
        
        base_difficulty = 'Hard' if persona == 'technical' else 'Medium'
        
        questions.append({
            'question_text': q_text,
            'skill_name': skill if persona != 'hr' else 'Behavioral',
            'difficulty': base_difficulty,
            'question_type': 'text',
            'expected_keywords': f"{skill.lower()},experience,approach,solution"
        })
        generated_count += 1
        
    # Fill remaining if skills ran out
    while len(questions) < count:
        # Pick random skill from user's list or General
        skill = random.choice(selected_skills) if selected_skills else 'General'
        q_text = SmartQuestionBuilder.build(skill, persona)
        
        if any(q['question_text'] == q_text for q in questions):
            continue 

        base_difficulty = 'Hard' if persona == 'technical' else 'Medium'
        questions.append({
            'question_text': q_text,
            'skill_name': skill if persona != 'hr' else 'Behavioral',
            'difficulty': base_difficulty,
            'question_type': 'text',
            'expected_keywords': "situation,action,result"
        })
        
    return questions[:count]
