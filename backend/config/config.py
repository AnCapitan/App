from dotenv import load_dotenv
import os
load_dotenv()

BINANCE_API = os.environ.get('BINANCE_API')
BINANCE_SECRET_KEY = os.environ.get('BINANCE_SECRET_KEY')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
POSTGRES_NAME = os.environ.get('POSTGRES_NAME')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')