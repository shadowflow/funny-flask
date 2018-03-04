from flask import Flask
from db_model import *
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)
db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    # db.drop_all()
    db.create_all()
