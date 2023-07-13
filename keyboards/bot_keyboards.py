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
])

