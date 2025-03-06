from dotenv import load_dotenv
import os

load_dotenv()

sqlite = os.environ['SQLite']
secret_key = os.environ['secret_key']