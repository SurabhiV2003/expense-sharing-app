from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')


    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import api
    app.register_blueprint(api, url_prefix='/api')


    return app

