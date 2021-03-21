from apps.logs import dm_logs
from apps.users import dm_users
from flask import session


def register_new_log(category, message):
    try:
        user = dm_users.get_user_by_email(session['username'])
    except:
        user = None
    dm_logs.add_new_log(category, message, user)
    return True


def get_log_list():
    logs = dm_logs.get_all_log()
    return logs

