import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'instance/messages.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Email settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'stacyjuma018@gmail.com'         # <-- Change this
    MAIL_PASSWORD = 'nlfiqfhsoyvkfijp'       # <-- Use App Password, NOT real one
    MAIL_DEFAULT_SENDER = 'stacyjuma018@gmail.com'
