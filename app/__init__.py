from flask import Flask
import os

from flask_bootstrap import Bootstrap

def create_app(config_filename=None):
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_pyfile(config_filename)
    register_blueprints(application)
    Bootstrap(application)
    return application

def register_blueprints(application):
    from app.controllers import user_blueprints
    application.register_blueprint(user_blueprints)


