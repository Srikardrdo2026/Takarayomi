import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{os.getenv('db_user')}:{os.getenv('db_password')}@{os.getenv('db_host')}:{os.getenv('db_port')}/{os.getenv('db_name')}"
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "fallbacksecret")
