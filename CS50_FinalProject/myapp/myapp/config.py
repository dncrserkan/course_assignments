import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')       # Change
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') # Change
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')    # Change
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')    # Change
