from server.config import app
from flask import render_template, request, redirect, jsonify
from apps.users import o_users, dm_users
from apps.users.o_login import login_required


@app.route("/users")
def route_get_all_users():
    users = o_users.serialize_user_form()
    return users
