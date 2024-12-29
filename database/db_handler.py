import json
import os

DB_FILE = 'database.json'

def initialize_db():
    """Initialize the database file if it doesn't exist."""
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w') as db_file:
            json.dump([], db_file)

def load_users():
    """Load all users from the database."""
    with open(DB_FILE, 'r') as db_file:
        return json.load(db_file)

def save_users(users):
    """Save the user list to the database."""
    with open(DB_FILE, 'w') as db_file:
        json.dump(users, db_file)

def add_user(user):
    """Add a new user."""
    users = load_users()
    users.append(user)
    save_users(users)

def delete_user(user_id):
    """Delete a user by ID."""
    users = load_users()
    users = [user for user in users if user['id'] != user_id]
    save_users(users)
