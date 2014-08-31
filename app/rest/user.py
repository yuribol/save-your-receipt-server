from flask import Blueprint, jsonify, current_app

from app.models import User
from app.database.db import db
from app.ext import login_required

class BlueprintUser:
    bp = Blueprint("user", __name__)
    bp_prefix = "/user"

    @staticmethod
    @bp.route("/sign-in", methods=["POST"])
    @login_required
    def user_sign_in(user_id=None):
        print db.session.query(User).filter().all()
        print "Hello world! ", user_id
        return jsonify({"token": "redisgeneratedtoken"})

    @staticmethod
    @bp.route("/sign-up", methods=["GET"])
    @login_required
    def user_sign_up():
        print db.session.query(User).filter().all()
        print "Hello world!"
        return jsonify({"hello": "world!"})