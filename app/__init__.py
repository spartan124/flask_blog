from auth import (ContactAdminView, HomeAdminView, PostAdminView,
                  RoleAdminView, TagAdminView, UserAdminView)
from config.config import config_dict
from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager
from flask_migrate import Migrate
from models import ContactUs, Post, Role, Tag, User
from utils import db


def create_app(config=config_dict['dev']):
    app = Flask(__name__)
    
    db.init_app(app)
    
    migrate = Migrate(app, db)
    
    login_manager = LoginManager(app)
    login_manager.init_app(app)
    login_manager.login_view="login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get_or_404(int(user_id))
    
    admin = Admin(app, 'Blogify', url='/',
    index_view=HomeAdminView(name='Home'))


    admin.add_view(PostAdminView(Post, db.session))
    admin.add_view(TagAdminView(Tag, db.session))
    admin.add_view(ContactAdminView(ContactUs, db.session))
    admin.add_view(UserAdminView(User, db.session))
    admin.add_view(RoleAdminView(Role, db.session))

    return app


    
    
