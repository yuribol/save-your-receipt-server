import datetime

from app.database.db import db


class Budget(db.Model):
    __tablename__ = "budget"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    limit = db.Column(db.Float, nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    status = db.Column(db.Integer)