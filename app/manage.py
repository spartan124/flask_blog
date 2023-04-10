from app import create_app
from .utils import db
from flask_script import Manager

app = create_app()

manager = Manager(app, db)


if __name__=='__main__':
    manager.run()
