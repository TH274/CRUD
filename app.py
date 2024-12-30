# app.py
from flask import Flask, redirect, url_for
from controllers.user_controller import user_blueprint
from controllers.user_controller import auth_blueprint
from database.db_handler import initialize_db

app = Flask(__name__)
app.secret_key = 'c0c520efe46e83bbaf00290ef5e139d1b73403ade999ad48'

initialize_db()

app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(auth_blueprint, url_prefix='/auth')

@app.route('/')
def default():
    return redirect(url_for('auth.login'))

if __name__ == "__main__":
    app.run(debug=True)
