# (c) @RoyalDwip

import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", "23830477"))
    API_HASH = os.getenv("API_HASH", "19f8365d98fb11c9cd6c1eaa8b1fa4b8")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6185597348:AAHHDoRBg8PI9b2J_WQNoB5f_7CUFRLSGsg")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "Drm Downloader bot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", -1001912120311))
    BOT_USERNAME = os.getenv("BOT_USERNAME", "@drmdownloader111bot")
    BOT_OWNER = int(os.getenv("BOT_OWNER","1867884587"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG", '''**Hᴇʏ, {}! 😃

I Aᴍ A Sɪᴍᴘʟᴇ Mᴏᴠɪᴇ Sᴇᴀʀᴄʜ Bᴏᴛ. 😅

Yᴏᴜ Cᴀɴ Aᴅᴅ Mᴇ Oɴ Yᴏᴜʀ Gʀᴏᴜᴘ As Aᴅᴍɪɴ 🤪

Nᴏᴛᴇ - ɪ ᴄᴀɴ Pʀᴏᴠɪᴅᴇ Yᴏᴜʀ Mᴏᴠɪᴇs Lɪɴᴋs Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ 😜

Fᴏʀ ᴍᴏʀᴇ ɪɴғᴏ Cʟɪᴄᴋ Oɴ Hᴇʟᴘ. ✅**''')
    START_PHOTO = os.getenv("START_PHOTO")
    HOME_TEXT = os.getenv("HOME_TEXT", '''**Hᴇʏ,{}! 😃

I Aᴍ A Sɪᴍᴘʟᴇ Mᴏᴠɪᴇ Sᴇᴀʀᴄʜ Bᴏᴛ. 😅

Yᴏᴜ Cᴀɴ Aᴅᴅ Mᴇ Oɴ Yᴏᴜʀ Gʀᴏᴜᴘ As Aᴅᴍɪɴ 🤪

Nᴏᴛᴇ - ɪ ᴄᴀɴ Pʀᴏᴠɪᴅᴇ Yᴏᴜʀ Mᴏᴠɪᴇs Lɪɴᴋs Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ 😜

Fᴏʀ ᴍᴏʀᴇ ɪɴғᴏ Cʟɪᴄᴋ Oɴ Hᴇʟᴘ. ✅**''')
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "")
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Khrish:<12121212>@cluster1.hh7bbcz.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001834338888"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 5))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 300))
    MDISK_API = os.getenv("MDISK_API", "")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "30"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", '''Enter About Text''')
    ABOUT_HELP_TEXT = os.getenv("HELP_TEXT", '''Enter Help Text''')
