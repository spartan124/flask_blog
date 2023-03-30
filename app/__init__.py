from flask import Flask
from config.config import config_dict
from utils import db
from flask_migrate import Migrate
from flask_login import LoginManager

def create_app(config=config_dict['dev']):
    app = Flask(__name__)
    
    db.init_app(app)
    
    migrate = Migrate(app, db)
    
    login_manager = LoginManager(app)
    login_manager.init_app(app)
    login_manager.login_view="login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    
    
