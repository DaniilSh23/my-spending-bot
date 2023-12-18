from typing import Tuple
import aiohttp
from settings.config import START_BOT_URL, MY_LOGGER, TOKEN, GET_SETTINGS_URL, GET_DAY_SPENDING_URL, \
    GET_MONTH_SPENDING_URL, GET_AVERAGE_SPENDING_URL


async def start_bot_post_request(tlg_id, tlg_username, first_name, last_name, language_code):
    """
    POST запрос при старте бота.
    """
    async with aiohttp.ClientSession() as session:
        data = {
            'tlg_id': int(tlg_id),
            'tlg_username': tlg_username,
            'first_name': first_name,
            'last_name': last_name,
            'language_code': language_code,
            'api_token': TOKEN,
        }
        async with session.post(url=START_BOT_URL, data=data) as response:
            if response.status == 200:
                MY_LOGGER.success(f'Успешный POST запрос при старте бота')
                return 200
            elif response.status == 400:
                MY_LOGGER.warning(f'Неудачный запрос при старте бота. Код 400')
                return 400
            else:
                MY_LOGGER.warning(f'Вообще хз, что тут произошло ещё.')
                return response.status


async def get_settings(setting_key: str) -> Tuple[int, dict]:
    """
    POST запрос для получения какой-либо настройки из БД
    :param setting_key: str - ключ настройки
    :return: str
    """
    data = {
        "key": setting_key,
        "api_token": TOKEN,
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url=f"{GET_SETTINGS_URL}", data=data) as response:
            if response.status == 200:
                MY_LOGGER.success(f'Успешный POST запрос для получения настроек по ключу {setting_key!r}')
            else:
                MY_LOGGER.warning(f'Неудачный POST запрос для получения настроек по ключу {setting_key!r} | '
                                  f'Ответ: {response.text}')
            return response.status, await response.json()


async def get_day_spending(tlg_id: str) -> Tuple[int, dict]:
    """
    GET запрос для получения трат за текущий день
    :param tlg_id: TG ID юзера
    :return: (int, dict) - (статус код, данные)
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url=f'{GET_DAY_SPENDING_URL}?tlg_id={tlg_id}') as response:
            if response.status == 200:
                MY_LOGGER.success(f'Успешный GET запрос для получения трат за день юзера {tlg_id!r}')
            else:
                MY_LOGGER.warning(f'Неудачный GET запрос для получения трат за день юзера {tlg_id!r}')
            return response.status, await response.json()


async def get_month_spending(tlg_id: str) -> Tuple[int, dict]:
    """
    GET запрос для получения трат за текущий месяц
    :param tlg_id: TG ID юзера
    :return: (int, dict) - (статус код, данные)
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url=f'{GET_MONTH_SPENDING_URL}?tlg_id={tlg_id}') as response:
            if response.status == 200:
                MY_LOGGER.success(f'Успешный GET запрос для получения трат за месяц юзера {tlg_id!r}')
            else:
                MY_LOGGER.warning(f'Неудачный GET запрос для получения трат за месяц юзера {tlg_id!r}')
            return response.status, await response.json()


async def get_average_spending(tlg_id: str) -> Tuple[int, dict]:
    """
    GET запрос для получения средней суммы трат по категориям
    :param tlg_id: TG ID юзера
    :return: (int, dict) - (статус код, данные)
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url=f'{GET_AVERAGE_SPENDING_URL}?tlg_id={tlg_id}') as response:
            if response.status == 200:
                MY_LOGGER.success(f'Успешный GET запрос для получения средней суммы трат по категориям | '
                                  f'tlg_id == {tlg_id!r}')
            else:
                MY_LOGGER.warning(f'Неудачный GET запрос для получения средней суммы трат по категориям | '
                                  f'tlg_id == {tlg_id!r}')
            return response.status, await response.json()
