from loguru import logger
import os
from dotenv import load_dotenv

WORKING_CLIENTS = dict()    # Словарь для запущенных клиентов
BOT_MANAGER_ID = int(os.environ.get('BOT_MANAGER_ID', 1978587604))    # tlg_id аккаунта, управляющего ботом
MY_LOGGER = logger

load_dotenv()

TOKEN = os.environ.get('TOKEN', 'bot_token')
API_ID = os.environ.get('API_ID', '1234567890')
API_HASH = os.environ.get('API_HASH', 'какой-то там хэш')
ADMIN_LOGIN = os.environ.get('ADMIN_LOGIN', 'admin')
ADMIN_PASS = os.environ.get('ADMIN_PASS', 'admin')

# Константы для API Django проекта
BASE_HOST_URL = os.environ.get('BASE_HOST_URL', 'http://127.0.0.1:8000/')
START_BOT_URL = f'{BASE_HOST_URL}myspending/start_bot/'
GET_SETTINGS_URL = f'{BASE_HOST_URL}myspending/get_settings/'
GET_DAY_SPENDING_URL = f'{BASE_HOST_URL}myspending/get_day_spending/'
GET_MONTH_SPENDING_URL = f'{BASE_HOST_URL}myspending/get_month_spending/'
GET_AVERAGE_SPENDING_URL = f'{BASE_HOST_URL}myspending/average_amount_spent/'

BOT_DEBUG = os.environ.get('BOT_DEBUG', '0')

if BOT_DEBUG == '1':
    WRITE_SPENDING_LINK = 'https://danyasevas11.fvds.ru/myspending/write_spending/'
else:
    WRITE_SPENDING_LINK = f'{BASE_HOST_URL}myspending/write_spending/'

# Хранилища для всякого
MONTH_SPENDING_DATA = dict()    # {tlg_id: data}
