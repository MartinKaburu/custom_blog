from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from config import Config
from flask_script import Manager

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/admin/login'

from . import models, views, utils
app.register_blueprint(views.bp)


@app.errorhandler(404)
def not_found(error):
    return render_template('404/404.html'), 404
