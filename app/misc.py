import os
from json import dump, load

from loguru import logger
from dotenv import load_dotenv

logger.add('log/debug.log', level='DEBUG',
           format='{time} {level} {message}', rotation='10 KB', compression='zip')

dotenv_path = '.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

URL = 'https://www.securitylab.ru/news/'
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
USER_ID = os.getenv('USER_ID')


def write_json(data):
    with open('news.json', 'w', encoding='utf-8') as f:
        dump(data, f, indent=2, ensure_ascii=False)


def read_json():
    with open('news.json', encoding='utf-8') as f:
        return load(f)
