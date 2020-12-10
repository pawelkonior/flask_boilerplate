import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
from flask_migrate import Migrate


from logging import DEBUG

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()
# login_manager = LoginManager()


def create_app():
    app = Flask(__name__, template_folder=os.path.join(basedir, 'app', 'templates'))

    app.config.from_object("project.config.Config")

    from project.app.views import main_bp

    app.register_blueprint(main_bp)

    db.init_app(app)

    # login_manager.session_protection = 'strong'
    # login_manager.login_view = 'login'
    # login_manager.init_app(app)

    app.logger.setLevel(DEBUG)
    
    Migrate(app, db)

    return app
