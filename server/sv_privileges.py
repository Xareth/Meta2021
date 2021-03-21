from server.config import app
from flask import render_template, request, session, redirect
from models.m_users import LoginForm
from operations import o_login, o_logs
from operations.o_login import login_required
from data_manager import dm_users, dm_privileges
from operations import o_privileges


@app.route("/privilege/<name>")
@login_required
def route_add_privilege(name):
    dm_privileges.add_new_privilege(name)
    return redirect('/')


@app.route("/roles")
@login_required
def route_roles():
    roles = o_privileges.get_all_roles()
    return render_template("privileges/roles-list.html", roles=roles)


@app.route("/roles/add/<name>")
def route_add_new_role(name):
    o_privileges.add_new_role(name)
    return redirect("/roles")


@app.route("/role/<id>")
def route_role_details(id):
    role = o_privileges.get_role_by_id(id)
    privileges = o_privileges.get_all_privileges()
    return render_template("privileges/role-details.html", role=role, privileges=privileges)


@app.route("/privilege/<role_id>/add/<privilege_id>")
@login_required
def route_add_privilege_to_role(role_id, privilege_id):
    o_privileges.add_privilege_to_role(role_id, privilege_id)
    return redirect(f"/role/{role_id}")


@app.route("/privilege/<role_id>/remove/<privilege_id>")
@login_required
def route_remove_privilege_from_role(role_id, privilege_id):
    o_privileges.remove_privilege_from_role(role_id, privilege_id)
    return redirect(f"/role/{role_id}")


@app.route("/role/<user_id>/add/<role_id>")
def route_add_role_to_user(user_id, role_id):
    o_privileges.add_role_to_user(user_id, role_id)
    return redirect(f"/user-details/{user_id}")


@app.route("/role/<user_id>/remove/<role_id>")
def route_remove_role_from_user(user_id, role_id):
    o_privileges.remove_role_from_user(user_id, role_id)
    return redirect(f"/user-details/{user_id}")

