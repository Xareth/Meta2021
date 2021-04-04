from apps.users import dm_login, dm_users, m_users
from server.connection import update
from apps.logs import o_logs
from flask import session, redirect, jsonify
from functools import wraps


def verify_login(data):
    try:
        user = dm_users.get_user_by_email(data[0]['value'])
        result = dm_login.verify_password(data[1]['value'], user.password)
        if result:
            o_logs.register_new_log("login", f"Użytkownik {user.email} poprawnie zalogował się do systemu")
            return result
        o_logs.register_new_log("login", f"Użytkownik {user.email} podał złe hasło")
        return False
    except Exception:
        o_logs.register_new_log("login", f"Ktoś próbował zalogować się do systemu przy użyciu maila: {data[0]['value']}")
        return False


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' in session:
            print("user name in sessions")
            return func(*args, **kwargs)
        print("user name NOT in sessions")
        return "nice"
    return wrapper


@update
def change_password_by_form(password_form, user):
    try:
        user = dm_users.get_user_by_email(user)
        old_password = dm_login.verify_password(password_form.old_password.data, user.password)
        if password_form.new_password.data == password_form.new_password2.data and old_password:
            user.password = dm_login.hash_password(password_form.new_password.data)
            o_logs.register_new_log("login", f"Udało się zmienić hasło użytkownika {user.email}")
            return True
        o_logs.register_new_log("login", f"Użytkownik {user.email} podał złe dane podczas zmiany hasła. Stare hasło, "
        f"bądź niepoprawnie potwierdził nowe hasło")
        return False
    except Exception:
        o_logs.register_new_log("login", f"Wystąpił błąd podczas zmiany hasła użytkownika {user.email}")
        return False


def serialize_login_form():
    form = jsonify({"form": m_users.login_form()})
    return form
