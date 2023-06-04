from pyrogram.types import InlineKeyboardMarkup

from keyboards.bot_buttons import BUTTONS_DCT


ADMIN_KBRD = InlineKeyboardMarkup([
    [
        BUTTONS_DCT['ADMIN_PANEL']
    ],
])
WRITE_SPENDING_KBRD = InlineKeyboardMarkup([
    [
        BUTTONS_DCT['WRITE_SPENDING']
    ],
])

