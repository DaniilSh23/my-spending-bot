from pyrogram import filters
from pyrogram.types import CallbackQuery

from settings.config import BOT_MANAGER_ID


async def func_bot_manager_filter(_, __, update):
    """
    Функция фильтрации апдейтов от аккаунта - управляющего ботом.
    """
    return update.from_user.id == BOT_MANAGER_ID


async def func_get_day_pending(_, __, update: CallbackQuery):
    """
    Функция фильтра для колбэка получения трат за сегодня
    """
    return update.data == 'get_day_spending'


bot_manager_filter = filters.create(func_bot_manager_filter)
get_day_pending_filter = filters.create(func_get_day_pending)
