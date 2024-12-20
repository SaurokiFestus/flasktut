from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager #manages all login related things

db = SQLAlchemy()
DB_NAME= 'test.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'H'
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    # db = SQLAlchemy(app)

    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view ='auth.login' #redirects when user not logged in
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #get looks for primary key

    return app

def create_database(app):
    if not path.exists('website1/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created db!')

    pass