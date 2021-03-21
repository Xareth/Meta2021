from server.config import app
from flask import render_template


@app.route("/nice")
def route_nice():
    html = "<div>nice message</div>"
    return html


@app.route('/')
@app.route("/home")
def route_main():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return "404"
