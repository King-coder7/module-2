import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import os

# RISK 1 MITIGATION: Use a relative path so it works in Lab/Home [cite: 19]
KEY_PATH = './serviceAccountKey.json'

def initialize_firebase():
    if not os.path.exists(KEY_PATH):
        print(f"Error: {KEY_PATH} not found in this folder!")
        return None
    cred = credentials.Certificate(KEY_PATH)
    firebase_admin.initialize_app(cred)
    return firestore.client()

db = initialize_firebase()

# --- CRUD FUNCTIONS ---

def add_task(uid, title):
    """CREATE: Adds a document with the required schema."""
    db.collection('tasks').add({
        'user_id': uid,
        'title': title,
        'status': 'Pending',
        'created_at': datetime.now()
    })
    print(f"Added: {title}")

def view_tasks(uid, status_filter=None):
    """READ & QUERY: Isolates data by user and filters by status."""
    query = db.collection('tasks').where('user_id', '==', uid)
    if status_filter:
        query = query.where('status', '==', status_filter)
    
    docs = query.stream()
    print(f"\n{'ID':<25} | {'Title':<20} | {'Status'}")
    for d in docs:
        t = d.to_dict()
        print(f"{d.id:<25} | {t['title']:<20} | {t['status']}")

def seed_database(uid):
    """PROFESSIONAL TOUCH: Populate sample data automatically."""
    samples = ["Research Firebase", "Setup VS Code", "Clean up code"]
    for s in samples:
        add_task(uid, s)
    print("Database seeded!")

# --- CLI MENU ---

def main():
    user_id = "patrick_sano" # Data Isolation 
    while db:
        print("\n--- CLOUD TASK MANAGER ---")
        print("1. Add Task\n2. View All\n3. Filter by Status\n4. Seed Data\n5. Exit")
        choice = input("Choice: ")
        
        if choice == '1':
            add_task(user_id, input("Task name: "))
        elif choice == '2':
            view_tasks(user_id)
        elif choice == '3':
            status = input("Filter (Pending/Completed): ")
            view_tasks(user_id, status_filter=status)
        elif choice == '4':
            seed_database(user_id)
        elif choice == '5':
            break

if __name__ == "__main__":
    main()