from .auth import (ContactAdminView, HomeAdminView, PostAdminView,
                  RoleAdminView, TagAdminView, UserAdminView)
from .auth.users import auth
from .config import config_dict
from flask import Flask, render_template
from flask_admin import Admin
from flask_login import LoginManager
from flask_migrate import Migrate
from .models import ContactUs, Post, Role, Tag, User
from .utils import db
from flask_restx import Api
from .posts.blueprint import posts
from .resources.pages import pages

def create_app(config=config_dict['dev']):
    app = Flask(__name__)
    app.config.from_object(config)
    
    db.init_app(app)
    
    migrate = Migrate(app, db)
    
    api = Api(app)
    
    login_manager = LoginManager(app)
    login_manager.init_app(app)
    login_manager.login_view="login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get_or_404(int(user_id))
    
    
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html')

    admin = Admin(app, 'Blogify', url='/',
    index_view=HomeAdminView(name='Home'))


    admin.add_view(PostAdminView(Post, db.session))
    admin.add_view(TagAdminView(Tag, db.session))
    admin.add_view(ContactAdminView(ContactUs, db.session))
    admin.add_view(UserAdminView(User, db.session))
    admin.add_view(RoleAdminView(Role, db.session))

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(posts, url_prefix='/blog')
    app.register_blueprint(pages, url_prefix='')
    
    return app


    
    
