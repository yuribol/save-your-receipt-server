import datetime

from app.database.db import db


class BudgetUser(db.Model):
    __tablename__ = "budget_user"

    id = db.Column(db.Integer, primary_key=True)
    budget_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
