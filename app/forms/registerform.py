from wtforms import StringField, PasswordField, ValidationError, SubmitField
from wtforms.validators import DataRequired, EqualTo
from flask_wtf import FlaskForm
from ..models import User

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
