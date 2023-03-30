from flask_sqlalchemy import SQLAlchemy
import re

db = SQLAlchemy()


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)