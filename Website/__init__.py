from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .models import db, User

db=SQLAlchemy()

login_manager=LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY']='daichamaicha'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    db.init_app(app)

    login_manager.login_view='auth.login_signup'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        from .models import User
        return User.query.get(int(id))

    from .views import views as views_blueprint
    from .auth import auth as auth_blueprint

    app.register_blueprint(views_blueprint,url_prefix='/')  
    app.register_blueprint(auth_blueprint,url_prefix='/')

    with app.app_context():
        db.create_all()   
    
    return app