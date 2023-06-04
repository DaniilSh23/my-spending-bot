from pyrogram import Client

api_id = 12659845
api_hash = '546ae7406a8f706a958882ae0fcc7108'

app = Client(
    "my_acc2",
    api_id=api_id, api_hash=api_hash,
)

app.run()
