from flask import Blueprint, jsonify, current_app

from app.models import User
from app.database.db import db

class ReceiptBlueprint:
    bp = Blueprint("receipt", __name__)
    bp_prefix = "/receipt"

    @staticmethod
    @bp.route("/add", methods=["GET"])
    def add_receipt():
        print db.session.query(User).filter().all()
        print "Hello world!"
        return jsonify({"hello": "world!"})