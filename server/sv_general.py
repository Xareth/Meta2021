from server.config import app, db
from flask import render_template, request, session, redirect, jsonify
from models.m_users import User


@app.route('/')
@app.route("/home")
def route_main():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return "404"

