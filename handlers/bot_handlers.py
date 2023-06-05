import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message

from keyboards.bot_keyboards import ADMIN_KBRD, WRITE_SPENDING_KBRD
from settings.config import MY_LOGGER, ADMIN_LOGIN, ADMIN_PASS
from utils.req_to_project_api import start_bot_post_request, get_settings


@Client.on_message(filters.command('start'))
async def start_handler(client: pyrogram.Client, update: Message):
    """
    Хэндлер для команды start
    """
    MY_LOGGER.debug(f'Кидаем стартовый запрос к апи')
    start_req_rslt = await start_bot_post_request(
        tlg_id=update.from_user.id,
        tlg_username=update.from_user.username if update.from_user.username else None,
        telephone=update.from_user.username if update.from_user.username else None,
        first_name=update.from_user.first_name if update.from_user.first_name else None,
        last_name=update.from_user.last_name if update.from_user.last_name else None,
        language_code=update.from_user.language_code if update.from_user.language_code else None,
    )

    MY_LOGGER.debug(f'Получаем список админов')
    get_adm_status, admins_lst = await get_settings(setting_key='bot_admin')
    if get_adm_status != 200:
        MY_LOGGER.error(f'Не удалось получить список админов. Ответ: {get_adm_status, admins_lst}')
    else:
        MY_LOGGER.debug(f'Список админов получен.')

    if start_req_rslt != 200:
        MY_LOGGER.error(f'У бота что-то неисправно. Поломка при стартовом запросе к апи. Статус код={start_req_rslt}')
        await update.reply_text(text=f'🚧 У бота что-то неисправно...\n'
                                     f'👌 Мы уже решаем эту проблему, скоро всё будет ок.')

        if get_adm_status == 200:
            MY_LOGGER.debug(f'Отправляем уведомления админам о неисправности бота')
            for i_admin_id in admins_lst.get("result"):
                await client.send_message(
                    text=f'🛰Хьюстон, у нас проблема‼️\nУ бота что-то неисправно. Поломка при стартовом запросе. '
                         f'Статус код={start_req_rslt}',
                    chat_id=int(i_admin_id),
                )
            return

    # Отправляем клавиатуру главного меню
    await update.reply_text(
        text=f'👇 Жми на кнопку ниже, чтобы <b>внести сумму трат</b>',
        reply_markup=WRITE_SPENDING_KBRD,
    )

    # Кнопка для входа в админку для админов
    if get_adm_status == 200 and str(update.from_user.id) in admins_lst.get("result"):
        MY_LOGGER.debug(f'Отправляем админу клавиатуру для входа в админку')
        await update.reply_text(
            text=f'Данные для входа в админку: <code>{ADMIN_LOGIN}</code> | <code>{ADMIN_PASS}</code>',
            reply_markup=ADMIN_KBRD
        )


@Client.on_message()
async def test_handler(client, update):
    """
    Получаем апдейты
    """
    # MY_LOGGER.debug(f'Получен апдейт в тестовом хэндлере')
    # MY_LOGGER.debug(update)
