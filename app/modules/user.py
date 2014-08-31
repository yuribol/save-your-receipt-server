import random

from app.database import db
from app.models import User

class ModuleUser:

    @classmethod
    def user_sign_in(cls, username, password):

        user = db.session.query(User).filter(User.username == username).first()

        if user is None:
            return False

        if user.password == cls._create_password(user.salt, password):
            # login successful, generate token
            token = cls._generate_token()
            return True, token, user.id

        return False

    @classmethod
    def _create_password(cls, salt, password):
        return salt + password

    @classmethod
    def _generate_token(cls):
        return random.randint(0, 1000)