import asyncio
from loguru import logger
import uvloop
from pyrogram import Client
from pyrogram.raw import functions


async def invite_user():
    async with Client("test_bot") as client:

        # Получаем объекты InputPeer для юзера и канала
        user_input_obj = await client.resolve_peer(peer_id='DaniilSh23')
        chat_input_obj = await client.resolve_peer(peer_id=-1001738908869)

        # Инвайтим в группу
        await client.invoke(
            functions.channels.InviteToChannel(
                channel=chat_input_obj,
                users=[user_input_obj]
            )
        )


def client_work():
    """
    Такс в eventloop'e для одного клиента телеграм
    """
    plugins = dict(
        root="handlers",
        include=[
            "client_handlers",
        ]
    )
    uvloop.install()  # Это для ускорения работы бота
    Client("my_acc2", plugins=plugins).run()


if __name__ == '__main__':
    # asyncio.run(invite_user())
    client_work()

