import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "database/pickJourney.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False