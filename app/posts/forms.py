from wtforms import Form, StringField, TextAreaField, BooleanField, PasswordField, ValidationError, validators, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length
from flask_wtf import FlaskForm
from wtforms.widgets import TextArea
# from flask_ckeditor import CKEditorField
from ..models import User

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
    # author = StringField('Author')
    submit = SubmitField("Post")


class ContactForm(FlaskForm):
    fullname = StringField('Full Name', validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send Message")


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
    def validate_email(self, email):
        existing_email= User.query.filter_by(
        email=email.data).first()
        if existing_email:
            raise ValidationError("That email already exists. Log in or use a different email ")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])

    password = PasswordField("Password", validators=[DataRequired()])

    submit = SubmitField("Login")

class PasswordForm(FlaskForm):
	email = StringField("What's Your Email", validators=[DataRequired()])
	password_hash = PasswordField("What's Your Password", validators=[DataRequired()])
	submit = SubmitField("Submit")
