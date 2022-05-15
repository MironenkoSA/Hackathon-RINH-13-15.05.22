from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql://localhost/hacknight'
app.config['SQLALCHEMY_DATABASE_URL'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)


from papka import models, routes


db.create_all()