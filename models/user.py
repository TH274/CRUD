from database.db_handler import load_users, add_user, delete_user, save_users, load_admin_users, add_admin_user
import bcrypt

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

    @staticmethod
    def get_by_email(email):
        users = load_users()
        for user in users:
            if user['email'] == email:
                return user
        return None
    
    @staticmethod
    def is_email_for_user(user_id, email):
        user = User.get_by_id(user_id)
        if user and user['email'] == email:
            return True
        return False

class Admin:
    @staticmethod
    def create(name, email, password):
        admins = load_admin_users()
        admin_id = max([admin['id'] for admin in admins], default=0) + 1
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_admin = {"id": admin_id, "name": name, "email": email, "password": hashed_password.decode('utf-8')}
        add_admin_user(new_admin)
        return new_admin

    @staticmethod
    def authenticate(email, password):
        admins = load_admin_users()
        for admin in admins:
            if admin['email'] == email and bcrypt.checkpw(password.encode('utf-8'), admin['password'].encode('utf-8')):
                return admin
        return None