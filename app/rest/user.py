from flask import Blueprint, jsonify, current_app

from app.models import User
from app.database.db import db

class UserBlueprint:
    bp = Blueprint("user", __name__)
    bp_prefix = "/user"

    @staticmethod
    @bp.route("/sign-in", methods=["POST"])
    def user_sign_in():
        print db.session.query(User).filter().all()
        print "Hello world!"
        return jsonify({"token": "redisgeneratedtoken"})

    @staticmethod
    @bp.route("/sign-up", methods=["GET"])
    def user_sign_up():
        print db.session.query(User).filter().all()
        print "Hello world!"
        return jsonify({"hello": "world!"})