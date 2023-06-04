from pyrogram import filters

from settings.config import BOT_MANAGER_ID


async def func_bot_manager_filter(_, __, update):
    """
    Функция фильтрации апдейтов от аккаунта - управляющего ботом.
    """
    return update.from_user.id == BOT_MANAGER_ID


bot_manager_filter = filters.create(func_bot_manager_filter)
