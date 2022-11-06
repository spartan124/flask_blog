from flask import render_template
from flask import request, url_for, redirect
from posts.blueprint import *
from posts.forms import *

from app import *
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

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
        if bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('posts.posts_list'))
            if current_user.is_authenticated:
                return redirect(url_for('posts.posts_list'))
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect_url(url_for('login'))

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(firstname=form.firstname.data, lastname=form.lastname.data,
        username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
