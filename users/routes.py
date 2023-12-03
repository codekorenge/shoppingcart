from flask import *
from .models.user import User

user_bp = Blueprint('user',
                    __name__,
                    template_folder='templates',
                    static_folder='static')


@user_bp.route('/users', methods=['POST'])
def create_user():
    if request.method == 'POST':
        # Parse form data
        users = User()
        users.username = request.form['username']
        users.password = request.form['password']
        users.email= request.form['email']
        users.phone = request.form['phone']

    return 'CREATED!'


# /users?name=roberto
@user_bp.route('/users')
def get_user():
    find = request.args.get('name')
    found = User.query.filter_by(username=find).first()

    return {'users': found}
