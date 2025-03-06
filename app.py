from flask import Flask
from routes.creditos import creditos_bp
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
from config import sqlite, secret_key

app = Flask(__name__)

app.secret_key = secret_key

app.config['SQLALCHEMY_DATABASE_URI'] = sqlite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(creditos_bp)