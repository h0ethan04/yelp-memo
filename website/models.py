from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    note = db.relationship('Note')

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    img = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Numeric(scale=1), nullable=False)
    business_id = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(500), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
