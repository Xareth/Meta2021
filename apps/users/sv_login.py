from server.config import app
from flask import render_template, request, session, redirect, jsonify
from apps.logs import o_logs
from apps.users import o_login
from apps.users.o_login import login_required


@app.route("/_login", methods=['GET'])
def route_login_form():
    form = o_login.serialize_login_form()
    return form


@app.route("/_login", methods=['POST'])
def route_login_post():
    if request.method == "POST":
        print(request.json)

    else:
        print("get detected")
    return jsonify({"route": "/_login"})
