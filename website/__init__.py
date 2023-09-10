from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
from flask_login import LoginManager
from config import app_key

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = app_key
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Yelp

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        """ Tells flask how we get the user (grabs the primary key of user)"""
        return User.query.get(int(id))
    
    return app


def create_database(app: Flask):
    """ creates database with the categories listed in models.py"""
    db_path = Path('website/' + DB_NAME)
    if not db_path.exists():
        with app.app_context():
            db.create_all()