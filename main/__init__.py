#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 13225039
API_HASH = "43bb1945ef7fad8164b51647fb9428d1"
BOT_TOKEN = "6995997849:AAGUFLKkjRkTAvD1i8I1cwAc3BXuqEjWJK4"
SESSION = "BQAAxJIAIawhpymMWUUe-BJSFCJW_Ttlzjv4xNGSUAZD1BYe8dLYNyg12ZAaA8Hbrht4PA7dqxHRb-10TZdqIfz2IyVtEmZXZlkNABUz90PrCZ6q9oQH7MtTjHu9n412LHdlJnCHMilQUzblsQQH4whpwVdEpW36i0IcHuWHLOh-X54_WEKEnRYF3j0nS2jfHV0A2PtCI2lk8v7xsYK526YL8Hf96ROCcXPHYTYTnrWaF8qsAjqpODMZmxbifmKY5r6rHuehPh8JkTh5Mtk-6iOPSPveJhc_J19sfl1AW2Z5M6__IaHrNZlaTEc8cm1dh5xIBM2fBsk_G0rVkv-KDt8JNbhNSwAAAAA53jH2AA"
FORCESUB = "coverzio"
AUTH = 392836663

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
