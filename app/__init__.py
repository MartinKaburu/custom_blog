from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

@app.errorhandler(404)
def not_found(error):
    return render_template('404/404.html'), 404

from . import utils, views, models
app.register_blueprint(views.bp)

