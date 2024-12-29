from flask import Flask
from controllers.user_controller import user_blueprint
from database.db_handler import initialize_db

app = Flask(__name__)
app.secret_key = 'c0c520efe46e83bbaf00290ef5e139d1b73403ade999ad48'

# Initialize database
initialize_db()

# Register blueprints
app.register_blueprint(user_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
