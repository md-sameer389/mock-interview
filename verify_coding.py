
import requests
import json
import sqlite3

BASE_URL = "http://127.0.0.1:5000"
AUTH_URL = f"{BASE_URL}/auth"
INTERVIEW_URL = f"{BASE_URL}/interview"
RESUME_URL = f"{BASE_URL}/resume"

def get_coding_question_id():
    conn = sqlite3.connect('database/interview.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, question_text FROM questions WHERE question_type = 'coding' LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0], row[1]
    return None, None

def run_test():
    session = requests.Session()
    
    # 1. Register/Login
    print("1. Logging in...")
    try:
        res = session.post(f"{AUTH_URL}/login", json={"email": "testbot@mock.com", "password": "password123"})
        if res.status_code != 200:
             # Try register
             res = session.post(f"{AUTH_URL}/register", json={"full_name":"Test Bot","email":"testbot@mock.com","password":"password123"})
             res = session.post(f"{AUTH_URL}/login", json={"email": "testbot@mock.com", "password": "password123"})
             
        token = res.json()['token']
        headers = {'Authorization': f'Bearer {token}'}
        print("   -> Login success.")
    except Exception as e:
        print(f"Login failed: {e}")
        return

    # 2. Get Coding Question ID
    q_id, q_text = get_coding_question_id()
    if not q_id:
        print("No coding question found in DB. Cannot verify.")
        return
    print(f"2. Found Coding Question ID {q_id}: {q_text}")

    # 3. Start Session (Required to submit answer)
    print("3. Starting Session...")
    # Need resume ID? Use existing if possible or upload dummy
    # Short circuit: upload dummy
    MINIMAL_PDF = (b"%PDF-1.1\n1 0 obj <</Type/Catalog/Pages 2 0 R>> endobj\n2 0 obj <</Type/Pages/Kids[3 0 R]/Count 1>> endobj\n3 0 obj <</Type/Page/Parent 2 0 R/MediaBox[0 0 595 842]/Contents 4 0 R/Resources<<>>>> endobj\n4 0 obj <</Length 21>> stream\nBT /F1 12 Tf (Test) Tj ET endstream endobj\nxref\n0 5\n0000000000 65535 f\n0000000009 00000 n\n0000000060 00000 n\n0000000109 00000 n\n0000000213 00000 n\ntrailer <</Size 5/Root 1 0 R>>\nstartxref\n284\n%%EOF")
    files = {'file': ('dummy.pdf', MINIMAL_PDF, 'application/pdf')}
    res = session.post(f"{RESUME_URL}/upload", headers=headers, files=files)
    if res.status_code == 200:
        resume_id = res.json()['resume_id']
    else:
        # Maybe use existing?
        print("Upload failed, trying to continue with hardcoded resume ID if possible... or fail.")
        print(res.text)
        return

    res = session.post(f"{INTERVIEW_URL}/start", headers=headers, json={'resume_id': resume_id, 'persona': 'technical'})
    session_id = res.json()['session_id']
    print(f"   -> Session ID: {session_id}")

    # 4. Submit Coding Answer
    print("4. Submitting Coding Answer...")
    code_answer = "def solution():\n    return 'Hello'"
    
    res = session.post(f"{INTERVIEW_URL}/submit-answer", headers=headers, json={
        'session_id': session_id,
        'question_id': q_id,
        'user_answer': code_answer
    })
    
    print(f"   -> Status Code: {res.status_code}")
    if res.status_code == 200:
        data = res.json()
        print(f"   -> Score: {data.get('score')}")
        print(f"   -> Feedback: {data.get('feedback')[:100]}...")
    else:
        print(f"   -> Error: {res.text}")

    # 5. Verify Split Scores in Result
    print("5. Verifying Split Scores...")
    res = session.get(f"{INTERVIEW_URL}/results/{session_id}", headers=headers)
    data = res.json()
    answers = data.get('answers', [])
    if answers:
        last = answers[-1]
        print(f"   -> Tech Score: {last.get('technical_score')}")
        print(f"   -> Comm Score: {last.get('communication_score')}")
        
        if last.get('technical_score') is not None:
             print("   -> ✅ SUCCESS: Technical Score persisted.")
        else:
             print("   -> ❌ FAILURE: Technical Score missing.")
    else:
        print("   -> No answers found.")

if __name__ == "__main__":
    run_test()
