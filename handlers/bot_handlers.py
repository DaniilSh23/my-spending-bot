import datetime
from _decimal import Decimal

import pyrogram
import pytz
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery

from filters.bot_filters import get_day_pending_filter
from keyboards.bot_keyboards import ADMIN_KBRD, HEADPAGE_RBRD
from settings.config import MY_LOGGER, ADMIN_LOGIN, ADMIN_PASS
from utils.req_to_project_api import start_bot_post_request, get_settings, get_day_spending


@Client.on_message(filters.command('start'))
async def start_handler(client: pyrogram.Client, update: Message):
    """
    Хэндлер для команды start
    """
    MY_LOGGER.debug(f'Кидаем стартовый запрос к апи')
    start_req_rslt = await start_bot_post_request(
        tlg_id=update.from_user.id,
        tlg_username=update.from_user.username if update.from_user.username else None,
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
        reply_markup=HEADPAGE_RBRD,
    )

    # Кнопка для входа в админку для админов
    if get_adm_status == 200 and str(update.from_user.id) in admins_lst.get("result"):
        MY_LOGGER.debug(f'Отправляем админу клавиатуру для входа в админку')
        await update.reply_text(
            text=f'Данные для входа в админку: <code>{ADMIN_LOGIN}</code> | <code>{ADMIN_PASS}</code>',
            reply_markup=ADMIN_KBRD
        )


@Client.on_callback_query(get_day_pending_filter)
async def get_day_spending_handler(client: pyrogram.Client, update: CallbackQuery):
    """
    Хэндлер для обработки нажатия кнопки получения расходов за день.
    """
    MY_LOGGER.debug(f'Апдейт в хэндлере получения расходов за день от пользователя {update.from_user.id}')
    resp_status, resp_data = await get_day_spending(tlg_id=str(update.from_user.id))

    if resp_status != 200:
        MY_LOGGER.debug(f'Статус-код ответа на запрос о получении расходов за день == {resp_status}')
        await update.edit_message_text(
            text=f'🚧 Неудачный запрос для получения трат за день.\n🛠 У бота что-то сломалось, надо чинить.',
            reply_markup=HEADPAGE_RBRD,
        )
        return

    MY_LOGGER.debug(f'Выполняем подсчёт трат.')
    spend_stat = {'total': 0}
    for i_spend in resp_data:
        categ_name = i_spend.get("category")
        if spend_stat.get(categ_name):
            spend_stat[i_spend.get("category")] += float(i_spend.get("amount"))
        else:
            spend_stat[i_spend.get("category")] = float(i_spend.get("amount"))
        spend_stat["total"] += float(i_spend.get("amount"))

    MY_LOGGER.debug(f'Формируем текст сообщения')
    date_now = datetime.datetime.now(tz=pytz.timezone("Europe/Moscow")).strftime("%d.%m.%Y")
    time_now = datetime.datetime.now(tz=pytz.timezone("Europe/Moscow")).strftime("%H:%M:%S")
    msg_txt = f'💳 <b>Траты за {date_now} по состоянию на {time_now}</b>\n\n'
    for i_categ, i_amount in spend_stat.items():
        if i_categ == 'total':
            msg_txt = ''.join([msg_txt, f'🔹 <b>Всего трат: {Decimal(i_amount).quantize(Decimal("0.01"))} руб.</b>\n\n'])
            continue
        msg_txt = ''.join([msg_txt, f'{i_categ}: {Decimal(i_amount).quantize(Decimal("0.01"))} руб.\n'])

    MY_LOGGER.debug(f'Изменяем сообщение в телеге, вставляя в него текст трат за сегодня')
    await update.edit_message_text(
        text=msg_txt,
        reply_markup=HEADPAGE_RBRD,
    )


@Client.on_message()
async def test_handler(client, update):
    """
    Получаем апдейты
    """
    # MY_LOGGER.debug(f'Получен апдейт в тестовом хэндлере')
    # MY_LOGGER.debug(update)
