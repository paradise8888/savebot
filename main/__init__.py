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
SESSION = config("BQCK6qGNMTOYX3aUyJaGn6QZPX739G21afoW14VXjEeDVOw1IGqIWTgpfvo5jfRSURN1B7HPSWviMSus6iNj3SvPclJkieBFLZVjZ-uiR2v-fzz4duVWaf4mWuXgOJJ6gQl3oUE0qQogAPR1O7EEcFk91ydebtWacAzcSPddWr7Or-lCsOJEM0wqEdk2hBWfE9Vaf3HBeioJsKIB3TQ2j4HUgwMhASe_fUmDY5hmUHbxucStyK6v1HkpQMzWVNlgDKmWoXtSEt5EpzIAmGntKXnyGOJoy8QxiwgNt7bbXhdAbDFN1YLcduMROE-azEmhp-mLtopUf7AMG39hSsUUcs0UAAAAATaM_jsA", default=None)
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
