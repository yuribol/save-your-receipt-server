import json
from functools import wraps

from flask import request, make_response, jsonify

from app.database import redis
from app.modules.user import ModuleUser

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "token" in request.args:
            user_id = redis.get(request.args["token"])
            if user_id is not None:
                kwargs["user_id"] = user_id
                return f(*args, **kwargs)

        request_data = json.loads(request.data)
        if "username" in request_data and "password" in request_data:
            sign_in_success, token, user_id = ModuleUser.user_sign_in(username=request_data["username"], 
                                                                      password=request_data["password"])

            result = {"error": 0}
            if sign_in_success:
                if token and user_id:
                    redis.set(token, user_id) 
                    result = {"token": token}

            return make_response(jsonify(result))
        else:
            return make_response(jsonify({"error": 0}, 400))

        return f(*args, **kwargs)

    return wrapper
