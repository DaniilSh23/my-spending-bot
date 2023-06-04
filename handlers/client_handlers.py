import asyncio

from pyrogram import Client, filters
from pyrogram.errors import exceptions as pyro_except

from filters.client_filters import listening_channel_filter
from settings.config import MY_LOGGER


@Client.on_message(filters.group & listening_channel_filter)
async def listening_chat_handler(client, update):
    """
    Ловим апдейты от чатов, которые прослушиваем.
    """
    # Пишем коммент
    MY_LOGGER.debug(f'Пишем коммент к посту в канале')
    await update.reply_text(
        text=f'Коммент на пост: {update.text!r}'
    )


@Client.on_message()
async def all_updates(client, update):
    """
    Все апдейты
    """
    MY_LOGGER.success(f'Клиент {client.name!r} в работе. Получил апдейт.')
    MY_LOGGER.debug(update)



