from server.config import app
from flask import render_template
from apps.logs import o_logs


@app.route("/logs")
def route_logs():
    logs = o_logs.get_log_list()
    return render_template("logs/logs-list.html", logs=logs)
