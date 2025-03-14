import sys
import os

venv_path = os.path.join(os.path.dirname(__file__), "venv", "Lib", "site-packages")

sys.path.insert(0, venv_path)

sqlite = "sqlite:///database.db"
secret_key = "tu_clave_secreta_aqui"  