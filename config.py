import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6134757239:AAEwejjgkvEN6qLwx8IlMiX7AkL8_VEnMtI")

    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", "15257211"))
    API_HASH = os.environ.get("API_HASH", "8b7cf73ce577720d74a213bbb98f4104")
    # Get these values from my.telegram.org

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1350212613").split())

    # Ban Unwanted Members..
    BANNED_USERS = []

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # Database url
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://AMMAAAAA:AMMAAAAA@cluster0.mi7ldio.mongodb.net/?retryWrites=true&w=majority")

    # Update channel for Force Subscribe, add bot as admin in the channel.
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "AM_FILMS")
