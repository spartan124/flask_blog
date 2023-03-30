from flask import Flask
from flask import redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView

from flask_security import SQLAlchemyUserDatastore, Security
from flask_security import RoleMixin
from flask_login import LoginManager
from flask_login import UserMixin, login_user, login_required, logout_user, current_user
# from flask_ckeditor import CKEditor

from config import Config



app = Flask(__name__)
# ckeditor = CKEditor(app)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SECRET_KEY']='afkjasdfjnnfjhdfjjkfbs'

db = SQLAlchemy(app)

from models import *


migrate = Migrate(app, db)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)

#flask_login
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view="login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class AdminMixin:
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login',
        next=request.url))


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass

class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        if is_created:
            model.generate_slug()
        return super().on_model_change(form, model,
         is_created)
class PostAdminView(AdminMixin, BaseModelView):
    form_columns = ['title', 'body', 'tags']

class TagAdminView(AdminMixin, BaseModelView):
    pass
class UserAdminView(AdminMixin, BaseModelView):
    pass
class ContactAdminView(AdminMixin, BaseModelView):
    pass
class RoleAdminView(AdminMixin, BaseModelView):
    pass
admin = Admin(app, 'Blogify', url='/',
index_view=HomeAdminView(name='Home'))


admin.add_view(PostAdminView(Post, db.session))
admin.add_view(TagAdminView(Tag, db.session))
admin.add_view(ContactAdminView(ContactUs, db.session))
admin.add_view(UserAdminView(User, db.session))
admin.add_view(RoleAdminView(Role, db.session))


#Flask-Security
# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security(app, user_datastore)
