from database.db_handler import load_users, add_user, delete_user

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
