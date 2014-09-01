from flask import Blueprint, jsonify

from app.models import User, Budget, BudgetUser
from app.database.db import db
from app.ext import login_required

class BlueprintBudget:
    bp = Blueprint("budget", __name__)
    bp_prefix = "/budget"

    @staticmethod
    @bp.route("/create", methods=["POST"])
    @login_required
    def budget_create(user_id=None):
        print db.session.query(User).filter().all()
        print "Hello world! ", user_id
        return jsonify({"token": "redisgeneratedtoken"})

    @staticmethod
    @bp.route("/read", methods=["POST"])
    @login_required
    def budget_read(user_id=None):
        print db.session.query(User).filter().all()
        print "Hello world! ", user_id
        return jsonify({"token": "redisgeneratedtoken"})

    @staticmethod
    @bp.route("/update", methods=["POST"])
    @login_required
    def budget_update(user_id=None):
        print db.session.query(User).filter().all()
        print "Hello world! ", user_id
        return jsonify({"token": "redisgeneratedtoken"})

    @staticmethod
    @bp.route("/delete", methods=["GET"])
    @login_required
    def budget_delete():
        print db.session.query(User).filter().all()
        print "Hello world!"
        return jsonify({"hello": "world!"})

    @staticmethod
    @bp.route("", methods=["GET"])
    @login_required
    def budget_get_all(user_id=None):
        budgets = db.session.query(Budget)\
            .join(BudgetUser, BudgetUser.budget_id == Budget.id)\
            .join(User, User.id == BudgetUser.user_id)\
            .filter(User.id == user_id).all()

        res = []

        for budget in budgets:
            res.append({
                "id": budget.id,
                "name": budget.name,
                "limit": budget.limit
            })
        return jsonify({"budgets": res})
