from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])

    password = PasswordField("Password", validators=[DataRequired()])

    submit = SubmitField("Login")