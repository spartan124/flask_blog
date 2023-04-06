from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user
from flask import redirect, url_for, request
from ..models import User, Post

class AdminMixin:
    def is_accessible(self):
        return current_user.is_authenticated 

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login',
                                next=request.url))


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    
    def is_visible(self):
        return current_user.is_authenticated

    def _get_num_users(self):
        return User.query.count()

    def _get_num_posts(self):
        return Post.query.count()

    def _get_num_users_html(self):
        num_users = self._get_num_users()
        return f'<a href="{url_for("admin.index", url="/admin/user")}"><strong>{num_users}</strong> registered users</a>'

    def _get_num_posts_html(self):
        num_posts = self._get_num_posts()
        return f'<a href="{url_for("admin.index", url="/admin/post")}"><strong>{num_posts}</strong> posts</a>'

    
    def render(self, template, **kwargs):
        # Get the number of registered users and posts
        num_users_html = self._get_num_users_html()
        num_posts_html = self._get_num_posts_html()

        # Get the links to edit and delete posts
        posts = Post.query.all()
        
        return super().render(template, num_users_html=num_users_html,
                               num_posts_html=num_posts_html, **kwargs)


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
