from flask import Blueprint
from ..models.user import User

api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/')
def home():
    return 'home'


@api_bp.route('/user/<name>')
def create_user(name):
    user = User.query.filter_by(username=name).first()

    return {'user': user}
    # return 'just name!'
