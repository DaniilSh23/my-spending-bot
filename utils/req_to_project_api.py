from typing import Tuple

import aiohttp

from settings.config import CHECK_USER_URL, MY_LOGGER, TOKEN, GET_SETTINGS_URL


async def check_user_id(tlg_id, tlg_username):
    """
    POST запрос для проверки пользователя в системе.

    Принимает параметры:
        token - TOKEN бота, необходим для идентификации оригинального запроса
        tlg_id - ID пользователя в телеграме
        tlg_username - username пользователя в телеграме

    Значения статус кодов:
        200 - юзер найден в системе,
        201 - юзер новый и был создан в системе,
        400 - неверный запрос, стоит также проверить параметры запроса

    Возвращает (пример):
        status_code 201 - {"created": True, "trial_days": 5}
        status_code 200 - {"created": False, "trial_days": 5}
        status_code 400 - {"result": "description of errors"}
    """
    async with aiohttp.ClientSession() as session:
        data = {
            'token': TOKEN,
            'tlg_id': int(tlg_id),
            'tlg_username': tlg_username,
        }
        async with session.post(url=CHECK_USER_URL, data=data) as response:
            if response.status == 200:
                MY_LOGGER.success(f'Успешный POST запрос. Юзер с tlg_id == {tlg_id} НАЙДЕН в системе. Код 200')
                return 200, await response.json()
            elif response.status == 201:
                MY_LOGGER.success(f'Успешный POST запрос. Юзер с tlg_id == {tlg_id} СОЗДАН в системе. Код 201')
                return 201, await response.json()
            elif response.status == 400:
                MY_LOGGER.warning(f'Неудачный запрос для проверки юзера с tlg_id == {tlg_id}. Код 400')
                return 400, await response.json()
            else:
                MY_LOGGER.warning(f'Вообще хз, что тут произошло ещё.')
                return response.status, {'result': 'unexpected error'}


async def get_settings(setting_key: str) -> Tuple[int, dict]:
    """
    GET запрос для получения какой-либо настройки из БД
    :param setting_key: str - ключ настройки
    :return: str
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url=f"{GET_SETTINGS_URL}?key={setting_key}") as response:
            if response.status == 200:
                MY_LOGGER.success(f'Успешный GET запрос для получения настроек по ключу {setting_key!r}')
            else:
                MY_LOGGER.warning(f'Неудачный GET запрос для получения настроек по ключу {setting_key!r}')
            return response.status, await response.json()
