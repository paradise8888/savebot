#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 22330771
API_HASH = "5961c742f33534c68418694e08a776f7"
BOT_TOKEN = "6787784929:AAE44K3JCBDbT2JPa7ONqLA7AvZVRQytnLw"
SESSION = "BQFUvZMAIhkuloddVM3oS4B3nXJZK0mvVVvQXLsZ8iez6YvWz0mjvfcKATo4a-ccbFlFbSS4SPSw5l7TOBakRZ2EB9e-UgQlOaexKeJirAK5oBjMiqsRRsuxJTGeUVa5VDzGG7gZnKbRhSS6qdMp9K7lehfdcPIgFP9KlHayuVLelDQxXLNtk7iJIlDVTa3tbIsH2aosbt63xuVhsbISjVNU1SWuZEJnM7TPSYN3vuC0_TgA8YQOEiCBIE_RtWFqBnJuH4KFkmbpM8qKZqaZuro-KNRh0-kPskZVUp-djBn8o6pj8AYJ_n6v3YZuHkW8nUq5XtYjwkicr85tPiq-f2L8Fy2ecgAAAAGUlWDhAQ"
FORCESUB = "TiktokViralBarue"
AUTH = 1281619082

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
