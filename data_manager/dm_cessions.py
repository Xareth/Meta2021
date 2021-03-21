from models.m_cessions import Cession
from flask import session
from data_manager.connection import add
from data_manager import dm_general, dm_users
from datetime import date


def get_all_cessions():
    cessions = Cession.query.all()
    return cessions


def get_cession_by_id(cession_id):
    cession = Cession.query.filter_by(id=cession_id).first()
    return cession


@add
def add_cession(form):
    sub_departments = compare_form_strings_with_sql_departments(form)
    seller = dm_users.get_user_by_email(session['username'])
    buyer = compare_form_strings_with_sql_users(form)
    new_cession = Cession(
        status=True,
        seller_sub_department=sub_departments['seller_sub_department'],
        buyer_sub_department=sub_departments['buyer_sub_department'],
        seller_user_id=seller.id,
        buyer_user_id=buyer['buyer'],
        vin=form['vin'],
        seller_description=form['seller_description'],
        seller_identification=form['seller_identification'],
        stage='NOWA CESJA',
        value_goods=(int(form['value_goods']) if form['value_goods'] != '' else 0),
        value_services=(int(form['value_services']) if form['value_services'] != '' else 0),
        value_outsourcing=(int(form['value_outsourcing']) if form['value_outsourcing'] != '' else 0),
        user_id_created=seller.id
    )
    return new_cession


def compare_form_strings_with_sql_departments(form):
    new_form = {}
    sub_departments = dm_general.get_all_sub_departments()
    for sub_department in sub_departments:
        if form['seller_sub_department'] == str(sub_department):
            new_form['seller_sub_department'] = sub_department.id
        if form['buyer_sub_department'] == str(sub_department):
            new_form['buyer_sub_department'] = sub_department.id
    return new_form


def compare_form_strings_with_sql_users(form):
    new_form = {}
    users = dm_users.get_all_users()
    for user in users:
        if form['buyer'] == str(user):
            new_form['buyer'] = user.id
    return new_form
