from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

curr_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(curr_dir, "../db.env"))

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

USE_SQLITE = False


def create_app():
    """
    Application Factory
    https://flask.palletsprojects.com/en/2.3.x/tutorial/factory/
    """
    app = Flask(__name__)

    if USE_SQLITE:
        app.config["SECRET_KEY"] = "secret-key-goes-here"
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    else:
        app.config["SECRET_KEY"] = os.getenv("POSTGRES_PASSWORD")
        app.config[
            "SQLALCHEMY_DATABASE_URI"
        ] = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@pgsql:5432/{os.getenv('POSTGRES_DB')}"

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    migrate = Migrate(app, db)

    from .models import User

    # Specify the user loader
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
