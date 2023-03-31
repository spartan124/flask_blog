from ..utils import db
from flask_login import UserMixin
from ..models import roles_users
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__= 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    date_added = db.Column(db.DateTime, default=datetime.now())
    roles = db.relationship('Role', secondary=roles_users,
    backref=db.backref('users'), lazy='dynamic')
