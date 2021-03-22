from apps.users import dm_users
from flask import redirect, session, jsonify
from apps.users.a_schemas import UserSchema
from server.connection import update
from functools import wraps
from apps.logs import o_logs
from apps.users import m_users


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


def serialize_user_form():
    user_form = m_users.user_form()
    return jsonify(user_form)
def serialize_user_form():
    user_form = m_users.user_form()
    return jsonify(user_form)
