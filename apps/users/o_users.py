from apps.users import dm_users
from flask import redirect, session, jsonify
from apps.users.a_schemas import UserSchema
from server.connection import update
from functools import wraps
from apps.logs import o_logs


def user_active_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' in session:
            user = dm_users.get_user_by_email(session['username'])
            if user.status:
                return func(*args, **kwargs)
        return redirect("/")
    return wrapper


def get_all_users_jsonify():
    user_db = dm_users.get_all_users()
    schema_user = UserSchema(many=True)
    user = schema_user.dump(user_db).data
    return jsonify(user)


def get_user_by_session_jsonify():
    user_db = dm_users.get_user_by_email(session['username'])
    user_schema = UserSchema()
    user = user_schema.dump(user_db).data
    return jsonify({'user': user})


@update
def update_user_by_id(user_form):
    old = dm_users.get_user_by_id(user_form['id'])
    old.email = user_form['email']
    old.first_name = user_form['first_name']
    old.last_name = user_form['last_name']
    old.position = user_form['position']
    old.department = user_form['department']
    o_logs.register_new_log("users", f"Użytkownik {session['username']} edytował użytkownika {old.email}")
    return old


@update
def deactivate_user(user_id):
    try:
        user = dm_users.get_user_by_id(user_id)
        user.status = False
        o_logs.register_new_log("users", f"Użytkownik {session['username']} dezaktywował użytkownika {user.email}")
        return True
    except Exception:
        return False


@update
def activate_user(user_id):
    try:
        user = dm_users.get_user_by_id(user_id)
        user.status = True
        o_logs.register_new_log("users", f"Użytkownik {session['username']} aktywował użytkownika {user.email}")
        return True
    except Exception:
        return False


def add_admin_user(form):
    form.email.data = 'test@test.pl'
    form.first_name.data = 'Admin'
    form.last_name.data = 'Administrator'
    try:
        dm_users.add_new_user(form)
        return True
    except Exception:
        return False


