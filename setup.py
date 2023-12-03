from extensions import db
from app import create_app
from users.models import *

app = create_app()
with app.app_context():
    db.create_all()
