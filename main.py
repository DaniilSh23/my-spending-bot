import time

import uvloop
from pyrogram import Client
from loguru import logger

from settings.config import WORKING_CLIENTS

if __name__ == '__main__':
    logger.debug('Запускаем бота')
    plugins = dict(
        root="handlers",
        include=["bot_handlers"]
    )  # Создаём плагины с хэндлерами

    uvloop.install()  # Это для ускорения работы бота

    try:
        Client("test_bot", plugins=plugins).run()
        # Client("work_bot", plugins=plugins).run()

    except Exception as error:
        logger.error(f'BOT CRASHED WITH SOME ERROR\n\t{error}')

        # Остановка запущенных клиентов
        for i_key, i_value in WORKING_CLIENTS.items():
            i_value[0].set()    # Устанавливаем флаг для остановки клиентов
            logger.debug(f'Флаг остановки клиента для {i_key} == {i_value[0].is_set()}')
        logger.debug('Ждём 5 сек для завершения всех тасков')
        time.sleep(5)
        logger.debug(f'Все таски завершены')

    except (KeyboardInterrupt, SystemExit):
        logger.warning('BOT STOPPED BY CTRL+C!')

        # Остановка запущенных клиентов
        for i_key, i_value in WORKING_CLIENTS.items():
            i_value[0].set()    # Устанавливаем флаг для остановки клиентов
            logger.debug(f'Флаг остановки клиента для {i_key} == {i_value[0].is_set()}. Ожидаем завершения таска')
        logger.debug('Ждём 5 сек для завершения всех тасков')
        time.sleep(5)
        logger.debug(f'Все таски завершены')

    # TODO: дописать обработку сигналов
