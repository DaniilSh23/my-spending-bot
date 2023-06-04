import asyncio

import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message

from client_work import client_work
from filters.bot_filters import bot_manager_filter
from keyboards.bot_keyboards import ADMIN_KBRD, make_headpage_keyboard
from settings.config import WORKING_CLIENTS, MY_LOGGER, ADMIN_LOGIN, ADMIN_PASS
from utils.req_to_project_api import check_user_id, get_settings


@Client.on_message(filters.command('start'))
async def start_handler(client: pyrogram.Client, update: Message):
    """
    Хэндлер для команды start
    """
    MY_LOGGER.debug(f'Проверяем наличие tlg_id в БД')
    check_usr_rslt = await check_user_id(
        tlg_id=update.from_user.id,
        tlg_username=update.from_user.username if update.from_user.username else None
    )

    MY_LOGGER.debug(f'Получаем список админов')
    get_adm_status, admins_lst = await get_settings(setting_key='bot_admin')
    if get_adm_status != 200:
        MY_LOGGER.error(f'Не удалось получить список админов. Ответ: {get_adm_status, admins_lst}')
    else:
        MY_LOGGER.debug(f'Список админов получен.')

    if check_usr_rslt[0] not in (201, 200):
        MY_LOGGER.error(f'У бота что-то неисправно. Поломка при проверке юзера. '
                        f'Результат функции check_user_id={check_usr_rslt}')
        await update.reply_text(text=f'🚧 У бота что-то неисправно...\n'
                                     f'👌 Мы уже решаем эту проблему, скоро всё будет ок.')

        if get_adm_status == 200:
            MY_LOGGER.debug(f'Отправляем уведомления админам о неисправности бота')
            for i_admin_id in admins_lst.get("result"):
                await client.send_message(
                    text=f'🛰Хьюстон, у нас проблема‼️\nУ бота что-то неисправно. Поломка при проверке юзера. '
                         f'Результат функции check_user_id={check_usr_rslt}',
                    chat_id=int(i_admin_id),
                )
            return

    # Обработка для нового пользователя
    elif check_usr_rslt[0] == 201:
        MY_LOGGER.debug(f'Новый пользователь с tlg_id == {update.from_user.id}')
        msg_for_pin = await update.reply(
            text=f'🎉<b>Рад, что Вы с нами!</b>\n'
                 f'📆Новым пользователям доступен <b>бесплатный период</b> {check_usr_rslt[1].get("trial_days")} дней.'
        )
        await msg_for_pin.pin(both_sides=True)

    # Отправляем клавиатуру главного меню
    await update.reply_text(
        text=f'🗣️ <b>First Word Bot</b>\n'
             f'🥇 <i><b>"Первый должен быть лучшим"</b> - золотое правило Олимпийских игр</i>\n\n'
             f'💬 Этот бот позволит Вам <b>первым автоматически оставлять лучший комментарий</b> '
             f'под новым постом в канале.\n\n🔝 А как это использовать ? Дело за Вами.\n'
             f'📣 Кажется, это может быть хорошим инструментом, чтобы заявить о чём-либо.\n\n'
             f'👩🏼‍🏫 Подробнее в инструкции.',
        reply_markup=await make_headpage_keyboard(tlg_id=update.from_user.id)
    )

    # Кнопка для входа в админку для админов
    if get_adm_status == 200 and str(update.from_user.id) in admins_lst.get("result"):
        MY_LOGGER.debug(f'Отправляем админу клавиатуру для входа в админку')
        await update.reply_text(
            text=f'Данные для входа в админку: <code>{ADMIN_LOGIN}</code> | <code>{ADMIN_PASS}<code>',
            reply_markup=ADMIN_KBRD
        )


@Client.on_message(filters.command('start_client') & filters.private & bot_manager_filter)
async def start_thread_with_client(_, update):
    """
    Хэндлер для старта нового потока с клиентом аккаунта телеграм.
    Акк, управляющий ботом должен отправить /start_thread <имя сессии>
    """
    session_name = update.text.split()[1]
    MY_LOGGER.debug(f'Получен апдейт для старта клиента {session_name!r}')

    # Получаем текущий eventloop, создаём task
    loop = asyncio.get_event_loop()
    task = loop.create_task(client_work(session_name))

    # Флаг остановки таска
    stop_flag = asyncio.Event()

    # Запись таска и флага в общий словарь (флаг пока опущен)
    WORKING_CLIENTS[session_name] = [stop_flag, task]


@Client.on_message(filters.command('stop_client'))
async def stop_client(client, update):
    """
    Хэндлер для остановки клиента по его имени сессии
    """
    session_name = update.text.split()[1]
    MY_LOGGER.debug(f'Получен апдейт по остановке клиента {session_name!r}')

    # Поднимаем стоп-флаг для остановки таска
    stop_flag = WORKING_CLIENTS[session_name][0]
    WORKING_CLIENTS[session_name][0] = stop_flag.set()

    # Ожидаем завершения таска клиента (там в словаре лежит объект таска)
    await WORKING_CLIENTS[session_name][1]

    # Удаляем клиент из общего списка
    WORKING_CLIENTS.pop(session_name)
    MY_LOGGER.success(f'Клиент {session_name!r} успешно остановлен')


@Client.on_message()
async def test_handler(client, update):
    """
    Получаем апдейты
    """
    # MY_LOGGER.debug(f'Получен апдейт в тестовом хэндлере')
    # MY_LOGGER.debug(update)
