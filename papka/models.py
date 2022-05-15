from flask_login import UserMixin 
from papka import db, manager
from datetime import datetime


class Prodagi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazvanie = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Prodagi %r>' % self.id


class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)


@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)