from app import app
from flask import render_template, url_for, request, redirect
from datetime import datetime as dt
from app.models import BlogPosts, db


@app.route('/')
def index():
    posts = BlogPosts.query.order_by(BlogPosts.date_posted.desc()).all()
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    post = BlogPosts.query.filter_by(id=post_id).one()
    return render_template('post.html', post=post)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login/add')
def add():
    return render_template('add.html')

@app.route('/login/addpost', methods = ['GET','POST'])
def addpost():
    title = request.form.get('title')
    subtitle = request.form.get('subtitle')
    author = request.form.get('author')
    date_posted = dt.now()
    content = request.form.get('content')
    post = BlogPosts(title=title, subtitle=subtitle, author=author, date_posted=dt.now(), content=content)
    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))
