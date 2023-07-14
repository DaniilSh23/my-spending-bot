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


async def func_get_month_spending_filter(_, __, update: CallbackQuery):
    """
    Функция фильтра для колбэка получения трат за месяц
    """
    return update.data == 'this_month_spending'


async def func_filter_back_to_headpage(_, __, update: CallbackQuery):
    """
    Функция фильтра для колбэка возврата к главному меню
    """
    return update.data == 'back_to_headpage'


async def func_filter_make_month_file(_, __, update: CallbackQuery):
    """
    Функция фильтра для колбэка формирования файла-отчёта за месяц
    """
    return update.data == 'month_spending_to_file'


bot_manager_filter = filters.create(func_bot_manager_filter)
get_day_pending_filter = filters.create(func_get_day_pending)
get_month_spending_filter = filters.create(func_get_month_spending_filter)
filter_back_to_headpage = filters.create(func_filter_back_to_headpage)
filter_make_month_file = filters.create(func_filter_make_month_file)
