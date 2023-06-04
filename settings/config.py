from loguru import logger
import os
from dotenv import load_dotenv

WORKING_CLIENTS = dict()    # Словарь для запущенных клиентов
BOT_MANAGER_ID = int(os.environ.get('BOT_MANAGER_ID', 1978587604))    # tlg_id аккаунта, управляющего ботом
MY_LOGGER = logger

load_dotenv()

TOKEN = os.environ.get('TOKEN', '5265303938:AAE1daGp-VJR0R15J9tHksR38hQlbCXMYdU')
API_ID = os.environ.get('API_ID', '1234567890')
API_HASH = os.environ.get('API_HASH', 'какой-то там хэш')
FORM_LINK = os.environ.get('FORM_LINK', 'https://f5cc-78-30-211-223.ngrok-free.app/service_desk_bot/fill_an_app/')
ADMIN_LOGIN = os.environ.get('ADMIN_LOGIN', 'admin')
ADMIN_PASS = os.environ.get('ADMIN_PASS', 'admin')

# Константы для API Django проекта
BASE_HOST_URL = os.environ.get('BASE_HOST_URL', 'http://127.0.0.1:8000/')
START_BOT_URL = f'{BASE_HOST_URL}/myspending/start_bot/'
GET_SETTINGS_URL = f'{BASE_HOST_URL}/myspending/get_settings/'

# TODO: пока на этом заглушка, потому что телега не может найти url адреса
# STATISTIC_LINK = f'{BASE_HOST_URL}/first_word/statistic/'
WRITE_SPENDING_LINK = 'https://yandex.ru'
