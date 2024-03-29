from flask import Blueprint, redirect, flash, render_template, request, url_for
from flask_login import login_required, current_user

from ..forms import PostForm
from ..models import *
from ..utils import db, save_to_db

posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/create', methods=['POST', 'GET'])
@login_required
def post_create():
    form = PostForm()

    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')

        try:
            post = Post(title=title, body=body)
            save_to_db(post)
        except:
            print('Very long traceback error')
        return redirect(url_for('posts.post_detail',
        slug=post.slug))


    return render_template('posts/post_create.html', form=form)



#localhost:5000/blog/
@posts.route('/')
def posts_list():
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

@posts.route( '/<slug>' )
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first_or_404()
    return render_template('posts/post_detail.html', post=post)


@posts.route('/tags/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first_or_404()
    return render_template('posts/tag_detail.html', tag=tag)

@posts.route('/<slug>/edit', methods=['POST', 'GET'])
@login_required
def post_update(slug):
    post = Post.query.filter(Post.slug==slug).first_or_404()

    if request.method =='POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()
        return redirect(url_for('posts.post_detail',
        slug=post.slug))
    form = PostForm(obj=post)
    return render_template('posts/edit.html', post=post,
    form=form)

# @posts.route('/<int:id>/edit', methods=['GET', 'POST'])
# @login_required
# def edit_post(id):
#     post = Post.query.get_or_404(id)
#     if post.author.username != current_user:
#         flash('You are not authorized to edit this post', 'danger')
#         return redirect(url_for('posts.post', id=post.id))
#     form = PostForm(obj=post)
#     if form.validate_on_submit():
#         form.populate_obj(post)
#         db.session.commit()
#         flash('Your post has been updated', 'success')
#         return redirect(url_for('posts.post', id=post.id))
#     return render_template('edit_post.html', form=form, post=post)