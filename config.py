from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "23803580"))
API_HASH = getenv("API_HASH", "7d91da02949db09dc81df55532c93863")

BOT_TOKEN = getenv("BOT_TOKEN","7836141612:AAGyJrUcnbj2Qp8mWGQwUkYneZnqiSMcDgU")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://spicystring:Nothing0000@string.rsr5s28.mongodb.net/?retryWrites=true&w=majority&appName=String")

OWNER_ID = int(getenv("OWNER_ID", 7381712992))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/SpicyxNetwork")
