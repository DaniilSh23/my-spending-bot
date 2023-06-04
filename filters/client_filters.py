from pyrogram import filters


async def func_listening_channel_filter(_, client, update):
    """
    Фильтрация апдейта из канала, который прослушивает аккаунт.
    """
    if update.forward_from_chat:
        return update.forward_from_chat.id == -1001871383245 and update.chat.id == -1001738908869


listening_channel_filter = filters.create(func_listening_channel_filter)