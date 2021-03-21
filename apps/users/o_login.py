from apps.users import dm_login, dm_users
from server.connection import update
from apps.logs import o_logs
from flask import session, redirect
from functools import wraps


def verify_login(data):
    try:
        user = dm_users.get_user_by_email(data['email'])
        result = dm_login.verify_password(data['password'], user.password)
        if result:
            o_logs.register_new_log("login", f"Użytkownik {user.email} poprawnie zalogował się do systemu")
            return result
        o_logs.register_new_log("login", f"Użytkownik {user.email} podał złe hasło")
        return False
    except Exception:
        o_logs.register_new_log("login", f"Ktoś próbował zalogować się do systemu przy użyciu maila: {data['email']}")
        return False


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' in session:
            return func(*args, **kwargs)
        return redirect("/login")
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
