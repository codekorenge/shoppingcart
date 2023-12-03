from flask import Flask

from app.extensions import db
from app.routes.api import api_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(api_bp)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
