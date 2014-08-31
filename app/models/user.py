import datetime

from app.database.db import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    salt = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    status = db.Column(db.Integer)