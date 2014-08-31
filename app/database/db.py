from flask.ext.sqlalchemy import SQLAlchemy
from redis import Redis

db = SQLAlchemy()
redis = Redis(db=5)