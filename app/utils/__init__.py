from flask_sqlalchemy import SQLAlchemy
import re

db = SQLAlchemy()


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)

def save_to_db(self):
    db.session.add(self)
    db.session.commit()