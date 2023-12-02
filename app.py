from flask import Flask

app = Flask(__name__)


# app.config['SECRET_KEY'] = 'thisisasecretkey'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#
# db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return 'welcome'


if __name__ == "__main__":
    app.run(debug=True)