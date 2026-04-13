# Add any model classes for Flask-SQLAlchemy here
from . import db

from werkzeug.security import generate_password_hash

class lab5(db.Model):

    __tablename__ = 'lab5'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(255))
    poster = db.Column(db.String(100))
    #created_at (date time)