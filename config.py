from os import getenv
from dotenv import load_dotenv
load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
LOG_ID = int(getenv("LOG_ID", "-1002139661881"))

MONGO_DB_URI = getenv("MONGO_DB_URI", None)
SUDO_USER = list(map(int, getenv("SUDO_USER", "6180225412").split()))
