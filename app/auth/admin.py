from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user
from flask import redirect, url_for, request

class AdminMixin:
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login',
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
