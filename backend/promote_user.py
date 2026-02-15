import sqlite3
import os
import sys

# Add backend to path to import config if needed (or just assume db path)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Depending on where script is run, '../database/interview.db' or 'database/interview.db'
# Best is to be relative to THIS file
DB_PATH = os.path.join(BASE_DIR, '../database/interview.db')

def promote_user():
    email = input("Enter the email of the user to promote to ADMIN: ").strip()
    if not email:
        print("Email cannot be empty.")
        return

    if not os.path.exists(DB_PATH):
        print(f"Error: Database not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # Check if user exists
    user = cur.execute("SELECT id, full_name, role FROM users WHERE email = ?", (email,)).fetchone()
    
    if not user:
        print(f"Error: User with email '{email}' not found.")
        conn.close()
        return
        
    print(f"Found User: ID={user[0]}, Name={user[1]}, Current Role={user[2]}")
    
    confirm = input("Are you sure you want to promote this user to 'admin'? (y/n): ").lower()
    if confirm == 'y':
        try:
            cur.execute("UPDATE users SET role = 'admin' WHERE email = ?", (email,))
            conn.commit()
            print("Success! User is now an Admin.")
            print("Please log out and log back in to access the Admin Portal.")
        except Exception as e:
            print(f"Error updating role: {e}")
    else:
        print("Operation cancelled.")
        
    conn.close()

if __name__ == "__main__":
    promote_user()
