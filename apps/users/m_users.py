from server.config import db
from datetime import datetime
from apps.logs.m_logs import Log
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
    logs = db.relationship("Log", backref="ex_users")

    def __repr__(self):
        return f'Użytkownik {self.first_name} {self.last_name}'


def user_form():
    user_form = [
        {
            "label": "Email",
            "type": "email",
            "placeholder": "np. test@test.pl"
        },
        {
            "label": "Nazwisko",
            "type": "name",
            "placeholder": "np. Kowalski"
        }
    ]

    return user_form
