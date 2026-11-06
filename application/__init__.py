import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    os.makedirs(app.instance_path, exist_ok=True)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(app.instance_path, "todo.sqlite"),
    )

    db.init_app(app)

    from .views import bp
    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()

    return app
