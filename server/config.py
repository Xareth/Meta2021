from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_marshmallow import Marshmallow

app = Flask(__name__, template_folder="../frontend-react/build", static_folder="../frontend-react/build/static")

app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'sdjashljqww!@3123123es5rtdsff'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:1234@127.0.0.1:5433/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)
