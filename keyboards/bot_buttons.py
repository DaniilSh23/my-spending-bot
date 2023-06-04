from pyrogram.types import InlineKeyboardButton, WebAppInfo

from settings.config import BASE_HOST_URL, WRITE_SPENDING_LINK

BUTTONS_DCT = {
    'ADMIN_PANEL': InlineKeyboardButton(
        text=f'⌨️Админ-панель',
        url=f'{BASE_HOST_URL}admin/'
    ),
    'WRITE_SPENDING': InlineKeyboardButton(
        text=f'🖋 Записать расходы',
        web_app=WebAppInfo(url=WRITE_SPENDING_LINK)
    ),
}
