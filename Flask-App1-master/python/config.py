import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-123')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:666666@localhost/stat'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
