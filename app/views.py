from flask import render_template, request, url_for, redirect, flash
from posts.blueprint import *
from posts.forms import *

from app import *

from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def index():
    q = request.args.get('q')

    if q:
        posts = Post.query.filter(Post.title.contains(q) |
        Post.body.contains(q))
    else:
        posts = Post.query.order_by(Post.created.desc())

    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    pages = posts.paginate(page=page, per_page=1)

    return render_template('posts/posts.html', posts=posts,
    pages=pages)


@app.route('/login', methods=['GET','POST'])
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

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("You Have Been Logged Out! Thanks For Dropping By....")
    return redirect(url_for('login'))

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            #Hash the password
            hashed_password = generate_password_hash(form.password_hash.data, "sha256")
            new_user = User(firstname=form.firstname.data, lastname=form.lastname.data,
            username=form.username.data, email=form.email.data, password_hash=hashed_password)
            db.session.add(new_user)
            db.session.commit()

        firstname = form.firstname.data
        form.firstname.data = ''
        form.lastname.data = ''
        form.username.data = ''
        form.email.data = ''
        form.password_hash.data = ''

        flash("User Added Successfully!")

    our_users = User.query.order_by(User.date_added)
    return render_template('register.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
