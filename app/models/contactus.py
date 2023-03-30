from ..utils import db
from datetime import datetime


class ContactUs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text)
    created_on = db.Column(db.DateTime, default=datetime.now())
    slug = db.Column(db.String(140), unique=True)