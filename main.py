from flask import Flask
from routes.creditos import creditos_bp
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
from config import sqlite, secret_key

# 🔹 Primero creamos la instancia de Flask
app = Flask(__name__)

# 🔹 Configuramos la base de datos
app.secret_key = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = sqlite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 🔹 Inicializamos la base de datos
db.init_app(app)

# 🔹 Registramos los Blueprints
app.register_blueprint(creditos_bp)

# 🔹 Evitamos la importación circular asegurándonos de ejecutar esto solo si es el script principal
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
