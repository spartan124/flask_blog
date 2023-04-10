from flask_login import login_user, logout_user
from ..models import User
from ..forms import RegisterForm, LoginForm
from ..utils import db, save_to_db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, redirect, url_for, flash


auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            #Hash the password
            hashed_password = generate_password_hash(form.password_hash.data, "sha256")
            new_user = User(
                firstname=form.firstname.data, 
                lastname=form.lastname.data,
                username=form.username.data, 
                email=form.email.data, 
                password_hash=hashed_password
            )
            save_to_db(new_user)
            

        firstname = form.firstname.data
        form.firstname.data = ''
        form.lastname.data = ''
        form.username.data = ''
        form.email.data = ''
        form.password_hash.data = ''

        flash("User Added Successfully!")

    our_users = User.query.order_by(User.date_added)
    redirect(url_for('auth.login'))
    return render_template('register.html', form=form, our_users=our_users)

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                flash("Login Successfull!!!")
                return redirect(url_for('posts.posts_list'))
            else:
                flash("Wrong Password - Try Again...")
        else:
            flash("User Doesn't Exist! Try Again...")


                # return redirect(url_for('posts.posts_list'))
    return render_template('login.html', form=form)

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("You Have Been Logged Out! Thanks For Dropping By....")
    return redirect(url_for('auth.login'))

