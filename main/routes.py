from flask import render_template
from flask import Blueprint

main_bp = Blueprint('main',
                    __name__,
                    template_folder='templates',
                    static_folder='static')


@main_bp.route('/')
def home():
    return render_template("home.html")


@main_bp.route('/register')
def register():
    return render_template("register.html")
