# Controller
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

    # Validate inputs
    if not name or not email or not age:
        flash("All fields are required!", "error")
        return redirect(url_for('users.index'))

    if not email.count("@") or not email.count("."):
        flash("Invalid email format!", "error")
        return redirect(url_for('users.index'))

    try:
        age = int(age)
        if age <= 0:
            raise ValueError("Age must be a positive integer!")
    except ValueError as e:
        flash(f"Invalid age: {e}", "error")
        return redirect(url_for('users.index'))

    try:
        if User.email_exists(email):
            flash("Email already exists!", "error")
            return redirect(url_for('users.index'))

        User.create(name=name, email=email, age=age)
        flash("User added successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "error")

    return redirect(url_for('users.index'))

@user_blueprint.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        age = request.form.get('age')

        # Validate inputs
        if not name or not email or not age:
            flash("All fields are required!", "error")
            return redirect(url_for('users.update_user', user_id=user_id))

        if not email.count("@") or not email.count("."):
            flash("Invalid email format!", "error")
            return redirect(url_for('users.update_user', user_id=user_id))

        try:
            age = int(age)
            if age <= 0:
                raise ValueError("Age must be a positive integer!")
        except ValueError as e:
            flash(f"Invalid age: {e}", "error")
            return redirect(url_for('users.update_user', user_id=user_id))

        try:
            if User.email_exists(email) and not User.is_email_for_user(user_id, email):
                flash("Email already exists!", "error")
                return redirect(url_for('users.update_user', user_id=user_id))

            User.update(user_id=user_id, name=name, email=email, age=age)
            flash("User updated successfully!", "success")
        except Exception as e:
            flash(f"Error: {e}", "error")

        return redirect(url_for('users.index'))

    user = User.get_by_id(user_id)
    if not user:
        flash("User not found!", "error")
        return redirect(url_for('users.index'))

    return render_template('user.html', user=user, editing=True)

@user_blueprint.route('/delete/<int:user_id>')
def delete_user(user_id):
    try:
        if not User.id_exists(user_id):
            flash("User ID does not exist!", "error")
            return redirect(url_for('users.index'))

        User.remove(user_id)
        flash("User deleted successfully!", "success")
    except Exception as e:
        flash(f"Error: {e}", "error")
    return redirect(url_for('users.index'))
