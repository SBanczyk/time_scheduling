from flask import Flask
from .views import views
from .auth import auth
from .models import create_database


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "sajdasljdlaskjaskldj"
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_database()

    @app.route("/")
    def home():
        return "Hello, Flask with SQLite!"

    return app
