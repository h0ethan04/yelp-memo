from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    yelp = db.relationship('Yelp')

class Yelp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
