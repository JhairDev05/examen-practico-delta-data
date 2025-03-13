import sys
import os

# Obtiene la ruta del entorno virtual
venv_path = os.path.join(os.path.dirname(__file__), "venv", "Lib", "site-packages")

# Agrega la ruta de las librerías del entorno virtual a sys.path
sys.path.insert(0, venv_path)

# Define las variables que estás intentando importar
sqlite = "sqlite:///database.db"  # O la ruta que necesites para tu base de datos SQLite
secret_key = "tu_clave_secreta_aqui"  # Reemplaza con una clave secreta segura