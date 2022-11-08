from wtforms import Form, StringField, TextAreaField, BooleanField, PasswordField, ValidationError, validators, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length
from flask_wtf import FlaskForm
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField
from models import *
from app import *
from views import *

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = CKEditorField('Body', validators=[DataRequired()])
    author = StringField('Author')
    submit = SubmitField("Post")


class RegisterForm(FlaskForm):
    firstname = StringField("First Name", validators=[DataRequired()])
    lastname = StringField("Last Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password_hash = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords Must Match!')])
    confirm =  PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_name = User.query.filter_by(
            username=username.data).first()
        if existing_user_name:
            raise ValidationError(
            "That username already exists. Please choose a different one."
            )
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])

    password = PasswordField("Password", validators=[DataRequired()])

    submit = SubmitField("Login")

class PasswordForm(FlaskForm):
	email = StringField("What's Your Email", validators=[DataRequired()])
	password_hash = PasswordField("What's Your Password", validators=[DataRequired()])
	submit = SubmitField("Submit")
