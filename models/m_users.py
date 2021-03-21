from server.config import db
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Email
from datetime import datetime
from models.m_privileges import role_user
from models.m_logs import Log
from server.config import db, ma


def user_choices():
    return User.query


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
    status = db.Column(db.Boolean)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(30), unique=False, nullable=False)
    last_name = db.Column(db.String(30), unique=False, nullable=False)
    position = db.Column(db.String(50))
    avatar = db.Column(db.String(120))
    password = db.Column(db.String(120))
    role_id = db.relationship("Role",
                              secondary=role_user, backref="users", lazy="dynamic")
    logs = db.relationship("Log", backref="ex_users")

    def __repr__(self):
        return f'Użytkownik {self.first_name} {self.last_name}'


class RegistrationForm(FlaskForm):
    id = IntegerField('ID')
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    first_name = StringField('Imię', validators=[DataRequired()])
    last_name = StringField('Nazwisko', validators=[DataRequired()])
    position = StringField('Stanowisko', validators=[DataRequired()])
    submit = SubmitField('Dodaj', id='submit_add_user')


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj', id='submit_login')


class ChangePasswordForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    old_password = PasswordField('Stare hasło', validators=[DataRequired()])
    new_password = PasswordField('Nowe hasło', validators=[DataRequired()])
    new_password2 = PasswordField('Potwierdź nowe hasło', validators=[DataRequired()])
    submit = SubmitField('Zmień hasło', id='submit_password_change')
