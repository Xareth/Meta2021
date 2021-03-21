from data_manager import dm_logs, dm_users
from flask import session
from models.m_logs import Log
from models.m_users import User
from uuid import uuid1
from data_manager.connection import update
from random import random


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

