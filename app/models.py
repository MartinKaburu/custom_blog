from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class BlogPosts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    subtitle = db.Column(db.String(256), nullable=False)
    author = db.Column(db.String(32), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)


class Administrator(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(32), unique = True, nullable = False)
    username = db.Column(db.String(32), unique = True, nullable = False)
    password = db.Column(db.String(256), nullable = False)
    isadmin = db.Column(db.Boolean, default=False)

