from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from .routes import users, posts, comments, todos, albums, photos
        app.register_blueprint(users.bp)
        app.register_blueprint(posts.bp)
        app.register_blueprint(comments.bp)
        app.register_blueprint(todos.bp)
        app.register_blueprint(albums.bp)
        app.register_blueprint(photos.bp)

    return app
