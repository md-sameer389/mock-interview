-- Mock Interview Platform Database Schema
-- SQLite Database

-- Users table: Store user credentials
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT DEFAULT 'student', -- Added role for admin access
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Resumes table: Store uploaded resume data and extracted text
CREATE TABLE IF NOT EXISTS resumes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    filename TEXT NOT NULL,
    extracted_text TEXT NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Skills table: Master list of skills with keyword patterns
CREATE TABLE IF NOT EXISTS skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_name TEXT UNIQUE NOT NULL,
    keywords TEXT NOT NULL  -- Comma-separated keywords for matching
);

-- Questions table: Interview questions with associated skills
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_id INTEGER NOT NULL,
    question_text TEXT NOT NULL,
    difficulty TEXT NOT NULL CHECK(difficulty IN ('Easy', 'Medium', 'Hard')),
    expected_keywords TEXT NOT NULL,  -- Comma-separated keywords for evaluation
    FOREIGN KEY (skill_id) REFERENCES skills(id)
);

-- Interview sessions table: Track each interview attempt
CREATE TABLE IF NOT EXISTS interview_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    resume_id INTEGER NOT NULL,
    total_questions INTEGER NOT NULL,
    total_score REAL DEFAULT 0,
    status TEXT DEFAULT 'in_progress' CHECK(status IN ('in_progress', 'completed')),
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (resume_id) REFERENCES resumes(id)
);

-- Answers table: Store user answers and scores
CREATE TABLE IF NOT EXISTS answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    user_answer TEXT NOT NULL,
    score REAL NOT NULL,
    feedback TEXT NOT NULL,
    flagged BOOLEAN DEFAULT 0, -- Added for reporting issues
    flag_reason TEXT,          -- Reason for flagging
    answered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES interview_sessions(id),
    FOREIGN KEY (question_id) REFERENCES questions(id)
);

-- Drives table: Placement drives
CREATE TABLE IF NOT EXISTS drives (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    role TEXT NOT NULL,
    description TEXT,
    date TEXT NOT NULL,
    status TEXT DEFAULT 'Upcoming' -- Upcoming, Open, Completed
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_resumes_user_id ON resumes(user_id);
CREATE INDEX IF NOT EXISTS idx_questions_skill_id ON questions(skill_id);
CREATE INDEX IF NOT EXISTS idx_sessions_user_id ON interview_sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_answers_session_id ON answers(session_id);