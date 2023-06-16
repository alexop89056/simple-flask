import os
from pathlib import Path

path = Path(__file__).parent.absolute()

SECRET_KEY = os.urandom(12)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f'sqlite:///{path}/db/main.db'
SESSION_FILE_DIR = f'{path}/sessions'
SESSION_PERMANENT = False
SESSION_TYPE = 'filesystem'
DEBUG = True
USERS_PER_PAGE = 10
