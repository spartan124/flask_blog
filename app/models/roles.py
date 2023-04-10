from ..utils import db, slugify
from time import time
from flask_security import RoleMixin


roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer,
                       db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer,
                       db.ForeignKey('role.id'))
                      )

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug = self.generate_slug()
    def generate_slug(self):
        if self.name:
            self.slug = slugify(self.name)
        else:
            self.slug =str(int(time()))
            