from models.m_logs import Log
from models.m_users import User
from data_manager.connection import add
from flask import session
from server.config import db


@add
def add_new_log(category, message, username=None):
    new_log = Log(
        category=category,
        message=message,
        ex_users=username
    )
    return new_log


def get_log_by_unique(unique):
    log = Log.query.filter_by(unique_code=unique).first()
    return log


def get_all_log():
    logs = Log.query.all()
    return logs
