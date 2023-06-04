from typing import Tuple
import aiohttp
from settings.config import START_BOT_URL, MY_LOGGER, TOKEN, GET_SETTINGS_URL


async def start_bot_post_request(tlg_id, tlg_username, telephone, first_name, last_name, language_code):
    """
    POST запрос при старте бота.
    """
    async with aiohttp.ClientSession() as session:
        data = {
            'tlg_id': int(tlg_id),
            'tlg_username': tlg_username,
            'telephone': telephone,
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
                MY_LOGGER.success(f'Успешный GET запрос для получения настроек по ключу {setting_key!r}')
            else:
                MY_LOGGER.warning(f'Неудачный GET запрос для получения настроек по ключу {setting_key!r}')
            return response.status, await response.json()
