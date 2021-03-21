from server.config import app
from flask import render_template, request, redirect, jsonify, url_for
from models.m_users import RegistrationForm
from data_manager import dm_users, dm_privileges, dm_logs
from operations import o_users, o_privileges, o_logs
from operations.o_login import login_required


@app.route("/logs")
def route_logs():
    logs = o_logs.get_log_list()
    return render_template("logs/logs-list.html", logs=logs)
