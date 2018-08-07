import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////{}'.format(os.path.join(os.getenv('HOME'), 'Desktop/blog/instance/blog.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Th3_g0d5--dR1nk_ruM'
