from server.config import app
from flask import render_template, request, redirect, jsonify
from apps.users import o_users, dm_users
from apps.users.o_login import login_required


@app.route("/login")
def route_get_all_users():
    user = o_users.get_all_users_jsonify()
    user2 = o_users.serialize_user_form()
    return user2


@app.route("/_get-user")
def route_get_current_user():
    user = o_users.get_user_by_session_jsonify()
    return user
