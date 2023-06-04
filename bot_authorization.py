from pyrogram import Client

api_id = 12659845
api_hash = '546ae7406a8f706a958882ae0fcc7108'
bot_token = '5265303938:AAHn68aqrQuDA9zThfUXFBQMX5hmgjqoTts'

app = Client(
    "test_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

app.run()
