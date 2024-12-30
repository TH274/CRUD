import json
import os

ADMIN_DB_FILE = 'admin_users.json'
USER_DB_FILE = 'users.json'

def initialize_db():
    """Initialize both admin and user account database files if they don't exist."""
    for db_file in [ADMIN_DB_FILE, USER_DB_FILE]:
        if not os.path.exists(db_file):
            with open(db_file, 'w') as db_file_handle:
                json.dump([], db_file_handle)

def load_data(file_path):
    """Load data from the given JSON file."""
    with open(file_path, 'r') as db_file:
        return json.load(db_file)

def save_data(file_path, data):
    """Save data to the given JSON file."""
    with open(file_path, 'w') as db_file:
        json.dump(data, db_file)

# Admin Functions
def load_admin_users():
    return load_data(ADMIN_DB_FILE)

def save_admin_users(users):
    save_data(ADMIN_DB_FILE, users)

def add_admin_user(user):
    users = load_admin_users()
    users.append(user)
    save_admin_users(users)

# User Functions
def load_users():
    return load_data(USER_DB_FILE)

def save_users(users):
    save_data(USER_DB_FILE, users)

def add_user(user):
    users = load_users()
    users.append(user)
    save_users(users)

def delete_user(user_id):
    """Delete a user by ID."""
    users = load_users()
    users = [user for user in users if user['id'] != user_id]
    save_users(users)