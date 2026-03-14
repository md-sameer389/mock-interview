
import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def verify_dashboard():
    print("1. Logging in as Admin...")
    try:
        # Correct path is /auth/login (not /api/auth/login) based on app.py registration
        resp = requests.post(f"{BASE_URL}/auth/login", json={
            "email": "admin@mock.com", 
            "password": "admin123"
        })
        
        if resp.status_code != 200:
            print(f"Login failed: {resp.status_code} {resp.text}")
            return
            
        data = resp.json()
        token = data.get('token')
        print(f"Login successful. Token received: {token[:10]}...")
        
        headers = {"Authorization": f"Bearer {token}"}
        
        # Admin routes are defined as /api/admin/... and blueprint has no prefix
        # So full path is /api/admin/...
        
        print("\n2. Fetching Admin Dashboard Stats...")
        stats_resp = requests.get(f"{BASE_URL}/api/admin/stats", headers=headers)
        if stats_resp.status_code == 200:
            print("Stats Response:", json.dumps(stats_resp.json(), indent=2))
        else:
            print(f"Failed to fetch stats: {stats_resp.status_code} {stats_resp.text}")

        print("\n3. Fetching Recent Activity...")
        activity_resp = requests.get(f"{BASE_URL}/api/admin/activity", headers=headers)
        if activity_resp.status_code == 200:
            print("Activity Response:", json.dumps(activity_resp.json()[:2], indent=2)) # Show only first 2
        else:
            print(f"Failed to fetch activity: {activity_resp.status_code} {activity_resp.text}")

        print("\n4. Fetching Student List...")
        students_resp = requests.get(f"{BASE_URL}/api/admin/students", headers=headers)
        if students_resp.status_code == 200:
            print(f"Students found: {len(students_resp.json())}")
            print("First student:", json.dumps(students_resp.json()[0], indent=2))
        else:
            print(f"Failed to fetch students: {students_resp.status_code} {students_resp.text}")
            
    except Exception as e:
        print(f"Error during verification: {e}")

if __name__ == "__main__":
    verify_dashboard()
