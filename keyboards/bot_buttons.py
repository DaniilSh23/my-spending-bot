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
    'DAY_SPENDING': InlineKeyboardButton(
        text=f'💸 Траты за день',
        callback_data='get_day_spending'
    ),
    'THIS_MONTH_SPENDING': InlineKeyboardButton(
        text=f'📅 Расходы за этот месяц',
        callback_data='this_month_spending'
    ),
    'LAST_MONTH_SPENDING': InlineKeyboardButton(
        text=f'📅 Расходы за прошлый месяц',
        callback_data='last_month_spending'
    ),
    'MAKE_MONTH_FILE': InlineKeyboardButton(
        text=f'📄 Отчёт в файл',
        callback_data='month_spending_to_file'
    ),
    'AVERAGE_CATEGORY_SPENDING': InlineKeyboardButton(
        text=f'📊 Средние траты по категориям',
        callback_data='average_category_spending'
    ),
    'BACK_TO_HEADPAGE': InlineKeyboardButton(
        text=f'🔙 Назад',
        callback_data='back_to_headpage'
    ),
}
