import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import os

# RISK 1 MITIGATION: Relative pathing [cite: 12, 19]
KEY_PATH = './serviceAccountKey.json'

def init_db():
    try:
        cred = credentials.Certificate(KEY_PATH)
        firebase_admin.initialize_app(cred)
        return firestore.client()
    except Exception as e:
        print(f"Error: {e}")
        return None

db = init_db()

# --- CRUD OPERATIONS ---

def add_task(uid, title):
    """CREATE: Predictable schema as per feedback [cite: 1]"""
    db.collection('tasks').add({
        'user_id': uid,
        'title': title,
        'status': 'Pending',
        'created_at': datetime.now()
    })
    print(f"Task '{title}' added.")

def view_tasks(uid, status_filter=None):
    """READ & QUERY: Professional touch with data isolation [cite: 1]"""
    query = db.collection('tasks').where('user_id', '==', uid)
    if status_filter:
        query = query.where('status', '==', status_filter)
    
    docs = query.stream()
    print(f"\n{'ID':<25} | {'Title':<20} | {'Status'}")
    print("-" * 60)
    for d in docs:
        t = d.to_dict()
        print(f"{d.id:<25} | {t['title']:<20} | {t['status']}")

def update_task(doc_id, new_status):
    """UPDATE: Modify existing record [cite: 12]"""
    db.collection('tasks').document(doc_id).update({'status': new_status})
    print(f"Task {doc_id} updated to {new_status}.")

def delete_task(doc_id):
    """DELETE: Remove record [cite: 12]"""
    db.collection('tasks').document(doc_id).delete()
    print(f"Task {doc_id} deleted.")

def seed_data(uid):
    """SEED: Professional touch to populate DB instantly [cite: 1]"""
    for i in range(1, 11):
        add_task(uid, f"Sample Task {i}")
    print("10 sample records created!")

# --- USER INTERFACE (Week 2 Task) [cite: 12] ---

def main():
    user_id = "patrick_sano" 
    while db:
        print("\n--- CLOUD TASK MANAGER ---")
        print("1. Add Task\n2. View All\n3. Filter by Status\n4. Update Task\n5. Delete Task\n6. Seed Sample Data\n0. Exit")
        choice = input("Select: ")
        
        if choice == '1':
            add_task(user_id, input("Task title: "))
        elif choice == '2':
            view_tasks(user_id)
        elif choice == '3':
            view_tasks(user_id, input("Filter (Pending/Completed): "))
        elif choice == '4':
            update_task(input("Task ID: "), input("New Status: "))
        elif choice == '5':
            delete_task(input("Task ID: "))
        elif choice == '6':
            seed_data(user_id)
        elif choice == '0':
            break

if __name__ == "__main__":
    main()
    #testing
    