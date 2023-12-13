#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("22330771", default=None, cast=int)
API_HASH = config("5961c742f33534c68418694e08a776f7", default=None)
BOT_TOKEN = config("6787784929:AAE44K3JCBDbT2JPa7ONqLA7AvZVRQytnLw", default=None)
SESSION = config("BQCmRV-FqBnnDVRstZLrIZd41Eg5p0hYv2vKsfJz_Y8mOR35Q20_JHbyE6b1DNv3nJcRwzYMJIBCayV77n1Evg01LO-Uw7RbLit-bNXW5dsnF4-9eSFagAqoNdr0Sz5lc8y3XbkP0VjFY-TGJc7u2Zw2Ww6cuNGP5rslP02JZk71q1_Z0P7caN3nnABHJGVm1Gh-Vd9KjrMC2POj7-UdgOrAGZcGyKf5Mr-Ex8ZtPuWRX3Ai5SV0Z6uOuhhTr-UwFr9gs9Jpm5zp31ljiMks4FkFwK6gxj0YWfrXVdps1vYfxTERCePNsvHU8fOZ1uqvQDTQsskQcTVIIryFn8DYS-I1AAAAATaM_jsA", default=None)
FORCESUB = config("tiktokviralbarue", default=None)
AUTH = config("1281619082", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
