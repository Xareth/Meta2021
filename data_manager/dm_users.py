from models.m_users import User
from data_manager.connection import add, update
from data_manager import dm_login
from datetime import datetime


def jsonify_user(user_db):
    user = {}
    user['id'] = user_db.id
    user['date_created'] = user_db.date_created
    user['date_modified'] = user_db.date_modified
    user['status'] = user_db.status
    user['email'] = user_db.email
    user['first_name'] = user_db.first_name
    user['last_name'] = user_db.last_name
    user['department'] = user_db.department
    user['position'] = user_db.position
    user['avatar'] = user_db.avatar
    return user


def get_all_users():
    users = User.query.all()
    return users


@add
def add_new_user(user_form):
    new_user = User(
        email=user_form.email.data,
        first_name=user_form.first_name.data,
        last_name=user_form.last_name.data,
        department=user_form.department.data,
        position=user_form.position.data,
        status=True,
        password=dm_login.hash_password('1234'),
        avatar=''
    )
    return new_user


def get_user_by_id_json(user_id):
    user_db = User.query.filter_by(id=user_id).first()
    user = jsonify_user(user_db)
    return user


def get_user_by_id(user_id):
    user = User.query.filter_by(id=int(user_id)).first()
    return user


def get_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    return user





