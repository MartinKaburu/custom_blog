from app import app, login_manager, db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_migrate import Migrate
from datetime import datetime as dt


class BlogPosts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    subtitle = db.Column(db.String(256), nullable=False)
    author = db.Column(db.String(32), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __init__(self,title, subtitle, author, date_posted, content):
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.date_posted = date_posted
        self.content = content

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def __repr__():
        return "title:<{}>".format(self.title)


class Administrator(db.Model):
    #__table__ = 'administrators'
    userid = db.Column('userid', db.Integer, primary_key = True)
    email = db.Column('email', db.String(32), unique = True, nullable = False, index=True)
    username = db.Column('username', db.String(32), unique = True, nullable = False, index=True)
    password = db.Column('password', db.String(256), nullable = False)
    reg_date = db.Column('reg_date', db.DateTime)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.reg_date = dt.now()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.userid)

    def __repr__(self):
        return '<User %r>' % (self.username)

@login_manager.user_loader
def load_user(id):
    return Administrator.query.get(int(id))
