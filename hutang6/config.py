import os

class Config:
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/utang_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
