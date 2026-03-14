import sqlite3
import json
import argparse
import sys
import os

DATABASE_PATH = 'database/interview.db'
if not os.path.exists(DATABASE_PATH):
    if os.path.exists('interview.db'):
        DATABASE_PATH = 'interview.db'
    elif os.path.exists('../database/interview.db'):
        DATABASE_PATH = '../database/interview.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def list_questions(args):
    conn = get_db_connection()
    try:
        query = "SELECT id, question_text, skill_id, difficulty, topic, question_type FROM questions"
        params = []
        
        if args.skill:
            query += " WHERE skill_id = ?"
            params.append(args.skill)
        elif args.type:
            query += " WHERE question_type = ?"
            params.append(args.type)
            
        questions = conn.execute(query, params).fetchall()
        
        print(f"\nFound {len(questions)} questions:")
        print("-" * 100)
        print(f"{'ID':<5} {'Type':<10} {'Topic':<15} {'Diff':<8} {'Question (truncated)'}")
        print("-" * 100)
        
        for q in questions:
            text = q['question_text'][:60] + "..." if len(q['question_text']) > 60 else q['question_text']
            print(f"{q['id']:<5} {q['question_type']:<10} {q['topic'][:15]:<15} {q['difficulty']:<8} {text}")
        print("-" * 100)
    finally:
        conn.close()

def add_question(args):
    print("\n--- Add New Question ---")
    
    # 1. Skill
    conn = get_db_connection()
    skills = conn.execute("SELECT id, skill_name FROM skills").fetchall()
    print("\nAvailable Skills:")
    for s in skills:
        print(f"{s['id']}: {s['skill_name']}")
    
    skill_id = input("\nEnter Skill ID: ").strip()
    
    # 2. Basic Info
    text = input("Question Text: ").strip()
    difficulty = input("Difficulty (Easy/Medium/Hard): ").strip()
    if difficulty not in ['Easy', 'Medium', 'Hard']:
        print("Invalid difficulty. Defaulting to Medium.")
        difficulty = "Medium"
        
    keywords = input("Expected Keywords (comma-separated): ").strip()
    q_type = input("Question Type (text/coding/behavioral) [text]: ").strip() or "text"

    # Simplified: No longer asking for Premium fields
    
    # 3. Insert
    try:
        from backend.models.question_model import create_dynamic_question
        # Use valid args for create_dynamic_question(text, skill_name, difficulty, keywords, q_type)
        # But wait, create_dynamic_question takes skill_name, not ID. 
        # Let's fix this to use ID directly or fetch name.
        
        # Actually easier to just use raw SQL here to match previous behavior
        conn.execute("""
            INSERT INTO questions (
                skill_id, question_text, difficulty, expected_keywords, question_type
            ) VALUES (?, ?, ?, ?, ?)
        """, (skill_id, text, difficulty, keywords, q_type))
        conn.commit()
        print(f"\nQuestion added successfully.")
    except Exception as e:
        print(f"\nError adding question: {e}")
    finally:
        conn.close()

def delete_question(args):
    if not args.id:
        print("Error: --id is required for deletion.")
        return

    conn = get_db_connection()
    try:
        q = conn.execute("SELECT id, question_text FROM questions WHERE id = ?", (args.id,)).fetchone()
        if not q:
            print("Question not found.")
            return
            
        confirm = input(f"Are you sure you want to delete question {args.id}: '{q['question_text']}'? (y/N): ")
        if confirm.lower() == 'y':
            conn.execute("DELETE FROM questions WHERE id = ?", (args.id,))
            conn.commit()
            print("Question deleted.")
        else:
            print("Deletion cancelled.")
    finally:
        conn.close()

def main():
    parser = argparse.ArgumentParser(description="Manage Question Database")
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # List
    list_parser = subparsers.add_parser('list', help='List questions')
    list_parser.add_argument('--skill', type=int, help='Filter by Skill ID')
    list_parser.add_argument('--type', type=str, help='Filter by Question Type')
    
    # Add
    add_parser = subparsers.add_parser('add', help='Add a new question')
    
    # Delete
    delete_parser = subparsers.add_parser('delete', help='Delete a question')
    delete_parser.add_argument('--id', type=int, required=True, help='Question ID to delete')
    
    args = parser.parse_args()
    
    if args.command == 'list':
        list_questions(args)
    elif args.command == 'add':
        add_question(args)
    elif args.command == 'delete':
        delete_question(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
