from server.config import app
from flask import render_template, request, session, redirect
from apps.logs import o_logs
from apps.users import o_login
from apps.users.o_login import login_required


@app.route("/_users")
def route_login_form():
    form = o_login.serialize_login_form()
    print(form)
    return form
