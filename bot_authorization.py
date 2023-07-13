from pyrogram import Client

from settings.config import API_ID, API_HASH, TOKEN

app = Client(
    # "work_bot",
    'test_bot',
    api_id=API_ID, api_hash=API_HASH,
    bot_token=TOKEN
)

app.run()
