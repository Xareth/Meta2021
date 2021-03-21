from server.config import app
from flask import render_template, request, session, redirect
from models.m_users import LoginForm, User
from models.m_privileges import Privilege
from operations import o_login, o_logs
from data_manager import dm_users, dm_privileges
from data_manager.connection import update
from server.config import db


@update
def add_privilege_to_role(role_id, privilege_id):
    role = dm_privileges.get_role_by_id(role_id)
    privilege = dm_privileges.get_privilege_by_id(privilege_id)
    role.privileges.append(privilege)
    o_logs.register_new_log("privileges", f"Użytkownik {session['username']} dodał uprawnienie {privilege.name}"
    f" do roli {role.name}")
    return role


@update
def remove_privilege_from_role(role_id, privilege_id):
    role = dm_privileges.get_role_by_id(role_id)
    privilege = dm_privileges.get_privilege_by_id(privilege_id)
    role.privileges.remove(privilege)
    o_logs.register_new_log("privileges", f"Użytkownik {session['username']} odebrał uprawnienie {privilege.name} "
    f"z roli {role.name}")
    return role


@update
def add_role_to_user(user_id, role_id):
    user = dm_users.get_user_by_id(user_id)
    role = dm_privileges.get_role_by_id(role_id)
    user.roles.append(role)
    o_logs.register_new_log("privileges", f"Użytkownik {session['username']} dodał rolę {role.name} do użytkownika "
    f"{user.email}")
    return role


@update
def remove_role_from_user(user_id, role_id):
    user = dm_users.get_user_by_id(user_id)
    role = dm_privileges.get_role_by_id(role_id)
    user.roles.remove(role)
    o_logs.register_new_log("privileges", f"Użytkownik {session['username']} usunął rolę {role.name} od użytkownika "
    f"{user.email}")
    return role


def get_all_roles():
    roles = dm_privileges.get_all_roles()
    return roles


def get_role_by_id(role_id):
    role = dm_privileges.get_role_by_id(role_id)
    return role


def add_new_role(name):
    dm_privileges.add_new_role(name)
    o_logs.register_new_log("privileges", f"Użytkownik {session['username']} dodał nową rolę do systemu")


def get_all_privileges():
    privileges = dm_privileges.get_all_privileges()
    return privileges


