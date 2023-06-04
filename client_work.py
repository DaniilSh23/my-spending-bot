from settings.config import WORKING_CLIENTS, MY_LOGGER
import uvloop
from pyrogram import Client


async def client_work(session_name):
    """
    Такс в eventloop'e для одного клиента телеграм
    """
    plugins = dict(
        root="handlers",
        include=[
            "client_handlers",
        ]
    )

    uvloop.install()  # Это для ускорения работы бота

    MY_LOGGER.info(f'Запускаем клиент аккаунта {session_name!r}')
    client = Client(session_name, plugins=plugins)

    MY_LOGGER.debug(f'WORKING_CLIENTS.get(session_name) == {WORKING_CLIENTS.get(session_name)}')
    try:
        await client.start()    # Стартуем клиент аккаунта
        stop_flag = WORKING_CLIENTS.get(session_name)[0]
        MY_LOGGER.success(f'Клиент {session_name!r} успешно запущен!')
        await stop_flag.wait()  # Ожидаем поднятия флага

        MY_LOGGER.warning(f'Стоп флаг был поднят. Останавливаем клиент {session_name!r}')
        await client.stop()  # Останавливаем клиент аккаунт
        return  # Выходим из функции

    except Exception as error:
        MY_LOGGER.error(f'CLIENT {session_name!r} CRASHED WITH SOME ERROR\n\t{error}')
        await client.stop()

    except (KeyboardInterrupt, SystemExit):
        MY_LOGGER.warning(f'CLIENT {session_name!r} STOPPED BY CTRL+C!')
        await client.stop()
