#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "0")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "0"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "0"))

REQUEST_CHANNEL1 = int(os.environ.get("REQUEST_CHANNEL1", "0"))
REQUEST_CHANNEL2 = int(os.environ.get("REQUEST_CHANNEL2", "0"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5090651635"))

#Port
PORT = os.environ.get("PORT", "8010")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "0")
DB_NAME = os.environ.get("DATABASE_NAME", "0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", ""))

HELP_TXT = "<b>Hi Dude!\nThis is an file to link bot work for <a href=https://t.me/Anime_Sub_Society>ᴀɴɪᴍᴇ sᴏᴄɪᴇᴛʏ</a>\n\n❏ Bot Cammands\n├/start : start the bot\n├/about : Our Information\n└/help : Help related Bot\n\n⚡ Simply click on link and start the bot join both channels and try again thats it.....!\n\n🧑‍💻 Developed by <a href=https://t.me/Its_Oreki_Hotarou>Hōᴛᴀʀō Oʀᴇᴋɪ</a></b>"
ABOUT_TXT = "<b>⟦<a href=https://t.me/Anime_Sub_Society>ᴀɴɪᴍᴇ sᴏᴄɪᴇᴛʏ</a>⟧ Hi There {first}!💫\n┏━━━━━━━❪❂❫━━━━━━━━\n⌬ ᴏᴡɴᴇʀ : <a href=https://t.me/rin_nanakura>ʀɪɴ</a>\n⌬ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Ongoing_society'>ᴏɴɢᴏɪɴɢ sᴏᴄɪᴇᴛʏ</a>\n⌬ ᴀɴɪᴍᴇ sᴏᴄɪᴇᴛʏ : <a href='https://t.me/anime_sub_society'>ᴀɴɪᴍᴇ sᴏᴄɪᴇᴛʏ</a>\n⌬ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://t.me/team_society_1'>ʙᴏᴛ sᴏᴄɪᴇᴛʏ</a>\n⌬ sᴏᴄɪᴇᴛʏ ᴄʜᴀᴛ ᴢᴏɴᴇ : <a href='https://t.me/ahss_help_zone'>ᴄʜᴀᴛ ᴢᴏɴᴇ</a>\n࿂ Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ : <a href='https://t.me/i_killed_my_clan'>❰⏤͟͞ 𝚯𝗕𝗜𝗧𝗢 -//-❱</a>\n┗━━━━━━━❪❂❫━━━━━━━━</b>"

START_PIC = os.environ.get("START_PIC", "https://envs.sh/W9M.jpg")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜɪ ᴛʜᴇʀᴇ... {first}! 👀\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\nᴘᴏᴡᴇʀᴇᴅ ʙʏ - <a href=https://t.me/Anime_Sub_Society>ᴀɴɪᴍᴇ sᴏᴄɪᴇᴛʏ</a></b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5090651635").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}!⚡\n\n🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "600"))
DEL_MSG = "<b>This File is deleting automatically in {time}. Forward in your Saved Messages..!</b>"

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ​ - @Anime_X_Hunters"

ADMINS.append(OWNER_ID)
ADMINS.append(5090651635)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
