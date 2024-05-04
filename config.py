import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

#❖ Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", None))
API_HASH = getenv("API_HASH", None)

#❖ Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME", "toxic_tanji")

#❖  Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME", "hina_lovely_bot")

#❖  Don't Add style font 
BOT_NAME = getenv("BOT_NAME", "HINA BABY")

#❖ get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME", "LOVELY_HINA")

#❖ Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

#❖ Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600000))

#❖  Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1001392902114"))

#❖ Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5195444280"))

#❖  Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

#❖  Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/haxkx/hina-baby-3.0",
)

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  #❖ Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/haxkx")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/haxkx_discussion")

#❖ Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


#❖ Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "e319091f771445b18c029299505d5d4f")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "293c334a2861415197a697b2d11dd4de")


#❖ Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 2500))


#❖ Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
#❖ Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


#❖ Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/93cf947713f49e9e4f99a.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/fe28e2fb73cdade0c8a10.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/6e59e4dbcb74fec678d10.jpg"
STATS_IMG_URL = "https://graph.org/file/1bfce7a64228c69e43802.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/3434af0772e3ed4e4f27c.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/18ba535b174ac0649b23b.jpg"
STREAM_IMG_URL = "https://graph.org/file/8bd25e1b5fffb97ea343e.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/1a4e7f09f968d9207a291.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/851a9a173ea0bbe740e4c.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/244e7569f41400dd0e024.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/709fdd164660d5add7b5f.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/49379e9fe323b923a2dc4.jpg"



def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
