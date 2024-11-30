from os import getenv
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

DATABASE_HOST = getenv('DATABASE_HOST')
DATABASE_NAME = getenv('DATABASE_NAME')
DATABASE_USER = getenv('DATABASE_USER')
DATABASE_PASS = getenv('DATABASE_PASS')

DATABASE_URL = 'postgresql+asyncpg://{user}:{passw}@{host}/{name}'.format(
    user=DATABASE_USER,
    passw=DATABASE_PASS,
    host=DATABASE_HOST,
    name=DATABASE_NAME
)

ROOT_LOGIN = getenv('ROOT_LOGIN')
ROOT_PASSWORD = getenv('ROOT_PASSWORD')

SECRET_KEY = getenv('SECRET_KEY')

TG_API_ID = int(getenv('TG_API_ID'))
TG_API_HASH = getenv('TG_API_HASH')

APP_URL = getenv('APP_URL')
APP_TITLE = getenv('APP_TITLE')

ADMIN_LIST = getenv('ADMIN_LIST').split(',')
WORDS_LIST_ID = getenv('WORDS_LIST_ID')
STOP_WORDS_LIST_ID = getenv('STOP_WORDS_LIST_ID')
