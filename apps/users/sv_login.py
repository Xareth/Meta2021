from server.config import app
from flask import render_template, request, session, redirect
from apps.users.m_users import LoginForm, ChangePasswordForm
from apps.logs import o_logs
from apps.users import o_login
from apps.users.o_login import login_required


@app.route("/login", methods=['GET', 'POST'])
def route_login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        form_data = request.form
        result = o_login.verify_login(form_data)
        if result:
            session['username'] = request.form['email']
            return redirect("/")
        return redirect("/login")
    return render_template("users/login-form.html", login_form=login_form)


@app.route("/logout")
@login_required
def route_logout():
    o_logs.register_new_log("login", f"Użytkownik {session['username']} poprawnie wylogował się z systemu")
    session.clear()
    return redirect("/")


@app.route("/change-password", methods=['GET', 'POST'])
@login_required
def route_change_password():
    form = ChangePasswordForm()
    user = session['username']
    if request.method == 'POST':
        result = o_login.change_password_by_form(form, user)
        return redirect("/")
    return render_template("users/password-change.html", form=form, user=user)
