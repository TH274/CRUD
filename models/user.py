# Model
from database.db_handler import load_users, add_user, delete_user, save_users

class User:
    @staticmethod
    def get_all():
        return load_users()

    @staticmethod
    def create(name, email, age):
        users = load_users()
        user_id = max([user['id'] for user in users], default=0) + 1
        new_user = {"id": user_id, "name": name, "email": email, "age": age}
        add_user(new_user)
        return new_user

    @staticmethod
    def remove(user_id):
        delete_user(user_id)

    @staticmethod
    def email_exists(email):
        users = load_users()
        return any(user['email'] == email for user in users)

    @staticmethod
    def id_exists(user_id):
        users = load_users()
        return any(user['id'] == user_id for user in users)

    @staticmethod
    def get_by_id(user_id):
        users = load_users()
        for user in users:
            if user['id'] == user_id:
                return user
        return None

    @staticmethod
    def update(user_id, name, email, age):
        users = load_users()
        for user in users:
            if user['id'] == user_id:
                user['name'] = name
                user['email'] = email
                user['age'] = age
                break
        save_users(users)