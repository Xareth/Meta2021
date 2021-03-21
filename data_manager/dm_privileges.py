from models.m_privileges import Privilege, Role
from models.m_users import User
from data_manager.connection import add
from data_manager import dm_users
from server.config import db
from operations import o_logs
from flask import session


def get_all_privileges():
    privileges = Privilege.query.all()
    return privileges


def get_privilege_by_id(privilege_id):
    privilege = Privilege.query.filter_by(id=int(privilege_id)).first()
    return privilege


@add
def add_new_privilege(name):
    new_privilege = Privilege(
        name = name
    )
    o_logs.register_new_log("Privileges", f"Użytkownik {session['username']} dodał nowe uprawnienie do systemu: {name}")
    return new_privilege


def get_all_roles():
    roles = Role.query.all()
    return roles


def get_role_by_id(id):
    role = Role.query.filter_by(id=id).first()
    return role


@add
def add_new_role(name):
    new_role = Role(
        name = name
    )
    o_logs.register_new_log("Privileges", f"Użytkownik {session['username']} dodał nową rolę do systemu: {name}")
    return new_role


# todo function does not work
def get_all_privileges_by_user(user_id):
    user = dm_users.get_user_by_id(user_id)
    users_privileges = db.session.query(Privilege).outerjoin(Privilege.user_id)
    return users_privileges

