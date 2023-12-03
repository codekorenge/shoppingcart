from flask import Flask

from extensions import db
from main.routes import main_bp
from users.routes import user_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp, url_prefix='/users')

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
