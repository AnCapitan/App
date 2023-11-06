from dotenv import load_dotenv
import os
load_dotenv()
SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = os.environ.get('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES'))

BINANCE_API = os.environ.get('BINANCE_API')
BINANCE_SECRET_KEY = os.environ.get('BINANCE_SECRET_KEY')

VK_ID_API=os.environ.get('VK_ID_API')
VK_SECRET_KEY=os.environ.get('VK_SECRET_KEY')
VK_SERVICE_KEY=os.environ.get('VK_SERVICE_KEY')

POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
POSTGRES_NAME = os.environ.get('POSTGRES_NAME')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')