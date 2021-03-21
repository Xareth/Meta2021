from server.config import app
from flask import render_template, request, redirect, jsonify, url_for
from models.m_users import RegistrationForm
from data_manager import dm_users
from operations import o_users
from operations.o_login import login_required
from operations.o_users import user_active_required


@app.route("/users", methods=['GET', 'POST'])
@login_required
def route_users():
    form = RegistrationForm()
    users = dm_users.get_all_users()
    if request.method == 'POST':
        dm_users.add_new_user(form)
        return redirect('/users')
    return render_template("users/users-list.html", form=form, users=users)


@app.route("/deactivate-user/<id>")
@login_required
def route_deactivate_user(id):
    result = o_users.deactivate_user(id)
    if result:
        return redirect("/users")
    return redirect("/users")


@app.route("/activate-user/<id>")
@login_required
def route_activate_user(id):
    result = o_users.activate_user(id)
    if result:
        return redirect("/users")
    return redirect("/users")


@app.route("/_get_edit_user")
@login_required
def route_get_edit_user():
    user_id = request.args.get('row_id')
    user = dm_users.get_user_by_id_json(user_id)
    return jsonify(result=user)


@app.route("/_update_user")
@login_required
def route_update_user():
    form = request.args.to_dict()
    o_users.update_user_by_id(form)
    return redirect("/users")


@app.route("/admin-create")
def route_create_admin_account():
    form = RegistrationForm()
    o_users.add_admin_user(form)
    return redirect("/")


@app.route("/_get-all-users")
def route_get_all_users():
    user = o_users.get_all_users_jsonify()
    return user


@app.route("/_get-user")
def route_get_current_user():
    user = o_users.get_user_by_session_jsonify()
    return user
