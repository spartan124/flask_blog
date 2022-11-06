from wtforms import Form, StringField, TextAreaField, BooleanField, PasswordField, ValidationError, validators, SubmitField
from flask_wtf import FlaskForm
from models import *
from app import *
from views import *

class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')


class RegisterForm(FlaskForm):
    firstname = StringField([validators.Length(min=4, max=25)],
                            render_kw={"placeholder": "First name"})
    lastname = StringField([validators.Length(min=4, max=25)],
                            render_kw={"placeholder": "Last name"})
    username = StringField([validators.Length(min=4, max=25)],
                            render_kw={"placeholder": "Username"})
    email = StringField([validators.Length(min=6, max=35)], render_kw={"placeholder": "Email address"})
    password = PasswordField([validators.DataRequired(), validators.EqualTo
    ('confirm', message='Passwords must match')], render_kw=
                            {"placeholder": "Password"})
    confirm = PasswordField(render_kw={"placeholder": "Repeat Password"})
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_name = User.query.filter_by(
            username=username.data).first()
        if existing_user_name:
            raise ValidationError(
            "That username already exists. Please choose a different one."
            )
class LoginForm(FlaskForm):
    email = StringField([validators.Length(min=6, max=35)],
    render_kw={"placeholder": "Email address"})

    password = PasswordField([validators.DataRequired(), validators.EqualTo
    ('confirm', message='Passwords must match')], render_kw= {"placeholder": "Password"})

    submit = SubmitField("Login")
