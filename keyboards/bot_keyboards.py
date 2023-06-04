from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from keyboards.bot_buttons import BUTTONS_DCT
from settings.config import STATISTIC_LINK, SUBSCRIPTION_LINK


async def make_headpage_keyboard(tlg_id):
    """
    Функция, которая делает клавиатуру для главного меню.
    Подставляет в кнопки WebApp tlg_id юзера и возвращает объект клавиатуры
    :param tlg_id: str - ID телеграмма
    :return:
    """
    return InlineKeyboardMarkup([
        [
            BUTTONS_DCT['MY_ACCS'],
            BUTTONS_DCT['MY_CHANNELS'],
        ],
        [
            BUTTONS_DCT['INSTRUCTION'],
        ],
        [
            InlineKeyboardButton(
                text=f'📊 Статистика',
                web_app=WebAppInfo(url=f'{STATISTIC_LINK}?tlg_id={tlg_id}')
            ),
            BUTTONS_DCT['SUPPORT'],
        ],
        [
            InlineKeyboardButton(
                text=f'🗞 Подписка',
                web_app=WebAppInfo(url=f'{SUBSCRIPTION_LINK}?tlg_id={tlg_id}')
            ),
        ],
    ])


ADMIN_KBRD = InlineKeyboardMarkup([
    [
        BUTTONS_DCT['ADMIN_PANEL']
    ],
])


# НИЖЕ ВСЁ СТАРОЕ

CANCEL_AND_CLEAR_STATE_KBRD = InlineKeyboardMarkup([
    [
        BUTTONS_DCT['CANCEL_AND_CLEAR_STATE'],
    ],
])

BACK_TO_HEAD_PAGE_KBRD = InlineKeyboardMarkup([
    [
        BUTTONS_DCT['BACK_TO_HEAD_PAGE'],
    ],
])
