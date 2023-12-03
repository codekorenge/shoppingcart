from flask import *
from .models.user import User
from extensions import db

user_bp = Blueprint('user',
                    __name__,
                    template_folder='templates',
                    static_folder='static')


# @user_bp.route('/')
# def get_user():
#     return 'hello user here'
#
# #
@user_bp.route('/', methods=['POST'])
def create_user():
    if request.method == 'POST':
        # Parse form data
        user = User()
        user.username = request.form['username']
        user.password = request.form['password']
        user.email= request.form['email']
        user.phone = request.form['phone']
        db.session.add(user)
        db.session.commit()

    return 'CREATED!'


# /users?name=roberto
@user_bp.route('/')
def get_user():
    find = request.args.get('name')
    found = User.query.filter_by(username=find).first()

    return {'users': found}
