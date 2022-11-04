from flask import render_template
from flask import request
from posts.blueprint import *

from app import app


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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
