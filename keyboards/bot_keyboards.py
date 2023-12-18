from pyrogram.types import InlineKeyboardMarkup

from keyboards.bot_buttons import BUTTONS_DCT


ADMIN_KBRD = InlineKeyboardMarkup([
    [
        BUTTONS_DCT['ADMIN_PANEL']
    ],
])
HEADPAGE_RBRD = InlineKeyboardMarkup([
    [
        BUTTONS_DCT['WRITE_SPENDING'],
    ],
    [
        BUTTONS_DCT['DAY_SPENDING'],
    ],
    [
        BUTTONS_DCT['THIS_MONTH_SPENDING']
    ],
    [
        BUTTONS_DCT['AVERAGE_CATEGORY_SPENDING']
    ],
])
MAKE_MONTH_FILE_KBRD = InlineKeyboardMarkup([
    [
        BUTTONS_DCT['MAKE_MONTH_FILE'],
    ],
    [
        BUTTONS_DCT['BACK_TO_HEADPAGE'],
    ],
])

BACK_TO_HEADPAGE_KBRD = InlineKeyboardMarkup([
    [
        BUTTONS_DCT['BACK_TO_HEADPAGE'],
    ],
])