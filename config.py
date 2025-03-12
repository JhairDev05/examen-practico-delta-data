from dotenv import load_dotenv
import os

load_dotenv()

sqlite = os.getenv('SQLite', 'sqlite:///creditos.db')
secret_key = os.getenv('secret_key', 'palabraSuperSecreta')