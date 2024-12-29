from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.user import User

user_blueprint = Blueprint('users', __name__, template_folder='../templates')

@user_blueprint.route('/')
def index():
    users = User.get_all()
    return render_template('user.html', users=users)

@user_blueprint.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    email = request.form.get('email')
    age = request.form.get('age')

    if not name or not email or not age:
        flash("All fields are required!", "error")
        return redirect(url_for('users.index'))

    try:
        User.create(name=name, email=email, age=int(age))
        flash("User added successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "error")

    return redirect(url_for('users.index'))

@user_blueprint.route('/delete/<int:user_id>')
def delete_user(user_id):
    try:
        User.remove(user_id)
        flash("User deleted successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "error")
    return redirect(url_for('users.index'))
