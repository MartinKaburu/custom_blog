import smtplib
from . import app
from flask import render_template, url_for, request, redirect, Blueprint, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import  generate_password_hash
from datetime import datetime as dt
from app.models import BlogPosts, db, Administrator
from app.utils import sendmail
from app.forms import LoginForm


@app.route('/')
def index():
    posts = BlogPosts.query.order_by(BlogPosts.date_posted.desc()).all()
    return render_template('index.html', posts=posts)
@app.route('/older')
def older():
    flash("[-] No older Posts")
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    post = BlogPosts.query.filter_by(id=post_id).first_or_404()
    #alternatively use .first_or_404() instead of .first() to return a 404 error if not found instead of None
    return render_template('post.html', post=post)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method is 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        sendmail(name, email, phone, message)

        redirect(url_for('index'))
    else:
        return render_template('contact.html')

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/add')
@login_required
def add():
    return render_template('add.html')

@bp.route('/addpost', methods = ['POST'])
@login_required
def addpost():
    title = request.form.get('title')
    subtitle = request.form.get('subtitle')
    author = request.form.get('author')
    date_posted = dt.now()
    content = request.form.get('content')
    post = BlogPosts(title, subtitle, author, dt.now(), content)
    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = Administrator.query.filter_by(email=email, password=password).first()
        if user is None:
            flash("Invalid email or password", 'error')
            return redirect(url_for('index'))
        else:
            login_user(user)
            flash('Logged in successfully')
            return redirect(request.args.get('next') or url_for('admin.add'))
    else:
        return render_template('login.html', form=form)

@bp.route('/remove')
@login_required
def remove():
    posts = BlogPosts.query.order_by(BlogPosts.date_posted.desc()).all()
    return render_template('remove.html', posts=posts)

@bp.route('/delete<int:post_id>')
@login_required
def delete(post_id):
    post = BlogPosts.query.filter_by(id=post_id).first()
    flash("Post: ::deleted successfully")
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
